# Resolved TODO items — archived 2026-10-01

This archive records the completed checklist items removed from the active [TODO.md](../TODO.md) on 2026-10-01, grouped by their original section. Normative meaning remains in the binding corpus; this file is a process-history record. The 2026-09-27 section below was already superseded and is kept whole.

## 2026-10-01 — Principle term alignment: simplification candidates

- [x] **Constraint label** done 2026-10-01: Safety (Constraint) is now Safety (Constitutional Constraint); anchors unchanged. Still open: whether to align the §3.1 and §3.2 heading parentheticals ("Harm Constraint", "Epistemic Integrity Constraint").
- [x] **Materiality and Foreseeability** done 2026-10-01: definitions retitled from Materiality Determination and Foreseeability Diligence; anchors unchanged.

## 2026-10-01 — Chapter One principles and Chapter Five definitions: already covered

- [x] **§10.5 Duty to Resist.** The record (Attributable Action), the protection (Protected Reporting, Good Faith) and the steward (Stewardship) are defined. The refusal duty itself has no Chapter Five home. Decide whether it is a leaf of the Stewardship cluster (**Def.C2**) or stays principle-owned with Chapter Ten §5.4 and CS-4 §10. Done 2026-10-01: Chapter Five entry added (accountability band).
- [x] **§8.1 Constitutional No-Bypass.** Cited by only three generic definitions (Accountability, Auditability, Contestability). No-bypass appears as one list item under Authority Stack and Internal Hierarchy. Decide whether it needs its own entry or an explicit sentence in the Authority Stack definition. Pair with the Process definition item in the 2026-09-30 section below. Done 2026-10-01: Chapter Five entry added (integrative band); a future Process definition can cite it.
- [x] **Materially Binding Act is cited by no principle widget.** The audit lists it, Documented Legitimacy Mechanism, and Heightened Scrutiny as definitions no principle cites. Materially Binding Act's own Trace points to §11.2, but §11.2's widget does not list it, so the link runs one way. Likely fix: add it to §11.2's Definitions · Assessment · Compliance widget. Decide separately whether the other two need a Chapter One citation. Done 2026-10-01: row added to the §11.2 widget.

## 2026-09-30 — Operative steward boxes removed from the core

- [x] **Remove all 15 boxes and their anchors.** Done 2026-09-30. The "Steward door (non-operative)" lines now point at the card.
- [x] **Add the four sentences.** Article XIII-A (adopted implementation text cannot close challenge, review, or redress); Chapter Nine §3.1 (privacy and opacity are not a standing-measurement exemption); Chapter Twelve §6 anti-delay floor (a met throughput target is not timely while harm continues); Chapter Eight Part B §14.2 (the challenge path opens when the system first has stakeholders; pilots expected at every class).
- [x] **Rework the lockstep audit, schema, and lookup tool.** The audit now diffs each card's owner pointer and next step against the index; `corpus_lookup.py` hydrates the owner text and the card (`door_owner`, `steward_card`) instead of the box.
- [x] **Article V-B.** Done 2026-09-30: added the floor sentence that adequacy is judged on currently mapped flows and no allocation formula is a precondition; collapsed the certification-procedure bullets (verify, how, when) into a pointer to Chapter Eight §6. Article V-A done the same day: kept "What must be mapped", recast complete/current/auditable/backed-by-evidence as "What the maps must be", collapsed the when/verify/how bullets into one "How certification checks it" pointer to Chapter Eight §6, and pointed hiding-defect consequences to Chapter Eight §6 and §16.

## 2026-09-17 — Conceptual overview and corpus alignment follow-ups

- [x] **Complete source coverage.** Extend the thematic review into a tracked review of remaining core, definition, and adopted-implementation provisions. Record what was actually read and checked; identify translation and implementation coverage separately. Recheck findings against current source before claiming complete alignment. Initial inventory and audit disposition: [source coverage record](evidence/2026-09-17/source_coverage_2026-09-17.md).

## 2026-09-14 — Nested-list readability pass (remaining chapters)

- [x] **Remaining numbered chapters** — Preamble; Chapters One through Four; Chapters Fifteen through Sixteen (including split files: Chapter One Parts A–C). For each: extend the candidate finder, run the ranked scan, nest only parallel checklists, then re-scan nested children and nest only parallel subbullets. Out of scope unless separately requested: adopted layers (`corpus_*`), `core_09-12_application_vignettes.md`, and implementation/adoption pages.

## P1 — Regression And Evidence

- [x] **P1 — Validate regression scenarios and evidence workflow:** reconcile the present `CONSTITUTIONAL_REGRESSION_SCENARIOS.md` file with the `evidence/<YYYY-MM-DD>/` workflow so matrix integrity, snapshot validation, and dated artifact recording resume as an active process.

## Superseded section (kept whole)

### 2026-09-27 — Move operative steward statements out of reader-facing text

*Superseded 2026-09-30: the boxes were removed.* Operative steward statements (Owner / Forbidden move / Clock boxes) are steward routing content, not reader-facing constitutional text. Put each one in a collapsed widget (`<details>` with a blue "Operative steward statement" summary, the same pattern as the Trace and Definitions widgets), not in a bare blockquote in the article body. [Chapter One Part B](core_01_b_interaction_interpretation.md) already does this; use it as the model.

- [x] **Wrap every bare box in a widget.** Done 2026-09-27: all 16 boxes are now in collapsed widgets. Generated plain-terms, reader-accessibility, and boundary-chunk outputs were regenerated.
- [x] **Keep the audit anchors.** Leave each `<a id="operative-steward-statement-…">` anchor and the `**Operative steward statement.**` text as they are, so `tools/steward_door_lockstep_audit.py` and the `implementation/steward_owner_clock_index.json` hrefs still resolve. Re-run the audit after the change.
- [x] **Keep binding substance in the article.** When a box states something the article body does not (for example, the Contest rule that the bar is fixed now rather than later; the general rule that lower text cannot narrow the Rights Floor already lives in the Authority Stack), make sure the article body still carries it before the box goes behind a widget. Done 2026-09-27: reviewed all 16 boxes. Each applies rules stated in its owning section to a steward's next step; the boxes stay operative text inside their widgets, so collapsing them removes nothing binding. No additions needed.
- [x] **Make the Steward door pointers consistent.** Make the "Steward door (non-operative)" pointer lines the same across doors, or move them into the same widget. Done 2026-09-27: removed the eleven same-unit pointers (the box now sits in the adjacent widget); the four cross-file pointers (Chapter One §9.1 → XXII-A, Chapter Five Auditability → XV, Chapter Five Cross-System Contribution → IV-B, Chapter Twelve §6 → XXV-C) share one format.
