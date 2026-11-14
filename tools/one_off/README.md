# One-off scripts (finished)

Each script here ran once to carry out a numbered move recorded in `doc_architecture.md` or `archive/`. None is called by the Makefile, the workflows, another tool, or any rule text, and none has a test. They are kept as the record of how each move was made, and they only make sense against the tree as it was at that move.

To run one again (not expected): `PYTHONPATH=tools python3 tools/one_off/<name>.py --help` from the repository root. Some assume they live directly in `tools/` and import sibling modules, and they have not been re-tested here.

Moved from `tools/` on 2026-11-14 (509th move's follow-on; see the 510th move). Two scripts that looked similar were left in `tools/`: `parallel_norm_check` (it has a test) and `principle_check` (its purpose is unclear).

| Script | What its docstring says |
|---|---|
| `apply_cjs_op_to_guidepost_migration.py` | Migrate CJS operational cluster oDef OP-O/OP-E/OP-C triads to Chapter Five guidepost form. |
| `apply_file_top_placement.py` | One-shot helper: wrap core_* binding banners in Corpus placement widgets. |
| `apply_measurements_to_e_migration.py` | Migrate Chapter Five leaf definitions to the guidepost O/M/E/C entry model. |
| `apply_o_scope_migration.py` | One-pass migration: add In scope / Out of scope sub-bullets to Chapter Five O components. |
| `apply_wave9_primary_measurements.py` | Apply Wave 9 primary-only *Measurements:* blocks to residual Chapter Five definitions. |
| `ch06_education_article_iv_restructure.py` | Chapter Six: combine education into a new Article IV and renumber. |
| `ch06_promote_lequ_section_4.py` | Promote Chapter Nine LEQU from Chapter One §8.2 to top-level §4; renumber §3.3→§5, §3.4→§6. |
| `ch06_prune_legacy_anchors.py` | Remove legacy duplicate anchors from core_06; update corpus links. |
| `ch06_renumber_4_to_3.py` | Renumber Chapter Nine §4 → §3; §4.0 → Chapter One §8.1; Chapter One §8.1 → Chapter One §8.2; Chapter One §8.2 → §3.3; §3.3 → §3.4. |
| `ch06_swap_22_23.py` | Swap Ch6 Chapter One §8.2 (operational) and Chapter One §8.3 (no-offset); renumber subsections and anchors. |
| `ch1_continuity_relocation.py` | Relocate Chapter One's Continuity principles into Part A as §§6–9 and renumber §§6–16. |
| `ch1_part_b_consecutive_renumber.py` | Renumber Chapter One Part B §§11–16 → §§9–14 (consecutive after Part A §§1–8). |
| `ch1_swap_6_7.py` | Swap Chapter One §6 and §7 (Part A): Shared-System Capacity becomes §6, Resilience and Self-Healing Design becomes §7. |
| `ch5_constitutional_migration.py` | Migrate Chapter Five definitions to constitutional Triad / Aims band organization. |
| `ch5_def_cluster_id_migration.py` | Migrate Chapter Five dependent-cluster IDs from §3.x to Def.{band}{n}. |
| `ch5_path_rename_rewrite.py` | Rewrite Chapter Five path references after core_05_* rename. |
| `ch8_certification_status_rename.py` | Rename the Chapter Eight status vocabulary from "recognition" to "certification". |
| `ch8_fix_after_reorder.py` | Fix Chapter Eight anchors after § reorder and update corpus cross-references. |
| `ch8_go_live_gate_reorder.py` | Chapter Eight third reorder: go-live gate, challenge path moves to Operate (CH9-PROCESS-ORDER-01). |
| `ch8_phase2_split_remap.py` | Chapter Eight: split Phase II (Evaluate) into sub-phases IIa / IIb / IIc. |
| `ch8_reorder_sections.py` | Reorder Chapter Eight sections and renumber (drop 6A–6E letter suffixes). |
| `ch8_reorg_link_remap.py` | Remap links after the Chapter Eight §1–§9 reorganization. |
| `ch8_reorg_link_remap_stage2.py` | Stage 2 of the Chapter Eight reorganization: nest §4–§5 under §3 (§3.8, §3.9) and renumber Part B §6–§9 to §4–§7. |
| `ch8_section_renumber.py` | Renumber Chapter Eight: §1A → §2; shift §2–§10 up by one (§2→§3 … §10→§11). |
| `ch8_split_parts.py` | Split Chapter Eight into Part A (evaluation) and Part B (record/process). |
| `chapter_numbering_inverse_proof.py` | Check changed tracked files against the pre-chapter-numbering baseline. |
| `cjs_read_with_relocation.py` | Move operative-prose ``Read it with:`` blocks into the owning Trace widget. |
| `fix_widget_top_stack.py` | One-shot: make file-top opening widgets contiguous. |
| `insert_plain_terms_gloss.py` | Insert ``*In plain terms:*`` glosses into adopted-implementation subfiles. |
| `migrate_dec_to_dac.py` | Rename D/A/C widget infrastructure to D/A/C (prerelease, 2026-07). |
| `migrate_e_to_a.py` | One-off migration: rename the definition Assessment component from E -> A. |
| `promote_cs_bold_headings.py` | Turn the bold run-in labels in the CS protocol files into real headings. |
| `promote_cs_headings.py` | Promote CS numeric headings to CS-n.m form and drop self-only section Traces. |
| `repair_ch5_dac_anchors.py` | Insert missing NAV-DAC-12 entry / E / C anchor tags on Chapter Five definitions. |
| `split_gloss_pointer_sentence.py` | Break the three-clause pointer sentence at the end of adopted-implementation glosses. |
| `wrap_ch5_trace_blocks.py` | Wrap plain **Trace** blocks in Chapter Five band files with NAV-DEC Trace widgets. |
