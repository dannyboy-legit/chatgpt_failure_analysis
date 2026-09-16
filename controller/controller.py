"""Deterministic controller prototype derived from MASTER_DIAGNOSIS.md.

This module does not call an LLM or image generator. It enforces the state,
authority, provenance, retry, QA, and transactional rules around such calls.
"""
from __future__ import annotations
from dataclasses import dataclass, field, replace
from enum import Enum
from hashlib import sha256
import json
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple


class Status(str, Enum):
    ACTIVE = "active"
    OVERRIDDEN = "overridden"
    REJECTED = "rejected"
    HISTORICAL = "historical_only"


class Verdict(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    UNVERIFIABLE = "unverifiable"


@dataclass(frozen=True)
class Constraint:
    constraint_id: str
    value: Any
    source_id: str
    source_class: str
    authority_rank: int
    scope: str
    hard: bool = True
    observable_predicate: str = ""
    status: Status = Status.ACTIVE
    valid_from: Optional[str] = None
    valid_until: Optional[str] = None
    supersedes: Tuple[str, ...] = ()

    def canonical(self) -> Dict[str, Any]:
        d = dict(self.__dict__)
        d["status"] = self.status.value
        d["supersedes"] = list(self.supersedes)
        return d


@dataclass(frozen=True)
class ReferenceRole:
    reference_id: str
    source_class: str
    allowed: Tuple[str, ...]
    forbidden: Tuple[str, ...]
    authority_rank: int
    canonical: bool = False


@dataclass
class EditContract:
    must_change: Set[str] = field(default_factory=set)
    must_not_change: Set[str] = field(default_factory=set)
    recompute_from_canonical: Set[str] = field(default_factory=set)


@dataclass
class QAResult:
    verdicts: Dict[str, Verdict]
    evidence: Dict[str, str] = field(default_factory=dict)
    soft_scores: Dict[str, float] = field(default_factory=dict)

    @property
    def accepted(self) -> bool:
        return bool(self.verdicts) and all(v is Verdict.PASS for v in self.verdicts.values())


@dataclass
class ControllerState:
    constraints: Dict[str, Constraint] = field(default_factory=dict)
    references: Dict[str, ReferenceRole] = field(default_factory=dict)
    current_edit_base: Optional[str] = None
    clean_ancestor: Optional[str] = None
    rejected_fingerprints: Set[str] = field(default_factory=set)
    audit: List[str] = field(default_factory=list)


class ControllerError(RuntimeError):
    pass


class Controller:
    """Fail-closed controller for compiling and committing execution state."""

    def __init__(self, state: Optional[ControllerState] = None):
        self.state = state or ControllerState()

    def add_constraint(self, c: Constraint) -> None:
        # Explicit supersession first.
        for old_id in c.supersedes:
            old = self.state.constraints.get(old_id)
            if old:
                self.state.constraints[old_id] = replace(old, status=Status.OVERRIDDEN)
        old = self.state.constraints.get(c.constraint_id)
        if old and old.status is Status.ACTIVE:
            if c.authority_rank < old.authority_rank:
                raise ControllerError(
                    f"AUTHORITY_REBINDING: {c.source_id} rank {c.authority_rank} "
                    f"cannot replace {old.source_id} rank {old.authority_rank} for {c.constraint_id}"
                )
            if c.authority_rank == old.authority_rank and c.source_id != old.source_id and c.value != old.value:
                raise ControllerError(f"AUTHORITY_CONFLICT: {c.constraint_id}")
        self.state.constraints[c.constraint_id] = c

    def add_reference(self, r: ReferenceRole) -> None:
        if set(r.allowed) & set(r.forbidden):
            raise ControllerError(f"REFERENCE_ROLE_CONFLICT: {r.reference_id}")
        self.state.references[r.reference_id] = r

    def active_constraints(self) -> Dict[str, Constraint]:
        return {k: v for k, v in self.state.constraints.items() if v.status is Status.ACTIVE}

    def normalize(self) -> List[Constraint]:
        """Return deterministic active-only state; history never enters execution."""
        return sorted(self.active_constraints().values(), key=lambda c: (c.scope, c.constraint_id))

    def validate_source_to_ir(self) -> None:
        for c in self.normalize():
            if not c.source_id or not c.source_class:
                raise ControllerError(f"MISSING_PROVENANCE: {c.constraint_id}")
            if c.hard and not c.observable_predicate:
                raise ControllerError(f"MISSING_OBSERVABLE: {c.constraint_id}")

    def validate_reference_roles(self) -> None:
        # Canonical identity/physique references must not donate scene variables.
        scene_attrs = {"pose", "camera", "wardrobe", "environment", "expression", "lighting"}
        for r in self.state.references.values():
            if r.canonical and set(r.allowed) & scene_attrs:
                raise ControllerError(f"REFERENCE_CONTAMINATION_RISK: {r.reference_id}")

    def precommit_audit(self, contract: EditContract, required_references: Iterable[str]) -> str:
        self.validate_source_to_ir()
        self.validate_reference_roles()
        missing = sorted(set(required_references) - set(self.state.references))
        if missing:
            raise ControllerError(f"MISSING_REFERENCE: {', '.join(missing)}")
        overlap = contract.must_change & contract.must_not_change
        if overlap:
            raise ControllerError(f"EDIT_CONTRACT_CONFLICT: {sorted(overlap)}")
        packet = {
            "constraints": [c.canonical() for c in self.normalize()],
            "references": [self.state.references[k].__dict__ for k in sorted(self.state.references)],
            "base": self.state.current_edit_base,
            "must_change": sorted(contract.must_change),
            "must_not_change": sorted(contract.must_not_change),
            "recompute": sorted(contract.recompute_from_canonical),
        }
        fp = sha256(json.dumps(packet, sort_keys=True, default=list).encode()).hexdigest()
        if fp in self.state.rejected_fingerprints:
            raise ControllerError("REJECTED_ROUTE_REUSE")
        self.state.audit.append(f"PRECOMMIT {fp}")
        return fp

    def reject(self, fingerprint: str, reason: str) -> None:
        self.state.rejected_fingerprints.add(fingerprint)
        self.state.audit.append(f"ROLLBACK {fingerprint} {reason}")

    def verify_artifact(self, qa: QAResult, hard_constraint_ids: Iterable[str]) -> bool:
        required = set(hard_constraint_ids)
        missing = required - set(qa.verdicts)
        if missing:
            raise ControllerError(f"QA_MISSING_AXES: {sorted(missing)}")
        # UNVERIFIABLE is deliberately not PASS.
        return all(qa.verdicts[c] is Verdict.PASS for c in required)

    def commit(self, artifact_id: str, fingerprint: str, qa: QAResult, hard_constraint_ids: Iterable[str]) -> None:
        if fingerprint in self.state.rejected_fingerprints:
            raise ControllerError("CANNOT_COMMIT_REJECTED_ROUTE")
        if not self.verify_artifact(qa, hard_constraint_ids):
            self.reject(fingerprint, "artifact QA failed or unverifiable")
            raise ControllerError("TRANSACTION_ABORTED")
        if self.state.clean_ancestor is None:
            self.state.clean_ancestor = artifact_id
        self.state.current_edit_base = artifact_id
        self.state.audit.append(f"COMMIT {fingerprint} {artifact_id}")


def susan_reference_roles(face_ref: str, physique_ref: str) -> List[ReferenceRole]:
    """Canonical role split from the current master diagnosis."""
    return [
        ReferenceRole(face_ref, "canonical_face", ("facial_geometry",),
                      ("pose", "physique", "wardrobe", "environment", "expression", "lighting", "camera"), 100, True),
        ReferenceRole(physique_ref, "canonical_physique", ("anatomy", "silhouette"),
                      ("facial_geometry", "pose", "wardrobe", "environment", "expression", "lighting", "camera"), 100, True),
    ]
