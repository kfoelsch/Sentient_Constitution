# CI to CJS Relocation Pilot Note

Date: 2026-06-12

This note records the first conservative relocation pilot from `corpus_institutions/` into `corpus_joint_structure/`. It implements the pilot scope selected from `ci_to_cjs_relocation_audit.md`; topical/domain-heavy high-score candidates remain deferred.

## Accepted moves

| Source | Destination | Action |
|--------|-------------|--------|
| **CI-1** (*Scope, purpose, and legitimacy interface*) | **CJS-1.1**, **CJS-1.3**, **CJS-2.2**, **CJS-3.6**, **CJS-5** | Replaced repeated joint-read and source-hierarchy prose with a short pointer to shared CJS reading, routing, and owner-discipline rules. |
| **CI-1.1** (*Definition discipline and source hierarchy*) | **CJS-1.1**, **CJS-1.4**, **CJS-1.5**, **CJS-5** | Kept single-home discipline but shortened repeated owner lists that are already stated by the CJS shared preamble contract. |
| **CI-1.4** (*Proportionality rule*) | **CJS-5A.1**, **CJS-5A.4**, **CJS-5A.6** | Kept CI-specific burden-scaling bullets; converted shared proportionality/procedure explanation into a compact CJS pointer. |
| **CI-9.3** (*Delegated subunits, institutional design class, and attachment discipline*) | **CJS-4.7** and **CJS-4.1** | Moved reusable delegated-subunit abstraction and forum-specific overlap discipline into CJS; kept institutional design-class and applicability mechanics in CI. |
| **CI-7.3** (*Contest-integrity monitoring*) | **CJS-5B.1** | Added shared contest-integrity pathway-chain OP block to CJS; kept monitor designation, reporting line, cadence, scope, and outputs in CI. |

## Deferred candidates

The pilot intentionally does not move high-score topical/domain candidates such as **CI-16**, **CI-10**, and **CI-15**. Those sections mix joint-interface signals with domain-heavy institutional policy and need a separate review wave.

**CI-26** (*Compliance mapping and stable registry*) was reviewed during continuation and left in CI. It is a local `INST-PROTO-*` registry, not shared joint doctrine; the audit's near-duplicate signal comes from ordinary corpus-alignment and registry metadata. Future CI-26 edits should prefer CJS pointers for shared drafting discipline, but the institutional protocol list remains in CI.

## Continuation moves

| Source | Destination | Action |
|--------|-------------|--------|
| **CI-6** (*Procedure integrity, contestability, and secondary review*) | **CJS-4.7**, **CJS-5A.6** | Moved the reusable **common decision rule** explanation into the shared CJS procedural-integrity cluster and replaced CI repetition with a pointer plus institution-specific publication and record duties. |
| **CI-5.1** (*Integrity trigger taxonomy and cross-layer routing*) | **CJS-5B.1** | Moved the reusable cross-layer integrity-trigger routing chain into the shared CJS evidence/audit cluster and left CI with institutional trigger labels plus owner-specific consequences. |

## Validation record

Run after the pilot edits and continuation:

- `make reference-audit`
- `make ci-cjs-relocation-audit-evidence`
- `make corpus-markdown-audit`
- `make ai-corpus-sync`
- `make ai-manifest-validate`

Result: reference and markdown audits pass; relocation evidence regenerates; AI corpus manifests validate after regeneration. The relocation audit still flags some accepted pilot sections because pointer text and cross-file routing remain visible to the heuristic, so candidate count is not treated as a success metric for this pass.
