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
| **CI-11** (*Resource stewardship and incentive integrity*) | **CJS-5D.1**, **CJS-5B.1** | Moved the reusable funding / staffing / capacity dependency evaluation into the shared CJS dependency-integrity cluster and left CI with institutional stewardship triggers, malus / clawback interface, Protocol A-G supervisory trigger, and Protocol S5 funding alignment. |
| **CI-5** (*Conflict integrity, anti-capture, and anti-corruption*) | **CJS-5B.1** | Moved the reusable anti-capture control stack into the shared CJS evidence/audit cluster and left CI with institutional disclosure, cure, sortition-integrity, role-forfeiture, referral, and event-market controls. |
| **CI-4** (*Appointment, competency, rotation, and removal*) | **CJS-4.6** | Moved the reusable role-boundary and class-scaled competency-redundancy rule into the shared CJS lane-staffing interlock and left CI with institutional appointment, performance review, interpretive-body composition, and role-record duties. |
| **CI-12.3** (*Digital self-service pathway integrity*) | **CJS-5D.2** | Moved the reusable entry / management / downgrade / renewal / accessibility / exit-integrity rule into the shared CJS exit-integrity cluster and left CI with institutional supervision, attestation artifacts, billing-interface, and offense-classification routing. |
| **CI-7.1** (*Controls declaration*) | **CJS-5B.1** | Moved the reusable control-failure declaration chain into the shared CJS evidence/audit cluster and left CI with institutional publication, `INST-PROTO-*` lane, and supervised-system packet duties. |
| **CI-7.2** (*External assurance triggers*) | **CJS-5B.1** | Moved the reusable external-assurance trigger floor into the shared CJS evidence/audit cluster and left CI with institutional trigger publication and CI-8 escalation duties. |
| **CI-8** (*Cross-institution coordination and escalation*) | **CJS-5B.1** | Moved the reusable coordination / deadlock / backup-routing / anti-self-judging escalation chain into the shared CJS evidence/audit cluster and left CI with institutional publication, local role / record / deadline duties, CF-8 cooperation, and external-order boundary rules. |
| **CI-24** (*Neurodiversity, disability justice, and trauma-informed participation*) | **CJS-5C.2** | Moved the reusable adaptive-participation / cognitive-accessibility floor into the shared CJS participation cluster and left CI with disability-, neurodiversity-, and trauma-specific institutional application plus anti-exclusion review discipline. |
| **CI-17** (*Scientific publication, peer review, replication, and evidence stewardship*) | **CJS-5B.4** | Moved the reusable structured claim-testing, reliance, replication, and correction-integrity floor into the shared CJS independent-verification cluster and left CI with science-publication intake, review, access, incentive, oversight, and technical-forum application duties. |
| **CI-18** (*Community life, voluntary association, and non-instrumental time*) | **CJS-5C.1** | Moved the reusable community / associational pathway integrity floor into the shared CJS participation cluster and left CI with institutional civic-infrastructure stewardship, voluntary-association, anti-coercion, and escalation application. |
| **CI-10.2** (*Recurring charges, renewals, and commercial billing integrity*) | **CJS-5D.2** | Moved the reusable commitment, renewal, trial-conversion, bundled-offer, cancellation, downgrade, and billing-cessation floor into the shared CJS exit-integrity cluster and left CI with public-revenue / institutional billing supervision, stricter-law, and class/tier documentation duties. |
| **CI-16** (*Innovation reward, disclosure, and anti-enclosure*) | **CJS-5D.2** | Moved the reusable repair / verification / interoperability / public-interest-use / access-preserving-reward / anti-warehousing floor into the shared CJS exit-integrity cluster and left CI with institutional registry, claim-record, local public-access mechanism, sunset, reclassification, and specialist-review duties. |
| **CI-15** (*Vulnerable personal services markets - general regulation and Article X-C interface*) | **CJS-5D.2** | Moved the reusable high-vulnerability personal-service pathway floor into the shared CJS exit-integrity cluster and left CI with Article X-C-specific institutional enforcement, decriminalization, transition, and anti-pretext duties. |
| **CI-10.1** (*Public revenue, user fees, and class-aligned burden*) | **CJS-5A.4** | Moved the reusable class-aligned revenue / access-burden floor into the shared CJS constraint cluster and left CI with institutional documentation, supervised charge-interface, constrained-priority, and Protocol S5 revenue-allocation duties. |

## Validation record

Run after the pilot edits and continuation:

- `make reference-audit`
- `make ci-cjs-relocation-audit-evidence`
- `make corpus-markdown-audit`
- `make ai-corpus-sync`
- `make ai-manifest-validate`

Result: reference and markdown audits pass; relocation evidence regenerates; AI corpus manifests validate after regeneration. The heuristic candidate count remains 37. The relocation audit still flags some accepted pilot sections because pointer text and cross-file routing remain visible to the heuristic; CI-8 now remains visible as an explicit CJS pointer rather than repeated protocol text, so candidate count is not treated as a success metric for this pass. After the CI-10.2 continuation, the CI-10.2 score drops from 20 to 15 because repeated commitment / renewal / cancellation detail moved to CJS while the local billing pointer remains. After the CI-16 continuation, the CI-16 score drops from 32 to 29 and moves out of the top candidate slot because repeated anti-enclosure detail moved to CJS while local institutional registry and review mechanics remain. After the CI-15 continuation, the CI-15 score rises because the remaining local section now carries explicit CJS-5D.2 pointer language; this is expected and confirms why score movement is only an exposure signal, not a completion metric. After the CI-10.1 continuation, the CI-10.1 score drops because repeated class-aligned fiscal orientation moved to CJS while local institutional documentation and revenue-allocation duties remain. The CI-24, CI-17, CI-18, CI-10.2, CI-16, CI-15, and CI-10.1 continuations follow the same rule: preserve a short CI pointer where the local institutional topic still matters, and move only the reusable participation-accessibility, claim-integrity, associational-pathway, charge-exit, anti-enclosure, high-vulnerability pathway, or class-aligned access-burden floor.
