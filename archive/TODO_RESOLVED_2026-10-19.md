# Resolved TODO items — archived 2026-10-19

This archive records completed narrative removed from the active [TODO.md](../TODO.md) on 2026-10-19, kept verbatim and grouped by its original section. The open follow-ups stay in TODO.md under each heading. Normative meaning remains in the binding corpus; this file is a process-history record.

## 2026-10-13 — Institutional alignment certification (Chapter Nine Part D): drafted on a branch, signed off by the steward 2026-10-13

Evaluation: [institutional-alignment-certification-evaluation](../evidence/2026-10-13/institutional_alignment_certification_implementation.md) (project doc `claude/institutional-alignment-certification-evaluation.md`). Drafted on branch `docs/ch09-institutional-alignment-certification` and committed there (7fadbbe4). This is a core change touching Chapters 7, 8, 9, and 13 (Lane D). The earlier hold on core changes to Chapter Nine and Chapter Thirteen was **lifted by the steward on 2026-10-13**: the announcement will not be made until the corpus is complete, so there is no timing hold.

## 2026-10-13 — Formation check (Chapter Seven §7) and remediation readiness with denial and revocation (Chapter Nine Part B §7.1–§7.2, Part D §12.2 item 7 and §13.5): drafted on the same branch, signed off by the steward 2026-10-13

Note: [formation_check_and_remediation_readiness](../evidence/2026-10-13/formation_check_and_remediation_readiness.md). The Chapter Nine hold was lifted on 2026-10-13 (see the entry above).

## 2026-10-19 — Housekeeping closed in the session that followed the Chapter Seven and "instrument" work

- **Old local branch deleted:** `docs/ch13-prompt-review-cul-nul-windows` (its commit `b0c6021f` was contained in the later branches and in `main`). Local `main` was fast-forwarded to `origin/main` (`b3a2c7b5`) and the work moved to `docs/ch07-regression-fixes-and-todo-audit`.
- **Continuity aim Trace updated** (`core_05_apex_continuity_aim.md`): the Downstream principles now list Chapter One §8 (the aim's own introduction), §9, §10, §11 and §12, in numeric order, plus §19.1.5 as before. §13 to §15 were checked and left out: Chapter One §12 states that §§9 to 12 build the Continuity aim and §§13 to 15 supply the tradeoff procedure that weighs it against Flourishing, and the aim file already cites §13 for that.
- **Regression restored to green** (`make regression`, all 101 targets): four pre-existing failures fixed in `core_07_charters.md` (two unnamed section cites in §2.1, a lead-in sentence for §2.4, a list-intro colon in §2, and "publishing its charter" now "publishing its System Charter or Institutional Charter"); `project/MEMLOG.md` exempted from the `avoid-instrument` scan, as it already is for the bare-pathway scan, because it names the banned word when it records the ban; three uses of the banned word in the `charter` entry of `tools/architecture/lexical_guardrails.json` replaced with "document"; `ai_corpus/indexes` regenerated with `make ai-corpus-sync`.


## 2026-10-17 — Backup Record Authority: umbrella name closed (2026-10-19)

- [x] **Drop the umbrella name:** "Registry" was dropped; revisit only if registrars and the Backup Record Authority ever need a shared parent. Closed by the steward 2026-10-19 with no action: registrars and the Backup Record Authority keep separate names, under the naming rule TERM-BODY-01 (authority, custodian, registrar; [doc_architecture.md](../doc_architecture.md), fifty-first move).

## 2026-10-17 — Backup Record Authority (CF-5.7): Chapter Thirteen §2.3 bullet approved by the steward 2026-10-19

The new Chapter Thirteen §2.3 bullet says a contest of a record the Backup Record Authority opened goes to a forum with jurisdiction and never back to that authority. It repeats CF-5.7's own "does not hear a contest" line in core text, where the authority is not otherwise mentioned; Chapters Seven and Ten already cite CF-5.7, so the pointer has precedent. Approved as written, with the wording of TERM-BODY-01 ("that authority", not "that office"). Chapter Seventeen §1 heightened review for this core-text change stays open in TODO.md.

## 2026-10-17 — Chapter Ten §3.7 "sentient acting alone" bullet approved by the steward 2026-10-19

A lone sentient can ask for a record of their own contribution without any group or Charter. Their own logs and photos count as inputs, not verification, and any disinterested relying body can verify. Where no relying body exists, the record goes to a forum under §3.6 (forums are already record-opening authorities there). Approved as drafted. Alternatives not taken: widening the Backup Record Authority to this case (it would mix its Charter-gap job with a different one), and routing it to the CF-9.6 investigative service (that service investigates and does not verify contributions). Chapter Seventeen §1 heightened review for this core-text change stays open in TODO.md.

## 2026-10-17 — Chapter Ten §3.7 *Segregation of duties*, Request row: approved by the steward 2026-10-19

Old text: the requesting party "holds no seat." New text: the requesting party "holds the initiating seat on its own request and needs no institution to do so." Chapter Eight §2 defines the initiating seat as the one that "requests, proposes, operates, claims," so the old text contradicted it. No new conflict: *No self-custody* already stops the requester from verifying or holding the record. Approved as drafted. Chapter Seventeen §1 heightened review for this core-text change stays open in TODO.md.
