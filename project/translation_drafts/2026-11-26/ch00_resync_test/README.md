# Chapter 0 resynchronization test — structural pass

**Status:** Structural test bases only. No locale draft is a complete resynchronization, reviewed translation, or publication candidate. All outputs remain under `project/translation_drafts/`.

## Pinned English source

- Commit: `5ce40ac4b11fc03a99aa603e04eb5ec242470440`
- Edition: `SC-Corpus-2026.11.25`
- Source: [`core_00.000_preamble.md`](../../../../core_00.000_preamble.md)
- SHA-256: `90799cb8019b41356fa5dd90565e3f9540fc346e8c77e2c321b841654f39b274`

## Test operation

For each locale, the test read the existing `translations/<locale>/core_00_preamble.md`, retained the opening and §§1–3, removed the old §3.2 *Key Governance Processes*, carried old §3.3 *Governance Layers* forward as current §3.2, and dropped old §§4–9, which now belong to the Constitutional Map. It updated the corresponding local governance-layer anchor. Japanese and Korean lacked the complexity-orientation paragraph in the published files, so their previous unreviewed excerpt drafts supplied that paragraph in these structural bases.

## Locale results

| Locale | Existing file bytes | Structural base bytes | Kept body lines | Existing pin |
|---|---:|---:|---:|---|
| `ar` | 63706 | 29133 | 133 | SC-Corpus-2026.08.09 |
| `bn` | 94487 | 42832 | 133 | SC-Corpus-2026.08.09 |
| `es` | 63526 | 24016 | 134 | SC-Corpus-2026.08.09 |
| `fa` | 69296 | 31877 | 133 | SC-Corpus-2026.08.09 |
| `fr` | 55780 | 25639 | 133 | SC-Corpus-2026.08.09 |
| `hi` | 98515 | 44789 | 133 | SC-Corpus-2026.08.09 |
| `id` | 50730 | 24038 | 133 | SC-Corpus-2026.08.09 |
| `ja` | 51101 | 24850 | 134 | SC-Corpus-2026.08.09 |
| `ko` | 47532 | 23227 | 134 | SC-Corpus-2026.08.09 |
| `mr` | 102269 | 44681 | 131 | SC-Corpus-2026.08.09 |
| `pt` | 55607 | 23972 | 131 | SC-Corpus-2026.08.09 |
| `ru` | 86985 | 37285 | 131 | SC-Corpus-2026.08.09 |
| `ta` | 124645 | 51397 | 131 | SC-Corpus-2026.08.09 |
| `te` | 105113 | 44440 | 131 | SC-Corpus-2026.08.09 |
| `th` | 108054 | 46836 | 131 | SC-Corpus-2026.08.09 |
| `tr` | 54173 | 23346 | 131 | SC-Corpus-2026.08.09 |
| `ur` | 69476 | 30438 | 131 | SC-Corpus-2026.08.09 |
| `vi` | 63193 | 27404 | 131 | SC-Corpus-2026.08.09 |
| `zh` | 44904 | 19370 | 131 | SC-Corpus-2026.08.09 |

The boundary and heading-order test passed for all **19/19 locales**. After the structural transform, all **13 current English Preamble anchors** are present in each base. Each output is under the 1 MB file limit.

## Findings and remaining work

- The published translations contain the pre-reorganization Preamble structure; §§4–9 need to be preserved as input for Chapter 1 resynchronization, not deleted from the overall translation corpus.
- All 19 files have prior Chapter 0 source-refresh excerpts, but those excerpts target older source revisions and contain older chapter/file references. They are supporting material, not current text.
- The structural bases do not yet translate the current opening widget, align the new §2.1–§2.4 structure, reconcile all changed English wording, refresh cross-reference targets, or complete glossary and fluent review.
- Existing locale README files state language varieties and glossary choices; these must govern any full AI-assisted drafting and later independent review.
- Existing translation pins differ from the current source snapshot. No files in `translations/` were changed.

## Output files

One `*__structural_base.md` per supported locale is in this directory. Each file is visibly marked as an internal, incomplete structural base; it is not ready to read, publish, or synchronize. The test confirms the section split and anchor mapping, but does not pass the full-fidelity drafting/review gate in the [resynchronization plan](../../../plans/translation_resynchronization_plan_2026-11-25.md).
