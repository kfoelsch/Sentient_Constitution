# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-09-27 — New Chapter Five term Hard Content (Def.P3):** `core_05_band_participation.md#hard-content`, placed after Expression and added to the Def.P3 member roster, the alphabetical directory, and `measurement_tier_seeds.json` (3.4 Participation). Defines the three categories (sexual or intimate; violent; severe-psychological-harm-risk) as a kind of Expression, not a lesser tier; excludes the underlying conduct and merely offensive/uncomfortable expression. Linked from Article XI-B (bullet text and D/A/C widget) and from Expression's Trace.

**2026-09-27 — Plain-language backlog cleared; XI-B hard content broken out:** All 26 `dense-guidance-sentence` findings rewritten (mostly Trace / Read-with glosses that stacked *operative*, *framing*, *context*, *orientation*): plain glosses, split sentences, section titles moved into link text; also fixed a malformed nested CI-14.1–14.3 link in XXVII-D. `make plain-language-audit` now reports none outside `_pages_site`. **Article XI-B** (*Expression*): the expression floor now lists ordinary views only and points to a new **Hard content is still expression** bullet with one sub-bullet each for sexual or intimate, violent, and severe-psychological-harm-risk expression (what stays protected; which conduct rules still govern). Old *Sensitive-content lanes* wording folded in; **Audience routing for hard content** is now its own bullet. No rule changed.

**2026-09-27 — Open items cleared; full `make regression` green:** Article VI gained the standard Two Aims / Tetrad / *material stake* framing (ch1-ch6 alignment now PASS). Lexical fixes: `core_09` §2.1 *breaches* → *violates*; IX-D *people* → *others*. The five unmigrated apex heads (Flourishing; Accountability, Oversight, Participation, Timeliness legs) moved from letter O/M/A/C under a `####` heading to the guidepost form Continuity already used — wording unchanged; explicit `#flourishing`, `#oversight`, `#participation`, `#timeliness` anchors kept so old links resolve (ch5-omac-format-audit now PASS). Legacy Chapter One "§11.4" citations in CJS-3.4/3.7/3.12/3.13/3.14/3.22/3.23 (the old stewardship-override subsection, now folded into §11.1) repointed to §11 in `cjs_03*.md` and `tools/ch1_cjs3_alignment_audit.py`. CI-19 renamed `ci_19_vulnerable_personal_services_markets_article_viie_interface.md`.

**2026-09-27 — Institutional secularism moved to Chapter One §18.2:** The *Secular constitution and institutional neutrality* rules formerly in **Article XI-A** are now **[Chapter One §18.2 Institutional Secularism and Worldview Neutrality](../core_01_c_stewardship_capacity_principles.md#182-institutional-secularism-and-worldview-neutrality)**, wording unchanged. XI-A keeps the individual freedom plus a one-line pointer to §11.4; §5's downstream range now runs through §5.5. (§5.5 rather than §11.4 because legacy bare "§11.4" Chapter One citations were still live in CJS-3 — since repointed to §11.)

**2026-09-27 — Articles X and XI restructured; X-G split; old XI-C moved to VII-E; new Chapter Five term:** Article X is retitled *Self-Determination, Agency, and Participation* and now holds only **X-A** (*Agency and Freedom from Manipulation*), **X-B** (*Governance Participation and Voting Entitlement*; was X-C, rewritten in plain language), **X-C** (*Stakeholder Role and Participation Rights*; was X-B, now also holding the independent-audit bullet and the stakeholder-lock rule), and **X-D**. Article XI is retitled *Conscience, Expression, Association, and Cooperative Interaction* and now runs **XI-A** (*Freedom of conscience, religion, and comparable worldview*; was X-F), **XI-B** (*Expression*), **XI-C** (*Press and Journalistic Activity*), and **XI-D** (*Assembly, Dissent, and Peaceful Protest*) — XI-B–XI-D split from old X-G, whose limitations, anti-chilling, and scope disciplines now sit in XI-B and apply to XI-C and XI-D; `#x-g-*` protest anchors are now `#xi-d-*` — then **XI-E** (*Institutional Formation and Business Creation*; was X-E), **XI-F** (*Non-Imposition and Consent in Association*; was XI-A), and **XI-G** (*Collective Harm Boundary and Enforcement Interface*; was XI-B). Old **XI-C** (*Adult consensual commercial sexual services and sexual exploitation*) is now **VII-E**. Old X-G citations were routed by topic to XI-B, XI-C, or XI-D. Article X neighbors now list Chapter One §7 Freedom. New Chapter Five Integrative term **Documented Legitimacy Mechanism** (seeded in `measurement_tier_seeds.json`, linked from X-B, Chapter Thirteen §1, and Constitutional Contract Layer). IDs and anchors rewritten across the English corpus, tools, and generated indexes; archive/, evidence/, translations/, and this log's older entries were left as-is.

Earlier session narratives (2026-06-15 through 2026-09-26: Chapter Six restructures, link and archive cleanups, Pages build, reader entry pages, new Chapter Five terms, segregation of duties, seat catalog, evaluation follow-ups) are in [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md).

## Standing Decisions

**Translations paused (editor decision, 2026-09-23):** Translations under [translations/](../translations/) may fall out of date while the English edit pass continues; do not resync after each English change. The English numbered `core_*` files govern. At the restart, resync fully against the English source. Known gaps: translated files still use pre-renumbering chapter filenames (e.g. `translations/es/core_07_system_alignment_certification.md` holds Chapter Eight), which accounts for nearly all remaining broken links in the repo; translated text still uses the published-edition article labels (only links into English files were re-anchored). Chapter Six has been renumbered several times since; the old → new label mapping is in the 2026-09-25 through 2026-09-27 entries of [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md). Translation lane: [CONTRIBUTING.md](../CONTRIBUTING.md#lane-f).

**Pages build:** `_pages_site/` is a local preview only; CI rebuilds it on each deploy. `make pages-deploy-gate` runs in `pages.yml` before every build; `.github/workflows/checks.yml` runs `make regression` on every push and PR. Do not list "Regenerated `_pages_site`" in editing passes. **Open:** switch **Settings → Pages → Source** to *GitHub Actions* before the announcement.

**Reader entry pages:** **README** is the one public door for all readers (timed reading paths at `README.md#reading-paths`); **START_HERE** is the start page for would-be adopters and operators; [guides/CONCEPTUAL_OVERVIEW.md](../guides/CONCEPTUAL_OVERVIEW.md) is the second-step big-picture map.

**Link rules:** Binding corpus links only by relative path or `#fragment` (LINK-OFF-CORPUS-15, `make external-link-audit`) and never deep-links into a README section (SUPPORT-DOC-POINTER-01). A pasted `https://file+.vscode-resource.vscode-cdn.net/…` link is the VS Code Markdown preview rewriting a correct relative link, not corpus text.

**Warning:** `tools/emit_regression_scenarios.py` is stale against the hand-maintained [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](CONSTITUTIONAL_REGRESSION_SCENARIOS.md) (running it drops rows and flips draft/pass). Do not run it until its catalog is resynced.

## Active Threads

**Regression:** full `make regression` green as of 2026-09-27.

**Evaluation:** I1 (human evidence) remains open in [TODO.md](TODO.md); resolved follow-ups are in [archive/TODO_RESOLVED_2026-09-17.md](../archive/TODO_RESOLVED_2026-09-17.md).

**Regression scenarios:** `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` is present; active validation and dated evidence publication remain deferred unless reinstatement is requested. Open P1 path in [TODO.md](TODO.md).

**Architecture process:** [doc_architecture.md](../doc_architecture.md) remains the stable ownership and editing map. Optional AI corpus follow-ups remain in [plans/ai_corpus_optimization_plan.md](plans/ai_corpus_optimization_plan.md).

## Archive Index

- **2026-09-27 prune:** [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md)
- **Architecture process (canonical):** [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md) — see [README.md](../README.md)
- **2026-06-18 Chapter Five closeout:** [archive/MEMLOG_SNAPSHOT_2026-06-18.md](../archive/MEMLOG_SNAPSHOT_2026-06-18.md), [archive/TODO_SNAPSHOT_2026-06-18.md](../archive/TODO_SNAPSHOT_2026-06-18.md)
- **2026-05-01 root retirement:** [archive/MEMLOG_ROOT_RETIRED_2026-05-01.md](../archive/MEMLOG_ROOT_RETIRED_2026-05-01.md), [archive/TODO_ROOT_RETIRED_2026-05-01.md](../archive/TODO_ROOT_RETIRED_2026-05-01.md)
- **Older MEMLOG/TODO snapshots:** removed 2026-06-17; retrieve from git history if needed

## Operating Rule

Add new session entries above the archive index only when they carry forward current context, decisions, verification status, or next actions. For detailed closure narratives, create a dated archive snapshot and leave a one-line pointer here.

Standard closeout order: commit substantive corpus/source changes first; then snapshot active meta files (`TODO.md`, `MEMLOG.md`, and living worklists) into `archive/`; then slim the active meta files to pointers and current open work.
