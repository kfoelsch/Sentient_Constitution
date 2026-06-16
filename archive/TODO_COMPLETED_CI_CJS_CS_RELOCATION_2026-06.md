# Archived TODO — CI→CJS relocation, companion splits, and CS label migration

**Archived:** 2026-06-15. **Active checklist:** [`TODO.md`](../TODO.md).

## Status

Closed on branch `cursor/ci-cjs-relocation-pointer-calibration-closure` through pre-release cleanup commit `0276156` (2026-06-14 evidence refresh series through `c5c60df`).

## Completed scope

- **CI→CJS relocation pilot:** topical owner-map tightening, structural floors, residual pointer calibration, and owner-duty routing across `corpus_institutions/` and `corpus_joint_structure/` (commits from `89e58e3` through `28f5f7b`).
- **Companion humanization:** reader-facing openings, navigation footers, and retirement of stale CP labels (`6883a15`, `e1d0c9c`).
- **CJS boundary and router discipline:** CJS-1 reader-first renumbering (`ce2db41`); CJS-2.1 router-first primary-owner routing with bidirectional sync (`71364d2`); opening trilogy alignment across CI, CS, and CF (`381688c`).
- **Rule 14:** in-paragraph link discipline and regression audit (`949b5f3`).
- **CJS-5 cluster library:** classification-scaled governance burden moved to **CJS-5.2**; numeric cluster IDs (`2100178`).
- **CJS-4:** hybrid authority nested under **CJS-4.1**; trace routing audit (`4f471d2`); retired **CJS-4.2** stub removed and sections renumbered (`0276156`).
- **Chapter Five Merits Determination** and support-role boundary cites (`ab34ed0`).
- **`corpus_systems` split:** substantive CS text in `corpus_systems/` subfiles with routing wrapper (`022c211`).
- **CS stable IDs:** **CS-3**, **CS-4**, **CS-5** relabel across corpus, tooling, README, and `doc_architecture.md` (`39a6667` through `c5c60df`).
- **AI corpus navigation layer:** required migration scope closed per [`plans/ai_corpus_optimization_plan.md`](../plans/ai_corpus_optimization_plan.md) (2026-05-30 closeout note).

## Verification pattern

Non-regression companion passes used `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`. CI→CJS relocation evidence refreshed under `evidence/` through 2026-06-14. Regression scenario validation (`make scenario-audit`) remained out of scope unless separately reinstated.

## Narrative detail

Session-level notes for this closure window are in [MEMLOG_SNAPSHOT_2026-06-15.md](MEMLOG_SNAPSHOT_2026-06-15.md). Prior meta-file state before root retirement: [TODO_ARCHIVED_2026-05-07.md](TODO_ARCHIVED_2026-05-07.md), [MEMLOG_ARCHIVED_2026-05-07.md](MEMLOG_ARCHIVED_2026-05-07.md).
