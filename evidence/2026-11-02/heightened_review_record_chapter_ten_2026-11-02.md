# Heightened review record: Chapter Ten and Chapter Nine cross-comparison changes (2026-11-02)

Status: **steward sign-off given in session on 2026-11-02 (all four groups, as written); two AI review rounds done and their fixes applied; the second-round fixes are not independently re-reviewed.** Adoption and the contest period stay open until the announcement. Nothing is committed.

Standard: [Chapter Eighteen §1 Heightened Review for Rights-Affecting Changes](../../core_18.000_amendment_ratification.md#1-heightened-review-for-rights-affecting-changes) and [Heightened Scrutiny](../../core_05.050_band_oversight.md#heightened-scrutiny). Non-regression: [Chapter Sixteen](../../core_16.000_non_regression.md). The earlier records this one follows are [Chapter Seven §4 and related edits](../2026-10-20/heightened_review_record_2026-10-20.md) and the [older batches](../2026-10-20/heightened_review_record_older_batches_2026-10-20.md).

Note on the cite: the TODO and the 2026-10-20 records say "Chapter Seventeen §1". The section is in the Chapter Eighteen file; this record uses the current number.

## 1. What was reviewed

Changes made on 2026-11-02 after the cross comparison of Chapter Nine and Chapter Ten (moves 224 to 233 in [doc_architecture.md](../../doc_architecture.md)), measured against commit `60d79cb7` (which holds moves up to 223). The full diff of the five affected text files, current as of move 236 (so it includes the review fixes), is [heightened_review_patch_chapter_ten_2026-11-02.diff](heightened_review_patch_chapter_ten_2026-11-02.diff). Sections 3.1 to 3.3 describe the changes as made in moves 224 to 233; section 4.2 lists what the review changed afterwards.

| File | Change |
| --- | --- |
| [core_10.000_institutional_alignment_certification.md](../../core_12.000_institutional_alignment_certification_evaluation.md) | All rule changes and wording changes below; about 320 lines changed |
| [core_09.000_system_alignment_certification_evaluation.md](../../core_09.000_system_alignment_certification_evaluation.md) | Placement note, reader-guide link text, three Trace labels, a pointer to CS-9.320 §12 |
| [core_09.010_system_alignment_certification_record_recertification.md](../../core_11.000_system_alignment_certification_records_recertification.md) | §9.2 bullet now points to Chapter Ten §9.6; §10.2 and §11.3 pointers |
| [cs_09.315 run sheet](../../corpus_systems/cs_09.315_system_alignment_certification_run_sheet.md) | Step 12: "eight institutional items" and the reopening sentence |
| [cs_09.320 illustrations](../../corpus_systems/cs_09.320_system_alignment_certification_illustrations.md) | New §12, three worked Institution walkthroughs (non-operative) |

Also added but not reviewable as constitutional text: the `CH10-DUPLICATION-01` audit and its tests (move 233), and the TODO update (move 234).

## 2. Burden and alternatives

The actor is the drafting work (the custodian directing, Claude drafting in session). Every rule change below was put to the custodian with alternatives through the session's question prompts before it was made; the evaluation that set out the options is `claude/ch09-ch10-cross-comparison-evaluation.md` in the project. The custodian took the recommended option on A1, A4, A5, A6, A7 (item 4 only) and B5, and chose "notice but no hold" on A3.

## 3. Inventory of changes by kind

### 3.1 Rule changes (meaning changed; these need the steward's attention)

| Ref | Move | Where | What changed | Who bears the burden or gains the protection | Review trigger |
| --- | --- | --- | --- | --- | --- |
| R1 | 226 | Chapter Ten §9.6 (new), Chapter Nine Part C §9.2, §9.5 rule 4 | A governance violation (a failure on §3 items 1, 3, 4, 5, 7 or 8) reopens the review of **every** System the Institution operates, stewards or controls. The Institution must give notice at once; if it does not, the lead forum of the Institution's evaluation gives it within the intake target. The reopened review is not a verdict, operation continues, urgent protection does not wait. This replaces the older trigger, which reached only Systems the finding "bears on". | Burden on Institutions (notice) and on lead forums (a reopened review per System). Protection widens for stakeholders of every System under the Institution. | Integrity and oversight conditions |
| R2 | 227 (A1) | Chapter Ten §7.4, §1.1, §7.3 | In a one-System evaluation the System is denied or revoked only on a ground resting on the System's own findings; the Institution is published Not Certified only on a ground resting on institutional findings; a ground resting on both gives both. A System-only ground leaves the Institution's status unchanged unless the cause finding places the cause in the Institution. Replaces the rule that any denial made the Institution Not Certified and denied the System. | Narrows denial of the System on institution-only grounds; narrows Not Certified status on System-only grounds. | Adjudication pathways; standing effects |
| R3 | 227 (A3) | Chapter Ten §9.2.2 | New duty to publish each clearance (including "for the time being") at once with the §10 challenge path open. The Institution may exercise the authority from clearance and waits for no notice interval; affected sentients may challenge and ask for a stay or interim protection. | Adds a publication duty on the lead forum. No waiting interval added. | Adjudication pathways |
| R4 | 227 (A4) | Chapter Ten §1.1, §9.2.2 | A Class P Institution that decides to take on new material authority is reclassified to at least Class L when it gives notice; the notice opens a first certification limited to the new authority. | Burden on Class P Institutions that expand. | Integrity and oversight conditions |
| R5 | 227 (A5) | Chapter Ten §1.3 | For an Institution already operating, a first-certification window that ends with no certification and no Article XXVIII-B reauthorization is an Adoption Transition milestone failure, and the Chapter Eleven path opens. Restraint duties run from the effective date. A new Institution's missed window stays a defect to log and correct. Still no gate on forming or running. | Consequence added for operating Institutions that miss the window. | **Standing effects** (highest scrutiny of this batch) |
| R6 | 227 (A6) | Chapter Ten §3 (new item 8), §2.2, §4, §6.2, §8.1, CS-9.315 step 12 | New eighth item, *The Institution's own institutional duties* (CI-8.210, CI-6.205, CI-6.215, CI-12.205): the pathways must exist, be usable in fact and answer in time, tested against observed operation. Item 8 is also a governance-violation item for R1. | Widens what an Institution is evaluated on. | Integrity and oversight conditions |
| R7 | 227 (A7) | Chapter Ten §3 item 4 | Carries the Time-Consistency Constraint of Chapter Nine Part A §3.3. | Burden on Institutions' reward and incentive design. | Integrity and oversight conditions |
| R8 | 227 (C3) | Chapter Ten §7.5 item 2 | Referral notice goes to the forums of every System the Institution operates, stewards or controls, not only those citing its record. | Burden on the notifying forum; protection widens. | Adjudication pathways |
| R9 | 232 | Chapter Ten §9.2.1 | A pilot or trial of any new material authority counts as new material authority and waits for recertification, scaled to the pilot's scope, population and duration. | Narrows what an Institution may begin without waiting. | Integrity and oversight conditions |
| R10 | 232 | Chapter Ten §8.1, §3 | The Institutional Certification Record carries a data types and handling entry for data handled outside any System. | Adds a record duty. | Integrity and oversight conditions |

### 3.2 Clarifications that could be mistaken for rule changes

| Ref | Move | Change |
| --- | --- | --- |
| C1 | 227 (B5) | "Regression testing" for an Institution means the regression results carried by the cited System Certification Records. There is no separate Institution regression test. Wording in §9.3.1, §11.5 and the §8.1 portfolio bullet. |
| C2 | 228 | §10.1 opens the published-record challenge path when the record opens for an Institution that already has stakeholders (before: "no outcome yet"). |
| C3 | 224 | §9.2 lists four triggers taken over from Chapter Nine Part C §9.2 (fall in contribution to shared foundations, ecological objection, data-type misalignment or overdue re-evaluation, misalignment under any applicable evaluation). Chapter Ten had not listed them. |
| C4 | 224 | §8 imports the Chapter Nine Part C §8 record-keeping rules; §8.1 adds §5 findings, the review submissions log and the completeness sentence. |

### 3.3 Wording and structure only

- **Moves 224, 225, 228:** cross-reference corrections, the rename "one-System evaluation", the Class L interval wording, §6.2 import of Chapter Nine Part B §6.1, and Chapter Nine Part C §10.2 and §11.3 pointers.
- **Move 229:** the wait rule is stated once (§9.2.2); §1.2 and §7.1 point to it.
- **Move 231:** Chapter Ten §9.3 to §11 reduced to summaries and pointers into Chapter Nine Part C. Anchors and headings unchanged. The §9.3.1 reader-guide table was removed because it only restated the text. This is the largest edit by volume and the one most likely to have dropped substance, so it is the first target of reviewer B in section 4.
- **Move 230:** the §9.2.2 reader-guide figure and CS-9.320 §12. Both are non-operative; Chapter Ten controls where they differ.

## 4. Independent review

Run: three fresh AI reviewers with read-only access, none having seen the drafting conversation. As in the 2026-10-20 records, they are independent of the drafting session only; they are not a human body and not independent of Anthropic or of the author and steward. Each reviewer's findings are checked against the files before they go to the steward.

- **Reviewer A, rules and non-regression:** R1 to R10. For each, does it remove or weaken any protection (Chapter Sixteen), open a loophole, or conflict with Chapter Eleven, Twelve or Article XXVIII-A/B? Specific questions: can R2 let an Institution avoid Not Certified status when the cause of a System's failure is institutional? Does R5 reach Institutions that Article XXVIII-B already covers, so the consequence is not double-counted? Is leaving item 6 (currency of System certifications) out of R1's governance-violation items deliberate and consistent with the §9.5 cascade?
- **Reviewer B, nothing lost in the pointer rewrite:** compare Chapter Ten §9.3 to §11 at commit `60d79cb7` with the current text and Chapter Nine Part C. Is every Institution-specific rule still stated or reachable by a pointer? Does any reader of Chapter Ten alone now miss a duty?
- **Reviewer C, consistency:** "eight items" everywhere; anchors and cites; CS-9.315 and CS-9.320 against Chapter Ten §3, §7.4, §8.1, §9.2 and §9.6; the §9.2.2 figure against the §9.2.2 text.

### 4.1 Results (three AI reviewers, run 2026-11-02)

The reviewers were read-only Claude agents that had not seen the drafting conversation. No reviewer found a blocker. Every finding below is open until the steward decides; those marked "rule" change meaning and go to the steward, and those marked "wording" can be applied without a rule decision.

**Reviewer A: rules and non-regression**

| ID | Kind | Finding | Touches |
| --- | --- | --- | --- |
| A1 | rule | Chapter Nine Part C §9.2 now reopens Systems only on a "governance violation". The baseline trigger (a failed or withdrawn Institutional Certification Record of the operator, where the finding bears on the System) is gone. A denial or revocation of the Institution, or a §9.5 rule 2 institutional-cause finding, reopens nothing. Part C §11.3 says a not-yet-aligned finding is not a violation, so "violation finding" is ambiguous. | R1 |
| A2 | rule | The one-System outcome split is only partly closed. §1.1 says §9.5 does not apply to a one-System evaluation, which removes the test for where a cause lies. Grounds that are the governing authority's conduct (unwillingness, concealment, missed conditions) are unclassified. Most item 3, 4 and 5 grounds also rest on System findings, so the "System-only" half is close to empty. A first-certification Institution denied on a System-only ground "stays as it stood", which is Not Certified. The record has one status entry for what are now two outcomes. | R2 |
| A3 | rule | §9.6 leaves out item 2 (portfolio and aggregate effect) with no stated reason. The one-System bullet is wrong for a violation found in a forum case. The notice fallback falls on a lead forum that does not exist for a Class P Institution or one still inside its first window, and the forum that makes a finding has no duty to tell anyone. Failure to give notice has no stated consequence. | R1 |
| A4 | rule | Pilots wait "whatever their scope", which is wider than Article XI-E, where the wait applies only to authority that is material under Domain-Specific Materiality. | R9 |
| A5 | rule | Publication at clearance leaves a stay as the only remedy, with no response time and no notice to known affected parties. Not a regression against the baseline (which was silent), but thin protection. | R3 |
| A6 | rule | The missed-window consequence extends Article XXVIII-A by analogy, so Chapter Ten should say it is its own rule. It has no class limit (Class P is only encouraged), no exception for an Institution that filed and cooperated while a forum overran, and the parent bullet still says "a defect to log and correct". | R5 |
| A7 | minor | Item 8 lets the Institution state its own response times. Use the floor timing as the minimum. | R6 |
| A8 | minor | A Class P Institution reclassified on notice may be discouraged from giving notice. Say whether the class holds if the plan is withdrawn or never exercised. | R4 |

**Reviewer B: nothing lost in the §9.3 to §11 pointer rewrite**

| ID | Kind | Finding |
| --- | --- | --- |
| B1 | rule | The §9.3.1 gloss on regression testing puts a cited System's failed regression inside "no misalignment is current". Under §9.3.2 that would be a failed recertification, but §9.5 treats a cited System's problem as an indicator only, and §11.5 lists it as violation input. The "no separate regression test" statement is a new rule, not a summary. |
| B2 | wording | §10.2 lost the conditions for when the lead-integrity and escalation paths apply. Restore one clause each, or say the Part C §10.2 conditions apply unchanged. |
| B3 | wording | §11.5 lost two qualifiers ("where systemic risk was in scope", "where disclosure was required"). Keep them. |
| B4 | wording | §10.1 changed its test from operating or outcome to stakeholders. State that the Chapter Ten bullets replace Part C's first and fourth bullets, and remove the circular "already operating already has stakeholders". |
| B5 | minor | Five small omissions, none changing a duty (indicator definition, "or its process", "so recertification comes sooner", the §9.3.3 pointer to §9.5, the "last two requirements" numbering). |

All 66 links in the rewritten range resolve. The Institution-specific rules were all found still stated or reachable by pointer.

**Reviewer C: consistency**

| ID | Kind | Finding |
| --- | --- | --- |
| C1 | wording | The Chapter Ten header says CS-9.320 holds System illustrations "not extended here". It now holds §12 Institution walkthroughs. |
| C2 | wording | The clinic walkthrough reaches Not Certified without a readiness finding, and does not say denial or revocation. Chapter Ten §7.3 allows denial or revocation only on a readiness ground. Cite §7.3 and §7.4. |
| C3 | rule | §9.2 "Cited System events" lists "reopened", which also triggers §9.5. A §9.6 reopening of a System would then trigger a reopening of the Institution's review, which loops back to §9.6. Say a §9.6 reopening is not a cited System event. |
| C4 | wording | The §9.2.2 figure omits the "blocker not decided inside the tier window" exit; its `classDef` sets white text on no fill, which is invisible on a light page; node I says "status is unchanged" where the text says "not by itself changed". |
| C5 | wording | The Part C §9.2 bullet group heading still says "Institutional Certification Record", and its wording ("an operator or steward that is an Institution") is narrower than §9.6 ("operates, stewards, or materially controls"). |
| C6, C7 | rule | Same as A3 (item 2 omitted; no fallback forum). |
| C8 | wording | §9.6's record entry (each System notified and the date) is not in §8.1, and the §9 Trace lacks three cites §9.6 uses. |
| C9 | wording | Walkthrough 3 says "the record it links to", "the operator", and no reason for Class A; walkthrough 2 says "one one-System evaluation". |
| C10 | wording | The §9 plain-terms line says "looked at again, right away"; the text gives notice at once and runs the review on the tier windows. |
| C11 | wording | A Chapter Nine Part A link label says "Institution System Class Evaluation"; the heading is "Institution Class Evaluation". |

No "seven items" remains anywhere live, "eight" is used consistently, and every cite to an item number points to the right item.

### 4.2 Dispositions (custodian decisions in session, 2026-11-02; applied in move 236)

| IDs | Disposition |
| --- | --- |
| A1, A3, C5, C6, C7 | **Fixed** (custodian: broaden and close gaps). §9.6 now has three triggers (a governance determination on items 1 to 5, 7 or 8, including item 2; a denial or revocation on those grounds; a §9.5 rule 2 institutional cause). The forum that makes the determination gives notice if the governing authority does not, with a default for Class P and first-window cases; failure to give notice is an item 3 defect. The one-System bullet covers forum cases. Chapter Nine Part C §9.2 uses the same terms and heading. |
| A2 | **Fixed** (custodian: tie-break and two status lines). §7.4 applies the §9.5 rule 2 test by name, treats the governing authority's conduct and shared Chapter Nine Part A §3.1 facts as resting on both, and gives the record two status lines; §1.1 and §8.1 match. |
| A4, R9 | **Fixed** (custodian: wait only if material). §9.2.1 counts a pilot only if it is itself material on its actual scope, population and duration. |
| A5 | **Fixed** (custodian). §9.2.2 adds notice at publication and a stay response target tied to CF-14.445 §2. |
| A6 | **Fixed** (custodian). §1.3 calls the rule Chapter Ten's own, limits it to Class L or higher, excepts an Institution that filed and cooperated while a forum overran, and says "also". |
| B1 | **Fixed** (custodian). §9.3.1 and §11.5 route a cited System's failed regression testing through §9.5. |
| C3 | **Fixed.** A §9.6 reopening is not a cited System event. |
| B2, B3, B4, C1, C2, C4, C8, C9, C10 | **Fixed** (wording). See move 236. C11 was already correct. |
| A7, A8, B5 | **Not done.** Not selected by the custodian (A7, A8) or judged non-substantive (B5). A7 and A8 stay on record as open minor points for the steward. |

Checks after the fixes: hygiene, layout, Chapter Five, vocabulary, time, alignment, records, generated and tests all pass, except the known `ch1-cjs3-alignment-audit` evidence-prune failure; the link audits were re-run after the last cite edits (see section 5). The fixes have not been independently re-reviewed.

### 4.3 Second review round (two AI reviewers, run 2026-11-02, on the move 236 fixes)

Two fresh read-only reviewers checked the fixes (A: rules and non-regression; B: consistency and wording). One blocker, no other new blocker.

| ID | Kind | Finding | Disposition |
| --- | --- | --- | --- |
| R2-A/B2 | **blocker**, rule | The "Not Certified, but the §7.5 effects do not follow" sentence in §7.4 conflicted with §6.3 and §7.5 item 4 (seat bar keyed to Not Certified), §9.3.1 (first certification is provisional) and §1.3. | **Fixed** (custodian): the Institution's pass ends on its own institutional findings (provisional certification), so it is not Not Certified; the System's denial is an indicator under §9.5 rule 1; §1.3 keys the milestone failure to no completed first pass, with exceptions for a forum overrun and for a running deferral. |
| R2-A/B3 | rule | The one-System case skipped the §9.5 rule 1 step-down, rewarding structuring as one System. | **Fixed** (same). §7.4 and §1.1 apply rules 1 and 2. |
| R2-A/D1, D2, R2-B/B2 | rule, cite | §1.3 exception did not cover a decided or deferred pass, and cited §9.2.2 (new authority) for a first-certification overrun. | **Fixed.** Cites Chapter Fourteen §6 (*Overrun review*) and Chapter Nine Part C §9.3.4. |
| R2-B/B1 (A) | rule | The §7.4 tie-break swallowed the split (Part A §3.1 treats nearly every institutional fact as shared). | **Fixed** (custodian): a ground is joint only where it is the governing authority's conduct, or rests on a fact Part A §3.1 attributes to the System itself, not one taken by link from the Institution's record. |
| R2-A/A1 | rule | A §9.6 reopening could loop. | **Fixed** (custodian): once per determination; a cause finding or defect in a §9.6 review is not a new §9.6 trigger; a System that fails after a reopening is still a cited System event for the Institution's own status. |
| R2-A/A2, R2-B/B3 | rule | §9.6 left out the §4/§5 evaluations, the systemic-risk and data parts of Part A §3, and denials on the governing authority's conduct. | **Fixed** (custodian: wider triggers). |
| R2-A/A3 | rule | No materiality test or close valve; a trivial first-filing determination reopened every System. | **Fixed** (custodian): material only, scaled to class; a System's lead forum may close a reopening on a short on-record note inside the intake target. |
| R2-A/E1, R2-B/B1 | cite | CF-14.445 §2 holds no urgent-relief figure by tier. | **Fixed.** Points to the intake target in CF-14.445 §3.1, or the Emergency setting's bound where it applies. |
| R2-A/F1, R2-B/B9 | wording | A cited System's failed or missing regression testing is not literally a rule 1 event. | **Fixed.** "Treated as the event in §9.5 rule 1". |
| R2-A/A4, R2-B/B5, B6, B7, B8, B13 | wording | Term clash ("governance violation" yet "not a violation"); cites to Part C §11.3 instead of §11.2; forum-case sentence; "finding" and "determination" mixed; "stated" and "actual" pilot scope; unnamed figure cite; Part C §9.2 wording. | **Fixed.** The name is kept and said not to mean a violation for standing. |
| R2-B/B4, B10, B11 | wording | CS-9.320 clinic example could rest on both grounds; no System status line; Class L trust core item not explained; plain-terms line said "every system". | **Fixed.** |
| R2-B/B12, B11 (Class P window) | minor | Two notice duties after an institutional-ground denial are not related; a Class P Institution reclassified on notice has no stated first-certification window. | **Not done.** Recorded with A8 for the steward. |

New vocabulary rule added in the same pass, at the custodian's request: **GROUND-QUALIFIED-01** (a bare "ground" must say its kind). Chapter Ten and CS-9.320 §12 were brought into line; 56 older lines elsewhere sit in a shrink-only baseline. The second-round fixes have not been independently re-reviewed.

## 5. Checks already run

- Audit categories hygiene, links, layout, Chapter Five, vocabulary, time, alignment, records, generated and tests passed after the last text change, except the known `ch1-cjs3-alignment-audit` failure (an evidence-prune `PermissionError` because the connected folder does not allow deletes; unrelated to these changes). Hygiene and links were re-run after the TODO update and passed. The translations category was not run (paused).
- `CH10-DUPLICATION-01` passes against its baseline (71 accepted near-copies).
- One drafting error caught and fixed during the work: the first rewrite of §9.3.1 narrowed the failed-regression rule and dropped the "no misalignment is current" detail; the original scope was restored.

## 6. Limits and dissent

- The reviewers will be AI. The project is a team of two sentients, so no human or institutional reviewer is planned before the announcement.
- The drafting session's own checks above are not independent review.
- The fixes that follow the review will not be independently re-reviewed unless the steward asks for it.
- Translations are paused and untouched. The new text adds to the translation backlog in `TODO.md`.
- Non-regression (Chapter Sixteen): no change in this batch removes a protection by design. R2 and R9 are the two that narrow something (R2 narrows denial and Not Certified status to the ground that supports them; R9 adds a wait). Reviewer A tests both.
- Contest: the contest period stays open until the announcement; the steward adopts at the announcement.

## 7. Steward sign-off

Given in session on 2026-11-02, after the final wording was shown in four groups. Each group was signed off **as written**, with no changes:

1. Chapter Ten §9.6 *Reopening the Institution's Systems* and the Chapter Nine Part C §9.2 bullet.
2. The one-System evaluation (§1.1, §7.3, §7.4, §8.1) and the missed first-certification window (§1.3).
3. New material authority (§1.1 Class P, §9.2.1, §9.2.2).
4. Evaluation scope and record (§3 items 4 and 8, §7.5 item 2, §8.1, §9.3.1, §11.5, §9.2).

The three points left open at that sitting were decided and signed off later the same day, each on the recommended option (move 240): A7 (item 8 times capped at the floor timing), A8 and B11 (Class P reclassification reverts if the notice is withdrawn before clearance or the authority is not cleared and nothing was exercised; the window runs from the notice), and B12 (one notice with two purposes). That wording was not independently re-reviewed. The sign-off does not replace the Chapter Eighteen §1 requirements of independent review and contestable publication: both stay open until the announcement. Resolved-item record: [TODO_RESOLVED_2026-11-02.md](../../archive/TODO_RESOLVED_2026-11-02.md).
