# Source Coverage Ledger

Updated: 2026-09-15 20:16Z

Purpose: prevent repeated searching of the same evidence while leaving categories unchecked. Evidence grades: A direct project/runtime evidence; B peer-reviewed/primary scientific evidence; C primary preprint/implementation evidence; D community evidence; E secondary discovery/context.

## Project-source corpus
Fully/high relevance: Master Project Outline; Susan Character Bible v5 and v4.3; Documentary Cinematography Bible; Realism Bible; Hypothetical Reality Bible v1.1; Beeg Standard; Real Giantess Project Notebook; Project Continuity Rules; Drop-In Prompt Card; Locked Project Rules Template. Structurally useful: Kayla Character Bible Revised.

Still inventory: standalone material-fidelity, anatomy, camera-physics, simplified-rules/addenda not yet independently reconciled; canonical visual reference assets assessed by role; obsolete revisions only for contradiction tracing.

## Scientific/benchmark corpus

### Long-context / state / evolving intent
Lost in the Middle; Context Length Alone Hurts LLM Performance Despite Perfect Retrieval; LIFBench; Context Rot; U-Fold; MT-OSC; LLMs Get Lost in Multi-Turn Conversation; StructFlowBench; EvolIF; MultiChallenge; StateMemBench; SEQUOR.

### Multimodal grounding / cross-modal reasoning
MemLens; Remember-R1; Take-along Visual Conditioning; Learning When to Look; VAPO; Multimodal Retrieval Heads; Visually-Guided Policy Optimization; **ROVER (ICLR 2026): reciprocal cross-modal reasoning, 1,312 human-annotated tasks/1,876 images; interleaved cross-modal systems outperform non-interleaved combinations, showing text-plan quality and image-generation quality do not guarantee correct binding.**; **C3PO (Aug 2026 preprint): cross-modal composition/conflict benchmark; deeper primary-paper validation pending.**; MILR (ICLR 2026, joint image-text latent reasoning; applicability to reference-grounded editing pending).

### Instruction/constraint following and verification
AgentIF; DriftBench; FollowBench; ComplexBench; CFBench; EIFBench; Instruction Hierarchy; NSVIF/VIFBENCH; IF-CRITIC; ManyIH-Bench; IH-Benchmark; VerIH; IH-Challenge; RECAST; Paradoxical Interference; MCJudgeBench; STAIF; IFMTBench; IFEval++; Verify Before You Commit; Agentic Rubrics.

### Agent/tool reliability and recovery
tau-bench; ReliabilityBench; CAR-bench; AgencyBench; GAIA; OSWorld; AgentBoard; Why Do LLM-based Web Agents Fail?; Tool-Reflection-Bench; FAMA; RAFFLES; ParaRecover; CAR/ToolHop-Pro; Fission-GRPO; AgenticRAGTracer; WindowsWorld; LongCLI-Bench; ToolGate; ToolBench-X; ToolMisuseBench.

### Self-correction / feedback
TACL critical survey; ReAct; Reflexion; Self-Refine; automated correction survey; Verify Before You Commit.

### Identity/reference conditioning
WithAnyone; MMIG-Bench; MultiRef; TRACE-Bench; T2I-CompBench; InstantID; PhotoMaker; ConsistentID; Persistent Identity Preservation benchmark (Sep 2026); Selectively Informative Description; ComposeMe; MOSAIC; DynamicID; CogCanvas; DEADiff; InstaFace; Beyond Facial Consistency; **SIGMA-GEN (ICLR 2026; Adobe/UMass): single-pass identity + structural/spatial guidance from coarse boxes through masks/depth; supports explicit geometry channel rather than prose-only layout.**; SpatialID (2026 preprint; spatially adaptive identity injection, deeper validation pending).

### Iterative/multi-turn image editing and QA
FreqEdit (CVPR 2026); Layer-wise Memory + Multi-Edit Bench; AnchorEdit; Banana100; ProductConsistency; VIBE; PIE-Bench; CompBench; GEditBench v2; EdiVal-Agent; RC-GRPO-Editing; MIRAGE; **MT-EditFlow (Apple research, July 2026): treats multi-turn editing as trajectory-level all-or-nothing/error-propagation problem; reports +6.85 turn-3 overall improvement on FLUX.1-Kontext-dev and motivates cumulative trajectory health rather than only per-turn QA.**; IMAGAgent/MTEditBench (primary preprint, constraint-aware plan-execute-reflect; deeper full-paper validation pending).

## Official/product evidence
OpenAI Creating images with ChatGPT; OpenAI Images 2.5 announcement (2026-09-08); OpenAI model/reasoning guidance; image-generation documentation; GitHub/OpenAI tool/automation documentation; Adobe Research SIGMA-GEN official research summary; Apple Machine Learning Research MT-EditFlow page.

## Implementation/community corpus
Checked issue families: reference named/visible but not delivered to image backend; reference requests hang while no-reference controls succeed; repeated failed tool-call loops; missing circuit breakers/duplicate fingerprints. Community expansion still needed: Images 2.5 long-session preservation, recurring-character identity drift, multi-reference contamination, client-specific reference transport, agent retry behavior. Community reports remain anecdotal and never proof of internals.

## Current highest-value falsification tests
1. Compact authoritative state vs raw long thread.
2. Narrative summary vs supersession graph.
3. Nearest-angle single face reference vs multi-view.
4. End-to-end reference pixel transport.
5. Per-constraint artifact QA.
6. pass^k across varied Susan scenes.
7. Retry fingerprint invalidation.
8. Recursive edit vs clean accepted ancestor + canonical anchor.
9. Unrequested-region drift.
10. Anchor/Disentangle/Apply/Compose scoring.
11. Early reference inspection vs late visual re-ground.
12. Text-compressed identity vs immutable pixels + symbolic role state.
13. Accumulated packet vs fresh active-only recompilation after rollback/override.
14. LOCAL_REPAIR vs ROUTE_INVALIDATING replanning.
15. Flat constraints vs authority DAG.
16. Redundant prompts vs normalized packet.
17. Holistic judge vs constraint vector + deterministic gates.
18. Judge stability under neutral perturbations.
19. Cousin prompts → identical normalized action state/reliable@k.
20. PRE_COMMIT_AUDIT vs post-generation-only QA.
21. Transactional COMMIT/ROLLBACK vs immediate mutation.
22. Face + physique hard gates + holistic coherence.
23. Explicit reference→allowed target correspondence map.
24. DELTA_CONTRACT: MUST_CHANGE + MUST_NOT_CHANGE + RECOMPUTE_FROM_CANONICAL.
25. Boundary invariants across CHAT→STATE→TOOL→OUTPUT→QA→COMMIT.
26. **CROSS_MODAL_CLOSURE: symbolic constraint IDs must map to observable visual predicates and artifact evidence must map back to the same IDs.**
27. **GEOMETRY_CHANNEL: prose-only scale/layout vs boxes/masks/depth/landmarks where supported.**
28. **TRAJECTORY_HEALTH + REBASE_TRIGGER: cumulative drift thresholds vs per-turn QA alone.**
29. **UNVERIFIABLE identity state at insufficient pixel scale/viewpoint vs forced PASS/FAIL judgment.**

## Automation/repository state
Deterministic collector has produced source_queue artifacts but previously encountered arXiv timeouts/HTTP 429s; academic discovery remains incomplete. Direct research remains necessary. Repository read/write succeeded at 20:16Z. MASTER_DIAGNOSIS is stale at 12:54Z and should be comprehensively refreshed after the final scheduled research pass rather than patched piecemeal now.

## Coverage rule
No pass may claim no new result until it checks an uncovered evidence class or attempts to falsify a high-confidence mechanism. No conclusion is promoted solely from community anecdotes. Contradictory evidence must be retained.