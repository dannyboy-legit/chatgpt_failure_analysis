# Master Diagnosis

Updated: 2026-09-15T22:19Z

This document consolidates the scheduled research sequence. It separates direct project/runtime evidence from external research and does not claim access to private model internals.

## Executive diagnosis

The dominant failure is not missing instructions. The project already contains unusually explicit rules for identity, physique, scale, camera, realism, continuity and editing. The failure is the unreliable conversion of those sources into a small, current, provenance-correct execution state; reliable transport of that state and its visual references into tools; correct cross-modal binding into pixels; and artifact-level verification before state is committed.

A reliable workflow therefore needs a controller, not more prose: source/version authority → active-state compilation → reference-role disentanglement → pre-commit validation → verified tool transport → generation/edit → constraint-vector QA → transactional commit/rollback → trajectory-health monitoring.

## 1. Highest-confidence mechanisms

### A. Source authority is documented but not enforced — HIGH
Susan v5 explicitly separates Facial Identity, Physique and Scale; canonical visual references outrank prose for their governed attributes; nearest-angle face/physique references are selected rather than averaged; pose/camera do not redefine identity or physique. Project Continuity Rules say an edit preserves identity, physique, clothing, camera/framing, lighting/mood, environment, scale relationships and composition unless specifically changed. Observed failures repeatedly knew these rules yet acted without enforcing them.

### B. Source-version conflict is real inside the project corpus — HIGH, direct evidence
The Library contains contradictory Susan rules. Current Susan v5 says changing height changes absolute size only and does not alter anatomical proportions. The older Dynamic Scale Addendum says growth proportionally develops shoulders/legs/musculature and still names older Chloe-based face references. Therefore broad semantic retrieval can return stale but relevant rules that conflict with current canon. A version/supersession gate is mandatory.

### C. Declarative recall and behavioral adherence dissociate — HIGH
The conversation repeatedly contains correct restatements immediately after violations. DriftBench independently reports a knows-but-violates phenomenon. Asking whether the model understands a rule is not a control.

### D. Multi-turn path dependence and evolving state are distinct from raw context length — HIGH
Research on long/multi-turn interaction shows early assumptions and sequential constraints can degrade reliability even when information remains available. StateMemBench-style evidence supports explicit supersession/current-state representation. A chronological summary can faithfully preserve a wrong branch. Failed and overridden branches must be excluded from active execution state while remaining in audit history.

### E. Long context and redundant constraints remain risk multipliers — HIGH general; MEDIUM per individual failure
AgentIF, Lost in the Middle, LIFBench, Context Rot and related work show nominal context capacity does not imply uniform effective use. Constraint-heavy contexts are fragile. Additional redundant reminders can also interfere. The execution packet should be compact, normalized and active-only.

### F. Visual grounding can decay during long reasoning — HIGH general multimodal evidence
ACL 2026 Look Light, Think Heavy and Visually-Guided Policy Optimization show that extended multimodal reasoning can reduce visual grounding/attention; Remember-R1 and related work target the same failure. Therefore reference inspection should be re-grounded late, close to generation and QA. More reasoning is not automatically safer for perception-heavy gates.

### G. Identity preservation and scene variation are separate objectives — HIGH
WithAnyone and related identity-conditioning work identify copy-paste/reference leakage: preserving identity can wrongly preserve pose/expression/lighting/presentation. Susan's own Bible already says identity is invariant to pose, hairstyle, lighting and expression. Canonical face pixels define who Susan is, not the whole photograph.

### H. Multi-reference conditioning needs explicit role separation — HIGH
TRACE-Bench, MultiRef, generalized multi-image editing and related work show reference binding/disentanglement is difficult. Each reference needs allowed and forbidden contributions. Face reference: facial geometry only. Physique reference: anatomy/silhouette only. Pose reference: pose/camera only. Scene request: expression/gaze/hair/clothing/environment/etc. where not otherwise locked.

### I. Correct symbolic state does not guarantee correct visual binding — HIGH as architecture principle
Cross-modal research shows that text planning quality and image-generation capability do not ensure correct reciprocal grounding. Constraints need observable visual predicates and artifact evidence must map back to the same constraint IDs. This is CROSS_MODAL_CLOSURE.

### J. Reference availability is not proof of reference transport — MEDIUM-HIGH tool-path risk
Public implementation reports document cases where reference files exist in context but are not actually delivered to image generation. These reports do not prove the exact ChatGPT runtime mechanism, but they establish transport as a separate precondition. Required reference pixels must be verified as actual tool inputs; filenames/descriptions are insufficient.

### K. Iterative editing accumulates drift — HIGH
FreqEdit, AnchorEdit, MT-EditFlow and related work show sequential edits can progressively degrade identity/detail and propagate errors. The latest accepted image cannot replace immutable canonical identity/physique anchors. Track cumulative trajectory health and rebase from a clean ancestor when thresholds are crossed.

### L. Preservation is a two-sided edit contract — HIGH
PIE-Bench/CompBench/GEditBench-style evaluation separates edit success from untouched-region preservation. Over-editing and under-editing are both failures. The contract is MUST_CHANGE + MUST_NOT_CHANGE + RECOMPUTE_FROM_CANONICAL.

### M. Protected semantic state is not raw pixel invariance — HIGH, direct project evidence
The updated Documentary Cinematography Bible's re-capture layer says identity/core anatomy stay stable while skin reflectivity, highlights, tonal response, atmosphere, exposure and camera imperfections legitimately vary with environmental capture. QA must distinguish geometric/semantic invariants from photometric covariates. For a local edit, lighting/mood remain semantically stable unless requested, but physically plausible sensor-level variation is not automatically drift.

### N. Self-critique and generic judges are insufficient — HIGH
The TACL self-correction survey weakens intrinsic self-correction as a reliability mechanism. MCJudge/AgentProp-style evidence shows automated judges can miss partial failures and simple heuristic judges can be extremely unreliable. Use per-constraint QA with deterministic checks where possible; semantic judges require calibration/stability checks.

### O. Rejection and recovery are different capabilities — MEDIUM-HIGH
AgentProp-Bench reports parameter-level errors frequently propagate and that rejection of corrupted inputs and recovery after accepting them are statistically independent. Measure PRE_COMMIT_REJECTION and POST_FAILURE_RECOVERY separately.

### P. Retry loops require structural invalidation — HIGH
Repeated failed routes should be fingerprinted and invalidated. Local malformed-argument errors permit local repair; wrong reference authority, wrong edit base, missing required pixels, stale state or recurring identity route invalidate the whole plan. Runtime enforcement is stronger than reminders.

### Q. State mutation must be transactional — HIGH architecture principle
Tool/artifact results are provisional until verified. `current_edit_base`, reference availability, workflow health and accepted character state mutate only after hard gates pass. Ambiguity/failure rolls back. This prevents an incorrect intermediate result from becoming new truth.

### R. Constraint provenance must survive every boundary — HIGH architecture principle
Every compiled field needs source_id, source class, authority rank, scope, validity/supersession status and observable predicate. Generated descendants, QA outputs and historical retrieval are evidence, not authority. Silent migration of authority from canonical Susan references to generated descendants is AUTHORITY_REBINDING.

## 2. Weakened/rejected explanations

- Instructions were missing — rejected for core Susan failures.
- More prose reminders will solve it — strongly weakened.
- Bigger context alone solves continuity — rejected.
- All relevant project documents can safely be retrieved together — rejected by direct version conflict.
- If a file is visible/named, generation necessarily receives its pixels — rejected as an assumption.
- More reasoning is always safer — rejected for perception-heavy multimodal gates.
- One successful image proves reliability — rejected; use repeated varied trials/reliable@k/pass^k.
- Latest accepted image can become the sole identity source — rejected; canonical anchor remains immutable.
- Pixel sameness is the correct preservation metric — rejected; use typed semantic/geometric vs photometric invariance.
- One holistic visual judge is sufficient — rejected/strongly weakened.
- Good pre-action rejection implies good post-fault recovery — rejected.
- Formalizing rules automatically solves the problem — weakened; source→IR translation can itself be wrong and must be validated.

## 3. Consolidated controller

### Stage 0 — Source/version gate
Inventory candidate sources. Mark canonical, superseded, historical-only. Resolve contradictions before compilation. Current source authority beats stale semantically similar documents.

### Stage 1 — Provenance IR
For every constraint record:
`constraint_id | value | source_id | source_class | authority_rank | scope | valid_from | valid_until | supersedes | hard/soft | observable_predicate`.

### Stage 2 — Active-state compiler
Classify turn: new scene / refinement / local edit / override / rollback / continuation / critique-only. Rebuild from persistent + active constraints after rollback/material override. Do not carry rejected branch state into generation.

### Stage 3 — Authority DAG / reference roles
Susan face: nearest-angle canonical face → facial geometry only.
Susan physique: nearest-angle canonical physique → anatomy/silhouette only.
Pose reference: joint/body/camera geometry only.
Accepted base: current composition/environment/camera for edits.
Scene instruction: requested delta and scene variables.
Explicitly encode forbidden contributions from each reference.

### Stage 4 — Typed edit contract
`MUST_CHANGE`, `MUST_NOT_CHANGE`, `RECOMPUTE_FROM_CANONICAL`.
Split invariants into semantic/geometric locks and legitimate photometric covariates.

### Stage 5 — Perception/reference gate
Directly inspect/re-ground required canonical pixels close to action. Keep visual verification concise; do not replace it with long textual reconstruction. If identity is too small/occluded for reliable judgment, return UNVERIFIABLE rather than PASS.

### Stage 6 — Tool/transport preconditions
Verify required reference pixels are actual visual inputs; verify current edit base; verify requested tool capability. Fail closed if a hard prerequisite is missing.

### Stage 7 — Pre-commit audit
Check source versions, authority conflicts, required references, edit delta, protected invariants, geometry anchors, retry fingerprint and tool contract before execution.

### Stage 8 — Execute once
Record fingerprint of active state + references + roles + camera + scale + delta. Do not repeat a failed fingerprint unchanged.

### Stage 9 — Constraint-vector artifact QA
Hard axes: identity, physique, requested edit presence, protected-region/semantic preservation, camera/geometry lock, scale anchors, required reference-specific attributes.
Soft axes: photographic/material realism, naturalness, capture imperfections where appropriate.
No average score may compensate for a hard FAIL. UNVERIFIABLE is distinct from PASS.

### Stage 10 — Cross-modal closure
For every hard constraint, require observable visual evidence tied back to its constraint ID. A sentence in the prompt is not proof of pixel-level satisfaction.

### Stage 11 — Transactional commit/rollback
Only a fully accepted artifact becomes current_edit_base. Failed/ambiguous artifacts remain diagnostic evidence only.

### Stage 12 — Trajectory health
Track cumulative identity drift from canonical anchor, protected-scene drift from clean ancestor, camera/scale-anchor displacement and material/detail degradation. Rebase when thresholds are exceeded.

## 4. Reliability tests

1. Cousin prompts must compile to the same normalized state.
2. Stale-source negative control: v5 + Dynamic Scale Addendum must resolve to v5, not merge contradictions.
3. Pose-reference contamination control: different person's pose image must not acquire identity/physique authority.
4. Single nearest-angle face reference vs multi-view reference test.
5. End-to-end reference transport marker/control.
6. Compact active state vs raw long thread.
7. Fresh active-only recompilation vs accumulated packet after rollback.
8. Recursive edit vs clean-ancestor rebase + canonical anchor.
9. MUST_CHANGE anti-under-edit and MUST_NOT_CHANGE anti-over-edit gates.
10. Short direct visual grounding vs extended CoT for identity/reference verification.
11. Separate rejection and recovery fault-injection tests.
12. pass^k/reliable@k across materially varied Susan scenes.

## 5. Evidence grading

A — direct project/runtime evidence: Susan v5/v4.3, Dynamic Scale Addendum contradiction, Documentary Cinematography UPDATED v2, Realism/Continuity rules, observed conversation/tool failures.

B — peer-reviewed/primary scientific evidence: AgentIF; ACL/EMNLP long-context and multimodal-grounding papers; tau-bench; CAR-bench; WithAnyone; TRACE-Bench; FreqEdit; PIE-Bench family; instruction-hierarchy/verification work.

C — primary preprints/implementation evidence: AgentProp-Bench; newer identity/editing benchmarks; public implementation issue reports. These support mechanisms but do not prove private ChatGPT internals.

D/E — community/secondary sources: discovery/support only, never promoted alone.

## 6. Research-process findings

The deterministic collector did produce source_queue artifacts; an earlier claim that it was absent was caused by inspecting the wrong directory and was retracted. Some collector passes encountered arXiv timeouts/HTTP 429s, so automated academic discovery was incomplete and direct search remained necessary. Repository reads/writes succeeded throughout later passes.

## 7. Remaining work

- Locate/reconcile standalone Anatomy Addendum and Simplified Rules if stored under non-obvious names.
- Inspect canonical Susan visual reference assets directly and run nearest-angle vs multi-view tests.
- Implement the source-to-IR compiler and run stale-source/authority-rebinding negative controls.
- Establish geometry/semantic edit-locality metrics tolerant of legitimate photometric recapture.
- Build a repeatable Susan reliability benchmark across scene, pose, expression, lighting and scale variation.
- Validate preprint-only mechanisms as peer-reviewed evidence becomes available.

## Bottom line

The accumulated evidence increasingly rejects an instruction-writing diagnosis. The project already specified the intended behavior. Reliability depends on enforcing current source authority, preserving provenance, keeping canonical visual anchors alive, separating semantic invariants from scene/photometric variation, verifying transport and cross-modal binding, rejecting bad plans before execution, and preventing failed artifacts from mutating future state.