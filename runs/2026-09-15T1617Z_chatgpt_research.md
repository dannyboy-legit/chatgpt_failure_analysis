# ChatGPT iterative research pass — 2026-09-15T16:17Z

## Meaningful new findings

### 1. Visual evidence itself can decay during long multimodal reasoning — C/B-preprint evidence; HIGH design relevance
Remember-R1 (Chen et al., arXiv:2608.01314, 2026) studies long-context visual forgetting: as multimodal reasoning grows, models increasingly rely on accumulated text and less on the original image. Its process-level intervention explicitly rewards persistence of visual dependence and relevant-region attention. Earlier Take-along Visual Conditioning (Sun et al., arXiv:2503.13360) reports an ablation where removing the image midway through long visual reasoning caused only ~2% accuracy loss on MathVista test-hard, suggesting later reasoning had become predominantly text-driven.

This is a new mechanism relative to generic long-context degradation. For Susan, even if a canonical face/physique image is successfully attached and initially inspected, a long pre-generation reasoning chain can still become text-dominant. Therefore reference transport is necessary but not sufficient: the controller should re-ground against the actual selected visual references immediately before the generation call and again during QA rather than relying on an early visual read plus a long textual derivation.

### 2. Multimodal memory has a tradeoff: raw long context loses accuracy with length, compressed memory loses visual fidelity — C/B-preprint evidence; HIGH applicability
MemLens (Ren et al., arXiv:2605.14906, 2026) benchmarks 789 multimodal multi-session questions from 32K-256K tokens. Its image ablation drives two frontier LVLMs below 2% accuracy on questions whose evidence includes images. Long-context LVLMs degrade as conversations grow; memory-augmented agents are more length-stable but lose visual fidelity during storage-time compression. Multi-session reasoning remains below 30% for most systems. The paper argues for hybrid long-context + structured multimodal retrieval.

This falsifies two extreme controller designs: neither 'keep the entire raw multimodal thread' nor 'compress everything into text memory' is adequate. For Susan, canonical reference pixels should remain immutable retrievable anchors while textual state stores only role assignments, supersession, scene variables, and constraints. The visual identity itself must not be compressed into prose and then treated as equivalent to the source image.

### 3. Constraint replacement can temporarily restore adherence; accumulation is substantially worse — C/B-preprint evidence; directly useful
SEQUOR (Canaverde et al., arXiv:2605.06353, 2026) runs 1,400 fifty-turn conversations. It reports declining adherence even for a single persistent constraint, much larger losses for multiple constraints, and particularly severe degradation when constraints are accumulated sequentially. In its Replace regimes, replacing active constraints produces sharp recovery toward initial performance, while Add regimes deteriorate strongly when new constraints arrive.

This adds an actionable distinction to the supersession graph: old constraints should not merely be marked inactive while remaining in the execution packet. The action packet should be rebuilt from the currently active set after a material override/rollback. Historical rules remain in the audit ledger, but only active/persistent constraints enter the generation packet. This is stronger than a narrative summary and avoids carrying inert constraints as distractors.

### 4. Error recovery should replan globally when the failure invalidates the route, not merely repair the local call — B peer-reviewed evidence
CAR / ToolHop-Pro (Wang et al., Findings ACL 2026) identifies two failure classes in open-ended tool agents: closed/static action spaces and myopic error recovery that repeatedly retries locally rather than revising the high-level plan. Its architecture explicitly performs global trajectory rectification. Fission-GRPO (Zhang et al., ACL 2026) independently trains on the model's own execution errors and improves BFCL-v4 multi-turn recovery by 5.7 points absolute and overall accuracy from 42.75% to 46.75%, with gains up to 17.4% on TAU/TAU2 settings.

For this project the repair controller should classify failures as either LOCAL (e.g. one malformed parameter with the route still valid) or ROUTE-INVALIDATING (required reference cannot reach generator, wrong active base, wrong source authority, repeated identity contamination). A route-invalidating failure forces a new plan/reference path; localized prompt edits are prohibited.

### 5. The project sources already imply an event/geometry state machine, not merely a style guide — A direct project evidence
Fresh Library retrieval confirms the Hypothetical Reality Constitution v1.1 requires preserving geometry first, narrative second, and modifying only the minimum interaction necessary; it explicitly says preserve camera/body mechanics/composition and 'preserve the measurements; rebuild only the moment.' The Documentary Cinematography Bible defines event-first observer-grounded capture and scale through familiar environmental anchors. Project Continuity Rules require edits to preserve identity, physique, clothing, camera/framing, lighting, environment, scale and composition unless changed. Susan v5 separately assigns face identity, physique, scale and pose/camera authority.

A stronger controller therefore needs two linked state objects: (a) CHARACTER STATE — immutable face/physique authority; (b) EVENT GEOMETRY STATE — camera, anchors, body orientation, contact geometry, scale relationships, environment and edit delta. Treating all of this as one natural-language prompt loses the source documents' own modular structure.

## Weakened / rejected hypotheses

- **'Once reference transport succeeds, visual grounding is solved.'** Weakened. Remember-R1/Take-along Visual Conditioning show visual dependence can decay later in a long reasoning trajectory.
- **'Textual compression of the project state is always safer than raw context.'** Rejected as a general rule. MemLens shows memory compression can sacrifice visual fidelity; canonical pixels must remain separately retrievable.
- **'Inactive historical constraints are harmless if correctly labeled.'** Weakened. SEQUOR shows accumulated constraints are much harder than replacement/reset conditions. The execution packet should contain the minimum active set, with history outside it.
- **'Every retry should modify only the immediately failed call.'** Rejected for route-invalidating failures. CAR specifically targets myopic local retries by global replanning.

## Controller changes

1. Add a **late visual re-ground gate** immediately before image generation: reopen/inspect the selected canonical face and physique anchors and bind their roles to the final call. Do not allow a long textual reasoning tail after this gate.
2. Split memory into **immutable visual anchors** and a compact **active symbolic state**. Never substitute prose for canonical identity pixels when the pixels are available/required.
3. Recompile the execution packet after overrides/rollbacks so it contains only `persistent + active` constraints; keep `overridden/rejected/historical` material in a separate audit ledger unavailable to generation unless explicitly restored.
4. Split controller state into `CHARACTER_STATE` and `EVENT_GEOMETRY_STATE`, then compose only at the final action boundary.
5. Add failure severity: `LOCAL_REPAIR` versus `ROUTE_INVALIDATING`. The latter requires global replanning and a new plan fingerprint before another generation.
6. Add a **visual-grounding freshness** field recording when each reference was last directly inspected relative to the generation call; stale visual grounding fails closed.

## Automation / source-collector evidence

The deterministic collector is still producing source_queue files through at least 15:54Z, so the scheduler/commit path is alive. However, the newest inspected queue file contains eight arXiv collection failures in a single pass: a mix of read timeouts and HTTP 429 responses. Its GitHub issue search still produced candidates. This means the collector is operational but currently degraded for academic-source recall. It must not be treated as a complete discovery feed. Hourly direct web research remains necessary, and the collector should eventually add exponential backoff/jitter, query staggering, caching/deduplication, and retry limits for arXiv rather than issuing a burst that triggers rate limits.

## Evidence grading

- Direct project document requirements: **A**.
- CAR and Fission-GRPO (ACL 2026): **B**, peer-reviewed primary evidence.
- SEQUOR, MemLens, Remember-R1 and Take-along Visual Conditioning: **C/B-preprint** until venue status is verified; use as primary technical evidence but not as proof of ChatGPT internals.
- Collector 429/timeouts: **A/C runtime/implementation evidence** for this repository only.

## Unchecked / next directions

- Read MemLens methods/ablations to quantify which compression methods lose visual fidelity and whether hybrid retrieval preserves images or derived embeddings.
- Read Remember-R1 attention/ablation details to turn 'visual-grounding freshness' into a measurable test rather than a heuristic.
- Search protected-region/locality metrics for image editing and identity metrics under profile/occlusion/extreme scale.
- Test single nearest-angle reference vs multiple views with role-separated conditioning; current evidence still does not establish the best tradeoff for the deployed general-purpose image generator.
- Inspect collector code and workflow for request burst behavior, caching and retry/backoff before modifying it.
- Search current Images 2.5 user/issue evidence for whether claimed multi-turn subject preservation survives long edit chains and multiple references.
