<!--
DRAFT — not corpus. Working plan under project/plans/ (AGENTS.md: drafts and WIP under project/).
-->

# Core reorganization plan

**Date:** 2026-11-20, revised the same day after the custodian's second and third rounds.

**Asked for by:** the custodian. The first round said: "if you agree, please begin a plan … Please evaluate". The second round said:

> "We're going to be doing a massive renumbering anyway. Now is the time to split chapters. As far as the corpus not being binding, there are several relatively easy fixes for that. Two are: we make the corpus binding, or we come up with a new category of file, like 'sub-core' that is still binding like the core, but outside of the core files. We want the core files to be relatively accessible to sentients. … chunking it down will help readers process it."

The third round settled the open decisions:

> "E subcore is clearer to average readers than schedule … F Chapter one stays one chapter. My intent was to put a list of the independent institutions in the core in the new chapter on them, and then have each institution's file in the subcore so we don't drown readers in that detail. B I think we split the preamble after section 3. That way the rest becomes an overview and an ownership guide."

**Goal.** Make the core something a sentient can actually read, while every guarantee stays as binding and as hard to change as it is now.

**What this plan covers:**

- a new binding tier of files outside the core;
- one renumbering, done now, that also splits:
  - Chapter Eight §11 *Independent Bodies* into its own chapter;
  - the Preamble into two chapters;
  - the five public offices, listed in the Independent Bodies chapter, with each office's full text in the subcore;
- forum intake and the pipeline detail, moved out of the core;
- leaner office texts.

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

### Option 2: a new binding tier outside the core (adopted)

Add a tier with the same force as the core, kept in separate files, called the **subcore** (decision E: the custodian chose *subcore* over *Schedules* as clearer to most readers). Each subcore file sits at the repository root beside the core, named `subcore_<chapter>.<nnn>_<slug>.md`, so it sorts next to its chapter and the tooling can find it the way it finds `core_*` files.

The rules for the tier:

- **Same force.** A subcore file is part of the Constitution. It binds every adopter, as the core does, without separate incorporation.
- **Same amendment route.** A subcore file changes only by amendment under Chapter Twenty-Nine, with the same heightened review for rights-affecting changes.
- **Attached to a chapter.** Each subcore file belongs to one core chapter and is named for it (for example, *Subcore 16-A: Measurement Procedure*). The chapter lists its subcore files.
- **Core states, subcore details.** The core states every guarantee in plain words, at least in one line. The subcore gives the full rule and procedure. A subcore file may not narrow its chapter. Where the two seem to differ, the reading more protective of the affected sentient controls, and the gap is a drafting defect to fix.
- **The corpus stays as it is.** It remains adopter-shaped implementation that binds as adopted, for what may properly vary between adopters.

That gives three tiers, and a three-way placement test for every sentence:

| Tier | What goes there |
|---|---|
| **Core** | Purpose, plain-terms explanation, and one line for every guarantee: rights, who decides and who can contest, floors and bounds, bars, and consequences. It is written to be read. |
| **Subcore** | The full text of guarantees and procedure that must be the same for every adopter: detailed tests, sequences, seat placements, record contents, and tables the core cites. It is written to be relied on. |
| **Corpus** | Implementation that may properly differ between adopters: staffing, forms, templates, sharing arrangements, worked examples, and reference methods. It is written to be adopted. |

**What the tier needs before any content moves:**

- the [Chapter Five *Corpus*](../../core_05.045_band_integrative.md#corpus) entry and the *Corpus and Authority Stack* definitions;
- [Preamble §9](../../core_00.000_preamble.md#9-adopted-implementation-corpus), the owner register, and the [Chapter Thirty §4.1](../../core_30.000_expansion_supremacy.md#41-internal-hierarchy-for-adopters) hierarchy;
- Chapter Twenty-Nine (amendment covers the subcore);
- Chapter Thirty-One (the subcore needs no separate incorporation);
- `README.md`;
- the audit tooling: every audit that scans "binding text" must scan `subcore_*` files too, and the chapter-number tooling must know them.

## 3. Renumbering now: agree

One renumbering is cheaper than two. We can do it now, splitting what needs splitting, and placing the five office chapters in the same pass. The renumbering is mechanical but large:

- every chapter cite and anchor;
- `tools/architecture/chapter_numbers.json`, which already records an `old_id` for earlier renumberings;
- file names, owner registers, and the AI corpus indexes.

The translations are paused, so they will be re-synced later rather than edited now.

**New outline (decisions F and B; numbers illustrative until the renumbering pass):**

| New | Content | From |
|---|---|---|
| Preamble | What the Constitution is for: *What Systems Reward*, *The Model*, *Measurements Overview*, *Governance and Stewardship* (about 2,850 words) | Preamble opening and §1–§3 |
| 1 | **Constitutional Map**: an overview and ownership guide: principles, definitions and rights; charters and separation of duties; the pipelines; process ownership and the owner register; change and incorporation; the three tiers (about 4,500 words) | Preamble §4–§9 |
| 2–5 | Values and principles (Chapter One stays one chapter, in its five files), definition structure and integrity, burden and traceability | Chapters One to Four |
| … | Definitions, rights, charters | Chapters Five to Seven |
| … | Functional independence and separation of duties | Chapter Eight §1–§10 |
| … | **Independent Bodies**: the general rules for every body, and a list of the bodies the Constitution creates, with each one's purpose and a one-line statement of each guarantee it gives sentients | Chapter Eight §11, and the office drafts |
| … | Pipeline chapters, each shortened, with subcore files | Chapters Nine to Twenty-Four |
| … | Enforcement, special enforcement, governance | Chapters Twenty-Five to Twenty-Seven |
| … | Non-regression, amendment, supremacy, incorporation | Chapters Twenty-Eight to Thirty-One |

**How the offices are placed (decision F).** The five office drafts (Finance, Information, Monetary, Debt, Bank Supervision; about 21,000 words together) do not become core chapters. Each becomes one subcore file attached to the Independent Bodies chapter, for example *Subcore IB-M: Public Monetary Office*. The chapter's list gives each office a short entry (purpose, who it answers to, and one line for each guarantee that protects sentients directly), so a reader learns what each office promises without reading its operating rules. Examples of such one-line guarantees:

- Monetary: no direct financing of government; cash stays available; a digital currency keeps payments private.
- Debt: every public obligation is published, including guarantees; debt already lawfully issued is paid first; a procedural limit never causes a missed payment.
- Bank Supervision: protected deposits are paid within a set time; owners and creditors bear losses before public money does.
- Information: published findings carry a stated confidence rung.
- Finance: funding floors, and how shortfalls are shared.

The list also says how a body is added: a body the Constitution requires of every adopter is added by amendment, with its file in the subcore; a body an adopter creates on its own follows the chapter's general rules and lives in the corpus.

The general rules now in Chapter Eight §11 are about 2,770 words. They stay whole in the new chapter, since every body relies on them and they are short enough to read.

**How the Preamble splits (decision B).** The Preamble keeps its opening and §1–§3; §4–§9 become the *Constitutional Map*. One adjustment I recommend: move §3.2 *Key Governance Processes* into the Map beside §6 *Key Practical Process Pipelines*, because it lists the same pipelines; §3.1 (measurements in governance) and §3.3 (governance layers) stay in the Preamble. About 7,700 links point into the Preamble; the renumbering pass rewrites the ones whose sections move.

## 4. What moves into subcore files (after the renumbering)

These are listed in order of reading benefit:

1. **Chapter Five definitions bands (about 170,000 words).** This is the biggest win. Each definition keeps a short entry in the core: the term, a one-sentence meaning, and its anchor. The full entry, with its Trace, tests, and distinctions, moves to a definitions subcore file. Most links point at the short entry's anchor and keep working.
2. **Pipeline chapters (Nine to Twenty-Four).** Each chapter keeps its purpose, plain terms, a one-line statement of each guarantee, the seats, the outcomes, contest routes, and time bounds, plus a list of its subcore files. Detailed tests and sequences go to the chapter's subcore files; procedure that may vary goes to the corpus. One chapter per move, smallest first (Chapter Eighteen). Standing and violations (Chapters Fifteen, Sixteen, and Nineteen) come last.
3. **Forum intake.** Chapter Twenty-Three keeps the right to file, the primary-stakes test, good-faith characterization, the time bounds, and the routing asymmetry. The triage desk's steps, the routing sequence, the default venue table, and the special routing rules move to a Chapter Twenty-Three subcore file. They become subcore text, not corpus text, because the venue table decides who hears a case and must not vary between adopters.
4. **Independent Bodies.** The general rules stay whole; the office texts go to the subcore when the chapter is created (step 3).

**Guarantee check for every move.** Before and after each move, list each guarantee sentence and confirm that it is either still in the core or stated there in one line, with the full text in a subcore file. Record the list in the move log.

## 5. Office texts

Each office's subcore file shrinks to:

- a short *Designation* section with only what is special to that office; and
- the office's own substance.

Do it as each office text moves into the subcore, so it points at the Independent Bodies chapter's anchors.

## Proposed order

| Step | Work | Size | Depends on |
|---|---|---|---|
| 1 | Write the three-tier placement test into `doc_architecture.md` | small | none |
| 2 | Create the subcore tier: amend Chapters Five, Twenty-Nine, Thirty, Thirty-One, the Preamble, and the README, and extend the tooling | medium | step 1 |
| 3 | Split the chapters (the Preamble and Constitutional Map, and Independent Bodies) and put the office texts in the subcore | medium | step 2 |
| 4 | One renumbering pass | large | step 3 |
| 5 | Lean office texts | small | step 4 |
| 6 | Forum intake to a Chapter Twenty-Three subcore file (pilot) | medium | steps 2 and 4 |
| 7 | Definitions bands to a definitions subcore | large | step 6 reviewed |
| 8 | Pipeline chapters, one at a time | large | step 6 reviewed |

Each step is its own move, with preflight and the full audit, and an archive and merge at the custodian's call. Steps 3 and 4 run back to back in one session, with `work` held, because a half-renumbered tree breaks every cite.

## Decisions

All settled by the custodian on 2026-11-20:

- **A and C** (second round): split into new chapters now; shorten each chapter, with the detail in the subcore.
- **E**: Option 2, named *subcore*.
- **F**: Chapter One stays one chapter. The public offices are listed in the Independent Bodies chapter, each with its full text in the subcore.
- **B**: the Preamble splits after §3; the rest becomes the *Constitutional Map*. Open only in detail: whether §3.2 moves to the Map (recommended above).
