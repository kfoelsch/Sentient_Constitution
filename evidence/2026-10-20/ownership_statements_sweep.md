# Ownership statements swept across the corpus: implementation note (2026-10-20)

Status: done, uncommitted, on branch `docs/ownership-statements-sweep` (cut from `main`). Logged as the Sixty-sixth move in `doc_architecture.md`. No operative duty changed. Translations were not touched.

## Request (custodian)
CI-13 opens with "This file is the institutional implementation home for CI-13 (Institutional failure and dissolution)." That is an ownership statement. Sweep the corpus for places where one is missing or not clearly stated, and resolve.

## The two standards that already existed
- **Core chapters, OWNER-OPENING-01:** `Chapter <N> is the constitutional owner of **<domain>**.` Split chapters use `Chapter <N>, Part <X>, is …`. It is binding operative prose, visible without expanding a widget, placed after the file-top widgets and any chapter Trace and before the *In plain terms* gloss.
- **Adopted implementation files, NAV-IMPL-SUBFILE-01:** `This file is the <layer> implementation home for **<ID>** (*<name>*).`

## What the sweep found (every `core_*`, CJS, CS, CI, and CF file)
| Finding | Files | Fix |
| --- | --- | --- |
| Missing visible owner line | Preamble; Chapter One Parts A, B, C; Chapter Five hub; Chapter Six Parts B to E | Added in the standard form. Preamble claim is new (see open items) |
| Held only in a collapsed widget, or only as "holds" | Chapter Five: 6 apex files, Continuity and Integrative bands (Oversight, Participation, and Accountability bands said "owns" in the body but not first) | Visible `Chapter Five, <name>, is the constitutional owner of …` first line; "do not duplicate leg-head O/M/A/C" kept |
| Registry annexes had no owner sentence | `cf_00`, `ci_00`, `cs_00`, `cjs_00` | Added after the file-top widgets (the widget-top audit requires that placement) |
| Index or illustration files that own nothing did not say so | Chapter Nine reading index; Chapter Nine Part C; Chapters Ten to Thirteen vignettes | Visible "owns no rule" line naming the owning chapters or parts |
| Off the standard wording | Chapter Ten ("owns"); CS-2 and CS-3 Parts A and B ("**CS-2** … owns") | Standard formula; Chapter Ten keeps its Question 1 / Question 2 split and the Question 3 pointer |
| Owner line after the gloss or inside the first section | Chapters Ten and Eleven; CS-4 | Moved ahead |
| One ID spans several files and the owner line did not say what each holds | CS-5 and CS-5 Part A (since split into CS-5 and CS-13); CJS-1 (`cjs_01` vs `cjs_04`, `cjs_05`, `cjs_06`); CJS-3 hub (claimed all of CJS-3, holds CJS-3.0 and CJS-3.1); CJS-3.3 (`cjs_03o` vs `cjs_03u`) | Each file says what it holds and points to the others |
| Wrong section name in the owner line | `cjs_04` (CJS-1.7), `cjs_06` (CJS-1.9), CI-19 (title twice) | Heading names used. The same wrong names were cited in 11 places in nine files and were corrected too |
| Already clear, left alone | `cf_sentience_status_record.md` ("designated implementation text", Chapter Five's own term); `cjs_reader_guide.md` (says it is reader guidance only); all other CI, CF, CS, and CJS-2 files | none |

## Rules added to `doc_architecture.md`
OWNER-OPENING-01 gained "Part files, band files, and files that own nothing". NAV-IMPL-SUBFILE-01 gained "Owner sentence rules".

## Decisions and open items
1. **Preamble claim: confirmed by the steward (2026-10-20).**
2. **CS-5 name: resolved the same day.** 46 citations called CS-5 "User-facing capability surfaces" while the family map named it *Design, testing, verification, and deployment* and gave the first title to CS-5 Part A. The steward found the two-title situation poor. Resolved by splitting the family: CS-5 is now *System lifecycle* and Part A is CS-13 *System requirements*. On reading the citations, 74 carried the Part A label and nearly all pointed at lifecycle sections, so they were relabelled rather than retargeted; 8 moved to CS-13. See `evidence/2026-10-20/cs13_system_requirements_split.md` (Sixty-seventh move).
3. **Audit: built.** `make owner-line-audit` (`tools/owner_line_audit.py`, tests in `tools/test_owner_line_audit.py`, 23 cases). Core files need one visible claim line (`is the constitutional owner of` with a bold domain, or `owns no rule` for the three listed files) before the first gloss and section, naming the right chapter and Part, once. Implementation subfiles need the "implementation home for" sentence before the first `##` heading, with the right layer word and ID prefix, claimed IDs that are headings in the same file, and no ID claimed by two files. Two files are listed exceptions with the sentence each must keep. It is registered in `audit_registry.json` (category layout; its test under tests), in `rule_registry.json` (OWNER-OPENING-01), in the `make regression` list, and in the rule table in `doc_architecture.md`. Its first run flagged the Constitutional Performance band (fixed) and two over-strict checks in the audit itself (bold domain in a list under the line; "own no rule" for the vignettes), which were relaxed.
4. Chapter Six Part A keeps its chapter-level line and does not name "Part A" (the one listed exception in the audit).

## Verification
- `make audit-report`: 105 targets (103 plus the audit and its test); all pass after `make ai-corpus-sync` except `ch1-cjs3-alignment-audit` from this computer's folder (below). Earlier, an `make audit-report-all` added a 2026-10-20 run of the alignment evidence family, so the retention rule (keep the newest two runs) wants to delete the 2026-10-04 run. That makes `ch1-cjs3-alignment-audit` fail from this computer's connected folder, where deletion is off (the other 104 targets pass). Where deletion works it prunes and passes; it passes in a scratch copy.
- Four derived files regenerated because the source text moved lines: `doc_architecture/generated/boundary_chunks.json`, `plain_terms_edition.json`, `print_pack.md`, `rights_floor_sheet.json`. Their `-check` targets pass.
- Out-of-gate audits compared with a pristine copy of `HEAD`: the same ones fail before and after (plain-language, readability, front-door freshness, translations). The alignment and relocation audits pass in a scratch copy. From this computer's connected folder, targets that prune old evidence fail because file deletion is switched off there; that is not a corpus failure.
- `make audit-report-all` wrote new untracked files under `evidence/2026-10-20/`; delete them if you do not want them. `ch1_cjs3_audit_log_2026-10-20.json` was restored to its committed content.
