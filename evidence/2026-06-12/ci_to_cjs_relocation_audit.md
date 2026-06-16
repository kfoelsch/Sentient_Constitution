# CI to CJS Relocation Candidate Audit

Generated: 2026-06-12

Scope: `corpus_institutions/*.md` compared against `corpus_joint_structure/*.md` and the CJS-2.1 topic router.

This is an editorial exposure audit. It identifies candidate passages for relocation, pointer replacement, or split ownership; it does not apply moves.

## Summary

- Candidate threshold: relocation score >= 5
- Candidates: 36
- Confidence: high 20, medium 9, low 7

## Classification rules

- `split-CI-and-CJS`: likely shared rule should move to CJS while CI keeps institution-specific application.
- `replace-with-pointer`: CI appears to restate existing or near-existing CJS text; replace local repetition with a short CJS pointer after review.
- `needs-human-review`: cross-layer signals exist, but ownership is ambiguous or mixed.

## Candidates

### 1. CI-15: Vulnerable personal services markets — general regulation and Article X-C interface

- Source: `corpus_institutions/ci_15_vulnerable_personal_services_markets_article_xc_interface.md:1`
- Score / confidence: 40 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.16–CJS-5.18, CJS-5.12–CJS-5.15, CJS-5.8–CJS-5.11
- Signals: joint-interface(2), multi-owner-routing(3), routing-read-with(5), cjs-cluster(2), shared-procedure(4), dependency-failure(3), forum-system-touch(12)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: fees

Summary: **Constitutional index (abridged)** - Topic-level routing and cited authorities remain in subsection text and cross-references. - Canonical owner map: `corpus_joint_structure.md` **CJS-2.1** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4....

### 2. CI-9.3: Delegated subunits, institutional design class, and attachment discipline

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:112`
- Score / confidence: 32 / high
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7, CJS-3 / CJS-4
- Signals: joint-interface(4), multi-owner-routing(3), routing-read-with(2), shared-procedure(1), forum-system-touch(12), near-duplicate(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: institution-specific

Summary: **Purpose.** This subsection applies the shared delegated-body abstractions in `corpus_joint_structure.md` **CJS-4.1** (*Mandatory hybrid authority composition (delegated binding bodies)*) and **CJS-4.7** (*Shared procedural abstractions for delegated bodie...

Near CJS matches:
- 0.36: `corpus_joint_structure/cjs_03_joint_structural_obligations.md:163` (CJS-3.5 Classification alignment for supervised scope) — When an institution supervises systems governed by `corpus_systems.md` **CS-4** or **CS-5**, its published maps under **CI-9....

### 3. CI-1: Scope, purpose, and legitimacy interface

- Source: `corpus_institutions/ci_01_scope_purpose_legitimacy_interface.md:23`
- Score / confidence: 30 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3 / CJS-4, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7
- Signals: joint-interface(2), multi-owner-routing(2), routing-read-with(3), cjs-cluster(2), shared-procedure(2), forum-system-touch(4)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R11 — Forum continuity
- Keep-in-CI cautions: local procedure

Summary: **Constitutional index (abridged)** - Apply `corpus_joint_structure.md` **CJS-1.2** (*Shared implementation-corpus preamble contract*), **CJS-1.1** (*Joint structural boundary and owner discipline*), **CJS-2.1** (*Topic router (stable IDs)*), and **CJS-3.6*...

### 4. CI-16: Innovation reward, disclosure, and anti-enclosure

- Source: `corpus_institutions/ci_16_innovation_reward_disclosure_anti_enclosure.md:1`
- Score / confidence: 29 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-3 / CJS-4, CJS-5.16–CJS-5.18
- Signals: joint-interface(2), routing-read-with(6), cjs-cluster(1), shared-procedure(5), dependency-failure(4), forum-system-touch(8)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: local procedure

Summary: **Purpose and owner boundary.** This section governs institutional handling of innovation-reward systems where constitutional adoption brings them within scope. Constitutional meaning remains in **Chapter Five** (*Innovation Reward and Anti-Enclosure*) and...

### 5. CI-7.3: Contest-integrity monitoring (Class A and Class B)

- Source: `corpus_institutions/ci_07_oversight_assurance_controls_evidence.md:106`
- Score / confidence: 28 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-4.4, CJS-3 / CJS-4
- Signals: multi-owner-routing(2), routing-read-with(3), cjs-cluster(2), shared-procedure(6), dependency-failure(2), forum-system-touch(13)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: appointment, rotation, removal

Summary: Where institutional governed scope includes **Class A** or **Class B** systems (`corpus_systems.md` **CS-4**), institutions must maintain **contest-integrity** capacity as part of the **independent assurance line**, or through an equivalent documented...

### 6. CI-17: Scientific publication, peer review, replication, and evidence stewardship

- Source: `corpus_institutions/ci_17_scientific_publication_peer_review_replication_evidence_stewardship.md:1`
- Score / confidence: 26 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-5.19–CJS-5.23, CJS-4.4
- Signals: joint-interface(1), multi-owner-routing(1), routing-read-with(3), cjs-cluster(1), shared-procedure(8), dependency-failure(3), forum-system-touch(8)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R16 — Cross-institution coordination, deadlock, and escalation

Summary: **Purpose and owner boundary.** This section governs the institutional custody, funding, ranking, archival, reliance, and review mechanics for scientific and scholarly claims where constitutional adoption brings those functions within scope. Constitutional...

### 7. CI-26: Compliance mapping and stable registry

- Source: `corpus_institutions/ci_26_compliance_mapping_stable_registry.md:1`
- Score / confidence: 25 / high
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-3 / CJS-4, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7
- Signals: multi-owner-routing(2), routing-read-with(8), shared-procedure(4), dependency-failure(1), forum-system-touch(9), near-duplicate(1)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: appointment, removal, public revenue, fees, billing, dissolution

Summary: Institutional protocol IDs use the `INST-PROTO-*` convention and remain stable across editorial renumbering. Core registry: - `INST-PROTO-1`: Delegation and authority custody - `INST-PROTO-2`: Appointment, qualification, and removal - `INST-PROTO-3`: Confli...

Near CJS matches:
- 1.0: `corpus_joint_structure/cjs_00_registry_and_reading_rules.md:91` (Stable identifiers, edition alignment, and drafting notes) — *Corpus alignment:* edition `SC-Corpus-2026.04.30`, effective **2026-04-18**; canonical mapping in [doc_architecture.md](../doc_architect...

### 8. CI-11: Resource stewardship and incentive integrity

- Source: `corpus_institutions/ci_11_resource_stewardship_incentive_integrity.md:1`
- Score / confidence: 24 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.16–CJS-5.18, CJS-4.4, CJS-5.12–CJS-5.15
- Signals: multi-owner-routing(3), routing-read-with(4), shared-procedure(2), dependency-failure(1), forum-system-touch(12)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship
- Keep-in-CI cautions: public revenue, fees, billing

Summary: **Continuity planning:** Institutions must maintain resource adequacy for safe continuity and constitutional performance. Shared dependency-chain evaluation for funding, staffing, capacity, and resource adequacy is governed by `corpus_joint_structure.md` **...

### 9. CI-10.1: Public revenue, user fees, and class-aligned burden

- Source: `corpus_institutions/ci_10_public_revenue_fees_recurring_charges_billing_integrity.md:29`
- Score / confidence: 20 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-4.4, CJS-3 / CJS-4, CJS-5.19–CJS-5.23
- Signals: joint-interface(1), multi-owner-routing(3), routing-read-with(1), shared-procedure(2), forum-system-touch(10)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: public revenue, fees, billing

Summary: This subsection states the institutional application of the shared class-aligned revenue and access-burden floor in `corpus_joint_structure.md` **CJS-5.5** (*Implementation and cross-implementation burden-of-justification and constraint terms*). It does **...

### 10. CI-9: Classification-linked institutional obligations

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:1`
- Score / confidence: 20 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7, CJS-3 / CJS-4
- Signals: joint-interface(1), multi-owner-routing(1), routing-read-with(4), shared-procedure(2), forum-system-touch(8)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: dissolution, institutional formation

Summary: **Constitutional index (abridged)** - Topic-level routing and cited authorities remain in subsection text and cross-references. - Canonical owner map: `corpus_joint_structure.md` **CJS-2.1** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4....

### 11. CI-14.1: Interface — Article XXV-D (non-compliant property, seizure, voluntary incentives)

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:34`
- Score / confidence: 19 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.16–CJS-5.18, CJS-5.8–CJS-5.11, CJS-3 / CJS-4
- Signals: multi-owner-routing(2), routing-read-with(3), shared-procedure(3), forum-system-touch(8)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Where transition plans address **non-compliant property or systems** under **Sentient Constitution Chapter Ten, Article XXV-D**, institutions must publish and maintain: - **Eligibility and process:** clear criteria linking measures to **Chapter Six** compli...

### 12. CI-13: Institutional failure, sanctions, dissolution, and accountability

- Source: `corpus_institutions/ci_13_institutional_failure_sanctions_dissolution_accountability.md:1`
- Score / confidence: 18 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.12–CJS-5.15, CJS-5.16–CJS-5.18, CJS-5.19–CJS-5.23
- Signals: joint-interface(1), multi-owner-routing(1), routing-read-with(3), cjs-cluster(1), dependency-failure(1), forum-system-touch(2)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: dissolution

Summary: **Constitutional index (abridged)** - Topic-level routing and cited authorities remain in subsection text and cross-references. - Canonical owner map: `corpus_joint_structure.md` **CJS-2.1** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4....

### 13. CI-20: Care labor, dependent support, respite, and care-economy fairness

- Source: `corpus_institutions/ci_20_care_labor_dependent_support_respite_care_economy_fairness.md:1`
- Score / confidence: 16 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3 / CJS-4, CJS-5.16–CJS-5.18, CJS-4.4
- Signals: routing-read-with(7), cjs-cluster(2), dependency-failure(2)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: public revenue, fees, billing

Summary: **Purpose and owner boundary.** This section states the institutional application of the shared care, respite, and support-dependency floor in `corpus_joint_structure.md` **CJS-5.16** (*Implementation and cross-implementation dependency integrity and disclo...

### 14. CI-8: Cross-institution coordination and escalation

- Source: `corpus_institutions/ci_08_cross_institution_coordination_escalation.md:1`
- Score / confidence: 16 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3 / CJS-4, CJS-5.8–CJS-5.11, CJS-5.12–CJS-5.15
- Signals: routing-read-with(6), cjs-cluster(1), shared-procedure(1), forum-system-touch(4)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R16 — Cross-institution coordination, deadlock, and escalation

Summary: Where institutions share jurisdiction, evidence custody, review responsibility, enforcement support, investigative interface, or forum-adjacent routing, they must maintain a published coordination and escalation protocol. The shared coordination, deadlock,...

### 15. CI-5.1: Integrity trigger taxonomy and cross-layer routing (control package)

- Source: `corpus_institutions/ci_05_conflict_integrity_anti_capture_anti_corruption.md:57`
- Score / confidence: 16 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-4.4, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7
- Signals: routing-read-with(3), shared-procedure(5), dependency-failure(2), forum-system-touch(4)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: appointment, rotation, removal

Summary: This subsection names institutional trigger categories for **CI-5** (*Conflict integrity, anti-capture, and anti-corruption*) control maps and training. Shared cross-layer routing for integrity triggers is governed by `corpus_joint_structure.md` **CJS-5.8*...

### 16. CI-5: Conflict integrity, anti-capture, and anti-corruption

- Source: `corpus_institutions/ci_05_conflict_integrity_anti_capture_anti_corruption.md:1`
- Score / confidence: 16 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-4.4, CJS-5.12–CJS-5.15
- Signals: multi-owner-routing(1), routing-read-with(1), shared-procedure(5), dependency-failure(4), forum-system-touch(3)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship
- Keep-in-CI cautions: institution-specific, rotation, dissolution

Summary: Institutions must maintain: - auditable conflict controls that cover financial, relational, and role-based conflicts. - anti-corruption and anti-fraud controls across prevention, detection, response, and remediation. Required controls include: - disclosure...

### 17. CI-10.2: Recurring charges, renewals, and commercial billing integrity

- Source: `corpus_institutions/ci_10_public_revenue_fees_recurring_charges_billing_integrity.md:65`
- Score / confidence: 15 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-4.4, CJS-5.16–CJS-5.18, CJS-5.12–CJS-5.15
- Signals: multi-owner-routing(2), shared-procedure(3), dependency-failure(2), forum-system-touch(15)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: public revenue, fees, billing

Summary: **Purpose.** This subsection records institutional requirements for **recurring and transaction-linked charges**, including subscriptions, memberships, paid tiers, and trial-to-paid conversion, where institutions **supervise, charter, or set compliance expe...

### 18. CI-18: Community life, voluntary association, and non-instrumental time

- Source: `corpus_institutions/ci_18_community_life_voluntary_association_non_instrumental_time.md:1`
- Score / confidence: 14 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-3 / CJS-4, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7
- Signals: multi-owner-routing(1), routing-read-with(2), shared-procedure(3), forum-system-touch(5)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R16 — Cross-institution coordination, deadlock, and escalation

Summary: **Purpose.** This section records **institutional and system design expectations** for **community belonging**, **cultural gathering**, **play**, **recreation**, **solitude**, and **non-productive time** that are **adjacent to** but **not exhausted by** **A...

### 19. CI-9.2: Published industry and domain mapping

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:75`
- Score / confidence: 12 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7, CJS-5.16–CJS-5.18, CJS-5.8–CJS-5.11
- Signals: multi-owner-routing(2), shared-procedure(1), dependency-failure(1), forum-system-touch(8)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: Institutions with regulated or supervised scope must publish how major industries and regulatory domains under their authority are located against `corpus_systems.md` **CS-4** classes and **CS-5** stewardship tiers. That published map should use...

### 20. CI-7: Oversight, assurance, controls, and evidence

- Source: `corpus_institutions/ci_07_oversight_assurance_controls_evidence.md:1`
- Score / confidence: 12 / high
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-3 / CJS-4, CJS-5.19–CJS-5.23
- Signals: joint-interface(1), routing-read-with(4), shared-procedure(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: **Constitutional index (abridged)** - Topic-level routing and cited authorities remain in subsection text and cross-references. - Canonical owner map: `corpus_joint_structure.md` **CJS-2.1** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4....

### 21. CI-9.4: Survival floors, voluntary exchange, and markets (Article III-A interface)

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:271`
- Score / confidence: 11 / medium
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-3 / CJS-4, CJS-5.8–CJS-5.11, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7
- Signals: multi-owner-routing(1), routing-read-with(1), shared-procedure(2), forum-system-touch(4)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: public revenue, fees, billing

Summary: **Purpose.** **Article III-A** (*Survival*) in `core_10-10_rights_part_*.md` states outcome obligations for essential resources, housing, and connectivity. This subsection records how institutions should connect those outcomes to public revenue, user charge...

### 22. CI-1.1: Definition discipline and source hierarchy

- Source: `corpus_institutions/ci_01_scope_purpose_legitimacy_interface.md:60`
- Score / confidence: 11 / medium
- Suggested action: `split-CI-and-CJS`
- Proposed CJS destination: CJS-5.16–CJS-5.18, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7, CJS-3 / CJS-4
- Signals: joint-interface(1), multi-owner-routing(1), dependency-failure(1), forum-system-touch(4)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Definition discipline is single-home: - Constitutional definition structure, compliance-state meaning, offense classification, rights meaning, and authority-stack order remain in the numbered Sentient Constitution `core_*` files under the CJS shared preambl...

### 23. CI-9.3.2: Authority composition

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:183`
- Score / confidence: 9 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-3 / CJS-4, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7, CJS-5.8–CJS-5.11
- Signals: joint-interface(2), multi-owner-routing(1)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R01 — Delegated binding bodies and hybrid composition (non-forum institutions)
- Keep-in-CI cautions: institution-specific

Summary: **Joint minimum.** Delegated subunits in scope must satisfy **`corpus_joint_structure.md` CJS-4.1** (*Mandatory hybrid authority composition*). Read **CJS-4.1** (*Mandatory hybrid authority composition (delegated binding bodies)*) with **CI-9.3.1** (*Identi...

### 24. CI-7.1: Controls declaration

- Source: `corpus_institutions/ci_07_oversight_assurance_controls_evidence.md:40`
- Score / confidence: 9 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5.19–CJS-5.23, CJS-5.8–CJS-5.11, CJS-5.16–CJS-5.18
- Signals: routing-read-with(1), dependency-failure(3), forum-system-touch(4)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: At least annually, each institution must publish a declaration on whether material controls are operating effectively. If material controls fail, apply `corpus_joint_structure.md` **CJS-5.8** (*Implementation and cross-implementation integrity assurance an...

### 25. CI-4: Appointment, competency, rotation, and removal

- Source: `corpus_institutions/ci_04_appointment_competency_rotation_removal.md:1`
- Score / confidence: 9 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7, CJS-5.12–CJS-5.15, CJS-3 / CJS-4
- Signals: routing-read-with(3), shared-procedure(1), dependency-failure(1), forum-system-touch(1)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship
- Keep-in-CI cautions: appointment, rotation, removal

Summary: Institutions must maintain role criteria that are clear, relevant to impact, and accessible to qualified participants. Role assignment must not rely on arbitrary gatekeeping. Each institution must maintain: - qualification standards, - disqualification stan...

### 26. CI-14: Transitional governance and institutional evolution

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:1`
- Score / confidence: 8 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5.16–CJS-5.18, CJS-3 / CJS-4
- Signals: multi-owner-routing(1), routing-read-with(1), forum-system-touch(3)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R11 — Forum continuity

Summary: Institutional redesign, consolidation, or transfer must preserve non-regression and continuity duties. Apply `corpus_joint_structure.md` **CJS-5.18** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*) **Transition conti...

### 27. CI-6: Procedure integrity, contestability, and secondary review

- Source: `corpus_institutions/ci_06_procedure_integrity_contestability_secondary_review.md:1`
- Score / confidence: 8 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7, CJS-4.4
- Signals: routing-read-with(1), shared-procedure(8), forum-system-touch(2)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: Procedure rules here must remain consistent with **Chapter Five** (*Procedural Fairness*, *Contestability*, *Accountability*, *Redress and Remediation*) and with `core_02-04_definition_mechanics.md` **Chapter Four** verification and traceability rules. Shar...

### 28. CI-22: Commons, cooperatives, mutual aid, and non-market community governance

- Source: `corpus_institutions/ci_22_commons_cooperatives_mutual_aid_non_market_governance.md:1`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-5.16–CJS-5.18, CJS-5.8–CJS-5.11, CJS-5.12–CJS-5.15
- Signals: routing-read-with(1), shared-procedure(2), forum-system-touch(6)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: rotation

Summary: **Purpose.** This section supports **commons**-based and **community-managed** **resource** **patterns** **without** **forcing** every **durable** **institution** into **only** **state**, **corporate**, or **adversarial-forum** **molds** — while **keeping**...

### 29. CI-12.3: Digital self-service pathway integrity

- Source: `corpus_institutions/ci_12_transparency_participation_accessible_pathways.md:119`
- Score / confidence: 7 / medium
- Suggested action: `replace-with-pointer`
- Proposed CJS destination: CJS-4.4, CJS-5.16–CJS-5.18, CJS-5.12–CJS-5.15
- Signals: joint-interface(2), dependency-failure(1), forum-system-touch(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: billing

Summary: Digital self-service pathway integrity (Operational; Corpus Institutions) - OP-O: Apply `corpus_joint_structure.md` **CJS-5.17** (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*) **Digital self-service pathw...

### 30. CI-25: Collective public health, epidemic response, and addiction-informed care

- Source: `corpus_institutions/ci_25_collective_public_health_epidemic_response_addiction_informed_care.md:1`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5.19–CJS-5.23, CJS-5.12–CJS-5.15, CJS-5.8–CJS-5.11
- Signals: multi-owner-routing(1), routing-read-with(1), forum-system-touch(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: **Purpose.** This section frames **contagion**, **environmental** **exposure**, **population**-**level** **harms**, and **addiction** as **collective**-**care** and **governance** **problems** **under** **Article I-D**, **Article III-C**, **Article VII-C**,...

### 31. CI-24: Neurodiversity, disability justice, and trauma-informed participation

- Source: `corpus_institutions/ci_24_neurodiversity_disability_justice_trauma_informed_participation.md:1`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5.16–CJS-5.18, CJS-5.19–CJS-5.23, CJS-5.12–CJS-5.15
- Signals: routing-read-with(1), shared-procedure(1), dependency-failure(1), forum-system-touch(2)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: **Purpose.** This section applies the shared adaptive-participation floor in `corpus_joint_structure.md` **CJS-5.13** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) to neurodiversity, disability justice, and...

### 32. CI-12: Transparency, participation, and accessible pathways

- Source: `corpus_institutions/ci_12_transparency_participation_accessible_pathways.md:1`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5.12–CJS-5.15, CJS-3 / CJS-4, CJS-5.8–CJS-5.11
- Signals: routing-read-with(1), shared-procedure(1), forum-system-touch(3)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R18 — Class-scaled lane staffing and competency redundancy for materially binding stewardship

Summary: Institutional governance must be understandable and accessible to materially affected participants. Institutions must provide practical access to participation, review, and challenge channels, including accessibility accommodations sufficient for substantiv...

### 33. CI-9.1: Formation proportionality

- Source: `corpus_institutions/ci_09_classification_linked_institutional_obligations.md:37`
- Score / confidence: 6 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-5.16–CJS-5.18, CJS-5.2–CJS-5.7 / CJS-4.1 / CJS-4.7
- Signals: shared-procedure(3), dependency-failure(1), forum-system-touch(2)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: Institutions whose governed scope is only planned Class P systems must have low-friction and low-cost formation paths with simplified pre-authorization checks. Institutions governing Class A systems must satisfy extensive due diligence proportional to scope...

### 34. CI-14.2: Article XXV-D — trigger catalog, anti-abuse metrics, and publication requirements

- Source: `corpus_institutions/ci_14_transitional_governance_institutional_evolution.md:77`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-5.19–CJS-5.23, CJS-5.12–CJS-5.15
- Signals: routing-read-with(2), dependency-failure(2)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)
- Keep-in-CI cautions: dissolution

Summary: **Constitutional home:** **Chapter Ten**, **Article XXV-D** (*Non-Compliant Property, Seizure, Impoundment, Quarantine, Forfeiture, and Voluntary Turnover Incentives*). This subsection is **implementation-only**; it does not restate the Rights Floor. **Trig...

### 35. CI-12.1: Stakeholder oversight, notification, and binding-governance pathway integrity

- Source: `corpus_institutions/ci_12_transparency_participation_accessible_pathways.md:38`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5.12–CJS-5.15, CJS-5.16–CJS-5.18, CJS-5.8–CJS-5.11
- Signals: shared-procedure(1), dependency-failure(4)
- Router matches: CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R15 — Contest-integrity monitoring (pathway integrity, not merits)

Summary: Institutions must maintain practical channels through which materially affected stakeholders can receive notice, participate, contest, and track outcomes for governance decisions that materially affect them. **Stakeholder oversight channels.** Institutions...

### 36. CI-3.2: Functional separation lanes

- Source: `corpus_institutions/ci_03_institutional_design_separation_of_powers.md:60`
- Score / confidence: 5 / low
- Suggested action: `needs-human-review`
- Proposed CJS destination: CJS-5.8–CJS-5.11, CJS-5.19–CJS-5.23
- Signals: routing-read-with(1), shared-procedure(2), dependency-failure(1)
- Router matches: CJS-R17 — Cross-implementation trust integrity (joint operation model); CJS-R19 — Implementation and cross-implementation integrity assurance and resilience operations; CJS-R14 — Institutional functional lanes and non-delegable splits

Summary: Institutions must separate core governance functions enough to prevent capture, unchecked concentration, and silent failure. The following functional separations (lanes) must be maintained: - direction and policy lane, - execution lane, - challenge and revi...

## Recommended next pass

1. Review high-confidence `split-CI-and-CJS` candidates first.
2. For each accepted move, relocate only the shared operational rule to CJS and leave CI with a one-line pointer plus institution-specific application.
3. Run `make reference-audit` after any actual relocation.
