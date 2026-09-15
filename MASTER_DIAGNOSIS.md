# Master Diagnosis

Updated: 2026-09-15T12:54Z

This document separates observed failures from plausible mechanisms. It does not claim access to private model internals. Mechanisms are ranked by how directly they are supported by the conversation/project evidence and external research.

## 1. Strongest supported mechanisms

### A. Source authority is documented but not reliably converted into action gates — HIGH confidence

The Real Giantess project documents already specify a modular authority system: Susan's canonical face references govern facial identity; physique references govern body anatomy/silhouette; scene instructions govern pose, expression, hairstyle arrangement, environment, camera and related variation. Susan Character Bible v5 explicitly says reference images are guides rather than pasted assets, that facial identity is invariant to hairstyle/pose/lighting/expression, and that the nearest facial/physique reference should be selected by camera angle. The observed workflow repeatedly knew these rules yet generated before enforcing them.

This is more consistent with an execution/control failure than with missing instructions. The corrective mechanism must therefore be structural: compile source rules into machine-checkable preconditions before generation rather than merely restating them in prose.

### B. Declarative recall can dissociate from behavioral adherence — HIGH confidence

The conversation repeatedly shows the assistant accurately restating a constraint after violating it, including reference roles, wallpaper aspect ratio, identity preservation and GitHub access state. This pattern is independently consistent with 2026 DriftBench results ('Models Recall What They Violate'), which report a knows-but-violates phenomenon: models can restate constraints they fail to obey during iterative work.

Implication: asking the same model whether it understands the rule is not a meaningful control. Verification must inspect the planned action or resulting artifact.

### C. Long, constraint-heavy agent contexts are intrinsically fragile — HIGH confidence as a general mechanism; MEDIUM as the cause of any single Susan failure

AgentIF (NeurIPS 2025) evaluates realistic agent prompts averaging 1,723 words and 11.9 constraints and finds major failures particularly around complex constraint structures and tool specifications. Lost in the Middle, Chroma's Context Rot experiments, LIFBench, and later work show that long input length, position and distractors can reduce effective use of relevant information even within nominal context windows. A 2025 EMNLP paper further reports performance degradation from sheer input length even when relevant evidence is perfectly retrieved.

The Susan thread contains long accumulated history, multiple project versions, tool schemas, generated failures and repeated restatements. That makes raw full-context dependence a poor reliability strategy. The correction is not simply 'use a bigger context window'; it is to distill an authoritative working state immediately before action.

### D. Reference identity and scene variation are separate objectives; over-conditioning can cause copy-paste behavior — HIGH confidence

WithAnyone (ICLR 2026) explicitly identifies a copy-paste failure in identity-consistent generation: reconstruction-driven systems may reproduce the reference face rather than preserve identity across natural pose, expression or lighting changes. This closely matches the user's complaint that a Susan face reference must define who she is, not freeze expression, hairstyle or head posture.

The correct target is identity invariance + contextual variation. Face geometry is a hard identity constraint; expression/head orientation/hair arrangement are separately synthesized from the scene.

### E. Multi-reference conditioning is itself difficult and needs explicit role separation — HIGH confidence as a general image-generation limitation

MultiRef (ACM MM 2025) reports that even strong systems degrade on multi-reference conditioning relative to single-reference tasks. MMIG-Bench (NeurIPS 2025) evaluates identity preservation separately from prompt-image alignment and visual artifacts. This supports decomposing Susan's references by role and evaluating each dimension separately rather than supplying a large undifferentiated bundle of images.

### F. Reference availability in the reasoning context does not prove pixel conditioning reached the image backend — MEDIUM-HIGH confidence as a tool-path risk

The conversation contains an actual earlier mismatch between being able to inspect Library images and being unable to materialize/pass them as raw image inputs. Public OpenAI Codex issue #30121 describes a similar class of failure where a reference file exists and is named in the prompt, but the image-generation backend does not receive its pixels and produces an unrelated image.

This issue report is not evidence that the exact same Codex regression caused the ChatGPT failure. It is evidence that end-to-end reference transfer is a distinct precondition that must be verified. The workflow should fail closed if a required reference cannot be attached as a visual input.

### G. Intrinsic self-critique is not a sufficient QA mechanism — HIGH confidence

A TACL 2024 critical survey of LLM self-correction finds little evidence for reliable prompted intrinsic self-correction except in unusually suitable tasks, while reliable external feedback materially improves correction. In the conversation, prose explanations of what went wrong frequently preceded another similar failure.

Therefore post-generation QA must be grounded in observable artifact checks and hard acceptance criteria, not only the generator's own narrative confidence.

### H. Retry loops need runtime enforcement, not more reminders — HIGH confidence

The conversation repeatedly regenerated after failure without materially changing the plan. Multiple independent 2026 agent implementation issues report the same family of behavior: identical or near-identical failed tool calls continue despite textual warnings, and developers propose call fingerprints, bounded retries and hard circuit breakers.

These implementation reports do not establish ChatGPT's internal architecture. They do strongly support a controller principle: warnings are weaker than enforcement. A failed generation should invalidate its exact plan fingerprint. The same plan must not run again without a material change.

### I. Premature action and unsupported capability claims are a recurring agent reliability failure — HIGH confidence

CAR-bench (ACL 2026) finds frontier reasoning models below 50% on disambiguation tasks due to premature actions and documents fabrication/policy violations when tools or information are missing. In this conversation the assistant generated before resolving reference transport, and later asserted an interactive GitHub authorization problem before checking repository access. This mechanism is directly observable here.

Corrective control: action is prohibited until required state/tool claims have been empirically checked in the current run.

### J. Single-run success is not evidence of a reliable workflow — HIGH confidence

Tau-bench introduced pass^k to capture consistency over repeated trials and found state-of-the-art function-calling agents below 50% task success with pass^8 below 25% in retail. ReliabilityBench extends this idea to repeated execution, semantic perturbation and injected tool faults. A Susan workflow that produces one good image after several failures has not demonstrated reliability.

The project needs repeated-trial metrics across intentionally varied scenes, poses, expressions, lighting and scale while identity/physique remain fixed.

## 2. Weakened or rejected explanations

- **'The instructions were missing.'** Rejected for the core Susan failures. The latest Character Bible and other project documents already encode the necessary role separation and preservation rules.
- **'More prose reminders will solve it.'** Strongly weakened. Both the conversation and instruction-following research show that explicit constraints can be recalled yet violated.
- **'A bigger context window alone solves continuity.'** Rejected. Long-context research shows nominal capacity and effective use are different.
- **'If the model can see/reference a file, image generation must be conditioned on it.'** Rejected as an assumption. End-to-end tool transport requires verification.
- **'The same model's self-critique is enough to approve its own output.'** Strongly weakened; external/observable feedback is needed.
- **'A successful image proves the system is fixed.'** Rejected; reliability must be measured over repeated varied trials.

## 3. Corrective controller

Before an image/tool action, compile a small authoritative state object from sources rather than relying on the entire chat. It must contain: goal, canonical identity authority, physique authority, scene-variable authority, protected invariants, requested variables, tool prerequisites, tool-input proof, and hard acceptance tests.

For Susan specifically:

1. **Identity state:** choose one nearest-angle canonical face reference for geometry only. Explicitly mark expression, gaze, hairstyle arrangement and head posture as scene variables unless the user locks them.
2. **Physique state:** choose one nearest-angle physique reference for anatomy/silhouette only. Do not allow face, clothing or scene composition to bleed from this reference.
3. **Scene state:** independently design pose/expression/gaze/hair from what Susan is doing and from composition needs. This is where novelty belongs.
4. **Reference transport gate:** prove the chosen visual references are actual image inputs to the generator. A filename, Library lookup or textual description is not proof. If visual transport is unavailable, stop rather than silently degrade to prompt-only generation.
5. **Wallpaper gate:** verify landscape target/aspect ratio and composition/negative space before generation.
6. **One generation attempt:** record a fingerprint of references + role map + scene plan + camera + scale + prompt. Do not repeat the same fingerprint after failure.
7. **Artifact QA:** independently score at least identity, physique, expression/head/hair variation, pose mechanics, scale geometry, camera realism, material realism, wallpaper composition and unrequested changes. Any hard-axis failure rejects the result regardless of overall attractiveness.
8. **Repair selection:** diagnose the earliest failed layer (source state, reference transport, prompt binding, generation, QA) and modify that layer only. Do not add generic prompt volume as the default fix.
9. **Reliability logging:** record pass/fail by dimension across varied scenes. Track repeatability rather than anecdotal best cases.

## 4. Current external evidence set

Primary/peer-reviewed or primary technical sources currently examined include: Susan Character Bible v5 and the Real Giantess project realism/cinematography/continuity documents; AgentIF; Lost in the Middle; Context Rot; LIFBench; Context Length Alone Hurts LLM Performance Despite Perfect Retrieval; FollowBench; ComplexBench; CFBench; EIFBench; tau-bench; GAIA; OSWorld; AgentBoard; ReliabilityBench; CAR-bench; AgencyBench; ReAct; Reflexion; Self-Refine; the TACL critical survey of self-correction; FAMA; Tool-Reflection-Bench; WithAnyone; MMIG-Bench; MultiRef; T2I-CompBench; InstantID; PhotoMaker; ConsistentID; and the September 2026 Persistent Identity Preservation benchmark.

Supporting implementation/community evidence includes public issue reports on image-reference transfer failures and repeated tool-call loops. These are treated as anecdotes/implementation evidence, not proof of ChatGPT internals.

## 5. Unresolved questions / next experiments

- Quantify how much a compact authority-state summary improves compliance compared with raw full-thread context for the same Susan task.
- Test one face reference vs several face references while holding scene constant, measuring both identity fidelity and copy-paste/variation.
- Test whether selecting the nearest-angle reference outperforms supplying all facial views simultaneously.
- Separate reference-transport failure from model identity-generation failure using an unmistakable visual marker/reference-control experiment.
- Build a pass^k Susan benchmark: same identity/physique across at least 8 materially different scene conditions.
- Evaluate whether an independent visual QA pass catches identity/physique failures before user intervention more reliably than generator self-critique.
- Continue searching new academic work, official documentation, implementation issues and forum reports for contradictory evidence and alternative mechanisms.

## 6. Research automation state

The original GitHub worker failed because it used the retired GitHub Models inference endpoint and received HTTP 410. It has been replaced with a deterministic quarter-hour source collector that gathers fresh arXiv and GitHub issue candidates without outsourcing reasoning to Copilot. An hourly ChatGPT task now performs the analysis itself, is instructed to read primary sources deeply, re-check the project source documents, falsify prior hypotheses, track uncovered areas and update the research state when repository tools are available. The :15 GitHub workflow now builds a mechanical source index instead of calling the retired model endpoint.
