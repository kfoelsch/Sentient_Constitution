# Corpus chapter numbering migration plan

**Drafted:** 2026-10-20 (Claude session, from a steward proposal). **Revised 2026-10-20 (evening):** the core files are renamed in the same migration, and the core chapter list is treated as fixed (D1, D10, Phase 0). **Signoff update 2026-10-20:** D2, D4, D5, D7, D8, D9, D11, D12, D13 and D14 approved; D6 revised by the steward to align lettered chapter files during this migration. **Final signoff update 2026-10-21:** all D1-D14 design decisions and all chapter-home assignments are settled, including the revised D6 and dotted reader-facing numbers. **Implementation status (2026-10-21):** The approved registry, crosswalk, chapter renames, resolver, audits, and Trace updates are applied on `codex/chapter-numbering-migration`. The expanded numbering prose proof passes for all 43 core and 74 corpus files after reference, filename, anchor, Core home, and approved Trace normalization. `renumber_corpus_chapters.py --verify` reports zero legacy-id findings. All 482 unique qualified sections and 485 heading anchors round-trip; chapter-number migration tests pass for all 117 rows and finalizer markers. The inverse checker passes for all tracked changes after recording the planned policy/front-door/support/generated changes; it reports 141 new untracked files separately, including dated evidence outputs, two implementation templates with no baseline counterpart, migration tooling, and the plan/worklist. `make audit-report` is 104/105: the sole remaining finding is three Japanese translation Markdown-format findings in `translations/ja/core_05_band_integrative.md`, unchanged from baseline. `make audit-report-all` is 130/138, matching the previously recorded baseline: in addition to that translation formatting finding, the same plain-language/readability findings and paused translation audits remain outside the regression gate. Translation files remain untouched under the standing translation decision. Front-door, link, section-label, local-fragment, generated-file, and audit-test categories pass. The Phase 4 technical proof is ready for steward signoff on the core-file id-only diff; that human approval is still pending. The regression gate remains at its baseline translation finding, which cannot be repaired under the paused translation decision. The plan's verification scope and the reviewed collateral paths are recorded below.

## Filename format correction (2026-10-21)

The initial rename used concatenated five-digit filenames such as `core_06005_…` even though reader-facing identifiers use `6.005`. All active English numbered filenames now insert the separator explicitly as `core_06.005_…`, `cjs_05.105_…`, and so on. The five-digit machine IDs and registry identifiers are unchanged. Translation files and their filenames remain unchanged under standing decision D12.

## 1. Purpose

Corpus chapter numbers (CJS, CS, CI, CF) are unrelated to core chapter numbers and to each other. "13" currently means the Forum chapter (Chapter Thirteen), CF-13 (fallback operation), CI-13 (failure and dissolution), and CS-13 (system requirements). Inserting a chapter shifts everything after it: Chapter Seven's insertion renumbered the core, and CI-13's split had to put CI-28 at the end because there was no room beside CI-13.

The steward's proposal: give each corpus chapter a number that starts from the core chapter it serves, with room between numbers for growth. The goal is long-term maintainability and consistency. Migration cost is not a constraint. The window is: the corpus is pre-release, old anchors are not kept as redirects ([doc_architecture.md](../../doc_architecture.md), anchors and renumbering), and the CONTRIBUTING lanes start after the announcement.

## 2. The approved scheme

A corpus chapter number is **five digits, `CCLSS`**, fixed width, zero padded:

| Digits | Meaning | Values |
|---|---|---|
| `CC` | Core home: the core chapter whose rules this chapter implements. The same two digits as the core chapter's own number. | `00`-`18` |
| `L` | Layer | `0` core, `1` CJS, `2` CI, `3` CS, `4` CF; `5`-`9` reserved for future layers and subdocuments |
| `SS` | Sequence inside the (home, layer) slot, in reading order | `05`, `10`, ... `95` (steps of 5) |

### Reader-facing number format

Steward direction in session 2026-10-20: group the thousands with a separator for readability. Use a **dot**, with no leading zero in the thousands group: `01005` displays as **1.005**, `02015` as **2.015**, `06000` as **6.000**, and `13415` as **13.415**. Values below 1,000 display with a zero group, such as **0.105**. These are identifier strings, never decimal quantities.

Implementation convention at initial migration: registry keys and machine ids retained fixed-width `CCLSS` digits, while filenames lacked the separator used in reader-facing references. Filename correction (2026-10-21): active English numbered filenames now use `CC.LSS` with a literal dot after the two-digit chapter home; the machine IDs remain `CCLSS` and registry rows remain authoritative. Translation filenames are unchanged under standing decision D12. Reader-facing corpus references include the prefix, such as **CI-6.220**, **CF-13.415**, and **CJS-5.105**. Use `§` for section references (**CI-11.210 §4**) so the grouping dot is distinct from the section hierarchy. Lookup must accept dotted display references as well as machine ids and legacy ids. D11 subsequently confirmed the existing core-file order and vignette placement at **10.005**.

Examples: **CI-6.220** is the CI chapter on neurodiversity and disability justice (home: Chapter Six, the Articles). **CF-13.415** is CF routing operations (home: Chapter Thirteen, Forum). **CJS-5.105** is the CJS-3 operational terms (home: Chapter Five).

Machine section ids keep their suffix: `CI-13.4` becomes `CI-11210.4`. File names carry the same padded number: `ci_11.210_institutional_failure_dissolution.md`. Each lettered corpus file receives its own chapter number during this migration (D6); its file name uses that number and drops the ordering letter. The registry maps old file-qualified section ids to their new chapter ids. Existing section suffixes are preserved unless a separately reviewed mapping requires a change. The layer prefix stays in every id as a readable check on the layer digit.

### Core chapters and core parts

Core chapters live in the same number space, with layer digit `0`. A core chapter is `CC000` (Chapter Six is `06000`). A chapter that has one file uses `CC000` as that file's number. A chapter that is split into files gives its index or compass file `CC000` if it has one, and gives the other files `CC005`, `CC010`, ... in reading order. Examples: Chapter Six's five parts are `06005` to `06025`; Chapter Seven is `07000`; Chapter Nine's reading index is `09000` and its Parts A to D are `09005` to `09020`.

Core filenames group the same five-digit number as `CC.LSS`: `core_06.005_rights_part_a.md`, `core_07.000_charters.md`. The part letter is dropped from the file name because the number now carries the order; prose still says "Part A". The visible chapter names ("CHAPTER SIX", "Chapter Six" in prose and headings), Article numbers, and chapter-local section numbers (Chapter One §15.4.4) do not change. The registry records both the number and the ordinal name. Approved mapping: Appendix C.

## 3. Improvements over the original proposal

| Original | Plan | Why |
|---|---|---|
| Core chapters become 0, 1000, 2000, ... | Core chapters get the registry numbers `00000`, `01000`, ..., `18000`, and core files are renamed to match (`core_06.005_...`). The visible names ("Chapter Six") stay in prose and headings. | One number space for every chapter and file, so the tools, the resolver, and the audits treat core and corpus alike, with room for new core parts. Writing "Chapter 6000" in prose (about 14,000 "Chapter X" references, plus translations and citations) would cost readability and add nothing the registry does not already carry. Decision D1. |
| `0100`, `6100` (four digits, mixed widths) | Fixed five digits, `CCLSS`. | One regex, string order equals numeric order, the first two digits are always the core home, and the preamble no longer collapses to "CJS-100". It also removes the anchor ambiguity that `tools/renumber_ci_narrative.py` has to guess around (`ci-121` could be 12.1 or 1.21). |
| Gaps of 100 | Steps of 5 inside each slot (four insertions fit between neighbours), with 19 chapters per slot. | Steps of 10 would cap a slot at 9; home 06 / CI has 15 approved files. |
| Numbers imply the core relationship | Each corpus file also gets a one-line `Core home:` declaration, and an audit checks the number, the declaration, and the registry agree. | Without enforcement the alignment drifts the first time a chapter moves. |
| Align all chapter file names now | Each lettered corpus file receives a distinct chapter number in this migration (D6). Registry and crosswalk rows identify the original file and section as well as the old shared chapter id. | Establishes one file per chapter number now; inverse mapping must preserve the original file boundaries and text. |
| One-off scripts with hard-coded maps (`renumber_ci_narrative.py`) | One registry-driven tool that all four layers and later renumberings use. | The existing scripts hard-code old and new numbers and cover CI only. |
| (not covered) | A permanent machine-readable old-to-new crosswalk, wired into `corpus_lookup.py resolve`. | Review records, translation drafts, and anyone holding an earlier edition can still resolve old ids. It is data, not anchors, so it does not break the fossil-anchor rule. |

## 4. Recorded steward decisions

| # | Decision | Recorded outcome |
|---|---|---|
| D1 | Core chapters and files. | Decided 2026-10-20 (steward): rename core files into the same number space in this migration (section 2, Appendix C). Prose keeps "Chapter Six". Whether to write the number itself in prose is a separate, later choice. |
| D2 | Layer digits. | Approved by the steward in session 2026-10-20: core 0, CJS 1, CI 2, CS 3, CF 4; 5-9 reserved. |
| D3 | Home, order and number for each corpus file. | Approved in session groups on 2026-10-20 and 2026-10-21; the completed mapping in Appendix A records all 74 destination files. The final group approved CI-26 at CI-0.215, CI-4 at CI-14.205, CS-4 at CS-14.305, CJS-4 at CJS-18.105 and CJS-2 at CJS-18.110. CS-12 precedes CS-9 in the systems rights group. Source inventory and implementation verification remain required; these approvals do not claim the migration is implemented. |
| D4 | Layer front matter (registry annex `X-0` and scope chapter `X-1`) lives at home `00`, the Preamble that already hosts the corpus owner register. | Approved by the steward in session 2026-10-20 for all four layers. This numbering placement does not change authority or scope. |
| D5 | Spacing inside a slot. | Approved by the steward in session 2026-10-20: sequence numbers 05, 10, ... 95, allowing 19 chapters per slot and four insertions between adjacent assigned numbers. |
| D6 | Lettered files that share one chapter id (`cjs_03a/c/i/o/p/u`, `cs_02_a/b`, `cs_03_a/b`). | Steward rejected deferral in session 2026-10-20: align chapter file names now for long-term maintainability. Give every lettered corpus file its own number and matching file name during this migration. Homes and reading order are approved under D3; no optional later split phase. |
| D7 | Dated history (archive, evidence, evaluation results, dated TODO and MEMLOG entries, the doc_architecture.md move log). | Approved by the steward in session 2026-10-20: preserve original numbering. In historical passages within active documents, retarget links but retain displayed ids, with a dated crosswalk note. |
| D8 | Edition bump. | Approved by the steward in session 2026-10-20: run `make edition-bump` when the migration lands, because public identifiers change. |
| D9 | Unnumbered files (`cf_sentience_status_record.md`, `cjs_reader_guide.md`). | Approved by the steward in session 2026-10-20: give the Sentience-Status Adjudication Record protocol its own CF number; keep the reader guide unnumbered. D3 confirms the protocol at CF-13.475. |
| D10 | Core chapter list. | Treated as fixed from now (steward, 2026-10-20). A chapter that does appear before the announcement takes the next unused core number if it is added at the end; if it must go in the middle, the registry re-prefixes the affected corpus ids in one run (Phase 0 note). After the announcement, a new core chapter takes the next unused number and no chapter is renumbered. |
| D11 | Core reading order inside split chapters (Chapter Five's compass, apex, and band files; Chapter Nine's index and Parts A-D). `core_10-13_application_vignettes.md` spans Chapters 10-13. | Approved by the steward in session 2026-10-20: preserve the existing file order in Appendix C and place the vignettes at **10.005** (machine key `10005`, filename `core_10.005_application_vignettes.md`), retaining their Chapters Ten–Thirteen title and illustrative scope. |
| D12 | Translation files (`translations/*`) mirror earlier core file names. | Approved by the steward in session 2026-10-20: leave existing translation filenames unchanged during the English migration. Publish the filename crosswalk and a translations README note; align translations through the settled-chapter workflow. Existing translation work remains separate from English edits. |
| D13 | Numbers in Trace widgets (918 widgets across core and corpus). Trace widgets only: not the Downstream/Applies/Compare widgets (steward, 2026-10-20). | Format approved by the steward in session 2026-10-20. Corpus ids already carry the core home in the number. Add the registry number after each link that names a chapter or part: `[Chapter Nine Part A §2 ...](...) (9.005 §2)`. Do not add it to term links, same-file `§` links, or Article links. Generated from the registry, never typed by hand. |
| D14 | Bullets in Trace widgets. Today each line (Upstream, Downstream, Read with, ...) is one semicolon-separated run; 2,820 lines in 918 widgets, 1,012 of them with four or more references and 327 with seven or more (the longest has 23). | Approved by the steward in session 2026-10-20. A line with four or more references becomes a parent bullet with one reference per sub-bullet; lines with one to three stay inline. Done in the same pass as D13, as its own commit, so each widget is touched once. |

## 5. Phases and exit gates

**Phase 0: prepare.**
- Design decisions D1-D14 and the mappings in Appendices A and C are approved as of 2026-10-21. Carry them into the registry and confirm the source-file inventory.
- Land or park in-flight work. Start from current `main` (GIT-LOCAL-SYNC-01) on a branch named for the work. Record a fresh baseline `make audit-report-all` result. The historical 2026-10-20 regression baseline was 103/105; the latest signoff-session regression run passes 105/105. Do not treat historical failures as permission to regress.
- Tag the pre-migration commit.
- Announce a freeze: no merges touching `core_*`, `corpus_*`, ids, or the front doors until the migration lands.
- Core chapter list check: the steward confirms the 19 chapters (0-18) and their order are final (D10). A new chapter after this point costs one registry edit and one tool run, but it is much cheaper before.
- *Gate:* decisions recorded in this file, clean branch, tag.

**Phase 1: registry and tooling (no content change).**
- Add the chapter registry (extend [family_map.json](../../tools/architecture/family_map.json) or add `chapter_numbers.json`). One row per destination chapter/file, including each formerly lettered corpus file (D6): old id and original file, new machine id, dotted display id, layer, core home, title, destination file, status (`active`, `retired`, `reserved`). Retired numbers are never reused (CI-2 and CF-2 are already gaps).
- Write one registry-driven rewrite tool, `tools/renumber_corpus_chapters.py`, on the model of [renumber_ci_narrative.py](../../tools/renumber_ci_narrative.py): placeholders, file renames through temporary slots, finalize, `--verify`, `--dry-run`, `--report`. It must resolve anchors by matching the real anchor set from `section_manifest.json`, not by guessing digit splits. Add a round-trip unit test: forward map then inverse map returns the original tree, including shared-id references and all original lettered file boundaries. A legacy shared chapter id without a section or file returns its destination list; it must not silently select one file.
- Add audit `CHAPTER-NUMBER-01` in report-only mode (see section 7).
- *Gate:* tool tests pass; a dry run produces a report with zero unresolved anchors.

**Phase 2: dry run and review worklist.**
- Run the tool on a scratch copy. Produce: counts of changed files and ids; every range or list expression that needs hand edits ("CI-14 to CI-27", "CF-5.7/5.9", "CS-5.11 to CS-13"); counts and ordering words ("28 CI chapters", "the next free number"); tables and Mermaid charts that sort or list ids; and every hard-coded id or file pattern in tools and tests (38 files plus the Makefile today).
- *Gate:* worklist reviewed; no pattern in the tool's "unknown" bucket.
- **Review disposition (2026-10-21):** The current report's remaining range/list candidates were checked against the registry and source headings. Dated architecture/MEMLOG entries remain historical; the CJS `5.105–5.135` oDef range and CI `6.220–6.270` domain-owner range remain valid; non-contiguous chapter families in the active planning, benchmark, and review files were expanded to explicit destination ids. The five shared legacy-id groups remain intentionally one-to-many and resolve through the crosswalk. `renumber_corpus_chapters.py --verify` reports zero unresolved legacy-id findings.

**Phase 3: migrate (one branch, separate commits).**
1. Registry and tool, plus the new audit in report-only mode.
2. File renames (`git mv` through temporary slots): corpus files and core files, including a distinct number and matching file name for each lettered corpus file (D6), and chapter ids inside `corpus_*` and the wrappers. Link targets to renamed core files are rewritten here (about 270,000 file-name occurrences in 393 files, mostly generated indexes).
3. Corpus ids and renamed-file links inside core files (about 780 corpus ids in 18 core files, plus links to core files). A separate commit so the steward can see it is id-and-link-only (see the proof in section 6). Core wording stays under steward control.
4. Operative support: `doc_architecture.md`, `ai_corpus/`, `doc_architecture/`, `project/plain_language`, `docs/`, `guides/`, tools, tests, the Makefile, workflows, the easy-entry guides, and the front doors (README, START_HERE, `llms.txt`, ANNOUNCEMENT). Trace widgets get registry numbers on chapter and part links (D13) and sub-bullets on long lines (D14), written by the tool from the registry, as a separate commit after the renumbering commits; the trace audits (NAV-TRACE-08-10, `trace_routing_prose_audit`, `ch5_trace_crosslink_audit`, `trace_dac_widget_order_audit`, `widget_top_placement_audit`) are updated for the new form. The D/A/C widgets are not changed.
5. Regenerate generated files (`make family-map-indexes`, `architecture-index`, `ai-manifest-regenerate`, the pages index, the print pack). Never hand-edit them.
6. Hand edits from the Phase 2 worklist.
- *Gate:* `make audit-report-all` matches the baseline; `make fossil-anchor-audit` and the link audits pass; no stale old id remains in the operative tree (`--verify`).

**Phase 4: verify (section 6).** Technical verification passes as recorded in section 6. Steward signoff on the core-file id-only diff remains pending.

**Phase 5: policy and docs.**
- Add a "Chapter numbering (CHAPTER-NUMBER-01)" section to [doc_architecture.md](../../doc_architecture.md): the scheme, how to add, move, retire, or split a chapter, and what to update.
- Update CONTRIBUTING, AGENTS.md (the renumbering paragraph), `ai_corpus/AI_NAVIGATION_GUIDE.md`, `ai_corpus/MAINTENANCE.md`, and the architecture move log (one dated entry with the cutoff note from D7).
- Switch `CHAPTER-NUMBER-01` to failing mode and add it to `make regression`. Retire the hard-coded one-off renumber scripts to `archive/`.
- Run `make edition-bump` and `make front-door-audit`.
- *Gate:* regression green; the edition label is new.

**D6 alignment is part of Phases 1-4.** Registry rows, file names, heading ids, section references, crosswalk entries, and review evidence must cover every formerly lettered corpus file before the migration lands. There is no deferred Phase 6. This does not authorize changes to duties or an automatic restart of section suffixes.

## 6. Verification

**Inverse comparison update (2026-10-21):** `tools/chapter_numbering_inverse_proof.py` checks 454 tracked path changes; after classifying reviewed collateral, its normalized comparisons pass. Planned collateral includes `corpus_joint_structure/cjs_reader_guide.md`, `implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md`, `implementation/PRE_PUBLICATION_SPEC.md`, `implementation/adoption/INSTITUTION_FOUNDATION_KIT.md`, `implementation/adoption/MINIMUM_VIABLE_ADOPTER.md`, `project/plans/announcement_review_inventory_2026-10-20.md`, `project/plans/ai_corpus_optimization_plan.md`, `project/plans/announcement_readiness_2026-10-20.md`, and `project/reviews/announcement_interlocks_B04_2026-10-20.md`; these carry migration-related chapter names, ids, or paths. The two implementation template renames (`GOVERNANCE_DISCLOSURE_TEMPLATE_CI8_CI26.md` to `GOVERNANCE_DISCLOSURE_TEMPLATE.md`, and `ROLE_SEPARATION_MATRIX_CI3_CI12.md` to `ROLE_SEPARATION_MATRIX.md`) are planned path changes. The checker lists 141 new untracked files separately and does not claim baseline content comparisons for those additions. No translation file was changed.

- **Content-neutral proof.** Apply the inverse map to the migrated tree and diff against the baseline tag. For the numbered core and corpus source files, expected differences are renamed files and the new `Core home:` lines; prose, headings, sections, anchors, and body text must match after reversing the approved references and D13/D14 formatting. The full-tree comparison also includes files intentionally changed by Phases 1, 3, and 5: the registry and crosswalk; migration tools, audits, tests, and Makefile wiring; policy and maintenance guidance (`doc_architecture.md`, `CONTRIBUTING.md`, `AGENTS.md`, `ai_corpus/AI_NAVIGATION_GUIDE.md`, and `ai_corpus/MAINTENANCE.md`); front doors and their edition labels; generated indexes, page output, and print pack; and the reviewed migration-reference updates in `corpus_joint_structure/cjs_reader_guide.md`, `implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md`, `implementation/PRE_PUBLICATION_SPEC.md`, `implementation/adoption/INSTITUTION_FOUNDATION_KIT.md`, `implementation/adoption/MINIMUM_VIABLE_ADOPTER.md`, `project/plans/announcement_review_inventory_2026-10-20.md`, `project/plans/ai_corpus_optimization_plan.md`, `project/plans/announcement_readiness_2026-10-20.md`, and `project/reviews/announcement_interlocks_B04_2026-10-20.md`. The two implementation template renames are planned path changes. Report these paths separately as planned changes; do not treat them as content-neutral source files. Every other tracked operative file must be byte-identical after the inverse map. Run `make core-numbering-content-proof` separately for `core_*`; it compares baseline prose after normalizing links and corpus identifiers and omitting Trace widgets, which have the independent D13/D14 check.
- **Obligation inventory.** `tools/obligation_inventory_diff.py` before and after: zero changed obligations.
- **Structure.** Section count, heading titles, and body hashes (ids normalized) match between the old and new `section_manifest.json`.
- **Links.** `local_markdown_fragment_audit`, `in_paragraph_link_audit`, `fossil_anchor_audit`, `anchor_heading_drift_audit`, `corpus_ref_name_audit`, `section-label-anchor-audit`, the external-link report, and the Pages build.
- **Trace widgets.** Undo the D13 numbers and the D14 sub-bullets (join the sub-bullets back into one semicolon-separated line) and the text must equal the pre-reformat text. Check separately from the renumbering proof.
- **Core files.** After the rename, every core file's text equals its old text except link targets and corpus ids; its heading still reads "CHAPTER SIX" and so on; the registry's ordinal name matches the heading.
- **Unique and complete.** Every chapter number is unique across layers and matches its file name, heading, and registry row; no old id survives outside the exempt files.
- **Lookup.** `corpus_lookup.py resolve CI-13.4` returns the new machine id, dotted display reference and legacy-id note. `CI-11.210 §4` and `CI-11210.4` resolve to the same source section. Formatting and parsing round-trip all registry numbers without locale-dependent decimal conversion; `retrieve`, `hydrate`, and `route` still work on the new ids.

## 7. New audit: CHAPTER-NUMBER-01

Fails when: a file name, its heading id, and its registry row disagree; the layer digit does not match the folder; the first two digits do not match the file's `Core home:` line; two chapters share a number across layers; a retired number is reused; slot sequence order differs from reading order; a file lacks the `Core home:` line; an id uses the wrong width; or formerly lettered corpus files still share a destination chapter number. It checks dotted reader-facing numbers against fixed-width machine ids using the registry display formatter. It also checks every number written in a Trace widget (D13): the number must exist in the registry and must match the file the link points to, which catches a stale link whose text and target disagree. It reads the registry, so adding a chapter means adding one row.

## 8. History and exempt files

- Exempt from rewriting (they record old numbering): `archive/`, `evidence/`, `evaluation/results/`, the crosswalk file, this plan's Appendix A, and dated entries in `TODO.md`, `project/MEMLOG.md`, and the `doc_architecture.md` move log.
- In operative history, retarget links so the link audits pass, leave the displayed old id as written, and add one cutoff note: ids before the migration entry use the old numbering; see the crosswalk.
- D12 preserves existing translation filenames during the English migration. Publish the filename crosswalk and add a note to `translations/README.md` that localized corpus ids and filenames predate the migration. Translation alignment follows the settled-chapter workflow in `project/MEMLOG.md`; this migration does not resync translation text or include existing translation work in English commits.

## 9. Risks and rollback

| Risk | Handling |
|---|---|
| Merge conflicts with other work | Freeze window; one branch; start from current `main`. |
| Anchor digit ambiguity before migration | Resolve against the real anchor set, never by digit splitting. |
| Ranges and counts silently change meaning | Phase 2 worklist; hand edits in commit 6. |
| Core files change | Separate commit, id-only proof, steward sign-off. Reopen no review batch for an id-only change. |
| Tests and tools with hard-coded ids | Found in Phase 2; update fixtures with the registry rather than regex edits. |
| Published page URLs change | Accepted pre-release; no redirects. |
| Mis-homed chapter | A move is one registry row plus a rename; the tool and audit handle it. |
| Rollback | Tag before migration; the inverse map restores the tree; the branch is not merged until Phase 4 passes. |

## 10. Schedule

Place this before the 75 family-file reviews start on November 9 ([announcement plan](announcement_readiness_2026-10-20.md)): review records, the 523-path inventory, and translation alignment should cite final ids. Suggested window: Phase 0 by October 25; Phases 1-2 by October 29; Phases 3-5 in the October 30-November 5 freeze, including D6 file alignment before the family-file reviews.

## Appendix A. Approved home and number table

All chapter homes, reading order and destination numbers are approved by the steward in sessions on 2026-10-20 and 2026-10-21. Introductory homes follow D4; the remaining groups were signed off under D3. D6 gives every lettered corpus file its own number in this migration. The table shows machine ids; reader-facing references use dots (for example, CI-0.215).

The Old id column is a legacy file label where necessary, not a substitute for source-heading inventory. In particular, `cjs_04_drafting_contracts.md`, `cjs_05_odef_parse_mechanics.md` and `cjs_06_support_hosting_classification.md` contain CJS-1 section ids despite their filename numbers. The registry and crosswalk must map each actual original file and section, not infer old ids from filenames.

| Core home | Old id | New machine id | Conf. | Title (from file name) |
|---|---|---|---|---|
| 00 | CJS-0 | CJS-00105 | Approved D4 2026-10-20 | registry and reading rules |
| 00 | CJS-1 | CJS-00110 | Approved D4 2026-10-20 | scope purpose boundary interface |
| 00 | CI-0 | CI-00205 | Approved D4 2026-10-20 | registry and reading rules |
| 00 | CI-1 | CI-00210 | Approved D4 2026-10-20 | scope purpose legitimacy interface |
| 00 | CI-26 | CI-00215 | Approved D4 2026-10-20 | compliance mapping stable registry |
| 00 | CS-0 | CS-00305 | Approved D4 2026-10-20 | registry and reading rules |
| 00 | CS-1 | CS-00310 | Approved D4 2026-10-20 | scope purpose identifier rules |
| 00 | CF-0 | CF-00405 | Approved D4 2026-10-20 | registry and reading rules |
| 00 | CF-1 | CF-00410 | Approved D4 2026-10-20 | scope authority boundary rules |
| 05 | CJS-3 (main file) | CJS-05105 | Approved 2026-10-20 | cross implementation operational terms |
| 05 | CJS-3 (`cjs_03o`) | CJS-05110 | Approved 2026-10-20 | oversight operations |
| 05 | CJS-3 (`cjs_03u`) | CJS-05115 | Approved 2026-10-20 | audit process |
| 05 | CJS-3 (`cjs_03p`) | CJS-05120 | Approved 2026-10-20 | participation operations |
| 05 | CJS-3 (`cjs_03a`) | CJS-05125 | Approved 2026-10-20 | accountability operations |
| 05 | CJS-3 (`cjs_03c`) | CJS-05130 | Approved 2026-10-20 | continuity operations |
| 05 | CJS-3 (`cjs_03i`) | CJS-05135 | Approved 2026-10-20 | integrative operations |
| 05 | CJS-5 | CJS-05140 | Approved 2026-10-20 | odef parse mechanics |
| 06 | CI-8 | CI-06205 | Approved 2026-10-21 | transparency participation accessible pathways |
| 06 | CI-10 | CI-06210 | Approved 2026-10-21 | public revenue fees recurring charges billing integrity |
| 06 | CI-11 | CI-06215 | Approved 2026-10-21 | resource stewardship incentive integrity |
| 06 | CI-15 | CI-06220 | Approved 2026-10-20 | neurodiversity disability justice trauma informed participation |
| 06 | CI-16 | CI-06225 | Approved 2026-10-20 | care labor dependent support respite care economy fairness |
| 06 | CI-17 | CI-06230 | Approved 2026-10-20 | end of life continuity memorial dignity posthumous data |
| 06 | CI-18 | CI-06235 | Approved 2026-10-20 | collective public health epidemic response addiction informed care |
| 06 | CI-19 | CI-06240 | Approved 2026-10-20 | vulnerable personal services markets (Article VII-E interface) |
| 06 | CI-20 | CI-06245 | Approved 2026-10-20 | relational coercive control intimate power anti domination |
| 06 | CI-21 | CI-06250 | Approved 2026-10-20 | community life voluntary association non instrumental time |
| 06 | CI-22 | CI-06255 | Approved 2026-10-20 | commons cooperatives mutual aid non market governance |
| 06 | CI-23 | CI-06260 | Approved 2026-10-20 | place based stewardship indigenous continuity consultation |
| 06 | CI-24 | CI-06265 | Approved 2026-10-20 | innovation reward disclosure anti enclosure |
| 06 | CI-25 | CI-06270 | Approved 2026-10-20 | scientific publication peer review replication evidence stewardship |
| 06 | CI-14 | CI-06275 | Approved 2026-10-20 | transitional governance institutional evolution |
| 06 | CS-2 Part A | CS-06305 | Approved 2026-10-20 | information types and handling |
| 06 | CS-2 Part B | CS-06310 | Approved 2026-10-20 | data classifications |
| 06 | CS-6 | CS-06315 | Approved 2026-10-20 | comprehensibility complexity stewardship |
| 06 | CS-7 | CS-06320 | Approved 2026-10-20 | justice safeguards restitution rehabilitation |
| 06 | CS-8 | CS-06325 | Approved 2026-10-20 | adaptive sustainability ecosystem resilience |
| 06 | CS-12 | CS-06330 | Approved 2026-10-20 | decentralized continuity partition resilience |
| 06 | CS-9 | CS-06335 | Approved 2026-10-20 | resource allocation funding stewardship |
| 06 | CS-13 | CS-06340 | Approved 2026-10-20 | system requirements |
| 06 | CS-5 | CS-06345 | Approved 2026-10-20 | design testing verification deployment |
| 06 | CS-10 | CS-06350 | Approved 2026-10-21 | transition constitution migration governance |
| 06 | CS-11 | CS-06355 | Approved 2026-10-21 | subversion response replacement reconstitution |
| 08 | CJS-6 | CJS-08105 | Approved 2026-10-21 | support hosting classification |
| 08 | CI-3 | CI-08205 | Approved 2026-10-21 | institutional design separation of powers |
| 08 | CI-5 | CI-08210 | Approved 2026-10-21 | conflict integrity anti capture anti corruption |
| 08 | CI-7 | CI-08215 | Approved 2026-10-21 | oversight assurance controls evidence |
| 09 | CI-9 | CI-09210 | Approved 2026-10-20 | classification linked institutional obligations |
| 09 | CS-3 Part A | CS-09305 | Approved 2026-10-20 | system classification machinery |
| 09 | CS-3 Part B | CS-09310 | Approved 2026-10-20 | system impact classifications |
| 11 | CI-27 | CI-11205 | Approved 2026-10-21 | remedy systems institutional redress capacity |
| 11 | CI-13 | CI-11210 | Approved 2026-10-21 | institutional failure dissolution |
| 11 | CI-28 | CI-11215 | Approved 2026-10-21 | institutional accountability sanctions |
| 13 | CI-6 | CI-13205 | Approved 2026-10-20 | procedure integrity contestability secondary review |
| 13 | CI-12 | CI-13210 | Approved 2026-10-20 | cross institution coordination escalation |
| 13 | CF-3 | CF-13405 | Approved 2026-10-20 | forum formation chamber structure |
| 13 | CF-4 | CF-13410 | Approved 2026-10-20 | panel formation disclosure recusal bench constitution |
| 13 | CF-5 | CF-13415 | Approved 2026-10-20 | routing operations transfer certification representative treatment |
| 13 | CF-6 | CF-13420 | Approved 2026-10-20 | appeal secondary review exhaustion pathways |
| 13 | CF-7 | CF-13425 | Approved 2026-10-20 | integrity safeguards anti capture anti self judging |
| 13 | CF-8 | CF-13430 | Approved 2026-10-20 | forum forensic analytical support |
| 13 | CF-9 | CF-13435 | Approved 2026-10-20 | independent investigative service prosecution interface |
| 13 | CF-10 | CF-13440 | Approved 2026-10-20 | technical specialist forums specialist chambers |
| 13 | CF-11 | CF-13445 | Approved 2026-10-20 | performance backlog publication accessibility |
| 13 | CF-12 | CF-13450 | Approved 2026-10-20 | forum continuity |
| 13 | CF-13 | CF-13455 | Approved 2026-10-20 | fallback operation |
| 13 | CF-14 | CF-13460 | Approved 2026-10-20 | emergency adjudication |
| 13 | CF-15 | CF-13465 | Approved 2026-10-20 | standard records forms evidence artifacts |
| 13 | CF-16 | CF-13470 | Approved 2026-10-20 | staffing reserve capacity structural records |
| 13 | `cf_sentience_status_record.md` (unnumbered) | CF-13475 | Approved 2026-10-20 | sentience-status adjudication record protocol |
| 14 | CI-4 | CI-14205 | Approved 2026-10-21 | appointment competency rotation removal |
| 14 | CS-4 | CS-14305 | Approved 2026-10-21 | critical system stewardship |
| 18 | CJS-4 | CJS-18105 | Approved 2026-10-21 | drafting contracts |
| 18 | CJS-2 | CJS-18110 | Approved 2026-10-21 | specific joint interlocks |

Capacity: 74 proposed numbered corpus files after D6 alignment and D9 inclusion; none over 19 per slot. The largest slots are CF in home 13 (15) and CI in home 06 (15). Home 06 carries 26 proposed numbered corpus files in all, which confirms Chapter Six (the Articles) is where most implementation text attaches.

## Appendix B. Scale (measured 2026-10-20)

About 24,000 corpus-id occurrences (CI about 5,900, CJS about 7,600, CS about 6,900, CF about 3,600), roughly 290 operative files outside archive, evidence, and translations, 38 tool, test, and Makefile files with hard-coded id or file patterns, and about 780 corpus ids cited from core files. About 530 distinct section ids. About 270,000 occurrences of `core_NN...` file names across 393 files (mostly generated indexes). The "Chapter X" prose in core is not touched.

## Appendix C. Approved core file mapping

Reading order inside split chapters and vignette placement were approved by the steward in session 2026-10-20 (D11). Letters are dropped from file names. The Number column uses dotted reader-facing numbers; filenames retain padded machine digits.

| Core chapter | Current file | New file | Number |
|---|---|---|---|
| 0 | core_00_preamble.md | core_00.000_preamble.md | 0.000 |
| 1 | core_01_a_values_principles.md | core_01.005_values_principles.md | 1.005 |
| 1 | core_01_b_interaction_interpretation.md | core_01.010_interaction_interpretation.md | 1.010 |
| 1 | core_01_c_stewardship_capacity_principles.md | core_01.015_stewardship_capacity_principles.md | 1.015 |
| 2 | core_02_definition_structure.md | core_02.000_definition_structure.md | 2.000 |
| 3 | core_03_definition_integrity.md | core_03.000_definition_integrity.md | 3.000 |
| 4 | core_04_burden_traceability_verification.md | core_04.000_burden_traceability_verification.md | 4.000 |
| 5 | core_05__definitions_home.md | core_05.000_definitions_home.md | 5.000 |
| 5 | core_05_apex_accountability_leg.md | core_05.005_apex_accountability_leg.md | 5.005 |
| 5 | core_05_apex_continuity_aim.md | core_05.010_apex_continuity_aim.md | 5.010 |
| 5 | core_05_apex_flourishing_aim.md | core_05.015_apex_flourishing_aim.md | 5.015 |
| 5 | core_05_apex_oversight_leg.md | core_05.020_apex_oversight_leg.md | 5.020 |
| 5 | core_05_apex_participation_leg.md | core_05.025_apex_participation_leg.md | 5.025 |
| 5 | core_05_apex_timeliness_leg.md | core_05.030_apex_timeliness_leg.md | 5.030 |
| 5 | core_05_band_accountability.md | core_05.035_band_accountability.md | 5.035 |
| 5 | core_05_band_continuity.md | core_05.040_band_continuity.md | 5.040 |
| 5 | core_05_band_integrative.md | core_05.045_band_integrative.md | 5.045 |
| 5 | core_05_band_oversight.md | core_05.050_band_oversight.md | 5.050 |
| 5 | core_05_band_participation.md | core_05.055_band_participation.md | 5.055 |
| 5 | core_05_band_performance.md | core_05.060_band_performance.md | 5.060 |
| 6 | core_06_rights_part_a.md ... part_e.md | core_06.005_rights_part_a.md ... core_06.025_rights_part_e.md | 6.005-6.025 |
| 7 | core_07_charters.md | core_07.000_charters.md | 7.000 |
| 8 | core_08_functional_independence_segregation_of_duties.md | core_08.000_functional_independence_segregation_of_duties.md | 8.000 |
| 9 | core_09_system_alignment_certification.md (index) | core_09.000_system_alignment_certification.md | 9.000 |
| 9 | core_09_a_system_alignment_certification_evaluation.md | core_09.005_system_alignment_certification_evaluation.md | 9.005 |
| 9 | core_09_b_system_alignment_certification_record_process.md | core_09.010_system_alignment_certification_record_process.md | 9.010 |
| 9 | core_09_c_system_alignment_certification_illustrations.md | core_09.015_system_alignment_certification_illustrations.md | 9.015 |
| 9 | core_09_d_institutional_alignment_certification.md | core_09.020_institutional_alignment_certification.md | 9.020 |
| 10 | core_10_standing_assessment.md | core_10.000_standing_assessment.md | 10.000 |
| 10-13 | core_10-13_application_vignettes.md (non-operative) | core_10.005_application_vignettes.md | 10.005 (D11) |
| 11 | core_11_standing_integration.md | core_11.000_standing_integration.md | 11.000 |
| 12 | core_12_a_misconduct_designation.md | core_12.005_misconduct_designation.md | 12.005 |
| 12 | core_12_b_misconduct_pattern_applications.md | core_12.010_misconduct_pattern_applications.md | 12.010 |
| 13 | core_13_forum.md | core_13.000_forum.md | 13.000 |
| 14 | core_14_governance.md | core_14.000_governance.md | 14.000 |
| 15 | core_15_non_regression.md | core_15.000_non_regression.md | 15.000 |
| 16 | core_16_expansion_supremacy.md | core_16.000_expansion_supremacy.md | 16.000 |
| 17 | core_17_amendment_ratification.md | core_17.000_amendment_ratification.md | 17.000 |
| 18 | core_18_incorporation.md | core_18.000_incorporation.md | 18.000 |

Chapters 1, 6, and 12 have no index file, so their registry number (`1.000`, `6.000`, `12.000`) names the chapter and the first part starts at `005`.
