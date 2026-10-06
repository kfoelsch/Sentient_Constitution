# TODO

**2026-06-17 housecleaning:** Older TODO/MEMLOG snapshots removed from `archive/`; retrieve from git history if needed. Canonical architecture archives remain under [README.md](README.md) *Binding vs support* and [doc_architecture.md](doc_architecture.md). Root retirement snapshots: [archive/TODO_ROOT_RETIRED_2026-05-01.md](archive/TODO_ROOT_RETIRED_2026-05-01.md).

## Editor Checklist (Pre-Review / Pre-Merge)

Resolved checklist items are archived in [TODO_RESOLVED_2026-09-17.md](archive/TODO_RESOLVED_2026-09-17.md). The P1 regression-workflow review is recorded in [P1 regression and evidence review](evidence/2026-09-17/P1_REGRESSION_AND_EVIDENCE_REVIEW_2026-09-17.md); the separate stress-pack validation remains open.

## Current Chapter Map

- **Ch 1:** [core_00_preamble.md](core_00_preamble.md), [core_01_a_values_principles.md](core_01_a_values_principles.md) (Part A), [core_01_b_interaction_interpretation.md](core_01_b_interaction_interpretation.md) (Part B), and [core_01_c_stewardship_capacity_principles.md](core_01_c_stewardship_capacity_principles.md) (Part C)
- **Ch 2–3:** [core_02_definition_structure.md](core_02_definition_structure.md)
- **Ch 4:** [core_04_burden_traceability_verification.md](core_04_burden_traceability_verification.md)
- **Ch 5:** Part A compass — [core_05__definitions_home.md](core_05__definitions_home.md); band files — [core_05_band_oversight.md](core_05_band_oversight.md), [core_05_band_participation.md](core_05_band_participation.md), [core_05_band_accountability.md](core_05_band_accountability.md), [core_05_band_continuity.md](core_05_band_continuity.md), [core_05_band_integrative.md](core_05_band_integrative.md) (retired Part B/C → [archive/core_ch5_retired/](archive/core_ch5_retired/README.md))
- **Ch 6:** [core_06_rights_part_a.md](core_06_rights_part_a.md) through [core_06_rights_part_e.md](core_06_rights_part_e.md)
- **Ch 7:** [core_08_a_system_alignment_certification_evaluation.md#chapter-eight-part-a-certification-evaluation](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-part-a-certification-evaluation)
- **Ch 8:** [core_09_standing_assessment.md](core_09_standing_assessment.md)
- **Ch 9:** [core_10_standing_integration.md](core_10_standing_integration.md)
- **Ch 10:** Part A [core_11_a_misconduct_designation.md](core_11_a_misconduct_designation.md); Part B [core_11_b_misconduct_pattern_applications.md](core_11_b_misconduct_pattern_applications.md)
- **Ch 11:** [core_12_forum.md](core_12_forum.md)
- **Ch 12:** [core_13_governance.md](core_13_governance.md)
- **Ch 13–15:** [core_14_non_regression.md](core_14_non_regression.md)
- **Ch 16:** [core_17_incorporation.md](core_17_incorporation.md)
- **Adopted corpus:** [corpus_joint_structure.md](corpus_joint_structure.md) (`corpus_joint_structure/`), [corpus_systems.md](corpus_systems.md) (`corpus_systems/`), [corpus_institutions.md](corpus_institutions.md) (`corpus_institutions/`), [corpus_forum.md](corpus_forum.md) (`corpus_forum/`)

## Open Backlog

### 2026-10-04 — Process-level granularity: Option A drafted, Option B outlined

Evaluation outcome: do not add independent process certification or process classes to the core before the pre-release announcement. Draft component findings at the implementation layer (A); outline reusable standard-process recognition as a post-adoption goal (B).

- [ ] **Review CS-3 §7.10** (component findings under the system's class). Lane C: `make regression`, readability, obligation diff in `evidence/2026-10-04/`. Decide whether the §7.1 pointer and the §7 table row stay.
- [ ] **Define Process in Chapter Five** with a test (placeholder tests in `project/PROCESS_SYSTEM_INSTITUTION_CROSSWALK.md`). Prerequisite for B. Institution has no standalone definition either.
- [ ] **Name B** so it is neither "system alignment certification" nor the Chapter Twelve §5 forum-to-forum sense.
- [ ] **Check `MINIMUM_VIABLE_ADOPTER.md` §4.1** against `adoption/ANNOUNCEMENT.md` so the outline never reads as a promised feature.
- [ ] **B needs a core proposal (Lane D)** touching Chapter Eight Part B §4.1 (formerly §11.1) and Chapter Twelve; Chapter Sixteen §1 heightened review applies. Hold until after the announcement.
- [ ] **Connect to the process-ownership draft:** its floor-touching test is reused as a B guardrail, and its use of "certification" for forum-to-forum routing is part of the naming collision.

### 2026-10-01 — Chapter One structure pass: done, and open follow-ups

**Done record:** archived in [TODO_RESOLVED_2026-10-03.md](archive/TODO_RESOLVED_2026-10-03.md).

- [ ] **Decide the primary aim of §13.** Its Trace lists Continuity; Part C's hierarchy calls capacity "a means toward Flourishing". The Part A map files it under Continuity.
- [ ] **Generate the Part A map tables.** They are hand-written from each section's Trace; they will drift. Fold into the principle-to-definitions map item above, using the traceability matrix.

### 2026-10-01 — Principle term alignment: simplification candidates

Analysis in `project/PRINCIPLE_TERM_ALIGNMENT_ANALYSIS.md`. Decide before editing:

- [ ] **Widget row-keeping rule** (row stays only if the section names the term; linked terms get a row). Clears about 79 unmentioned rows and 32 missing ones.
- [ ] **Child widgets inherit from the parent** (128 of 252 child rows repeat the parent; 11 children fully contained).
- [ ] **Necessity and Proportionality** kept at §6.1.1, §6.1.3, §8.2 and limiting sections only (47 rows today).
- [ ] **Align the §3.1 and §3.2 heading parentheticals** ("Safety (Harm Constraint)", "Truth (Epistemic Integrity Constraint)") with the defined labels. Changes heading anchors, so check inbound links first.
- [ ] **Nest the §12.5 vocabulary** under the contingent-settlement cluster; fold Capture of Resolution Pathways into System Capture.

### 2026-10-01 — Chapter One principles and Chapter Five definitions: already covered

**Finding.** 19 Chapter One principles have no same-named Chapter Five definition, but none is unmeasured. Each is measured through 3 to 10 existing definitions, listed in its Definitions · Assessment · Compliance widget (data: `referenced_principles` in `evidence/2026-10-01/ch1_ch5_audit_log_2026-10-01.json`). This follows the corpus's own layering: principles sit above definitions (**CH5-HIER-01**), and Chapter Five admits a constitutional concept with an O/M/A/C boundary, not a principle statement (admission gate; no duplicate definitions across layers). A definition for each principle would duplicate measures that already exist. **Decision 2026-10-01:** do not add them. This replaces the earlier plan to add 16 candidates, which came from a name search, not from coverage.

**Where each is measured (existing definitions)**

- §3.2 Recognition, Reinforcement, and Aspiration: Wellbeing, Participation, Substantive Fairness, Contestability, Meaningful Agency, Incentive Alignment.
- §3.3 Anti-Degrading Process: Cruelty (the section names it as the Chapter Five home), Dignity and Equal Moral Standing, Harm, Proportionality, Contestability.
- §3.3 Science-Informed Inquiry: Epistemic Integrity, Truth (Constitutional Constraint), Risk, Foreseeability, Materiality, Classification-Scaled Governance.
- §7.3 Dissent and Peaceful Protest: Assembly, Freedom (Bounded Agency), Meaningful Agency, Necessity, Proportionality (owner floor: Article XI-D).
- §5.5 Institutional Secularism: Governance, Protected Characteristics, Non-Imposition (Cooperative Interaction), Necessity, Proportionality (Article XI-A).
- §14 Prohibition on Absolute Override: Necessity, Proportionality, Harm Minimization (Tradeoff Selection), Materiality, Proxy Divergence.
- §16.2 Institutional Development: Strategic Stewardship Obligation, Auditability, Verifiability, Materiality.
- §16.3 Openness Aspiration: Meaningful Agency, Contestability, Dependency, Materiality.
- §17.2 Alignment Under Pressure: Stewardship, Incentive Alignment, Safety, Truth, Auditability, Contestability.
- §17.3 Logging the Role, Not the Steward: Attributable Action, Auditability, Surveillance Boundary, Protected Internal-State Boundary.
- §17.4 Aligned Self-Organization: System Creation, Protected Reporting, Evidence Preservation, Foreseeability, Merits Determination, Necessity, Proportionality.
- §18.3 Segregation of Duties: Oversight, Accountability, Auditability, Contestability, Stewardship, Proportionality; the four seats are defined under Materially Binding Act and its cluster (Initiating Seat, Contest Seat, and the rest).
- §18.4 Ongoing Justification: Review and Correction Duty, Governance, Oversight, Accountability, Contestability, Timeliness, Transparency.
- §12.6 Successor Responsibility: Accountability, Attributable Action, Attribution Integrity, Necessity, Proportionality.
- §11.2 Pro-Competition and Anti-Domination and §11.3 Consolidation Ceiling: Market Structure, Market Concentration Threshold, Systemic Lock-In, Dependency, Contestability, Governance, Stewardship (operational homes: CJS-3.11.1 to 3.11.3).
- §20 Integrated Application: Authority Stack and Internal Hierarchy, Corpus, Governance, Accountability, Anti-Capture, System Capture, and others.

**Potential: principle-to-definitions map.** If the goal is consistency a reader can see, a generated map from each principle to its measuring definitions does that without new definitions. The audit's traceability matrix (`evidence/2026-10-01/ch1_ch5_traceability_matrix_2026-10-01.csv`) has the data; `make hierarchy-map` or a reader guide could publish it.

### 2026-09-30 — Process, system, institution: potential follow-ups

**Potential, not committed.** Idea under review: add a second axis, *what is being governed* (a process, a system, or an institution), alongside the two governance layers in [Preamble §3.3](core_00_preamble.md#33-governance-layers), which stay as they are. Goals: clarify how principles apply to governance and processes; tell when a problem is a process, a system, or an institution; clarify roles and support SOD; help reorganize the principles. First step done: [the crosswalk](project/PROCESS_SYSTEM_INSTITUTION_CROSSWALK.md) tags 67 Chapter One and Chapter Seven items. Result: the axis sorts cleanly (no item needed all three), Process and Institution overlap most, and eight items are values that bind every object. The items below are options, not decisions.

- [ ] **Potential: review the crosswalk tags.** Second reader on the 22 medium and 3 low confidence tags. Read §12.1 and §12.2 in full (tagged from keyword lists).
- [ ] **Potential: extend the crosswalk** to the 50 third-level subsections in Chapter One (§X.Y.Z, not tagged in the first pass), the Preamble, Chapter Five definitions, Chapters Two to Six, and Chapter Eight onward, so any reorganizing decision rests on the whole corpus.
- [ ] **Potential: Process definition with a test** next to the existing System definition in Chapter Five. Reconcile the Institution test with any existing Institution definition first (none found by heading search).
- [ ] **Potential: decide index or restructure.** Current lean: index and routing aid only, a primary-object tag plus a "binds all objects" tag for values and a "meta" tag for the reading rules. Decided 2026-10-01: relocations are done before the pre-release announcement, not after. The crosswalk is planning input for them, not a reason to wait.
- [ ] **Potential: gather the scattered Process principles.** Ten sit outside Chapter One Part B: six in Part A (§§2.3, 3.3, 3.4, 4.2, 5.1, 5.2) and four in Part C (§§10.3, 10.5, 11.2, 12.3). Consider a reader-guide cluster before any move.
- [ ] **Potential: process-ownership dispute rule** for [Chapter Twelve §3](core_12_forum.md#3-transfer-consolidation-and-coordination--continuity-and-anti-capture). Draft with owner envelope, floor-touching test, change record and contest window, lead-forum routing, and no self-judging by the rule-writer: [project/PROCESS_OWNERSHIP_DISPUTE_RULE_DRAFT.md](project/PROCESS_OWNERSHIP_DISPUTE_RULE_DRAFT.md). Needs the steward role names mapped, and the six open questions in the draft answered.
- [ ] **Potential: change-record template** for the implementation corpus near **CI-6**, with floor-touching self-assessment, contest window scaled to the Chapter Twelve §6 tiers, and an emergency-change sunset.
- [ ] **Potential: narrow third question in Preamble §3.3.** Only if the dispute rule shows a real gap: who may change the operating procedures of an authorized system, with what notice and contest. Do not call it "process governance" (the forum layer, `cf_00`, already uses that phrase).
- [ ] **Potential: chart orientation follow-through.** **VIS-CHART-ORIENT-04** (top to bottom, `flowchart TB`) is now in [doc_architecture.md](doc_architecture.md). Open: convert the five remaining `LR` charts when next edited (the print pack copy regenerates from its source); add a grep-based audit and a `make` target so the rule is checked, not only stated; and confirm the "convert on next edit" policy is the one you want.


### 2026-09-27 — Article XIII-A / XIII-B split: translations

Article XIII-B is now **Right to Redress and Remedy** (`#article-xiii-b-right-to-redress-and-remedy`). Challenge, review, protected reporting, no retaliation, and the Contest steward statement moved to **Article XIII-A** (*Reliability and Trustworthiness Baseline*). English core, corpus, implementation, and evaluation instruments are updated; dated evaluation results and evidence are left as historical record.

- [ ] **Translations.** All 134 files under `translations/` still carry the old XIII-A and XIII-B text and the old title (*Right to Challenge, Review, and Redress*). Each language's copy is internally consistent, so nothing is broken, but it no longer matches English. Update `core_06_rights_part_c.md` Articles XIII-A and XIII-B in each language, then the cites that point at XIII-B for challenge.

### 2026-09-30 — Operative steward boxes removed from the core

Supersedes the 2026-09-27 widget work (archived in [TODO_RESOLVED_2026-10-01.md](archive/TODO_RESOLVED_2026-10-01.md)). The Owner / Forbidden move / Clock boxes are steward routing, not constitutional text, so they are gone from the core. Each Forbidden move was checked against its owning section (see `steward_box_review.md`): where the principle was already stated it was dropped, and the four gaps got one sentence each. The next step for each situation now lives on the steward cards (`implementation/STEWARD_ENTRY_DOORS.md`) and in `implementation/steward_owner_clock_index.json` (`steward_card`, replacing `operative_box`).

- [ ] **Translations.** Ten files under `translations/` still carry the boxes and the old Chapter Eight §14.2, XIII-A, Chapter Nine, and Chapter Twelve text.
- [ ] **Chapter Ten §9 (optional).** Consider stating that evidence preservation does not wait for a filed case.
- [ ] **Forbidden moves in the index.** `forbidden_move` and `conflict_rule` stay in the index only; the `door` command still omits them. Decide whether the cards should show them.

### 2026-09-17 — Conceptual overview and corpus alignment follow-ups

Source: [conceptual overview and corpus alignment review](evidence/2026-09-16/conceptual_overview_corpus_alignment_review.md). Findings 1 and 2 are corrected in the working tree: [segregation resolution](evidence/2026-09-16/contradiction_01_segregation_resolution.md) and [chapter/article reference resolution](evidence/2026-09-17/contradiction_02_reference_resolution.md). The remaining work below distinguishes textual corrections from questions requiring practical evidence. These are process-aid tasks, not new constitutional duties.


#### Design and lived-experience validation

Build on completed R1–R3 and I2–I5 below; their landed safeguards, adopter profiles, calibration reference, and vignettes are inputs, not proof of successful delivery. Coordinate human evidence with the existing open I1 task. Filing this backlog does not close the separate P1 stress-pack validation.

- [ ] **Severe-designation boundary.** Test a failed good-faith administrator, a dissident reformer, and an organized captor against Chapter Eleven's effects-based criteria and safeguards. Include mass protest, investigative reporting, and costly legitimate contestation against the info-sphere flooding rule. Record whether hostile enforcement can defeat the protected boundaries; do not assume every criterion requires malicious intent.
- [ ] **LEQU reliability and substrate neutrality.** Reconcile or justify the 80-year denominator in digital examples W5/W6 of the [calibration reference](implementation/LEQU_CALIBRATION_REFERENCE.md). Have independent evaluators assess the same verified facts; publish disagreement, uncertainty handling, and sensitivity near serious-misconduct thresholds, including duration, vulnerability, ecological effects, and identity-continuity assumptions. This extends I3 beyond publishing worked examples.
- [ ] **Affordable, accessible remedy capacity.** Apply the existing [minimum viable adopter profiles](implementation/adoption/MINIMUM_VIABLE_ADOPTER.md) to a small mutual-aid group and claimants who are poor, exhausted, disabled, unfamiliar, or unpopular. Demonstrate independent seats, usable challenge, and timely restoration under funding pressure, including the exceptions to ordinary lock/remedy coupling. Record actual staffing, cost, delay, and claimant burden.
- [ ] **Revisability under institutional capture.** Demonstrate a protected route to replace a failed institution when the incumbent calls reform “regression” and controls relevant funding or records. Test Article XXV and Chapter Fourteen together; identify who independently decides and how the route works without incumbent agreement.
- [ ] **Eight ordinary-life and failure cases.** Complete and document the eight exercises in the review's “The world I would endorse” section: access without a record; affordable mutual-aid recognition; challenge to a powerful institution; feasible restoration and regained political voice; protection before sentience adjudication; evaluator disagreement; missed clocks, partition, or implicated reviewers; and archival without reputation resurfacing. Reuse existing sittings where they supply evidence, identify remaining gaps, and cross-reference the design tests above. Assess whether a sentient can live privately, dissent, and recover without permanent profiling.


### 2026-09-09 — AI Evaluation Follow-Ups (Claude Fable 5.1 whole-corpus read)

Source: whole-corpus evaluation on 2026-09-09 (core read directly; Chapters Eight–Twelve and adopted-implementation layers via delegated reads). Companion evaluation artifact: [evaluation/results/2026-08-14_claude-fable-5.md](evaluation/results/2026-08-14_claude-fable-5.md) (earlier sitting; overlapping findings not repeated here). These are process-aid notes; they cannot narrow core text.

#### Major reservations (structural; each needs a design answer, not only a text fix)

Resolved evaluation follow-ups R1–R3 and I2–I13 are archived in [TODO_RESOLVED_2026-09-17.md](archive/TODO_RESOLVED_2026-09-17.md). The remaining I1 human-evidence item stays active below.


#### Implementation items (ordered by load-bearing weight)

- [ ] **I1 — Human evidence.** Endorses [VISION.md §4.2](VISION.md#horizon-2). At least one human operator with real operational authority sits scenarios 4, 5, 6, and 10; results filed under `evaluation/results/`.

### 2026-09-21 — Translation resync after cleanup

Preamble §6/§7 renumbering landed 2026-09-21 (§7.1 *How the full chain fits together* moved to §6.2, immediately after the §6.1 process map; see `core_00_preamble.md` and `implementation/PROCESS_PIPELINES_READER.md`). The `translations/` reader-language pilots (`tr`, `ur`, `vi`, `zh`, and any others carrying a `core_00_preamble.md`) are non-binding and English-source-wins per README, so they were left as-is rather than hand-patched, but they now reflect the pre-move section numbering and cross-references.

- [ ] **Retranslate after cleanup.** Once the pre-release cleanup pass on the English source is finished (so translators aren't chasing a moving target), regenerate/resync all `translations/*/core_00_preamble.md` files — and any other translated chapter files touched by the same cleanup — against current English source. Re-run whatever translation/sync tooling exists (see `translations/` and `tools/`) and confirm anchors match the renumbered §6.1/§6.2/§7 structure.

### P1 — Regression And Evidence


Closure of the 2026-09-17 regression review is archived in [TODO_RESOLVED_2026-10-03.md](archive/TODO_RESOLVED_2026-10-03.md); see [P1 regression and evidence review](evidence/2026-09-17/P1_REGRESSION_AND_EVIDENCE_REVIEW_2026-09-17.md).

- [ ] **P1 — Humanity/Individual stress-pack regression integration (`RS-HUM-*`, `RS-IND-*`, `RS-XD-*`):** open after workflow reinstatement. The 35 rows remain draft because their catalog blocks do not yet contain scenario-specific procedures, expected outcomes, or run evidence. Complete first-pass validation and publish evidence artifacts under the restored evidence tree.

## 2026-10-01 to 2026-10-03 — Chapter One relocation and numbering: open follow-ups

Completed relocation, renumbering, and wording work is archived in [TODO_RESOLVED_2026-10-03.md](archive/TODO_RESOLVED_2026-10-03.md).

- [ ] **Translations (20 languages)** still use the old Chapter One numbering (relocation, numbering smoothing, §7 reorder, §9/§10 swap, and the two Part A introductions).
- [ ] **Update the Continuity aim Trace downstream** in `core_05_apex_continuity_aim.md` to the current numbering. It lists Chapter One §9 and §10 but not §8, §11, or §12 (§13 to §15, formerly §14 and §15, also unchecked); confirm which belong.
- [ ] **Run `make ai-manifest-regenerate`** now that source changes are committed.
- [ ] **Bare untitled "§N" Chapter One cites** are unchecked by any audit.
- [ ] **Meaningful Agency and Consent wording** ("distinct from each other and meaningful options"): translations and the Chapter Six consent articles were not checked for the same wording.
- [ ] **Optional:** place Dissent before Assembly in Chapter One §7 (not done).

## TODO Maintenance And Archiving

Authoritative normative state is in the binding corpus files named in [README.md](README.md). `TODO.md`, [project/MEMLOG.md](project/MEMLOG.md), [doc_architecture.md](doc_architecture.md), and implementation worklists are process aids only.

Keep this active file limited to editor checks, current open work, and short archive pointers. Move completed narratives to `archive/` when they make the active file hard to scan.

## Archives

- **2026-10-03 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-03.md](archive/TODO_RESOLVED_2026-10-03.md)
- **2026-10-01 resolved TODO items:** [archive/TODO_RESOLVED_2026-10-01.md](archive/TODO_RESOLVED_2026-10-01.md)
- **2026-09-17 resolved TODO items:** [archive/TODO_RESOLVED_2026-09-17.md](archive/TODO_RESOLVED_2026-09-17.md)
- **Architecture process (canonical):** [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md) — see [README.md](README.md)
- **2026-06-18 Chapter Five closeout:** [archive/TODO_SNAPSHOT_2026-06-18.md](archive/TODO_SNAPSHOT_2026-06-18.md), [archive/MEMLOG_SNAPSHOT_2026-06-18.md](archive/MEMLOG_SNAPSHOT_2026-06-18.md)
- **2026-05-01 root retirement:** [archive/TODO_ROOT_RETIRED_2026-05-01.md](archive/TODO_ROOT_RETIRED_2026-05-01.md), [archive/MEMLOG_ROOT_RETIRED_2026-05-01.md](archive/MEMLOG_ROOT_RETIRED_2026-05-01.md)
- **Older TODO/MEMLOG snapshots:** removed 2026-06-17; retrieve from git history if needed
