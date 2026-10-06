# Chapter Eight: data-type floors for every CS-2 type, and §3 restructure

**Date:** 2026-10-06
**Branch:** `docs/ch08-data-type-floors-and-s3-renumber` (cut from `main` at `41678b5f`)
**Lane:** D (core text) with Lane A/E housekeeping
**Status:** Process / evidence support. This file does **not** bind. Indexes point; source binds.
**Drafting:** drafted by an AI (Claude) at the custodian's request; reviewed turn by turn by the custodian in session, not yet reviewed as a whole.

## Problem

1. **Type-N-only floor.** Chapter Eight §3.2 (*Privacy (Informational) Joint Invocation*) preserved only the **Type N** floor (for **Article VII-B**). CS-2 now has eleven types (E, G, O, H, I, N, S, Y, W, U, T), each with its own handling duties; proper handling is required across all of them. §3.8 *Privacy discipline* and the Def.C3 type lists in Chapter Five also stopped at Type S, omitting Type Y (which names privacy homes) and the creator-works types W, U, and T.
2. **Misplaced §3.7.** Part A §3.7 (*Illustrative whole-system application by class*) was a stub in the middle of §3 — a pointer to Part C plus a "Reading across classes" paragraph whose rule already lives in §2 and §2.1 and whose examples duplicate Part C *Reclassification*. The pointer to the worked examples sat at the bottom of the §3 intro.
3. **Plain-language drift.** The §3.6 plain-terms gloss said "four basics" instead of the Tetrad; one §3.2 bullet on privacy-vs-disclosure trades was hard to read.

## Changes by finding

| # | Finding | Change | Where |
|---|---|---|---|
| 1 | Type-N-only floor in the privacy joint-invocation factor | *Type-N floor preserved* → **Type floors preserved**: the factor narrows no applicable CS-2 type; each type's posture, duties, and privacy homes apply in full; most-protective-governs under CS-2 Part A §2; meeting one type does not discharge another. Locus → type map (VII-A → I; VII-B and X-A → N; IX → I, H, Y and onward W/U/T with reserved rights; XIV-A → S). Bulleted rule that open/audit types keep embedded H/I/N handling, that privacy alone does not justify withholding Type O or Type E beyond their own hold-backs, and that a real privacy-vs-disclosure conflict is decided openly and on the record under CS-2 Part A §7 | `core_08_a` §3.2 |
| 2 | §3.8 privacy discipline stopped at Type S | Adds **Type Y**; adds a certification check for **Type W, U, T** works: withdrawal of a public release, limits of each recorded grant, the creator's reserved rights, and no grant treated as consent to an unnamed use | `core_08_a` §3.7 (was §3.8) |
| 3 | Def.C3 type lists stopped at Type S | Adds **Type Y** (carrying into W, U, T) to the Read-with line and the operational-alignment line | `core_05_band_continuity` Privacy (Informational) |
| 4 | "Four basics" | Now "the four legs of the Tetrad" (linked to its Preamble definition), each leg named beside its question | `core_08_a` §3.6 plain-terms gloss |
| 5 | Part A §3.7 stub mid-§3 | Stub deleted. Early pointer to Part C placed directly under the §3 plain-terms gloss; old bottom-of-intro pointer removed; trace entries retargeted to Part C | `core_08_a` §1, §3 |
| 6 | "Reading across classes" for §3.1–§3.6 | Moved to the end of Part C's whole-system walkthrough, rewritten in plain language as a lead-in and three bullets (one per example system), pointing to Part A §2.1 for the rule | `core_08_c` |
| 7 | Part C whole-system section numbered after a Part A section that no longer exists | Unnumbered, like *Class profiles* and *Reclassification* (anchor `#illustrative-whole-system-application-by-class-non-exhaustive`); index table, class-profile table, plain-terms lead-ins and file blurb updated | `core_08_c` |
| 8 | Numbering gap left by finding 5 | **Renumber:** Part A §3.8 → **§3.7** (and §3.8.1 → §3.7.1); §3.9 → **§3.8** (and every §3.9.N / §3.9.N.1 → §3.8.N / §3.8.N.1). Headings, anchors, link fragments and visible "Chapter Eight §3.x" cites updated in Parts A–C and in Chapters Five and Six, CS-2, CS-3 and the Chapter Eight index | 11 core files, 3 CS files |
| 9 | Untitled cites on lines touched by the renumber | 34 section-number cites given titles (SECTION-CITE-NAME-01); Article glosses on 4 lines via `tools/apply_article_cite_gloss.py` | `core_08_a`, `core_08_b`, `core_05_band_continuity`, CS-3 Part A |

## Non-regression self-check (Test 1)

- **No Rights Floor narrowed.** Finding 1 generalizes a floor (Type N → every applicable type) and keeps Type N/VII-B named explicitly. Findings 2–3 add types to existing lists.
- **Obligation diff** ([obligation_inventory_diff_ch08_type_floors_s3.json](obligation_inventory_diff_ch08_type_floors_s3.json)), 14 core/CS files, 2016 → 2015 obligations, 4 flags:
  - `core_08_a` **DROPPED or WEAKENED PROHIBITION** ("A Class A survival-critical system must not be downclassified…") and `core_08_c` **ADDED PROHIBITION / ADDED DUTY**: one item **moved**, not dropped (finding 6). The rule also stands in Part A itself: §2 requires the System Classification Record to show the **highest class that applies** under current conditions and treats keeping an old class label after conditions change as a defect; §2.1 requires a system whose real role outgrows its class to be reclassified and re-evaluated.
  - `core_08_a` **ADDED DUTY** (Type W/U/T creator-control check): intended (finding 2). It adds certification burden only where those types are in scope, and implements duties CS-2 Part B §9.9–§9.13 already set.
- **The renumber changes no wording of any duty**; only section labels and link targets move.

## Gate results

| Gate | Result |
|---|---|
| `make regression` (77 targets) | Run on clean exports of `41678b5f` and of this branch. Three failures, all **identical to HEAD** in output: `ch5-measurement-coverage-audit`, `prose-continuity-audit`, `lexical-vocabulary-audit`. All other targets pass, including `reference-audit`, `local-markdown-fragment-audit`, `section-cite-name-audit`, `corpus-ref-name-audit`, `article-cite-gloss-audit`, `anchor-heading-drift-audit`, `fossil-anchor-audit`, and `in-paragraph-link-audit` |
| Link-label consistency (session script) | Every link into Parts A and C shows the same section number as the heading it lands on; no links to removed anchors remain outside `archive/`, `evidence/`, `evaluation/results/`, and old `tools/ch8_*` migration scripts |
| `translation-link-audit` | Output identical to HEAD (pre-existing findings only) |
| Readability (touched Chapter Eight files) | Part A 20.49 → 20.57; Part B 16.58 → 16.83 (mostly titled link text, finding 9); Part C 16.78 → 16.77; Chapter Five continuity band unchanged |
| Derived artifacts | Regenerated `ai-corpus-sync`, `architecture-index`, `plain-terms-edition`, `reader-accessibility`, `boundary-chunks`; timestamp-only changes reverted |

## Environment note

Regression ran on clean exports because the working folder holds untracked "`… 2.md`" sync duplicates that macOS will not let the tools read (`Resource deadlock avoided`); `make regression` in place fails on them regardless of content. Those files were not touched.

## Not done (needs the custodian)

- **Proposal issue** before the pull request (Lane D entry), and the spec change-log line on merge.
- **Translations:** link fragments retargeted only; their text keeps the old §3.8/§3.9 numbers and the Type-N-only wording until the translation restart.
- **Other Part A stubs** (§3.7.1 and §3.8.N.1) keep the same pointer-plus-"Reading across classes" pattern that §3.7 had; the same restructure could apply to them.
- **The "`… 2.md`" duplicates** in the working folder should be reviewed and removed so regression can run in place.
