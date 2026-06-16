# TODO

**2026-06-15 archive snapshot:** Full active meta-file text immediately before the 2026-06-15 slim pass. Completed P3 and CI→CJS/CS relocation narratives moved to [TODO_COMPLETED_P3_HOLISTIC_REDUNDANCY_SWEEP.md](TODO_COMPLETED_P3_HOLISTIC_REDUNDANCY_SWEEP.md) and [TODO_COMPLETED_CI_CJS_CS_RELOCATION_2026-06.md](TODO_COMPLETED_CI_CJS_CS_RELOCATION_2026-06.md). Prior full archive: [TODO_ARCHIVED_2026-05-07.md](TODO_ARCHIVED_2026-05-07.md).

**2026-05-07 root retirement:** Active `TODO.md` at repository root was retired to [TODO_ARCHIVED_2026-05-07.md](TODO_ARCHIVED_2026-05-07.md) without a slim replacement. The sections below reconstruct the last known active backlog plus work completed on branch `cursor/ci-cjs-relocation-pointer-calibration-closure` through 2026-06-14.

**2026-05-06 cleanup:** Full active snapshots are preserved at [archive/TODO_SNAPSHOT_2026-05-06.md](archive/TODO_SNAPSHOT_2026-05-06.md). Migration backlog from Constitution/ folder archived as completed. Older snapshots and completed-work archives remain listed below.

**2026-04-30 cleanup:** Full active snapshots are preserved at [archive/TODO_SNAPSHOT_2026-04-30.md](archive/TODO_SNAPSHOT_2026-04-30.md) and [archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md](archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md). Older snapshots and completed-work archives remain listed below.

## Editor Checklist (Pre-Review / Pre-Merge)

- [x] Filename convention check: use underscore-style canonical names, no spaces. Canonical chapter and corpus files are listed in [README.md](README.md).
- [x] Corpus edits happen in canonical Markdown files only; no parallel `.txt` layer.
- [x] Reference integrity check: update prose, links, and script references in the same change when filenames move.
- [x] Regression suite check: update and run `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` for any material constitutional change. **Deferred in this continuation:** the scenarios file is present, but regression validation and evidence publication are out of active scope unless reinstatement is requested.
- [x] Single-home discipline check: new term definitions follow [doc_architecture.md](doc_architecture.md) section 4 owner rules.
- [x] Layered framing check: apply `definitions -> principles -> articles -> core -> joint structure -> institutions/systems/forum` and pointer-first restatement discipline.

## Current Chapter Map

- **Ch 1:** [core_00-01_principles.md](core_00-01_principles.md)
- **Ch 2-4:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)
- **Ch 5:** [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md), [core_05-05_definitions_b_semi_independent.md](core_05-05_definitions_b_semi_independent.md), [core_05-05_definitions_c_dependent_clusters.md](core_05-05_definitions_c_dependent_clusters.md)
- **Ch 6:** [core_06-06_standing_classification.md](core_06-06_standing_classification.md), [core_06-06_standing_integration.md](core_06-06_standing_integration.md)
- **Ch 7:** [core_07-07_misconduct.md](core_07-07_misconduct.md)
- **Ch 8:** [core_08-08_forum.md](core_08-08_forum.md)
- **Ch 9:** [core_09-09_rights_part_a.md](core_09-09_rights_part_a.md) through [core_09-09_rights_part_d.md](core_09-09_rights_part_d.md)
- **Ch 10:** [core_10-10_governance.md](core_10-10_governance.md)
- **Ch 11-13:** [core_11-13_amendment.md](core_11-13_amendment.md)
- **Ch 14:** [core_14-14_incorporation.md](core_14-14_incorporation.md)
- **Companion corpus:** [corpus_joint_structure.md](corpus_joint_structure.md), [corpus_systems.md](corpus_systems.md), [corpus_institutions.md](corpus_institutions.md), [corpus_forum.md](corpus_forum.md)

Retired compatibility wrapper names such as `core_constitution.md`, `core_definitions.md`, and `core_amendment.md` are not current source files. Use the numbered files above.

## Open Backlog

### P2 - Load-Bearing Capitalization Pass

- [ ] **P2 - Standardize reader-signal capitalization for core constitutional objects:** Capitalize **Wellbeing**, **Safety**, **Truth**, **Rights Floor**, and **Foundational Rights** when they identify named constitutional objectives, constraints, layers, or chapter titles; keep ordinary lowercase uses for generic wellbeing, safety, truth, and rights-language.

  **Acceptance checks:** add a short capitalization rule to `doc_architecture.md`; sweep active binding/current guidance scope for `rights floor`, `rights-floor`, `Foundational rights`, and named-object uses of `wellbeing` / `safety` / `truth`; preserve lowercase ordinary uses such as `challenge rights`, `review rights`, `audit rights`, `sentient wellbeing`, and operational `safety`; update `tools/lexical_vocabulary_audit.py` with high-confidence drift checks for **Rights Floor** / **Foundational Rights** casing; run `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`. Regression scenario validation remains deferred unless separately reinstated.

### P3 - Holistic Redundancy Sweep

- [x] **User acceptance gate:** Accept, repurpose, or continue the holistic redundancy / definitions-first sweep after a final grep-per-theme dedup across the four companion corpus files.

  **Engineer status as of 2026-04-30 cleanup:** Many 2026-04-29 non-regression passes corrected stale chapter, article, anchor, and terminology routing without flipping this user-owned checkbox. Full detail is archived in [archive/TODO_SNAPSHOT_2026-04-30.md](archive/TODO_SNAPSHOT_2026-04-30.md) and summarized in [MEMLOG.md](MEMLOG.md).

  **2026-04-30 continuation:** The non-regression redundancy sweep continued across the four companion corpus files and was committed as `ad3f704` (`Tighten companion corpus ownership pointers`). Detailed pass notes are archived in [archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md](archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md) and [MEMLOG.md](MEMLOG.md). Regression testing was intentionally left out.

  **2026-04-30 continuation addendum:** Normalized remaining **Protocol A**, subsection **G** continuity pointers in `corpus_forum.md`, `corpus_institutions.md`, and `corpus_systems.md` so forum, institutional, and steward-continuity references use the established owner phrasing instead of the stale **Protocol A G** shorthand. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`.

  **2026-04-30 continuation addendum 2:** Completed another targeted non-regression grep pass for owner-phrasing drift across the companion corpus. Normalized `corpus_institutions.md` S2/S3 references, tightened a **Sentient Constitution Chapter Nine, Article XV-A** pointer, restored **Article X-C**/**Article X-A** to the CI-15 rights-owner boundary, and tightened `corpus_systems.md` **Article XXV-A** transition routing to **Sentient Constitution Chapter Nine**. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`. Regression testing remained intentionally omitted.

  **2026-05-06 continuation addendum:** Continued the non-regression companion-corpus redundancy sweep for remaining owner-phrasing drift. Tightened `corpus_institutions.md` **CI-1.5**, **CI-6**, and **CI-9.1B** into pointer-first applications of Chapter Seven, `corpus_joint_structure.md` **CJS-3.12**, and delegated-body owner language; tightened `corpus_forum.md` **CC-6.1** and **CC-10.0** into pointer-first applications of **CJS-3.3**, **CJS-3.33**, and existing rights owners; tightened `corpus_systems.md` **Protocol S4** and **Protocol S5** so Article XXI-A and due-process rights stay in their owner layers while the systems companion preserves only allocation, cause-mapping, funding-record, and incentive-governance mechanics. Also corrected local Markdown emphasis and sentence-wrap defects found during the sweep. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`. Regression testing remained intentionally omitted.

  **Suggested acceptance check:** run targeted theme greps across `corpus_joint_structure.md`, `corpus_systems.md`, `corpus_institutions.md`, and `corpus_forum.md`; convert duplicative companion prose to pointers where it repeats Chapter Five definitions or Chapter Nine rights without adding implementation detail.

### Deferred - P1 Regression And Evidence

*Out of active continuation scope unless regression reinstatement is requested.*

- [ ] **P1 - Validate regression scenarios and evidence workflow:** reconcile the present `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` file with the `evidence/<YYYY-MM-DD>/` workflow so matrix integrity, snapshot validation, and dated artifact recording resume as an active process.

  **Acceptance checks:** `make scenario-audit` is intentionally run as a reinstatement step; `.cursor/rules/testing.mdc` suspension language is retired or reconciled; TODO/editor checklist deferral notes are removed; queued observations are landed as `RS-*` rows where appropriate; dated evidence artifacts are recorded for the reinstatement run.

- [ ] **P1 - Humanity/Individual stress-pack regression integration (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`):** blocked on regression-scenarios reinstatement. Complete first-pass validation and publish evidence artifacts under the restored evidence tree.

## TODO Maintenance And Archiving

Authoritative normative state is in the binding corpus files named in [README.md](README.md). `TODO.md`, [MEMLOG.md](MEMLOG.md), [doc_architecture.md](doc_architecture.md), and implementation worklists are process aids only.

Keep this active file limited to:

- editor checks that should remain visible before each review;
- current open work;
- short archive pointers for completed work.

Move completed narratives to `archive/` when they make the active file hard to scan. Archived TODO text is history only; if it disagrees with the current corpus, the corpus wins.

## Standard Procedure

For future substantive cleanup passes:

1. Commit corpus/source changes first, excluding generated noise such as `.DS_Store`.
2. Then snapshot active meta files such as `TODO.md`, `MEMLOG.md`, and `implementation/ARCHITECTURE_WORKLIST.md` into `archive/`.
3. Trim active meta files back to current open work, archive pointers, and the minimum context needed for the next session.
4. Keep regression/evidence artifacts separate unless regression reinstatement or validation is explicitly in scope.

## Archives

- **2026-04-30 post-commit active snapshot:** [archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md](archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md)
- **2026-04-30 active cleanup snapshot:** [archive/TODO_SNAPSHOT_2026-04-30.md](archive/TODO_SNAPSHOT_2026-04-30.md)
- **2026-04-29 snapshot:** [archive/TODO_SNAPSHOT_2026-04-29.md](archive/TODO_SNAPSHOT_2026-04-29.md)
- **2026-04-26 full archive and snapshot:** [archive/TODO_ARCHIVED_2026-04-26.md](archive/TODO_ARCHIVED_2026-04-26.md), [archive/TODO_SNAPSHOT_2026-04-26.md](archive/TODO_SNAPSHOT_2026-04-26.md)
- **Completed-work cuts:** [archive/TODO_COMPLETED_2026-04-17.md](archive/TODO_COMPLETED_2026-04-17.md), [archive/TODO_COMPLETED_2026-04-16.md](archive/TODO_COMPLETED_2026-04-16.md), [archive/TODO_COMPLETED_2026-Q2.md](archive/TODO_COMPLETED_2026-Q2.md), [archive/TODO_COMPLETED_SC-Corpus-2026.04.md](archive/TODO_COMPLETED_SC-Corpus-2026.04.md)
- **Structural sync and older P3 sub-items:** [archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md](archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md)

## Open Backlog (added after 2026-05-07 root retirement — now archived)

### CI→CJS relocation, companion splits, and CS label migration

- [x] **CI→CJS relocation pilot closure:** owner-map calibration, pointer discipline, and evidence publication through 2026-06-14 (`28f5f7b` … `0276156`). Detail: [TODO_COMPLETED_CI_CJS_CS_RELOCATION_2026-06.md](TODO_COMPLETED_CI_CJS_CS_RELOCATION_2026-06.md).

- [x] **AI corpus navigation layer:** required migration scope closed per `plans/ai_corpus_optimization_plan.md` (2026-05-30 closeout).
