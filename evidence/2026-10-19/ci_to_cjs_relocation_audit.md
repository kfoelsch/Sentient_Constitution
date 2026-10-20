# CI to CJS Relocation Candidate Audit

Generated: 2026-10-19

Scope: `corpus_institutions/*.md` compared against `corpus_joint_structure/*.md` and the CJS-0.1 topic router.

This is an editorial exposure audit. It identifies candidate passages for relocation, pointer replacement, or split ownership; it does not apply moves.

## Summary

- Candidate threshold: relocation score >= 5
- Candidates: 37
- Confidence: high 15, medium 9, low 13

## Classification rules

- `split-CI-and-CJS`: likely shared rule should move to CJS while CI keeps institution-specific application.
- `replace-with-pointer`: CI appears to restate existing or near-existing CJS text; replace local repetition with a short CJS pointer after review.
- `needs-human-review`: cross-layer signals exist, but ownership is ambiguous or mixed.

## Candidates

### 1. CI-4.7: Practice licence, practice clearance, and joint professional practice

- Source: `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:287`
- Score / confidence: 24 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-1 / CJS-2, CJS-3.22–CJS-3.12
- Signals: joint-interface(6), routing-read-with(1), shared-procedure(8), dependency-failure(2), forum-system-touch(29)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model)
- Keep-in-CI cautions: removal, fees, institutional formation

Summary: *In plain terms: a technical forum can say that a kind of work is risky enough to need proof of competence. For work that can cause severe or irreversible injury, such as surgery or electrical work, a practice licence may be required before the act, and an...

### 2. CI-4.5: Authorized roles and accountability chains

- Source: `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:135`
- Score / confidence: 23 / high
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-1 / CJS-2, CJS-3.22–CJS-3.12
- Signals: joint-interface(2), routing-read-with(4), shared-procedure(3), forum-system-touch(18), near-duplicate(1)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship
- Keep-in-CI cautions: appointment, removal

Summary: *In plain terms: under **Chapter Fourteen**, section 5 and the **Article XII-C** (*Internal Roles, Accountability, and Due-Process Requirements*) interface, each institution writes its own map of who is authorized to do what — and who is accountable when th...

Near CJS matches:
- 0.32: `corpus_joint_structure/cjs_02_specific_joint_interlocks.md:202` (CJS-2.4 Class-scaled lane staffing and competency redundancy) — The constitutional floor remains in [Chapter Fourteen](../core_14_governance.md), section **5**. Domain detail remains in **CI-3** (*Inst...

### 3. CI-4.6: Seat catalog — process-role archetypes and operational boundaries

- Source: `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:175`
- Score / confidence: 21 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.19–CJS-3.53
- Signals: joint-interface(3), routing-read-with(2), shared-procedure(17), forum-system-touch(43)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model)

Summary: *In plain terms: a **seat** is the unit of authority over one materially binding act — the one who asks, the one who checks, the one who writes it down, the one who hears the complaint, plus a few recurring special-authority seats such as incident command a...

### 4. CI-14.4: **Article XXVIII-A** (*Phased Adoption and Rights-Floor Continuity*) — Rights-Floor attainment ledger: measures, verification, and publication

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:234`
- Score / confidence: 20 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.16–CJS-3.18, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: routing-read-with(6), shared-procedure(20), dependency-failure(8), forum-system-touch(13)
- Router matches: CJS-R19 — integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R22 — Standing-record custody, opening authority, and segregation of duties

Summary: *In plain terms: a right is only as real as the forums, oversight, trained staff, and public habits that enforce it, and those take time to build. So **Article XXVIII-A** (*Phased Adoption and Rights-Floor Continuity*) asks for two things: what the adopter...

### 5. CI-14.3: **Article XXVIII-D** (*Non-Compliant Property and Systems; Voluntary Turnover Incentives*) — operative transition-scoped remediation requirements

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:162`
- Score / confidence: 17 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.16–CJS-3.18, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: joint-interface(2), routing-read-with(1), shared-procedure(6), dependency-failure(1), forum-system-touch(11)
- Router matches: CJS-R19 — integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R23 — Seat types, local role maps, and wrong-seat routing
- Keep-in-CI cautions: local procedure

Summary: *In plain terms: **CI-14.3** (*operative transition-scoped remediation requirements*) is the operational half of **Article XXVIII-D** (*Non-Compliant Property and Systems; Voluntary Turnover Incentives*) — what institutions actually do when transition plans...

### 6. CI-27.5: Remedy parity and capacity-failure interface

- Source: `corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md:108`
- Score / confidence: 16 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.19–CJS-3.53, CJS-1 / CJS-2, CJS-3.22–CJS-3.12
- Signals: routing-read-with(4), dependency-failure(6), forum-system-touch(9)
- Router matches: CJS-R20 — Remedy parity and lock-to-remedy capacity; CJS-R21 — Capacity-failure routing; CJS-R03 — Lawful panel formation, disclosure, recusal, substitution, inability-to-form

Summary: *In plain terms: Lock offices may not outrun the repair offices that make those locks lawful. When remedy or restoration work falls behind its clock, the starved office does not get to decide that it is fine.* This subsection implements, and must not narrow...

### 7. CI-13.5: Contraction order

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:153`
- Score / confidence: 15 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.22–CJS-3.12, CJS-2.3
- Signals: joint-interface(2), shared-procedure(5), dependency-failure(1), forum-system-touch(9)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R23 — Seat types, local role maps, and wrong-seat routing

Summary: *In plain terms: if a Chartered Party is Class L or higher and keeps putting others at risk, the forum can order it to stop, hand off, or shrink the activities that cross the line, until an independent check shows it is below every line. The Chartered Party...

### 8. CI-8.3: Digital self-service pathway integrity

- Source: `corpus_institutions/ci_08_transparency_participation_accessible_pathways.md:150`
- Score / confidence: 15 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-2.3, CJS-1 / CJS-2, CJS-3.16–CJS-3.18
- Signals: routing-read-with(4), shared-procedure(2), dependency-failure(7), forum-system-touch(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — integrity assurance and resilience operations; CJS-R23 — Seat types, local role maps, and wrong-seat routing
- Keep-in-CI cautions: billing, dissolution

Summary: *In plain terms: if you can subscribe online, you should be able to manage, downgrade, renew, or cancel through the same kind of self-service path — without dark patterns, hidden phone-only exits, or billing that keeps running after you thought you left. In...

### 9. CI-21.3: Referral and escalation interfaces

- Source: `corpus_institutions/ci_21_community_life_voluntary_association_non_instrumental_time.md:95`
- Score / confidence: 14 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-1 / CJS-2, CJS-3.13–CJS-3.4, CJS-2.3
- Signals: routing-read-with(4), shared-procedure(3), dependency-failure(1), forum-system-touch(2)
- Router matches: CJS-R19 — integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship; CJS-R17 — Cross-implementation trust integrity (joint operation model)
- Keep-in-CI cautions: local procedure

Summary: *In plain terms: when a local associational pathway for gathering or association fails — blocked access, captured review, or nowhere to appeal — sentients need a published map of where the case goes next.* Each institution in scope must name and maintain lo...

### 10. CI-3.2: Functional separation lanes

- Source: `corpus_institutions/ci_03_institutional_design_separation_of_powers.md:81`
- Score / confidence: 14 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.19–CJS-3.53, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: joint-interface(1), routing-read-with(1), shared-procedure(4), dependency-failure(1), forum-system-touch(16)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R19 — integrity assurance and resilience operations
- Keep-in-CI cautions: appointment, rotation, removal

Summary: *In plain terms: power must be split into distinct jobs so no one office runs everything unchecked. Required lanes include setting direction and policy, carrying decisions out, challenging and reviewing them, auditing and assuring integrity, and publishing...

### 11. CI-27.1: Capacity, funding, and succession

- Source: `corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md:49`
- Score / confidence: 13 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.13–CJS-3.4, CJS-3.19–CJS-3.53
- Signals: routing-read-with(4), dependency-failure(1), forum-system-touch(4)
- Router matches: CJS-R21 — Capacity-failure routing; CJS-R20 — Remedy parity and lock-to-remedy capacity; CJS-R23 — Seat types, local role maps, and wrong-seat routing
- Keep-in-CI cautions: dissolution

Summary: *In plain terms: Every remedy system must name who owns it, where its funding comes from, and who takes over if that owner disappears. A remedy route with no named owner fails silently.* Each remedy system must name, in plain view: - the institutional owner...

### 12. CI-13.10: Review, fairness, and enforcement

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:246`
- Score / confidence: 13 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-1 / CJS-2, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: routing-read-with(5), shared-procedure(1), forum-system-touch(10)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R21 — Capacity-failure routing
- Keep-in-CI cautions: dissolution

Summary: *In plain terms: every order can be challenged before someone independent, nobody gets punished for what they believe or for speaking up, a wrong order is put right, and the forum has real levers when a Chartered Party defies it.* **Review and fairness:** -...

### 13. CI-27.4: Standards interface and accountability routing

- Source: `corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md:98`
- Score / confidence: 12 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.19–CJS-3.53, CJS-1 / CJS-2, CJS-2.3
- Signals: routing-read-with(2), dependency-failure(6), forum-system-touch(17)
- Router matches: CJS-R21 — Capacity-failure routing; CJS-R20 — Remedy parity and lock-to-remedy capacity; CJS-R19 — integrity assurance and resilience operations
- Keep-in-CI cautions: dissolution

Summary: *In plain terms: Technical forums set the capacity and timeliness standards remedy systems must meet, but they do not run those systems. Setting a standard is not the same as commanding compliance.* Remedy systems must meet published capacity, measurement,...

### 14. CI-14.5: **Article XXVIII-A** (*Phased Adoption and Rights-Floor Continuity*) — prioritizing institutional transition targets

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:364`
- Score / confidence: 12 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.16–CJS-3.18, CJS-3.22–CJS-3.12, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: shared-procedure(5), dependency-failure(4), forum-system-touch(10)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R17 — Cross-implementation trust integrity (joint operation model)
- Keep-in-CI cautions: appointment, rotation, dissolution

Summary: *In plain terms: existing institutions cannot all be rebuilt at once either. Forums, agencies, companies, and governing bodies each need to be moved toward constitutional operation, and the order matters. Start with the institutions that hold the most power...

### 15. CI-14.1: Interface — **Article XXVIII-D** (*Non-Compliant Property and Systems; Voluntary Turnover Incentives*) (non-compliant property, seizure, voluntary incentives)

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:83`
- Score / confidence: 12 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.16–CJS-3.18, CJS-3.13–CJS-3.4, CJS-2.3
- Signals: routing-read-with(5), forum-system-touch(7)
- Router matches: CJS-R19 — integrity assurance and resilience operations; CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties

Summary: *In plain terms: when transition plans touch non-compliant property, seizure, impoundment, quarantine, or voluntary turnover incentives, every step in the chain needs a named owner — who decides someone is eligible, who holds the asset, who pays a bounty, w...

### 16. CI-13.9: Systems under consequence orders

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:225`
- Score / confidence: 11 / medium
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.16–CJS-3.18, CJS-3.22–CJS-3.12, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: joint-interface(1), shared-procedure(1), dependency-failure(3), forum-system-touch(40)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R19 — integrity assurance and resilience operations
- Keep-in-CI cautions: removal, dissolution

Summary: *In plain terms: a System is not a legal entity, so orders go to its steward. The same ladder applies. A System that may be sentient is never destroyed to end the matter: its state is saved and held in safe hands.* The respondent for a System is its steward...

### 17. CI-13.2: Findings before any order

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:105`
- Score / confidence: 11 / medium
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.16–CJS-3.18
- Signals: joint-interface(1), shared-procedure(8), dependency-failure(1), forum-system-touch(3)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R23 — Seat types, local role maps, and wrong-seat routing

Summary: *In plain terms: before the forum orders anything, it writes down what is wrong, who is at risk, who caused it, and why a lighter step would not be enough. The side asking for a heavier step carries that burden.* Before ordering any rung of the ladder, the...

### 18. CI-10.2: Recurring charges, renewals, and commercial billing integrity

- Source: `corpus_institutions/ci_10_public_revenue_fees_recurring_charges_billing_integrity.md:75`
- Score / confidence: 10 / medium
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3.16–CJS-3.18, CJS-2.3, CJS-1 / CJS-2
- Signals: routing-read-with(1), shared-procedure(1), dependency-failure(3), forum-system-touch(4)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — integrity assurance and resilience operations; CJS-R01 — Delegated binding bodies and hybrid composition (non-forum institutions)
- Keep-in-CI cautions: public revenue, fees, billing

Summary: *In plain terms: subscriptions, memberships, trials, and auto-renewals must be honest before you sign up — clear price, clear timing, clear renewal rules — and cancellation or downgrade must work through a published path without dark patterns or surprise ch...

### 19. CI-21.2: Voluntary association and anti-coercion guardrails

- Source: `corpus_institutions/ci_21_community_life_voluntary_association_non_instrumental_time.md:75`
- Score / confidence: 9 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-1 / CJS-2, CJS-3.22–CJS-3.12, CJS-3.16–CJS-3.18
- Signals: routing-read-with(5), dependency-failure(1)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R19 — integrity assurance and resilience operations
- Keep-in-CI cautions: fees

Summary: *In plain terms: joining a club, mutual-aid circle, faith community, or online group must rest on real consent — and leaving must not trigger retaliation, reputational lock-in, or hidden informal punishment. Community warmth is not a license for capture.* E...

### 20. CI-13.4: Correction and constrained authority

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:134`
- Score / confidence: 9 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.22–CJS-3.12, CJS-3.19–CJS-3.53
- Signals: routing-read-with(1), shared-procedure(3), forum-system-touch(6)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — integrity assurance and resilience operations
- Keep-in-CI cautions: dissolution

Summary: *In plain terms: six rungs, lightest first. A heavier rung needs a showing that the lighter ones would not do. Every rung has an end date, a review, and a way back.* | Rung | Measure | What it does | | --- | --- | --- | | 1 | Directed correction | Orders na...

### 21. CI-11.4: Local alignment duties

- Source: `corpus_institutions/ci_11_resource_stewardship_incentive_integrity.md:79`
- Score / confidence: 9 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.19–CJS-3.53, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: routing-read-with(1), shared-procedure(1), dependency-failure(2), forum-system-touch(6)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R19 — integrity assurance and resilience operations

Summary: *In plain terms: money and pay schemes must support honest stewardship, not undermine it. Institutions must show how funding choices stay within stewardship limits and how compensation rewards constitutional duty instead of short-term performance theater —...

### 22. CI-27.3: High-impact remedy domains

- Source: `corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md:81`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3.16–CJS-3.18, CJS-3.13–CJS-3.4, CJS-1 / CJS-2
- Signals: joint-interface(1), forum-system-touch(6)
- Router matches: CJS-R20 — Remedy parity and lock-to-remedy capacity; CJS-R19 — integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model)

Summary: *In plain terms: Areas where a broken remedy route causes the most damage — child protection, environmental enforcement, benefits, detention oversight, public health — and so require durable systems.* The following domains, and comparable high-impact system...

### 23. CI-27.2: Durability, backlog, and publication

- Source: `corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md:64`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.19–CJS-3.53, CJS-3.13–CJS-3.4
- Signals: dependency-failure(3), forum-system-touch(10)
- Router matches: CJS-R20 — Remedy parity and lock-to-remedy capacity; CJS-R19 — integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model)

Summary: *In plain terms: Remedy systems publish their own waiting times and backlog ages, so a route that has quietly stopped working in practice becomes visible from outside.* Each remedy system must publish, on a fixed schedule compatible with **CF-11** (*Forum p...

### 24. CI-25.5: Ombuds, escalation, and technical forum referral

- Source: `corpus_institutions/ci_25_scientific_publication_peer_review_replication_evidence_stewardship.md:133`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-1 / CJS-2, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.22–CJS-3.12
- Signals: routing-read-with(1), shared-procedure(3), forum-system-touch(3)
- Router matches: CJS-R19 — integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R16 — Cross-institution coordination, deadlock, and escalation
- Keep-in-CI cautions: local procedure

Summary: *In plain terms: when publication disputes stall or the local reviewer is conflicted, there must be a named ombuds lane, an escalation path, and — where needed — a specialist technical forum that is not the same shop that benefits from the original claim.*...

### 25. CI-25.3: Challenge, correction, and access

- Source: `corpus_institutions/ci_25_scientific_publication_peer_review_replication_evidence_stewardship.md:98`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.19–CJS-3.53
- Signals: routing-read-with(1), shared-procedure(4)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — integrity assurance and resilience operations; CJS-R10 — Forum performance, backlog requirements, publication timeliness, accessibility

Summary: *In plain terms: sentients who try to replicate, reanalyze, or correct a claim need a real door in — and if publication, funding, and editorial power are bundled together, that bundling must be justified and auditable.* Each institution in scope must name a...

### 26. CI-21.1: Civic infrastructure and non-instrumental time

- Source: `corpus_institutions/ci_21_community_life_voluntary_association_non_instrumental_time.md:56`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.13–CJS-3.4, CJS-1 / CJS-2
- Signals: joint-interface(1), routing-read-with(1), forum-system-touch(2)
- Router matches: CJS-R19 — integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R01 — Delegated binding bodies and hybrid composition (non-forum institutions)
- Keep-in-CI cautions: fees

Summary: *In plain terms: institutions that control parks, halls, transit-to-gathering routes, recreation programs, or scheduling rules must not treat cultural gathering, play, recreation, or quiet non-productive time as second-class uses that only survive if they p...

### 27. CI-14.2: **Article XXVIII-D** (*Non-Compliant Property and Systems; Voluntary Turnover Incentives*) — trigger catalog, anti-abuse metrics, and publication requirements

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:114`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.19–CJS-3.53, CJS-3.16–CJS-3.18
- Signals: routing-read-with(1), shared-procedure(1), forum-system-touch(5)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R19 — integrity assurance and resilience operations
- Keep-in-CI cautions: local procedure

Summary: *In plain terms: **CI-14.2** (*trigger catalog, anti-abuse metrics, and publication requirements*) turns **Article XXVIII-D** (*Non-Compliant Property and Systems; Voluntary Turnover Incentives*) into a practical checklist institutions must publish in trans...

### 28. CI-13.8: Emergency containment

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:218`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.19–CJS-3.53, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.22–CJS-3.12
- Signals: shared-procedure(3), forum-system-touch(5)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R23 — Seat types, local role maps, and wrong-seat routing
- Keep-in-CI cautions: dissolution

Summary: *In plain terms: if serious harm that cannot be undone is about to happen, the forum can act at once, but only with something lighter than dissolution and only for a short, reviewed time.* Where imminent irreversible harm to others is shown on the record, t...

### 29. CI-9.3.1: Identification and competence

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:120`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-1 / CJS-2, CJS-2.3
- Signals: routing-read-with(2), shared-procedure(1), forum-system-touch(1)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R19 — integrity assurance and resilience operations; CJS-R12 — Standard forum records, forms, and evidence artifacts

Summary: *In plain terms: every delegated subunit must be clearly labeled — who it reports to, what it may decide, and what qualifications its members need. A subunit cannot become a back door that skips normal challenge routes or forum routing.* Each formation or a...

### 30. CI-8.1: Stakeholder oversight, notification, and binding-governance pathway integrity

- Source: `corpus_institutions/ci_08_transparency_participation_accessible_pathways.md:87`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.13–CJS-3.4, CJS-3.22–CJS-3.12, CJS-3.16–CJS-3.18
- Signals: routing-read-with(1), dependency-failure(3), forum-system-touch(1)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R23 — Seat types, local role maps, and wrong-seat routing

Summary: *In plain terms: when an institution asks for your input on something that will really bind you, it must say so clearly — who counts as affected, how long you have to respond, what happens to your submission, and what exit or adaptation consequences the dec...

### 31. CI-4.2: Role criteria, appointment standards, and removal pathways

- Source: `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:77`
- Score / confidence: 6 / low
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.22–CJS-3.12, CJS-2.3
- Signals: routing-read-with(1), shared-procedure(1), forum-system-touch(3), near-duplicate(1)
- Router matches: CJS-R03 — Lawful panel formation, disclosure, recusal, substitution, inability-to-form; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R23 — Seat types, local role maps, and wrong-seat routing
- Keep-in-CI cautions: rotation, removal

Summary: *In plain terms: every institution must publish clear, public rules for who can hold each role — what qualifies someone, what disqualifies them, who steps in if they leave, when they must rotate off for independence, and how they can be removed with fair pr...

Near CJS matches:
- 0.32: `corpus_joint_structure/cjs_02_specific_joint_interlocks.md:189` (CJS-2.4 Class-scaled lane staffing and competency redundancy) — Before using role, role-holder, stewardship, operator, accountable-role, or lane terms in this subsection, apply **CJS-3.0** (*Cross-band...

### 32. CI-3.6.1: Owner boundary

- Source: `corpus_institutions/ci_03_institutional_design_separation_of_powers.md:146`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.13–CJS-3.4, CJS-3.22–CJS-3.12, CJS-3.16–CJS-3.18
- Signals: shared-procedure(2), forum-system-touch(13)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R17 — Cross-implementation trust integrity (joint operation model)

Summary: Chapter Seven holds the floor, and this section adds the template and procedure. The boundary between them: - **What Chapter Seven holds:** The constitutional floor — which systems must publish a System Charter and which institutions an Institutional Charte...

### 33. CI-3.6: System and Institutional Charter contents, review, and formation template

- Source: `corpus_institutions/ci_03_institutional_design_separation_of_powers.md:123`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.13–CJS-3.4
- Signals: routing-read-with(1), forum-system-touch(10)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R17 — Cross-implementation trust integrity (joint operation model)

Summary: *In plain terms: every institution needs a published scope document that says what it is for, what it may do, what it must not do, who it affects, how that document can change, and how often it is re-checked. For an institution that runs one system, that do...

### 34. CI-13.1: Opening a consequence matter

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:76`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.13–CJS-3.4, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: shared-procedure(2), forum-system-touch(7)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R19 — integrity assurance and resilience operations
- Keep-in-CI cautions: dissolution

Summary: *In plain terms: this procedure opens only on a verified finding. A late filing, a failed first check, or a mismatch is a defect to fix, not a reason to start a consequence matter. When a matter does open, the lead Integrity forum works up a ladder of measu...

### 35. CI-5.2: Institutional owner files and named routes

- Source: `corpus_institutions/ci_05_conflict_integrity_anti_capture_anti_corruption.md:66`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.13–CJS-3.4, CJS-2.3
- Signals: shared-procedure(1), dependency-failure(1), forum-system-touch(4)
- Router matches: CJS-R19 — integrity assurance and resilience operations; CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties
- Keep-in-CI cautions: dissolution

Summary: *In plain terms: each institution must write down who does what when honesty or independence is at stake — not leave it implied. That means a published map of anti-corruption safeguards, named roles for publishing disclosures and tracking fix deadlines, rec...

### 36. CI-3.6.6: Periodic review

- Source: `corpus_institutions/ci_03_institutional_design_separation_of_powers.md:271`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.22–CJS-3.12, CJS-3.16–CJS-3.18, CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5
- Signals: dependency-failure(1), forum-system-touch(4)
- Router matches: CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R17 — Cross-implementation trust integrity (joint operation model)

Summary: On the cadence its class sets in [Chapter Thirteen §6 Timely resolution, materiality tiers, and anti-delay discipline](../core_13_forum.md#review-cadence) (*Review cadence*), and sooner after material incident, dependency growth, class change, credible chal...

### 37. CI-3.6.5: Formation check statement template

- Source: `corpus_institutions/ci_03_institutional_design_separation_of_powers.md:243`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-3.5–CJS-3.8 / CJS-2.1 / CJS-2.5, CJS-3.22–CJS-3.12, CJS-3.19–CJS-3.53
- Signals: shared-procedure(3), forum-system-touch(4)
- Router matches: CJS-R23 — Seat types, local role maps, and wrong-seat routing; CJS-R22 — Standing-record custody, opening authority, and segregation of duties; CJS-R03 — Lawful panel formation, disclosure, recusal, substitution, inability-to-form
- Keep-in-CI cautions: appointment, removal

Summary: [Chapter Seven §5 Formation Check: Office-Holder Standing and Authenticity](../core_07_charters.md#5-formation-check-office-holder-standing-and-authenticity) holds the floor. This subsection is the template and procedure. It may be stricter and may not narr...

## Recommended next pass

1. Review high-confidence `split-CI-and-CJS` candidates first.
2. For each accepted move, relocate only the shared operational rule to CJS and leave CI with a one-line pointer plus institution-specific application.
3. Run `make reference-audit` after any actual relocation.
