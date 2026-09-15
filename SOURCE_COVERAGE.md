# Source Coverage Ledger

Updated: 2026-09-15

Purpose: prevent the investigation from repeatedly searching the same few sources while silently leaving entire evidence classes unchecked. A category is not 'covered' merely because one search result was read. Each hourly research pass should add newly checked sources, contradictions, and remaining gaps.

## Evidence grades

- **A — Direct project/runtime evidence:** conversation trajectory, tool outputs/logs, canonical project source documents, generated artifacts.
- **B — Primary scientific/technical evidence:** peer-reviewed paper, primary benchmark paper, official technical documentation/report.
- **C — Primary implementation evidence:** maintainer issue tracker, reproducible bug report, source code, official changelog.
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

### Instruction and constraint following
- AgentIF
- DriftBench / Models Recall What They Violate
- FollowBench
- ComplexBench
- CFBench
- EIFBench
- Instruction Hierarchy

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
- T2I-CompBench
- InstantID
- PhotoMaker
- ConsistentID
- Persistent Identity Preservation benchmark/preprint

## Official documentation / product evidence
- OpenAI: Creating images with ChatGPT (multiple-reference guidance and explicit reference roles)
- OpenAI current model/reasoning guidance (outcome-first prompts, stopping criteria, higher reasoning not automatically better)
- OpenAI current image-generation capability/release material where relevant
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

## Current highest-value falsification tests

1. Compare compact authoritative state vs raw long-thread context on the same Susan task.
2. Compare nearest-angle single face reference vs multiple face references for identity fidelity and expression/pose freedom.
3. Verify reference pixel transport end-to-end using an unmistakable reference-control marker.
4. Run independent artifact QA rather than asking the generator to approve itself.
5. Measure pass^k across varied Susan scenes rather than judging one successful generation.
6. Invalidate and refuse exact retry fingerprints after a failed generation/tool call.

## Coverage rule

No hourly pass may claim 'nothing new' until it has checked at least one still-uncovered evidence class or attempted to falsify one existing high-confidence mechanism. No conclusion is promoted solely from community anecdotes. Contradictory evidence must be recorded rather than omitted.
