# TODO

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

### Migration from Constitution/ Folder (Recent Work Salvage)

**Context:** User worked in the wrong folder (`/Users/kfoelsch/Documents/Constitution/`) recently (last 2 days: May 5-6, 2026). Salvageable work identified via file mod dates and content diffs. Plan focuses on selective changes, not global overwrites.

- [ ] **Copy new/unique files (no conflicts):**
  - `tools/ch1_ch5_alignment_audit.py`
  - `tools/ch5_stub_pointer_audit.py`
  - `tools/ch5_alphabetical_directory_audit.py`
  - `tools/README.md`
  - Entire `evidence/2026-05-06/` directory (audit artifacts: `ch1_ch5_traceability_matrix_2026-05-06.csv`, `ch1_ch5_alignment_report_2026-05-06.md`, `ch1_ch5_audit_log_2026-05-06.json`)
  - Skip non-content files (`.DS_Store`, `__pycache__`)

- [ ] **Apply selective changes to existing files (based on diffs):**
  - Priority: Files modified on May 6, then May 5.
  - `core_02-04_definition_mechanics.md`: Merge added text on joint component satisfaction and anti-evasion rules.
  - `architecture_primer.md`: Add "locked" status note; restructure framing into bullet points/tables.
  - Other core files (e.g., `core_05-05_definitions_b_semi_independent.md`, `core_09-09_rights_part_a.md`): Review diffs and apply readability/rephrasing changes only (e.g., emphasis additions, minor rearrangements). Avoid deletions that remove content.
  - For locked files (`architecture_primer.md`, `core_02-04_definition_mechanics.md`): Use targeted edits if direct copy fails.

- [ ] **Validation and testing:**
  - Run new tools (e.g., `tools/ch1_ch5_alignment_audit.py`) to ensure functionality.
  - Check links/references in updated `.md` files.
  - Run workspace build/lint tools if available (e.g., `make reference-audit`).

**Total candidates:** ~25 files. Skip anything unchanged or older than 2 days.

### P3 - Holistic Redundancy Sweep

- [ ] **User acceptance gate:** Accept, repurpose, or continue the holistic redundancy / definitions-first sweep after a final grep-per-theme dedup across the four companion corpus files.

  **Engineer status as of 2026-04-30 cleanup:** Many 2026-04-29 non-regression passes corrected stale chapter, article, anchor, and terminology routing without flipping this user-owned checkbox. Full detail is archived in [archive/TODO_SNAPSHOT_2026-04-30.md](archive/TODO_SNAPSHOT_2026-04-30.md) and summarized in [MEMLOG.md](MEMLOG.md).

  **2026-04-30 continuation:** The non-regression redundancy sweep continued across the four companion corpus files and was committed as `ad3f704` (`Tighten companion corpus ownership pointers`). Detailed pass notes are archived in [archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md](archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md) and [MEMLOG.md](MEMLOG.md). Regression testing was intentionally left out.

  **2026-04-30 continuation addendum:** Normalized remaining **Protocol A**, subsection **G** continuity pointers in `corpus_forum.md`, `corpus_institutions.md`, and `corpus_systems.md` so forum, institutional, and steward-continuity references use the established owner phrasing instead of the stale **Protocol A G** shorthand. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`.

  **2026-04-30 continuation addendum 2:** Completed another targeted non-regression grep pass for owner-phrasing drift across the companion corpus. Normalized `corpus_institutions.md` S2/S3 references, tightened a **Sentient Constitution Chapter Nine, Article XV-A** pointer, restored **Article X-C**/**Article X-A** to the CI-15 rights-owner boundary, and tightened `corpus_systems.md` **Article XXV-A** transition routing to **Sentient Constitution Chapter Nine**. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`. Regression testing remained intentionally omitted.

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
