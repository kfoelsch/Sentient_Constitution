# Chapter 5 Cluster Definition Audit & Restructuring Plan

**Date:** 2026-05-08
**Scope:** Chapter 5, Sections 2 and 3
**Objective:** Trace which definitions actually need dependent cluster status vs. semi-independent definitions

---

## Executive Summary

Based on the shell cluster audit report, **30 of 42 clusters (71%)** in Section 3 are "shell clusters" - containing no local O/E/C definition content, only external pointers. This plan evaluates which clusters require true joint invocation (dependent) status vs. which can migrate to Section 2 as semi-independent definitions.

---

## Phase 1: Current State Catalog

### Section 3 Cluster Inventory (42 Total)

#### Meta/Meta-Rule Clusters (2) - KEEP
| ID | Title | Status |
|----|-------|--------|
| 3.1 | Joint invocation and satisfaction | Meta-rule (required) |
| 3.2 | Standalone definitions interaction | Meta-rule (required) |

#### Healthy Clusters with Local O/E/C (10) - KEEP
| ID | Title | Local Definitions |
|----|-------|-------------------|
| 3.4 | Animal Life, Sentient Life, and Sentience Status | Animal Life, Contested-Sentient Life, Sentience Status Adjudication, Sentient, Sentience Non-Exclusion, etc. |
| 3.6 | Binding Stakeholder Choice | Decision-Resolution Process, Weighted Participation Limits, Rights-Collision Record |
| 3.9 | Collective Harm Boundary, Harm, and Harassment | Harm, Collective Harm Boundary, Psychological Harm, Irreversible Harm |
| 3.14 | Creative Work, Training-Data Use... | Training-Data Use |
| 3.19 | Forum Families and Dispute Routing | All 6 forum families (Sentient, Technical, Institutional, Environment, Integrity, Constitutional) |
| 3.33 | Self-Determination, Meaningful Agency, Expression... | Self-Determination, Expression, Educational Agency |
| 3.38 | Transparency, Auditability, and Verification | Transparency, Audit Scope Sufficiency, Auditability, Evaluation Completeness, Observability, Verifiability, Verification Accessibility, Verification Feasibility, Verification Independence, Verification Proportionality, Verification Robustness |
| 3.39 | Trust and Trustworthiness | Trust, Trustworthiness, Trust Degradation and Misleading Reliance |
| 3.40 | Truth and Epistemic Integrity | Truth (Constitutional Constraint), Epistemic Integrity, Publication and High-Impact Communication, Foreseeability Diligence, Reasonably Foreseeable |

#### Shell Clusters (30) - CANDIDATES FOR MIGRATION

| ID | Title | External Targets | Assessment |
|----|-------|-----------------|------------|
| 3.3 | Accountability, Contestability, Adjudication... | definitions_b (4 members) | **MARGINAL** - These work together but are already in §2 |
| 3.5 | Assembly and Collective Organization | definitions_b (2 members) | **MIGRATE** - Clear §2 candidates |
| 3.7 | Bodily-Maintenance Access, Safe Conditions... | definitions_a, definitions_b (6 members) | **MIGRATE** - Survival-floor grouping, not interdependent |
| 3.8 | Capture, Resolution Integrity... | definitions_a, definitions_b (2 members) | **MARGINAL** - Only 2 members, minimal interdependence |
| 3.10 | Consent and Sexual Consent | definitions_b (2 members) | **MIGRATE** - Sexual consent is specialization |
| 3.11 | Corpus, Authority Stack... | definitions_a, definitions_b (4 members) | **KEEP** - Governance architecture requires joint invocation |
| 3.12 | Constitutional Contract/Foundational Choice | definitions_a (2 members) | **MARGINAL** - Layer distinction is important |
| 3.13 | Contingent Claim, Event-Contract, Game of Chance | definitions_a (3 members) | **MIGRATE** - Typology grouping |
| 3.15 | Derived/Developing Sentients, Instantiation... | definitions_b (6 members) | **MIGRATE** - Article VII-D family grouping |
| 3.16 | Ecological Integrity, Footprint, Sustainability | definitions_b (4 members) | **MIGRATE** - Article I-A/B related |
| 3.17 | Emergency and Contingency | definitions_b (4 members) | **MARGINAL** - Layer-sensitive, some interdependence |
| 3.18 | Family, Care, Reproductive Autonomy... | definitions_b (3 members) | **MIGRATE** - Article VII-D family |
| 3.20 | Governance Architecture, Oversight... | definitions_a, definitions_b (7 members) | **MARGINAL** - Large, governance-related |
| 3.21 | Indigenous Continuity, Language Culture... | definitions_a, definitions_b (4 members) | **MIGRATE** - Heritage continuity grouping |
| 3.22 | Info-Shere, Expression, Press... | definitions_a (3 members) | **MIGRATE** - Article VIII related |
| 3.23 | Material Impact, Materiality, Classification... | definitions_a, definitions_b (4 members) | **MARGINAL** - Evaluation framework cluster |
| 3.24 | Movement, Refuge, Non-Statelessness... | definitions_b (3 members) | **MIGRATE** - Article XVIII-D related |
| 3.25 | Nondiscrimination, Protected Characteristics... | definitions_a, definitions_b (5 members) | **MIGRATE** - Article V-B grouping |
| 3.26 | Privacy (Informational) | definitions_b, core_09* (6 members) | **MARGINAL** - Peer-level cluster head |
| 3.27 | Proportionality, Necessity, Feasibility... | definitions_a, definitions_b (8 members) | **MARGINAL** - Limitations discipline |
| 3.28 | Protected Internal-State Boundary | definitions_b (1 member) | **MIGRATE** - Single definition |
| 3.29 | Protected Reporting and Anti-Retaliation | definitions_b (2 members) | **MIGRATE** - Article XIII-A related |
| 3.30 | Proxy Integrity and Indicator-Reality | definitions_b (2 members) | **MIGRATE** - Metrics evaluation |
| 3.31 | Adjudication, Redress, Restorative... | definitions_a, definitions_b (4 members) | **MARGINAL** - Rights enforcement pathway |
| 3.32 | Resilience, Safety, Reversibility... | definitions_a (6 members) | **MIGRATE** - Protective concepts |
| 3.34 | Stakeholder Status, Emergency, Participation | definitions_b (2 members) | **MIGRATE** - SSP layer concepts |
| 3.35 | Standing State, Contribution, Violation | definitions_b (6 members) | **MARGINAL** - Chapter Six interface |
| 3.36 | Strategic Stewardship and Stewardship Defect | definitions_b (2 members) | **MIGRATE** - Chapter Ten related |
| 3.37 | Substantive and Procedural Fairness | definitions_b (2 members) | **MIGRATE** - Justice concepts |
| 3.41 | Use of Force, Autonomous Coercion... | definitions_b (6 members) | **KEEP** - Article XIII-B/C requires joint discipline |

---

## Phase 2: Classification Framework

### Criteria for Dependent (Section 3) Status

A cluster **REQUIRES** §3 joint invocation if:

1. **Segmentation Defeats Purpose**: Using definitions independently creates loopholes
2. **Cross-Cutting Rights Collision**: Spans multiple Rights-Floor articles requiring coordination
3. **Anti-Bypass Critical**: Cherry-picking members defeats functional protection
4. **Compound Definition**: Members form single functional requirement (e.g., "Binding Stakeholder Choice")

### Criteria for Semi-Independent (Section 2) Status

A cluster **CAN MIGRATE** to §2 if:

1. **Article-Specific Grouping**: Related to single Rights-Floor article
2. **Typological Convenience**: Similar concepts grouped for navigation
3. **Standalone Viable**: Individual use doesn't create loopholes
4. **Shell Status**: Currently has no local O/E/C content (external pointers only)

---

## Phase 3: Recommended Migration Mapping

### KEEP in Section 3 (12 clusters)

| Cluster | Rationale |
|---------|-----------|
| 3.1, 3.2 | Meta-rules governing cluster behavior (required) |
| 3.4 | Sentience status adjudication requires joint invocation across taxonomy/welfare/rights |
| 3.6 | Compound: decision-resolution + representation + rights-collision must be joint |
| 3.9 | Harm/boundary separation defeats protection |
| 3.11 | Corpus/authority/supremacy interdependence critical for validity |
| 3.38 | Transparency→Auditability→Verification chain requires joint discipline |
| 3.39 | Trust/Trustworthiness joint test prevents reliance without evidence |
| 3.40 | Truth/Epistemic Integrity/Foreseeability interdependence |
| 3.41 | Use of Force discipline requires joint evaluation under Article XIII-B/C |
| *(plus healthy clusters 3.19, 3.33, 3.42)* | Already have local O/E/C content |

### MIGRATE to Section 2 (21 clusters)

| Current §3 | Proposed §2 Home | Article/Domain |
|------------|------------------|----------------|
| 3.5 | "Assembly and Collective Organization" topic group | Article V-H, III-D |
| 3.7 | "Safe Conditions and Continuity" topic group | Article III-A/C/D |
| 3.8 | "Capture and Anti-Capture" topic group | Governance layer |
| 3.10 | "Consent and Coercion" topic group | Article VII-A, X-C |
| 3.12 | "Constitutional Authorization" topic group | Chapter Ten |
| 3.13 | "Contingent Structures" topic group | §7.2.5 principles |
| 3.15 | "Derivation and Care" topic group | Article VII-D |
| 3.16 | "Ecological Governance" topic group | Article I-A/B |
| 3.17 | "Emergency Pathways" topic group | Article XXIII-D |
| 3.18 | "Family and Reproductive Autonomy" topic group | Article VII-D |
| 3.20 | "Governance Structure" topic group | Chapter Ten |
| 3.21 | "Heritage and Continuity" topic group | Article V-B, XVIII-D |
| 3.22 | "Info-Sphere and Expression" topic group | Article II-E, V-H, VIII |
| 3.23 | "Materiality and Classification" topic group | Chapter Six |
| 3.24 | "Movement and Refuge" topic group | Article XVIII-D |
| 3.25 | "Nondiscrimination" topic group | Article V-B |
| 3.26 | "Privacy" topic group | Article VII-A/B, VIII, IX-A |
| 3.27 | "Limitations Discipline" topic group | §6.1 principles |
| 3.28 | "Privacy (continued)" | Article VII-B |
| 3.29 | "Protected Reporting" topic group | Article XIII-A |
| 3.30 | "Proxy Integrity" topic group | Evaluation |

### MARGINAL Cases (9 clusters)

| Cluster | Assessment |
|---------|------------|
| 3.3 | Could migrate - Accountability/Contestability/Adjudication already in §2 |
| 3.12 | Could keep - Constitutional Contract/Foundational Choice layer distinction matters |
| 3.17 | Could keep - Emergency layer-sensitivity requires joint discipline |
| 3.20 | Could keep - Large governance cluster, significant interdependence |
| 3.23 | Could keep - Materiality framework cluster |
| 3.26 | KEEP - Peer-level cluster head by design |
| 3.31 | Could migrate - Rights enforcement pathway grouping |
| 3.32 | Could migrate - Resilience/safety concepts |
| 3.35 | KEEP - Chapter Six interface requires precision |
| 3.37 | Could migrate - Fairness concepts |

---

## Phase 4: Validation Checklist

For each migrated cluster:

- [ ] All member definitions have O/E/C content in source file
- [ ] Cross-references from cluster point to correct anchors
- [ ] "Cluster component:" trace metadata preserved
- [ ] Read-with definitions updated
- [ ] No orphaned anchors in definitions_c
- [ ] ch5_cluster_content_audit.py passes

---

## Phase 5: Implementation Steps

1. **Create topic groups in Section 2** for migrated clusters
2. **Add cluster metadata** to migrated entries ("Former cluster:" trace)
3. **Update definitions_c** to remove shell clusters
4. **Run audit suite** to verify no regression
5. **Update doc_architecture.md** with new structure

---

## Summary

| Outcome | Count |
|---------|-------|
| Keep in Section 3 | 12 clusters |
| Migrate to Section 2 | 21 clusters |
| Marginal/Review | 9 clusters |

**Expected Impact:**
- Reduces Section 3 to true joint-invocation clusters only
- Improves navigability by placing definitions in Section 2
- Eliminates 21 "shell clusters" with no local content
- Maintains all O/E/C definition integrity
