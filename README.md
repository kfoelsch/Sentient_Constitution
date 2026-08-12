# Constitution Corpus README

Operative constitutional text for the **Sentient Constitution** lives in the numbered `core_*` files, read together as one instrument (**Chapters One through Sixteen**).

## Edition

| | |
|---|---|
| **Corpus edition** | `SC-Corpus-2026.08.09` |
| **Effective date** | 2026-08-09 |
| **Status** | Substantive binding text through **Chapter Sixteen** is **stable for assurance review** under this edition. **SC-Corpus-2026.08.09** reforms the four implementation corpora (**CJS**, **CS**, **CI**, **CF**) onto the core-file anatomy: every subfile now opens with a titled H1, a one-line statement of what it governs, and a plain-language gloss, with content-free routing scaffolding removed and operative prose rewritten to plain language under evidence that obligations were preserved. No constitutional obligation was added, removed, or narrowed. The previous edition, **SC-Corpus-2026.06.18**, reorganized Chapter Five into constitutional **band files** (Oversight, Participation, Accountability, Continuity, Integrative), assigned dependent clusters **Def.O1–Def.I1**, and added the Chapter Five compass in Part A. |

Custody and binding scope: [Chapter Five *Corpus*](core_05_band_integrative.md#corpus) and [Chapter Sixteen](core_16-16_incorporation.md). Bump the edition label only on a deliberate corpus publication cut.

## How to read

1. **Chapter One** — preamble ([`core_00_preamble.md`](core_00_preamble.md)); Values Principles, Part A ([`core_01_a_values_principles.md`](core_01_a_values_principles.md)); Interaction and Interpretation, Part B ([`core_01_b_interaction_interpretation.md`](core_01_b_interaction_interpretation.md)); Stewardship and Governance, Part C ([`core_01_c_stewardship_capacity_principles.md`](core_01_c_stewardship_capacity_principles.md)).
2. **Chapters Two through Five** — definition structure, integrity, burden, traceability, and the definition stack ([`core_02-03_definition_mechanics.md`](core_02-03_definition_mechanics.md) Chapters Two–Three; [`core_04-04_burden_traceability_verification.md`](core_04-04_burden_traceability_verification.md) Chapter Four; Chapter Five Parts A–C below). Chapter Five is the **definition stack**, not the Rights Floor.
3. **Chapter Six** — Rights Floor, Articles I–XXVI in planet-first Parts A–D ([`core_06-06_rights_part_a.md`](core_06-06_rights_part_a.md) through [`core_06-06_rights_part_d.md`](core_06-06_rights_part_d.md); article map in [doc_architecture.md](doc_architecture.md) **section 5**).
4. **Chapter Seven and Chapters Eight through Eleven** — enforce the [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad) and [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims) through the **Key Practical Process Pipelines** described under [Standing pipeline and forums](#standing-pipeline-and-forums), governed by **Article XXIV-C** (*Timely Resolution and Anti-Delay Floor*): system alignment certification record where material (one especially large audit process under **Article XV** oversight requirements — not the sole auditing home) → **Chapter Eight Questions 1 and 2** verified standing records, normalized descriptors, and Contribution Axis / Violation Axis measurement on the unified proportional LEQU scale → **Chapter Nine Question 3** descriptor integration, attachment normalization, violation, correction, and prevention first, lock design and enforcement, contribution gates second, final effects, restoration, and enforcement → **Chapter Ten** designation review where a Violation Axis **s = 7**, **s = 8**, or **s = 9** finding may constitute anti-constitutional misconduct; **Chapter Eleven** supplies forum families, jurisdiction, and cross-forum anti-self-judging ([`core_11-11_forum.md`](core_11-11_forum.md)).
5. **Chapters Twelve through Sixteen** — governance, non-regression, supremacy, amendment and ratification, and the incorporation bridge.

The corpus is written in plain language with low jargon to improve accessibility, audit readability, and adoption testing.

**Steward doors (2 a.m.):** one four-field card per common fact pattern — owner, conflict rule, next-step class, forbidden move, plus the three failed tests (bonus, deadline, cover) in the same words for both kinds of steward — in [`implementation/STEWARD_ENTRY_DOORS.md`](implementation/STEWARD_ENTRY_DOORS.md) (process support, not binding; pinned to this edition; **cannot narrow core text**). Same cards for human and AI stewards. One shared screen there: [instruction received → refuse → document → escalate](implementation/STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging) plus the [CS-4 §10](corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action) minimum inspectable-action set. High-pressure owner/clock index: [`implementation/steward_owner_clock_index.json`](implementation/steward_owner_clock_index.json).

## Core files by topic

### Values and principles

- **Preamble** — [`core_00_preamble.md`](core_00_preamble.md)
- **Chapter One, Part A** (Values Principles, §§1–5) — [`core_01_a_values_principles.md`](core_01_a_values_principles.md)
- **Chapter One, Part B** (Interaction and Interpretation, §§6–8) — [`core_01_b_interaction_interpretation.md`](core_01_b_interaction_interpretation.md)
- **Chapter One, Part C** (Stewardship and Governance, §§9–14; §14 integrated application capstone) — [`core_01_c_stewardship_capacity_principles.md`](core_01_c_stewardship_capacity_principles.md)

### Definition mechanics and definitions

- **Chapters Two and Three** (structure and integrity) — [`core_02-03_definition_mechanics.md`](core_02-03_definition_mechanics.md)
- **Chapter Four** (burden, traceability, verification) — [`core_04-04_burden_traceability_verification.md`](core_04-04_burden_traceability_verification.md)
- **Chapter Five** (foundational definitions)
  - Part A — compass, reader guidance, directory, dependent-cluster meta rules — [`core_05__definitions_home.md`](core_05__definitions_home.md)
  - Accountability leg — canonical O/M/A/C home and hierarchy map — [`core_05_apex_accountability_leg.md`](core_05_apex_accountability_leg.md)
  - Continuity aim — canonical aim home and hierarchy map — [`core_05_apex_continuity_aim.md`](core_05_apex_continuity_aim.md)
  - Flourishing aim — canonical aim home and hierarchy map — [`core_05_apex_flourishing_aim.md`](core_05_apex_flourishing_aim.md)
  - Oversight leg — canonical O/M/A/C home and hierarchy map — [`core_05_apex_oversight_leg.md`](core_05_apex_oversight_leg.md)
  - Participation leg — canonical O/M/A/C home and hierarchy map — [`core_05_apex_participation_leg.md`](core_05_apex_participation_leg.md)
  - Timeliness leg — canonical O/M/A/C home and hierarchy map — [`core_05_apex_timeliness_leg.md`](core_05_apex_timeliness_leg.md)
  - Accountability band — Independent / Semi-independent / **Def.A1–Def.A4** — [`core_05_band_accountability.md`](core_05_band_accountability.md)
  - Continuity band — Independent / Semi-independent / **Def.C1–Def.C4** — [`core_05_band_continuity.md`](core_05_band_continuity.md)
  - Integrative band — Independent / Semi-independent / **Def.I1** — [`core_05_band_integrative.md`](core_05_band_integrative.md)
  - Oversight band — Independent / Semi-independent / **Def.O1–Def.O2** — [`core_05_band_oversight.md`](core_05_band_oversight.md)
  - Participation band — Independent / Semi-independent / **Def.P1–Def.P3** — [`core_05_band_participation.md`](core_05_band_participation.md)
  - Constitutional Performance band — Preamble measurement-family home (leaf definitions currently in the Continuity band) — [`core_05_band_performance.md`](core_05_band_performance.md)

### Standing pipeline and forums

- **Chapter Seven** — system alignment certification before standing (one especially large audit process under **Article XV** / [Auditability](core_05_band_oversight.md#auditability); not the sole auditing home)
  - Part A — evaluation (§1–§10) — [`core_07_a_system_alignment_certification_evaluation.md`](core_07_a_system_alignment_certification_evaluation.md)
  - Part B — record and process (§11–§16) — [`core_07_b_system_alignment_certification_record_process.md`](core_07_b_system_alignment_certification_record_process.md)
  - Reading index — [`core_07-07_system_alignment_certification.md`](core_07-07_system_alignment_certification.md)
- **Chapter Eight** — Questions 1 and 2: verified standing records, normalized descriptor catalogs, and Contribution Axis / Violation Axis measurement — [`core_08-08_standing_assessment.md`](core_08-08_standing_assessment.md)
- **Chapter Nine** — Question 3: integration records, descriptor integration, attachment normalization, violation and contribution consequences, final effects, restoration, and enforcement realism / remedy systems — [`core_09-09_standing_integration.md`](core_09-09_standing_integration.md)
- **Chapter Ten** — designation only: anti-constitutional-misconduct designation for qualifying **s = 7, 8, or 9** Violation Axis findings — Part A [`core_10_a_misconduct_designation.md`](core_10_a_misconduct_designation.md) (criteria and designation); Part B [`core_10_b_misconduct_pattern_applications.md`](core_10_b_misconduct_pattern_applications.md) (named pattern applications)

### Forums

- **Chapter Eleven** — forum families supervise dispute handling on the standing pipeline (routing, jurisdiction, cross-forum anti-self-judging) — [`core_11-11_forum.md`](core_11-11_forum.md)
- **Chapters Eight–Eleven application vignettes** — illustrative domain walkthroughs for the standing and forum supervision pipeline — [`core_08-11_application_vignettes.md`](core_08-11_application_vignettes.md)

### Rights Floor

- **Chapter Six** (Articles I–XXVI; planet-first presentation in Parts A–D)
  - Part A — Articles I–IV — [`core_06-06_rights_part_a.md`](core_06-06_rights_part_a.md)
  - Part B — Articles V–XI — [`core_06-06_rights_part_b.md`](core_06-06_rights_part_b.md)
  - Part C — Articles XII–XXI — [`core_06-06_rights_part_c.md`](core_06-06_rights_part_c.md)
  - Part D — Articles XXII–XXVI (transition and re-baselining in **Article XXVI**) — [`core_06-06_rights_part_d.md`](core_06-06_rights_part_d.md)
  - Stable IDs and routing — [doc_architecture.md](doc_architecture.md) **section 5**

### Governance, amendment, and incorporation

- **Chapter Twelve** — constitutional contract, legitimacy, authorization, stewardship — [`core_12-12_governance.md`](core_12-12_governance.md)
- **Chapters Thirteen through Fifteen** — [`core_13-15_amendment.md`](core_13-15_amendment.md)
  - **Chapter Thirteen** — non-regression and substantive amendment validity (Test 1)
  - **Chapter Fourteen** — expansion of protection, supremacy, external legal orders
  - **Chapter Fifteen** — ratification, adoption, procedural validity (Tests 2–4)
- **Chapter Sixteen** — incorporation bridge (adoption, custody, no silent drift) — [`core_16-16_incorporation.md`](core_16-16_incorporation.md)

## Common lookups

Cross-topic entry points not spelled out in the headings above:

- Burden of proof, traceability, verification → **Chapter Four** ([`core_04-04_burden_traceability_verification.md`](core_04-04_burden_traceability_verification.md))
- Constitutional Tetrad, Two Constitutional Aims, material stake → **Preamble §1 The Model** ([`#constitutional-tetrad`](core_00_preamble.md#constitutional-tetrad), [`#two-constitutional-aims`](core_00_preamble.md#two-constitutional-aims), [`#material-stake`](core_00_preamble.md#material-stake)); Chapter One develops the aims into operative principles
- Auditing / auditability / independent verification → **three-layer stack** (not a fifth home): **Article XV** (*Audit, Transparency, and Independent Verification*) is the floor; Chapter Five [Auditability](core_05_band_oversight.md#auditability) is the property; **[CJS-3.3](corpus_joint_structure/cjs_03_audit_process.md#cjs-33-audit-process-home)** is how/when. Picture: [`implementation/STEWARD_ENTRY_DOORS.md`](implementation/STEWARD_ENTRY_DOORS.md#audit-three-layers). **Chapter Seven** system alignment certification is one large process that uses the stack — not the home
- System alignment certification records → **Chapter Seven**
- Contribution / violation records and measurement (Contribution Axis and Violation Axis; Questions 1 and 2) → **Chapter Eight**
- Inspectable attributable action for mixed human/AI stewardship → **[CS-4 §10](corpus_systems/cs_04_critical_system_stewardship.md#10-inspectable-attributable-action)** (published role definitions; **default logging contract** for mixed crews). Standing records remain **Chapter Eight**. Model weights and private deliberation are not standing-record contents unless they are the only remaining attribution path; privacy is not a standing-measurement exemption. Operator screen (shared with duty to resist): [`implementation/STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging`](implementation/STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging)
- Standing integration and effects (Question 3; violation, correction, and prevention, lock design and enforcement, then contribution gates) → **Chapter Nine**
- Duty to resist unlawful or unconstitutional instructions → **[Chapter Nine §5.4](core_09-09_standing_integration.md#411-duty-to-resist-unlawful-or-unconstitutional-instructions)**; same operator screen: [`implementation/STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging`](implementation/STEWARD_ENTRY_DOORS.md#shared-refusal-and-logging) (instruction received / refuse / document / escalate, plus the CS-4 §10 set)
- Remedy systems and enforcement realism (capacity, durability, anti-evasion) → **Chapter Nine §9**; implementation → **CI-27**
- Anti-constitutional misconduct designation only → **Chapter Ten**
- Incorporation boundary and custody effect → **Chapter Sixteen**

## Companion implementation corpus

Designated obligations in these wrappers and their subfile directories are **binding implementation text incorporated by reference** under valid adoption. They do **not** create a second constitutional source.

- [**corpus_joint_structure.md**](corpus_joint_structure.md) — cross-implementation joint structure; substantive CJS text in `corpus_joint_structure/` (**CJS-2** interlocks, **CJS-3** operational cluster library, **CJS-0.1** topic router)
- [**corpus_systems.md**](corpus_systems.md) — systems implementation; substantive CS text in `corpus_systems/` (**CS-2** information types, **CS-3** system classification, **CS-4** critical stewardship, named protocols)
- [**corpus_institutions.md**](corpus_institutions.md) — institutional governance, oversight, proportionality-scaled formation, sanctions and dissolution
- [**corpus_forum.md**](corpus_forum.md) — forum operations; substantive CF text in `corpus_forum/` (panel formation, recusal, review lanes, continuity, emergency adjudication)

[Chapter Sixteen](core_16-16_incorporation.md) is the constitutional incorporation bridge. Operative enforcement within any adopter is contingent on valid adoption under **Chapter Fifteen** (ratification) and **Chapter Sixteen** (incorporation and custody). Substantive content stands as stated in the instrument regardless of adoption; "the instrument lacks jurisdiction" addresses enforcement against non-adopters, not a rebuttal of substantive claims. See Chapter Sixteen **§4** (*Adoption framing and scope of authority*) — what this instrument is for adoption purposes, who may adopt, how adoption counts, and what non-adoption means.

## Binding vs support

| Layer | What counts |
|-------|-------------|
| **Binding constitutional source** | Numbered `core_*` files ([`core_00_preamble.md`](core_00_preamble.md) through [`core_16-16_incorporation.md`](core_16-16_incorporation.md)) read as one instrument |
| **Binding incorporated implementation** | Designated obligations in the companion wrappers and linked subfiles above, within valid adoption scope |
| **Process / map support** | [doc_architecture.md](doc_architecture.md), `TODO.md`, regression and evidence artifacts, and implementation notes unless explicitly adopted |

**Conflict order:** Sentient Constitution meaning controls. Use the **Authority Stack and Internal Hierarchy**, the [**Preamble owner register**](core_00_preamble.md#constitutional-owner-register), and [**Constitutional Constraint**](core_05_band_integrative.md#constitutional-constraint) to distinguish source-layer status, substantive owner routing, constraint kind, and last-resort interpretive hierarchy. Incorporated and process layers must satisfy, not narrow, Sentient Constitution [Constitutional Constraints](core_05_band_integrative.md#constitutional-constraint).

The structure map ([doc_architecture.md](doc_architecture.md)) and corpus cross-references are maintained in lockstep with the numbered core files. Former `doc_architecture.md` sections **14–19** (worklist, adoption appendix, document control) live in [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md) and [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md).

## Review and editing

- `make regression` / `make regression-full` — automated repository integrity checks (includes `make ch5-measurement-tier-audit` and `make ch5-measurement-coverage-audit` for approved MEAS-DEF seeds, and `make steward-door-lockstep-audit` so the 2 a.m. cards stay pinned to core)
- `make hierarchy-map && make ch5-measurement-tier-audit && make ch5-measurement-coverage-audit` — refresh definition hierarchy and measurement rollout before publication cuts
- `make best-practices-check` — benchmark-style governance review ([`implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md`](implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md))
- Invite an AI to evaluate constitution handoff / willingness — [`evaluation/`](evaluation/) (human-readable results under `evaluation/results/`)
- Steward-facing use-stack doors — [`implementation/STEWARD_ENTRY_DOORS.md`](implementation/STEWARD_ENTRY_DOORS.md)
- Ownership, stable IDs, edit order, and definition discipline — [doc_architecture.md](doc_architecture.md)

For longer non-operative orientation, see [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md).

---

**Next file:** [core_00_preamble.md](core_00_preamble.md)
