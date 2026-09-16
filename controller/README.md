# Failure Analysis Controller Prototype

This directory implements the controller architecture consolidated in `MASTER_DIAGNOSIS.md`.

## Implemented now

- provenance-bearing constraints
- active / overridden / rejected / historical-only state
- authority-rank enforcement and `AUTHORITY_REBINDING` rejection
- canonical Susan face/physique reference-role separation with explicit allowed/forbidden contributions
- active-only deterministic state normalization
- source-to-IR structural validation
- `MUST_CHANGE` / `MUST_NOT_CHANGE` / `RECOMPUTE_FROM_CANONICAL` edit contracts
- required-reference preconditions
- deterministic execution fingerprints
- failed-route invalidation
- PASS / FAIL / UNVERIFIABLE constraint-vector QA
- transactional artifact commit/rollback
- immutable clean-ancestor tracking

## Self-test status

GitHub Actions workflow `Controller self-tests` run 35046303634 completed successfully on 2026-09-16 UTC. The deterministic suite covers stale-source override rejection, generated-descendant authority rebinding, pose-reference contamination, canonical-reference scene leakage, missing references, contradictory edit contracts, failed-route reuse, UNVERIFIABLE handling, transactional rollback/commit, historical-state exclusion, and IR-level cousin-prompt equivalence.

## Not yet end-to-end tested

The current implementation deliberately stops at the deterministic controller boundary. It does **not yet** parse arbitrary natural-language project instructions into IR, inspect Susan reference pixels, prove that those pixels reached an image-generation call, generate an image, or compute artifact-level identity/geometry/protected-region metrics. Those require an adapter between this controller and the actual Library/image execution path.

The next test milestone needs:

1. resolvable IDs/paths for the current canonical Susan face and physique images;
2. machine-readable or explicitly mapped current canonical project documents (Susan v5, continuity, realism, cinematography, plus remaining addenda);
3. an execution adapter capable of attaching the selected visual references to an image-generation/edit call and returning the artifact plus call metadata;
4. artifact evaluators for face/physique identity, camera/scale geometry, requested-edit presence, and protected-region/semantic preservation.

With those pieces, the deterministic suite can be extended into an end-to-end Susan benchmark rather than merely testing controller invariants.
