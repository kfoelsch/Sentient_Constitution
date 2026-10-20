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

## 2026-10-17 — Certification seats and the invalid-Charter rule: option C chosen by the steward 2026-10-19

Question: does silence in the Charter Role Map about a certification seat (initiating, record, or contest) follow the invalid-Charter rule that applies to the standing-record offices? Options were A (keep it a defect, as it was), B (make it invalid at once) and C (keep it a defect, with a clock). Chosen: **C**. The gap is logged, the CI-3.2 lane map places the seat meanwhile so no pass stops, and the Chartered Party has the CI-13.3 response window and resolution window, counted from the logged notice, to place the seat by a dated amendment. A seat still unplaced when the resolution window ends makes the System Charter or Institutional Charter invalid on the same terms as a gap in CI-3.6 field 10. Written into Chapter Seven §4.7 (new bullet), Chapter Eight §5 (pointer), CI-3.2 *Fallback for certification seats* and CI-3.6 field 11 *If silent*. Drafting choice to check: the lane map keeps placing the seat for a pass already open after the Charter becomes invalid, so the pass is not stranded. Chapter Seventeen §1 heightened review stays open. Translations are not synced.

## 2026-10-17 — Backup Record Authority (CF-5.7): name, default route and 2026-10-19 additions approved by the steward 2026-10-19

**Decision 1, option A with the tidy.** The name "Backup Record Authority" and the default-route rule stay: where no route is named, the Backup Record Authority (CF-5.7) is the default for a record that *No self-custody* (Chapter Ten §3.7) sends to independent verification. The tidy is applied: the next sentence now reads "Absence of any such named route is a gap the steward must name in the log, not a reason to enter the record themselves," so it no longer reads as contradicting the default. Alternatives not taken: a more neutral rename (it would overlap with "independent route" and "independent verification" in the same paragraph and touch every CF-5.7 cite), and dropping the default (forums would take every unnamed-route record).

**Decision 7 additions.** The CF-5.7 draft is approved with its two flagged choices: the answer deadline reuses the class-to-Tier intake target of Chapter Seven §6 and states no day counts, and funding sits with the keeping forum family or local forum. The certification-seat clock choice (the lane map keeps placing the seat for an open pass after the Charter becomes invalid) is approved too.

Translations are not synced for any of the passages edited under Cluster 1 (paused). Chapter Seventeen §1 heightened review stays open in TODO.md.

## 2026-10-19 — Restricted information authority (CF-5.8) review: Cluster 2 decisions 1 to 6 approved by the steward 2026-10-19

Review note: project doc `claude/restricted-information-office-unread-files-review.md` (written before the rename from "office" to "authority").

- **1 (option B).** CF-13.4: the authority keeps answering during family-capture continuity; the displaced family does not appoint, staff, fund or instruct it or take part in its budget; the other families carry its share under the published formula until restoration.
- **2 (option A).** CF-5.7 *Family capture* bullet: the same rule for the Backup Record Authority, with the keeper named by the body the continuity record names for activation oversight.
- **4 (option A).** CS-2 Part A: a Type S access dispute goes first to the restricted information authority; other challenges go under CJS-3.13.
- **5 (option A).** CF-5.8 *What it does not do*: two bullets, audit access (Article XVI-B, CJS-3.4) and release review (CJS-3.22).
- **6 (option B).** Pointer only: CF-5.8 *What comes to it* and a Read-with line in the Chapter Ten §3 Trace; the operative §3.1 bullet is unchanged.
- **Also decided:** `exculpatory` and `inculpatory` go on the do-not-use list (rule `avoid-exculpatory-family`); five uses reworded in plain words.

- **3 (option A, approved later the same day).** CF-5.8 *What it decides under* now preserves material showing that a sentient is not at fault, or is less at fault (Article XIV-A); a summary, redaction or closed review may not strip it.

Translations are not synced (paused).

## 2026-10-18 — Time windows, sitting 1: seven decisions approved by the steward 2026-10-19

- **1 (option B).** CS-2 §8.5 and CS-3 §7.5 restore the bullet "no later than the intake target of the tier that matches the system's class, counted from when changed conditions are recognized", beside the certification-interval check; the CS-3 §3.5 pointer names it again. The record-update reading in the Test 1 note is resolved.
- **2 (option B).** CF-11.3.2: the fuller record is due no later than the end of the prompt-review window of the matter's tier (was the tier outer bound).
- **3 (option A).** CF-11.3.2 "Reasons are recorded as part of the decision, not after it" confirmed.
- **4 (option A).** CF-12.6 Document at Action wording confirmed.
- **5 (option A).** Chapter Seven §1.6 windows for a missing System Charter or Institutional Charter keep the tier scale for all classes (Class L: response 8 days, resolution 60 days). Added to the Test 1 note.
- **6 (steward's own option).** A Chartered Party that disputes its class has the windows of the class it already holds on its System Classification Record. The steward chose this over my option C. **Gap I filled:** a party that holds no class on record is counted at Tier C (my drafting; the old rule was Tier L). The regression scenario for the tool-lending club now says Tier C.
- **7 (option A).** The repeat-request clarification in Chapter Seven §1.6 confirmed as written.

Chapter Seventeen §1 heightened review stays open in TODO.md. Translations are not synced (paused).

## 2026-10-18 — Time windows, sitting 2: core wording signed off by the steward 2026-10-19

All recommendations confirmed.

- **1 (A).** Chapter Thirteen §6 outer bounds of 7 / 14 / 30 / 60 / 90 days (Tiers C, L, P were 28 / 56 / 84), with the restore-challenge windows and Interim Hold lapse dates that follow them.
- **2 (A).** Level 3 (Heavy) stays: Tier A up to 30 days and Tier B up to 60 on a renewed Continuation discipline showing.
- **3 (A).** The prompt-review window stays at the intake-target figures (24 hours, 2, 4, 8, 12 days), with no cap for Tiers L and P.
- **4 (A).** The Emergency level (Tier A only, protective steps within 3 days) and the calendar certification intervals, audit midpoint and audit advance allowance, as written.
- **5 (A).** Article II-E deletion: a disclosed period, no later than 14 days, whatever class.
- **6 (B).** Article XVIII-C, CS-5 and CS-9: the transition deadline is the outer bound of the Tier that matches the system's class (7, 14, 30, 60, 90 days), or 14 days where no class is held. CS-4 (Class C recovery) and CS-3 (Class L intervention) stay at 14 days. CJS-0.4 updated.
- **7 (B).** Chapter One §16.4: the Avoidable Burden defect applies "where capture was feasible and was not built".

Chapter Seventeen §1 heightened review stays open in TODO.md. Translations are not synced (paused).

## 2026-10-18 — Time windows, sitting 3: names and audit rule approved by the steward 2026-10-19

Recommendations 1, 3, 4 and 5 confirmed. Decision 2 (the "declaration window" collision) was answered in the same sitting: see the end of this entry.

- **1 (A).** Domain-Specific Materiality (`core_05_band_oversight.md`): the Operating Party's answer to a classification challenge is due inside the **response window**, counted from the challenge, at the intake target of the Tier that matches the class it already holds (Tier C where none). CJS-0.4 now lists "a classification challenge" in the response window sense.
- **3 (A).** CJS-0.4 gains two names in use: **Early-instantiation window** (Article VIII-C) and **Exclusivity term** (Article XVIII-D, CI-24). Nine registry names with no use in any owner were retired from `tools/time_reference_registry.json` (receipt window, completion window, register-entry window, contraction review interval, attachment spell ceiling, fee-use term, non-availability period, progress report interval, open-format transition window). The exclusivity term is kept.
- **4 (A).** New lexical rule `review-in-tier-window`: review of a measure, order, hold, stay, or interim decision "inside the (matching) tier window" must say **prompt-review window**. Zero hits when added; the dated move log in `doc_architecture.md` is exempt.
- **5 (A).** No Chapter Five definitions added for *complexity level*, *Emergency level*, or *Document at Action* (record only).

Correction recorded: the sitting-3 sheet first said CI-14.4 had no "declaration window" collision and that "open-format transition window" was used by owners. Article XXVIII-A does use "Declaration windows" for the CI-14.4 enforceability declaration, and only "open-format transition controls" appears, so nine names (not eight) were unused.

**2 (D, then A).** The steward chose to standardize the Article language on the Tier or Class window instead of renaming NUL-1's window. First, CI-14.4 was broken into subsections CI-14.4.1 to CI-14.4.12 (presentation only). Then, with option A for the basis: Article XXVIII-A *Declaration follows data* and CI-14.4.4 *Declaration bound* now say the enforceability declaration is due no later than the outer bound of the Tier that matches the scope's class (7 days for Class A, 14 for B, 30 for C, 60 for L, 90 for P) where the scope is a system class, and 14 days (Tier B) for any other scope, counted from when the verified criteria are met; the plan may state a shorter bound, not a longer one. "Declaration window" now belongs to NUL-1 alone; CJS-0.4 says so.

## 2026-10-18 — Dissolution Reformation Lock (Chapter Eleven §5.5, §8): Cluster 4, sitting 1, approved by the steward 2026-10-19

The steward confirmed every recommendation. Operative wording was signed off; Chapter Seventeen §1 heightened review stays open in `TODO.md`.

- **1 (A).** Permanent form on the two grounds as written: a final Chapter Twelve designation with a finding of pervasive conduct, or verified Irreversible Harm whose remedy has not been and cannot be delivered by restitution or lawful substitute restoration. A ground-2 lock is reassessed as non-permanent if later facts show the remedy was delivered.
- **2 (A).** Restorable form kept as written; ends only on an independent finding. No review cadence added.
- **3 (B).** Article XIX-D plain terms gain a parenthetical exception for the permanent form of the Dissolution Reformation Lock; the Chapter Five *Standing Lock* plain terms gain "No lock on a sentient is permanent."
- **4 (A).** A forum dissolved on a CF-11.4 threshold carries the lock (restorable unless the wind-down order records a permanence ground). CI-13.1 item 5 and the Chapter Eleven §5.5 trigger say so. Follow-on (steward, same session): the forum is suspended at once under CF-11.4, and its dissolution takes effect only on the two keys in CI-13.7, the lead Integrity forum's decision and the confirmation of a second independent forum. CF-11.4 and CI-13.1 item 5 say so.
- **5 (A).** A System retirement order sets the lock in the form the §5.5 *Systems* bullet gives. New CI-13.9 item 6; the §5.5 trigger names it.
- **6 (yes).** Placement of the permanence rule in Chapter Eleven §8 with a pointer in Chapter Twelve §4.2; burden on the party saying a vehicle is caught and no new audit or clock; Articles XIX-D and XIX-E list the special locks.

## 2026-10-15 — Dissolution and forced-contraction procedure (CI-13): Cluster 4, sitting 2, decisions 1, 3, 4, 5, 6 approved by the steward 2026-10-19

Decision 2 (Class P reach) was settled afterwards, below. Decision 7 (operative sign-off of CI-13) remains open.

- **1 (A).** CI-13.10 item 6 keeps defiance as a new verified fact (higher rung for the Chartered Party; Chapter Twelve review, the Institutional Authority Standing Lock and a CF-9 referral for the sentients) and adds: defiance that makes a remedy or process unusable in practice is assessed under Chapter Twelve criteria 4 and 6; the item adds no criterion.
- **3 (B, amended).** CI-13.7 item 4 is now an order of payment: remedy to those harmed; wages and other pay owed to workers; wind-down costs; non-culpable creditors, dependents and good-faith third parties; owners and members not at fault in proportion to stake (the steward set this order). A share that would go to an owner or insider found at fault, or to a vehicle caught by the lock, goes to unpaid remedy and then to the remedy system or receiver the forum names (CI-27). The steward first moved unpaid workers to directly after harmed parties and before creditors, then set wind-down costs third, after workers.
- **4 (ladder, as a bullet list).** CI-13.10 item 7: steward, receiver, liquidator and verifying-authority costs are met first from the Chartered Party's assets (after remedy and wages, ahead of every later step), then from the sentients found responsible through CI-11.4 malus and clawback, then from the published budget of the primary-stakes forum family (Chapter Eleven §9.2); never from affected sentients or dependents (§9.1). The earlier cites to CI-27 and CI-11 did not cover receiver funding.
- **5 (A).** CI-13.9 item 2: preservation ends only on a final finding that the System is not sentient, with no credible indicator left, followed by a forum order meeting the Article XXVIII-D destructive disposition floor. The steward never elects deletion. After a finding of sentience, state is never deleted under this procedure.
- **6 (A).** The name "contraction order" stays. No Chapter Five entry; CI-13.5 defines it.
- **2 (steward's own option).** All Class P entities, chartered or not, are subject to both the ladder and the Dissolution Reformation Lock. CI-13.1 reads "Chartered Party" to include a Class P Operating Party that has published no charter; CI-13.4 says rung 3 has nothing to remove from a Class P Operating Party; the Chapter Five *Chartered Party* out-of-scope bullet and Chapter Eleven §4.2 and §5.5 say the same. Decision 7 (sign-off of CI-13 as a whole) is still open.
