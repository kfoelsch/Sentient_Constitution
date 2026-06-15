# CI to CJS Relocation Candidate Audit

Generated: 2026-06-15

Scope: `corpus_institutions/*.md` compared against `corpus_joint_structure/*.md` and the CJS-2.2 topic router.

This is an editorial exposure audit. It identifies candidate passages for relocation, pointer replacement, or split ownership; it does not apply moves.

## Summary

- Candidate threshold: relocation score >= 5
- Candidates: 11
- Confidence: high 0, medium 6, low 5

## Classification rules

- `split-CI-and-CJS`: likely shared rule should move to CJS while CI keeps institution-specific application.
- `replace-with-pointer`: CI appears to restate existing or near-existing CJS text; replace local repetition with a short CJS pointer after review.
- `needs-human-review`: cross-layer signals exist, but ownership is ambiguous or mixed.

## Candidates

### 1. CI-15: Vulnerable personal services markets — general regulation and Article X-C interface

- Source: `corpus_institutions/ci_15_vulnerable_personal_services_markets_article_xc_interface.md:1`
- Score / confidence: 10 / medium
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5B, CJS-5D, CJS-3 / CJS-4
- Signals: routing-read-with(5), shared-procedure(1), dependency-failure(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship
- Keep-in-CI cautions: local procedure

Summary: Apply `corpus_joint_structure.md` **CJS-5D.2** **High-vulnerability personal-service pathway integrity** for the shared floor. **CI-15** states only the Article X-C application-file owner duties for authorization, enforcement separation, transition records,...

### 2. CI-20: Care labor, dependent support, respite, and care-economy fairness

- Source: `corpus_institutions/ci_20_care_labor_dependent_support_respite_care_economy_fairness.md:1`
- Score / confidence: 8 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3 / CJS-4
- Signals: routing-read-with(6)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Apply `corpus_joint_structure.md` **CJS-5D.1** **Care, respite, and support-dependency adequacy** for the shared floor. **CI-20** states only local respite, metrics, coercion-intake, and reproductive-labor routing owners. Name the respite pathway owner; **C...

### 3. CI-14.1: Interface — Article XXV-D (non-compliant property, seizure, voluntary incentives)

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:34`
- Score / confidence: 8 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5C, CJS-5A / CJS-4.1 / CJS-4.7, CJS-3 / CJS-4
- Signals: routing-read-with(3), forum-system-touch(2)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Apply `corpus_joint_structure.md` **CJS-5B.1** **Property-custody and incentive-separation control chain** for the shared floor. **CI-14.1** states only the Article XXV-D role map: eligibility owner, custody body, incentive or payout adjudicator, enforcemen...

### 4. CI-18: Community life, voluntary association, and non-instrumental time

- Source: `corpus_institutions/ci_18_community_life_voluntary_association_non_instrumental_time.md:1`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3 / CJS-4
- Signals: routing-read-with(3), forum-system-touch(1)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Apply `corpus_joint_structure.md` **CJS-5C.1** **Community and associational pathway integrity** for the shared floor. **CI-18** states only local stewardship, program, referral, and escalation owner duties. Name the local owner for civic infrastructure, vo...

### 5. CI-12.3: Digital self-service pathway integrity

- Source: `corpus_institutions/ci_12_transparency_participation_accessible_pathways.md:83`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3 / CJS-4, CJS-4.4
- Signals: routing-read-with(4)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: billing

Summary: Apply `corpus_joint_structure.md` **CJS-5D.2** **Digital self-service pathway integrity** for the shared floor. **CI-12.3** states only the supervision owner, operator-artifact file, offense-routing interface, and **CI-10.2** billing-interface read-with. ---

### 6. CI-5: Conflict integrity, anti-capture, and anti-corruption

- Source: `corpus_institutions/ci_05_conflict_integrity_anti_capture_anti_corruption.md:1`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5B, CJS-5C, CJS-3 / CJS-4
- Signals: routing-read-with(3), forum-system-touch(1)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: Apply `corpus_joint_structure.md` **CJS-5B.1** **Shared anti-capture control stack** and **Sortition and civic-lottery integrity controls** for the shared floors. **CI-5** states only institutional control-map ownership, disclosure and cure files, grave-bre...

### 7. CI-25: Collective public health, epidemic response, and addiction-informed care

- Source: `corpus_institutions/ci_25_collective_public_health_epidemic_response_addiction_informed_care.md:1`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5E, CJS-5B, CJS-5A / CJS-4.1 / CJS-4.7
- Signals: routing-read-with(3)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Apply `corpus_joint_structure.md` **CJS-5A.4** **Collective-health and emergency support-bundle floor** for the shared floor. **CI-25** states only the local pathway owner, support-bundle record, addiction-routing owner, stigma-control file, and emergency-s...

### 8. CI-10.1: Public revenue, user fees, and class-aligned burden

- Source: `corpus_institutions/ci_10_public_revenue_fees_recurring_charges_billing_integrity.md:29`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5A / CJS-4.1 / CJS-4.7
- Signals: routing-read-with(3)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Apply `corpus_joint_structure.md` **CJS-5A.4** **Class-aligned revenue and access-burden floor** for the shared floor. **CI-10.1** states only the fiscal-map owner, constrained-capacity priority owner, and **Protocol S5** reporting channel; identify **CI-10...

### 9. CI-7.3: Contest-integrity monitoring (Class A and Class B)

- Source: `corpus_institutions/ci_07_oversight_assurance_controls_evidence.md:91`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5B, CJS-3 / CJS-4, CJS-5A / CJS-4.1 / CJS-4.7
- Signals: routing-read-with(2), shared-procedure(1), forum-system-touch(1)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: Apply `corpus_joint_structure.md` **CJS-5B.1** for the shared contest-integrity pathway chain and contest-monitor independence floor. **CI-7.3** states only monitor designation, local monitor file, attestation interface, output duty, security-power file, an...

### 10. CI-10.2: Recurring charges, renewals, and commercial billing integrity

- Source: `corpus_institutions/ci_10_public_revenue_fees_recurring_charges_billing_integrity.md:56`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5D, CJS-5B, CJS-4.4
- Signals: routing-read-with(2), dependency-failure(1), forum-system-touch(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship
- Keep-in-CI cautions: billing

Summary: Apply `corpus_joint_structure.md` **CJS-5D.2** **Commitment, renewal, and charge-exit integrity** for the shared floor. **CI-10.2** states only the charge-supervision map owner, stricter-law check, reclassification trigger, and **CI-10.1** fiscal-interface...

### 11. CI-9.3: Delegated subunits, institutional design class, and attachment discipline

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:89`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5A / CJS-4.1 / CJS-4.7
- Signals: multi-owner-routing(1), forum-system-touch(2)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R01 — Delegated binding bodies and hybrid composition (non-forum institutions)

Summary: Apply `corpus_joint_structure.md` **CJS-4.1** and **CJS-4.7** for shared delegated-body abstractions. **CI-9.3** through **CI-9.3.4** state only institutional design-class, applicability, identification, authority-composition exception, rotating-attachment,...

## Recommended next pass

1. Review high-confidence `split-CI-and-CJS` candidates first.
2. For each accepted move, relocate only the shared operational rule to CJS and leave CI with a one-line pointer plus institution-specific application.
3. Run `make reference-audit` after any actual relocation.
