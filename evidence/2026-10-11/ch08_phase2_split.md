# Chapter Eight: Phase II split into IIa, IIb, and IIc

**Date:** 2026-10-11
**Branch:** `restructure/ch08a-3-4-split-3-8-reorder`
**Lane:** D (core text), structure only
**Status:** Process / evidence support. This file does **not** bind. Indexes point; source binds.
**Drafting:** drafted by an AI (Claude) at the custodian's request; the custodian chose the structure and asked for it in session. Not yet reviewed as a whole.

## Problem

Part A §3.8 (*Rights-Floor and Domain Evaluations*) held about half of Part A (about 4,900 prose words after the earlier trim) and sat five levels deep (§3.8.3.1 in Part C). The §3 introduction already sorted whole-system evaluation into three tiers (always, when implicated, when triggered), but only as a table.

## Decision (custodian, 2026-10-11)

Phase II (Evaluate) becomes three sub-phases, one section each. The six phases do not change.

| Sub-phase | Tier | Before | After |
|---|---|---|---|
| **IIa** | Always | §3.1–§3.4 | §3.1–§3.4 (unchanged) |
| **IIb** | When implicated | §3.5, §3.6, §3.7, §3.7.1 | new §4 *Evaluations Where Implicated*: §4.1, §4.2, §4.3, §4.3.1 |
| **IIc** | When triggered | §3.8, §3.8.1–§3.8.6 | §5, §5.1–§5.6 |
| Part C | | §3.8.k.1 | §5.k.1 |
| Part B | | §4, 4.1–4.4, §5, §6 (6.1, 6.2), §7 (7.1, 7.1.1, 7.2, 7.3), §8 | §6, 6.1–6.4, §7, §8 (8.1, 8.2), §9 (9.1, 9.1.1, 9.2, 9.3), §10 |

Part C §3.4.8 and Sections 1 through 3.4 do not move. The §3 title stays *Whole-System Certification Evaluation*.

## Changes

1. **Scripted renumber** (`tools/ch8_phase2_split_remap.py`): one simultaneous old-to-new table, so Part B's old §4 cannot collide with the new §4. Remapped 486 links, 32 explicit anchors and 32 headings in 24 files; link labels carrying an old number were relabelled. Historical records (`archive/`, `evidence/`, `evaluation/results/`, `MEMLOG.md`, `tools/ch8_*` migration scripts, translations) were left alone, except the 2026-08 external-audit findings, which the stage-2 move also retargeted.
2. **New §4 grouping heading** with a Trace block, a plain-terms gloss, and one sentence saying it groups the evaluations that apply where implicated and adds nothing to any subsection. §3 and §5 each gained one sentence naming their sub-phase.
3. **§3 introduction:** the tier table gains a sub-phase column; the sentence before it says Phase II has three tiers, each its own section; the Subsections line points forward to §4 and §5.
4. **§1:** the "mandatory at full depth" clause for Classes A, B, and C now reads §3, §4, and §5, each as its own tier applies. CS-3's matching sentence got the same wording.
5. **Chart, tables, and blurbs** (VIS-CHART-SYNC-03): the §1.1 chart (Phase II box shows IIa, IIb, IIc; Part B node numbers +2), the six-phase tables in Part A and the reading index, the run sheet, file-top blurbs in Parts A, B, C and the index, the CH8-PROCESS-ORDER-01 table and a new *Sixth move* entry in `doc_architecture.md`, `TODO.md`, and `MINIMUM_VIABLE_ADOPTER.md`.
6. **Unnamed cites:** two Part B links and one Article cite that the renumber touched were given titles (SECTION-CITE-NAME-01, REF-ARTICLES-GLOSS).

## Review of cites of "§3 Whole-System Certification Evaluation"

120 links in 20 files. Before this move they reached all three tiers; afterwards a literal reading reaches only IIa.

- **About 100 are routing aids** (Trace "Downstream: Principles", "Read with", "Upstream: Principles" lines in Chapters One, Five, and Six). 94 of them were relabelled in a second pass the same day to "Chapter Eight §3 Whole-System Certification Evaluation through §5 Rights-Floor and Domain Evaluations", so each reaches what it reached before. Obligation diff over the 14 files touched: 2009 → 2009, matched 1:1. All regression targets pass except `lexical-vocabulary-audit` (fails identically on the unchanged tree).
- **Widened to §3, §4, and §5** (they state a duty or coverage that reaches beyond the always tier): Chapter One §15.1.1 Anti-Segmentation Principle (anti-segmentation for a jointly invoked cluster, which lives in §4.1 and §4.3); Chapter Five Oversight (class scaling of whole-system review; evaluation-coverage check); CS-3 Part A (mandatory depth by class); Part A §1 (the same clause); Part B §6 Upstream.
- **Widened to §3 and §4:** Part B §8.1 (whole-system findings include privacy, exit, assembly, and dissent findings); Part C (*Evaluation requirements illustrated here*).
- **Part B §8.2 Completeness:** added "each §4 subsection whose locus or principle is implicated" to the list of evaluations a record must cover. This restates the sentence's own opening ("any evaluation that applied") and adds no duty.
- **Retargeted to §5.5:** Chapter Five Continuity cite whose parenthetical is about *accessibility* evaluation.
- **Left on §3 although a parenthetical hints at a tier:** Chapter Five cites about "cumulative / long-horizon" effects (those factors are §3.1 and §3.2).

## Non-regression self-check (Test 1)

- **No Rights Floor narrowed.** The renumber changes no wording of any duty. Every cite that reached a duty in the moved tiers still reaches it (see above).
- **Obligation diff** over the 23 core and CS files touched since the start of this session: 3029 → 3025 obligations, 5 flags. All five are from the earlier trim of §5.x (formerly §3.8.x) and were reported then: scope-limiting disclaimers moved into the §5 introduction (see *Related*). This move adds no flag.

## Gate results

| Gate | Result |
|---|---|
| `make regression` targets (81 run one by one on a copy with the changes uncommitted, so changed-line audits see the edit) | All pass except `lexical-vocabulary-audit`, which fails identically on the unchanged tree (20 findings, same set; only line numbers differ) |
| Individually: `local-markdown-fragment-audit`, `section-label-anchor-audit` (sibling headings consecutive: 1, 2, 3, 4, 5, …), `section-cite-name-audit`, `corpus-ref-name-audit`, `article-cite-gloss-audit`, `anchor-heading-drift-audit`, `fossil-anchor-audit`, `in-paragraph-link-audit` | Pass |
| Derived artifacts | Regenerated `plain-terms-edition`, `boundary-chunks`, `ai-corpus-sync`; `ai-manifest-validate` reports valid and fresh; timestamp-only index changes reverted |
| Residual sweep | No old Part A or Part B anchor remains outside historical records; plain-text cites to old numbers in Chapter Eight files were edited by hand and checked by grep |

## Not done / for the custodian

- **Translations** stay paused: their link fragments and text still use the old numbers (and the older ones from earlier moves).
- **Proposal issue:** drafted in `ch08_phase2_split_proposal_issue.md`, not filed (the drafting session had no GitHub access to the repository). The spec change-log row (v0.29) is in `implementation/PRE_PUBLICATION_SPEC.md` §8 and names the draft; add the issue number on filing. The spec header still says "Draft v0.27" although the log reached v0.28 before this row; I left the header alone.
- **`lexical-vocabulary-audit`** already failed before this move.

## Related

- Earlier in the same session: trimmed repeated scaffolding in §3.8 (now §5) without changing numbers; the scope-limiting disclaimers it moved are the source of the five obligation-diff flags above.
