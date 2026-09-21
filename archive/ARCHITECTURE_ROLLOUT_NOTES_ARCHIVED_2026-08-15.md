# Architecture rollout notes (archived 2026-08-15)

Process notes removed from [doc_architecture.md](../doc_architecture.md) during the 2026-08-15 editor-map cleanup. They are **not** corpus text. Live rules remain in `doc_architecture.md` section 4.

## Category-stub removal (2026-07)

The former Preamble §3 *Major Measurement Aspects* stubs and their `#measuring-*` category anchors were removed. The §2 overview links straight to Chapter Five, and Chapter Five definitions no longer back-link to Preamble category anchors. Machine seed keys `3.1`–`3.8` on the `ch00_measurement` tag remain as technical identifiers; they are not current Preamble section numbers.

## Guidepost O/M/A/C rollout (2026-07)

Reader-facing guidepost headers (**What it is** / **How to measure and assess** / **What must hold**), bold run-in sublabels (`**Primary measure:**` / `**Primary assessment:**` / `**Primary failure:**`, etc.), and `#{term}-a` / `#{term}-c` anchor placement became the corpus norm on Chapter Five leaf definitions. A contemporaneous count (~165 migrated / ~55 remainder on letter-marker or `*Measurements:*` form) is **not** current; band files no longer carry `*Measurements:*` blocks. Aim and Tetrad-leg apex heads may still use letter markers or guidepost headers. Migration helper used during the pass: `tools/apply_measurements_to_e_migration.py`.

Component-letter rename: Assessment was formerly labelled **Evaluative (E)** with `#{term}-e` anchors; it is now **Assessment (A)** with `#{term}-a` anchors. The architecture section anchor `measurement-informed-ec-meas-def-01` was preserved for inbound links.

## CJS oDef guidepost rollout (2026-08)

**CJS-3** joint operational definition entries adopted the same reader-facing guidepost headers and bold run-in sublabels as Chapter Five leaves, under **CJS-1.13**–**CJS-1.14**. They remain **oDef** / **CJS-3** joint operational rules — not Chapter Five **Def.*** Independent Definitions. Migration helper: `tools/apply_cjs_op_to_guidepost_migration.py`.

## Depends on pilot (2026-07)

Optional `**Depends on:**` under **What it is** was piloted on: Self-Healing; Incentive Alignment; Flourishing; Use of Force; Innovation Reward and Anti-Enclosure; Constitutional Constraint; System Alignment Certification; Autonomous Lethal System; Weapons of Mass Harm; Combatant / Non-Combatant Distinction; Autonomous Coercion Tool; Safety (Constraint); Truth (Constitutional Constraint); Emergency and Contingency. The live rule is in `doc_architecture.md` MEAS-DEF-01 (optional constitutive prerequisites under **What it is**).

## Measurement waves 1–9 (complete)

1. Pin tier schema on pilot and wave entries — `tools/architecture/measurement_tier_seeds.json`.
2. Preamble §2 overview links categories and subcategories directly to Chapter Five measurement-family homes — complete (former §3 category stubs removed).
3. Remove redundant measurement rollups from aim heads — complete.
4. `make ch5-measurement-tier-audit` wired in `make regression` — complete.
5. `make ch5-measurement-coverage-audit` wired in `make regression` — complete.
6. `make measurement-rollout-status` emits `doc_architecture/generated/measurement_rollout_status.md` — complete.
7. Wave 9 residual rollout via `tools/apply_wave9_primary_measurements.py` — complete.

Live status is the generated measurement-rollout file, not this archive.

## Systems file split and CS-2 cleanup notes (executed)

`corpus_systems.md` is a compatibility entrypoint; substantive CS text lives in `corpus_systems/` subfiles. Prefer **CS-2** over legacy “Chapter Two (Information Types…)” wording inside CS text. **CS-2** is split: Part A (`cs_02_a_information_types_and_handling.md`, §1–§7 handling rules); Part B (`cs_02_b_data_classifications.md`, §8 type descriptions). **CJS-2** and **CJS-3** are the live citation grammar for `corpus_joint_structure.md`.
