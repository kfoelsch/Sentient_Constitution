# MEMLOG

## Purpose

Session memory log for current project context, decisions, and next actions. Keep this file lean; archive detail snapshots rather than carrying full session history forward.

## Current State

**2026-10-07 — Sibling audit modes given one owner map:** The CJS-3.3 owner map now names an owner for each sibling audit mode: complexity audits (CS-6.3, Article XXIII-B), steward assurance reviews (CS-4.8, CS-4.11), claim verification (CJS-3.5), continuous audit (CS-5 ACA), plus the two record audits. The Chapter 5 SAC definition, Article XVI, and Chapter 8 Part A §1 use the same names. No new Chapter 5 definitions. See [evidence/2026-10-07/audit_modes_owner_map.md](../evidence/2026-10-07/audit_modes_owner_map.md).

**2026-10-07 — Chapter Eight Part B §7.1: new record item for concerns raised in the decision:** The record must now carry every objection, dissent, concern, and challenge raised in review or in reaching the outcome, with who raised it, how it was resolved or why it stays open, and any condition, reliance limit, or reopening trigger it produced (also stated in §6 and the Completeness paragraph). The one operative change since the reorder, and a new obligation. Wording needs the steward's sign-off before release. See [evidence/2026-10-07/ch08_record_decision_concerns.md](../evidence/2026-10-07/ch08_record_decision_concerns.md). Also: Part A §1 sibling-audit-modes closing bullet rewritten in plain language. §5.2 now states one record throughout: step 4 renamed "Integration for decision", new step 6 "Decision and completing the record", and a matching sentence in the §7 introduction; phase tables and chart say the record is opened at the start and completed in Phase V. Each recertification, and each reopened or fresh review, opens a new linked record (new §8 paragraph "New record for each pass", §7.1 item "Prior record", §7.2 versions wording, §5.2 step 1 "for each"). New obligation; steward sign-off on wording.

**2026-10-07 — Chapter Eight: Record moved after Decide; Operate phase added (pre-announcement):** Six phases now: I Frame (§2, §3), II Evaluate (§4), III Review (§5), IV Decide (§6 Certification Outcomes, from old §7 and §7.1), V Record (§7, from old §6), VI Operate (§8 Recertification and Reopening with §8.1 and §8.2, from old §7.2–§7.3; §9 Relationship to Standing, from old §8). Wording unchanged; obligations conserved. Rule CH8-PROCESS-ORDER-01 in [doc_architecture.md](../doc_architecture.md#chapter-eight-process-order-ch8-process-order-01); map and verification in [evidence/2026-10-07/ch08_record_after_decide.md](../evidence/2026-10-07/ch08_record_after_decide.md).

**2026-10-07 — Chapter Eight reordered into process order (pre-announcement):** Sections now run in five phases: I Frame (§2 class, §3 challenging a certification), II Evaluate (§4: always §4.1–§4.4, when implicated §4.5–§4.7, when triggered §4.8), III Review (§5), IV Record (§6), V Decide and keep current (§7–§8). The challenge path moved from Part B to Part A §3; the contestability chain stays at Part B §5.3. Reader aids added: five-phase chart and table, §4 tier table, hub run sheet, record checklist, recognition-status table. Wording unchanged; obligations conserved. Rule CH8-PROCESS-ORDER-01 in [doc_architecture.md](../doc_architecture.md#chapter-eight-process-order-ch8-process-order-01); map and verification in [evidence/2026-10-07/ch08_process_order_reorder.md](../evidence/2026-10-07/ch08_process_order_reorder.md).

**2026-10-01 to 2026-10-03 — Chapter One reorganized; Chapter Five and wording passes:** Continuity principles relocated within Part A, then numbering smoothed (§1 purpose; §2–§7 Flourishing; §8–§12 Continuity; Part B §§13–15; Part C §§16–20), with Part A opened by a reader map and two Mermaid-charted aims introductions. Cites repaired across CJS, Chapter Five, `evaluation/`, and `project/`. Chapter Five gained Duty to Resist, Constitutional No-Bypass, and Standardization; "reasonably effective/well" is banned in the Necessity and safer-alternative tests (`lexical-vocabulary-audit` passes). Steward boxes were removed from the core (steward cards now carry the next step). Closed items: [archive/TODO_RESOLVED_2026-10-03.md](../archive/TODO_RESOLVED_2026-10-03.md). Open follow-ups, including translation resync and `make ai-manifest-regenerate`, are in [TODO.md](../TODO.md).

Earlier session narratives (2026-06-15 through 2026-09-27: Chapter Six restructures, Articles X and XI restructure, institutional secularism move, Hard Content term, plain-language backlog, link and archive cleanups, Pages build, reader entry pages, new Chapter Five terms, segregation of duties, seat catalog, evaluation follow-ups) are in [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md) and [archive/MEMLOG_SNAPSHOT_2026-10-03.md](../archive/MEMLOG_SNAPSHOT_2026-10-03.md).

## Standing Decisions

**Chapter Eight order (editor decision, 2026-10-07):** Chapter Eight sections follow the order the certification work is done. New sections go in the phase where the work happens, not at the end of a file. Renumbered before the announcement so no redirect anchors are needed later.

**Translations paused (editor decision, 2026-09-23):** Translations under [translations/](../translations/) may fall out of date while the English edit pass continues; do not resync after each English change. The English numbered `core_*` files govern. At the restart, resync fully against the English source. Known gaps: translated files still use pre-renumbering chapter filenames (e.g. `translations/es/core_07_system_alignment_certification.md` holds Chapter Eight), which accounts for nearly all remaining broken links in the repo; translated text still uses the published-edition article labels (only links into English files were re-anchored). Chapter Six has been renumbered several times since; the old → new label mapping is in the 2026-09-25 through 2026-09-27 entries of [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md). Translation lane: [CONTRIBUTING.md](../CONTRIBUTING.md#lane-f).

**Pages build:** `_pages_site/` is a local preview only; CI rebuilds it on each deploy. `make pages-deploy-gate` runs in `pages.yml` before every build; `.github/workflows/checks.yml` runs `make regression` on every push and PR. Do not list "Regenerated `_pages_site`" in editing passes. **Open:** switch **Settings → Pages → Source** to *GitHub Actions* before the announcement.

**Reader entry pages:** **README** is the one public door for all readers (timed reading paths at `README.md#reading-paths`); **START_HERE** is the start page for would-be adopters and operators; [guides/CONCEPTUAL_OVERVIEW.md](../guides/CONCEPTUAL_OVERVIEW.md) is the second-step big-picture map.

**Link rules:** Binding corpus links only by relative path or `#fragment` (LINK-OFF-CORPUS-15, `make external-link-audit`) and never deep-links into a README section (SUPPORT-DOC-POINTER-01). A pasted `https://file+.vscode-resource.vscode-cdn.net/…` link is the VS Code Markdown preview rewriting a correct relative link, not corpus text.

**Warning:** `tools/emit_regression_scenarios.py` is stale against the hand-maintained [CONSTITUTIONAL_REGRESSION_SCENARIOS.md](CONSTITUTIONAL_REGRESSION_SCENARIOS.md) (running it drops rows and flips draft/pass). Do not run it until its catalog is resynced.

## Active Threads

**Regression:** full `make regression` green as of 2026-10-03 (after fixing list-intro colons in Chapter One §7.2/§7.3 and seeding Subversion).

**Evaluation:** I1 (human evidence) remains open in [TODO.md](../TODO.md); resolved follow-ups are in [archive/TODO_RESOLVED_2026-09-17.md](../archive/TODO_RESOLVED_2026-09-17.md).

**Regression scenarios:** `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` is present; active validation and dated evidence publication remain deferred unless reinstatement is requested. Open P1 path in [TODO.md](../TODO.md).

**Architecture process:** [doc_architecture.md](../doc_architecture.md) remains the stable ownership and editing map. Optional AI corpus follow-ups remain in [plans/ai_corpus_optimization_plan.md](plans/ai_corpus_optimization_plan.md).

## Archive Index

- **2026-10-03 prune:** [archive/MEMLOG_SNAPSHOT_2026-10-03.md](../archive/MEMLOG_SNAPSHOT_2026-10-03.md)
- **2026-09-27 prune:** [archive/MEMLOG_SNAPSHOT_2026-09-27.md](../archive/MEMLOG_SNAPSHOT_2026-09-27.md)
- **Architecture process (canonical):** [archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_PRIMER_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_ADOPTION_APPENDIX_ARCHIVED_2026-05-08.md), [archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md](../archive/ARCHITECTURE_WORKLIST_ARCHIVED_2026-05-08.md) — see [README.md](../README.md)
- **2026-06-18 Chapter Five closeout:** [archive/MEMLOG_SNAPSHOT_2026-06-18.md](../archive/MEMLOG_SNAPSHOT_2026-06-18.md), [archive/TODO_SNAPSHOT_2026-06-18.md](../archive/TODO_SNAPSHOT_2026-06-18.md)
- **2026-05-01 root retirement:** [archive/MEMLOG_ROOT_RETIRED_2026-05-01.md](../archive/MEMLOG_ROOT_RETIRED_2026-05-01.md), [archive/TODO_ROOT_RETIRED_2026-05-01.md](../archive/TODO_ROOT_RETIRED_2026-05-01.md)
- **Older MEMLOG/TODO snapshots:** removed 2026-06-17; retrieve from git history if needed

## Operating Rule

Add new session entries above the archive index only when they carry forward current context, decisions, verification status, or next actions. For detailed closure narratives, create a dated archive snapshot and leave a one-line pointer here.

Standard closeout order: commit substantive corpus/source changes first; then snapshot active meta files (`TODO.md`, `MEMLOG.md`, and living worklists) into `archive/`; then slim the active meta files to pointers and current open work.
