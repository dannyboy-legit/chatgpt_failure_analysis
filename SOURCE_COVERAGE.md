# Source Coverage Ledger

Updated: 2026-09-15 22:19Z

Purpose: prevent repeated searching while retaining unchecked categories. Evidence grades: A direct project/runtime evidence; B peer-reviewed/primary scientific evidence; C primary preprint/implementation evidence; D community evidence; E secondary discovery/context.

## Project-source corpus
Fully/high relevance: Master Project Outline; Susan Character Bible v5 and v4.3; Documentary Cinematography Bible including UPDATED v2 re-capture layer; Realism Bible; Hypothetical Reality Bible v1.1; Beeg Standard; Real Giantess Project Notebook; Project Continuity Rules; Drop-In Prompt Card; Locked Project Rules Template; Susan Dynamic Scale Addendum.

**New contradiction inventory:** Susan v5 says scale changes absolute size only and is independent from physique; the older Dynamic Scale Addendum says growth proportionally develops physique and still names Chloe-based face references. This is direct evidence that semantically relevant retrieval can surface stale/contradictory project authority. Superseded sources must be historical-only unless explicitly reactivated.

Still inventory: standalone Anatomy Addendum and Simplified Rules if separately stored under non-obvious filenames; canonical visual reference assets assessed by role; obsolete revisions only for contradiction tracing.

## Scientific/benchmark corpus

### Long-context / state / evolving intent
Lost in the Middle; Context Length Alone Hurts LLM Performance Despite Perfect Retrieval; LIFBench; Context Rot; U-Fold; MT-OSC; LLMs Get Lost in Multi-Turn Conversation; StructFlowBench; EvolIF; MultiChallenge; StateMemBench; SEQUOR.

### Multimodal grounding / cross-modal reasoning
MemLens; Remember-R1; Take-along Visual Conditioning; Learning When to Look; VAPO; Multimodal Retrieval Heads; Visually-Guided Policy Optimization (ACL 2026); Look Light, Think Heavy (ACL 2026); ROVER (ICLR 2026); C3PO; MILR. New synthesis: long CoT is not assumed beneficial for perception-heavy gates; direct/late visual grounding needs its own budget and verification.

### Instruction/constraint following and verification
AgentIF; DriftBench; FollowBench; ComplexBench; CFBench; EIFBench; Instruction Hierarchy; NSVIF/VIFBENCH; IF-CRITIC; ManyIH-Bench; IH-Benchmark; VerIH; IH-Challenge; RECAST; Paradoxical Interference; MCJudgeBench; STAIF; IFMTBench; IFEval++; Verify Before You Commit; Agentic Rubrics.

### Agent/tool reliability and recovery
tau-bench; ReliabilityBench; CAR-bench; AgencyBench; GAIA; OSWorld; AgentBoard; Why Do LLM-based Web Agents Fail?; Tool-Reflection-Bench; FAMA; RAFFLES; ParaRecover; CAR/ToolHop-Pro; Fission-GRPO; AgenticRAGTracer; WindowsWorld; LongCLI-Bench; ToolGate; ToolBench-X; ToolMisuseBench; AgentProp-Bench. New synthesis: pre-action rejection and post-fault recovery are distinct capabilities and must be measured separately.

### Self-correction / feedback
TACL critical survey; ReAct; Reflexion; Self-Refine; automated correction survey; Verify Before You Commit.

### Identity/reference conditioning
WithAnyone; MMIG-Bench; MultiRef; TRACE-Bench (ACM MM 2026); T2I-CompBench; InstantID; PhotoMaker; ConsistentID; Persistent Identity Preservation benchmark; Selectively Informative Description; ComposeMe; MOSAIC; DynamicID; CogCanvas; DEADiff; InstaFace; Beyond Facial Consistency; SIGMA-GEN; SpatialID; generalized multi-image editing with explicit per-image latent separation/indexing.

### Iterative/multi-turn image editing and QA
FreqEdit; Layer-wise Memory + Multi-Edit Bench; AnchorEdit; Banana100; ProductConsistency; VIBE; PIE-Bench; CompBench; GEditBench v2; EdiVal-Agent; RC-GRPO-Editing; MIRAGE; MT-EditFlow; IMAGAgent/MTEditBench.

## Official/product evidence
OpenAI Creating images with ChatGPT; OpenAI Images 2.5 announcement (2026-09-08); OpenAI model/reasoning guidance; image-generation documentation; Adobe Research SIGMA-GEN official summary; Apple MT-EditFlow page.

## Implementation/community corpus
Checked issue families: reference named/visible but not delivered to image backend; reference requests hang while no-reference controls succeed; repeated failed tool-call loops; missing circuit breakers/duplicate fingerprints. Community reports remain anecdotal and never proof of internals.

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
26. CROSS_MODAL_CLOSURE: symbolic constraint IDs ↔ observable visual predicates.
27. GEOMETRY_CHANNEL: prose-only vs boxes/masks/depth/landmarks where supported.
28. TRAJECTORY_HEALTH + REBASE_TRIGGER.
29. UNVERIFIABLE identity state at insufficient pixel scale/viewpoint.
30. PROVENANCE_IR + AUTHORITY_REBINDING negative controls.
31. SOURCE_TO_IR_VALIDATION.
32. **SOURCE_VERSION_GATE: v5 + stale Dynamic Scale Addendum must compile to v5 authority, not merged contradiction.**
33. **TYPED_INVARIANCE: semantic/geometric preservation while allowing legitimate photometric recapture.**
34. **PERCEPTION_BUDGET: short direct visual grounding vs extended CoT for identity/reference gates.**
35. **REJECTION_SCORE vs RECOVERY_SCORE as separate reliability axes.**

## Automation/repository state
Deterministic collector produced source_queue artifacts but encountered arXiv timeouts/HTTP 429s in some passes; academic discovery was incomplete and direct research remained necessary. Repository read/write succeeded through the final scheduled pass. MASTER_DIAGNOSIS was stale at 12:54Z and is being comprehensively refreshed from the accumulated runs rather than patched piecemeal.

## Coverage rule
No conclusion is promoted solely from community anecdotes. Contradictory evidence is retained. Superseded project sources remain visible for contradiction tracing but are not active authority.