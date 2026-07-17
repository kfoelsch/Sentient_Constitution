# Chapter 01 -> CJS-5 Principle Alignment Audit Report

**Date:** 2026-07-07
**Workflow:** CH1_CJS5_PRINCIPLE_ALIGNMENT_CHECK
**Auditor:** Automated static extraction with manual-review flags

## Executive Summary

| Metric | Result | Status |
|---|---:|---|
| CJS-5 clusters discovered | 24/23 | REVIEW |
| Clusters with complete OP-O/OP-E/OP-C triads | 24/24 | PASS |
| Clusters with direct Chapter 01 citations | 24/24 | REVIEW |
| Clusters with inferred Chapter 01 basis | 24/24 | PASS |
| Owner-routing issues | 0 | PASS |
| Potential overreach flags | 0 | PASS |

## Overall Assessment

CJS-5 is operationally aligned with Chapter 01 at the structural level: all expected clusters were found, all operational rules carry complete `OP-O` / `OP-E` / `OP-C` triads, and each cluster has an inferred Chapter 01 principle basis. The main audit finding is trace explicitness: most CJS-5 clusters rely on owner-file and subject-matter routing rather than direct Chapter 01 citations.

## Cluster Traceability Summary

| Cluster | Title | File | Inferred Chapter 01 Principles | Direct Chapter 01 Refs | Owner Refs | Status |
|---|---|---|---|---|---|---|
| CJS-5.0 | Cross-band: Role-definition preface and standing competency gate interface | `corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md` | 2.1, 3.4, 5.2, 7.1, 7.2, 10 | 2.1 | Article XI-D, CI, CS, Chapter Five, Chapter Nine, Chapter Six (+6) | complete |
| CJS-5.2 | Oversight: reflexive transparency and accountability terms | `corpus_joint_structure/cjs_05o_oversight_operations.md` | 3.2, 4, 5.2, 7.1, 7.2 | 12.1, 12.2, 2.2, 3, 4.2, linked | Chapter Five, Chapter Six | complete |
| CJS-5.3 | Oversight: auditability and reconstructability terms | `corpus_joint_structure/cjs_05o_oversight_operations.md` | 3.2, 4, 7.1, 7.2 | 12.1, 12.2, 2.2, 3, linked | Article VII-B, Article XV-A, Chapter Five, Chapter Six | complete |
| CJS-5.4 | Oversight: tiered transparency and audit-access terms | `corpus_joint_structure/cjs_05o_oversight_operations.md` | 3.2, 6.2, 6.4, 7.1, 8 | 11.2, 11.4, 12.1, 13, 2.2, 6.3.1, linked | Article VII-B, Article XV-A, CF, CS, Chapter Five, Chapter Six (+2) | complete |
| CJS-5.5 | Oversight: independent verification and claim-integrity terms | `corpus_joint_structure/cjs_05o_oversight_operations.md` | 3.2, 3.3, 4, 7.1, 7.2 | 12.1, 12.2, 2.2, 2.3, 3, linked | Chapter Five, Chapter Six | complete |
| CJS-5.6 | Oversight: integrity assurance and resilience operations | `corpus_joint_structure/cjs_05o_oversight_operations.md` | 3.1, 3.2, 4.1, 7.1, 7.2 | 12.1, 12.2, 2.1, 2.2, 3.1, linked | CF, CI, CS, Chapter Five, Chapter Six, Core definitions (+3) | complete |
| CJS-5.7 | Participation: quorum and participatory legitimacy terms | `corpus_joint_structure/cjs_05p_participation_operations.md` | 2.1, 4, 5.2, 6.4, 8, 10 | 7.1, linked | Article IX-C, Article XI, Article XI-A, Chapter Five, Chapter Six, Chapter Twelve | complete |
| CJS-5.8 | Participation: comprehensibility and cognitive accessibility terms | `corpus_joint_structure/cjs_05p_participation_operations.md` | 3.4, 5.2, 7.1, 8 | 12.1, 13, 2.4, 4.2, linked | Chapter Five, Chapter Six, corpus_systems.md | complete |
| CJS-5.9 | Participation: salience integrity and attention-allocation terms | `corpus_joint_structure/cjs_05p_participation_operations.md` | 2, 3.2, 4, 7.1, 8 | 12.1, 13, 2.2, 3, 8, linked | Article XV-A, Chapter Five, Chapter Six | complete |
| CJS-5.10 | Participation: disclosure sufficiency and observability terms | `corpus_joint_structure/cjs_05p_participation_operations.md` | 3.2, 6.2, 7.1, 8 | 11.2, 12.1, 13, 2.2, linked | Article VII-B, Article XV-A, Chapter Five, Chapter Six | complete |
| CJS-5.11 | Accountability: distributed and proportional authority terms | `corpus_joint_structure/cjs_05a_accountability_operations.md` | 2.1, 4, 5.2, 7.2, 10 | 13, 13.1, 13.2, 13.3, 13.3.1, 13.3.2, 7.1, linked | Article I-D, Article III-D, Article XII-A, Article XII-E, Article XIII-A, Article XIX (+5) | complete |
| CJS-5.12 | Accountability: burden-of-justification and constraint terms | `corpus_joint_structure/cjs_05a_accountability_operations.md` | 6.1, 6.3, 6.4, 7.1, 8, 9 | 11.1, 11.3, 11.4, 12.1, 13, 14, 6.3.1, linked | CF, CI, CS, Chapter Five, Chapter Six, Core definitions (+2) | complete |
| CJS-5.13 | Accountability: procedural integrity and adjudication terms | `corpus_joint_structure/cjs_05a_accountability_operations.md` | 2.1, 3.4, 6.4, 7.1, 8, 10 | 7.1, linked | CF, CI, CS, Chapter Five, Chapter Six, core_11-11_forum.md (+3) | complete |
| CJS-5.14 | Accountability: intervention governance and override-authorization terms | `corpus_joint_structure/cjs_05a_accountability_operations.md` | 3.1, 6.1, 6.4, 7.1, 9 | 11.1, 11.4, 12.1, 14, 2.1, linked | CF, Chapter Five, Chapter Six | complete |
| CJS-5.15 | Accountability: structural review, correction urgency, and disclosure terms | `corpus_joint_structure/cjs_05a_accountability_operations.md` | 3.1, 3.2, 4.1, 5.2, 7.1, 7.2 | 12.1, 12.2, 2.1, 2.2, 3.1, 4.2, linked | CS, Chapter Five, Chapter Six, corpus_systems.md | complete |
| CJS-5.16 | Continuity: dependency integrity and disclosure terms | `corpus_joint_structure/cjs_05c_continuity_operations.md` | 3.1, 4.1, 5.1, 7.1, 9 | 12.1, 14, 2.1, 3.1, 4.1, linked | Article XV-A, CI, CS, Chapter Five, Chapter Six, corpus_systems.md | complete |
| CJS-5.17 | Continuity: interoperability, portability, and exit-integrity terms | `corpus_joint_structure/cjs_05c_continuity_operations.md` | 5.1, 6.1, 7.1, 8, 9 | 11.1, 12.1, 13, 14, 4.1, linked | Article II-E, Article XIX, Article XV-A, CI, CS, Chapter Five (+3) | complete |
| CJS-5.18 | Continuity: data-retention and lifecycle-integrity terms | `corpus_joint_structure/cjs_05c_continuity_operations.md` | 3.2, 6.2, 7.1, 8, 9 | 11.2, 12.1, 13, 14, 2.2, linked | CS, Chapter Five, Chapter Six, corpus_systems.md | complete |
| CJS-5.19 | Continuity: graceful degradation and failure-mode integrity terms | `corpus_joint_structure/cjs_05c_continuity_operations.md` | 3.1, 4.1, 5.1, 6.1, 7, 9 | 11.1, 12, 14, 2.1, 3.1, 4.1, linked | Chapter Five, Chapter Six, corpus_systems.md | complete |
| CJS-5.20 | Continuity: reversibility and containment terms | `corpus_joint_structure/cjs_05c_continuity_operations.md` | 3.1, 4.1, 6.1, 7.1, 9 | 11.1, 12.1, 14, 2.1, 3.1, linked | Chapter Five, Chapter Six | complete |
| CJS-5.21 | Continuity: adversarial robustness and abuse-resistance terms | `corpus_joint_structure/cjs_05c_continuity_operations.md` | 3.1, 3.2, 4.1, 7.1, 7.2, 9 | 12.1, 12.2, 14, 2.1, 2.2, 3.1, linked | Chapter Five, Chapter Six | complete |
| CJS-5.22 | Integrative: constrained-secrecy and protected-investigation terms | `corpus_joint_structure/cjs_05i_integrative_operations.md` | 3.2, 6.2, 6.4, 7.1, 8, 9 | 11.2, 11.4, 12.1, 13, 14, 2.2, linked | Chapter Five, Chapter Six | complete |
| CJS-5.23 | Integrative: intervention and override integrity terms | `corpus_joint_structure/cjs_05i_integrative_operations.md` | 3.1, 6.1, 6.4, 7.1, 9 | 11.1, 11.4, 12.1, 14, 2.1, 6.3.1, linked | CF, Chapter Five, Chapter Six, corpus_forum.md | complete |
| CJS-5.1 | Library: Constitutional compass and cluster map | `corpus_joint_structure/cjs_05_cross_implementation_operational_terms.md` | 2.1, 3, 3.1, 3.2, 3.3, 3.4, 4, 4.1, 5, 5.1, 5.2, 6, 6.1, 6.2, 6.3, 6.4, 7, 7.1, 7.2, 8, 9, 10 | 6.2, 8.1, 8.2, linked | CF, CI, CS, Chapter Five | complete |

## Findings

No findings.
## Remediation Roadmap

1. Treat `weak_trace` items as advisory unless the project wants every CJS-5 cluster to cite Chapter 01 directly.
2. If direct traceability is desired, add concise `Read it with` bullets to high-risk clusters first: CJS-5.14, CJS-5.12, CJS-5.22, CJS-5.7–CJS-5.10.*, CJS-5.16–CJS-5.18.*, and CJS-5.19–CJS-5.15.*.
3. Keep remediation text limited to routing metadata; do not convert CJS-5 into a competing Chapter 01 or Chapter Five doctrine layer.

## Manual Review Notes

High-risk families for human review are CJS-5.11–CJS-5.13, CJS-5.7–CJS-5.10, CJS-5.16–CJS-5.18, and CJS-5.19–CJS-5.15. The automated pass checks structure and trace signals; semantic adequacy should be reviewed against the operative text before making corpus edits.
