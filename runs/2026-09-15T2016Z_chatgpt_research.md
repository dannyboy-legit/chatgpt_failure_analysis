# Iterative research pass — 2026-09-15T20:16Z

## New findings

### 1. The controller must verify cross-modal closure, not just text-plan correctness and final-image quality separately
Evidence grade: B.

ROVER (ICLR 2026) evaluates reciprocal cross-modal reasoning: using verbal reasoning to guide visual synthesis and visual outputs to guide/refine verbal reasoning. Across 17 unified models, interleaved systems outperform non-interleaved combinations, and the authors report that simply combining strong unimodal components does not reproduce robust cross-modal reasoning. This is a new correction to the controller: a correct textual Susan state and a competent image generator are not sufficient if the binding between them is weak.

Controller change: add CROSS_MODAL_CLOSURE gates. Before generation, every hard symbolic constraint must map to an observable visual target/region/relationship. After generation, visual observations must map back to the same constraint IDs. A constraint is not considered verified because it existed in prose; it must survive text→visual realization→visual verification.

### 2. Identity and spatial structure are competing objectives that benefit from explicit spatial control
Evidence grade: B (SIGMA-GEN is ICLR 2026; Adobe Research official summary plus primary paper metadata).

SIGMA-GEN explicitly frames identity preservation and spatial/structural control as simultaneous, difficult objectives. It supports identity plus coarse boxes, 3D boxes, masks, segmentation and depth in one pass and reports improved multi-subject identity preservation. This is directly relevant to giantess scenes where Susan identity, body geometry, John/environment placement and scale anchors must coexist.

This weakens the assumption that textual statements such as 'same Susan, larger, same room' are the strongest possible representation. Where the tool permits it, spatial constraints should be encoded geometrically rather than only linguistically: bounding regions, depth ordering, contact points, fixed anchor coordinates, masks/protected regions.

### 3. Multi-turn editing failure is trajectory-level, not just a sum of local edit failures
Evidence grade: B/C.

Apple's MT-EditFlow research page identifies two coupled failure modes: all-or-nothing sequence success and exposure-bias error propagation. It reports that optimizing aggregated trajectory reward and broadcasting advantage across the editing trajectory improves turn-3 overall performance of FLUX.1-Kontext-dev by 6.85 points. FreqEdit (CVPR 2026) independently identifies progressive high-frequency information loss and uses reference injection plus path compensation to stabilize 10+ edits. AnchorEdit likewise anchors initial identity and addresses causal sequential drift.

Controller change: add TRAJECTORY_HEALTH separate from per-turn QA. Maintain cumulative drift measures against immutable canonical references and the original/accepted scene geometry. A turn may individually pass while pushing the sequence toward collapse; cumulative thresholds can force rebase from a clean accepted ancestor plus canonical anchors rather than continuing recursively.

### 4. The project documents already supply the semantics needed for cross-modal closure
Evidence grade: A.

Project Continuity Rules require existing-image edits to preserve identity, physique, clothing style, camera/framing, lighting/mood, environment, scale relationships and composition, introducing only minimum requested changes. Documentary Cinematography makes real camera behavior and familiar environmental objects part of the scene's scale evidence. Therefore these are not merely prose aesthetics: they can be compiled into observable visual predicates (same camera geometry, same anchor positions, same relative scale/contact geometry, same identity features).

This strengthens the conclusion that the missing layer is executable grounding, not more creative-description prose.

### 5. Strong identity preservation does not imply instruction/spatial correctness, and vice versa
Evidence grade: B/C.

The September 2026 Persistent Identity Preservation benchmark reports identity degradation under iterative edits, small subject scales and multi-subject composition while noting that image quality/instruction adherence can remain comparatively strong. SIGMA-GEN's framing reaches the complementary conclusion from spatial control. These results reject a scalar 'overall quality' view: identity, structure/scale, edit instruction, and perceptual quality remain distinct axes.

Controller change: preserve hard vector gates and add scale-sensitive identity evaluation. If Susan occupies too few pixels for a reliable facial judgment, mark identity UNVERIFIABLE rather than PASS; require another view/reference or defer identity acceptance instead of hallucinating confidence.

## Weakened/rejected hypotheses

- 'A correct text state plus a good image generator is enough' — weakened by ROVER; cross-modal binding/reciprocal verification is its own capability.
- 'Local per-turn QA is sufficient for multi-turn editing' — rejected as a reliability strategy; trajectory-level exposure bias and cumulative degradation require cumulative health/rebase controls.
- 'Text is the best available representation for camera/scale/layout constraints' — weakened; explicit spatial structure improves controllability when supported.
- 'Identity can always be judged from the final image' — rejected for small-subject/extreme-scale cases; identity may be unobservable at available resolution.

## Concrete controller additions

1. CROSS_MODAL_CLOSURE: each hard symbolic constraint receives an ID and an observable visual predicate; artifact QA maps visual evidence back to the same ID.
2. GEOMETRY_CHANNEL: when available, encode camera/layout/scale/contact requirements as masks, boxes, depth ordering, landmarks or fixed anchor coordinates rather than prose alone.
3. TRAJECTORY_HEALTH: track cumulative identity drift, protected-region drift, texture/detail degradation and camera/anchor drift across accepted edits.
4. REBASE_TRIGGER: if cumulative drift exceeds threshold, restart from a clean accepted ancestor + immutable canonical identity/physique anchors and replay only still-active deltas.
5. UNVERIFIABLE state: hard constraints that cannot be reliably observed at current scale/resolution are not allowed to silently pass.
6. Continue separate hard axes: IDENTITY, PHYSIQUE, REQUEST_DELTA, CAMERA, SCALE/GEOMETRY, PROTECTED_REGIONS, MATERIAL/REALISM.

## Automation/repository evidence

Repository read and write access worked in this pass. MASTER_DIAGNOSIS remains at its earlier 12:54Z synthesis and does not yet contain the later controller refinements; this is state staleness in the research repository itself. SOURCE_COVERAGE was last updated at 18:16Z before the 19:16Z and current findings, so the coverage ledger also needs refresh. This pass writes the run artifact and updates SOURCE_COVERAGE separately.

## Still unchecked / next high-value work

- Inspect full ROVER paper/ablations for failure decomposition and whether reciprocal verification specifically reduces image-generation constraint failures.
- Read SIGMA-GEN full paper tables/ablations: quantify identity-vs-structure tradeoff and which spatial control granularity matters most.
- Establish practical observability thresholds for face identity at small subject scales and severe viewpoints; ordinary embedding scores may be unreliable.
- Determine whether the active image tool exposes any explicit geometry/mask/reference-role controls; if not, separate controller ideals from implementable controls.
- Build a prototype compiler that turns Project Continuity Rules into constraint IDs + visual predicates and test cousin prompts for identical compiled state.
- Refresh MASTER_DIAGNOSIS after the final scheduled research pass so the master synthesis incorporates later transactional, delta-contract, cross-modal and trajectory-level findings.
