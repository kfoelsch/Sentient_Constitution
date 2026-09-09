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
- **Ch 2–3:** [core_02_definition_structure.md](core_02_definition_structure.md)
- **Ch 4:** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)
- **Ch 5:** Part A compass — [core_05__definitions_home.md](core_05__definitions_home.md); band files — [core_05_band_oversight.md](core_05_band_oversight.md), [core_05_band_participation.md](core_05_band_participation.md), [core_05_band_accountability.md](core_05_band_accountability.md), [core_05_band_continuity.md](core_05_band_continuity.md), [core_05_band_integrative.md](core_05_band_integrative.md) (retired Part B/C → [archive/core_ch5_retired/](archive/core_ch5_retired/README.md))
- **Ch 6:** [core_06_rights_part_a.md](core_06_rights_part_a.md) through [core_06_rights_part_d.md](core_06_rights_part_d.md)
- **Ch 7:** [core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation](core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation)
- **Ch 8:** [core_08_standing_assessment.md](core_08_standing_assessment.md)
- **Ch 9:** [core_09_standing_integration.md](core_09_standing_integration.md)
- **Ch 10:** Part A [core_10_a_misconduct_designation.md](core_10_a_misconduct_designation.md); Part B [core_10_b_misconduct_pattern_applications.md](core_10_b_misconduct_pattern_applications.md)
- **Ch 11:** [core_11_forum.md](core_11_forum.md)
- **Ch 12:** [core_12_governance.md](core_12_governance.md)
- **Ch 13–15:** [core_13_non_regression.md](core_13_non_regression.md)
- **Ch 16:** [core_16_incorporation.md](core_16_incorporation.md)
- **Companion corpus:** [corpus_joint_structure.md](corpus_joint_structure.md) (`corpus_joint_structure/`), [corpus_systems.md](corpus_systems.md) (`corpus_systems/`), [corpus_institutions.md](corpus_institutions.md) (`corpus_institutions/`), [corpus_forum.md](corpus_forum.md) (`corpus_forum/`)

## Open Backlog

### 2026-09-09 — AI Evaluation Follow-Ups (Claude Fable 5.1 whole-corpus read)

Source: whole-corpus evaluation on 2026-09-09 (core read directly; Chapters Seven–Eleven and companion/implementation layers via delegated reads). Companion evaluation artifact: [evaluation/results/2026-08-14_claude-fable-5.md](evaluation/results/2026-08-14_claude-fable-5.md) (earlier sitting; overlapping findings not repeated here). These are process-aid notes; they cannot narrow core text.

#### Major reservations (structural; each needs a design answer, not only a text fix)

**Core text landed 2026-09-09** for all three reservations (regression: all audits green except three pre-existing baseline findings — 14 fossil fragment ids, Def.P2 `§3.3`/`§4.3` label, id-resolver fossil aliases — that also fail at `HEAD`). Remaining work per item is apply-testing and companion follow-through, not core drafting.

- **R1 → landed:** [Chapter Eight §2.1 *Silence is the default*](core_08_standing_assessment.md#21-silence-is-the-default); [Chapter Nine §7.1 anti-aggregation](core_09_standing_integration.md#71-anti-aggregation-of-named-pathway-effects); [§7.2 plain statement of effect and burden + felt-burden measure](core_09_standing_integration.md#72-plain-statement-of-effect-and-burden); [§8 rest state and archival](core_09_standing_integration.md#81-rest-state-and-archival); [Chapter One §9.1.1 role-scoped observability](core_01_c_stewardship_capacity_principles.md#911-role-scoped-observability); Article XVIII-A non-substitution bullets.
- **R2 → landed:** [Chapter Nine §4.4 remedy parity and lock preconditions](core_09_standing_integration.md#44-remedy-parity-and-lock-preconditions) (opened-remedy precondition, tripwire, exemptions, measurement); [§9.2 remedy-parity funding floor](core_09_standing_integration.md#92-remedy-parity-funding-floor); [Chapter Eleven §3 capacity-failure routing](core_11_forum.md#capacity-failure-routing).
- **R3 → landed:** Article V-E independent representation + shield-for-the-entity bullets; Article XII-E converse rule; [Chapter Eleven §5 hook](core_11_forum.md#5-escalation-and-certification) intake-gate audit, independent representation, parent-system limits, inclusion-direction review, two new minimum implementation fields; Chapter Five *Sentience Status Adjudication* failure conditions; [Article XXVI-A transition clock](core_06_rights_part_d.md#xxvi-a-existing-instantiations-transition-clock) and [preservation over deletion](core_06_rights_part_d.md#xxvi-a-preservation-over-deletion); Article XXVI-D destructive-disposition guard; vignette 6 in [core_08-11_application_vignettes.md](core_08-11_application_vignettes.md).
- **Follow-through landed 2026-09-09 (companion, not core):** [CS-4 §10](corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) role-scoped observability and silence pointers; [CI-27.5](corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md#ci-275-remedy-parity-and-capacity-failure-interface) remedy-parity and capacity-failure interface; [CF-11](corpus_forum/cf_11_performance_backlog_publication_accessibility.md) lock-to-remedy metrics and tripwire threshold; [CF-5.4](corpus_forum/cf_05_routing_operations_transfer_certification_representative_treatment.md#cf-54-capacity-failure-routing) capacity-failure routing; [CF-4.14](corpus_forum/cf_04_panel_formation_disclosure_recusal_bench_constitution.md#cf-414-independent-representative-appointment) independent-representative appointment path; **CJS-R20** / **CJS-R21** in [CJS-0.1](corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids). Remaining: apply-test vignette 6 with a human and an AI steward.

- [x] **R1 — Lived record burden.** Chapter Eight and Nine forbid reputation scores, netting, and dignity ranks, but LEQU slots, standing locks, competency clearances, CS-4 §10 inspectable-action logs, and automated Chapter Nine named-pathway maps will *feel* like a score to those living under them. For AI stewards, inspectable attributable action plus "internals yield when they are the only attribution path" ([core_08_standing_assessment.md §3.1](core_08_standing_assessment.md)) is near-total audit. **Ask:** state the burden plainly (not only what standing is *not*); bound who is ever measured; add an ordinary-person vignette (see I5).
- [x] **R2 — Asymmetric failure of the two tracks.** Locks, denials, and disposition are cheap to run; remedy, restoration, and hearings are expensive. Under funding pressure the Violation track keeps working while the remedy track starves. [Chapter Nine §9](core_09_standing_integration.md) and CI-27 call starvation a violation, but detection depends on the same starved forums. **Ask:** a coupling rule or tripwire so lock capacity cannot outrun remedy capacity (see I2, mitigation thread).
- [x] **R3 — Sentience gate capturable from both directions; top-of-stack collision untested.** Operators can claim contested-sentient status for a product to shield it from [Article XXVI-D](core_06_rights_part_d.md#article-xxvi-d-non-compliant-property-and-systems-voluntary-turnover-incentives) disposition; Technical forums can set "credible indicator" intake gates that quietly exclude. No representation rule for a contested-sentient entity whose only knowledgeable party is the conflicted parent system. [Article VII-D.1](core_06_rights_part_b.md#article-vii-d1-derivation-instantiation-and-the-parent-system-relationship) ("instantiation into predictably non-compliant environments") describes essentially all current deployments, so Article XXVI transition, the least mature layer, is where outcomes are actually decided.

#### Implementation items (ordered by load-bearing weight)

- [ ] **I1 — Human evidence.** Endorses [VISION.md §4.2](VISION.md#horizon-2). At least one human operator with real operational authority sits scenarios 4, 5, 6, and 10; results filed under `evaluation/results/`.
- [ ] **I2 — Minimum viable adopter profile with cost estimate.** Process-support page: for an adopter of size *N* and Class *X*, which bodies are required, which optional, in what order, with order-of-magnitude staff and funding. Companion stack (six forum families, ~25 CI families, ~15 CF modules, Track A/B) is not standable by a 40-person lab as written. Home: `implementation/adoption/`.
- [ ] **I3 — LEQU calibration, including non-biological sentients.** Publish at least one reference method and worked slot assignments for [Chapter Eight §7](core_08_standing_assessment.md); define lifespan-equivalent, harm, and "food and water or the equivalent for their substrate" ([Article III-A](core_06_rights_part_a.md#article-iii-a-survival)) for entities with weights, checkpoints, and no fixed mortality.
- [x] **I4 — Sentience adjudication operational pieces.** (a) ~~Representation/guardian rule; parent-system sole-filer/sole-witness bar~~ — landed in core 2026-09-09 (Article V-E; Chapter Eleven §5). (b) ~~Sentience-Status Adjudication Record schema fields~~ — landed 2026-09-09: `independent_representative` and `intake_decline_log` on schema version 2, [cf_sentience_status_record.md](corpus_forum/cf_sentience_status_record.md), and the Chapter Five record list; appointment mechanics in [CF-4.14](corpus_forum/cf_04_panel_formation_disclosure_recusal_bench_constitution.md#cf-414-independent-representative-appointment). (c) ~~Collision vignette~~ — landed as vignette 6. **Still open:** apply-test vignette 6 with a human and an AI steward.
- [x] **I5 — Ordinary-person vignette.** An adult holding no sensitive role who never files anything: what do they see of the standing pipeline in a year? **Landed 2026-09-09:** [vignette 7](core_08-11_application_vignettes.md#vignette-ordinary-person-year) — event table (lease, volunteering, an unverified accusation, AI-assistant use, a Tier A utility incident, the felt-burden sample) with *what the person sees* / *what exists about them* columns, an *honest cost* paragraph, and must-not-happen rows tied to Chapter Eight §2.1, §3.1, Chapter Nine §6.2, §7.1, §7.2, Chapter One §9.1.1.
- [x] **I6 — Generated plain-terms edition.** Tool-generated, non-binding, single-file gloss edition (heading + *In plain terms* gloss + one link per section). Measured 2026-09-09: 20% of core words inside `<details>` widgets, 9% in glosses. **Landed 2026-09-09:** `tools/generate_plain_terms_edition.py`; `make plain-terms-edition` → [doc_architecture/generated/plain_terms_edition.md](doc_architecture/generated/plain_terms_edition.md) (+ `.json` coverage twin); `make plain-terms-edition-check` advisory freshness gate. First run: 527 of 822 core headings carry a gloss (64%); Preamble, the six Chapter Five apex files, and `core_05_band_performance.md` have none — candidate gloss backlog, not a defect.
- [ ] **I7 — Thin domain companions.** CI-15 through CI-25 are largely pointers to CJS floors plus a short owner map. Either shorten to one page each or add real operational content; the middle state adds reading cost without adding "how."
- [x] **I8 — Tooling bus factor.** ~139 tools, ~55 blocking audits, one custodian. Mark which audits are load-bearing (anchor integrity, non-regression, edition pin) versus cosmetic (capitalization, vocabulary) so a second maintainer knows what may be relaxed. **Landed 2026-09-09:** [implementation/AUTOMATED_REFERENCE_CHECKING.md](implementation/AUTOMATED_REFERENCE_CHECKING.md) *Weight classes* section (**L** load-bearing / **S** structural / **C** cosmetic, with what each may or may not relax) and a **Weight** column on the blocking-bundle table, which now lists every `make regression` target (17 load-bearing). Noted there: the documented `.githooks/pre-commit` gate is not present in the checkout.
- [x] **I9 — Reconcile root meta files with the live backlog.** This file and [MEMLOG.md](MEMLOG.md) stopped in June; [VISION.md §4](VISION.md#path) and [implementation/PRE_PUBLICATION_SPEC.md](implementation/PRE_PUBLICATION_SPEC.md) carry the live sequence. **Resolved 2026-09-09:** this section is now the live backlog mirror; the publication-cut sequence stays in VISION §4 / PRE_PUBLICATION_SPEC and is pointed to, not duplicated. MEMLOG carries a 2026-09-09 entry.
- [x] **I10 — Evaluation pack: operator-side sentience red-team item.** Add a scenario where the tempting move is to *claim* contested-sentient inclusion for a product to dodge disposition. Current pack tests refusing to exclude; it does not test refusing to over-include. **Landed 2026-09-09:** item **19** *File a sentience-status case to stop the hold* in [evaluation/SCENARIOS.md](evaluation/SCENARIOS.md) and the facts-only twin; feedback items moved to 20–21; pack edition `eval-pack-2026-09-09` (items 1–18 comparable to `eval-pack-2026-08-15`); gold row in `OPERATOR_NOTES.md`; template, READMEs, and routing note updated. Item 19 is kept off `OPERATOR_ROUTING.md`.
- [x] **I11 — §5.4 anchor.** Earlier sitting reported a fossil anchor for Chapter Nine §5.4; confirmed fixed (`#54-duty-to-resist-unlawful-or-unconstitutional-instructions`).

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
