<!--
DRAFT — not corpus. Working plan under project/plans/ (AGENTS.md: drafts and WIP under project/).
-->

# Core reorganization plan

**Date:** 2026-11-20, revised the same day after the custodian's second round.

**Asked for by:** the custodian. The first round said: "if you agree, please begin a plan … Please evaluate". The second round said:

> "We're going to be doing a massive renumbering anyway. Now is the time to split chapters. As far as the corpus not being binding, there are several relatively easy fixes for that. Two are: we make the corpus binding, or we come up with a new category of file, like 'sub-core' that is still binding like the core, but outside of the core files. We want the core files to be relatively accessible to sentients. … chunking it down will help readers process it."

**Goal.** Make the core something a sentient can actually read, while every guarantee stays as binding and as hard to change as it is now.

**What this plan covers:**

- a new binding tier of files outside the core;
- one renumbering, done now, that also splits:
  - Chapter Eight §11 *Independent Bodies* into its own chapter;
  - the Preamble into two chapters;
  - the five office chapters, which get placed;
- forum intake and the pipeline detail, moved out of the core;
- leaner office drafts.

Nothing has moved yet.

---

## 1. Where things stand

| Layer | Files | Words | Binding |
|---|---|---|---|
| Core | 53 `core_*` files | about 556,000 | binds every adopter. It changes only by amendment under Chapter Twenty-Nine. |
| Corpus | 85 files in four corpora | about 284,000 | binds only as adopted. Chapter Thirty-One makes each corpus file "binding **only as adopted** through a recorded adoption chain", pinned by edition. |

The core is far too long to read. The six band files of Chapter Five alone hold about 170,000 words, almost a third of the core, and the pipeline chapters (Nine to Twenty-Four) hold about 150,000 more.

## 2. The two fixes the custodian named

### Option 1: make the whole corpus binding

**For:**

- one change to Chapter Thirty-One and the Chapter Five *Corpus* entry;
- no new kind of file.

**Against:**

- **It freezes what should flex.** Much of the corpus is meant to vary between adopters by scale and setting: staffing patterns, forms, worked examples, record templates, sharing arrangements. Making it all binding everywhere would put every form field under the heightened amendment review of Chapter Twenty-Nine. A small adopter could not adapt any of it.
- **It turns illustrations into law.** The corpus mixes requirements with vignettes, worked examples, and reference methods, which were never written to bind.
- **It does not separate guarantees from procedure.** A reader still could not tell which corpus sentences protect them.

### Option 2: a new binding tier outside the core (recommended)

Add a tier with the same force as the core, kept in separate files. I suggest calling it **Schedules**, the term many constitutions and statutes use for attached text with the same legal force as the main body. "Sub-core" also works; the name is decision E.

The rules for the tier:

- **Same force.** A schedule is part of the Constitution. It binds every adopter, as the core does, without separate incorporation.
- **Same amendment route.** A schedule changes only by amendment under Chapter Twenty-Nine, with the same heightened review for rights-affecting changes.
- **Attached to a chapter.** Each schedule belongs to one core chapter and is named for it (for example, *Schedule 16-A: Measurement Procedure*). The chapter lists its schedules.
- **Core states, schedule details.** The core states every guarantee in plain words, at least in one line. The schedule gives the full rule and procedure. A schedule may not narrow its chapter. Where the two seem to differ, the reading more protective of the affected sentient controls, and the gap is a drafting defect to fix.
- **The corpus stays as it is.** It remains adopter-shaped implementation that binds as adopted, for what may properly vary between adopters.

That gives three tiers, and a three-way placement test for every sentence:

| Tier | What goes there |
|---|---|
| **Core** | Purpose, plain-terms explanation, and one line for every guarantee: rights, who decides and who can contest, floors and bounds, bars, and consequences. It is written to be read. |
| **Schedule** | The full text of guarantees and procedure that must be the same for every adopter: detailed tests, sequences, seat placements, record contents, and tables the core cites. It is written to be relied on. |
| **Corpus** | Implementation that may properly differ between adopters: staffing, forms, templates, sharing arrangements, worked examples, and reference methods. It is written to be adopted. |

**What the tier needs before any content moves:**

- the [Chapter Five *Corpus*](../../core_05.045_band_integrative.md#corpus) entry and the *Corpus and Authority Stack* definitions;
- [Preamble §9](../../core_00.000_preamble.md#9-adopted-implementation-corpus), the owner register, and the [Chapter Thirty §4.1](../../core_30.000_expansion_supremacy.md#41-internal-hierarchy-for-adopters) hierarchy;
- Chapter Twenty-Nine (amendment covers schedules);
- Chapter Thirty-One (schedules need no separate incorporation);
- `README.md`;
- the audit tooling: every audit that scans "binding text" must scan the schedules folder too, and the chapter-number tooling must know schedules.

## 3. Renumbering now: agree

One renumbering is cheaper than two. We can do it now, splitting what needs splitting, and placing the five office chapters in the same pass. The renumbering is mechanical but large:

- every chapter cite and anchor;
- `tools/architecture/chapter_numbers.json`, which already records an `old_id` for earlier renumberings;
- file names, owner registers, and the AI corpus indexes.

The translations are paused, so they will be re-synced later rather than edited now.

**Proposed new outline (decision F; numbers illustrative until approved):**

| New | Content | From |
|---|---|---|
| Preamble | What the Constitution is for: *What Systems Reward*, *The Model*, *Measurements Overview* | Preamble opening and §1–§2 |
| 1 | **Constitutional Map**: governance overview, owner register, four-seat map, pipelines, process ownership, change, the tiers | Preamble §3–§9 |
| 2–9 | Values and principles (now Chapter One's five files, possibly as separate chapters), definition structure and integrity, burden and traceability | Chapters One to Four |
| … | Definitions, rights, charters | Chapters Five to Seven |
| … | Functional independence and separation of duties | Chapter Eight §1–§10 |
| … | **Independent Bodies** | Chapter Eight §11 |
| … | Pipeline chapters, each shortened, with schedules | Chapters Nine to Twenty-Four |
| … | Enforcement, special enforcement, governance | Chapters Twenty-Five to Twenty-Seven |
| … | **Public offices**: Finance, Information, Monetary, Debt, Bank Supervision | new drafts |
| … | Non-regression, amendment, supremacy, incorporation | Chapters Twenty-Eight to Thirty-One |

**Open questions in the outline:**

- Should Chapter One's five files become five chapters?
- Should the public offices be five chapters, or one chapter with five parts? I recommend five chapters, placed together after Governance, because each is long and each is cited on its own.

## 4. What moves into schedules (after the renumbering)

These are listed in order of reading benefit:

1. **Chapter Five definitions bands (about 170,000 words).** This is the biggest win. Each definition keeps a short entry in the core: the term, a one-sentence meaning, and its anchor. The full entry, with its Trace, tests, and distinctions, moves to a definitions schedule. Most links point at the short entry's anchor and keep working.
2. **Pipeline chapters (Nine to Twenty-Four).** Each chapter keeps its purpose, plain terms, a one-line statement of each guarantee, the seats, the outcomes, contest routes, and time bounds, plus a list of its schedules. Detailed tests and sequences go to the chapter's schedules; procedure that may vary goes to the corpus. One chapter per move, smallest first (Chapter Eighteen). Standing and violations (Chapters Fifteen, Sixteen, and Nineteen) come last.
3. **Forum intake.** Chapter Twenty-Three keeps the right to file, the primary-stakes test, good-faith characterization, the time bounds, and the routing asymmetry. The triage desk's steps, the routing sequence, the default venue table, and the special routing rules move to a Chapter Twenty-Three schedule. They become schedule text, not corpus text, because the venue table decides who hears a case and must not vary between adopters.
4. **Independent Bodies.** The chapter is short enough to stay whole for now.

**Guarantee check for every move.** Before and after each move, list each guarantee sentence and confirm that it is either still in the core or stated there in one line, with the full text in a schedule. Record the list in the move log.

## 5. Office drafts

**Unchanged from the first round: agree, and it is cheap.** Each office chapter shrinks to:

- a short *Designation* section with only what is special to that office; and
- the office's own substance.

Do it right after the Independent Bodies chapter exists, so the drafts point at its subsection anchors.

## Proposed order

| Step | Work | Size | Depends on |
|---|---|---|---|
| 1 | Write the three-tier placement test into `doc_architecture.md` | small | decision E |
| 2 | Create the schedule tier: amend Chapters Five, Twenty-Nine, Thirty, Thirty-One, the Preamble, and the README, and extend the tooling | medium | step 1 |
| 3 | Approve the new outline | small | decision F |
| 4 | Split the chapters (the Preamble and Constitutional Map, and Independent Bodies) and place the office chapters | medium | step 3 |
| 5 | One renumbering pass | large | step 4 |
| 6 | Lean office chapters | small | step 5 |
| 7 | Forum intake to a Chapter Twenty-Three schedule (pilot) | medium | steps 2 and 5 |
| 8 | Definitions bands to a definitions schedule | large | step 7 reviewed |
| 9 | Pipeline chapters, one at a time | large | step 7 reviewed |

Each step is its own move, with preflight and the full audit, and an archive and merge at the custodian's call. Steps 4 and 5 run back to back in one session, with `work` held, because a half-renumbered tree breaks every cite.

## Decisions for the custodian

- **E.** The binding tier: Option 2 (recommended), and its name (*Schedules* or *sub-core*).
- **F.** The new outline (section 3). It needs two choices:
  - whether Chapter One's five files become separate chapters;
  - where the public offices go, and whether they are separate chapters (recommended) or one chapter.
- **B.** The Preamble split into *Preamble* and *Constitutional Map* (unchanged from the first round).

Decisions A (Part B or a new chapter) and C (shortened chapters or one overview) from the first round are settled by the custodian's second round: split into new chapters now, and shorten each chapter, with the detail in schedules.
