<!--
DRAFT — not corpus. Working plan under project/plans/ (AGENTS.md: drafts and WIP under project/).
-->

# Core reorganization plan

**Date:** 2026-11-20. **Asked for by:** the custodian ("if you agree, please begin a plan … Please evaluate").

**What this plan covers.** The custodian named five changes:

1. Chapter Eight §11 *Independent Bodies* becomes its own chapter.
2. The three office drafts stop repeating the standard Independent Body rules.
3. The Preamble splits into two chapters.
4. The forum intake process moves from the core into the forum corpus.
5. The pipeline chapters keep a summary in the core, with their detail moved into the corpus.

This plan evaluates each change, proposes an order, and lists the choices the custodian needs to make. Nothing has moved yet.

---

## 0. The rule every move must follow

The biggest risk in this plan is moving a guarantee out of the core by accident.

**Why it matters.** Under [Preamble §9](../../core_00.000_preamble.md#9-adopted-implementation-corpus) and [Chapter Thirty-One](../../core_31.000_incorporation.md), the core binds every adopter. The corpus binds only when an adopter incorporates it, and it is amended by a different route. Text moved from the core to the corpus therefore becomes adoption-dependent and easier to change.

**Proposed test (to be written into `doc_architecture.md` as a placement rule before step 4):** a sentence stays in the core if it does any of the following:

- grants, limits, or protects a right or a standing effect;
- names who decides, who checks, or who may contest;
- sets a floor, a ceiling, an outer bound, or a time bound that a sentient can rely on;
- bars a practice; or
- says what happens when a duty is not met.

A sentence moves to the corpus only if it says *how* a duty in the core is carried out, such as forms, steps, record fields, staffing patterns, worked sequences, and routing tables. Everything that moves keeps a one-line core pointer, and the core keeps the outcome the corpus text must reach.

---

## 1. Independent Bodies as their own chapter

**Evaluation: agree.** §11 is about 2,800 of Chapter Eight's 9,600 words, nearly 30 percent of the chapter. It is a different subject from the four-seat rule. Its rules are about to be cited by five chapters (finance, information, monetary, debt, and bank supervision).

**Placement choice (decision A):**

- **A1 (recommended now): Chapter Eight Part B.** Put the section in a new file `core_08.010_independent_bodies.md` as *Chapter Eight, Part B: Independent Bodies*. This is the pattern Chapters One, Six, Nine, and Fourteen already use, so no other chapter is renumbered, and the part tooling (`tools/architecture/chapter_numbers.json`, PART-CITE-CHAPTER-01) already supports it.
- **A2: a new numbered chapter (Chapter Nine), renumbering Chapters Nine to Thirty-One.** This is cleaner to read, but it rewrites every cite and anchor to twenty-three chapters, the chapter-number tooling, and the paused translations.

**Recommendation.** Take A1 now. Do a single renumbering pass later, once we know where the five office chapters go, because placing them will force a renumbering anyway (see decision D). Renumbering once is far cheaper than renumbering twice.

**Steps under A1:**

- move §11 verbatim into the new file, with its own Trace, purpose, and plain-terms lines;
- split it into numbered subsections (designation; independence and appointment; protected funding; information, audit, and open decisions; conflicts and market-moving information; scaling);
- leave a pointer and the old anchor in Chapter Eight;
- rewrite the 33 links to `#11-independent-bodies` in 8 files, update the owner register in Preamble §4, and add the chapter-number entry;
- run preflight and the full audit.

## 2. Leaner office drafts

**Evaluation: agree, and it is cheap.** Each draft still restates material that Chapter Eight now owns:

- its own "Independent Body" bullet lists;
- *No dual roles* paragraphs that partly repeat the general rule;
- general purpose language in the audit, funding, and scaling sections.

**Proposed shape for every office chapter:** one short *Designation* section that names the office an Independent Body and lists only:

- what it does;
- its seats;
- its competency gate;
- what *Market-moving information* covers for it; and
- any rule stricter than the general one.

After that come only the office's own substance, such as the target, the fiscal rule, licensing, or the confidence ladder. Audit, funding, reserve, shortfall, and scaling sections shrink to their office-specific lines or disappear.

**Do it right after step 1**, so the drafts can point at the new Part's subsection anchors instead of at one long section.

## 3. Splitting the Preamble

**Evaluation: agree.** The Preamble does two jobs. Its first 1,500 words say what the Constitution is for (*What Systems Reward*, §1 *The Model*, and §2 *Measurements Overview*). The remaining 5,500 words (§3 to §9) are a map of the whole Constitution: governance, the owner register, the separation map, the pipelines, process ownership, change, and the corpus.

**Proposed split (decision B):**

- **Preamble** keeps the purpose: *What Systems Reward*, *The Model*, and *Measurements Overview*. This is the text a first-time reader should meet.
- **A new "Constitutional Map" chapter** takes §3 to §9: the owner register, the four-seat map, the pipelines, process ownership, change, and the corpus. It sits at `core_00.010_constitutional_map.md` so no chapter is renumbered.

**Cost.** Anchors in the Preamble are among the most linked in the corpus, such as `#constitutional-tetrad`, `#material-stake`, and the owner register. Most of the heavily linked definitions are in §1 and stay put. The owner-register and pipeline anchors move and need a link rewrite.

## 4. Forum intake into the corpus

**Evaluation: agree in part.** Chapter Twenty-Three §3.2 *Primary-Stakes Routing and Intake* (about 1,800 words with §3.3 and §3.4) and §4.1 *Intakes* mix two kinds of text:

- **Stays in the core** (rights and outcomes): the right to file and be heard; the primary-stakes test; the rule that characterization must be in good faith; the lead-forum rule and the bar on self-judging; the time bounds on initial access; and the routing asymmetry that protects the weaker party.
- **Moves to the corpus** (how): the intake triage desk's operating steps, the routing sequence at filing, the default venue table, the special routing rules, and the intake record fields. The natural home is **CF-23.415** (*Routing operations, transfer, certification, and representative treatment*), which already holds routing operations.

This step is the **pilot** for the placement test in section 0. Do it before step 5, and review the result together before scaling up.

## 5. Summaries of the pipeline chapters

**Evaluation: agree with the direction, with care.** Chapters Nine to Twenty-Four hold about 150,000 words. Much of it is procedure that fits the corpus, and the corpus already has matching files for most of these chapters:

- Chapter Ten has 20 related corpus files, Chapter Twenty-Three 19, Chapter Twenty 11, and Chapter Twenty-One 10.
- Chapters Sixteen, Seventeen, and Eighteen have none yet.

But these chapters also hold many of the Constitution's strongest protections for individuals, such as fault before a violation record, honest error, silence by default, anti-aggregation, and contest routes. Those must stay in the core under section 0.

**Proposed approach:**

- **Shape of each pipeline chapter after the change:**
  - purpose and plain terms;
  - the guarantees (the section 0 test);
  - who holds each seat;
  - the outcomes and the records they produce;
  - contest routes and time bounds; and
  - a pointer table to the corpus files that carry the procedure.
  
  The target is a core chapter of a third to a half of its present length.
- **One chapter per move, smallest first.** Start with Chapter Eighteen (2,500 words) to prove the shape. Then do the certification triplets (Chapters Nine to Fourteen), where the corpus already carries most of the procedure. Leave Chapters Fifteen, Sixteen, and Nineteen (standing assessment, measurement, and violation consequences) for last, because they hold the densest protections.
- **New corpus files** where none exist (Chapters Sixteen to Eighteen), numbered under the existing CJS or CI families.
- **A guarantee check for each chapter:** before and after each move, list every guarantee sentence and confirm that each one is still in the core or is quoted there. The list goes in the move log.

**Decision C:** whether the summary chapters keep their current numbers and file names (recommended: yes, so anchors to retained guarantees do not break), or become a single "Pipeline Overview" chapter with the detail spread across the corpus. I recommend keeping each chapter, shortened, because the pipeline order is itself a protection (no step skipped), and one chapter per stage keeps that order visible.

---

## Proposed order

| Step | Work | Size | Depends on |
|---|---|---|---|
| 0 | Write the core-or-corpus placement test into `doc_architecture.md` | small | — |
| 1 | Independent Bodies to Chapter Eight Part B (A1) | medium | decision A |
| 2 | Lean office drafts | small | step 1 |
| 3 | Preamble split | medium | decision B |
| 4 | Forum intake to CF-23.415 (pilot of the placement test) | medium | step 0 |
| 5 | Pipeline chapters, one at a time, starting with Chapter Eighteen | large | step 4 reviewed; decision C |
| 6 | One renumbering pass, placing the office chapters and any new chapters | large | decision D |

Each step is its own move, with preflight and the full audit, and an archive and merge at the custodian's call.

## Decisions for the custodian

- **A.** Independent Bodies as Chapter Eight Part B now (recommended), or a new numbered chapter with an immediate renumbering.
- **B.** Split the Preamble into *Preamble* (purpose) and *Constitutional Map* (the map of the whole), as above, or another split.
- **C.** Keep each pipeline chapter, shortened (recommended), or merge them into one overview chapter.
- **D.** Later: where the five office chapters sit (for example, as a group after Chapter Twenty-Seven *Governance*, or as parts of one "Public Offices" chapter), which sets the final renumbering.
