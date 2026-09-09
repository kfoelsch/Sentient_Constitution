# Core filename normalize — reference audit

**Date:** 2026-09-09  
**Gate:** [doc_architecture.md](../../doc_architecture.md) rename readiness (reference audit, same-change link updates, dated evidence, compatibility decision, edition/custody record).

## Change

Split the remaining multi-chapter core files and drop doubled `NN-NN` names so each chapter file is `core_<nn>_*.md`.

| Old filename | New filename(s) |
|---|---|
| `core_02-03_definition_mechanics.md` | `core_02_definition_structure.md` (Chapter Two); `core_03_definition_integrity.md` (Chapter Three) |
| `core_13-15_amendment.md` | `core_13_non_regression.md`; `core_14_expansion_supremacy.md`; `core_15_amendment_ratification.md` |
| `core_04-04_burden_traceability_verification.md` | `core_04_burden_traceability_verification.md` |
| `core_06-06_rights_part_*.md` | `core_06_rights_part_*.md` |
| `core_07-07_system_alignment_certification.md` | `core_07_system_alignment_certification.md` |
| `core_08-08_standing_assessment.md` | `core_08_standing_assessment.md` |
| `core_09-09_standing_integration.md` | `core_09_standing_integration.md` |
| `core_11-11_forum.md` | `core_11_forum.md` |
| `core_12-12_governance.md` | `core_12_governance.md` |
| `core_16-16_incorporation.md` | `core_16_incorporation.md` |

Section anchors are unchanged. The only remaining hyphenated range file is the cross-chapter vignette `core_08-11_application_vignettes.md`.

## Compatibility decision

No redirect stub files. This corpus is **pre-release**: inbound cites were retargeted in the same change. Historical mentions of the old filenames remain only under `archive/` and dated `evidence/` snapshots.

## Edition / custody

No publication-cut edition bump. Edition label remains `SC-Corpus-2026.08.09` in [README.md](../../README.md).

## Same-change link updates

Live corpus, tools path registries (`tools/corpus_paths.py`, `tools/footer_audit.py`), generated indexes, and family maps were updated in the same change. Regenerators: `make ai-corpus-sync`, `python3 tools/emit_architecture_index.py`.

## Reference audit

Post-rename grep of the working tree excluding `archive/` and `evidence/` found **no** remaining live references to the doubled `NN-NN` chapter filenames or to `core_02-03_definition_mechanics.md` / `core_13-15_amendment.md`, except the one-shot migrator `tools/core_filename_normalize.py` (already applied; not rerun).
