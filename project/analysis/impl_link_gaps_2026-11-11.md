# Implementation-file links from core chapters: gap list (2026-11-11)

**Status:** working analysis, not corpus. Produced by `make impl-link-report` (`tools/impl_link_report.py`), which is report only and never fails. Re-run it for current numbers.

**How to read it.** Each implementation file (`cjs_`, `cs_`, `ci_`, `cf_`) carries a `Core home: NN` line. The report checks the core files of that chapter, using `tools/architecture/chapter_numbers.json` for the mapping, and records the best status: linked in a Trace widget, linked only elsewhere in the chapter, named by ID without a link, or not named. A file "not named in the home chapter" may still be cited by other core chapters; that case is listed apart from files that no core file names at all.

**Limits.**

- It counts markdown links to the file and literal IDs such as `CF-15.425`. A citation by title only is not seen.
- For chapters split across several core files (5, 6, 9), the status is the best across the parts, so a gap in one part can be hidden.
- A gap is not automatically a defect. Some files may be meant to be reached through a section-level link, a layer registry, or a chapter other than their home. This list is for deciding, not for fixing in bulk.
- The nine registry and scope annexes (section family 00 of each layer) are excluded; the Preamble is not expected to link them.

| Core home | Files | trace | body only | ID only | none in home chapter | of which named by no core file |
|---|---|---|---|---|---|---|
| - | 1 | 0 | 0 | 0 | 0 | 0 |
| 05 | 8 | 1 | 2 | 2 | 3 | 0 |
| 06 | 26 | 8 | 7 | 0 | 11 | 8 |
| 08 | 4 | 2 | 0 | 0 | 2 | 0 |
| 09 | 5 | 3 | 1 | 0 | 1 | 0 |
| 11 | 1 | 1 | 0 | 0 | 0 | 0 |
| 13 | 3 | 1 | 0 | 2 | 0 | 0 |
| 15 | 17 | 7 | 4 | 1 | 5 | 3 |
| 16 | 2 | 2 | 0 | 0 | 0 | 0 |
| 20 | 2 | 0 | 0 | 0 | 2 | 1 |

Totals: 69 files; trace 25, body only 14, ID only 5, none in home chapter 24 (12 named by no core file).

## Named by ID but never linked (5)

- Core home 05: CJS-5.110, CJS-5.135
- Core home 13: CI-13.210, CI-13.215
- Core home 15: CF-15.410

## Named by no core file at all (12)

- Core home 06: CI-6.225, CI-6.230, CI-6.235, CI-6.245, CI-6.250, CI-6.260, CI-6.265, CS-6.355
- Core home 15: CF-15.450, CF-15.455, CF-15.460
- Core home 20: CJS-20.105

## Not named in the home chapter, but named in other core chapters (12)

- Core home 05: CJS-5.120 (also in 2 other core files), CJS-5.130 (also in 4 other core files), CJS-5.140 (also in 1 other core file)
- Core home 06: CI-6.255 (also in 1 other core file), CS-6.320 (also in 3 other core files), CS-6.340 (also in 1 other core file)
- Core home 08: CI-8.215 (also in 3 other core files), CJS-8.105 (also in 1 other core file)
- Core home 09: CI-9.210 (also in 6 other core files)
- Core home 15: CF-15.440 (also in 3 other core files), CF-15.470 (also in 2 other core files)
- Core home 20: CJS-20.110 (also in 5 other core files)

## Linked, but not in a Trace widget (14)

- Core home 05: CJS-5.115, CJS-5.125
- Core home 06: CI-6.205, CI-6.220, CI-6.240, CI-6.270, CS-6.315, CS-6.330, CS-6.350
- Core home 09: CS-9.315
- Core home 15: CF-15.445, CF-15.465, CF-15.475, CI-15.210

## No Core home line

- corpus_joint_structure/cjs_reader_guide.md

Registry and scope annexes (not expected to be linked from the core): 9 files.

