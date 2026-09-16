"""Mock image execution pipeline for deterministic controller integration tests.

No paid API is required. Reference payloads are represented by bytes and are
verified against manifest SHA-256 values before execution.
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from typing import Dict, Iterable, Mapping, Optional, Tuple

from controller import Controller, ControllerError, EditContract, QAResult, ReferenceRole, Verdict


@dataclass(frozen=True)
class ManifestReference:
    reference_id: str
    path: str
    sha256: str
    source_class: str
    allowed: Tuple[str, ...]
    forbidden: Tuple[str, ...]
    authority_rank: int
    canonical: bool
    view: str
    version: str


class SusanReferenceManifest:
    def __init__(self, references: Mapping[str, ManifestReference]):
        self.references = dict(references)

    @classmethod
    def load(cls, path: Path) -> "SusanReferenceManifest":
        raw = json.loads(path.read_text(encoding="utf-8"))
        refs = {}
        for item in raw["references"]:
            r = ManifestReference(
                reference_id=item["reference_id"], path=item["path"], sha256=item["sha256"],
                source_class=item["source_class"], allowed=tuple(item["allowed"]),
                forbidden=tuple(item["forbidden"]), authority_rank=int(item["authority_rank"]),
                canonical=bool(item["canonical"]), view=item["view"], version=item["version"])
            if r.reference_id in refs:
                raise ControllerError(f"DUPLICATE_REFERENCE_ID: {r.reference_id}")
            refs[r.reference_id] = r
        return cls(refs)

    def register(self, controller: Controller, ids: Iterable[str]) -> None:
        for rid in ids:
            r = self.references.get(rid)
            if not r:
                raise ControllerError(f"MANIFEST_REFERENCE_MISSING: {rid}")
            controller.add_reference(ReferenceRole(r.reference_id, r.source_class, r.allowed,
                                                   r.forbidden, r.authority_rank, r.canonical))

    def resolve_payloads(self, root: Path, ids: Iterable[str]) -> Dict[str, bytes]:
        payloads = {}
        root = root.resolve()
        for rid in ids:
            r = self.references.get(rid)
            if not r:
                raise ControllerError(f"MANIFEST_REFERENCE_MISSING: {rid}")
            p = (root / r.path).resolve()
            if root not in p.parents and p != root:
                raise ControllerError(f"REFERENCE_PATH_ESCAPE: {rid}")
            if not p.is_file():
                raise ControllerError(f"REFERENCE_FILE_MISSING: {rid}")
            data = p.read_bytes()
            actual = sha256(data).hexdigest()
            if actual != r.sha256:
                raise ControllerError(f"REFERENCE_CHECKSUM_MISMATCH: {rid}")
            payloads[rid] = data
        return payloads


@dataclass(frozen=True)
class ExecutionPacket:
    fingerprint: str
    reference_ids: Tuple[str, ...]
    prompt: str
    current_edit_base: Optional[str]


@dataclass(frozen=True)
class ExecutionReceipt:
    executor: str
    fingerprint: str
    artifact_id: str
    transmitted_reference_ids: Tuple[str, ...]
    transmitted_reference_sha256: Mapping[str, str]
    prompt_sha256: str


class MockImageExecutor:
    """Deterministic stand-in for a real image backend.

    It proves which byte payloads crossed the execution boundary and can inject
    transport omissions or a deterministic artifact id for negative tests.
    """
    def __init__(self, drop_reference: Optional[str] = None):
        self.drop_reference = drop_reference

    def execute(self, packet: ExecutionPacket, payloads: Mapping[str, bytes]) -> ExecutionReceipt:
        transmitted = {k: v for k, v in payloads.items() if k != self.drop_reference}
        missing = set(packet.reference_ids) - set(transmitted)
        if missing:
            raise ControllerError(f"TRANSPORT_REFERENCE_MISSING: {sorted(missing)}")
        hashes = {k: sha256(v).hexdigest() for k, v in transmitted.items()}
        material = json.dumps({"fp": packet.fingerprint, "refs": hashes,
                               "prompt": packet.prompt, "base": packet.current_edit_base},
                              sort_keys=True).encode()
        artifact_id = "mock:" + sha256(material).hexdigest()[:24]
        return ExecutionReceipt("MockImageExecutor", packet.fingerprint, artifact_id,
                                tuple(sorted(transmitted)), hashes,
                                sha256(packet.prompt.encode()).hexdigest())


def run_mock_pipeline(controller: Controller, manifest: SusanReferenceManifest, root: Path,
                      reference_ids: Iterable[str], contract: EditContract, prompt: str,
                      qa: QAResult, hard_axes: Iterable[str],
                      executor: Optional[MockImageExecutor] = None) -> ExecutionReceipt:
    ids = tuple(reference_ids)
    manifest.register(controller, ids)
    payloads = manifest.resolve_payloads(root, ids)
    fp = controller.precommit_audit(contract, ids)
    packet = ExecutionPacket(fp, ids, prompt, controller.state.current_edit_base)
    receipt = (executor or MockImageExecutor()).execute(packet, payloads)
    # Receipt is evidence, not authority. Commit only after hard QA passes.
    controller.commit(receipt.artifact_id, fp, qa, hard_axes)
    return receipt
