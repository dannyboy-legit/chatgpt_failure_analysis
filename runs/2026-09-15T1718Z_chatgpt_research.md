# ChatGPT research pass — 2026-09-15 17:18Z

## Meaningful new findings

### 1. Authority conflict is a distinct failure dimension from ordinary constraint overload
**Evidence grade: B (primary benchmark/preprint + peer-reviewed ACL evidence). Confidence: HIGH as general mechanism; MEDIUM for individual project failures.**

ManyIH-Bench (2026) evaluates up to 12 instruction privilege levels across 853 agentic tasks and reports frontier-model accuracy around 40% when conflicts scale. IH-Benchmark (2026) separately finds hierarchy compliance spanning 98.2% to 20.5% across 37 models and, importantly, that strong system>user compliance does not reliably predict user>tool compliance. Reasoning Up the Instruction Ladder (Findings ACL 2026) obtains roughly 20% absolute gains in conflict settings by explicitly training models to reason about priority before answering. IH-Challenge reports +10 percentage points average hierarchy robustness for GPT-5-Mini after targeted adversarial RL.

Implication: the project controller must distinguish (a) many simultaneous compatible constraints from (b) conflicting authorities. A flat list of constraints is insufficient. Compile a typed authority DAG before action, resolve conflicts first, then verify surviving constraints.

This also qualifies an earlier diagnosis: raw 'number of constraints' is not the only relevant complexity measure. Source count, authority edges, and conflict surfaces matter independently.

### 2. Adding more explicit reminders can itself damage task execution
**Evidence grade: C/B-boundary (2026 primary preprint; needs peer-reviewed follow-up). Confidence: MEDIUM.**

On the Paradoxical Interference between Instruction-Following and Task Solving (2026) measures SUSTAINSCORE by inserting self-evident constraints already satisfied by a successful output; it reports substantial task-performance drops even on advanced models. RECAST (ICLR 2026) independently confirms that performance becomes difficult as explicit requirements exceed ~10, while showing that targeted multi-constraint training can improve this.

Implication: after compiling the authoritative state, do not feed the generator every historical rule and reminder. Remove redundant constraints that are implied by stronger invariants; preserve them in the audit ledger, not the action packet. This is not permission to omit hard requirements: it is a reason to normalize and deduplicate them.

This weakens the hypothesis that maximal prompt verbosity is monotonically helpful.

### 3. QA itself has a reliability problem; one holistic judge is not a sufficient acceptance gate
**Evidence grade: C (2026 primary preprint) plus B (NSVIF official Microsoft preprint/technical report). Confidence: HIGH as controller principle.**

MCJudgeBench (2026) evaluates judges at the individual-constraint level and finds that high overall correctness does not imply reliable detection of partial/no violations; reasoning improves correctness without uniformly improving stability. NSVIF/VIFBENCH models instruction verification as explicit logical + semantic constraint satisfaction and outperforms LLM-only verification.

Implication: Susan QA should be a vector, not a verdict. Each hard constraint receives PASS/PARTIAL/FAIL with evidence. Hard FAIL rejects the artifact. Judge stability should itself be tested with controlled perturbations. Where deterministic geometry checks are possible (aspect ratio, subject count, anchor measurements, crop, known camera invariants), prefer them over free-form judging.

### 4. Hard and soft constraints should not be optimized or scored identically
**Evidence grade: C/B-boundary (STAIF preprint; IFMTBench primary preprint; MDP-GRPO peer-reviewed ACL). Confidence: MEDIUM-HIGH.**

STAIF explicitly separates subjective/soft constraints from objectively verifiable/hard constraints. IFMTBench uses deterministic gating constraints plus continuous rubric scores and combines them multiplicatively to resist reward hacking. MDP-GRPO focuses on strict multi-constraint satisfaction and shows that discrete violation-sensitive optimization behaves differently from holistic quality optimization.

Implication for image QA: identity, reference transport, requested edit locality, scale geometry, camera lock, and protected-region preservation are hard gates when the scene defines them as such. Aesthetic realism/material quality can be continuous scores. A beautiful image cannot compensate for a failed identity or wrong camera.

### 5. Visual forgetting now has peer-reviewed corroboration, not only preprints
**Evidence grade: B (ACL 2026). Confidence: HIGH as a general multimodal reasoning mechanism; MEDIUM for this product path.**

Visually-Guided Policy Optimization (ACL 2026) reports temporal visual forgetting along reasoning steps and improves visual-dependent performance by explicitly reinforcing visual activation. This independently corroborates Remember-R1 and Take-along Visual Conditioning.

Implication: retain the late visual re-ground gate from the previous pass. Do not replace canonical Susan pixels with prose. Keep final planning-to-generation distance short after re-grounding.

## Project-source comparison

Susan Character Bible v5 explicitly defines three independent systems (Facial Identity, Physique, Scale), places canonical visual references above prose, says references are guides rather than pasted assets, instructs nearest-angle reference selection rather than averaging, and makes facial identity invariant to hairstyle/pose/lighting/expression. It also defines a preservation order: facial identity > physique > scale intent > pose > clothing > environment.

Project Continuity Rules require existing-image edits to preserve identity, physique, clothing style, camera/framing, lighting/mood, environment, scale relationships and composition unless specifically changed, and to introduce only the minimum necessary change.

The Realism Bible adds a different class of requirements: physical camera behavior, environmental scale anchors, posture/environment coupling, and coherent physique. These are not character-identity authorities and should not compete at the same node in the authority graph.

Therefore a flat 'all project rules' packet is structurally wrong. The documents themselves imply typed authorities and different verification domains.

## Controller changes

1. Add `AUTHORITY_DAG`: source -> governed attributes -> priority -> scope -> supersession condition.
2. Add `CONFLICT_RESOLUTION_GATE`: no generation until all authority conflicts are resolved explicitly.
3. Add `CONSTRAINT_NORMALIZER`: deduplicate redundant reminders and compile only active non-redundant requirements into the action packet.
4. Split requirements into `HARD_GATES` and `SOFT_OBJECTIVES`.
5. Replace holistic QA with `CONSTRAINT_VECTOR_QA`: PASS/PARTIAL/FAIL per constraint plus evidence.
6. Add `JUDGE_STABILITY_CHECK` for ambiguous/semantic constraints; deterministic checks take precedence when available.
7. Preserve `LATE_VISUAL_REGROUND` immediately before generation and again before visual QA.
8. Do not allow soft quality scores to compensate for any hard-gate failure.

## Weakened/rejected hypotheses

- **'Constraint count alone explains the failures.'** Weakened. Authority conflict topology and source boundaries are independently difficult.
- **'More reminders are always safer.'** Weakened. Redundant/self-evident constraints can interfere with task solving; action packets should be normalized rather than maximally verbose.
- **'One strong LLM judge is enough for QA.'** Rejected as a reliability assumption. Constraint-level judges can be inconsistent, especially on partial/no cases.
- **'Visual forgetting evidence is only speculative/preprint-level.'** Weakened/rejected as stated: ACL 2026 provides peer-reviewed corroboration of temporal visual forgetting in VLM reasoning. Product-specific causality remains unproven.

## Evidence discipline

Direct project evidence supports what the controller *should have done*. External papers support general failure mechanisms and controller design; none reveal private ChatGPT/Image model internals. Community/issue evidence remains supporting evidence only.

## Remaining unchecked / next pass

- Full methods/ablations for IH-Benchmark and ManyIH-Bench, especially whether failures correlate with number of tiers vs conflict type.
- Controlled literature on redundant-instruction interference and whether normalization/deduplication helps at inference time without retraining.
- Image-edit locality/protected-region metrics with source-available rather than no-reference IQA.
- Face/identity metrics under extreme viewpoint, occlusion, and giant-scale composition.
- Single nearest-angle vs multi-view identity conditioning under controlled pose/expression changes.
- Current Images 2.5 community reports that directly test multi-turn preservation claims, treated only as D-grade evidence.
- Collector arXiv throttling root cause at code level.
