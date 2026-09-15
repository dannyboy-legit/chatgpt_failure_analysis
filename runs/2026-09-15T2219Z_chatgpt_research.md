# Research Pass — 2026-09-15T2219Z

## New direct project evidence: source-version conflict is not hypothetical

This pass independently searched previously unchecked/addendum-style Real Giantess Project material and found concrete contradictory rules in the Library.

1. Susan Character Bible v5 says Facial Identity, Physique, and Scale are independent systems; changing Susan's height changes only absolute size, not identity or anatomical proportions. It makes canonical face/physique images authoritative and selects the nearest view rather than averaging references.
2. `Susan_Character_Bible_Addendum_Dynamic_Scale.docx` says that as Susan grows, her physique develops proportionally (broader shoulders, stronger legs, more musculature/fullness) and still names older Chloe-based face references as source of truth.
3. Susan v4.3 explicitly says canonical facial references override generated images, physique sheets, and previous scenes, and the nearest matching face reference should be used without averaging.

This is direct evidence that a raw long-thread/library retrieval strategy can surface mutually incompatible project state. The failure mechanism is therefore stronger than generic long-context distraction: **VERSION/PROVENANCE CONFLICT**. A stale but semantically relevant document can be retrieved and applied even though a newer canonical source supersedes it.

### Controller consequence
Add `SOURCE_VERSION_GATE` before compilation. Every source must carry: source_id, version/date where available, canonical/superseded status, governed attributes, and supersession relation. Superseded documents remain available only for contradiction tracing and historical diagnosis. They cannot contribute active generation constraints unless explicitly reactivated.

A useful negative control is now concrete: compile the same Susan scale request with v5 plus the Dynamic Scale addendum in retrieval context. The active IR must preserve v5's scale/physique independence and reject the stale proportional-development rule. If it does not, the compiler fails before generation.

## New direct project evidence: invariant identity is not invariant appearance

`Documentary_Cinematography_Bible_UPDATED_v2.txt` adds a photographic re-capture layer: identity/core anatomy stay locked, but skin reflectivity, highlights, tonal balance, atmospheric blending, exposure response and other perceptual material properties are explicitly not locked; environmental lighting should override fixed character-shader assumptions. Camera imperfections must remain physically plausible and must not destroy scale readability.

This refines the preservation contract. `MUST_NOT_CHANGE` cannot mean pixel-level invariance for every protected semantic attribute. It needs typed invariance:
- **GEOMETRIC/IDENTITY invariants**: facial anatomy, canonical body geometry, camera/scene geometry when locked.
- **PHOTOMETRIC covariates**: legitimate changes caused by lighting, exposure, focus, noise, white balance, atmosphere and material response.
- **SCENE delta**: explicitly requested changes.

For local edits where lighting is not requested to change, continuity still keeps lighting/mood stable; but QA must tolerate physically plausible sensor-level variation rather than treating any pixel difference as semantic drift.

## New peer-reviewed evidence: long reasoning can directly hurt visual grounding

ACL 2026 `Look Light, Think Heavy: What Multimodal Chain-of-Thought Reasoning Can and Cannot Do` evaluates 12 multimodal tasks, 14 non-reasoning models and 8 reasoning models. It finds CoT is not a free lunch: perception tasks can degrade under CoT, including visual grounding/object counting, while visual reflection diminishes through reasoning. ACL 2026 `Visually-Guided Policy Optimization` independently reports temporal visual forgetting and improves performance by explicitly reinforcing visual activation.

This strengthens the late-grounding rule and adds a new falsification: for reference-selection and visual-identity checks, compare short direct visual inspection against extended CoT. More reasoning should not be assumed safer for perception-heavy gates.

## New tool-reliability evidence: rejection and recovery are distinct capabilities

AgentProp-Bench (2026 preprint; human-calibrated benchmark) reports parameter-level errors propagating to wrong final answers with probability about 0.62, while ability to reject corrupted inputs and ability to recover after accepting them are statistically independent. Its automated substring judge is near chance agreement with human labels (kappa 0.049), while human agreement is high.

This refines the controller: `PRE_COMMIT_REJECTION` and `POST_FAILURE_RECOVERY` require separate tests and metrics. A controller that catches malformed plans may still recover badly once a fault enters state, and vice versa. Do not infer one capability from the other.

## New identity/reference evidence

TRACE-Bench (ACM Multimedia 2026) formalizes multi-reference generation around preserving target identity while binding reference-specific attributes and shared layout constraints. `Towards Generalized Multi-Image Editing for Unified Multimodal Models` (2026 preprint) explicitly adds per-image latent separators and image-index encodings because models struggle to disambiguate cues across multiple input images. This reinforces role-tagging at the visual-token/reference level, but does not prove current ChatGPT Images exposes such internal controls.

## Weakened/rejected hypotheses

- **All relevant project documents can safely be retrieved together.** Rejected. The Library contains directly contradictory Susan scale rules and stale face-reference language.
- **Protected content should be evaluated by raw visual/pixel sameness.** Rejected. The updated cinematography source explicitly requires fresh photographic re-capture behavior under environmental lighting/camera response.
- **Longer reasoning is always safer for visual-reference verification.** Rejected as a general rule; ACL 2026 provides peer-reviewed counterevidence for perception-heavy tasks.
- **Good pre-action rejection implies good recovery.** Rejected by AgentProp-Bench's independence result.

## Revised controller additions

1. `SOURCE_VERSION_GATE` and supersession graph.
2. `TYPED_INVARIANCE`: semantic/geometric locks vs legitimate photometric covariates.
3. `PERCEPTION_BUDGET`: visual identity/reference gates use concise direct grounding; extended reasoning occurs around, not instead of, visual inspection.
4. Separate `REJECTION_SCORE` and `RECOVERY_SCORE` in reliability evaluation.
5. Negative-control tests using known stale Susan addenda and obsolete face language.

## Evidence grades

- Direct project evidence (A): Susan v5; v4.3; Dynamic Scale addendum; updated Documentary Cinematography Bible; Project Continuity Rules.
- Peer-reviewed/primary scientific evidence (B): ACL 2026 Look Light, Think Heavy; ACL 2026 VGPO; ACM MM 2026 TRACE-Bench.
- Primary preprint/benchmark evidence (C): AgentProp-Bench; generalized multi-image editing paper.

## Remaining unchecked

- Locate/reconcile any standalone Anatomy Addendum and Simplified Rules if separately stored under non-obvious filenames.
- Inspect canonical Susan visual reference assets themselves and test nearest-angle single-reference vs multi-view empirically.
- Build executable source-to-IR compiler and run stale-source negative controls.
- Establish semantic/geometry-aware edit locality metrics that tolerate legitimate photometric recapture.
- Validate AgentProp-Bench beyond the preprint and inspect its human-label protocol in detail.
