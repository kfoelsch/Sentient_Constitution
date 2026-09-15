# Chapter 5 Section 2 vs Section 3 Reference Audit Report

**Date:** 2026-05-09  
**Auditor:** ch5_section2_section3_duplicate_audit.py, fix_ch5_section2_cluster_references.py  
**Files Analyzed:**
- `core_05-05_definitions_b_semi_independent.md` (Section 2)
- `core_05-05_definitions_c_dependent_clusters.md` (Section 3)

---

## Executive Summary

**Critical Finding:** Section 2 contains **12 "Cluster context" blocks** that reference **non-existent Section 3 clusters**. These are stale references to old cluster numbers that were restructured.

### Current State

| Metric | Count |
|--------|-------|
| Section 2 topic groups referencing Section 3 | 12 |
| References to non-existent clusters | 12 (100%) |
| Valid Section 3 references | 0 |

---

## Problem Details

### What Exists in Section 3 (Current)

Section 3 currently has **14 clusters** numbered 3.1 through 3.14:

| Cluster # | Title |
|-----------|-------|
| 3.1 | Animal Life, Sentient Life, and Sentience Status |
| 3.2 | Binding Stakeholder Choice |
| 3.3 | Collective Harm Boundary, Harm, and Harassment and Bullying |
| 3.4 | Corpus, Authority Stack, Supremacy, and Enforceability |
| 3.5 | Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement |
| 3.6 | Forum Families and Dispute Routing |
| 3.7 | Privacy (Informational) — peer-level cluster head |
| 3.8 | Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity |
| 3.9 | Standing State, Contribution, and Violation |
| 3.10 | Transparency, Auditability, and Verification |
| 3.11 | Trust and Trustworthiness |
| 3.12 | Truth and Epistemic Integrity |
| 3.13 | Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm |

### What Section 2 References (Incorrect)

Section 2 references these **non-existent clusters**:

| Old Ref | Topic Group in Section 2 | Status |
|---------|--------------------------|--------|
| §3.3 | Accountability, contestability, adjudication... | **WRONG** - Actual §3.3 is "Collective Harm Boundary" |
| §3.5 | Assembly and collective organization | **WRONG** - Actual §3.5 is "Creative Work..." |
| §3.7 | Safe conditions, bodily maintenance... | **WRONG** - Actual §3.7 is "Privacy" |
| §3.10 | Consent, sexual consent... | **WRONG** - Actual §3.10 is "Transparency" |
| §3.15 | Derivation, care, family... | **DOES NOT EXIST** |
| §3.16 | Ecological footprint... | **DOES NOT EXIST** |
| §3.17 | Emergency and contingency... | **DOES NOT EXIST** |
| §3.20 | Governance architecture... | **DOES NOT EXIST** |
| §3.23 | Materiality, material impact... | **DOES NOT EXIST** |
| §3.24 | Movement, refuge... | **DOES NOT EXIST** |
| §3.29 | Protected reporting... | **DOES NOT EXIST** |
| §3.37 | Protected characteristics... | **DOES NOT EXIST** |

Plus 8 additional references to: 3.18, 3.21, 3.25, 3.27, 3.30, 3.31, 3.32, 3.36

---

## Root Cause Analysis

### What Happened

1. **Restructuring Occurred**: Section 3 was restructured from 42 clusters to 14 clusters
2. **Cluster Numbers Changed**: Old clusters 3.3, 3.5, 3.7, etc. were eliminated or renumbered
3. **Section 2 Not Updated**: The "Cluster context" blocks in Section 2 still reference the OLD cluster numbers

### Evidence from Archive

The file `evidence/2026-05-08/ch5s3_shell_cluster_audit_report.md` documents that 30 of 42 original clusters were "shell clusters" with no local O/E/C content. The restructuring consolidated these into the current 14 clusters.

---

## Impact Assessment

### Navigation Confusion
Users following Section 2 "Cluster context" links will:
- Land on wrong clusters (if numbers coincidentally exist)
- Find broken anchors (if clusters were removed)
- Be confused about where joint-invocation rules apply

### Semantic Drift
The "Cluster context" claims in Section 2 are now **false statements**:
- "corresponds to Chapter Five §3.14" is wrong for most topic groups
- Joint invocation discipline may be misapplied

---

## Recommended Fixes

### Option 1: Update References to Current Clusters (Minimal Fix)

Update Section 2 "Cluster context" blocks to reference the correct CURRENT Section 3 clusters where applicable, or remove the references if the concepts no longer exist as clusters.

**Example fixes:**
- "§3.3 Accountability..." → Remove reference (no such cluster)
- "§3.15 Derived..." → Remove reference (cluster migrated to Section 2)
- "§3.17 Emergency..." → Map to actual cluster if concept exists elsewhere

### Option 2: Comprehensive Restructuring (Per evidence/2026-05-08/plan)

The archived `chapter_5_cluster_restructuring_plan.md` recommends:
- Migrating 21 clusters from Section 3 to Section 2 as "topic groups"
- Keeping only 12 true joint-invocation clusters in Section 3
- This would align Section 2 references with the actual structure

---

## Detection Tools Created

1. **`tools/ch5_section2_section3_duplicate_audit.py`** - Detects duplicate definitions and mismatched references
2. **`tools/fix_ch5_section2_cluster_references.py`** - Proposes and applies fixes to Section 2 references

---

## Action Items

- [ ] Decide on Option 1 (minimal) vs Option 2 (comprehensive restructuring)
- [ ] Apply fixes to Section 2 cluster context blocks
- [ ] Run audit to verify no stale references remain
- [ ] Update documentation to reflect current structure

---

## Summary

**The issue is confirmed:** Section 2 contains 12 topic groups that reference non-existent Section 3 clusters. These are stale references from a previous restructuring. The references need to be updated or removed to match the current Section 3 structure of 14 clusters (3.1-3.14).

**No duplicate O/E/C definitions exist** - the definitions are correctly housed in Section 2 as semi-independent definitions. The only issue is the incorrect "Cluster context" cross-references.
