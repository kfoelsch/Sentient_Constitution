# Chapter 0/1 -> Chapter 6 Alignment Audit Report

**Date:** 2026-07-03
**Workflow:** CH0_CH1_CH6_ALIGNMENT_AUDIT
**Auditor:** Automated static extraction with manual-review flags

## Average-Reader Dashboard

**Overall status:** `REVIEW`

The audit found a mostly usable alignment map, with some review items where trace prose, measurement routing, or semantic fit may need editorial attention. The report separates machine-checkable issues from human doctrinal review.

### What Is Strong

- Chapter 6 article/subarticle inventory was discovered across all four rights files: `124` items.
- Direct Chapter 1 trace exists for `107/124` Chapter 6 items.
- Chapter 0 measurement frame signals are structurally visible on `37/124` items.

### What Needs Review

- Measurement-family routing is clear or not required for `124/124` items.
- Static semantic review flags remain: `10`.
- Non-manual findings remain: `18`.

### What May Need Edits

- `weak_trace` at `core_06-06_rights_part_a.md:116` (I): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_a.md:271` (II): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_a.md:474` (III): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_a.md:695` (IV): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_b.md:445` (VI): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_b.md:543` (VII): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_b.md:816` (VIII): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_b.md:1021` (IX): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_b.md:1190` (X): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_c.md:32` (XII): Chapter 1 basis is inferred from subject matter, not directly cited.
- Plus `8` additional machine-review item(s).

### Rights-Family Dashboard

| Rights family | Items | Direct Chapter 1 basis | Chapter 0 frame | Measurement routing | Status |
|---|---:|---:|---:|---:|---|
| survival/resources | 19 | 15/19 | 9/19 | 19/19 | REVIEW |
| equality/access | 23 | 20/23 | 4/23 | 23/23 | REVIEW |
| agency/participation | 15 | 13/15 | 4/15 | 15/15 | REVIEW |
| systems/trust/audit | 29 | 24/29 | 10/29 | 29/29 | REVIEW |
| standing/interpretation | 21 | 20/21 | 5/21 | 21/21 | REVIEW |
| justice/emergency/transition | 17 | 15/17 | 5/17 | 17/17 | REVIEW |

## Maintainer Metrics

| Metric | Result | Status |
|---|---:|---|
| Chapter 6 articles/subarticles discovered | 124 | PASS |
| Items with direct Chapter 1 basis | 107/124 | REVIEW |
| Items with Chapter 0 Tetrad/Aims/material-stake framing | 37/124 | REVIEW |
| Items with clear measurement routing or no measurement dependency | 124/124 | PASS |
| Broken or ambiguous Chapter 0/1/6 links | 0 | PASS |
| Owner-boundary risks | 0 | PASS |
| Potential overreach flags | 0 | PASS |
| Manual semantic-review items | 10 | REVIEW |

## Chapter 6 Article Traceability

| Article | Title | File | Chapter 1 basis | Inferred basis | Chapter 0 frame | Measurements | Status |
|---|---|---|---|---|---|---|---|
| I | Environmental Survival | `core_06-06_rights_part_a.md:116` | None | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint | weak_trace |
| I-A | Environmental Preconditions and Ecological Integrity | `core_06-06_rights_part_a.md:136` | 3, 4.1, 6.3.1, 11.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint | complete |
| I-B | Ecological Footprint and Transparency | `core_06-06_rights_part_a.md:173` | 4.2, 9.2, 11.1, linked | 2, 3.1, 3.2, 6.2, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Accessibility | complete |
| I-C | Intergenerational Responsibility | `core_06-06_rights_part_a.md:200` | 3, 4.1, 8.16, 8.21, 9, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Ecological Footprint | complete |
| I-D | Existential Risk and Ecological Recovery Capacity | `core_06-06_rights_part_a.md:230` | 4.1, 9, 10.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Timely Resolution | complete |
| II | Material Stewardship and Durable-Use Integrity | `core_06-06_rights_part_a.md:271` | None | 2, 3.1, 3.2, 6.2, 7, 8, 9, 9.2 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint | weak_trace |
| II-A | Material Stewardship and Lifecycle Honesty | `core_06-06_rights_part_a.md:299` | 4.2, 10.1, 11.1, linked | 3.2, 4, 6.2, 7, 8, 9, 9.2, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Productive Capacity, Ecological Footprint, Accessibility, Trustworthiness | complete |
| II-B | Repair, Maintenance, and Independent Servicing | `core_06-06_rights_part_a.md:332` | 4.1, 4.2, 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Dependency / Resource Flow | complete |
| II-C | Designed Obsolescence and Incentive Discipline | `core_06-06_rights_part_a.md:365` | 4.1, 10, 10.1, 10.2, linked | 3.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity | complete |
| II-D | Post-Sale Access and Subscription Integrity | `core_06-06_rights_part_a.md:395` | 4.2, 5, 10, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Dependency / Resource Flow, Trustworthiness | complete |
| II-E | Info-Sphere Dependency, Continuity, and Operator Non-Viability | `core_06-06_rights_part_a.md:424` | 4.1, 10.1, 10.2.4, 11.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Dependency / Resource Flow | complete |
| III | Survival and Equal Educational Access | `core_06-06_rights_part_a.md:474` | None | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint, Educational Agency | weak_trace |
| III-A | Survival | `core_06-06_rights_part_a.md:496` | 3, 4.1, 5, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Ecological Footprint, Dependency / Resource Flow, Timely Resolution | complete |
| III-B | Equal Educational Access | `core_06-06_rights_part_a.md:548` | 3, 4.2, 5, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad | Productive Capacity, Ecological Footprint, Substantive Fairness, Accessibility, Educational Agency | complete |
| III-C | Bodily-Maintenance and Healthcare Access | `core_06-06_rights_part_a.md:585` | 3, 5, 5.1, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Ecological Footprint, Substantive Fairness | complete |
| III-D | Labor and Economic Floor | `core_06-06_rights_part_a.md:632` | 3, 5, 5.1, 8.16, 9, 10.3, linked | 2, 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Substantive Fairness, Educational Agency, Trustworthiness | complete |
| IV | Resource Allocation, Dependencies, and Ecosystem Funding | `core_06-06_rights_part_a.md:695` | None | 2, 3.1, 3.2, 6.2, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Dependency / Resource Flow, Proportionate Cross-System Support | weak_trace |
| IV-A | Dependency Mapping and Resource-Flow Transparency | `core_06-06_rights_part_a.md:724` | 4.2, 10, 11.1, linked | 3.2, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Dependency / Resource Flow, Proportionate Cross-System Support | complete |
| IV-B | Cross-System Fairness and Sustainability | `core_06-06_rights_part_a.md:755` | 3, 8.20, 10.1, 11.1, 12.1, 14, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Proportionate Cross-System Support, Substantive Fairness, Timely Resolution | complete |
| V | Equal Basic Rights | `core_06-06_rights_part_b.md:57` | linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims, material stake | Avoidable Burden, Substantive Fairness, Accessibility | manual_review |
| V-A | Dignity and Equal Moral Standing | `core_06-06_rights_part_b.md:67` | 3, 5, 8.16, linked | 2, 3.1, 5, 5.1, 7, 8 | Tetrad, Aims | Productive Capacity, Substantive Fairness | complete |
| V-B | Nondiscrimination | `core_06-06_rights_part_b.md:95` | 5, 6.3, 8.1, 10.1, linked | 3.1, 5, 5.1, 6.1, 6.3, 7 | Tetrad, Aims | Constitutional Efficiency, Avoidable Burden, Ecological Footprint, Substantive Fairness, Accessibility | complete |
| V-C | Full Inclusion and Equality in Adjudication and Operations | `core_06-06_rights_part_b.md:144` | 4.1, 5, 6.3, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7, 10, 10.2 | Tetrad | Constitutional Efficiency, Avoidable Burden, Substantive Fairness | complete |
| V-D | Freedom of conscience, religion, and comparable worldview | `core_06-06_rights_part_b.md:178` | 5, 6.3, 10.1, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 8, 10, 10.2 | Tetrad | Avoidable Burden, Ecological Footprint, Substantive Fairness, Accessibility | complete |
| V-E | Sentience-Status Adjudication Floor | `core_06-06_rights_part_b.md:222` | 4.2, 8.1.1, 10.1, 10.1.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Avoidable Burden | complete |
| V-F | Developing Sentients, Best-Interest, and Graduated Capability | `core_06-06_rights_part_b.md:267` | 4.2, 5, 5.1, 8.1, 8.1.1, 8.16, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Substantive Fairness | complete |
| V-G | Accessibility | `core_06-06_rights_part_b.md:329` | 3, 5, 5.1, 6.3.1, 7.1, 10.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Accessibility, Educational Agency | complete |
| V-H | Expression, Assembly, and Press | `core_06-06_rights_part_b.md:392` | 4.2, 5, 5.1, 6.3.1, 7.2.1, 8.1.2, 8.16, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10.2 | Tetrad, Aims | Avoidable Burden, Ecological Footprint, Substantive Fairness, Educational Agency | complete |
| VI | Right to Sentient-Centered Education | `core_06-06_rights_part_b.md:445` | None | 2, 3.1, 3.2, 5, 5.1, 6.2, 8 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Substantive Fairness, Accessibility, Educational Agency | weak_trace |
| VI-A | Capability-Building Education Right | `core_06-06_rights_part_b.md:480` | 3, 5, 11.1, linked | 2, 3.1, 5, 5.1, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Educational Agency | complete |
| VI-B | Lifelong and Adaptive Learning and Contestability | `core_06-06_rights_part_b.md:509` | 4.2, 5, 10, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity, Accessibility, Educational Agency | complete |
| VII | Self-Ownership | `core_06-06_rights_part_b.md:543` | None | 2, 3.1, 3.2, 6.2, 8, 10, 10.2 | Tetrad, Aims, material stake | Avoidable Burden | weak_trace |
| VII-A | Self-Ownership of Body and Mind | `core_06-06_rights_part_b.md:564` | 5, 5.1, 6.3, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 10, 10.2 | Tetrad, Aims | Avoidable Burden | complete |
| VII-B | Internal-State Boundary and Type-N Protection | `core_06-06_rights_part_b.md:596` | 4.2, 5, 5.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Trustworthiness | complete |
| VII-C | Mental-Health Crisis and Involuntary-Intervention Floor | `core_06-06_rights_part_b.md:631` | 5, 5.1, 8.1.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Trustworthiness | complete |
| VII-D | Family, Care Relationships, Reproductive Autonomy, and Non-Separation | `core_06-06_rights_part_b.md:676` | 4.2, 5, 5.1, 8.16, 9, 10.1.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Substantive Fairness | complete |
| VII-E | Voluntary Discontinuation of One's Own Existence | `core_06-06_rights_part_b.md:759` | 5, 5.1, 8.1.1, 10.1.1, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Timely Resolution | complete |
| VIII | Likeness, Experiential Data, and Publication Rights | `core_06-06_rights_part_b.md:816` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Avoidable Burden | weak_trace |
| VIII-A | Self-Ownership of Likeness and Reputation | `core_06-06_rights_part_b.md:837` | 4.2, 5, 9.2, linked | 3.2, 5, 5.1, 6.2, 8, 10, 10.2 | Tetrad, Aims | None | complete |
| VIII-B | Experiential and Derived Data Rights | `core_06-06_rights_part_b.md:876` | 5, 6.3, 9.2, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | None | complete |
| VIII-C | Truthful Publication and High-Impact Publication Limits | `core_06-06_rights_part_b.md:922` | 4.2, 9.2, 11.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity | complete |
| VIII-D | Creative Work, Training-Data Use, and Anti-Displacement | `core_06-06_rights_part_b.md:967` | 4.2, 5, 6.1.2, 6.3.1, 8.16, 9, 10, 11.1, 11.3, 13.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint | complete |
| IX | Self-Determination and Agency | `core_06-06_rights_part_b.md:1021` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden | weak_trace |
| IX-A | Agency and Freedom from Manipulation | `core_06-06_rights_part_b.md:1055` | 5, 5.1, 10, linked | 2, 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity | complete |
| IX-B | Stakeholder Role and Participation Rights | `core_06-06_rights_part_b.md:1086` | 5, 6.3, 11.1, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Educational Agency | complete |
| IX-C | Governance Participation and Voting Entitlement | `core_06-06_rights_part_b.md:1131` | 5, 6.3, 8.1, 13, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity, Substantive Fairness | complete |
| IX-D | Inclusion and Exclusion Challenge Rights | `core_06-06_rights_part_b.md:1162` | 5, 6.3, 13, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity | complete |
| X | Cooperative Interaction | `core_06-06_rights_part_b.md:1190` | None | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint | weak_trace |
| X-A | Non-Imposition and Consent in Association | `core_06-06_rights_part_b.md:1222` | 5, 5.1, 10.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Avoidable Burden, Dependency / Resource Flow, Educational Agency | complete |
| X-B | Collective Harm Boundary and Enforcement Interface | `core_06-06_rights_part_b.md:1260` | 4.1, 5.1, 9, 10.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Ecological Footprint, Dependency / Resource Flow, Substantive Fairness, Educational Agency | complete |
| X-C | Adult consensual commercial sexual services and sexual exploitation | `core_06-06_rights_part_b.md:1304` | 4.1, 6.3, 10.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Dependency / Resource Flow, Substantive Fairness | complete |
| XI | Stakeholder System Participation, Representation, and Due Process | `core_06-06_rights_part_b.md:1363` | 8.1 | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Dependency / Resource Flow, Accessibility | manual_review |
| XI-A | Stakeholder System Participation and Representation | `core_06-06_rights_part_b.md:1403` | 4.2, 5, 11.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Dependency / Resource Flow, Accessibility | complete |
| XI-B | Weighted Participation Constraints | `core_06-06_rights_part_b.md:1434` | 5, 8.1, 10, 11.1, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Dependency / Resource Flow | complete |
| XI-C | Legitimacy Gate and Anti-Token Participation | `core_06-06_rights_part_b.md:1466` | 4.2, 5, 13, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity, Accessibility | complete |
| XI-D | Internal Roles, Accountability, and Due-Process Requirements | `core_06-06_rights_part_b.md:1496` | 4.2, 6.3, 10, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity, Accessibility | complete |
| XI-E | Non-Capture Safeguards | `core_06-06_rights_part_b.md:1534` | 4.2, 10, 11.1, linked | 3.2, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity | complete |
| XII | Right to Reliable and Trustworthy Systems | `core_06-06_rights_part_c.md:32` | None | 2, 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Dependency / Resource Flow, Trustworthiness, Timely Resolution | weak_trace |
| XII-A | Reliability and Trustworthiness Baseline | `core_06-06_rights_part_c.md:71` | 4.1, 4.2, 5, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10.2 | Aims | Trustworthiness | complete |
| XII-B | Right to Challenge, Review, and Redress | `core_06-06_rights_part_c.md:98` | 4.1, 4.2, 6.3, linked | 2, 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10.2 | Tetrad, Aims, material stake | Avoidable Burden, Accessibility, Trustworthiness, Timely Resolution | complete |
| XII-C | Prohibition of False Trust and Misleading Reliance | `core_06-06_rights_part_c.md:132` | 4.2, 5, 9.2, linked | 3.2, 4, 6.2, 8, 10.2 | Tetrad, Aims | Trustworthiness | complete |
| XII-D | Incentive-Alignment Constraint | `core_06-06_rights_part_c.md:160` | 4.1, 5, 10, 10.2.3, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Trustworthiness, Timely Resolution | complete |
| XII-E | High-Autonomy Systems and Tool-Mediated Process Integrity | `core_06-06_rights_part_c.md:200` | 4.2, 6.3, 10, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity | complete |
| XII-F | Resilience and Self-Healing Baseline | `core_06-06_rights_part_c.md:234` | 4.1, 4.2, 5, 6.1.2, 11.1, linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Trustworthiness, Timely Resolution | complete |
| XIII | Security, Intelligence, Force, and Autonomous Coercive Systems | `core_06-06_rights_part_c.md:279` | None | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Avoidable Burden, Trustworthiness, Timely Resolution | weak_trace |
| XIII-A | Security, Intelligence, and Covert-Power Limits | `core_06-06_rights_part_c.md:315` | 4.1, 5.1, 6.3, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Avoidable Burden, Timely Resolution | complete |
| XIII-B | Use of Force, Armed Conflict, and Military-Power Limits | `core_06-06_rights_part_c.md:404` | 4.1, 5.1, 6.3.1, 8.1.2, 8.16, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint, Substantive Fairness | complete |
| XIII-C | Autonomous Lethal Systems and Autonomous Coercion Tools | `core_06-06_rights_part_c.md:461` | 4.1, 5, 6.3.1, 7.3.1, 8.1.1, 8.1.2, 8.16, linked | 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity, Ecological Footprint, Trustworthiness | complete |
| XIV | Info-Sphere Integrity | `core_06-06_rights_part_c.md:513` | 4.2, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint, Trustworthiness, Timely Resolution | manual_review |
| XIV-A | Info-Sphere Plurality and Anti-Monopoly | `core_06-06_rights_part_c.md:550` | 4.2, 5, 10.2.3, 11.1, linked | 2, 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity | complete |
| XIV-B | Transparency, Auditability, and Contestability | `core_06-06_rights_part_c.md:583` | 4.2, 9.2, 13, linked | 3.2, 6.2, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Ecological Footprint, Accessibility | complete |
| XIV-C | Validation, Reporting, and Epistemic Stewardship | `core_06-06_rights_part_c.md:618` | 4.2, 9.2, 10.2, 11.1, linked | 3.2, 6.2, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint, Accessibility | complete |
| XV | Audit, Transparency, and Independent Verification | `core_06-06_rights_part_c.md:650` | None | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Dependency / Resource Flow, Accessibility, Timely Resolution | weak_trace |
| XV-A | Auditability and Observable Evidence | `core_06-06_rights_part_c.md:694` | 4.2, 9.2, 13, linked | 3.2, 6.2, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity | complete |
| XV-B | Distributed Oversight and Anti-Monopoly Review | `core_06-06_rights_part_c.md:717` | 4.2, 10, 11.1, linked | 3.2, 6.2, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity | complete |
| XV-C | Verification Accessibility | `core_06-06_rights_part_c.md:741` | 5, 10.1, 13, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity, Accessibility, Timely Resolution | complete |
| XVI | System Lifecycle, Environments, and Reversibility | `core_06-06_rights_part_c.md:771` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint, Dependency / Resource Flow, Proportionate Cross-System Support, Timely Resolution | weak_trace |
| XVI-A | Lifecycle Governance and Environment Separation | `core_06-06_rights_part_c.md:811` | 4.1, 11.1, 13, linked | 3.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Ecological Footprint | complete |
| XVI-B | Progressive Deployment and Reversibility | `core_06-06_rights_part_c.md:843` | 4.1, 10.1, 11.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | Productive Capacity, Dependency / Resource Flow | complete |
| XVI-C | Misclassification and Evasion Consequences | `core_06-06_rights_part_c.md:873` | 4.2, 11.1, 13, linked | 3.2, 6.1, 6.2, 6.3, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity | complete |
| XVII | Sandboxed Innovation, Experimentation, and Creative Freedom | `core_06-06_rights_part_c.md:898` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint, Dependency / Resource Flow, Educational Agency, Timely Resolution | weak_trace |
| XVII-A | Sandboxed Scope | `core_06-06_rights_part_c.md:921` | 4.1, 5, 11.1, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Productive Capacity | complete |
| XVII-B | Containment, Disclosure, and Opt-In | `core_06-06_rights_part_c.md:951` | 4.1, 5, 10.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Dependency / Resource Flow, Proportionate Cross-System Support | complete |
| XVII-C | Transition to Higher-Obligation Regimes | `core_06-06_rights_part_c.md:982` | 4.1, 11.1, 13, linked | 3.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Timely Resolution | complete |
| XVII-D | Innovation Reward, Disclosure, and Anti-Enclosure | `core_06-06_rights_part_c.md:1008` | 4.2, 5, 10, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Accessibility, Educational Agency, Timely Resolution | complete |
| XVII-E | Scientific Publication, Review, and Replication Integrity | `core_06-06_rights_part_c.md:1086` | 4.2, 9.2, 13, linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Educational Agency, Trustworthiness | complete |
| XVIII | Standing and Participation Status | `core_06-06_rights_part_c.md:1137` | 8.1 | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims, material stake | Avoidable Burden, Substantive Fairness, Timely Resolution | manual_review |
| XVIII-A | Standing Distinction | `core_06-06_rights_part_c.md:1182` | 5, 13, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Trustworthiness | complete |
| XVIII-B | Contestability and Proportional Restriction Limits | `core_06-06_rights_part_c.md:1223` | 5, 6.3, 10.1, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Accessibility, Trustworthiness, Timely Resolution | complete |
| XVIII-C | Good Standing, Responsibility, and Continuous Audit | `core_06-06_rights_part_c.md:1273` | 5, 8.1, 10, 11.1, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Substantive Fairness | complete |
| XVIII-D | Movement, Migration, Refuge, and Non-Statelessness Routing | `core_06-06_rights_part_c.md:1318` | None | 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 10, 10.2 | Tetrad | Avoidable Burden | weak_trace |
| XIX | Interoperability, Portability, Movement, Refuge, and Exit Integrity | `core_06-06_rights_part_c.md:1339` | 8.20, 8.24 | 3.1, 5, 5.1, 6.1, 6.3, 7, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Ecological Footprint, Dependency / Resource Flow, Timely Resolution | manual_review |
| XIX-A | Portability Rights | `core_06-06_rights_part_c.md:1380` | 5, 10.1, 11.1, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Timely Resolution | complete |
| XIX-B | Reciprocal Interoperability Boundaries | `core_06-06_rights_part_c.md:1408` | 5, 10.1, 11.1, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Dependency / Resource Flow | complete |
| XIX-C | Anti-Lock-In Rule | `core_06-06_rights_part_c.md:1432` | 5, 10, 11.1, linked | 5, 5.1, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Dependency / Resource Flow | complete |
| XIX-D | Movement, Migration, Refuge, and Non-Statelessness | `core_06-06_rights_part_c.md:1461` | 4.1, 5, 5.1, 6.3.1, 8.1.1, 8.24, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Substantive Fairness, Timely Resolution | complete |
| XX | Comprehensibility and Complexity Stewardship | `core_06-06_rights_part_c.md:1534` | 3.4, 6.1.2, 9.2, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Accessibility, Timely Resolution | manual_review |
| XX-A | Proportional Comprehensibility Right | `core_06-06_rights_part_c.md:1583` | 3.4, 4.2, 5, 6.1.2, 9.2, 11.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, material stake | Avoidable Burden, Productive Capacity, Accessibility | complete |
| XX-B | Complexity Audit and Modularity Requirements | `core_06-06_rights_part_c.md:1612` | 4.1, 11.1, 13, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Dependency / Resource Flow | complete |
| XXI | Root Cause Analysis and Adaptive Response | `core_06-06_rights_part_c.md:1647` | 4.1, 4.2, 10.1, 11.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Ecological Footprint, Dependency / Resource Flow, Timely Resolution | manual_review |
| XXI-A | Diagnostic Rigor and Causal Attribution | `core_06-06_rights_part_c.md:1692` | 4.1, 4.2, 11.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity | complete |
| XXI-B | Auditability, Challenge, and Reversibility Preference | `core_06-06_rights_part_c.md:1722` | 4.1, 10.1, 11.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Timely Resolution | complete |
| XXII | Constitutional Interpretation, Review, and Anti-Capture Safeguards | `core_06-06_rights_part_c.md:1753` | 4.2, 6.3, 10, 13, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Dependency / Resource Flow | manual_review |
| XXII-A | Bounded Interpretive Mandate | `core_06-06_rights_part_c.md:1797` | 6.3, 7, 13, linked | 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity | complete |
| XXII-B | Composition, Rotation, and Conflict Controls | `core_06-06_rights_part_c.md:1830` | 6.3, 10, 13, linked | 3.2, 6.1, 6.2, 6.3, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity | complete |
| XXII-C | Public Reasons, Challenge Rights, and External Review | `core_06-06_rights_part_c.md:1864` | 4.2, 6.3, 13, linked | 3.2, 6.1, 6.2, 6.3, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity, Accessibility | complete |
| XXII-D | Removal for Cause and Non-Entrenchment | `core_06-06_rights_part_c.md:1905` | 6.3, 10, 13, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity | complete |
| XXIII | Conflict Resolution, Escalation, and Emergency Proportionality | `core_06-06_rights_part_d.md:32` | None | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Avoidable Burden, Timely Resolution | weak_trace |
| XXIII-A | Justice Objective and Scope | `core_06-06_rights_part_d.md:63` | 4.1, 6.3, 13, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity | complete |
| XXIII-B | Non-Trivial Restriction, Restitution, and Restorative-Accountability Constraints | `core_06-06_rights_part_d.md:91` | 4.1, 6.3, 10.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden | complete |
| XXIII-C | Least-Restrictive and Time-Bounded Rule | `core_06-06_rights_part_d.md:135` | 6.3, 10.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Avoidable Burden, Substantive Fairness, Timely Resolution | complete |
| XXIII-D | Emergency Measures and Continuation Burden | `core_06-06_rights_part_d.md:175` | 4.1, 6.3, 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Ecological Footprint, Timely Resolution | complete |
| XXIV | Timely Retrospective Review and Restorative Alignment | `core_06-06_rights_part_d.md:225` | None | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad, material stake | Avoidable Burden, Timely Resolution | missing_ch0_measurement_frame, weak_trace |
| XXIV-A | Retrospective Review and Disclosure | `core_06-06_rights_part_d.md:249` | 4.2, 9.2, 13, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity | complete |
| XXIV-B | Rights-Collision Procedure and Restorative Alignment | `core_06-06_rights_part_d.md:284` | 6.3, 6.3.1, 13, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity, Timely Resolution | complete |
| XXIV-C | Timely Resolution and Anti-Delay Floor | `core_06-06_rights_part_d.md:320` | 6.1.2, 6.3, 13.2, linked | 3.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Constitutional Efficiency, Avoidable Burden, Productive Capacity, Accessibility, Timely Resolution | complete |
| XXV | Constitutional Evolution and Non-Entrenchment | `core_06-06_rights_part_d.md:352` | 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity | manual_review |
| XXV-A | Non-Entrenchment and Revisability | `core_06-06_rights_part_d.md:374` | 3, 11.1, linked | 2, 3.1, 3.2, 6.2, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity | complete |
| XXV-B | Periodic Revalidation and Transparent Change | `core_06-06_rights_part_d.md:403` | 4.2, 11.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity, Substantive Fairness, Educational Agency | complete |
| XXVI | Transition Governance, Continuity, and Re-Baselining | `core_06-06_rights_part_d.md:434` | linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Avoidable Burden, Trustworthiness, Timely Resolution | manual_review |
| XXVI-A | Phased Adoption and Rights-Floor Continuity | `core_06-06_rights_part_d.md:458` | 4.1, 10.1, 11.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Substantive Fairness, Accessibility, Timely Resolution | complete |
| XXVI-B | Transitional Authority Limits and Reauthorization | `core_06-06_rights_part_d.md:487` | 4.1, 10.1, linked | 3.1, 6.1, 6.3, 7, 8, 10, 10.2 | Tetrad | Avoidable Burden, Timely Resolution | complete |
| XXVI-C | Failure Off-Ramps, Re-Baselining, and Traceability | `core_06-06_rights_part_d.md:521` | 4.1, 10.1, 13, linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Avoidable Burden, Productive Capacity, Trustworthiness, Timely Resolution | complete |
| XXVI-D | Non-Compliant Property and Systems; Voluntary Turnover Incentives | `core_06-06_rights_part_d.md:556` | 4.1, 6.3, 11.1, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Substantive Fairness, Trustworthiness | complete |

## Chapter 1 Rights Surface

| Principle | Title | File | Chapter 6 references |
|---|---|---|---:|
| 1 | Purpose and Role | `core_01_a_values_principles.md:57` | 4 |
| 2 | Foundational Objective: Wellbeing | `core_01_a_values_principles.md:100` | 4 |
| 2.1 | Fairness | `core_01_a_values_principles.md:145` | 5 |
| 2.2 | Recognition, Reinforcement, and Aspiration | `core_01_a_values_principles.md:221` | 1 |
| 3 | Non-Negotiable Constraints: Safety and Truth | `core_01_a_values_principles.md:308` | 0 |
| 3.1 | Safety (Harm Constraint) | `core_01_a_values_principles.md:326` | 9 |
| 3.2 | Truth (Epistemic Integrity Constraint) | `core_01_a_values_principles.md:365` | 6 |
| 3.3 | Science-Informed Inquiry and Decision Support | `core_01_a_values_principles.md:404` | 5 |
| 3.4 | Plain-Language Accessibility (Stewardship Duty) | `core_01_a_values_principles.md:455` | 5 |
| 4 | System Stability Enabler: Trust (Coordination Integrity) | `core_01_a_values_principles.md:545` | 6 |
| 4.1 | Resilience and Self-Healing Design | `core_01_a_values_principles.md:588` | 5 |
| 5 | Freedom (Bounded Agency) | `core_01_a_values_principles.md:630` | 10 |
| 5.1 | Limitation Discipline | `core_01_a_values_principles.md:676` | 0 |
| 5.2 | Voluntary Discontinuation and Exit Rights | `core_01_a_values_principles.md:710` | 0 |
| 5.3 | Assembly, Collective Organization, and Institutional Formation | `core_01_a_values_principles.md:739` | 0 |
| 6 | Interaction and Conflict Resolution | `core_01_a_values_principles.md:777` | 3 |
| 6.1 | Core Tradeoff Principles | `core_01_a_values_principles.md:801` | 0 |
| 6.2 | Epistemic Disclosure Constraints | `core_01_a_values_principles.md:913` | 4 |
| 6.3 | Rights-Collision Procedure | `core_01_a_values_principles.md:1020` | 9 |
| 7 | Prohibition on Absolute Override | `core_01_a_values_principles.md:1093` | 5 |
| 8 | Constitutional Interpretation | `core_01_a_values_principles.md:1127` | 2 |
| 8.1 | Definitional layer and required disciplines | `core_01_a_values_principles.md:1157` | 0 |
| 8.2 | Ambiguity resolution | `core_01_a_values_principles.md:1169` | 0 |
| 8.3 | Conflict resolution procedure | `core_01_a_values_principles.md:1182` | 0 |
| 9 | Stewardship and Distributed Understanding | `core_01_c_stewardship_capacity_principles.md:104` | 9 |
| 9.1 | Stewardship | `core_01_c_stewardship_capacity_principles.md:158` | 1 |
| 9.2 | Distributed Understanding | `core_01_c_stewardship_capacity_principles.md:190` | 2 |
| 9.3 | Institutional Development | `core_01_c_stewardship_capacity_principles.md:220` | 1 |
| 9.4 | Openness Aspiration | `core_01_c_stewardship_capacity_principles.md:253` | 2 |
| 10 | Governance Under Stewardship Discipline | `core_01_c_stewardship_capacity_principles.md:291` | 0 |
| 10.1 | Governance as Authorized Structure | `core_01_c_stewardship_capacity_principles.md:310` | 0 |
| 10.2 | Incentive Alignment and System Capture | `core_01_c_stewardship_capacity_principles.md:334` | 7 |
| 10.3 | Stewardship and Operator Incentive Alignment | `core_01_c_stewardship_capacity_principles.md:511` | 0 |
| 11 | Shared-System Capacity | `core_01_c_stewardship_capacity_principles.md:561` | 8 |
| 11.1 | Productive Capacity (Instrumental Good) | `core_01_c_stewardship_capacity_principles.md:599` | 1 |
| 11.2 | Constitutional Efficiency | `core_01_c_stewardship_capacity_principles.md:628` | 0 |
| 12 | Market Structure | `core_01_c_stewardship_capacity_principles.md:644` | 3 |
| 12.1 | Concentration Threshold Mechanism (Adopter-Tunable) | `core_01_c_stewardship_capacity_principles.md:678` | 4 |
| 12.2 | Pro-Competition and Anti-Domination | `core_01_c_stewardship_capacity_principles.md:714` | 0 |
| 12.3 | Consolidation Ceiling | `core_01_c_stewardship_capacity_principles.md:751` | 0 |
| 13 | Systemic Evaluation Requirement | `core_01_c_stewardship_capacity_principles.md:798` | 0 |
| 13.1 | Required Evaluation Factors | `core_01_c_stewardship_capacity_principles.md:834` | 16 |
| 13.2 | Governance and Incentive Discipline | `core_01_c_stewardship_capacity_principles.md:985` | 1 |
| 14 | Integrated Application | `core_01_c_stewardship_capacity_principles.md:1000` | 4 |

## Chapter 0 Measurement Coverage

| Measurement family | Chapter 6 items referencing family |
|---|---:|
| Constitutional Efficiency | 6 |
| Avoidable Burden | 76 |
| Productive Capacity | 80 |
| Ecological Footprint | 36 |
| Dependency / Resource Flow | 38 |
| Proportionate Cross-System Support | 5 |
| Substantive Fairness | 26 |
| Accessibility | 25 |
| Educational Agency | 15 |
| Trustworthiness | 20 |
| Timely Resolution | 35 |

## Findings

### Missing Ch0 Measurement Frame

- **MEDIUM** `core_06-06_rights_part_d.md:225` `XXIV` — Missing top-level Chapter 0 frame signal(s): Aims.

### Weak Trace

- **MEDIUM** `core_06-06_rights_part_a.md:116` `I` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_a.md:271` `II` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_a.md:474` `III` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_a.md:695` `IV` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_b.md:445` `VI` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_b.md:543` `VII` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_b.md:816` `VIII` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_b.md:1021` `IX` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_b.md:1190` `X` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_c.md:32` `XII` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_c.md:279` `XIII` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_c.md:650` `XV` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_c.md:771` `XVI` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_c.md:898` `XVII` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_c.md:1318` `XVIII-D` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_d.md:32` `XXIII` — Chapter 1 basis is inferred from subject matter, not directly cited.
- **MEDIUM** `core_06-06_rights_part_d.md:225` `XXIV` — Chapter 1 basis is inferred from subject matter, not directly cited.

### Manual Review

- **LOW** `core_06-06_rights_part_b.md:57` `V` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_b.md:1363` `XI` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_c.md:513` `XIV` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_c.md:1137` `XVIII` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_c.md:1339` `XIX` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_c.md:1534` `XX` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_c.md:1647` `XXI` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_c.md:1753` `XXII` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_d.md:352` `XXV` — Top-level article frame is structurally present; semantic adequacy remains for human review.
- **LOW** `core_06-06_rights_part_d.md:434` `XXVI` — Top-level article frame is structurally present; semantic adequacy remains for human review.

## Remediation Roadmap

1. Fix any broken cross-layer links before semantic editing.
2. Resolve owner-boundary and overreach findings before adding explanatory trace prose.
3. Add or clarify Chapter 0 measurement-family routing only where the right actually depends on measurement.
4. Use manual-review rows as a reading list for doctrinal adequacy, not as automatic edit instructions.
