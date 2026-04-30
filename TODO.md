# TODO

**2026-04-30 cleanup:** A full pre-cleanup snapshot is preserved at [archive/TODO_SNAPSHOT_2026-04-30.md](archive/TODO_SNAPSHOT_2026-04-30.md). Older snapshots and completed-work archives remain listed below.

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

### P3 - Holistic Redundancy Sweep

- [ ] **User acceptance gate:** Accept, repurpose, or continue the holistic redundancy / definitions-first sweep after a final grep-per-theme dedup across the four companion corpus files.

  **Engineer status as of 2026-04-30 cleanup:** Many 2026-04-29 non-regression passes corrected stale chapter, article, anchor, and terminology routing without flipping this user-owned checkbox. Full detail is archived in [archive/TODO_SNAPSHOT_2026-04-30.md](archive/TODO_SNAPSHOT_2026-04-30.md) and summarized in [MEMLOG.md](MEMLOG.md).

  **2026-04-30 continuation:** Targeted theme greps across the four companion corpus files found concrete self-healing duplication in `corpus_systems.md`; Protocol S4 now points to Protocol A subsection H and keeps only ecosystem-specific cross-checks. A follow-on pass converted the decentralized-continuity self-healing section into a Protocol A subsection H application, preserving only partition/offline/rejoin-specific safeguards. A later comprehensibility pass tightened Protocol B into an Article XX / CJS-3.15-through-3.19 / CJS-3.27 application while keeping systems-specific scaling, audit, modularity, resilience, incident-learning, and simplification checks. A further institutional-continuity pass shortened `corpus_institutions.md` **CI-11** so it states only the institutional trigger and supervisory interface for Protocol A subsection G, leaving operative exercise, crisis-communication, recovery-record, and remediation requirements in `corpus_systems.md`. A transition-governance pass then tightened `corpus_institutions.md` **CI-14** into the institutional custody, authorization, and oversight interface for `corpus_systems.md` **Protocol T**, leaving system phase structure, gate criteria, fallback handling, off-ramps, and re-baselining mechanics in Protocol T. The same pass corrected a stale Protocol D internal reference from section **5.D** to **5A**. A forum-records pass then replaced the `corpus_forum.md` **CC-12** scaffold with a pointer-first standard records, forms, access classes, evidence artifacts, publication/retention, and non-compliance section aligned to `corpus_joint_structure.md` **CJS-R12**, and removed stale migration notes saying **CC-3**, **CC-10**, **CC-11**, and **CI-7A/CI-7B** still needed migration. A non-regression cleanup pass then removed process-only regression-coverage prompts from `corpus_institutions.md`, removed the regression-matrix hook from `corpus_forum.md` **CC-10.0**, and converted the `corpus_joint_structure.md` drafting note to use active review notes until regression reinstatement. A further institutional pass corrected stale **CI-1.4** section-range text from **CI-1 through CI-16** to **CI-1 through CI-24** and tightened **CI-15A** so Chapter Five / Article XVII-D / PRIM7 / PROT4 ownership is stated once in a pointer-first owner-boundary paragraph while preserving institutional registry, access-order, sunset, and appeal mechanics. A further forum-continuity pass tightened `corpus_forum.md` **CC-11** so generic emergency lifecycle, crisis-communication, exercise, restoration-evidence, and audit-trail mechanics point to `corpus_systems.md` **Protocol A** subsection **G**, while **CC-11** keeps forum-specific activation, routing, quorum, backup-forum, docket, and adjudicative-review rules. A final forum/institution pass tightened `corpus_forum.md` **CC-8** protected-investigation language into a pointer-first Article XIII-A / Chapter Five / secrecy-rules interface while preserving only forum-specific authorization, renewal, taint-remedy, and later-challenge record fields; tightened `corpus_forum.md` **CC-10.15** so Protocol C section 10 remains the lived-condition owner while **CC-10.15** records only forum performance/restoration tracking; and shortened `corpus_institutions.md` **CI-7.3** Article XIII-A monitoring language into a monitor-interface pointer to Article XIII-A and **CC-8**. A science-publication pass then tightened `corpus_institutions.md` **CI-15B** into the institutional custody, evidence-package, conflict-control, reliance-gate, correction, access, incentive, and appeal interface for **Article XVII-E**, leaving constitutional meaning in Chapter Nine and forum routing in `corpus_forum.md` **CC-9**. A final monitor-interface pass tightened the remaining **CI-7.3** Article XIII-A monitoring-emphasis paragraph so it tests pathway function, independence failure, protected-activity chill, secrecy drift, notice/disclosure availability, and bypass indicators without restating Article XIII-A safeguards. Regression testing was intentionally left out.

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

## Archives

- **2026-04-30 active cleanup snapshot:** [archive/TODO_SNAPSHOT_2026-04-30.md](archive/TODO_SNAPSHOT_2026-04-30.md)
- **2026-04-29 snapshot:** [archive/TODO_SNAPSHOT_2026-04-29.md](archive/TODO_SNAPSHOT_2026-04-29.md)
- **2026-04-26 full archive and snapshot:** [archive/TODO_ARCHIVED_2026-04-26.md](archive/TODO_ARCHIVED_2026-04-26.md), [archive/TODO_SNAPSHOT_2026-04-26.md](archive/TODO_SNAPSHOT_2026-04-26.md)
- **Completed-work cuts:** [archive/TODO_COMPLETED_2026-04-17.md](archive/TODO_COMPLETED_2026-04-17.md), [archive/TODO_COMPLETED_2026-04-16.md](archive/TODO_COMPLETED_2026-04-16.md), [archive/TODO_COMPLETED_2026-Q2.md](archive/TODO_COMPLETED_2026-Q2.md), [archive/TODO_COMPLETED_SC-Corpus-2026.04.md](archive/TODO_COMPLETED_SC-Corpus-2026.04.md)
- **Structural sync and older P3 sub-items:** [archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md](archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md)
