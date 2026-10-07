# Chapter Eight: record of concerns raised in the decision (2026-10-07)

Architectural rule: **CH8-PROCESS-ORDER-01** in [doc_architecture.md](../../doc_architecture.md#chapter-eight-process-order-ch8-process-order-01). Follows [ch08_record_after_decide.md](ch08_record_after_decide.md).

## Why

The record now follows the decision (Phase V after Phase IV). That lets it capture what was raised on the way to the outcome, but the minimum record contents did not require it. This change makes it a requirement.

## What changed

This is a new obligation, unlike the two reorders before it. Wording below is a draft for the steward's sign-off.

- **Part B §7.1, new record item** (before "Outcome and reliance limits"): *Concerns raised in review and decision* - every objection, dissent, concern, and challenge raised during forum review or in reaching the outcome, whether by a forum component, a member of the deciding body, a steward or operator, or an affected party through a challenge path, stating for each who raised it and what was raised; how it was resolved, or why it remains open; and any condition, reliance limit, or reopening trigger it produced.
- **Part B §7.1, Completeness paragraph:** a record is also incomplete if it omits a concern, objection, or dissent raised in review or in reaching the outcome, including one that did not change the outcome.
- **Part B §6:** the decision must state its outcome on the record *together with the concerns raised in reaching it*; plain-terms line extended to match.
- **Part B §7 Trace:** §6 added upstream; the stale downstream label for §6 replaced by §8 (recertification and reopening).
- **Hub record checklist:** one row added (Review and Decide).

## Also in this change (wording only)

- **Part A §1:** the last bullet under the sibling audit modes now reads "You can still run any of these checks on their own, without going through certification. Certification doesn't replace them."

## Not done

- Translations are not updated (translations paused; they follow the next re-sync).
- The §5.2 supervisory sequence still lists "Record integration" as step 4 before the decision. It reads as the lead forum keeping one working record through review; the Phase V record is the finished file. Worth a look if the steward wants the two to match.

## Verification

Run on a clean copy of tracked files (stray " 2.md" duplicates in the working folder make several audits fail with "Resource deadlock avoided").

- Passing: `local-markdown-fragment-audit`, `section-label-anchor-audit`, `fossil-anchor-audit`, `anchor-heading-drift-audit`, `widget-top-placement-audit`, `reference-audit`, `doc-architecture-section-audit`, `prose-continuity-audit`, `lexical-vocabulary-audit`, `plain-terms-edition-check`, `boundary-chunks-check`. `section-cite-name-audit` passes on the working folder (it needs git).
- `tools/obligation_inventory_diff.py` over Chapter Eight Parts A, B, C and the hub, against `origin/main`: 295 clauses before and after; one ADDED DUTY flag, the new §6 sentence ("...together with the concerns raised in reaching it"). That flag is the intended new obligation. Nothing else differs.
- Regenerated: `doc_architecture/generated/plain_terms_edition.md`, `plain_terms_edition.json`, `boundary_chunks.json`.
