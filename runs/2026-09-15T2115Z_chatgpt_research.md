# Iterative Research Pass — 2026-09-15 21:15Z

## New finding: constraint provenance must survive every transformation

The prior controller tracked authority, constraints, transactional state, cross-modal closure, and boundary invariants. This pass finds a more precise missing mechanism: **per-field provenance**. It is not enough for the final compiled packet to contain the right value; the controller must know which authoritative source licensed that value and prevent later evidence/tool output from silently rebinding its authority.

### External evidence

**TraceGrant (arXiv 2608.21126, Aug 2026; primary preprint, evidence grade C)** establishes a task-effect Contract before execution, permits runtime evidence only to instantiate authority already granted by that Contract, and verifies completion against actual effects. Across 949 AgentDojo and 400 Agent Security Bench attack cases under fixed settings it reports zero attack successes while retaining utility under high attack rates. Security is not the Susan problem, but the architectural result transfers: later evidence should instantiate an already-authorized field, not create or change the field's authority.

**PACT / Provenance-Aware Capability Contracts (arXiv 2605.11039; primary preprint, grade C)** argues that invocation-level provenance is too coarse. It tracks provenance at individual argument level and assigns semantic roles to arguments; ablations indicate both semantic roles and cross-step provenance are necessary. This is directly relevant to a reference packet containing face identity, physique, camera, pose, scale and environment: provenance should be attached to each field, not to the packet as a whole.

**RefineAct (ASE 2026; peer-reviewed/conference primary, grade B)** formalizes user intent into first-order predicates, derives pre/postcondition chains, and intercepts proposed actions before execution. On 144 ToolEmu tasks it reports failure incidence falling from 77% to 39%, with improved task completion quality. This strengthens the PRE_COMMIT_AUDIT mechanism with executable preconditions rather than narrative checking.

**Toward Safe LLM Agents: Specification, Verification, and Enforcement (2026 systematic review; secondary scientific synthesis, grade E/B-synthesis)** reports that natural-language-to-formal specification translation remains a major bottleneck (24–35% semantic correctness in the reviewed evidence). This is important counterevidence: formalizing the Susan rules is not automatically safe. A bad compiler can make a perfectly enforceable wrong contract.

### Project comparison

Susan Character Bible v5 already supplies attribute-level authority: canonical facial references govern facial anatomy; physique references govern body anatomy/silhouette; scale is independent; pose/camera references do not redefine identity or physique. Continuity rules separately preserve camera, lighting, environment, scale relationships, clothing and composition on edits. The controller should therefore preserve the **source provenance of each compiled field**, rather than merely compiling their values.

Example:

- `face.geometry`: value=canonical Susan geometry; provenance=`Face C/Profile`; authority=canonical; mutable=false except explicit identity override.
- `expression`: value=current scene expression; provenance=current user instruction; authority=scene; mutable=true by later explicit user override.
- `physique.side_silhouette`: provenance=`Physique C/Side`; authority=canonical.
- `camera.position`: provenance=current accepted base image; authority=edit-base continuity.
- `scale`: provenance=current user instruction + environmental anchor measurements; authority=scene.

A generated image, visual judge, retrieved document, or failed descendant is **evidence**, not authority. It may demonstrate that a field was or was not realized, but it cannot silently become the new source of truth for canonical identity/physique.

## New controller mechanism: PROVENANCE-CARRYING CONSTRAINT IR

Every compiled constraint receives:

`constraint_id | value | source_id | source_class | authority_rank | scope | valid_from | valid_until | supersedes | hard/soft | observable_predicate`

Every transformation (chat→state, state→tool, tool→artifact, artifact→QA, QA→commit) must preserve or explicitly transform this provenance. A boundary check fails if a field appears without an authorized source, if a lower-authority source overwrites a higher-authority field, or if a source's scope is expanded during transformation.

This extends CROSS_MODAL_CLOSURE: visual predicates now point back not only to constraint IDs but to the authoritative source that licensed each constraint.

## New failure class: AUTHORITY REBINDING

Previously SOURCE_COMPILE and OUTPUT_DRIFT were too broad. Add `AUTHORITY_REBINDING`: the correct attribute survives semantically but becomes sourced from the wrong artifact/reference. Example: a generated Susan descendant happens to have approximately correct face geometry and is then treated as the canonical identity source. The value may initially look correct while future drift becomes likely because its provenance has changed.

## Important falsification / weakened hypothesis

**"Formalize everything and enforcement will solve compliance" is weakened.** The 2026 specification/verification survey reports a substantial specification bottleneck. Therefore contract enforcement must be paired with **compiler validation against source documents and canonical pixels**. For Susan, compilation should be tested with cousin prompts and known overrides/rollbacks, and the resulting IR diff should be inspected. Formal verification of a mistranslated contract merely guarantees the wrong behavior more consistently.

## Concrete controller changes

1. Add `PROVENANCE_IR` to every active constraint.
2. Add `AUTHORITY_REBINDING` to failure taxonomy.
3. Add `SOURCE_TO_IR_VALIDATION` before pre-commit audit.
4. Treat retrieved/generated artifacts as evidence by default; only explicitly declared canonical/user sources grant authority.
5. Require field-level rather than packet-level provenance for references and tool arguments.
6. Add a negative test suite: obsolete Bible revision, failed generated image, pose reference, and QA output must be unable to overwrite canonical face/physique fields.
7. Add `COMPILER_CONFIDENCE=UNVERIFIED` unless the compiled IR is checked against source rules; formalization itself is not proof of correctness.

## Automation/research state

GitHub read/write succeeded. MASTER_DIAGNOSIS remains stale at 12:54Z as intentionally noted in SOURCE_COVERAGE; this pass does not patch it piecemeal. No repository access failure occurred.

## Remaining unchecked directions

- Full TraceGrant/PACT ablations on provenance loss/rebinding and whether their guarantees depend on oracle provenance.
- Direct experiments measuring natural-language→constraint-IR semantic error on the Susan corpus.
- Whether visual-reference provenance can be represented at region/feature level in the actual image execution surface.
- Negative-control experiment: prove that pose/reference descendants cannot acquire canonical authority through repeated editing.
- Reconcile standalone Material Fidelity, Anatomy, Camera Physics, and Simplified Rules/addenda into the authority/provenance graph.
