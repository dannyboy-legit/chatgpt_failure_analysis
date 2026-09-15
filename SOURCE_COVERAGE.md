# Source Coverage Ledger

Updated: 2026-09-15 17:18Z

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
- Kayla Character Bible Revised (reference-role separation, variation/identity distinction, material/anatomy/scale QA)

### Still to inventory/check
- Older/duplicate project-document revisions for contradictions not superseded by latest authority
- Any standalone material-fidelity, anatomy, camera-physics, simplified-rules or addendum files not surfaced by current semantic retrieval
- Visual reference assets themselves, assessed by assigned role (face vs physique), not as scene templates

## Scientific/benchmark corpus

### Long-context / context utilization
- Lost in the Middle
- Context Length Alone Hurts LLM Performance Despite Perfect Retrieval
- LIFBench
- Context Rot technical experiments
- ACON / context optimization work
- long-horizon context-management work
- U-Fold: Dynamic Intent-Aware Context Folding for User-Centric Agents (ACL Findings 2026)
- MT-OSC: One-off Sequential Condensation (ACL Findings 2026)
- Chain-of-Interactions dialogue summarization (EMNLP Findings 2025; deeper methods review pending)

### Multimodal long-context / visual forgetting
- MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models (2026 preprint; abstract/results checked, methods/ablations pending)
- Remember-R1: Mitigating Long-Context Visual Forgetting through Reinforcement Learning (2026 preprint; abstract checked, attention/ablation details pending)
- Take-along Visual Conditioning for Multi-modal Long CoT Reasoning (2025 preprint; key image-removal ablation checked)
- Learning When to Look / strategic perception (2025 preprint; surfaced, deeper review pending)
- More Thought, Less Accuracy? / VAPO (2025 preprint; surfaced, deeper review pending)
- Multimodal Retrieval Heads in Long-Context VLMs (2026 preprint; surfaced, causal masking result checked at abstract level)
- Visually-Guided Policy Optimization (ACL 2026; peer-reviewed corroboration of temporal visual forgetting and visual-attention reinforcement)

### Multi-turn structure / evolving intent / state
- LLMs Get Lost in Multi-Turn Conversation (ICLR 2026)
- StructFlowBench (ACL Findings 2025)
- EvolIF / One Battle After Another (ACL 2026)
- MultiChallenge (ACL Findings 2025)
- mtRAG / MTRAG-UN (TACL 2025 / ACL Findings 2026; deeper applicability review pending)
- StateMemBench / Can Agent Memory Systems Track Evolving State? (2026 preprint; abstract/results checked, methods/ablations pending)
- SEQUOR: A Multi-Turn Benchmark for Realistic Constraint Following (2026 preprint; full web text substantially reviewed: Single/Tuples/Add/Replace/Everything regimes and judge validation)

### Instruction and constraint following / verification
- AgentIF
- DriftBench / Models Recall What They Violate
- FollowBench
- ComplexBench
- CFBench
- EIFBench
- Instruction Hierarchy
- NSVIF + VIFBENCH / Neuro-Symbolic Verification on Instruction Following (Microsoft Research / 2026 preprint)
- IF-CRITIC (ACL 2026; surfaced, deeper comparison with NSVIF pending)
- Many-Tier Instruction Hierarchy / ManyIH-Bench (2026 preprint; up to 12 privilege levels; ~40% frontier accuracy reported; full ablations pending)
- IH-Benchmark (2026 preprint; 44 constraint families, system-user and user-tool conflicts; hierarchy robustness varies strongly by conflict surface)
- Reasoning Up the Instruction Ladder / VerIH (Findings ACL 2026; explicit hierarchy reasoning gives ~20% absolute conflict-setting improvement)
- IH-Challenge (OpenAI-led 2026 preprint/dataset; GPT-5-Mini hierarchy robustness reported +10 points across 16 evals)
- RECAST (ICLR 2026; multi-constraint training beyond 10 constraints; automatic verification)
- On the Paradoxical Interference between Instruction-Following and Task Solving (2026 preprint; self-evident added constraints can reduce task performance; deeper review pending)
- MCJudgeBench (2026 preprint; constraint-level judge correctness and stability are distinct; partial/no detection remains difficult)
- STAIF (2026 preprint; separates soft and hard constraint optimization)
- IFMTBench (2026 preprint; deterministic gating + continuous rubric scoring, multiplicative combination)
- MDP-GRPO (ACL 2026; strict multi-constraint satisfaction and violation-sensitive optimization)

### Agent/tool reliability and recovery
- tau-bench
- ReliabilityBench
- CAR-bench
- AgencyBench
- GAIA
- OSWorld
- AgentBoard
- Why Do LLM-based Web Agents Fail?
- Tool-Reflection-Bench / structured reflection
- FAMA
- RAFFLES
- ParaRecover (index surfaced; original manuscript still requires direct verification)
- CAR / ToolHop-Pro: Dynamic Tool Synthesis + Global Trajectory Rectification (Findings ACL 2026; abstract/motivation checked)
- Fission-GRPO: Learning to Recover from Execution Errors (ACL 2026; abstract/results checked)
- AgenticRAGTracer (Findings ACL 2026; surfaced: collapse vs over-extension failure diagnosis, deeper review pending)
- WindowsWorld (Findings ACL 2026; surfaced, deeper review pending)
- LongCLI-Bench (Findings ACL 2026; surfaced, deeper review pending)

### Self-correction / feedback
- TACL critical survey on self-correction
- ReAct
- Reflexion
- Self-Refine
- automated correction survey

### Image identity / reference conditioning
- WithAnyone
- MMIG-Bench
- MultiRef
- TRACE-Bench: Decomposing and Diagnosing Multi-Reference Image Generation (2026 preprint; abstract/operator result checked, full diagnostic tree pending)
- T2I-CompBench
- InstantID
- PhotoMaker
- ConsistentID
- Persistent Identity Preservation benchmark/preprint
- Selectively Informative Description / undesired embedding entanglement (CVPR 2024)
- ComposeMe: Attribute-Specific Image Prompts (SIGGRAPH Asia 2025 / arXiv)
- MOSAIC multi-subject alignment/disentanglement (2025 preprint; surfaced, deeper review pending)
- DynamicID (ICCV 2025; surfaced, deeper review pending)
- CogCanvas (2026 preprint; surfaced, deeper review pending)
- DEADiff reference style/semantic disentanglement (CVPR 2024; relevant analogy, not identity-specific)
- InstaFace (IEEE FG 2026; single-image identity preservation with separate expression/pose/lighting control; deeper methods review pending)

### Iterative / multi-turn image editing and QA
- FreqEdit: Preserving High-Frequency Features for Robust Multi-Turn Image Editing (CVPR 2026)
- Improving Editability in Image Generation with Layer-wise Memory + Multi-Edit Bench (CVPR 2025)
- AnchorEdit: Maintaining Temporal Consistency in Multi-turn Image Editing via Causal Memory (2026 preprint)
- Banana100: iterative degradation + failure of 21 NR-IQA metrics (2026 preprint)
- ProductConsistency (2026 preprint; product identity, surfaced, deeper review pending)
- VIBE: Visual Instruction Benchmark for Image Editing (Microsoft / 2026 preprint; visual-instruction performance degrades with task difficulty; task-specific LMM judging)

## Official documentation / product evidence
- OpenAI: Creating images with ChatGPT (multiple-reference guidance and explicit reference roles)
- OpenAI: Introducing ChatGPT Images 2.5 (2026-09-08; subject preservation, focused edits, multi-turn consistency claims)
- OpenAI current model/reasoning guidance (outcome-first prompts, stopping criteria, higher reasoning not automatically better)
- OpenAI current image-generation model documentation where relevant
- GitHub/OpenAI documentation for image/tool transport and current automation capabilities

## Implementation/community corpus

### Checked implementation issue families
- reference image is visible/named but not delivered to image generation backend
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

1. Compare compact authoritative state vs raw long-thread context on the same Susan task.
2. Compare narrative summary vs explicit supersession/state graph on the same revised multi-turn task.
3. Compare nearest-angle single face reference vs multiple face references for identity fidelity and expression/pose freedom.
4. Verify reference pixel transport end-to-end using an unmistakable reference-control marker.
5. Run independent constraint/artifact QA rather than asking the generator to approve itself.
6. Measure pass^k across varied Susan scenes rather than judging one successful generation.
7. Invalidate and refuse exact retry fingerprints after a failed generation/tool call.
8. Compare recursive edit-from-latest against edit-from-last-accepted-base + immutable canonical identity anchor.
9. Measure unrequested-region drift separately from requested edit success.
10. Score multi-reference tasks by Anchor/Disentangle/Apply/Compose operators rather than one holistic quality score.
11. Compare early-only reference inspection against a late visual re-ground immediately before generation.
12. Compare text-compressed identity state against immutable retrievable canonical pixels + symbolic role state.
13. Compare an accumulated execution packet against a freshly recompiled active-only packet after override/rollback.
14. Classify failed routes as LOCAL_REPAIR vs ROUTE_INVALIDATING and measure whether forced global replanning reduces repeated failures.
15. Compare flat constraint lists against an explicit authority DAG on tasks containing source conflicts.
16. Compare maximal/redundant action prompts against normalized non-redundant action packets while keeping all hard requirements semantically equivalent.
17. Compare holistic visual QA against per-constraint PASS/PARTIAL/FAIL QA with deterministic gates where possible.
18. Test judge stability under semantically neutral prompt/artifact perturbations before trusting a semantic QA axis.

## Automation state

The deterministic collector is producing source_queue files through at least 2026-09-15 15:54Z, so its scheduler/commit path remains operational. However, the inspected 15:54Z queue recorded eight arXiv collection errors in one pass (read timeouts and HTTP 429 responses), while GitHub issue collection continued. Academic discovery is therefore degraded and incomplete even though the workflow itself is alive.

Do not use collector output as a completeness claim. Direct hourly research remains required. Candidate collector improvements to inspect before changing code: exponential backoff/jitter, query staggering, caching/deduplication, and bounded retries.

## Coverage rule

No hourly pass may claim 'nothing new' until it has checked at least one still-uncovered evidence class or attempted to falsify one existing high-confidence mechanism. No conclusion is promoted solely from community anecdotes. Contradictory evidence must be recorded rather than omitted.
