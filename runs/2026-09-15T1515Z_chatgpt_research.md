# ChatGPT iterative research pass — 2026-09-15T15:15Z

## Meaningful new findings

### 1. Current-state tracking is a separate failure mechanism from generic long-context degradation — B evidence, strong applicability
StateMemBench (Fan et al., arXiv:2608.19652, 2026) explicitly tests whether agent memory reflects the *current* state rather than a superseded state. Existing memory, retrieval, and long-context baselines struggle. StateMem's explicit supersession/dependency representation improves current-state accuracy substantially; a length/cost-matched control attributes a large part of the gain to state structure rather than merely more context.

This sharpens the Susan diagnosis. The controller must not just summarize or retrieve rules. It must represent supersession: current selected image, last accepted base, rejected branches, current scene overrides, persistent canonical rules, and which older instructions have been replaced. A retrieved old instruction can be accurate historically and still be wrong operationally.

### 2. Multi-reference generation failures decompose into operators; disentanglement and attribute binding are the bottleneck — B evidence, direct design relevance
TRACE-Bench (Wang et al., arXiv:2608.16765, 2026) decomposes multi-reference generation into Anchor, Disentangle, Apply, and Compose operations. Across nine leading models, its primary bottleneck is disentanglement and attribute binding rather than scene-level composition; even the best model reports only 0.74 attribute fidelity.

This is stronger support for treating the Susan source system as an explicit operator graph rather than a bag of references: Anchor(face identity), Anchor(physique), Disentangle(reference-only attributes), Apply(scene expression/gaze/hair/clothing), Compose(environment/camera/scale). QA should score these operators separately so a visually plausible composition cannot hide identity/reference-role failure.

### 3. Reference leakage is not merely a theoretical risk; attribute-specific conditioning is an active research target — B evidence
ComposeMe (SIGGRAPH Asia 2025 / arXiv:2509.18092) is motivated by standard personalization leaking expression, head orientation, pose, hair or clothing from reference imagery. It uses attribute-specific reference tokens and deliberately misaligned cross-reference training to force disentanglement. This strongly supports the project's existing rule that a face reference controls identity rather than pose/expression and that a physique reference controls anatomy rather than scene content.

### 4. Iterative image degradation can evade generic image-quality evaluators — C/B-preprint evidence, important QA correction
Banana100 (arXiv:2604.03400, 2026) generates 28,000 images through repeated edits and reports progressive visible degradation plus instruction-following failure. More importantly for our controller, none of 21 tested no-reference IQA metrics consistently ranked heavily degraded outputs below clean ones.

Therefore a generic 'image quality' score cannot be the approval gate for Susan edits. QA must compare against anchors and requested deltas: identity similarity, protected-region change, geometry, scale anchors, materials, and instruction compliance. Absolute aesthetic/IQA scoring is supplementary only.

### 5. Constraint verification should be modeled as constraint satisfaction rather than generator self-confidence — B evidence
NSVIF/VIFBENCH (Su et al., Microsoft Research/arXiv:2601.17789, 2026) formalizes instruction-following verification as logical + semantic constraint satisfaction and reports better verification than LLM-only approaches, with verifier feedback improving following without post-training. This adds constructive evidence beyond the earlier negative self-correction literature: externalized constraints can become executable verification objects.

For the project, compile every generation into typed constraints: equality/preservation constraints (camera unchanged), role constraints (face ref cannot donate pose), geometry constraints (uniform scale relative to anchors), semantic constraints (ordinary documentary capture), and delta constraints (only requested region changes). Do not approve from a prose gestalt.

## Project-source cross-check

Fresh Library retrieval confirms that the project documents already contain the necessary conceptual separation:
- Susan Character Bible v5: canonical facial refs > physique refs > Bible > scene prompt; reference images are guides rather than pasted assets; facial identity is invariant to hairstyle, pose, lighting and expression; physique refs define anatomy/silhouette; nearest-angle refs are selected by camera angle.
- Hypothetical Reality Bible v1.1: preserve geometry first, change only the minimum necessary, environment is the ruler, translate the event rather than artistic style.
- Documentary Cinematography Bible: event-first, observer-grounded camera, ordinary real-world imperfections and environmental scale anchors, avoid poster/glamour framing by default.
- Locked Project Rules: edits preserve identity, physique, camera, lighting, environment, scale, clothing and composition unless explicitly changed.

This further weakens 'the source documents were underspecified' as an explanation. The missing layer is executable state/constraint binding and artifact verification.

## Weakened/rejected hypotheses

- **'A compact summary is enough.'** Weakened. StateMemBench indicates that explicit supersession/current-state structure matters independently of context length. Use a state graph, not merely a shorter narrative.
- **'Multi-reference difficulty is mainly composition complexity.'** Weakened by TRACE-Bench: disentanglement and attribute binding are reported as the dominant bottlenecks.
- **'A generic visual quality evaluator can catch iterative degradation.'** Rejected as a sufficient gate by Banana100's evaluator results.
- **'Reference leakage is just poor prompting.'** Further weakened by ComposeMe and TRACE-Bench; dedicated architectures/training objectives are being built specifically to solve it.

## Controller changes

1. Add an explicit **supersession graph** with `active`, `persistent`, `overridden`, `rejected`, and `historical-only` states for every inherited constraint/source.
2. Compile multi-reference tasks into an operator plan: **Anchor -> Disentangle -> Apply -> Compose**. Require an allowed/forbidden attribute map at each reference edge.
3. Convert prose requirements into typed, externally checkable constraints before tool execution.
4. Replace generic image-quality approval with differential QA against canonical anchors and protected regions.
5. Add an **ancestry budget**: after iterative edits, periodically regenerate/re-anchor from the last trusted base + canonical identity instead of indefinitely using descendants.
6. Treat a failed/rejected image as `historical-only`; it can inform diagnosis but cannot donate pixels, pose, identity, or scene state to a retry unless explicitly selected.

## Automation evidence correction

The previous 14:16Z note said deterministic quarter-hour collector artifacts were absent because it inspected only `runs/`. That diagnosis was wrong. The workflow writes to `source_queue/`, not `runs/`. Direct inspection now finds multiple collector artifacts from 12:58Z through at least 14:56Z, while `research.yml` schedules collection at 5,20,35,50 and `collect_sources.py` writes timestamped Markdown into `source_queue/`. Therefore the source collector is operational. The earlier 'collector absent' conclusion is retracted; the actual failure was our inspection path.

There is still a timing irregularity worth tracking: observed queue timestamps are not exactly the cron minute, which is normal for GitHub scheduled workflow dispatch latency and does not by itself imply failure. The meaningful health criterion is continued creation of source_queue artifacts and successful commits, not exact wall-clock start.

## Unchecked / next directions

- Read StateMemBench methods/ablations beyond abstract to determine the minimum supersession representation needed for our controller.
- Read TRACE-Bench full diagnostic tree and per-model operator results; map its operators to face/physique/pose/environment references.
- Examine whether identity metrics themselves fail under extreme scale, occlusion, profile views, or stylized lighting.
- Search specifically for protected-region/locality metrics in iterative image editing, not generic IQA.
- Inspect source_queue candidate quality/duplication rate and synthesis behavior; the collector is running, but useful recall vs noise is not yet measured.
- Find controlled evidence on whether single nearest-angle face reference or multiple identity views gives better identity/variation tradeoff in current general-purpose multimodal generators.
