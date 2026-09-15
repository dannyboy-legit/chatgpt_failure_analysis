# ChatGPT research pass — 2026-09-15 13:20Z

## Meaningful new findings

### 1. Multi-turn unreliability is a stronger explanation than raw context length alone
Evidence grade: B (primary research), with A-level fit to observed conversation trajectory.

Microsoft Research / ICLR 2026 Best Paper **LLMs Get Lost in Multi-Turn Conversation** reports an average 39% performance drop across six generation tasks when requirements are developed through multi-turn conversation rather than supplied fully specified in one turn. Their analysis attributes the larger effect to increased unreliability rather than loss of underlying aptitude, and identifies premature early assumptions plus failure to recover from a wrong conversational turn as a central pattern.

This sharpens the existing diagnosis. The Susan history is not merely a long-context problem. It is also an *interaction-path dependence* problem: early mistaken interpretations and failed branches can become anchors. A compact state compiler should therefore reconstruct intent from authoritative sources/current request rather than summarize the conversational trajectory indiscriminately.

Primary source: https://www.microsoft.com/en-us/research/publication/llms-get-lost-in-multi-turn-conversation/

### 2. Structural turn relationships need explicit state representation
Evidence grade: B.

**StructFlowBench** (Findings of ACL 2025) evaluates six kinds of structural relationships between dialogue turns and finds significant deficiencies in current models' understanding of multi-turn dialogue structure. This is directly relevant to image-edit workflows where a later turn may be a refinement, override, preservation request, correction, or continuation rather than an independent prompt.

Controller implication: every user turn affecting an active image should be typed before execution: {new scene, refinement, local edit, override, rollback, continuation, critique-only}. A refinement must inherit all unnamed locked variables; an override changes only named dimensions; a rollback must invalidate the failed branch.

Primary source: https://aclanthology.org/2025.findings-acl.486/

### 3. Conversation depth degrades failure recovery even in newer frontier systems
Evidence grade: B.

**EvolIF / One Battle After Another** (ACL 2026) uses evolving multi-turn evaluations across 12 constraint groups and reports deficiencies in failure recovery and fine-grained instruction following as conversational depth increases. GPT-5 leads the evaluated systems but reaches a 66.40% stability score rather than reliable saturation.

This weakens any hypothesis that a sufficiently capable base model alone eliminates the Susan problem. The controller needs explicit state tracking and recovery gates even when the underlying model is strong.

Primary source: https://aclanthology.org/2026.acl-long.433/

### 4. Error localization and recovery should be evaluated separately from final success
Evidence grade: B/C pending full manuscript verification.

A newly surfaced September 2026 benchmark, **ParaRecover**, targets process-level recovery in multi-turn parallel tool use with 14 error types and reports persistent difficulty with implicit tool failures, error propagation, and precise replanning. This is highly relevant to the repository incident where an obsolete GitHub Models endpoint failed: a robust controller must identify whether failure occurred in source retrieval, transport, tool invocation, model generation, or QA rather than treating all failures as prompt failures.

Source metadata/index: https://www.roboticscenter.ai/research/papers/pararecover-a-process-level-benchmark-for-error-localization-and-recovery-in-parallel-tool-2609

Status: promising but do not promote beyond supporting evidence until the original arXiv manuscript is directly verified.

## Hypotheses weakened or refined

1. **Raw context length is the primary cause** — weakened. Multi-turn path dependence and failure recovery appear independently important. The correction is not only compression; it is authoritative state reconstruction that deliberately excludes failed-branch momentum.
2. **A good summary of prior turns is sufficient state management** — weakened. Summaries can preserve the wrong conversational branch. State must encode turn relationships and source authority, not merely content.
3. **Better base-model intelligence removes the need for external control** — weakened. EvolIF still finds substantial stability limits in strong frontier models.
4. **Post-failure retry is one capability** — refined. The workflow should distinguish detection/localization from replanning/recovery; success at one does not imply success at the other.

## Concrete controller changes

Add these fields to the pre-action state object:

- `turn_relation`: new_scene | refinement | local_edit | override | rollback | continuation | critique_only
- `branch_status`: valid | failed | superseded
- `inherit_unnamed_constraints`: true by default for refinement/local-edit/continuation
- `failed_branch_fingerprint`: hash/reference preventing reuse of the same failed interpretation
- `source_of_truth`: explicit current image + canonical identity/physique assets + latest governing documents
- `recovery_layer`: retrieval | reference_transport | instruction_binding | tool_invocation | generation | artifact_QA

On failure, first localize `recovery_layer`; then change that layer. Do not rewrite the entire prompt by default.

## Susan-source comparison

Susan Character Bible v5 already demands a modular authority hierarchy: canonical facial references, canonical physique references, Bible, then scene prompt; it also says references guide identity/anatomy rather than being pasted assets, and pose/camera references must not redefine identity or physique. The observed failures therefore cannot be explained by absent project rules. The new multi-turn evidence suggests a more specific mechanism: correct rules were present, but conversational branch state and execution state were not reliably reconciled with those authorities immediately before action.

## Unchecked / next-pass targets

- Directly verify the original ParaRecover manuscript and methods/results tables.
- Search primary work on *intent reconstruction vs memory summarization* in multi-turn agents; test whether state reconstruction outperforms chronological summarization.
- Search image-generation work specifically measuring identity fidelity across iterative edits (not only one-shot subject-driven generation).
- Search evidence on negative transfer/interference from multiple visual references and role-tagging effectiveness.
- Inspect community/implementation reports only after primary-source expansion; use them to generate hypotheses, not infer internals.
- Build a formal turn-relation transition table for the Susan workflow and compare it against historical failure examples.
