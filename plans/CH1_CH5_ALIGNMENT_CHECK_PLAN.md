# Chapter 1 ↔ Chapter 5 Alignment Check Plan

**Purpose:** Ensure bidirectional alignment between Chapter 1 (Principles) and Chapter 5 (Foundational Definitions), verifying that definitions are properly referenced and principles are properly anchored.

**Scope:** 
- Chapter 1: [`core_00_preamble.md`, `core_01_values_principles.md`, and `core_01_stewardship_capacity_principles.md`](core_00-01_principles.md)
- Chapter 5: [`core_05-05_definitions_a_independent.md`](core_05-05_definitions_a_independent.md), [`core_05-05_definitions_b_semi_independent.md`](core_05-05_definitions_b_semi_independent.md), [`core_05-05_definitions_c_dependent_clusters.md`](core_05-05_definitions_c_dependent_clusters.md)

---

## Phase 1: Extract and Catalog References

### 1.1 Chapter 1 → Chapter 5 Forward References
**Task:** Extract all definition references from Chapter 1 principles

**Location to scan:**
- All `<details>` blocks with summary containing `Definitions · Evaluation · Compliance`
- Format: `- [Definition Name](path#anchor) · [O](path#anchor) · [E](path#anchor) · [C](path#anchor)`

**Data to capture:**
- Principle section number (e.g., "1", "2.1", "3.2")
- Principle title
- Referenced definition name
- Definition location (which Chapter 5 file)
- Presence of O/E/C links

**Expected pattern:**
```markdown
<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Proportionality](core_05-05_definitions_a_independent.md#proportionality) · [O](core_05-05_definitions_a_independent.md#proportionality) · [E](core_05-05_definitions_a_independent.md#proportionality-e) · [C](core_05-05_definitions_a_independent.md#proportionality-c)
```

### 1.2 Chapter 5 Definition Inventory
**Task:** Catalog all definitions across Chapter 5 parts A, B, and C

**For each definition, capture:**
- Definition name (header text after `#### `)
- Part (A=Independent, B=Semi-independent, C=Dependent clusters)
- Cluster affiliation (for Part C definitions)
- O/E/C component presence (check for `- O:`, `- E:`, `- C:` in trace blocks)
- Anchor/ID stability

---

## Phase 2: Completeness Verification

### 2.1 Verify All Chapter 1 Principles Have Definition Anchors
**Check:** Every principle section in Chapter 1 should have a `Definitions · Evaluation · Compliance` block

**Principles to verify:**
- [ ] 1. Purpose and Role
- [ ] 2. Foundational Objective: Wellbeing
- [ ] 2.1 Fairness
- [ ] 2.2 Recognition, Reinforcement, and Aspiration
- [ ] 3.1 Safety
- [ ] 3.2 Truth
- [ ] 4. Trust
- [ ] 5. Sustainability and Intergenerational Duty
- [ ] 5.1 Continuity
- [ ] 5.2 Stewardship and Distributed Understanding
- [ ] 6. Interaction and Conflict Resolution
- [ ] 6.1 Emergencies and Structural Limitations
- [ ] 6.2 Aggregation Limitations
- [ ] 6.3 Indispensable Rights
- [ ] 6.4 Rights Collision
- [ ] 7. Application
- [ ] 8. Freedom
- [ ] 9. Effective Access

**Gap criteria:** Missing compliance block = completeness gap

### 2.2 Verify All Referenced Definitions Exist
**Check:** Every definition referenced in Chapter 1 must exist in Chapter 5

**Validation steps:**
1. For each reference in Chapter 1, verify the target file exists
2. Verify the anchor/ID exists in the target file
3. Verify the definition header matches the linked text

**Gap criteria:** Broken link, missing file, or mismatched anchor = accuracy gap

---

## Phase 3: O/E/C Component Verification

### 3.1 Verify Complete O/E/C in Chapter 5 Definitions
**Check:** All definitions referenced by Chapter 1 must have complete O/E/C components

**Component definitions:**
- **O (Obligation/Operative):** What the definition requires
- **E (Evaluation):** How to evaluate/measure compliance
- **C (Compliance):** Compliance/satisfaction conditions

**Verification method:**
- For each referenced definition, locate the trace block
- Confirm presence of `- O:` section
- Confirm presence of `- E:` section  
- Confirm presence of `- C:` section

**Gap criteria:** Missing any O, E, or C component = accuracy gap

### 3.2 Verify O/E/C Links in Chapter 1 Are Valid
**Check:** All O/E/C links in Chapter 1 must point to valid anchors

**Validation:**
- O link should point to main definition anchor
- E link should point to `-e` variant anchor
- C link should point to `-c` variant anchor

**Gap criteria:** Broken O/E/C link = accuracy gap

---

## Phase 4: Bidirectional Traceability

### 4.1 Verify Chapter 5 → Chapter 1 Back-References
**Check:** Chapter 5 definitions should reference relevant Chapter 1 principles in their trace blocks

**Expected pattern in Chapter 5:**
```markdown
<details>
<summary>Trace</summary>

- Upstream: Principles: [Section X.Y](core_01_stewardship_capacity_principles.md#section-anchor)
```

**Validation:**
- Each definition should have an "Upstream: Principles" entry
- Link should be valid and point to correct principle section

### 4.2 Cross-Reference Matrix Construction
**Task:** Build bidirectional mapping table

| Principle | Definition | Direction | Status |
|-----------|------------|-----------|--------|
| 1. Purpose | Proportionality | 1→5 | ✓ |
| 1. Purpose | Necessity | 1→5 | ✓ |
| Wellbeing | 2. Foundational | 5→1 | ✓ |

---

## Phase 5: Dependent Cluster Integrity

### 5.1 Verify Cluster Component Completeness
**Check:** Part C (Dependent Clusters) definitions must maintain cluster integrity

**Rules:**
- All components of a cluster should be referenced together when applicable
- No partial segmentation of cluster references in Chapter 1
- Cluster definitions should reference each other appropriately

**Clusters to verify:**
- Authority Stack and Internal Hierarchy
- Stakeholder Status, Emergency, and Participation Weight
- Binding Collective Choice / Decision Resolution Process
- Collective Harm Boundary
- Contestability and Proportional Restriction Limits
- Constitutional Emergency and Contingency
- Autonomous Lethal System / Autonomous Coercion Tool
- Combatant / Non-Combatant Distinction
- Contested Sentient Life
- Audit Scope Sufficiency
- Force Majeure and System Failure

---

## Phase 6: Gap Analysis and Remediation

### 6.1 Gap Classification

| Gap Type | Severity | Description |
|----------|----------|-------------|
| Completeness | High | Principle missing definition anchors |
| Accuracy | High | Reference to non-existent definition |
| Accuracy | Medium | Incomplete O/E/C components |
| Coverage | Low | Orphan definition (no principle references) |
| Cluster | Medium | Segmented cluster references |

### 6.2 Remediation Priorities

1. **High Priority:** Fix completeness gaps (missing anchors)
2. **High Priority:** Fix broken references
3. **Medium Priority:** Complete O/E/C components
4. **Medium Priority:** Resolve cluster segmentation
5. **Low Priority:** Address orphan definitions (may be intentionally upstream)

---

## Phase 7: Deliverables

### 7.1 Alignment Report
**Format:** Markdown document
**Sections:**
- Executive summary (coverage stats)
- Completeness findings
- Accuracy findings (broken/incomplete references)
- Coverage findings (orphans)
- Cluster integrity findings
- Remediation roadmap with priorities

### 7.2 Traceability Matrix
**Format:** CSV
**Columns:**
- `principle_id`
- `principle_title`
- `definition_name`
- `ch5_location`
- `has_o_component`
- `has_e_component`
- `has_c_component`
- `reference_direction` (1→5, 5→1, bidirectional)
- `status` (valid, broken, incomplete)

### 7.3 Audit Log
**Format:** JSON
**Purpose:** Machine-readable gap data for automation
**Structure:**
```json
{
  "audit_date": "2026-05-11",
  "gaps": {
    "completeness": [...],
    "accuracy": [...],
    "coverage": [...],
    "cluster": [...]
  }
}
```

---

## Execution Tools

### Existing Tools Available:
- [`tools/ch1_ch5_alignment_audit.py`](tools/ch1_ch5_alignment_audit.py) - Automated alignment audit script

### Manual Verification Required:
- Semantic accuracy of references (tools can check existence, not relevance)
- Cluster co-reference appropriateness
- O/E/C content completeness (beyond component presence)

---

## Success Criteria

- [ ] 100% of Chapter 1 principles have definition anchors
- [ ] 100% of referenced definitions exist and are accessible
- [ ] 100% of referenced definitions have complete O/E/C components
- [ ] All bidirectional traceability links are valid
- [ ] No segmented cluster references
- [ ] All gaps documented with remediation steps

---

## Timeline Estimate

| Phase | Estimated Time |
|-------|----------------|
| 1. Extraction | 30 min (automated) |
| 2. Completeness | 45 min |
| 3. O/E/C Verification | 60 min |
| 4. Bidirectional Trace | 45 min |
| 5. Cluster Integrity | 30 min |
| 6. Gap Analysis | 30 min |
| 7. Report Generation | 15 min |
| **Total** | **~4 hours** |

---

*Plan Version: 1.0*
*Created: 2026-05-11*
*Applies to: Sentient Constitution Chapters 1 and 5*
