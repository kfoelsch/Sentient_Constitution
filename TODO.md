# TODO

**2026-06-17 housecleaning:** Older TODO/MEMLOG snapshots removed from `archive/`; retrieve from git history if needed. Canonical architecture archives remain under [README.md](README.md) *Binding vs support* and [doc_architecture.md](doc_architecture.md). Root retirement snapshots: [archive/TODO_ROOT_RETIRED_2026-05-01.md](archive/TODO_ROOT_RETIRED_2026-05-01.md).

## Editor Checklist (Pre-Review / Pre-Merge)

- [x] Filename convention check: use underscore-style canonical names, no spaces. Canonical chapter and corpus files are listed in [README.md](README.md).
- [x] Corpus edits happen in canonical Markdown files only; no parallel `.txt` layer.
- [x] Reference integrity check: update prose, links, and script references in the same change when filenames move.
- [x] Regression suite check: update and run `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` for any material constitutional change. **Deferred in this continuation:** the scenarios file is present, but regression validation and evidence publication are out of active scope unless reinstatement is requested.
- [x] Single-home discipline check: new term definitions follow [doc_architecture.md](doc_architecture.md) section 4 owner rules.
- [x] Layered framing check: apply `definitions -> principles -> articles -> core -> joint structure -> institutions/systems/forum` and pointer-first restatement discipline.

## Current Chapter Map

- **Ch 1:** [core_00_preamble.md](core_00_preamble.md), [core_01_a_values_principles.md](core_01_a_values_principles.md) (Part A), [core_01_b_interaction_interpretation.md](core_01_b_interaction_interpretation.md) (Part B), and [core_01_c_stewardship_capacity_principles.md](core_01_c_stewardship_capacity_principles.md) (Part C)
- **Ch 2–3:** [core_02-03_definition_mechanics.md](core_02-03_definition_mechanics.md)
- **Ch 4:** [core_04-04_burden_traceability_verification.md](core_04-04_burden_traceability_verification.md)
- **Ch 5:** Part A compass — [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md); band files — [core_05defs_oversight.md](core_05defs_oversight.md), [core_05defs_participation.md](core_05defs_participation.md), [core_05defs_accountability.md](core_05defs_accountability.md), [core_05defs_continuity.md](core_05defs_continuity.md), [core_05defs_integrative.md](core_05defs_integrative.md) (retired Part B/C → [archive/core_ch5_retired/](archive/core_ch5_retired/README.md))
- **Ch 6:** [core_06-06_rights_part_a.md](core_06-06_rights_part_a.md) through [core_06-06_rights_part_d.md](core_06-06_rights_part_d.md)
- **Ch 7:** [core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation](core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation)
- **Ch 8:** [core_08-08_standing_assessment.md](core_08-08_standing_assessment.md)
- **Ch 9:** [core_09-09_standing_integration.md](core_09-09_standing_integration.md)
- **Ch 10:** Part A [core_10_a_misconduct_designation.md](core_10_a_misconduct_designation.md); Part B [core_10_b_misconduct_pattern_applications.md](core_10_b_misconduct_pattern_applications.md)
- **Ch 11:** [core_11-11_forum.md](core_11-11_forum.md)
- **Ch 12:** [core_12-12_governance.md](core_12-12_governance.md)
- **Ch 13–15:** [core_13-15_amendment.md](core_13-15_amendment.md)
- **Ch 16:** [core_16-16_incorporation.md](core_16-16_incorporation.md)
- **Companion corpus:** [corpus_joint_structure.md](corpus_joint_structure.md) (`corpus_joint_structure/`), [corpus_systems.md](corpus_systems.md) (`corpus_systems/`), [corpus_institutions.md](corpus_institutions.md) (`corpus_institutions/`), [corpus_forum.md](corpus_forum.md) (`corpus_forum/`)

## Open Backlog

### P2 — Load-Bearing Capitalization Pass

- [ ] **P2 — Standardize reader-signal capitalization for core constitutional objects:** Capitalize **Wellbeing**, **Safety**, **Truth**, **Rights Floor**, and **Foundational Rights** when they identify named constitutional objectives, constraints, layers, or chapter titles; keep ordinary lowercase uses for generic wellbeing, safety, truth, and rights-language.

  **Status as of 2026-06-15:** `doc_architecture.md` load-bearing capitalization rule and `tools/lexical_vocabulary_audit.py` drift checks are in place; Rights Floor casing sweep landed in `71984fe`. Remaining acceptance: confirm no high-confidence drift in active binding scope; run `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`.

### Deferred — P1 Regression And Evidence

*Out of active continuation scope unless regression reinstatement is requested.*

- [ ] **P1 — Validate regression scenarios and evidence workflow:** reconcile the present `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` file with the `evidence/<YYYY-MM-DD>/` workflow so matrix integrity, snapshot validation, and dated artifact recording resume as an active process.

  **Acceptance checks:** `make scenario-audit` is intentionally run as a reinstatement step; `.cursor/rules/testing.mdc` suspension language is retired or reconciled; TODO/editor checklist deferral notes are removed; queued observations are landed as `RS-*` rows where appropriate; dated evidence artifacts are recorded for the reinstatement run.

- [ ] **P1 — Humanity/Individual stress-pack regression integration (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`):** blocked on regression-scenarios reinstatement. Complete first-pass validation and publish evidence artifacts under the restored evidence tree.

## TODO Maintenance And Archiving

Authoritative normative state is in the binding corpus files named in [README.md](README.md). `TODO.md`, [MEMLOG.md](MEMLOG.md), [doc_architecture.md](doc_architecture.md), and implementation worklists are process aids only.

Keep this active file limited to editor checks, current open work, and short archive pointers. Move completed narratives to `archive/` when they make the active file hard to scan.

## Archives

- **Architecture process (canonical):** [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md) — see [README.md](README.md)
- **2026-06-18 Chapter Five closeout:** [archive/TODO_SNAPSHOT_2026-06-18.md](archive/TODO_SNAPSHOT_2026-06-18.md), [archive/MEMLOG_SNAPSHOT_2026-06-18.md](archive/MEMLOG_SNAPSHOT_2026-06-18.md)
- **2026-05-01 root retirement:** [archive/TODO_ROOT_RETIRED_2026-05-01.md](archive/TODO_ROOT_RETIRED_2026-05-01.md), [archive/MEMLOG_ROOT_RETIRED_2026-05-01.md](archive/MEMLOG_ROOT_RETIRED_2026-05-01.md)
- **Older TODO/MEMLOG snapshots:** removed 2026-06-17; retrieve from git history if needed
