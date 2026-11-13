# Final chapter structure migration (one-off record)

These scripts produced the 492nd move in [doc_architecture.md](../../doc_architecture.md): Parts only in Chapters 1, 5 and 6; Chapter One split into six Parts; Chapter Six re-slotted by ten; Chapters 9, 10, 13 and 14 promoted to chapters (0–28, 50 core files); a §1 Purpose and Role stub in every chapter; sections restarted in each new chapter; corpus layers re-homed.

They run only against the pre-move tree. They are kept as the record of how every cite, link, anchor, registry row, tool constant and generated file was rewritten, in the same spirit as the earlier one-off moves in `tools/` (for example `ch1_secularism_move.py`). Run `run.sh` from a clean checkout of the commit before the move to reproduce the result.

| Script | Role |
|---|---|
| `mkspecs2.py` | Builds the Chapter One Part split spec from the current tree. |
| `split_parts.py` | Splits Chapter One into six Part files and re-slots the cut seams. |
| `patch_tools.py` | Updates tool constants for the Chapter One split. |
| `chapters.py` | Main engine: file renames, section restarts, cite, link and anchor rewrites, registry, corpus re-homing, footers, Purpose and Role stubs. |
| `patch_words.py` | Extends chapter-word lists in tools to Twenty-Eight. |
| `post2.py` | Retargets the duplication audit to Chapters 12–14 against 9–11. |
| `handedits.py` | Tool constants, test fixtures, README, TODO map, one corpus run sheet. |
| `autoname.py` | Adds the target heading title to unnamed section cites. |
| `fix_part_cites.py` | Repairs Part cites flagged by `part_cite_chapter_audit`. |
| `obligation_totals.py` | Counts obligation clauses before and after (3,815 both). |
