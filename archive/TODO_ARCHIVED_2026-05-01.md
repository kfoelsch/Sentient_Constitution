# TODO

**2026-05-01:** Full active backlog text before this slim pass: [archive/TODO_ARCHIVED_2026-05-01.md](TODO_ARCHIVED_2026-05-01.md). Earlier: [archive/TODO_ARCHIVED_2026-04-30.md](TODO_ARCHIVED_2026-04-30.md), [archive/TODO_SNAPSHOT_2026-04-30.md](TODO_SNAPSHOT_2026-04-30.md), [archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md](TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md).

## Editor Checklist (Pre-Review / Pre-Merge)

- [x] Filename convention check: use underscore-style canonical names, no spaces. Canonical chapter and corpus files are listed in [README.md](README.md).
- [x] Corpus edits happen in canonical Markdown files only; no parallel `.txt` layer.
- [x] Reference integrity check: update prose, links, and script references in the same change when filenames move.
- [x] Regression suite check: update and run `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` for any material constitutional change. **Deferred in recent continuations:** the scenarios file is present, but regression validation and evidence publication are out of scope unless reinstatement is requested.
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

### P1 — Chapter Five definition-location stabilization

Deterministic routing is now documented in [doc_architecture.md](doc_architecture.md) and enforced by `tools/ch5_definition_location_audit.py`: Chapter Five `Cluster members` lists are authoritative; Part B-owned member lists route canonical O/E/C homes to **§2**; Part C-owned member lists route canonical O/E/C homes to **§3**; non-cluster full O/E/C definitions default to **§1**. Continue from the script output, not hand classification.

**2026-05-01 implementation note:** `make ch5-definition-location-audit`, `make ch5-cross-file-link-audit`, `make ch5-structure-audit`, `make ch5-entry-format-audit`, `make ch5-cluster-order-audit`, and `make ch5-dec-widget-audit` pass after the parser / expectation update and the Chapter Five separator cleanup. `make regression` remains intentionally skipped for this pass.

- [ ] **Part 1a — Dependent-definition inventory:** run `python3 tools/ch5_definition_location_audit.py --root . --list-dependent` and use the emitted table as the relocation source of truth.
- [ ] **Part 1b — Dependent-definition audit:** run `python3 tools/ch5_definition_location_audit.py --root . --audit`; resolve all cluster-member findings, including missing expected homes, wrong-section homes, and duplicate same-title O/E/C definitions.
- [ ] **Part 1c — Dependent-definition relocation:** move mislocated cluster-member O/E/C blocks beside their cluster owners; preserve canonical anchors at the new home; replace noncanonical duplicates with ordinary links inside real definitions; leave zero locator stubs and zero shells.
- [ ] **Part 2a — Independent-definition inventory:** run `python3 tools/ch5_definition_location_audit.py --root . --list-independent` after dependent relocations to identify remaining full O/E/C definitions that are not cluster members.
- [ ] **Part 2b — Independent-definition audit:** ensure every non-cluster full O/E/C definition has its only canonical home in **§1** and no duplicate full O/E/C title remains elsewhere.
- [ ] **Part 2c — Independent-definition relocation:** move remaining non-cluster definitions to **§1**, update the Chapter Five alphabetical directory and affected links, and keep related-definition references as links within existing definitions rather than shells.
- [ ] **Post-relocation cleanup:** rerun `make ch5-definition-location-audit`, `make ch5-cross-file-link-audit`, `make ch5-structure-audit`, `make ch5-entry-format-audit`, `make ch5-cluster-order-audit`, `make ch5-dec-widget-audit`, and then `make regression`.
- [x] **Known adjacent blockers from latest regression:** fixed the CommonMark horizontal-rule spacing failure in `core_05-05_definitions_a_independent.md`; added missing trace separators for `Redress and Remediation` and Part C `Good Faith`; refreshed `tools/ch5_cluster_order_audit.py` expectations for current Chapter Five headings.

### Deferred — Chapter Five cluster ownership (tie-break backlog)

Single canonical cluster homes for definitions that currently admit multiple semi-independent or dependent contexts without an explicit precedence rule. Resolve by editorial tie-break or restructuring; until then, evaluators apply intersecting clusters only as materially implicated read-with routing.

- [ ] **Environmental Preconditions** — reconcile [§3.6 / bodily-maintenance survival floor](core_05-05_definitions_b_semi_independent.md#safe-conditions-tenure-security-and-environmental-preconditions-cluster), [semi-independent ecological footprint cluster](core_05-05_definitions_b_semi_independent.md#ecological-integrity-footprint-and-sustainability-cluster), and Part C [§3.31 resilience / environmental preconditions routing](core_05-05_definitions_c_dependent_clusters.md#resilience-safety-reversibility-self-healing-and-systemic-harm-cluster).
- [ ] **Adjudication and Dispute Resolution** — reconcile [§3.3 accountability / adjudication cluster](core_05-05_definitions_b_semi_independent.md#accountability-contestability-and-collective-accountability-failure-cluster) with [§3.30 redress / restorative / refuge cluster](core_05-05_definitions_b_semi_independent.md#adjudication-redress-restorative-review-correction-and-refuge-cluster) where both traces apply.
- [ ] **Oversight** — reconcile governance-architecture oversight routing with [§3.22 materiality / classification / oversight cluster](core_05-05_definitions_b_semi_independent.md#materiality-classification-oversight-and-capability-cluster) (*dual cluster membership* traces).
- [ ] **Family vs derivation** — align [§3.17 family cluster](core_05-05_definitions_b_semi_independent.md#family-care-reproductive-autonomy-non-separation-parent-system-and-instantiation-cluster) vs [§3.18 derivation cluster](core_05-05_definitions_c_dependent_clusters.md#derived-developing-sentients-instantiation-and-care-authority-cluster) primacy where cluster-component traces both cite.
- [ ] **Productive Capacity** — reconcile Part C [§3.26 proportionality / burden / productive-capacity cluster](core_05-05_definitions_c_dependent_clusters.md#proportionality-necessity-feasibility-burden-and-efficiency-cluster) with Part C [§3.13 creative-work / anti-displacement cluster](core_05-05_definitions_c_dependent_clusters.md#creative-work-training-data-attribution-compensation-and-anti-displacement-cluster) for `#productive-capacity-partc` dual cluster-component traces.
- [ ] **Incentive Alignment** — untangle nested read-with vs directory duplicates ([`#incentive-alignment`](core_05-05_definitions_b_semi_independent.md#incentive-alignment) vs [Governance Architecture … concentration cluster](core_05-05_definitions_b_semi_independent.md#governance-architecture-oversight-decentralization-and-concentration-cluster) routing).

### P3 — Holistic Redundancy Sweep

- [x] **User acceptance gate (waived for GitHub publish prep, 2026-04-30):** The grep-per-theme companion dedup sweep remains valuable post-release editorial work; it is **not** blocking the public GitHub corpus cut for edition **`SC-Corpus-2026.04.32`**. Re-open by unchecking this item when you resume theme greps across the four companion files.

  Continuation narrative (addenda 9–10, suggested acceptance checks, and pointers) lives in [archive/TODO_ARCHIVED_2026-05-01.md](TODO_ARCHIVED_2026-05-01.md) and [archive/TODO_ARCHIVED_2026-04-30.md](TODO_ARCHIVED_2026-04-30.md).

### Deferred — P1 Regression and Evidence

*Out of active continuation scope unless regression reinstatement is requested.*

- [ ] **P1 — Validate regression scenarios and evidence workflow:** reconcile the present `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` file with the `evidence/<YYYY-MM-DD>/` workflow so matrix integrity, snapshot validation, and dated artifact recording resume as an active process.

  **Acceptance checks:** `make scenario-audit` is intentionally run as a reinstatement step; `.cursor/rules/testing.mdc` suspension language is retired or reconciled; TODO/editor checklist deferral notes are removed; queued observations are landed as `RS-*` rows where appropriate; dated evidence artifacts are recorded for the reinstatement run.

- [ ] **P1 — Humanity/Individual stress-pack regression integration (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`):** blocked on regression-scenarios reinstatement. Complete first-pass validation and publish evidence artifacts under the restored evidence tree.

## TODO Maintenance and Archiving

Authoritative normative state is in the binding corpus files named in [README.md](../README.md). This file, the paired [session log](MEMLOG_ARCHIVED_2026-05-01.md), [doc_architecture.md](../doc_architecture.md), and [architecture worklist](ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-01.md) are process aids only (2026-05-01 archive cut).

Keep this active file limited to:

- editor checks that should remain visible before each review;
- current open work;
- short archive pointers for completed work.

Move completed narratives to `archive/` when they make the active file hard to scan. Archived TODO text is history only; if it disagrees with the current corpus, the corpus wins.

## Standard Procedure

For future substantive cleanup passes:

1. Commit corpus/source changes first, excluding generated noise such as `.DS_Store`.
2. Then snapshot active meta files (task list, session log, architecture worklist) into `archive/` with dated names.
3. When using root-level meta files again, trim them back to current open work, archive pointers, and the minimum context needed for the next session.
4. Keep regression/evidence artifacts separate unless regression reinstatement or validation is explicitly in scope.

## Archives

- **2026-05-01 (superseded mid-day snapshot):** [TODO_ARCHIVED_2026-05-01_prior.md](TODO_ARCHIVED_2026-05-01_prior.md)
- **2026-04-30 full archive (pre-slim):** [archive/TODO_ARCHIVED_2026-04-30.md](TODO_ARCHIVED_2026-04-30.md)
- **2026-04-30 post-commit active snapshot:** [archive/TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md](TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md)
- **2026-04-30 active cleanup snapshot:** [archive/TODO_SNAPSHOT_2026-04-30.md](TODO_SNAPSHOT_2026-04-30.md)
- **2026-04-29 snapshot:** [archive/TODO_SNAPSHOT_2026-04-29.md](TODO_SNAPSHOT_2026-04-29.md)
- **2026-04-26 full archive and snapshot:** [archive/TODO_ARCHIVED_2026-04-26.md](TODO_ARCHIVED_2026-04-26.md), [archive/TODO_SNAPSHOT_2026-04-26.md](TODO_SNAPSHOT_2026-04-26.md)
- **Completed-work cuts:** [archive/TODO_COMPLETED_2026-04-17.md](TODO_COMPLETED_2026-04-17.md), [archive/TODO_COMPLETED_2026-04-16.md](TODO_COMPLETED_2026-04-16.md), [archive/TODO_COMPLETED_2026-Q2.md](TODO_COMPLETED_2026-Q2.md), [archive/TODO_COMPLETED_SC-Corpus-2026.04.md](TODO_COMPLETED_SC-Corpus-2026.04.md)
- **Structural sync and older P3 sub-items:** [archive/TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md](TODO_ARCHIVED_STRUCTURAL_AND_GOVERNANCE_2026-04-08.md)
