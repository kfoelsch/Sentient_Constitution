# Chapter 0/1 -> Chapter 6 Alignment Audit Report

**Date:** 2026-10-21
**Workflow:** CH0_CH1_CH6_ALIGNMENT_AUDIT
**Auditor:** Automated static extraction with manual-review flags

## Average-Reader Dashboard

**Overall status:** `REVIEW`

The audit found a mostly usable alignment map, with some review items where trace prose, measurement routing, or semantic fit may need editorial attention. The report separates machine-checkable issues from human doctrinal review.

### What Is Strong

- Chapter 6 article/subarticle inventory was discovered across all four rights files: `140` items.
- Direct Chapter 1 trace exists for `140/140` Chapter 6 items.
- Chapter 0 measurement frame signals are structurally visible on `27/28` top-level articles.
- Explicit Preamble §3 category traces or anchors appear on `74/140` items.

### What Needs Review

- Measurement-family routing is clear or not required for `140/140` items.
- Structural findings remain: `1`.
- Doctrinal semantic adequacy is out of scope of this structural pass.

### What May Need Edits

- `missing_ch0_measurement_frame` at `core_06020_rights_part_d.md:426` (XX): Missing top-level Chapter 0 frame signal(s): material stake.

### Rights-Family Dashboard

| Rights family | Items | Direct Chapter 1 basis | Chapter 0 frame | Measurement routing | Status |
|---|---:|---:|---:|---:|---|
| survival/resources | 25 | 25/25 | 11/25 | 25/25 | PASS |
| equality/access | 22 | 22/22 | 6/22 | 22/22 | PASS |
| agency/participation | 19 | 19/19 | 7/19 | 19/19 | PASS |
| systems/trust/audit | 32 | 32/32 | 11/32 | 32/32 | PASS |
| standing/interpretation | 22 | 22/22 | 6/22 | 22/22 | PASS |
| justice/emergency/transition | 15 | 15/15 | 6/15 | 15/15 | REVIEW |

## Maintainer Metrics

| Metric | Result | Status |
|---|---:|---|
| Chapter 6 articles/subarticles discovered | 140 | PASS |
| Items with direct Chapter 1 basis | 140/140 | PASS |
| Top-level articles with Chapter 0 Tetrad/Aims/material-stake framing | 27/28 | REVIEW |
| Items with explicit Preamble §3 trace or anchor signal | 74/140 | PASS |
| Items with clear measurement routing or no measurement dependency | 140/140 | PASS |
| Broken or ambiguous Chapter 0/1/6 links | 0 | PASS |
| Owner-boundary risks | 0 | PASS |
| Potential overreach flags | 0 | PASS |
| Manual semantic-review items | 0 | PASS |

## Chapter 6 Article Traceability

| Article | Title | File | Chapter 1 basis | Inferred basis | Chapter 0 frame | Def.* | oDef | Measurements | Status |
|---|---|---|---|---|---|---|---|---|---|
| I | Environmental Survival | `core_06005_rights_part_a.md:213` | linked | 2, 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity | complete |
| I-A | Environmental Preconditions and Ecological Integrity | `core_06005_rights_part_a.md:245` | linked | 2, 3.1, 6.1, 6.1.5, 6.3, 7, 8 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions | complete |
| I-B | Ecological Footprint and Transparency | `core_06005_rights_part_a.md:308` | linked | 2, 3.1, 3.2, 6.2, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| I-C | Intergenerational Responsibility | `core_06005_rights_part_a.md:347` | linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity | complete |
| I-D | Existential Risk and Ecological Recovery Capacity | `core_06005_rights_part_a.md:379` | linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| II | Material Stewardship and Durable-Use Integrity | `core_06005_rights_part_a.md:437` | linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| II-A | Material Stewardship and Lifecycle Honesty | `core_06005_rights_part_a.md:474` | linked | 3.2, 4, 6.2, 7, 8, 9, 9.2 | Tetrad, Aims, material stake | None | None | Avoidable Burden, Ecological Footprint / Environmental Preconditions, Accessibility, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness | complete |
| II-B | Repair, Maintenance, and Independent Servicing | `core_06005_rights_part_a.md:517` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Dependency / Resource Flow, Truth / Epistemic Integrity | complete |
| II-C | Designed Obsolescence and Incentive Discipline | `core_06005_rights_part_a.md:554` | 19, linked | 3.1, 6.1, 6.1.5, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| II-D | Post-Sale Access and Subscription Integrity | `core_06005_rights_part_a.md:586` | 7, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Trustworthiness | complete |
| II-E | Data Handling and Network Dependency | `core_06005_rights_part_a.md:620` | linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Avoidable Burden, Dependency / Resource Flow, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| II-F | Continuity and Operator Shutdown | `core_06005_rights_part_a.md:688` | 19.6, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability | complete |
| III | Survival and Essential Access | `core_06005_rights_part_a.md:738` | 3.1, 5.2, 7.1, linked | 2, 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Accessibility, Educational Agency | complete |
| III-A | Survival | `core_06005_rights_part_a.md:791` | 7, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| III-B | Bodily-Maintenance and Healthcare Access | `core_06005_rights_part_a.md:837` | 7, linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Timely Resolution | complete |
| III-C | Labor and Economic Floor | `core_06005_rights_part_a.md:890` | 7, 11, 11.2, linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | cjs_05125_accountability_operations.md#distributed-and-proportional-authority-terms-c | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Substantive Fairness, Educational Agency, Privacy / Data Stewardship, Market Structure / Contestability, Timely Resolution | complete |
| III-D | Safe Working Conditions | `core_06005_rights_part_a.md:959` | linked | 2, 3.1, 4, 6.1, 6.1.5, 6.3, 7, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Privacy / Data Stewardship, Trustworthiness | complete |
| III-E | Rest and Recuperation | `core_06005_rights_part_a.md:1001` | linked | 2, 3.1, 5, 5.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Substantive Fairness | complete |
| IV | Right to Sentient-Centered Education | `core_06005_rights_part_a.md:1033` | 3.1, 5.2, 7.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2 | Tetrad, Aims, material stake | None | None | Wellbeing, Survival-floor access, Avoidable Burden, Productive Capacity, Substantive Fairness, Accessibility, Educational Agency | complete |
| IV-A | Equal Educational Access | `core_06005_rights_part_a.md:1091` | 7, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Productive Capacity, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Accessibility, Educational Agency, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| IV-B | Capability-Building Education Right | `core_06005_rights_part_a.md:1128` | 7, linked | 2, 3.1, 5, 5.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Productive Capacity, Educational Agency | complete |
| IV-C | Lifelong and Adaptive Learning and Contestability | `core_06005_rights_part_a.md:1163` | 7, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Productive Capacity, Accessibility, Educational Agency, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| V | Resource Allocation, Dependencies, and Ecosystem Funding | `core_06005_rights_part_a.md:1199` | linked | 2, 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Proportionate Cross-System Support, Incentive Alignment / Proxy Integrity | complete |
| V-A | Dependency Mapping and Resource-Flow Transparency | `core_06005_rights_part_a.md:1249` | 18, linked | 3.2, 6.2, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Productive Capacity, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| V-B | Cross-System Fairness and Sustainability | `core_06005_rights_part_a.md:1300` | 11, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Substantive Fairness, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| VI | Equal Basic Rights | `core_06010_rights_part_b.md:103` | linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims, material stake | None | None | Wellbeing, Avoidable Burden, Substantive Fairness, Accessibility, Market Structure / Contestability | complete |
| VI-A | Dignity and Equal Moral Standing | `core_06010_rights_part_b.md:138` | 7, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7, 8 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Productive Capacity, Substantive Fairness, Market Structure / Contestability | complete |
| VI-B | Sentience-Status Adjudication Floor | `core_06010_rights_part_b.md:178` | linked | 2, 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims | None | None | Avoidable Burden, Resilience / Systemic Risk, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| VI-C | Nondiscrimination | `core_06010_rights_part_b.md:223` | 7, linked | 2, 3.1, 4, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8 | Tetrad, Aims | None | None | Safety / Harm / Risk, Survival-floor access, Constitutional Efficiency, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Accessibility, Trustworthiness, Market Structure / Contestability | complete |
| VI-D | Accessibility | `core_06010_rights_part_b.md:278` | 5.2, 7, 7.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Survival-floor access, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Accessibility, Educational Agency, Truth / Epistemic Integrity | complete |
| VII | Self-Ownership | `core_06010_rights_part_b.md:350` | linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| VII-A | Self-Ownership of Body | `core_06010_rights_part_b.md:385` | 7, 7.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8 | Tetrad, Aims | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Educational Agency, Privacy / Data Stewardship | complete |
| VII-B | Self-Ownership of Mind | `core_06010_rights_part_b.md:430` | 7, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8 | Tetrad, Aims | None | None | Avoidable Burden, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness | complete |
| VII-C | Health Crisis and Involuntary-Intervention Floor | `core_06010_rights_part_b.md:472` | 7, 7.1, linked | 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Timely Resolution | complete |
| VII-D | Voluntary Discontinuation of One's Own Existence | `core_06010_rights_part_b.md:533` | 7, linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims | None | None | Survival-floor access, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Dependency / Resource Flow, Timely Resolution | complete |
| VII-E | Adult consensual commercial sexual services and sexual exploitation | `core_06010_rights_part_b.md:595` | linked | 2, 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, material stake | None | None | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Truth / Epistemic Integrity | complete |
| VIII | Family, Care, and Developing Sentients | `core_06010_rights_part_b.md:659` | linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity | complete |
| VIII-A | Family and Care Relationships | `core_06010_rights_part_b.md:696` | 7, linked | 2, 3.1, 3.2, 5, 5.1, 6.2, 7, 8, 10, 10.1 | Tetrad | None | None | Productive Capacity, Substantive Fairness, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| VIII-B | Reproductive and Lineage Autonomy | `core_06010_rights_part_b.md:731` | 7, linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 11, 12, 13 | Tetrad | None | None | Constitutional Efficiency, Productive Capacity, Dependency / Resource Flow, Substantive Fairness | complete |
| VIII-C | Derivation, Instantiation, and the Parent-System Relationship | `core_06010_rights_part_b.md:771` | 7, 11, linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Substantive Fairness, Educational Agency, Market Structure / Contestability | complete |
| VIII-D | Developing Sentients, Best-Interest, and Graduated Capability | `core_06010_rights_part_b.md:835` | 7, 7.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Productive Capacity, Resilience / Systemic Risk, Substantive Fairness, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| VIII-E | Non-Separation | `core_06010_rights_part_b.md:890` | 7.1, linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk | complete |
| IX | Likeness, Experiential Data, and Publication Rights | `core_06010_rights_part_b.md:931` | linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity | complete |
| IX-A | Self-Ownership of Likeness and Reputation | `core_06010_rights_part_b.md:966` | 7, linked | 3.2, 5, 5.1, 6.2, 7, 8, 10, 10.1 | Tetrad, Aims | None | None | Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability | complete |
| IX-B | Experiential and Derived Data Rights | `core_06010_rights_part_b.md:1009` | 7, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims | None | None | Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| IX-C | Truthful Publication and High-Impact Publication Limits | `core_06010_rights_part_b.md:1057` | linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8 | Tetrad, Aims | None | None | Safety / Harm / Risk, Resilience / Systemic Risk, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| IX-D | Creative Work, Training-Data Use, and Anti-Displacement | `core_06010_rights_part_b.md:1108` | 7, 11, 11.1, 13.3, 18, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability | complete |
| X | Self-Determination, Agency, and Participation | `core_06010_rights_part_b.md:1191` | 7, 7.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| X-A | Agency and Freedom from Manipulation | `core_06010_rights_part_b.md:1239` | 7, linked | 2, 3.1, 4, 5, 5.1, 6.1, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| X-B | Governance Participation and Voting Entitlement | `core_06010_rights_part_b.md:1272` | 7, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Productive Capacity, Substantive Fairness | complete |
| X-C | Stakeholder Role and Participation Rights | `core_06010_rights_part_b.md:1305` | 7, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, material stake | None | None | Survival-floor access, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Truth / Epistemic Integrity | complete |
| X-D | Inclusion and Exclusion Challenge Rights | `core_06010_rights_part_b.md:1354` | 7, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, material stake | None | None | Safety / Harm / Risk, Productive Capacity, Substantive Fairness, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XI | Conscience, Expression, Association, and Cooperative Interaction | `core_06010_rights_part_b.md:1393` | linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| XI-A | Freedom of conscience, religion, and comparable worldview | `core_06010_rights_part_b.md:1443` | 7, 18.2, linked | 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Accessibility | complete |
| XI-B | Expression | `core_06010_rights_part_b.md:1487` | 7, 7.1, 7.5, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Educational Agency, Truth / Epistemic Integrity | complete |
| XI-C | Press and Journalistic Activity | `core_06010_rights_part_b.md:1555` | 7, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8 | Tetrad | None | None | Truth / Epistemic Integrity | complete |
| XI-D | Assembly, Dissent, and Peaceful Protest | `core_06010_rights_part_b.md:1592` | 7, 7.3, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Timely Resolution | complete |
| XI-E | Institutional Formation and Business Creation | `core_06010_rights_part_b.md:1673` | 7.1, 7.5, 11, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Substantive Fairness, Educational Agency, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XI-F | Non-Imposition and Consent in Association | `core_06010_rights_part_b.md:1754` | 7, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Dependency / Resource Flow, Substantive Fairness, Educational Agency, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XI-G | Collective Harm Boundary and Enforcement Interface | `core_06010_rights_part_b.md:1799` | 11, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Substantive Fairness, Educational Agency, Market Structure / Contestability | complete |
| XII | Stakeholder System Participation, Representation, and Due Process | `core_06010_rights_part_b.md:1850` | linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Accessibility | complete |
| XII-A | Stakeholder System Participation and Representation | `core_06010_rights_part_b.md:1903` | 7, 20, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, material stake | None | None | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XII-B | Weighted Participation and Anti-Token Constraints | `core_06010_rights_part_b.md:1958` | 7, 18, linked | 3.2, 5, 5.1, 6.2, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Productive Capacity, Dependency / Resource Flow, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XII-C | Internal Roles, Accountability, and Due-Process Requirements | `core_06010_rights_part_b.md:2004` | linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XII-D | Non-Capture Safeguards | `core_06010_rights_part_b.md:2047` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XII-E | Influence-Contact and Lobbying Boundaries | `core_06010_rights_part_b.md:2153` | linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XIII | Right to Reliable and Trustworthy Systems | `core_06015_rights_part_c.md:74` | linked | 2, 3.1, 3.2, 4, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XIII-A | Reliability and Trustworthiness Baseline | `core_06015_rights_part_c.md:140` | 6.1, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| XIII-B | Right to Redress and Remedy | `core_06015_rights_part_c.md:196` | 6.1, linked | 2, 3.1, 3.2, 4, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| XIII-C | Prohibition of False Trust and Misleading Reliance | `core_06015_rights_part_c.md:242` | linked | 3.2, 4, 6.2, 7, 8 | Tetrad, Aims | None | None | Truth / Epistemic Integrity, Trustworthiness | complete |
| XIII-D | Incentive-Alignment Constraint | `core_06015_rights_part_c.md:272` | 19.5, linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XIII-E | High-Autonomy Systems and Tool-Mediated Process Integrity | `core_06015_rights_part_c.md:324` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XIII-F | Resilience and Self-Healing Baseline | `core_06015_rights_part_c.md:374` | 13.3, linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Resilience / Systemic Risk, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| XIV | Security, Intelligence, Force, and Autonomous Coercive Systems | `core_06015_rights_part_c.md:428` | linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Trustworthiness, Timely Resolution | complete |
| XIV-A | Security, Intelligence, and Covert-Power Limits | `core_06015_rights_part_c.md:491` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Timely Resolution | complete |
| XIV-B | Use of Force, Armed Conflict, and Military-Power Limits | `core_06015_rights_part_c.md:583` | 7.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Substantive Fairness, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability | complete |
| XIV-C | Autonomous Lethal Systems and Autonomous Coercion Tools | `core_06015_rights_part_c.md:653` | linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Truth / Epistemic Integrity, Trustworthiness | complete |
| XIV-D | Counter-Espionage Limits | `core_06015_rights_part_c.md:716` | linked | 3.1, 3.2, 4, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Substantive Fairness, Truth / Epistemic Integrity, Trustworthiness, Timely Resolution | complete |
| XV | Info-Sphere Integrity | `core_06015_rights_part_c.md:809` | linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XV-A | Info-Sphere Plurality and Anti-Monopoly | `core_06015_rights_part_c.md:857` | 19.5, linked | 2, 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, material stake | None | None | Safety / Harm / Risk, Survival-floor access, Truth / Epistemic Integrity, Trustworthiness, Market Structure / Contestability | complete |
| XV-B | Transparency, Auditability, and Contestability | `core_06015_rights_part_c.md:895` | linked | 3.2, 6.2, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, material stake | None | None | Productive Capacity, Ecological Footprint / Environmental Preconditions, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XV-C | Validation, Reporting, and Epistemic Stewardship | `core_06015_rights_part_c.md:932` | 19, linked | 3.2, 6.2, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Avoidable Burden, Ecological Footprint / Environmental Preconditions, Accessibility, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| XV-D | Scientific Publication, Review, and Replication Integrity | `core_06015_rights_part_c.md:972` | linked | 3.1, 3.2, 4, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, material stake | None | None | Safety / Harm / Risk, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Educational Agency, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness, Market Structure / Contestability | complete |
| XVI | Audit, Transparency, and Independent Verification | `core_06015_rights_part_c.md:1022` | linked | 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | cjs_05110_oversight_operations.md, cjs_05110_oversight_operations.md#cjs-34-audit-process-output-disclosure, cjs_05115_audit_process.md#cjs-5115-3--odef3-audit-process-home, cjs_05115_audit_process.md#sibling-audit-modes-owner-map | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XVI-A | Auditability and Observable Evidence | `core_06015_rights_part_c.md:1110` | linked | 3.2, 6.2, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | None | None | Productive Capacity, Truth / Epistemic Integrity | complete |
| XVI-B | Distributed Oversight and Anti-Monopoly Review | `core_06015_rights_part_c.md:1135` | 18.3, linked | 3.2, 4, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Productive Capacity, Resilience / Systemic Risk, Dependency / Resource Flow, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XVI-C | Verification Accessibility | `core_06015_rights_part_c.md:1175` | 5.2, 7, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | cjs_05110_oversight_operations.md#cjs-34-audit-process-output-disclosure | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XVII | System Lifecycle, Environments, and Reversibility | `core_06015_rights_part_c.md:1213` | linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability, Timely Resolution | complete |
| XVII-A | Lifecycle Governance and Environment Separation | `core_06015_rights_part_c.md:1269` | 20, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Ecological Footprint / Environmental Preconditions, Privacy / Data Stewardship | complete |
| XVII-B | Progressive Deployment and Reversibility | `core_06015_rights_part_c.md:1313` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8 | Tetrad, Aims | None | None | Safety / Harm / Risk, Resilience / Systemic Risk, Privacy / Data Stewardship | complete |
| XVII-C | Misclassification and Evasion Consequences | `core_06015_rights_part_c.md:1356` | 20, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Productive Capacity, Truth / Epistemic Integrity | complete |
| XVIII | Innovation, Experimentation, and Creative Freedom | `core_06015_rights_part_c.md:1395` | linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Educational Agency, Truth / Epistemic Integrity, Privacy / Data Stewardship, Incentive Alignment / Proxy Integrity, Timely Resolution | complete |
| XVIII-A | Sandboxed Scope | `core_06015_rights_part_c.md:1437` | 7, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Resilience / Systemic Risk, Truth / Epistemic Integrity, Privacy / Data Stewardship | complete |
| XVIII-B | Containment, Disclosure, and Opt-In | `core_06015_rights_part_c.md:1474` | 7, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Resilience / Systemic Risk, Dependency / Resource Flow, Proportionate Cross-System Support, Truth / Epistemic Integrity | complete |
| XVIII-C | Transition to Higher-Obligation Regimes | `core_06015_rights_part_c.md:1507` | 20, linked | 3.1, 6.1, 6.3, 7, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Privacy / Data Stewardship, Timely Resolution | complete |
| XVIII-D | Innovation Reward, Disclosure, and Anti-Enclosure | `core_06015_rights_part_c.md:1539` | 7, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity, Timely Resolution | complete |
| XVIII-E | Creative and Expressive Works | `core_06015_rights_part_c.md:1591` | 7, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Educational Agency, Truth / Epistemic Integrity, Privacy / Data Stewardship, Timely Resolution | complete |
| XVIII-F | Inventions, Processes, and Functional Systems | `core_06015_rights_part_c.md:1630` | 7, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Educational Agency, Truth / Epistemic Integrity, Privacy / Data Stewardship, Incentive Alignment / Proxy Integrity, Timely Resolution | complete |
| XIX | Standing and Participation Status | `core_06020_rights_part_d.md:83` | linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Substantive Fairness, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XIX-A | Standing Distinction | `core_06020_rights_part_d.md:168` | 7, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.2, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | None | None | Survival-floor access, Productive Capacity, Trustworthiness | complete |
| XIX-B | Contestability and Proportional Restriction Limits | `core_06020_rights_part_d.md:210` | 7, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Substantive Fairness, Accessibility, Truth / Epistemic Integrity, Trustworthiness, Market Structure / Contestability, Timely Resolution | complete |
| XIX-C | Contribution, Competency Bars, and Named-Pathway Eligibility | `core_06020_rights_part_d.md:274` | linked | 2, 3.1, 3.2, 4, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Substantive Fairness, Accessibility, Trustworthiness, Market Structure / Contestability | complete |
| XIX-D | Violations and Standing Locks | `core_06020_rights_part_d.md:331` | 7, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Productive Capacity, Market Structure / Contestability | complete |
| XIX-E | Voting and Special Locks | `core_06020_rights_part_d.md:377` | 7, linked | 3.1, 4, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Substantive Fairness, Incentive Alignment / Proxy Integrity | complete |
| XX | Justice After Verified Violation | `core_06020_rights_part_d.md:426` | linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Market Structure / Contestability, Timely Resolution | missing_ch0_measurement_frame |
| XX-A | Justice Objective and Scope | `core_06020_rights_part_d.md:463` | 3.3, linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Productive Capacity | complete |
| XX-B | Restriction Floors | `core_06020_rights_part_d.md:500` | linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Resilience / Systemic Risk, Substantive Fairness, Educational Agency, Market Structure / Contestability, Timely Resolution | complete |
| XXI | Interoperability, Portability, and Exit Integrity | `core_06020_rights_part_d.md:586` | linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability, Timely Resolution | complete |
| XXI-A | Portability Rights | `core_06020_rights_part_d.md:648` | 7, linked | 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Market Structure / Contestability, Timely Resolution | complete |
| XXI-B | Reciprocal Interoperability Boundaries | `core_06020_rights_part_d.md:683` | 7, linked | 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad, Aims | None | None | Avoidable Burden, Dependency / Resource Flow | complete |
| XXI-C | Anti-Lock-In Rule | `core_06020_rights_part_d.md:714` | 7, 18, linked | 5, 5.1, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Productive Capacity, Dependency / Resource Flow, Market Structure / Contestability | complete |
| XXI-D | Open Formats and Standards | `core_06020_rights_part_d.md:750` | 7, 16.3, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XXII | Movement, Migration, Refuge, and Non-Statelessness | `core_06020_rights_part_d.md:810` | 7, linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Substantive Fairness, Market Structure / Contestability, Timely Resolution | complete |
| XXII-A | Movement and Relocation | `core_06020_rights_part_d.md:871` | 7, linked | 2, 3.1, 5, 5.1, 6.1, 6.3, 7 | Tetrad, Aims | None | None | Safety / Harm / Risk, Survival-floor access | complete |
| XXII-B | Refuge from Non-Compliance | `core_06020_rights_part_d.md:905` | 7, linked | 2, 3.1, 5, 5.1, 6.1, 6.1.5, 6.3, 7, 8 | Tetrad | None | None | Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Ecological Footprint / Environmental Preconditions | complete |
| XXII-C | Non-Statelessness | `core_06020_rights_part_d.md:949` | 4, 7, linked | 3.1, 5, 5.1, 6.1, 6.3, 7, 10, 10.1 | Tetrad, Aims | None | None | Safety / Harm / Risk, Market Structure / Contestability | complete |
| XXII-D | Limitation, Custody, and Emergency Discipline | `core_06020_rights_part_d.md:996` | 7.1, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Substantive Fairness, Market Structure / Contestability, Timely Resolution | complete |
| XXIII | Comprehensibility and Complexity Stewardship | `core_06020_rights_part_d.md:1046` | 5.2, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Constitutional Efficiency, Avoidable Burden, Productive Capacity, Ecological Footprint / Environmental Preconditions, Dependency / Resource Flow, Accessibility, Truth / Epistemic Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XXIII-A | Proportional Comprehensibility Right | `core_06020_rights_part_d.md:1125` | 5.2, 7, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, material stake | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Accessibility, Truth / Epistemic Integrity | complete |
| XXIII-B | Complexity Audit and Modularity Requirements | `core_06020_rights_part_d.md:1160` | 18.5, 20, linked | 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Dependency / Resource Flow, Market Structure / Contestability | complete |
| XXIV | Root Cause Analysis and Adaptive Response | `core_06020_rights_part_d.md:1203` | linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Ecological Footprint / Environmental Preconditions, Resilience / Systemic Risk, Dependency / Resource Flow, Truth / Epistemic Integrity, Privacy / Data Stewardship, Trustworthiness, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XXIV-A | Diagnostic Rigor and Causal Attribution | `core_06020_rights_part_d.md:1270` | linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad | None | None | Safety / Harm / Risk, Truth / Epistemic Integrity, Trustworthiness, Market Structure / Contestability | complete |
| XXIV-B | Auditability, Challenge, and Reversibility Preference | `core_06020_rights_part_d.md:1306` | linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims | None | None | Safety / Harm / Risk, Resilience / Systemic Risk, Incentive Alignment / Proxy Integrity, Timely Resolution | complete |
| XXV | Constitutional Interpretation, Review, and Anti-Capture Safeguards | `core_06020_rights_part_d.md:1343` | linked | 3.2, 4, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Avoidable Burden, Productive Capacity, Dependency / Resource Flow, Truth / Epistemic Integrity, Trustworthiness, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XXV-A | Bounded Interpretive Mandate and Public Reasons | `core_06020_rights_part_d.md:1401` | 18, linked | 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad | None | None | Avoidable Burden, Productive Capacity, Accessibility, Incentive Alignment / Proxy Integrity, Market Structure / Contestability | complete |
| XXV-B | Challenge Rights and Independent Review | `core_06020_rights_part_d.md:1451` | linked | 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Productive Capacity, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| XXV-C | Constitutional Forum Independence and External Review | `core_06020_rights_part_d.md:1480` | linked | 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Productive Capacity, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity | complete |
| XXV-D | Removal for Cause and Non-Entrenchment | `core_06020_rights_part_d.md:1518` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| XXVI | Timely Retrospective Review and Restorative Alignment | `core_06025_rights_part_e.md:62` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Privacy / Data Stewardship, Market Structure / Contestability, Timely Resolution | complete |
| XXVI-A | Retrospective Review and Disclosure | `core_06025_rights_part_e.md:120` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Truth / Epistemic Integrity | complete |
| XXVI-B | Rights-Collision Procedure and Restorative Alignment | `core_06025_rights_part_e.md:157` | linked | 3.1, 3.2, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 11, 12, 13 | Tetrad | None | None | Safety / Harm / Risk, Avoidable Burden, Productive Capacity, Market Structure / Contestability, Timely Resolution | complete |
| XXVI-C | Timely Resolution and Anti-Delay Floor | `core_06025_rights_part_e.md:195` | 13.3, linked | 3.1, 6.1, 6.1.5, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims, material stake | None | None | Safety / Harm / Risk, Constitutional Efficiency, Avoidable Burden, Accessibility, Truth / Epistemic Integrity, Incentive Alignment / Proxy Integrity, Market Structure / Contestability, Timely Resolution | complete |
| XXVII | Constitutional Evolution and Non-Entrenchment | `core_06025_rights_part_e.md:239` | 18.4, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Avoidable Burden, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| XXVII-A | Non-Entrenchment and Revisability | `core_06025_rights_part_e.md:259` | 14, 18.4, linked | 2, 3.1, 3.2, 6.2, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Wellbeing, Productive Capacity, Incentive Alignment / Proxy Integrity | complete |
| XXVII-B | Periodic Revalidation and Transparent Change | `core_06025_rights_part_e.md:295` | 14, linked | 3.1, 3.2, 6.1, 6.2, 6.3, 7, 8 | Tetrad | None | None | Substantive Fairness, Educational Agency, Truth / Epistemic Integrity, Market Structure / Contestability | complete |
| XXVIII | Transition Governance, Continuity, and Re-Baselining | `core_06025_rights_part_e.md:332` | linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Trustworthiness, Timely Resolution | complete |
| XXVIII-A | Phased Adoption and Rights-Floor Continuity | `core_06025_rights_part_e.md:366` | 13.1, linked | 2, 3.1, 3.2, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Productive Capacity, Substantive Fairness, Accessibility, Truth / Epistemic Integrity, Timely Resolution | complete |
| XXVIII-B | Transitional Authority Limits and Reauthorization | `core_06025_rights_part_e.md:450` | linked | 3.1, 6.1, 6.1.5, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Avoidable Burden, Truth / Epistemic Integrity, Timely Resolution | complete |
| XXVIII-C | Failure Off-Ramps, Re-Baselining, and Traceability | `core_06025_rights_part_e.md:492` | linked | 3.1, 3.2, 4, 6.1, 6.2, 6.3, 7, 8, 9, 9.2, 10, 10.1, 11, 12, 13 | Tetrad, Aims | None | None | Safety / Harm / Risk, Productive Capacity, Resilience / Systemic Risk, Truth / Epistemic Integrity, Trustworthiness, Timely Resolution | complete |
| XXVIII-D | Non-Compliant Property and Systems; Voluntary Turnover Incentives | `core_06025_rights_part_e.md:529` | 13.3, linked | 2, 3.1, 3.2, 4, 5, 5.1, 6.1, 6.1.5, 6.2, 6.3, 7, 8, 10, 10.1, 11, 12, 13 | Tetrad, Aims, material stake | None | None | Wellbeing, Safety / Harm / Risk, Survival-floor access, Avoidable Burden, Substantive Fairness, Trustworthiness, Timely Resolution | complete |

## Chapter 1 Rights Surface

| Principle | Title | File | Chapter 6 references |
|---|---|---|---:|
| Preamble §1 | The Model | `core_00000_preamble.md:68` | 0 |
| Preamble §2 | Measurements Overview | `core_00000_preamble.md:114` | 0 |
| Preamble §3 | Governance and Stewardship | `core_00000_preamble.md:142` | 0 |
| Preamble §3.1 | Using Measurements in Governance | `core_00000_preamble.md:151` | 0 |
| Preamble §3.2 | Key Governance Processes | `core_00000_preamble.md:160` | 0 |
| Preamble §3.3 | Governance Layers | `core_00000_preamble.md:176` | 0 |
| Preamble §4 | Principles, Definitions, and Rights | `core_00000_preamble.md:192` | 0 |
| Preamble §5 | System and Institutional Charters, Functional Independence, and Segregation of Duties | `core_00000_preamble.md:257` | 0 |
| Preamble §5.1 | Four-seat separation map | `core_00000_preamble.md:289` | 0 |
| Preamble §6 | Key Practical Process Pipelines | `core_00000_preamble.md:324` | 0 |
| Preamble §6.1 | Process map | `core_00000_preamble.md:344` | 0 |
| Preamble §6.2 | How the full chain fits together | `core_00000_preamble.md:399` | 0 |
| Preamble §7 | Process Ownership and Outputs | `core_00000_preamble.md:417` | 0 |
| Preamble §8 | Governance, Change, and Incorporation | `core_00000_preamble.md:474` | 0 |
| Preamble §9 | Adopted Implementation Corpus | `core_00000_preamble.md:507` | 0 |
| 1 | Purpose and Role | `core_01005_values_principles.md:63` | 0 |
| 2 | Flourishing Aim: Introduction | `core_01005_values_principles.md:171` | 0 |
| 2.1 | Non-Negotiable Principle Constraints: Safety and Truth | `core_01005_values_principles.md:253` | 0 |
| 3 | Foundational Objective: Wellbeing (Flourishing Aim) | `core_01005_values_principles.md:288` | 0 |
| 3.1 | Fairness | `core_01005_values_principles.md:344` | 0 |
| 3.2 | Recognition, Reinforcement, and Aspiration | `core_01005_values_principles.md:443` | 0 |
| 3.3 | Anti-Degrading Process | `core_01005_values_principles.md:547` | 0 |
| 4 | Safety (Harm Constraint) | `core_01005_values_principles.md:615` | 0 |
| 5 | Truth (Epistemic Integrity Constraint) | `core_01005_values_principles.md:664` | 0 |
| 5.1 | Science-Informed Inquiry and Decision Support | `core_01005_values_principles.md:709` | 0 |
| 5.2 | Plain-Language Accessibility (Participation and Stewardship Duty) | `core_01005_values_principles.md:774` | 0 |
| 6 | Trust and Trustworthiness (Coordination Integrity) | `core_01005_values_principles.md:871` | 0 |
| 6.1 | Correction and Remedy | `core_01005_values_principles.md:927` | 0 |
| 7 | Freedom (Bounded Agency) | `core_01005_values_principles.md:966` | 0 |
| 7.1 | Limitation Discipline | `core_01005_values_principles.md:1052` | 0 |
| 7.2 | Assembly, Collective Organization, and Institutional Formation | `core_01005_values_principles.md:1101` | 0 |
| 7.3 | Dissent and Peaceful Protest | `core_01005_values_principles.md:1171` | 0 |
| 7.4 | Voluntary Discontinuation, Major Self-Modification, and Exit Rights | `core_01005_values_principles.md:1208` | 0 |
| 7.5 | Expression and the Harm Line | `core_01005_values_principles.md:1252` | 0 |
| 8 | Continuity Aim: Introduction | `core_01005_values_principles.md:1290` | 0 |
| 9 | Shared-System Capacity | `core_01005_values_principles.md:1377` | 0 |
| 9.1 | Productive Capacity (Instrumental Good) | `core_01005_values_principles.md:1456` | 0 |
| 9.2 | Constitutional Efficiency | `core_01005_values_principles.md:1549` | 0 |
| 10 | Resilience and Self-Healing Design | `core_01005_values_principles.md:1592` | 0 |
| 11 | Market Structure | `core_01005_values_principles.md:1650` | 0 |
| 11.1 | Market Concentration Threshold Mechanism (Adopter-Tunable) | `core_01005_values_principles.md:1706` | 0 |
| 11.2 | Pro-Competition and Anti-Domination | `core_01005_values_principles.md:1792` | 0 |
| 11.3 | Consolidation Ceiling | `core_01005_values_principles.md:1942` | 0 |
| 11.4 | Resource and Dependency Concentration (Adopter-Tunable) | `core_01005_values_principles.md:2087` | 0 |
| 12 | Systemic Evaluation Requirement | `core_01005_values_principles.md:2141` | 0 |
| 13 | Constitutional Collision Resolution Process | `core_01010_interaction_interpretation.md:80` | 0 |
| 13.1 | Core Tradeoff Principles | `core_01010_interaction_interpretation.md:168` | 0 |
| 13.2 | Epistemic Disclosure Constraints | `core_01010_interaction_interpretation.md:493` | 0 |
| 13.3 | Minimization of Avoidable Burden | `core_01010_interaction_interpretation.md:732` | 0 |
| 14 | Prohibition on Absolute Override | `core_01010_interaction_interpretation.md:775` | 0 |
| 15 | Constitutional Interpretation | `core_01010_interaction_interpretation.md:822` | 0 |
| 15.1 | Constitutional No-Bypass Principle | `core_01010_interaction_interpretation.md:870` | 0 |
| 15.2 | Definitional layer and required disciplines | `core_01010_interaction_interpretation.md:993` | 0 |
| 15.3 | Ambiguity resolution | `core_01010_interaction_interpretation.md:1048` | 0 |
| 15.4 | Constitutional Meaning Conflict Resolution | `core_01010_interaction_interpretation.md:1073` | 0 |
| 16 | Stewardship In Depth | `core_01015_stewardship_capacity_principles.md:37` | 0 |
| 16.1 | Distributed Understanding | `core_01015_stewardship_capacity_principles.md:188` | 0 |
| 16.2 | Institutional Development | `core_01015_stewardship_capacity_principles.md:241` | 0 |
| 16.3 | Openness Aspiration | `core_01015_stewardship_capacity_principles.md:293` | 0 |
| 16.4 | Document at Action | `core_01015_stewardship_capacity_principles.md:337` | 0 |
| 17 | Consequential Stewardship: The Steward Role | `core_01015_stewardship_capacity_principles.md:393` | 0 |
| 17.1 | Shared Stewardship Standard | `core_01015_stewardship_capacity_principles.md:479` | 0 |
| 17.2 | Alignment Under Pressure | `core_01015_stewardship_capacity_principles.md:533` | 0 |
| 17.3 | Logging the Role, Not the Steward | `core_01015_stewardship_capacity_principles.md:580` | 0 |
| 17.4 | Aligned Self-Organization | `core_01015_stewardship_capacity_principles.md:628` | 0 |
| 17.5 | Duty to Resist | `core_01015_stewardship_capacity_principles.md:726` | 0 |
| 17.6 | Portable Competence | `core_01015_stewardship_capacity_principles.md:796` | 0 |
| 18 | Governance Under Stewardship Discipline | `core_01015_stewardship_capacity_principles.md:863` | 0 |
| 18.1 | Governance as Authorized Structure | `core_01015_stewardship_capacity_principles.md:913` | 0 |
| 18.2 | Institutional Secularism and Worldview Neutrality | `core_01015_stewardship_capacity_principles.md:979` | 0 |
| 18.3 | Segregation of Duties | `core_01015_stewardship_capacity_principles.md:1016` | 0 |
| 18.4 | Ongoing Justification | `core_01015_stewardship_capacity_principles.md:1063` | 0 |
| 18.5 | Modular Architecture and Dependency Discipline | `core_01015_stewardship_capacity_principles.md:1112` | 0 |
| 18.6 | Standardization | `core_01015_stewardship_capacity_principles.md:1186` | 0 |
| 19 | Incentive Alignment and System Capture | `core_01015_stewardship_capacity_principles.md:1258` | 0 |
| 19.1 | Alignment Requirement | `core_01015_stewardship_capacity_principles.md:1330` | 0 |
| 19.2 | Convenient Proxies and Proxy Divergence | `core_01015_stewardship_capacity_principles.md:1454` | 0 |
| 19.3 | Misalignment Detection | `core_01015_stewardship_capacity_principles.md:1486` | 0 |
| 19.4 | Misalignment Correction and Capture Response | `core_01015_stewardship_capacity_principles.md:1559` | 0 |
| 19.5 | Contingent Claims, Games of Chance, and Event-Contract Markets | `core_01015_stewardship_capacity_principles.md:1608` | 0 |
| 19.6 | Keeping Responsibility When Ownership or Structure Changes | `core_01015_stewardship_capacity_principles.md:1774` | 0 |
| 20 | Integrated Application | `core_01015_stewardship_capacity_principles.md:1833` | 0 |

## Chapter 0 Measurement Coverage

| Measurement family | Chapter 6 items referencing family |
|---|---:|
| Wellbeing | 50 |
| Safety / Harm / Risk | 103 |
| Survival-floor access | 40 |
| Constitutional Efficiency | 5 |
| Avoidable Burden | 87 |
| Productive Capacity | 93 |
| Ecological Footprint / Environmental Preconditions | 41 |
| Resilience / Systemic Risk | 28 |
| Dependency / Resource Flow | 43 |
| Proportionate Cross-System Support | 5 |
| Substantive Fairness | 36 |
| Accessibility | 27 |
| Educational Agency | 19 |
| Truth / Epistemic Integrity | 83 |
| Privacy / Data Stewardship | 27 |
| Trustworthiness | 30 |
| Incentive Alignment / Proxy Integrity | 31 |
| Market Structure / Contestability | 65 |
| Timely Resolution | 46 |

## Findings

### Missing Ch0 Measurement Frame

- **MEDIUM** `core_06020_rights_part_d.md:426` `XX` — Missing top-level Chapter 0 frame signal(s): material stake.

## Remediation Roadmap

1. Fix any broken cross-layer links before semantic editing.
2. Resolve owner-boundary and overreach findings before adding explanatory trace prose.
3. Add or clarify Chapter 0 measurement-family routing only where the right actually depends on measurement.
4. Doctrinal semantic adequacy is out of scope of this structural pass; do not treat its absence as a machine gap.
