# Chapter 01 Principle Alignment Check for CJS-5

**Workflow name:** `CH1_CJS5_PRINCIPLE_ALIGNMENT_CHECK`

## Purpose

Verify that the CJS-5 implementation and cross-implementation operational cluster library preserves Chapter 01 principles and constraints without becoming a competing source of substantive constitutional doctrine.

## Scope

- Source principle layer: `core_00_preamble.md`, `core_01_values_principles.md`, and `core_01_stewardship_capacity_principles.md`
- CJS-5 target set:
  - `corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md`
  - `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md`
  - `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md`
  - `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md`
  - `corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md`
  - `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md`

## Audit Checks

1. Inventory all expected CJS-5 clusters: CJS-5.0, CJS-5.2 through CJS-5.7, CJS-5.8 through CJS-5.11, CJS-5.12 through CJS-5.15, CJS-5.16 through CJS-5.18, and CJS-5.19 through CJS-5.23.
2. Extract each cluster title, file location, `Read it with` references, direct Chapter 01 references, owner-layer routing references, and operational rules.
3. Infer the Chapter 01 principle basis from each cluster's subject matter, using Chapter 01 sections 1 through 10 as the principle inventory.
4. Validate `OP-O`, `OP-E`, and `OP-C` completeness for each cluster-level and material sub-rule.
5. Classify findings as `complete`, `missing_anchor`, `weak_trace`, `owner_drift`, `op_component_gap`, or `overreach`.

## Outputs

Run:

```bash
python tools/ch1_cjs5_alignment_audit.py --output-dir evidence/YYYY-MM-DD
```

Expected artifacts:

- `evidence/YYYY-MM-DD/ch1_cjs5_principle_alignment_report_YYYY-MM-DD.md`
- `evidence/YYYY-MM-DD/ch1_cjs5_traceability_matrix_YYYY-MM-DD.csv`
- `evidence/YYYY-MM-DD/ch1_cjs5_audit_log_YYYY-MM-DD.json`

## Validation

After generating evidence, run:

```bash
make reference-audit
make corpus-markdown-audit
```

If remediation edits are made to corpus text, run the broader regression bundle before closeout:

```bash
make regression
```

## Remediation Policy

Treat this as an audit-first workflow. Make corpus edits only when the report identifies a concrete trace, routing, or OP-triad defect. Preserve CJS-5 as an implementation-layer operational library: remediation should add or clarify routing metadata, not rewrite Chapter 01, Chapter Five, Chapter Ten, or CJS/CS/CI/CF owner rules.
