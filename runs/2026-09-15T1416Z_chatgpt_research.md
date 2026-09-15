# ChatGPT research pass — 2026-09-15 14:16Z

## Meaningful new findings

### 1. The edit workflow needs an immutable anchor, not merely inheritance from the immediately previous output
Evidence grade: B (CVPR 2026 + 2026 primary preprint), with strong fit to observed project behavior.

**FreqEdit** (CVPR 2026) explicitly studies multi-turn instruction-based image editing and reports severe progressive degradation under repeated edits. It identifies progressive loss of high-frequency information as a major cause and introduces reference-feature injection plus periodic path compensation; experiments report stronger identity preservation and instruction following over 10+ edits than seven baselines.

Primary: https://openaccess.thecvf.com/content/CVPR2026/html/Liao_FreqEdit_Preserving_High-Frequency_Features_for_Robust_Multi-Turn_Image_Editing_CVPR_2026_paper.html

**AnchorEdit** (June 2026 preprint) independently treats identity drift and error accumulation as a long-horizon editing problem and anchors inference to the initial subject identity rather than trusting only the latest edited frame. It also uses self-rollout training to address exposure bias from sequential edits.

Primary: https://arxiv.org/abs/2606.11751

Controller implication: distinguish `canonical_anchor` from `current_edit_base`. The current base supplies composition and all preserved pixels/scene state; canonical identity/physique anchors remain separately available for QA and identity recovery. Never recursively redefine Susan's identity from the latest generated image. Periodically compare against the canonical anchor, not only the previous output.

### 2. “Preserve everything except X” should be evaluated as a first-class objective, not assumed from an edit instruction
Evidence grade: B.

**Improving Editability in Image Generation with Layer-wise Memory** (CVPR 2025) introduces Multi-Edit Bench specifically because single-turn edit benchmarks miss sequential-edit failure. Its design stores editing history and includes Background Consistency Guidance to maintain unedited regions. This independently supports the project’s existing editing rule: unchanged regions/state need explicit preservation machinery and evaluation.

Primary: https://openaccess.thecvf.com/content/CVPR2025/papers/Kim_Improving_Editability_in_Image_Generation_with_Layer-wise_Memory_CVPR_2025_paper.pdf

The project continuity rules already say that when modifying an existing image, identity, physique, camera/framing, lighting, environment, scale relationships and composition remain stable unless explicitly changed. This is therefore not a newly invented project requirement; research indicates that sequential editors need architecture/controller support to realize it reliably.

### 3. Reference contamination is not just a vague multi-reference risk; pose/background bias can become entangled with subject identity
Evidence grade: B (CVPR 2024).

**Selectively Informative Description can Reduce Undesired Embedding Entanglements in Text-to-Image Personalization** categorizes reference-image biases including background, nearby objects, tied objects, substance/style and **pose bias**. These can become entangled in a learned subject representation, causing reference biases to reappear and reducing prompt alignment.

Primary: https://openaccess.thecvf.com/content/CVPR2024/html/Kim_Selectively_Informative_Description_can_Reduce_Undesired_Embedding_Entanglements_in_Text-to-Image_CVPR_2024_paper.html

This provides a more specific mechanism for the observed Susan problem where a facial identity reference can improperly donate expression/head posture/hairstyle/scene presentation. It does not prove ChatGPT Images uses the same embedding mechanism, but it demonstrates that identity-vs-reference-bias entanglement is a real technical problem in personalized image generation.

Controller implication: maintain explicit `allowed_from_reference` and `forbidden_from_reference` fields. For a Susan face reference, allowed = facial geometry/identity traits; forbidden = expression unless explicitly selected as expression authority, pose, background, wardrobe, scene lighting, camera, composition. The Susan Bible already encodes essentially this separation.

### 4. Intent-aware context folding is stronger evidence for state reconstruction than generic summarization
Evidence grade: B (ACL 2026).

**U-Fold** identifies two failure modes of generic context folding: irreversible loss of fine-grained constraints/intermediate facts and failure to track evolving user intent, causing omissions and erroneous actions. Its intent-aware evolving summary plus compact tool log outperforms ReAct and prior folding baselines, with a reported 71.4% win rate in long-context settings and improvements up to 27% over folding baselines.

Primary: https://aclanthology.org/2026.findings-acl.897/

**MT-OSC** (ACL Findings 2026) provides counterweight: selective sequential condensation can reduce tokens by up to 72% in 10-turn dialogues while improving or preserving accuracy. Thus “summarization is bad” is too broad. The better conclusion is: indiscriminate chronological summarization is risky; selective, intent/state-aware condensation can help.

Primary: https://aclanthology.org/2026.findings-acl.1354/

This refines the previous pass: the controller should reconstruct authoritative state, but it can use selective condensation as a mechanism so long as constraints, intent transitions, and tool state are explicitly protected.

### 5. Current OpenAI product evidence weakens the hypothesis that multi-turn image drift is simply unavoidable at the base-model level
Evidence grade: B (official product documentation).

OpenAI’s September 8, 2026 Images 2.5 release states that the current model is better at preserving subjects from reference photos, making focused edits while keeping other details stable, and maintaining quality/instructions across multiple editing turns. This does not guarantee perfect compliance, but it means repeated drift cannot be dismissed as an inevitable property of the current product generation model.

Official: https://openai.com/index/introducing-chatgpt-images-2-5/

OpenAI Academy guidance also recommends a small set of uploaded references and explicitly assigning each image a role, rather than a large undifferentiated bundle.

Official: https://openai.com/academy/image-generation/

Controller implication: when a current-product edit fails to preserve unrequested regions, treat it as a failed acceptance test and retry/replan from the original accepted base where possible rather than normalizing the drift as unavoidable.

### 6. Persistent identity is empirically distinct from image quality and instruction following
Evidence grade: B/C pending peer review (September 2026 preprint; primary source).

The **Persistent Identity Preservation in Generative Image Models** benchmark reports that strong image quality and instruction following do not imply strong identity fidelity, and that identity degradation worsens under iterative edits, small subject scales, degradation, and multi-subject composition. It argues for identity represented as persistent subject knowledge independent of the generative foundation model.

Primary preprint: https://arxiv.org/abs/2609.04151

This strengthens a controller-level separation already present in Susan’s Character Bible: `identity_score`, `instruction_score`, and `visual_quality_score` must be independent hard axes. A visually excellent image that follows the scene prompt but depicts the wrong Susan is a failure, not a partial pass.

## Hypotheses weakened/refined

1. **“Long context is the main problem.”** Further weakened. Sequential image editing has its own artifact-level accumulation mechanisms even if conversational state were perfect.
2. **“Always regenerate from the latest accepted edit.”** Weakened. Research supports retaining an immutable identity/initial anchor alongside the current edit base and periodically recalibrating against it.
3. **“Reference-role contamination is just prompt ambiguity.”** Weakened. Personalization research directly documents pose/background/object/style biases becoming entangled with subject representations. Exact applicability to ChatGPT Images internals remains unknown.
4. **“Summarization itself causes state loss.”** Refined. Generic/intent-insensitive summaries can lose constraints, while selective intent-aware condensation can improve long-context performance.
5. **“Current image-model limitations make exact preservation unrealistic by definition.”** Weakened. OpenAI’s current Images 2.5 product claims explicitly target multi-turn preservation and focused edits. Failure remains possible, but preservation is a supported target rather than an invalid expectation.

## Concrete controller changes

Add to execution state:

- `canonical_anchor`: immutable Susan identity/physique authorities.
- `current_edit_base`: most recent accepted image supplying composition/environment/pixel state.
- `edit_delta`: only requested change(s).
- `preservation_mask_semantic`: identity, physique, camera, composition, environment, lighting, scale, clothing, etc. that must not change.
- `allowed_from_reference` / `forbidden_from_reference` for every visual reference.
- `drift_budget`: zero for hard identity/scale/composition locks; separately configurable for soft texture/lighting details.
- `anchor_recheck`: compare each accepted output against canonical identity/physique anchors, not only the preceding image.
- `rollback_source`: after a rejected edit, retry from the last accepted base rather than editing the rejected artifact.
- independent scores for identity, instruction adherence, preservation of unedited regions, visual quality, scale geometry, and material realism.

## Project-source comparison

Susan Character Bible v5 defines facial identity, physique and scale as independent systems; tells the renderer to select the closest facial/physique reference by camera angle; and makes facial identity invariant to hairstyle, pose, lighting and expression. It explicitly says references are guides, not pasted assets. The Real Giantess continuity rules independently require minimum-change editing and preservation of identity, physique, camera/framing, lighting, environment, scale and composition. The Hypothetical Reality/Notebook material says to preserve geometry and translate the event rather than copy a pose/rendering. These requirements closely match the architectural separation advocated by the newly checked editing/personalization research.

## Automation/repository evidence

The repository contained only the previous ChatGPT research note under `runs/`; no new quarter-hour worker research output was present when this pass inspected it. The analysis automation itself is functioning because this pass can read and write the repository, but the deterministic source-collector path appears not to be producing committed run artifacts yet. This should be treated as an automation defect to inspect separately rather than silently assuming the worker corpus exists.

## Unchecked / next-pass targets

- Inspect GitHub workflow files and latest workflow-run logs to determine why deterministic collector outputs are not appearing.
- Read FreqEdit and AnchorEdit methods/results beyond abstracts, especially ablations separating identity drift, quality loss and instruction failure.
- Search iterative editing benchmarks for preservation of camera/composition/geometry, not only identity/perceptual quality.
- Investigate visual-reference role tagging or per-reference gating in current multimodal diffusion/AR architectures.
- Search contradictory evidence where multiple references improve identity robustness without sacrificing editability.
- Compare OpenAI Images 2.5 official claims against reproducible developer/community reports, keeping those reports at evidence grade C/D.
