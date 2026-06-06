# Chapter 01 -> CJS-5 Principle Alignment Audit Report

**Date:** 2026-06-06
**Workflow:** CH1_CJS5_PRINCIPLE_ALIGNMENT_CHECK
**Auditor:** Automated static extraction with manual-review flags

## Executive Summary

| Metric | Result | Status |
|---|---:|---|
| CJS-5 clusters discovered | 23/23 | PASS |
| Clusters with complete OP-O/OP-E/OP-C triads | 23/23 | PASS |
| Clusters with direct Chapter 01 citations | 3/23 | REVIEW |
| Clusters with inferred Chapter 01 basis | 23/23 | PASS |
| Owner-routing issues | 0 | PASS |
| Potential overreach flags | 0 | PASS |

## Overall Assessment

CJS-5 is operationally aligned with Chapter 01 at the structural level: all expected clusters were found, all operational rules carry complete `OP-O` / `OP-E` / `OP-C` triads, and each cluster has an inferred Chapter 01 principle basis. The main audit finding is trace explicitness: most CJS-5 clusters rely on PRIM/PROT, owner-file, and subject-matter routing rather than direct Chapter 01 citations.

## Cluster Traceability Summary

| Cluster | Title | File | Inferred Chapter 01 Principles | Direct Chapter 01 Refs | Owner Refs | Status |
|---|---|---|---|---|---|---|
| CJS-5.0 | Role-definition preface and standing competency gate interface | `corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md` | 2.1, 3.4, 5.2, 7.1, 7.2, 10 | None | Article XI-D, CI, Chapter Eleven, Chapter Seven, core_07-07_standing_integration.md, core_11-11_governance.md (+3) | weak_trace |
| CJS-5A.1 | Implementation and cross-implementation distributed and proportional authority terms | `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md` | 2.1, 4, 5.2, 7.2, 10 | None | CI, PRIM15, PRIM4, PRIM9, PROT1, PROT6 (+1) | weak_trace |
| CJS-5A.2 | Implementation and cross-implementation intervention governance and override-authorization terms | `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md` | 3.1, 6.1, 6.4, 7.1, 9 | None | CF, PRIM15, PRIM8, PRIM9, PROT1, PROT2 (+2) | weak_trace |
| CJS-5A.3 | Implementation and cross-implementation reflexive transparency and accountability terms | `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md` | 3.2, 4, 5.2, 7.1, 7.2 | None | PRIM10, PRIM11, PRIM15, PRIM4, PRIM9, PROT1 (+4) | weak_trace |
| CJS-5A.4 | Implementation and cross-implementation burden-of-justification and constraint terms | `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md` | 6.1, 6.3, 6.4, 7.1, 8, 9 | 6.4.1 | CF, Core definitions, PRIM15, PRIM4, PRIM7, PRIM9 (+3) | complete |
| CJS-5A.5 | Implementation and cross-implementation constrained-secrecy and protected-investigation terms | `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md` | 3.2, 6.2, 6.4, 7.1, 8, 9 | None | PRIM15, PRIM4, PRIM9, PROT1, PROT3, PROT4 (+2) | weak_trace |
| CJS-5A.6 | Implementation and cross-implementation procedural integrity and adjudication terms | `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md` | 2.1, 3.4, 6.4, 7.1, 8, 10 | None | PROT2, PROT3, PROT4, PROT6, corpus_forum.md, corpus_institutions.md (+1) | weak_trace |
| CJS-5B.1 | Implementation and cross-implementation integrity assurance and resilience operations | `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md` | 3.1, 3.2, 4.1, 7.1, 7.2 | None | Core definitions | weak_trace |
| CJS-5B.2 | Implementation and cross-implementation auditability and reconstructability terms | `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md` | 3.2, 4, 7.1, 7.2 | None | Article VII-B, Article XV-A, PRIM10, PRIM4, PRIM9 | weak_trace |
| CJS-5B.3 | Implementation and cross-implementation tiered transparency and audit-access terms | `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md` | 3.2, 6.2, 6.4, 7.1, 8 | 6.4.1 | Article VII-B, Article XV-A, CF, PRIM10, PRIM12, PRIM9 (+2) | complete |
| CJS-5B.4 | Implementation and cross-implementation independent verification and claim-integrity terms | `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md` | 3.2, 3.3, 4, 7.1, 7.2 | None | PRIM10, PRIM11, PRIM9 | weak_trace |
| CJS-5C.1 | Implementation and cross-implementation quorum and participatory legitimacy terms | `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md` | 2.1, 4, 5.2, 6.4, 8, 10 | None | Article IX-C, Article XI, Article XI-A, Chapter Eleven, Chapter Ten, PROT1 (+1) | weak_trace |
| CJS-5C.2 | Implementation and cross-implementation comprehensibility and cognitive accessibility terms | `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md` | 3.4, 5.2, 7.1, 8 | None | PRIM2, corpus_systems.md | weak_trace |
| CJS-5C.3 | Implementation and cross-implementation salience integrity and attention-allocation terms | `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md` | 2, 3.2, 4, 7.1, 8 | None | Article XV-A, Chapter Ten, PRIM1, PRIM14, PRIM4 | weak_trace |
| CJS-5C.4 | Implementation and cross-implementation disclosure sufficiency and observability terms | `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md` | 3.2, 6.2, 7.1, 8 | None | Article VII-B, Article XV-A, PRIM4, PRIM5 | weak_trace |
| CJS-5D.1 | Implementation and cross-implementation dependency integrity and disclosure terms | `corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md` | 3.1, 4.1, 5.1, 7.1, 9 | None | Article XV-A, PRIM15, PRIM4, PRIM5, PRIM7, PRIM9 (+1) | weak_trace |
| CJS-5D.2 | Implementation and cross-implementation interoperability, portability, and exit-integrity terms | `corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md` | 5.1, 6.1, 7.1, 8, 9 | None | Article XIX, Article XV-A, Foundational Rights, PRIM4, PRIM5, PRIM7 (+1) | weak_trace |
| CJS-5D.3 | Implementation and cross-implementation data-retention and lifecycle-integrity terms | `corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md` | 3.2, 6.2, 7.1, 8, 9 | None | PRIM10, PRIM11, PRIM12, PRIM15, PRIM9, corpus_systems.md | weak_trace |
| CJS-5E.1 | Implementation and cross-implementation graceful degradation and failure-mode integrity terms | `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md` | 3.1, 4.1, 5.1, 6.1, 7, 9 | None | PRIM1, PRIM12, PRIM15, PRIM5, PRIM6, corpus_systems.md | weak_trace |
| CJS-5E.2 | Implementation and cross-implementation intervention and override integrity terms | `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md` | 3.1, 6.1, 6.4, 7.1, 9 | 6.4.1 | CF, PRIM14, PRIM15, PRIM6, PRIM8, PRIM9 (+2) | complete |
| CJS-5E.3 | Implementation and cross-implementation reversibility and containment terms | `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md` | 3.1, 4.1, 6.1, 7.1, 9 | None | PRIM10, PRIM11, PRIM12, PRIM5, PRIM6, PRIM9 | weak_trace |
| CJS-5E.4 | Implementation and cross-implementation adversarial robustness and abuse-resistance terms | `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md` | 3.1, 3.2, 4.1, 7.1, 7.2, 9 | None | PRIM11, PRIM12, PRIM14, PRIM15, PRIM4, PRIM5 (+5) | weak_trace |
| CJS-5E.5 | Implementation and cross-implementation structural review, correction urgency, and disclosure terms | `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md` | 3.1, 3.2, 4.1, 5.2, 7.1, 7.2 | None | PRIM12, PRIM15, PRIM6, PROT3, PROT6, corpus_systems.md | weak_trace |

## Findings

### Weak Trace

- **CJS-5.0** `corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md`:7: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 2.1, 3.4, 5.2, 7.1, 7.2, 10.
- **CJS-5A.1** `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md`:16: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 2.1, 4, 5.2, 7.2, 10.
- **CJS-5A.2** `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md`:74: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.1, 6.1, 6.4, 7.1, 9.
- **CJS-5A.3** `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md`:123: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.2, 4, 5.2, 7.1, 7.2.
- **CJS-5A.5** `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md`:236: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.2, 6.2, 6.4, 7.1, 8, 9.
- **CJS-5A.6** `corpus_joint_structure/cjs_05a_00_authority_constraint_secrecy_procedure.md`:281: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 2.1, 3.4, 6.4, 7.1, 8, 10.
- **CJS-5B.1** `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md`:14: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.1, 3.2, 4.1, 7.1, 7.2.
- **CJS-5B.2** `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md`:47: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.2, 4, 7.1, 7.2.
- **CJS-5B.4** `corpus_joint_structure/cjs_05b_00_evidence_audit_claim_integrity.md`:133: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.2, 3.3, 4, 7.1, 7.2.
- **CJS-5C.1** `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md`:14: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 2.1, 4, 5.2, 6.4, 8, 10.
- **CJS-5C.2** `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md`:75: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.4, 5.2, 7.1, 8.
- **CJS-5C.3** `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md`:129: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 2, 3.2, 4, 7.1, 8.
- **CJS-5C.4** `corpus_joint_structure/cjs_05c_00_participation_comprehension_disclosure.md`:191: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.2, 6.2, 7.1, 8.
- **CJS-5D.1** `corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md`:13: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.1, 4.1, 5.1, 7.1, 9.
- **CJS-5D.2** `corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md`:62: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 5.1, 6.1, 7.1, 8, 9.
- **CJS-5D.3** `corpus_joint_structure/cjs_05d_00_dependency_exit_lifecycle_integrity.md`:127: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.2, 6.2, 7.1, 8, 9.
- **CJS-5E.1** `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md`:15: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.1, 4.1, 5.1, 6.1, 7, 9.
- **CJS-5E.3** `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md`:139: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.1, 4.1, 6.1, 7.1, 9.
- **CJS-5E.4** `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md`:177: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.1, 3.2, 4.1, 7.1, 7.2, 9.
- **CJS-5E.5** `corpus_joint_structure/cjs_05e_00_failure_robustness_intervention_correction.md`:260: Principle basis is inferred from subject matter, not directly cited to Chapter 01. Inferred principles: 3.1, 3.2, 4.1, 5.2, 7.1, 7.2.

## Remediation Roadmap

1. Treat `weak_trace` items as advisory unless the project wants every CJS-5 cluster to cite Chapter 01 directly.
2. If direct traceability is desired, add concise `Read it with` bullets to high-risk clusters first: CJS-5A.2, CJS-5A.4, CJS-5A.5, CJS-5C.*, CJS-5D.*, and CJS-5E.*.
3. Keep remediation text limited to routing metadata; do not convert CJS-5 into a competing Chapter 01 or Chapter Five doctrine layer.

## Manual Review Notes

High-risk families for human review are CJS-5A, CJS-5C, CJS-5D, and CJS-5E. The automated pass checks structure and trace signals; semantic adequacy should be reviewed against the operative text before making corpus edits.
