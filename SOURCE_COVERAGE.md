# Source Coverage Ledger

Updated: 2026-09-15 18:16Z

Purpose: prevent the investigation from repeatedly searching the same few sources while silently leaving entire evidence classes unchecked. A category is not 'covered' merely because one search result was read. Each hourly research pass should add newly checked sources, contradictions, and remaining gaps.

## Evidence grades

- **A — Direct project/runtime evidence:** conversation trajectory, tool outputs/logs, canonical project source documents, generated artifacts.
- **B — Primary scientific/technical evidence:** peer-reviewed paper, primary benchmark paper, official technical documentation/report.
- **C — Primary implementation/preprint evidence:** maintainer issue tracker, reproducible bug report, source code, official changelog, or primary preprint awaiting peer review.
- **D — Community evidence:** forums, Reddit, user reports, discussions. Useful for finding repeated patterns, never sufficient by itself to assert model internals.
- **E — Secondary commentary:** articles, summaries, opinion/analysis. Use mainly to discover primary sources or contextualize them.

## Project-source corpus

### Fully read / highest relevance
- Master Project Outline
- Susan Character Bible v5
- Susan Character Bible v4.3
- Documentary Cinematography Bible, consolidated/re-capture version
- Realism Bible
- Hypothetical Reality Bible v1.1
- The Beeg Standard
- Real Giantess Project Notebook
- Project Continuity Rules
- Drop-In Prompt Card
- Locked Project Rules Template

### Structurally useful cross-character documents
- Kayla Character Bible Revised

### Still to inventory/check
- Older/duplicate project-document revisions for contradictions not superseded by latest authority
- Any standalone material-fidelity, anatomy, camera-physics, simplified-rules or addendum files not surfaced by current semantic retrieval
- Visual reference assets themselves, assessed by assigned role

## Scientific/benchmark corpus

### Long-context / context utilization
- Lost in the Middle
- Context Length Alone Hurts LLM Performance Despite Perfect Retrieval
- LIFBench
- Context Rot technical experiments
- ACON / context optimization work
- long-horizon context-management work
- U-Fold (ACL Findings 2026)
- MT-OSC (ACL Findings 2026)
- Chain-of-Interactions dialogue summarization

### Multimodal long-context / visual forgetting
- MemLens
- Remember-R1
- Take-along Visual Conditioning
- Learning When to Look
- More Thought, Less Accuracy? / VAPO
- Multimodal Retrieval Heads in Long-Context VLMs
- Visually-Guided Policy Optimization (ACL 2026)

### Multi-turn structure / evolving intent / state
- LLMs Get Lost in Multi-Turn Conversation (ICLR 2026)
- StructFlowBench
- EvolIF
- MultiChallenge
- mtRAG / MTRAG-UN
- StateMemBench
- SEQUOR

### Instruction and constraint following / verification
- AgentIF
- DriftBench / Models Recall What They Violate
- FollowBench
- ComplexBench
- CFBench
- EIFBench
- Instruction Hierarchy
- NSVIF + VIFBENCH
- IF-CRITIC (ACL 2026)
- ManyIH-Bench
- IH-Benchmark
- Reasoning Up the Instruction Ladder / VerIH
- IH-Challenge
- RECAST
- On the Paradoxical Interference between Instruction-Following and Task Solving
- MCJudgeBench
- STAIF
- IFMTBench
- MDP-GRPO
- **IFEval++ / Revisiting the Reliability of Language Models in Instruction-Following (ACL 2026): cousin-prompt reliability; up to 61.8% degradation under nuanced modifications; motivates reliable@k-style testing.**
- **Verify Before You Commit (ACL 2026): pre-commit adversarial auditing + constraint-guided minimal repair under verifiable acceptance criteria.**
- **Agentic Rubrics as Contextual Verifiers (ACL 2026): newly surfaced; deeper applicability to visual/project-state rubrics pending.**

### Agent/tool reliability and recovery
- tau-bench
- ReliabilityBench
- CAR-bench
- AgencyBench
- GAIA
- OSWorld
- AgentBoard
- Why Do LLM-based Web Agents Fail?
- Tool-Reflection-Bench
- FAMA
- RAFFLES
- ParaRecover
- CAR / ToolHop-Pro
- Fission-GRPO
- AgenticRAGTracer
- WindowsWorld
- LongCLI-Bench
- **ToolGate (Findings ACL 2026): contract-grounded verified execution; symbolic state changes only through verified tool execution. Supports transactional COMMIT/ROLLBACK state.**

### Self-correction / feedback
- TACL critical survey on self-correction
- ReAct
- Reflexion
- Self-Refine
- automated correction survey
- Verify Before You Commit (cross-listed: pre-commit auditing rather than unconstrained intrinsic reflection)

### Image identity / reference conditioning
- WithAnyone
- MMIG-Bench
- MultiRef
- TRACE-Bench
- T2I-CompBench
- InstantID
- PhotoMaker
- ConsistentID
- Persistent Identity Preservation benchmark/preprint
- Selectively Informative Description / undesired embedding entanglement
- ComposeMe
- MOSAIC multi-subject alignment/disentanglement (2025 preprint; now reviewed for explicit semantic correspondence + orthogonal reference disentanglement)
- DynamicID
- CogCanvas
- DEADiff
- InstaFace
- **Beyond Facial Consistency: Personalized Person Image Generation with Holistic Identity Preservation (2026 preprint): local face vs global appearance tradeoff; dynamic/region-aware coordination; Pexels-100 benchmark.**

### Iterative / multi-turn image editing and QA
- FreqEdit
- Layer-wise Memory + Multi-Edit Bench
- AnchorEdit
- Banana100
- ProductConsistency
- VIBE

## Official documentation / product evidence
- OpenAI: Creating images with ChatGPT
- OpenAI: Introducing ChatGPT Images 2.5 (2026-09-08)
- OpenAI current model/reasoning guidance
- OpenAI current image-generation documentation
- GitHub/OpenAI documentation for image/tool transport and automation

## Implementation/community corpus

### Checked implementation issue families
- reference image visible/named but not delivered to image generation backend
- reference-image requests hang while no-reference controls succeed
- repeated identical/near-identical failed tool-call loops
- missing circuit breakers / duplicate-call fingerprints

### Forum/community areas still to expand
- recurring-character identity drift experiences
- multi-reference identity-versus-expression contamination
- long-session instruction drift
- image edit/reference transport failures across client surfaces
- agent loop/retry behavior in major agent frameworks
- current Images 2.5 reports specifically testing claimed multi-turn preservation improvements

## Current highest-value falsification tests

1. Compact authoritative state vs raw long-thread context.
2. Narrative summary vs explicit supersession/state graph.
3. Nearest-angle single face reference vs multiple face references.
4. Verify reference pixel transport end-to-end.
5. Independent constraint/artifact QA.
6. pass^k across varied Susan scenes.
7. Invalidate exact retry fingerprints.
8. Recursive edit-from-latest vs last-accepted-base + immutable canonical anchor.
9. Measure unrequested-region drift separately.
10. Score multi-reference tasks by Anchor/Disentangle/Apply/Compose.
11. Early-only reference inspection vs late visual re-ground.
12. Text-compressed identity vs immutable canonical pixels + symbolic role state.
13. Accumulated execution packet vs freshly recompiled active-only packet after override/rollback.
14. LOCAL_REPAIR vs ROUTE_INVALIDATING forced replanning.
15. Flat constraint lists vs explicit authority DAG.
16. Maximal/redundant prompts vs normalized non-redundant packets.
17. Holistic visual QA vs per-constraint PASS/PARTIAL/FAIL with deterministic gates.
18. Judge stability under neutral perturbations.
19. **Semantic-equivalent cousin prompts: same intended Susan task should compile to the same normalized action state and retain reliable@k performance.**
20. **PRE_COMMIT_AUDIT vs post-generation-only QA: measure prevented invalid generations and false-rejection cost.**
21. **Transactional COMMIT/ROLLBACK state vs immediate mutation after tool calls.**
22. **Hard face + physique gates plus HOLISTIC_CHARACTER_COHERENCE vs face/physique-only QA.**
23. **Explicit reference correspondence map (reference→allowed target attributes/regions) vs generic role prose.**

## Automation state

The deterministic collector is producing source_queue files; earlier inspection found arXiv timeouts/HTTP 429s while GitHub issue collection continued. Academic discovery is therefore degraded and incomplete even though the workflow is alive. Direct hourly research remains required.

Repository read/write access was verified during the 18:16Z pass, and a new research artifact was committed successfully.

## Coverage rule

No hourly pass may claim 'nothing new' until it has checked at least one still-uncovered evidence class or attempted to falsify one existing high-confidence mechanism. No conclusion is promoted solely from community anecdotes. Contradictory evidence must be recorded rather than omitted.
