# Iterative research pass — 2026-09-15T19:16Z

## New findings

### 1. Preservation and requested change must be evaluated as a coupled objective, not independent scores
Evidence grade: B/C.

PIE-Bench established mask-aware evaluation separating structure/background preservation (DINO self-similarity, PSNR, LPIPS, MSE, SSIM outside the edit mask) from edit fidelity. CompBench similarly decouples foreground instruction adherence from background preservation. GEditBench v2 identifies an under-editing trap: systems can score well on visual consistency by simply failing to perform the requested change. RC-GRPO-Editing (2026 preprint) reaches the same problem from training: global exploration perturbs non-target regions and noisy global rewards confound credit assignment, so it constrains exploration to the edit region and separately rewards attention concentration.

Implication: Susan QA cannot use preservation alone. A local edit passes only when BOTH requested-region change succeeds and protected-region change remains under threshold. Define a two-sided DELTA_CONTRACT: MUST_CHANGE region/attributes + MUST_NOT_CHANGE region/attributes. Reject under-editing and over-editing separately.

### 2. The project documents already imply a delta contract
Evidence grade: A.

Locked Project Rules explicitly say an existing-image edit preserves identity, physique, camera placement, lighting, environment, scale relationships, clothing and composition, and modifies only requested elements. Susan v5 separately assigns face identity, physique, scale, and pose/camera authorities. The Documentary Cinematography Bible makes the event and observer/camera behavior part of the realism target, while the Realism Bible requires stable environment/camera in transformation sequences and environmental scale anchors.

Thus the correct representation is not merely an attribute checklist. It is a typed state diff against an accepted base: each attribute/region is CHANGE, PRESERVE, or RECOMPUTE_FROM_CANONICAL_ANCHOR.

### 3. Some apparent preservation can be false success
Evidence grade: B/C.

GEditBench v2's under-editing trap is important counterevidence to the assumption that lower image drift always means better editing. Exact preservation metrics can reward doing nothing. Conversely, global semantic metrics can tolerate local spillover. This requires Pareto-style or gated evaluation rather than one aggregate score.

Controller change: hard gate requested edit completion first; then hard/graded preservation checks. Never let high preservation compensate for a missed edit, and never let successful edit semantics compensate for protected-region drift.

### 4. Constraint drift should be modeled across transformations of state, not just across conversational turns
Evidence grade: C (position/preprint evidence, not proof of ChatGPT internals).

Constraint State Governance (2026 preprint) frames constraint drift as loss/distortion as constraints pass through memory, delegation, communication, tools, audit, and optimization. This generalizes our existing authority-DAG idea: every transition that transforms state needs an invariant check. For this project those boundaries are chat→compiled state, compiled state→tool handoff, tool output→QA, QA→accepted base, and accepted base→next-turn state.

Controller change: attach invariant hashes/IDs to hard constraints and verify survival at every boundary. A constraint disappearing during compilation is distinguishable from a generator violating a correctly transported constraint.

### 5. Tool-environment unreliability should be treated separately from reasoning failure
Evidence grade: C/B depending final publication status.

ToolBench-X (2026 preprint) explicitly injects specification drift, invocation error, execution failure, output drift and cross-source conflict while keeping recovery paths available. ToolMisuseBench similarly separates invalid calls, interface drift, recovery quality and retry budgets. This strengthens a distinction already visible in this repository: a good plan can still fail because the tool contract or returned state differs from expectation.

Controller change: classify every failure as STATE_COMPILE, TOOL_CONTRACT, TOOL_TRANSPORT, TOOL_EXECUTION, OUTPUT_DRIFT, ARTIFACT_CONSTRAINT, or QA/JUDGE. Retry policy depends on class; do not rewrite the image prompt for a transport or tool-contract failure.

## Weakened/rejected hypotheses

- "Less visual change is always better for an edit" — rejected. Under-editing can game preservation metrics.
- "One aggregate edit-quality score can balance fidelity and preservation" — weakened. Evidence favors decoupled/gated foreground-vs-background or change-vs-preserve evaluation.
- "Constraint drift is primarily a long-context phenomenon" — weakened. The broader state-governance literature suggests drift can occur at any representation/tool boundary even with short contexts.
- "A failed tool action necessarily indicates a planning failure" — rejected as a general assumption; environment/contract/output hazards require separate diagnosis.

## Concrete controller additions

1. DELTA_CONTRACT = {MUST_CHANGE, MUST_NOT_CHANGE, RECOMPUTE_FROM_CANONICAL}.
2. Mask/region-aware preservation metrics where geometry permits: SSIM/LPIPS/PSNR or feature similarity outside edit region; semantic/geometry checks inside target region.
3. Anti-under-edit gate: requested change must be measurably present before preservation score is considered.
4. Boundary invariant checks at CHAT→STATE→TOOL→OUTPUT→QA→COMMIT.
5. Failure taxonomy that separates reasoning/state compilation from tool/environment hazards.
6. Preserve camera/environment not merely as prose but as base-relative geometry/feature checks when editing.

## Automation evidence

Repository read/write access worked in this pass. No repository-write blockage occurred. Direct web discovery remains necessary because SOURCE_COVERAGE records prior arXiv collector throttling/timeouts; no claim is made that the collector corpus is complete.

## Still unchecked / next high-value work

- Read original PIE-Bench/Direct Inversion and GEditBench v2 papers in full, especially metric failure analyses and human-correlation results.
- Determine whether current image-generation tooling exposes masks/regions or whether QA must infer them from the instruction/base image.
- Find robust face/identity metrics under extreme viewpoint, occlusion, scale and expression changes; quantify failure of ordinary face embeddings there.
- Test single nearest-angle Susan face reference against multi-view references under identical scene requests.
- Build an executable state compiler and compare its outputs under cousin prompts, overrides, rollbacks and local edits.
- Inspect current Images 2.5 community reports for claimed multi-turn preservation improvements versus regressions, treating them only as community evidence.