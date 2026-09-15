# ChatGPT Research Pass — 2026-09-15T1816Z

## New findings

### 1. Reliability must be tested over semantically equivalent requests, not only repeated identical trials
**Evidence grade: B (peer-reviewed ACL 2026).**

Dong et al., *Revisiting the Reliability of Language Models in Instruction-Following* (ACL 2026), introduce IFEval++ and reliable@k to measure consistency across 'cousin prompts' expressing analogous intent with nuanced wording. Across 46 models, performance can drop by up to 61.8% under nuanced prompt modifications.

**Implication for this project:** pass^k on an identical Susan prompt is necessary but insufficient. The workflow can overfit to one wording. Add a semantic-equivalence reliability test: preserve the same authority graph and image contract while varying natural-language phrasing, ordering, and conversational framing. A reliable controller should compile these cousin prompts into the same normalized action state.

### 2. Verification should happen before committing action/state, not only after an artifact exists
**Evidence grade: B (peer-reviewed ACL 2026).**

Yuan et al., *Verify Before You Commit* (ACL 2026), perform adversarial self-auditing to localize violations and apply constraint-guided minimal interventions under verifiable acceptance criteria before commitment. This provides stronger support for a PRE-COMMIT audit stage than the existing post-generation QA-only framing.

**Implication:** before image_gen/tool execution, audit the compiled action against the authority DAG and hard constraints. After execution, artifact QA remains separate. Pre-commit verification catches plan/reference-role errors that artifact QA would discover only after spending a generation.

### 3. Tool results should not mutate symbolic state until execution is verified
**Evidence grade: B (peer-reviewed Findings ACL 2026).**

Liu et al., *ToolGate: Contract-Grounded and Verified Tool Execution for LLMs*, explicitly guarantees symbolic state evolves only through verified tool executions, preventing invalid/hallucinated tool results from corrupting world state.

**Implication:** the controller needs transactional state semantics. A generation/tool attempt occurs in a provisional state. Only a verified successful result can COMMIT changes such as `current_edit_base`, repository status, or capability state. Failed/ambiguous calls ROLLBACK. This directly addresses the observed pattern where an assumption or failed branch contaminated later state.

### 4. Identity preservation is multi-scale; face fidelity alone is an incomplete identity gate
**Evidence grade: C (2026 primary preprint; direct empirical claim, peer review not established in this pass).**

Xiao et al., *Beyond Facial Consistency: Personalized Person Image Generation with Holistic Identity Preservation* (arXiv 2607.25622), identify a tradeoff between local facial fidelity and global appearance consistency. Their dual-branch baseline is unstable without dynamic balancing; region-aware optimization coordinates facial, appearance, and global supervision.

**Implication for Susan:** the existing separate face and physique authorities are directionally correct, but QA should not treat them as independent scores that can both narrowly pass while their integration is globally wrong. Add a `HOLISTIC_CHARACTER_COHERENCE` check spanning face-to-body proportions, hair/head/body integration, and overall recurring-person appearance. This is a soft/semantic check subordinate to the hard face/physique anchors, not a replacement for them.

### 5. Multiple reference subjects/features can interfere at representation level; explicit correspondence is a plausible mitigation
**Evidence grade: C (2025 primary preprint).**

MOSAIC (She et al., arXiv 2509.01977) attributes multi-subject failures to identity blending and attribute leakage and uses semantic correspondence plus orthogonal feature disentanglement to keep reference contributions separated.

**Implication:** strengthen the existing `allowed_from_reference` map into an explicit correspondence map: each reference has permitted target regions/attributes and forbidden regions/attributes. This is especially relevant when face and physique references coexist. This supports, but does not prove for ChatGPT Images, the hypothesis that role declarations should be spatial/attribute-specific rather than generic prose.

## Weakened / falsified hypotheses

- **'Repeated identical success is enough to establish reliability.'** Weakened further. IFEval++ shows substantial reliability loss across semantically equivalent cousin prompts. Reliability testing must include wording/context perturbation.
- **'Post-generation QA is the first meaningful verification point.'** Rejected. Peer-reviewed evidence supports verification before commitment; plan-level errors can be caught before tool execution.
- **'A successful tool return may immediately update working state.'** Rejected as a safe controller assumption. ToolGate supports commit-only-after-verification transactional semantics.
- **'Face identity + physique identity scores fully characterize recurring-person identity.'** Weakened. Holistic identity work indicates coordination between local facial and global appearance signals is itself a failure surface.

## Controller changes

Add:

1. `SEMANTIC_EQUIVALENCE_COMPILER_TEST`: cousin prompts with the same intent must compile to the same normalized state.
2. `PRE_COMMIT_AUDIT`: verify authority selection, active constraints, reference roles/transport proof, edit base, camera/scale state, and retry fingerprint before tool invocation.
3. `TRANSACTIONAL_STATE`: tool/generation attempts write only to provisional state; COMMIT only after verified success; otherwise ROLLBACK.
4. `REFERENCE_CORRESPONDENCE_MAP`: explicit reference -> allowed attributes/regions and forbidden attributes/regions.
5. `HOLISTIC_CHARACTER_COHERENCE`: soft semantic QA after hard face/physique checks to catch locally correct but globally incoherent identity integration.
6. Extend reliability benchmark from `pass^k` to `reliable@k`-style cousin-prompt trials plus varied-scene trials.

## Project-source comparison

Susan Character Bible v5 already establishes the architectural premise needed for these controls: canonical face references outrank prose for facial anatomy; physique references separately govern body anatomy/silhouette; scene-specific instructions govern other variables; and compromises preserve facial identity before physique, scale, pose, clothing and environment. The new research does not show that more Susan prose is needed. It strengthens the case that those existing authority rules must be compiled, pre-audited, transactionally executed, and independently verified.

## Automation/repository evidence

`runs/` contained research passes through 17:18Z when inspected. This 18:16Z pass was therefore not duplicating an already committed hourly analysis. Repository read/write access is functioning in this run.

## Sources newly checked

- Dong et al., *Revisiting the Reliability of Language Models in Instruction-Following*, ACL 2026, DOI 10.18653/v1/2026.acl-long.354.
- Yuan et al., *Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing*, ACL 2026, DOI 10.18653/v1/2026.acl-long.1440.
- Liu et al., *ToolGate: Contract-Grounded and Verified Tool Execution for LLMs*, Findings ACL 2026, DOI 10.18653/v1/2026.findings-acl.470.
- Wen et al., *IF-CRITIC*, ACL 2026 (newly surfaced as corroboration for constraint-decomposed verification; already present in coverage ledger, so not counted as a new category).
- Xiao et al., *Beyond Facial Consistency: Personalized Person Image Generation with Holistic Identity Preservation*, arXiv:2607.25622.
- She et al., *MOSAIC: Multi-Subject Personalized Generation via Correspondence-Aware Alignment and Disentanglement*, arXiv:2509.01977.

## Still unchecked / next high-value falsification

- Determine whether semantic-equivalence compilation can be made deterministic enough that differently worded Susan requests produce identical authority/constraint state.
- Find direct image-edit locality metrics that compare protected regions against the accepted base while tolerating global exposure/noise changes.
- Evaluate whether face/physique reference correspondence can be operationalized with the available image-generation interface or must remain a controller-side role contract.
- Search for counterexamples where pre-commit self-auditing increases hesitation/false rejection or worsens end-task performance.
- Deep-read holistic identity ablations to determine whether local/global coordination findings survive large pose, profile, occlusion and extreme subject-scale changes.
