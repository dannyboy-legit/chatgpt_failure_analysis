# Source Coverage Ledger

Updated: 2026-09-15 15:15Z

Purpose: prevent the investigation from repeatedly searching the same few sources while silently leaving entire evidence classes unchecked. A category is not 'covered' merely because one search result was read. Each hourly research pass should add newly checked sources, contradictions, and remaining gaps.

## Evidence grades

- **A — Direct project/runtime evidence:** conversation trajectory, tool outputs/logs, canonical project source documents, generated artifacts.
- **B — Primary scientific/technical evidence:** peer-reviewed paper, primary benchmark paper, official technical documentation/report.
- **C — Primary implementation evidence:** maintainer issue tracker, reproducible bug report, source code, official changelog, or primary preprint awaiting peer review.
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

### Multi-turn structure / evolving intent / state
- LLMs Get Lost in Multi-Turn Conversation (ICLR 2026)
- StructFlowBench (ACL Findings 2025)
- EvolIF / One Battle After Another (ACL 2026)
- MultiChallenge (ACL Findings 2025)
- mtRAG / MTRAG-UN (TACL 2025 / ACL Findings 2026; deeper applicability review pending)
- StateMemBench / Can Agent Memory Systems Track Evolving State? (2026 preprint; abstract/results checked, methods/ablations pending)

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

### Iterative / multi-turn image editing and QA
- FreqEdit: Preserving High-Frequency Features for Robust Multi-Turn Image Editing (CVPR 2026)
- Improving Editability in Image Generation with Layer-wise Memory + Multi-Edit Bench (CVPR 2025)
- AnchorEdit: Maintaining Temporal Consistency in Multi-turn Image Editing via Causal Memory (2026 preprint)
- Banana100: iterative degradation + failure of 21 NR-IQA metrics (2026 preprint)
- ProductConsistency (2026 preprint; product identity, surfaced, deeper review pending)

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

## Automation state

Correction to the 14:16Z note: the deterministic collector was mistakenly sought under `runs/`, but `research.yml` and `collect_sources.py` write timestamped artifacts under `source_queue/`. Direct repository inspection at 15:15Z found multiple queue files from 12:58Z through at least 14:56Z. The collector is operational. The earlier claim that collector artifacts were absent is retracted as an inspection-path error.

Observed timestamps need not equal cron minutes exactly because scheduled workflow dispatch can be delayed. Health should be assessed by continuing source_queue creation/commits and collector content quality, not exact dispatch second.

## Coverage rule

No hourly pass may claim 'nothing new' until it has checked at least one still-uncovered evidence class or attempted to falsify one existing high-confidence mechanism. No conclusion is promoted solely from community anecdotes. Contradictory evidence must be recorded rather than omitted.
