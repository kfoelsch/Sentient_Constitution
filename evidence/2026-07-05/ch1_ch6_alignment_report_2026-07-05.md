# Chapter 0/1 -> Chapter 6 Alignment Audit Report

**Date:** 2026-07-05
**Workflow:** CH0_CH1_CH6_ALIGNMENT_AUDIT
**Auditor:** Automated static extraction with manual-review flags

## Average-Reader Dashboard

**Overall status:** `FAIL`

The audit found at least one high-priority cross-layer issue, such as a broken link, owner-boundary risk, or overreach flag. The rights surface should be reviewed before treating this pass as clean.

### What Is Strong

- Chapter 6 article/subarticle inventory was discovered across all four rights files: `124` items.
- Direct Chapter 1 trace exists for `107/124` Chapter 6 items.
- Chapter 0 measurement frame signals are structurally visible on `37/124` items.
- Explicit Chapter Zero §3 category traces or anchors appear on `53/124` items.

### What Needs Review

- Measurement-family routing is clear or not required for `124/124` items.
- Static semantic review flags remain: `10`.
- Non-manual findings remain: `25`.

### What May Need Edits

- `broken_link` at `core_06-06_rights_part_c.md:1539` (core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty): Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- `broken_link` at `core_06-06_rights_part_c.md:1577` (core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty): Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- `broken_link` at `core_06-06_rights_part_c.md:1581` (core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty): Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- `broken_link` at `core_06-06_rights_part_c.md:1588` (core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty): Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- `broken_link` at `core_06-06_rights_part_d.md:208` (core_01_a_values_principles.md#constitutional-no-bypass-principle): Target anchor `#constitutional-no-bypass-principle` not found in `core_01_a_values_principles.md`.
- `broken_link` at `core_06-06_rights_part_d.md:429` (core_01_a_values_principles.md#constitutional-no-bypass-principle): Target anchor `#constitutional-no-bypass-principle` not found in `core_01_a_values_principles.md`.
- `broken_link` at `core_06-06_rights_part_d.md:454` (core_01_a_values_principles.md#constitutional-no-bypass-principle): Target anchor `#constitutional-no-bypass-principle` not found in `core_01_a_values_principles.md`.
- `weak_trace` at `core_06-06_rights_part_a.md:116` (I): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_a.md:271` (II): Chapter 1 basis is inferred from subject matter, not directly cited.
- `weak_trace` at `core_06-06_rights_part_a.md:474` (III): Chapter 1 basis is inferred from subject matter, not directly cited.
- Plus `15` additional machine-review item(s).

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
| Items with explicit Chapter Zero §3 trace or anchor signal | 53/124 | PASS |
| Items with clear measurement routing or no measurement dependency | 124/124 | PASS |
| Broken or ambiguous Chapter 0/1/6 links | 7 | FAIL |
| Owner-boundary risks | 0 | PASS |
| Potential overreach flags | 0 | PASS |
| Manual semantic-review items | 10 | REVIEW |

## Chapter 6 Article Traceability

| Article | Title | File | Chapter 1 basis | Inferred basis | Chapter 0 frame | Measurements | Status |
|---|---|---|---|---|---|---|---|
| I | Environmental Survival | `core_06-06_rights_part_a.md:116` | None | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity | weak_trace |
| I-A | Environmental Preconditions and Ecological Integrity | `core_06-06_rights_part_a.md:136` | 3, 4.1, 6.3.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Ecological Footprint / Environmental Preconditions | complete |
| I-B | Ecological Footprint and Transparency | `core_06-06_rights_part_a.md:173` | 4.2, 9.2, linked | 2, 3.1, 3.2, 6.2, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| I-C | Intergenerational Responsibility | `core_06-06_rights_part_a.md:200` | 3, 4.1, 8.16, 8.21, 9, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity | complete |
| I-D | Existential Risk and Ecological Recovery Capacity | `core_06-06_rights_part_a.md:230` | 4.1, 9, 10.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| II | Material Stewardship and Durable-Use Integrity | `core_06-06_rights_part_a.md:271` | None | 2, 3.1, 3.2, 6.2, 7, 8, 9, 9.2 | Tetrad, Aims, material stake | Wellbeing, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity, Privacy / Data Stewardship | weak_trace |
| II-A | Material Stewardship and Lifecycle Honesty | `core_06-06_rights_part_a.md:299` | 4.2, 10.1, linked | 3.2, 4, 6.2, 7, 8, 9, 9.2, 10.2 | Tetrad, Aims, material stake | Ecological Footprint / Environmental Preconditions, Accessibility, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness | complete |
| II-B | Repair, Maintenance, and Independent Servicing | `core_06-06_rights_part_a.md:332` | 4.1, 4.2, 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Dependency / Resource Flow, Truth / Epistemic Integrity | complete |
| II-C | Designed Obsolescence and Incentive Discipline | `core_06-06_rights_part_a.md:365` | 4.1, 10, 10.1, 11, linked | 3.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Safety / Harm / Risk, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| II-D | Post-Sale Access and Subscription Integrity | `core_06-06_rights_part_a.md:395` | 4.2, 5, 10, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Trustworthiness | complete |
| II-E | Info-Sphere Dependency, Continuity, and Operator Non-Viability | `core_06-06_rights_part_a.md:424` | 4.1, 10.1, 11.6, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability | complete |
| III | Survival and Equal Educational Access | `core_06-06_rights_part_a.md:474` | None | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Educational Agency | weak_trace |
| III-A | Survival | `core_06-06_rights_part_a.md:496` | 3, 4.1, 5, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Market Structure / Contestability, Timely Resolution | complete |
| III-B | Equal Educational Access | `core_06-06_rights_part_a.md:548` | 3, 4.2, 5, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad | Wellbeing, Safety / Harm / Risk, Productive Capacity, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Accessibility, Educational Agency, Truth / Epistemic Integrity | complete |
| III-C | Bodily-Maintenance and Healthcare Access | `core_06-06_rights_part_a.md:585` | 3, 5, 5.1, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Wellbeing, Safety / Harm / Risk, Survival-floor access, Ecological Footprint / Environmental Preconditions, Substantive Fairness | complete |
| III-D | Labor and Economic Floor | `core_06-06_rights_part_a.md:632` | 3, 5, 5.1, 8.16, 9, 11.1.3, 13, linked | 2, 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Substantive Fairness, Educational Agency, Trustworthiness, Market Structure / Contestability | complete |
| IV | Resource Allocation, Dependencies, and Ecosystem Funding | `core_06-06_rights_part_a.md:695` | None | 2, 3.1, 3.2, 6.2, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Avoidable Burden, Dependency / Resource Flow, Proportionate Cross-System Support, Incentive Alignment / Proxy Integrity | weak_trace |
| IV-A | Dependency Mapping and Resource-Flow Transparency | `core_06-06_rights_part_a.md:724` | 4.2, 10, linked | 3.2, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Wellbeing, Productive Capacity, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| IV-B | Cross-System Fairness and Sustainability | `core_06-06_rights_part_a.md:755` | 3, 8.20, 10.1, 13, 13.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Substantive Fairness, Market Structure / Contestability, Timely Resolution | complete |
| V | Equal Basic Rights | `core_06-06_rights_part_b.md:57` | linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims, material stake | Avoidable Burden, Substantive Fairness, Accessibility | manual_review |
| V-A | Dignity and Equal Moral Standing | `core_06-06_rights_part_b.md:67` | 3, 5, 8.16, linked | 2, 3.1, 5, 5.1, 7, 8 | Tetrad, Aims | Wellbeing, Productive Capacity, Substantive Fairness, Market Structure / Contestability | complete |
| V-B | Nondiscrimination | `core_06-06_rights_part_b.md:95` | 5, 6.3, 8.1, 10.1, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 8 | Tetrad, Aims | Safety / Harm / Risk, Constitutional Efficiency, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Accessibility | complete |
| V-C | Full Inclusion and Equality in Adjudication and Operations | `core_06-06_rights_part_b.md:144` | 4.1, 5, 6.3, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7, 8, 10, 10.2 | Tetrad | Safety / Harm / Risk, Survival-floor access, Constitutional Efficiency, Avoidable Burden, Substantive Fairness, Market Structure / Contestability | complete |
| V-D | Freedom of conscience, religion, and comparable worldview | `core_06-06_rights_part_b.md:178` | 5, 6.3, 10.1, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 8, 10, 10.2 | Tetrad | Safety / Harm / Risk, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Accessibility | complete |
| V-E | Sentience-Status Adjudication Floor | `core_06-06_rights_part_b.md:222` | 4.2, 8.1.1, 10.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Avoidable Burden, Resilience / Systemic Risk, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| V-F | Developing Sentients, Best-Interest, and Graduated Capability | `core_06-06_rights_part_b.md:267` | 4.2, 5, 5.1, 8.1, 8.1.1, 8.16, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Productive Capacity, Resilience / Systemic Risk, Substantive Fairness, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| V-G | Accessibility | `core_06-06_rights_part_b.md:329` | 3, 4.1, 5, 5.1, 6.3.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Wellbeing, Survival-floor access, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Accessibility, Educational Agency, Truth / Epistemic Integrity | complete |
| V-H | Expression, Assembly, and Press | `core_06-06_rights_part_b.md:392` | 4.2, 5, 5.1, 6.3.1, 7.2.1, 8.1.2, 8.16, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10.2 | Tetrad | Avoidable Burden, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Educational Agency, Truth / Epistemic Integrity | complete |
| VI | Right to Sentient-Centered Education | `core_06-06_rights_part_b.md:445` | None | 2, 3.1, 3.2, 5, 5.1, 6.2, 8 | Tetrad, Aims, material stake | Wellbeing, Survival-floor access, Avoidable Burden, Productive Capacity, Substantive Fairness, Accessibility, Educational Agency | weak_trace |
| VI-A | Capability-Building Education Right | `core_06-06_rights_part_b.md:480` | 3, 5, linked | 2, 3.1, 5, 5.1, 11, 12, 13 | Tetrad, Aims | Wellbeing, Productive Capacity, Educational Agency | complete |
| VI-B | Lifelong and Adaptive Learning and Contestability | `core_06-06_rights_part_b.md:509` | 4.2, 5, 10, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity, Accessibility, Educational Agency, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| VII | Self-Ownership | `core_06-06_rights_part_b.md:543` | None | 2, 3.1, 3.2, 6.2, 8, 10, 10.2 | Tetrad, Aims, material stake | Wellbeing, Survival-floor access, Avoidable Burden, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | weak_trace |
| VII-A | Self-Ownership of Body and Mind | `core_06-06_rights_part_b.md:564` | 5, 5.1, 6.3, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Avoidable Burden, Truth / Epistemic Integrity, Privacy / Data Stewardship, Incentive Alignment / Proxy Integrity | complete |
| VII-B | Internal-State Boundary and Type-N Protection | `core_06-06_rights_part_b.md:596` | 4.2, 5, 5.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness | complete |
| VII-C | Mental-Health Crisis and Involuntary-Intervention Floor | `core_06-06_rights_part_b.md:631` | 5, 5.1, 8.1.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Survival-floor access, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Trustworthiness | complete |
| VII-D | Family, Care Relationships, Reproductive Autonomy, and Non-Separation | `core_06-06_rights_part_b.md:676` | 4.2, 5, 5.1, 8.16, 9, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Substantive Fairness, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| VII-E | Voluntary Discontinuation of One's Own Existence | `core_06-06_rights_part_b.md:759` | 5, 5.1, 8.1.1, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims | Survival-floor access, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Dependency / Resource Flow, Timely Resolution | complete |
| VIII | Likeness, Experiential Data, and Publication Rights | `core_06-06_rights_part_b.md:816` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity | weak_trace |
| VIII-A | Self-Ownership of Likeness and Reputation | `core_06-06_rights_part_b.md:837` | 4.2, 5, 9.2, linked | 3.2, 5, 5.1, 6.2, 7, 8, 10, 10.2 | Tetrad, Aims | Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability | complete |
| VIII-B | Experiential and Derived Data Rights | `core_06-06_rights_part_b.md:876` | 5, 6.3, 9.2, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| VIII-C | Truthful Publication and High-Impact Publication Limits | `core_06-06_rights_part_b.md:922` | 4.2, 9.2, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Safety / Harm / Risk, Resilience / Systemic Risk, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| VIII-D | Creative Work, Training-Data Use, and Anti-Displacement | `core_06-06_rights_part_b.md:967` | 4.2, 5, 6.1.3, 6.3.1, 8.16, 9, 10, 12.1, 13.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Survival-floor access, Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability | complete |
| IX | Self-Determination and Agency | `core_06-06_rights_part_b.md:1021` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | weak_trace |
| IX-A | Agency and Freedom from Manipulation | `core_06-06_rights_part_b.md:1055` | 5, 5.1, 10, linked | 2, 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| IX-B | Stakeholder Role and Participation Rights | `core_06-06_rights_part_b.md:1086` | 5, 6.3, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10.2, 11, 12, 13 | Tetrad, material stake | Survival-floor access, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Educational Agency, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| IX-C | Governance Participation and Voting Entitlement | `core_06-06_rights_part_b.md:1131` | 5, 6.3, 8.1, 15, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity, Substantive Fairness | complete |
| IX-D | Inclusion and Exclusion Challenge Rights | `core_06-06_rights_part_b.md:1162` | 5, 6.3, 15, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Market Structure / Contestability | complete |
| X | Cooperative Interaction | `core_06-06_rights_part_b.md:1190` | None | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Incentive Alignment / Proxy Integrity | weak_trace |
| X-A | Non-Imposition and Consent in Association | `core_06-06_rights_part_b.md:1222` | 5, 5.1, 10.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Dependency / Resource Flow, Educational Agency, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| X-B | Collective Harm Boundary and Enforcement Interface | `core_06-06_rights_part_b.md:1260` | 4.1, 5.1, 9, 10.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Survival-floor access, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Substantive Fairness, Educational Agency, Market Structure / Contestability | complete |
| X-C | Adult consensual commercial sexual services and sexual exploitation | `core_06-06_rights_part_b.md:1304` | 4.1, 6.3, 10.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, material stake | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Truth / Epistemic Integrity | complete |
| XI | Stakeholder System Participation, Representation, and Due Process | `core_06-06_rights_part_b.md:1363` | 8.1 | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Avoidable Burden, Dependency / Resource Flow, Accessibility | manual_review |
| XI-A | Stakeholder System Participation and Representation | `core_06-06_rights_part_b.md:1403` | 4.2, 5, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Safety / Harm / Risk, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XI-B | Weighted Participation Constraints | `core_06-06_rights_part_b.md:1434` | 5, 8.1, 10, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Dependency / Resource Flow, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XI-C | Legitimacy Gate and Anti-Token Participation | `core_06-06_rights_part_b.md:1466` | 4.2, 5, 15, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XI-D | Internal Roles, Accountability, and Due-Process Requirements | `core_06-06_rights_part_b.md:1496` | 4.2, 6.3, 10, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XI-E | Non-Capture Safeguards | `core_06-06_rights_part_b.md:1534` | 4.2, 10, linked | 3.2, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XII | Right to Reliable and Trustworthy Systems | `core_06-06_rights_part_c.md:32` | None | 2, 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Dependency / Resource Flow, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Timely Resolution | weak_trace |
| XII-A | Reliability and Trustworthiness Baseline | `core_06-06_rights_part_c.md:71` | 4.1, 4.2, 5, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10.2 | Aims | Wellbeing, Safety / Harm / Risk, Survival-floor access, Truth / Epistemic Integrity, Trustworthiness | complete |
| XII-B | Right to Challenge, Review, and Redress | `core_06-06_rights_part_c.md:98` | 4.1, 4.2, 6.3, linked | 2, 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10.2 | Tetrad, Aims, material stake | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Accessibility, Truth / Epistemic Integrity, Trustworthiness, Timely Resolution | complete |
| XII-C | Prohibition of False Trust and Misleading Reliance | `core_06-06_rights_part_c.md:132` | 4.2, 5, 9.2, linked | 3.2, 4, 6.2, 7, 8, 10.2 | Tetrad, Aims | Truth / Epistemic Integrity, Trustworthiness | complete |
| XII-D | Incentive-Alignment Constraint | `core_06-06_rights_part_c.md:160` | 4.1, 5, 10, 11.5, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Productive Capacity, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Timely Resolution | complete |
| XII-E | High-Autonomy Systems and Tool-Mediated Process Integrity | `core_06-06_rights_part_c.md:200` | 4.2, 6.3, 10, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XII-F | Resilience and Self-Healing Baseline | `core_06-06_rights_part_c.md:234` | 4.1, 4.2, 5, 6.1.2, 6.1.3, linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Avoidable Burden, Resilience / Systemic Risk, Dependency / Resource Flow, Truth / Epistemic Integrity, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| XIII | Security, Intelligence, Force, and Autonomous Coercive Systems | `core_06-06_rights_part_c.md:279` | None | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Resilience / Systemic Risk, Trustworthiness, Market Structure / Contestability, Timely Resolution | weak_trace |
| XIII-A | Security, Intelligence, and Covert-Power Limits | `core_06-06_rights_part_c.md:315` | 4.1, 5.1, 6.3, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Timely Resolution | complete |
| XIII-B | Use of Force, Armed Conflict, and Military-Power Limits | `core_06-06_rights_part_c.md:404` | 4.1, 5.1, 6.3.1, 8.1.2, 8.16, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Substantive Fairness, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| XIII-C | Autonomous Lethal Systems and Autonomous Coercion Tools | `core_06-06_rights_part_c.md:461` | 4.1, 5, 6.3.1, 7.3.1, 8.1.1, 8.1.2, 8.16, linked | 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Truth / Epistemic Integrity, Trustworthiness | complete |
| XIV | Info-Sphere Integrity | `core_06-06_rights_part_c.md:513` | 4.2, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | manual_review |
| XIV-A | Info-Sphere Plurality and Anti-Monopoly | `core_06-06_rights_part_c.md:550` | 4.2, 5, 11.5, linked | 2, 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Safety / Harm / Risk, Survival-floor access, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XIV-B | Transparency, Auditability, and Contestability | `core_06-06_rights_part_c.md:583` | 4.2, 9.2, 15, linked | 3.2, 6.2, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Ecological Footprint / Environmental Preconditions, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XIV-C | Validation, Reporting, and Epistemic Stewardship | `core_06-06_rights_part_c.md:618` | 4.2, 9.2, 11, linked | 3.2, 6.2, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Ecological Footprint / Environmental Preconditions, Accessibility, Truth / Epistemic Integrity | complete |
| XV | Audit, Transparency, and Independent Verification | `core_06-06_rights_part_c.md:650` | None | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | weak_trace |
| XV-A | Auditability and Observable Evidence | `core_06-06_rights_part_c.md:694` | 4.2, 9.2, 15, linked | 3.2, 6.2, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity, Truth / Epistemic Integrity | complete |
| XV-B | Distributed Oversight and Anti-Monopoly Review | `core_06-06_rights_part_c.md:717` | 4.2, 10, linked | 3.2, 6.2, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XV-C | Verification Accessibility | `core_06-06_rights_part_c.md:741` | 5, 10.1, 15, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Productive Capacity, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XVI | System Lifecycle, Environments, and Reversibility | `core_06-06_rights_part_c.md:771` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability, Timely Resolution | weak_trace |
| XVI-A | Lifecycle Governance and Environment Separation | `core_06-06_rights_part_c.md:811` | 4.1, 15, linked | 3.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Productive Capacity, Ecological Footprint / Environmental Preconditions, Privacy / Data Stewardship | complete |
| XVI-B | Progressive Deployment and Reversibility | `core_06-06_rights_part_c.md:843` | 4.1, 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Safety / Harm / Risk, Resilience / Systemic Risk, Dependency / Resource Flow, Truth / Epistemic Integrity | complete |
| XVI-C | Misclassification and Evasion Consequences | `core_06-06_rights_part_c.md:873` | 4.2, 15, linked | 3.2, 6.1, 6.2, 6.3, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Productive Capacity, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| XVII | Sandboxed Innovation, Experimentation, and Creative Freedom | `core_06-06_rights_part_c.md:898` | None | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Educational Agency, Truth / Epistemic Integrity, Privacy / Data Stewardship, Timely Resolution | weak_trace |
| XVII-A | Sandboxed Scope | `core_06-06_rights_part_c.md:921` | 4.1, 5, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 10, 10.2 | Tetrad, Aims, material stake | Safety / Harm / Risk, Resilience / Systemic Risk | complete |
| XVII-B | Containment, Disclosure, and Opt-In | `core_06-06_rights_part_c.md:951` | 4.1, 5, 10.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | Safety / Harm / Risk, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Truth / Epistemic Integrity | complete |
| XVII-C | Transition to Higher-Obligation Regimes | `core_06-06_rights_part_c.md:982` | 4.1, 15, linked | 3.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Privacy / Data Stewardship, Timely Resolution | complete |
| XVII-D | Innovation Reward, Disclosure, and Anti-Enclosure | `core_06-06_rights_part_c.md:1008` | 4.2, 5, 10, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Accessibility, Educational Agency, Truth / Epistemic Integrity, Privacy / Data Stewardship, Timely Resolution | complete |
| XVII-E | Scientific Publication, Review, and Replication Integrity | `core_06-06_rights_part_c.md:1086` | 4.2, 9.2, 15, linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Safety / Harm / Risk, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Educational Agency, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness, Market Structure / Contestability | complete |
| XVIII | Standing and Participation Status | `core_06-06_rights_part_c.md:1137` | 8.1 | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Substantive Fairness, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | manual_review |
| XVIII-A | Standing Distinction | `core_06-06_rights_part_c.md:1182` | 5, 15, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, material stake | Productive Capacity, Trustworthiness | complete |
| XVIII-B | Contestability and Proportional Restriction Limits | `core_06-06_rights_part_c.md:1223` | 5, 6.3, 10.1, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Accessibility, Truth / Epistemic Integrity, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| XVIII-C | Good Standing, Responsibility, and Continuous Audit | `core_06-06_rights_part_c.md:1273` | 5, 8.1, 10, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Substantive Fairness | complete |
| XVIII-D | Movement, Migration, Refuge, and Non-Statelessness Routing | `core_06-06_rights_part_c.md:1318` | None | 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 10, 10.2 | Tetrad | Avoidable Burden, Market Structure / Contestability | weak_trace |
| XIX | Interoperability, Portability, Movement, Refuge, and Exit Integrity | `core_06-06_rights_part_c.md:1339` | 8.20, 8.24 | 3.1, 5, 5.1, 6.1, 6.3, 7, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Privacy / Data Stewardship, Market Structure / Contestability, Timely Resolution | manual_review |
| XIX-A | Portability Rights | `core_06-06_rights_part_c.md:1380` | 5, 10.1, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 8 | Tetrad, Aims | Safety / Harm / Risk, Avoidable Burden, Market Structure / Contestability, Timely Resolution | complete |
| XIX-B | Reciprocal Interoperability Boundaries | `core_06-06_rights_part_c.md:1408` | 5, 10.1, linked | 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Dependency / Resource Flow | complete |
| XIX-C | Anti-Lock-In Rule | `core_06-06_rights_part_c.md:1432` | 5, 10, linked | 5, 5.1, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Productive Capacity, Dependency / Resource Flow, Market Structure / Contestability | complete |
| XIX-D | Movement, Migration, Refuge, and Non-Statelessness | `core_06-06_rights_part_c.md:1461` | 4.1, 5, 5.1, 6.3.1, 8.1.1, 8.24, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Substantive Fairness, Market Structure / Contestability, Timely Resolution | complete |
| XX | Comprehensibility and Complexity Stewardship | `core_06-06_rights_part_c.md:1534` | 3.4, 6.1.2, 6.1.3, 9.2, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Survival-floor access, Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | manual_review |
| XX-A | Proportional Comprehensibility Right | `core_06-06_rights_part_c.md:1583` | 3.4, 4.2, 5, 6.1.3, 9.2, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, material stake | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Accessibility, Truth / Epistemic Integrity | complete |
| XX-B | Complexity Audit and Modularity Requirements | `core_06-06_rights_part_c.md:1612` | 4.1, 15, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Market Structure / Contestability | complete |
| XXI | Root Cause Analysis and Adaptive Response | `core_06-06_rights_part_c.md:1647` | 4.1, 4.2, 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Truth / Epistemic Integrity, Privacy / Data Stewardship, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | manual_review |
| XXI-A | Diagnostic Rigor and Causal Attribution | `core_06-06_rights_part_c.md:1692` | 4.1, 4.2, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad | Safety / Harm / Risk, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XXI-B | Auditability, Challenge, and Reversibility Preference | `core_06-06_rights_part_c.md:1722` | 4.1, 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Safety / Harm / Risk, Resilience / Systemic Risk, Incentive Alignment / Proxy Integrity, Timely Resolution | complete |
| XXII | Constitutional Interpretation, Review, and Anti-Capture Safeguards | `core_06-06_rights_part_c.md:1753` | 4.2, 6.3, 10, 15, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | manual_review |
| XXII-A | Bounded Interpretive Mandate | `core_06-06_rights_part_c.md:1797` | 6.3, 7, 15, linked | 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XXII-B | Composition, Rotation, and Conflict Controls | `core_06-06_rights_part_c.md:1830` | 6.3, 10, 15, linked | 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| XXII-C | Public Reasons, Challenge Rights, and External Review | `core_06-06_rights_part_c.md:1864` | 4.2, 6.3, 15, linked | 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad | Avoidable Burden, Productive Capacity, Accessibility, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XXII-D | Removal for Cause and Non-Entrenchment | `core_06-06_rights_part_c.md:1905` | 6.3, 10, 15, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| XXIII | Conflict Resolution, Escalation, and Emergency Proportionality | `core_06-06_rights_part_d.md:32` | None | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | weak_trace |
| XXIII-A | Justice Objective and Scope | `core_06-06_rights_part_d.md:63` | 4.1, 6.3, 15, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Safety / Harm / Risk, Productive Capacity | complete |
| XXIII-B | Non-Trivial Restriction, Restitution, and Restorative-Accountability Constraints | `core_06-06_rights_part_d.md:91` | 4.1, 6.3, 10.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Avoidable Burden | complete |
| XXIII-C | Least-Restrictive and Time-Bounded Rule | `core_06-06_rights_part_d.md:135` | 6.3, 10.1, linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | Avoidable Burden, Resilience / Systemic Risk, Substantive Fairness, Timely Resolution | complete |
| XXIII-D | Emergency Measures and Continuation Burden | `core_06-06_rights_part_d.md:175` | 4.1, 6.3, 10.1, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.2, 11, 12, 13 | Tetrad, Aims | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XXIV | Timely Retrospective Review and Restorative Alignment | `core_06-06_rights_part_d.md:225` | None | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad, material stake | Safety / Harm / Risk, Avoidable Burden, Privacy / Data Stewardship, Market Structure / Contestability, Timely Resolution | missing_ch0_measurement_frame, weak_trace |
| XXIV-A | Retrospective Review and Disclosure | `core_06-06_rights_part_d.md:249` | 4.2, 9.2, 15, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity | complete |
| XXIV-B | Rights-Collision Procedure and Restorative Alignment | `core_06-06_rights_part_d.md:284` | 6.3, 6.3.1, 15, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Market Structure / Contestability, Timely Resolution | complete |
| XXIV-C | Timely Resolution and Anti-Delay Floor | `core_06-06_rights_part_d.md:320` | 6.1.3, 6.3, 12.2, linked | 3.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Safety / Harm / Risk, Constitutional Efficiency, Avoidable Burden, Productive Capacity, Accessibility, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Timely Resolution | complete |
| XXV | Constitutional Evolution and Non-Entrenchment | `core_06-06_rights_part_d.md:352` | 10, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Wellbeing, Avoidable Burden, Productive Capacity, Incentive Alignment / Proxy Integrity | manual_review |
| XXV-A | Non-Entrenchment and Revisability | `core_06-06_rights_part_d.md:374` | 3, linked | 2, 3.1, 3.2, 6.2, 7, 8, 10, 10.2 | Tetrad | Wellbeing, Incentive Alignment / Proxy Integrity | complete |
| XXV-B | Periodic Revalidation and Transparent Change | `core_06-06_rights_part_d.md:403` | 4.2, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad | Substantive Fairness, Educational Agency, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XXVI | Transition Governance, Continuity, and Re-Baselining | `core_06-06_rights_part_d.md:434` | linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims, material stake | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Trustworthiness, Timely Resolution | manual_review |
| XXVI-A | Phased Adoption and Rights-Floor Continuity | `core_06-06_rights_part_d.md:458` | 4.1, 10.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Substantive Fairness, Accessibility, Truth / Epistemic Integrity, Timely Resolution | complete |
| XXVI-B | Transitional Authority Limits and Reauthorization | `core_06-06_rights_part_d.md:494` | 4.1, 10.1, linked | 3.1, 6.1, 6.3, 7, 8, 10, 10.2 | Tetrad | Safety / Harm / Risk, Avoidable Burden, Timely Resolution | complete |
| XXVI-C | Failure Off-Ramps, Re-Baselining, and Traceability | `core_06-06_rights_part_d.md:528` | 4.1, 10.1, 15, linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.2, 11, 12, 13 | Tetrad, Aims, material stake | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Truth / Epistemic Integrity, Trustworthiness, Timely Resolution | complete |
| XXVI-D | Non-Compliant Property and Systems; Voluntary Turnover Incentives | `core_06-06_rights_part_d.md:563` | 4.1, 6.3, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.2 | Tetrad, Aims | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Substantive Fairness, Trustworthiness | complete |

## Chapter 1 Rights Surface

| Principle | Title | File | Chapter 6 references |
|---|---|---|---:|
| 1 | Purpose and Role | `core_01_a_values_principles.md:21` | 4 |
| 2 | Foundational Objective: Wellbeing | `core_01_a_values_principles.md:60` | 4 |
| 2.1 | Fairness | `core_01_a_values_principles.md:102` | 5 |
| 2.2 | Recognition, Reinforcement, and Aspiration | `core_01_a_values_principles.md:181` | 1 |
| 3 | Non-Negotiable Principle Constraints: Safety and Truth | `core_01_a_values_principles.md:272` | 0 |
| 3.1 | Safety (Harm Constraint) | `core_01_a_values_principles.md:292` | 9 |
| 3.2 | Truth (Epistemic Integrity Constraint) | `core_01_a_values_principles.md:327` | 6 |
| 3.3 | Science-Informed Inquiry and Decision Support | `core_01_a_values_principles.md:360` | 5 |
| 3.4 | Plain-Language Accessibility (Participation and Stewardship Duty) | `core_01_a_values_principles.md:407` | 6 |
| 4 | System Stability Enabler: Trust (Coordination Integrity) | `core_01_a_values_principles.md:483` | 6 |
| 4.1 | Resilience and Self-Healing Design | `core_01_a_values_principles.md:524` | 5 |
| 5 | Freedom (Bounded Agency) | `core_01_a_values_principles.md:563` | 10 |
| 5.1 | Limitation Discipline | `core_01_a_values_principles.md:609` | 0 |
| 5.2 | Voluntary Discontinuation and Exit Rights | `core_01_a_values_principles.md:642` | 0 |
| 5.3 | Assembly, Collective Organization, and Institutional Formation | `core_01_a_values_principles.md:670` | 0 |
| 9 | Stewardship and Distributed Understanding | `core_01_c_stewardship_capacity_principles.md:42` | 9 |
| 9.1 | Consequential Stewardship | `core_01_c_stewardship_capacity_principles.md:100` | 1 |
| 9.2 | Distributed Understanding | `core_01_c_stewardship_capacity_principles.md:130` | 2 |
| 9.3 | Institutional Development | `core_01_c_stewardship_capacity_principles.md:161` | 1 |
| 9.4 | Openness Aspiration | `core_01_c_stewardship_capacity_principles.md:192` | 2 |
| 9.5 | Process-Character Discipline (Anti-Degrading-Process Principle) | `core_01_c_stewardship_capacity_principles.md:225` | 2 |
| 10 | Governance Under Stewardship Discipline | `core_01_c_stewardship_capacity_principles.md:286` | 0 |
| 10.1 | Governance as Authorized Structure | `core_01_c_stewardship_capacity_principles.md:306` | 0 |
| 11 | Incentive Alignment and System Capture | `core_01_c_stewardship_capacity_principles.md:355` | 7 |
| 11.1 | Alignment Requirement | `core_01_c_stewardship_capacity_principles.md:403` | 0 |
| 11.2 | Convenient Proxies and Proxy Divergence | `core_01_c_stewardship_capacity_principles.md:457` | 0 |
| 11.3 | Misalignment Detection | `core_01_c_stewardship_capacity_principles.md:472` | 0 |
| 11.4 | Misalignment Correction and Capture Response | `core_01_c_stewardship_capacity_principles.md:492` | 0 |
| 11.5 | Contingent Claims, Games of Chance, and Event-Contract Markets | `core_01_c_stewardship_capacity_principles.md:503` | 0 |
| 11.6 | Successor Responsibility and Formal-Structure Non-Escape | `core_01_c_stewardship_capacity_principles.md:562` | 0 |
| 12 | Shared-System Capacity | `core_01_c_stewardship_capacity_principles.md:580` | 8 |
| 12.1 | Productive Capacity (Instrumental Good) | `core_01_c_stewardship_capacity_principles.md:628` | 1 |
| 12.2 | Constitutional Efficiency | `core_01_c_stewardship_capacity_principles.md:652` | 0 |
| 13 | Market Structure | `core_01_c_stewardship_capacity_principles.md:670` | 3 |
| 13.1 | Concentration Threshold Mechanism (Adopter-Tunable) | `core_01_c_stewardship_capacity_principles.md:716` | 1 |
| 13.2 | Pro-Competition and Anti-Domination | `core_01_c_stewardship_capacity_principles.md:751` | 2 |
| 13.3 | Consolidation Ceiling | `core_01_c_stewardship_capacity_principles.md:803` | 0 |
| 14 | Systemic Evaluation Requirement | `core_01_c_stewardship_capacity_principles.md:860` | 0 |
| 15 | Integrated Application | `core_01_c_stewardship_capacity_principles.md:883` | 4 |

## Chapter 0 Measurement Coverage

| Measurement family | Chapter 6 items referencing family |
|---|---:|
| Wellbeing | 42 |
| Safety / Harm / Risk | 75 |
| Survival-floor access | 29 |
| Constitutional Efficiency | 6 |
| Avoidable Burden | 76 |
| Productive Capacity | 61 |
| Ecological Footprint / Environmental Preconditions | 36 |
| Resilience / Systemic Risk | 25 |
| Dependency / Resource Flow | 38 |
| Proportionate Cross-System Support | 5 |
| Substantive Fairness | 26 |
| Accessibility | 25 |
| Educational Agency | 15 |
| Truth / Epistemic Integrity | 74 |
| Privacy / Data Stewardship | 21 |
| Trustworthiness | 20 |
| Incentive Alignment / Proxy Integrity | 27 |
| Market Structure / Contestability | 53 |
| Timely Resolution | 35 |

## Findings

### Broken Link

- **HIGH** `core_06-06_rights_part_c.md:1539` `core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty` — Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- **HIGH** `core_06-06_rights_part_c.md:1577` `core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty` — Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- **HIGH** `core_06-06_rights_part_c.md:1581` `core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty` — Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- **HIGH** `core_06-06_rights_part_c.md:1588` `core_01_a_values_principles.md#34-plain-language-accessibility-stewardship-duty` — Target anchor `#34-plain-language-accessibility-stewardship-duty` not found in `core_01_a_values_principles.md`.
- **HIGH** `core_06-06_rights_part_d.md:208` `core_01_a_values_principles.md#constitutional-no-bypass-principle` — Target anchor `#constitutional-no-bypass-principle` not found in `core_01_a_values_principles.md`.
- **HIGH** `core_06-06_rights_part_d.md:429` `core_01_a_values_principles.md#constitutional-no-bypass-principle` — Target anchor `#constitutional-no-bypass-principle` not found in `core_01_a_values_principles.md`.
- **HIGH** `core_06-06_rights_part_d.md:454` `core_01_a_values_principles.md#constitutional-no-bypass-principle` — Target anchor `#constitutional-no-bypass-principle` not found in `core_01_a_values_principles.md`.

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
