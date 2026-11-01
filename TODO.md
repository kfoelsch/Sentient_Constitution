# TODO

**2026-10-21 cleanup:** Completed work moved to [TODO_RESOLVED_2026-10-21.md](archive/TODO_RESOLVED_2026-10-21.md). The complete pre-cleanup file is preserved in [TODO_SNAPSHOT_2026-10-21.md](archive/TODO_SNAPSHOT_2026-10-21.md). Older TODO/MEMLOG snapshots removed 2026-06-17 can be retrieved from Git history. Canonical architecture archives remain under [README.md](README.md) *Binding vs support* and [doc_architecture.md](doc_architecture.md).

## Announcement preparation — 2026-10-20

The [working announcement plan](project/plans/announcement_readiness_2026-10-20.md) records the schedule through December 31, [review inventory](project/plans/announcement_review_inventory_2026-10-20.md), batch evidence, and decision queue. It does not waive the publication spec or authorize release.

- [ ] Execute the [case packet](project/trials/agent_cooperative_2026-10-20/CASE_PACKET.md) in a fresh session without the preparer's analysis; retain outputs, assistance, effort, missed gates, and retest results. Human-operator evidence remains separate.
- [ ] Complete the non-core review batches and reopen affected portions when governing core changes.

## Current Chapter Map

- **Preamble and Ch 1:** [core_00.000_preamble.md](core_00.000_preamble.md), [core_01.000_values_principles.md](core_01.000_values_principles.md) (Part A), [core_01.005_interaction_interpretation.md](core_01.005_interaction_interpretation.md) (Part B), and [core_01.010_stewardship_capacity_principles.md](core_01.010_stewardship_capacity_principles.md) (Part C)
- **Ch 2:** [core_02.000_definition_structure.md](core_02.000_definition_structure.md)
- **Ch 3:** [core_03.000_definition_integrity.md](core_03.000_definition_integrity.md)
- **Ch 4:** [core_04.000_burden_traceability_verification.md](core_04.000_burden_traceability_verification.md)
- **Ch 5:** Part A compass — [core_05.000_definitions_home.md](core_05.000_definitions_home.md); band files — [core_05.050_band_oversight.md](core_05.050_band_oversight.md), [core_05.055_band_participation.md](core_05.055_band_participation.md), [core_05.035_band_accountability.md](core_05.035_band_accountability.md), [core_05.040_band_continuity.md](core_05.040_band_continuity.md), [core_05.045_band_integrative.md](core_05.045_band_integrative.md) (retired second and third Chapter Five files → [archive/core_ch5_retired/](archive/core_ch5_retired/README.md))
- **Ch 6:** [core_06.000_rights_part_a.md](core_06.000_rights_part_a.md) through [core_06.020_rights_part_e.md](core_06.020_rights_part_e.md)
- **Ch 7:** [core_07.000_charters.md](core_07.000_charters.md)
- **Ch 8:** [core_08.000_functional_independence_separation_of_duties.md](core_08.000_functional_independence_separation_of_duties.md)
- **Ch 9:** Part A [core_09.000_system_alignment_certification_evaluation.md](core_09.000_system_alignment_certification_evaluation.md); Part B [core_09.005_system_alignment_certification_record_process.md](core_09.005_system_alignment_certification_record_process.md); Part C [core_09.010_system_alignment_certification_record_recertification.md](core_09.010_system_alignment_certification_record_recertification.md); worked illustrations (systems family) [cs_09.320_system_alignment_certification_illustrations.md](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md)
- **Ch 10:** [core_10.000_institutional_alignment_certification.md](core_10.000_institutional_alignment_certification.md)
- **Ch 11:** [core_11.000_standing_assessment.md](core_11.000_standing_assessment.md)
- **Ch 12:** [core_12.000_standing_integration.md](core_12.000_standing_integration.md)
- **Ch 13:** Part A [core_13.000_misconduct_designation.md](core_13.000_misconduct_designation.md); Part B [core_13.005_misconduct_pattern_applications.md](core_13.005_misconduct_pattern_applications.md)
- **Ch 14:** [core_14.000_forum.md](core_14.000_forum.md)
- **Ch 15:** [core_15.000_governance.md](core_15.000_governance.md)
- **Ch 16:** [core_16.000_non_regression.md](core_16.000_non_regression.md)
- **Ch 17:** [core_17.000_expansion_supremacy.md](core_17.000_expansion_supremacy.md)
- **Ch 18:** [core_18.000_amendment_ratification.md](core_18.000_amendment_ratification.md)
- **Ch 19:** [core_19.000_incorporation.md](core_19.000_incorporation.md)
- **Ch 11–14 vignettes (non-operative):** [core_11.005_application_vignettes.md](core_11.005_application_vignettes.md)
- **Adopted corpus:** [corpus_joint_structure.md](corpus_joint_structure.md) (`corpus_joint_structure/`), [corpus_systems.md](corpus_systems.md) (`corpus_systems/`), [corpus_institutions.md](corpus_institutions.md) (`corpus_institutions/`), [corpus_forum.md](corpus_forum.md) (`corpus_forum/`)

## Open Backlog

### Chapter Seven §4 and CF-5.9 — adoption and translations

The implementation and signoffs are recorded in [TODO_RESOLVED_2026-10-21.md](archive/TODO_RESOLVED_2026-10-21.md) and [TODO_RESOLVED_2026-10-20.md](archive/TODO_RESOLVED_2026-10-20.md).

- [ ] Chapter Seventeen §1 heightened review: fixes were not independently re-reviewed; adoption and the contest period remain open until the announcement. Review records: [Chapter Seven §4](evidence/2026-10-20/heightened_review_record_2026-10-20.md) and [older batches](evidence/2026-10-20/heightened_review_record_older_batches_2026-10-20.md).
- [ ] Sync translations for Chapter Seven §4, CF-5.9, CI-3.6.3 custodian bullets, Chapter Ten §3.7, and the two Chapter Five entries after wording settles; include the Chapter Seven §2 and §3 widgets.

### Audit registry and category report — optional follow-up

Records: `tools/architecture/audit_registry.json`, `tools/audit_report.py`, `make audit-report`; project doc `claude/audit-registry-and-report-implementation.md`. See the fifty-second move in [doc_architecture.md](doc_architecture.md).

- [ ] Add an optional `--changed` mode that runs only categories touching files changed on the branch.

### Chapter Seven locks, time windows, and related edits — announcement follow-ups

Completed implementation details and signoffs are in [TODO_SNAPSHOT_2026-10-21.md](archive/TODO_SNAPSHOT_2026-10-21.md), [TODO_RESOLVED_2026-10-19.md](archive/TODO_RESOLVED_2026-10-19.md), and [TODO_RESOLVED_2026-10-20.md](archive/TODO_RESOLVED_2026-10-20.md). The relevant Test 1 record is [time-window-test-1-self-check](evidence/2026-10-18/time-window-test-1-self-check.md).

- [ ] Complete announcement adoption and contest steps for the Chapter Seventeen §1 heightened reviews; recorded review fixes were not independently re-reviewed.
- [ ] Run `make edition-bump` on release day.
- [ ] Sync translations for the Dissolution Reformation Lock, Chapter Seven §2–§4, Chapter One §16.4, CS-4, time windows and old week-based figures, Article XIV-A / Evidence Preservation wording, Chapter Ten §3 Trace, Article XXVIII-A / CI-14.4.4 declaration wording, Domain-Specific Materiality, the Adoption Document name, and TERM-BODY-01 authority names. Follow the settled-chapter schedule.
- [ ] Ensure the time-window Test 1 self-check is linked from the relevant PR.

### Backup Record Authority (CF-5.7) — announcement follow-ups

Implementation and steward signoff are recorded in [TODO_RESOLVED_2026-10-19.md](archive/TODO_RESOLVED_2026-10-19.md); the heightened review is in [evidence/2026-10-20/heightened_review_record_older_batches_2026-10-20.md](evidence/2026-10-20/heightened_review_record_older_batches_2026-10-20.md).

- [ ] Complete announcement adoption and contest steps after the heightened review; fixes were not independently re-reviewed.
- [ ] Sync translations for the edited passages after wording settles.

### Chapter Ten — open follow-ups

- [ ] Complete announcement adoption and contest steps after the recorded heightened review; see [older-batch review](evidence/2026-10-20/heightened_review_record_older_batches_2026-10-20.md).
- [ ] Sync translations after wording settles.

### Formation check and remediation readiness — open follow-ups

The signoffs and lifted-hold reference are in [TODO_RESOLVED_2026-10-19.md](archive/TODO_RESOLVED_2026-10-19.md); see also [formation_check_and_remediation_readiness](evidence/2026-10-13/formation_check_and_remediation_readiness.md).

- [ ] Sync translations after wording settles.

### Article XI-E gates and Institutional Authority Standing Lock — open follow-ups

- [ ] Complete announcement adoption and contest steps after the recorded heightened review; see [older-batch review](evidence/2026-10-20/heightened_review_record_older_batches_2026-10-20.md).
- [ ] Sync translations after wording settles.

### Interim Hold standard — open follow-ups

- [ ] Complete announcement adoption and contest steps after the recorded heightened review; see [older-batch review](evidence/2026-10-20/heightened_review_record_older_batches_2026-10-20.md).
- [ ] Revisit deferred applications after the first three applications run in practice: stakeholder-weight escrow, and holds on holders of authority over Class A, B, or C systems on grave anti-constitutional allegations.
- [ ] Sync translations after wording settles.

### Process-level granularity — Option B

The completed Option A review and process definitions are in [TODO_RESOLVED_2026-10-13.md](archive/TODO_RESOLVED_2026-10-13.md).

- [ ] Draft the Lane D core proposal for Chapter Nine Part C §8.1 and Chapter Thirteen; Chapter Seventeen §1 heightened review applies. Keep Option B an outlined post-adoption goal unless the steward decides otherwise.
- [ ] Connect the process-ownership draft's floor-touching test and certification terminology to the Option B guardrail and naming decision.

### Process, system, and institution — potential follow-ups

These remain optional planning questions, not decisions. Full notes and the 67-item crosswalk results are in [TODO_SNAPSHOT_2026-10-21.md](archive/TODO_SNAPSHOT_2026-10-21.md).

- [ ] Review the 22 medium- and 3 low-confidence crosswalk tags; extend the crosswalk to Chapter One third-level subsections and the remaining corpus if useful.
- [ ] Decide whether to define Process with a test, create an index or restructure, gather scattered Process principles, and whether a third Preamble question is needed.
- [ ] Continue the process-ownership dispute-rule draft, including steward role names and its six open questions; consider the CI-6 change-record template.
- [ ] Add a grep-based chart-orientation audit and `make` target; confirm the convert-on-next-edit policy.

### Translation follow-ups

- [ ] Update translations for the Article XIII-A / XIII-B split and cites to XIII-B.
- [ ] Update translations for the operative steward-box removal and the old Chapter Nine §14.2, Chapter Ten, and Chapter Thirteen references.
- [ ] Resync the 2026-09-21 Preamble §6/§7 changes and other translation files touched by the English cleanup, once the source is settled.
- [ ] Update translations for Chapter One relocation/numbering, §7 reorder, §9/§10 swap, Chapter One Part A introductions, and check Meaningful Agency and Consent wording against Chapter Six.

### Conceptual overview, lived-experience validation, and evaluation

See the [conceptual overview and corpus alignment review](evidence/2026-09-16/conceptual_overview_corpus_alignment_review.md). These are process-aid tasks, not new constitutional duties.

- [ ] Test severe-designation boundaries against failed good-faith administration, dissident reform, organized capture, mass protest, and investigative reporting.
- [ ] Reconcile or justify the 80-year denominator in digital examples W5/W6 of the [LEQU calibration reference](implementation/LEQU_CALIBRATION_REFERENCE.md); collect independent evaluator disagreement and sensitivity near serious-misconduct thresholds.
- [ ] Test affordable, accessible remedy capacity using the [minimum viable adopter profiles](implementation/adoption/MINIMUM_VIABLE_ADOPTER.md), including actual staffing, cost, delay, and claimant burden.
- [ ] Demonstrate a protected route to replace an institution under capture; test Article XXVI and Chapter Fifteen together.
- [ ] Complete and document the eight ordinary-life and failure exercises in the review's “The world I would endorse” section.
- [ ] Complete the redesigned human operator sitting and independent review under [evaluation/HUMAN_SITTING_PROTOCOL.md](evaluation/HUMAN_SITTING_PROTOCOL.md); file results under `evaluation/results/`.

### Translation resync after English cleanup

- [ ] Resync translated Preamble and other chapters after the pre-release English cleanup is finished; confirm anchors against the settled sources.

### P1 — Regression and evidence

- [ ] Complete first-pass validation of the 35 Humanity/Individual stress-pack rows (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`) and publish procedures, expected outcomes, and run evidence under the restored evidence tree.

## TODO Maintenance and Archives

Authoritative normative state is in the binding corpus files named in [README.md](README.md). `TODO.md`, [project/MEMLOG.md](project/MEMLOG.md), [doc_architecture.md](doc_architecture.md), and implementation worklists are process aids only. Keep this active file limited to editor checks, current open work, and short archive pointers.

## Archives

- **2026-10-23 resolved work:** [archive/TODO_RESOLVED_2026-10-23.md](archive/TODO_RESOLVED_2026-10-23.md)
- **2026-10-21 resolved work:** [archive/TODO_RESOLVED_2026-10-21.md](archive/TODO_RESOLVED_2026-10-21.md)
- **2026-10-21 pre-cleanup snapshot:** [archive/TODO_SNAPSHOT_2026-10-21.md](archive/TODO_SNAPSHOT_2026-10-21.md)
- **2026-10-20 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-20.md](archive/TODO_RESOLVED_2026-10-20.md)
- **2026-10-19 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-19.md](archive/TODO_RESOLVED_2026-10-19.md)
- **2026-10-18 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-18.md](archive/TODO_RESOLVED_2026-10-18.md)
- **2026-10-14 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-14.md](archive/TODO_RESOLVED_2026-10-14.md)
- **2026-10-13 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-13.md](archive/TODO_RESOLVED_2026-10-13.md)
- **2026-10-03 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-03.md](archive/TODO_RESOLVED_2026-10-03.md)
- **2026-10-01 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-01.md](archive/TODO_RESOLVED_2026-10-01.md)
- **2026-09-17 resolved TODO items:** [archive/TODO_RESOLVED_2026-09-17.md](archive/TODO_RESOLVED_2026-09-17.md)
- **Architecture process (canonical):** [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md) — see [README.md](README.md)
- **2026-06-18 Chapter Five closeout:** [archive/TODO_SNAPSHOT_2026-06-18.md](archive/TODO_SNAPSHOT_2026-06-18.md), [archive/MEMLOG_SNAPSHOT_2026-06-18.md](archive/MEMLOG_SNAPSHOT_2026-06-18.md)
- **2026-05-01 root retirement:** [archive/TODO_ROOT_RETIRED_2026-05-01.md](archive/TODO_ROOT_RETIRED_2026-05-01.md), [archive/MEMLOG_ROOT_RETIRED_2026-05-01.md](archive/MEMLOG_ROOT_RETIRED_2026-05-01.md)
- Older snapshots removed 2026-06-17 can be retrieved from Git history.
