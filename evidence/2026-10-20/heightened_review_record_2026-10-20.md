# Heightened review record: standing-record seats and custody (2026-10-20)

Status: review done, fixes applied, awaiting the steward's final adoption and the open contest period below. Follow-up fixes for the capacity and dependents questions were applied the same day (section 6).

Standard: [Chapter Seventeen §1 Heightened Review for Rights-Affecting Changes](../../core_17_amendment_ratification.md#1-heightened-review-for-rights-affecting-changes) (independent review and contestable publication before adoption) and [Heightened Scrutiny](../../core_05_band_oversight.md#heightened-scrutiny) (burden on the actor, a real alternatives analysis, independent review, published reasons, uncertainty and disagreement). Non-regression: [Chapter Fifteen](../../core_15_non_regression.md).

## 1. What was reviewed

The core-text changes of 2026-10-20 (patch kept as `heightened_review_patch_2026-10-20.diff`, taken against the commit before `83eb9fa6`):

- Chapter Seven §4 (restructure into §4.1 to §4.7; holder changes; standing-record custody; gaps) and the Reader-guidance widgets in §2 and §3.
- CF-5.9 *Backup Record Custodian* (new) and edits to CF-5.7 *Backup Record Authority*.
- CI-3.6.3 field 10 (who may be named; tests) and field 11.
- Chapter Ten §3.7 custody fallbacks.
- Chapter Five entries *Record-Opening Authority* and *Record Custodian*.
- Chapter Nine Part B §9.2: one sentence after the cause-of-misalignment list (design cause holds the clean-recertification count at zero until the redesign is verified). Earlier drafts of the records misnamed this as §7.2; the correct place is §9.2.

## 2. Why the changes were made, and by whom (burden)

The actor is the project's drafting work: the author and steward (one sentient) with Claude drafting in session. The project is a team of two sentients at present, so no further internal reviewer exists. Reasons, as given in the session record (`doc_architecture.md`, sixty-eighth and sixty-ninth moves):

- A Chartered Party could leave a record seat, a custodian, or a contest seat unfilled, or fill one with a body it controls, and no default existed to keep the record independent. CF-5.7 covered record-opening only.
- Expected effect: a default custodian (CF-5.9), an open list of eligible custodians with tests, and notice and a chance to contest on holder changes.
- Affected sentients: subjects, claimants, and challengers of operator standing records; Chartered Parties (duties and costs); the forum families that keep the backup offices.
- Foreseeable risks (before review): capture of the seats; overload and concentration in the keeping family; gaming the open list; a burden on small adopters; stalling an unfilled seat.
- Alternatives weighed in session: closed register of custodians versus open list with tests (open list chosen); forum as default custodian versus a forum-kept office (forum-kept office chosen, forum as fallback); professional organizations as hosts (rejected for records about their own members); hybrid gap scope versus moving all records (hybrid chosen); ban versus allow reciprocal hosting (ban chosen).

## 3. Independent review

Reviewer: a separate AI reviewer (a fresh Claude agent) that had not seen the drafting conversation. It read the patch and the full chapters it builds on, with read-only access. It is independent of the drafting session, not of Anthropic or of the author and steward, and it is not a human body. The team has no other reviewer before the announcement, so the open contest period in section 7 is the further check.

Verdict: **adopt with changes**. Two blocking findings, nine should-fix findings, six minor findings.

## 4. Findings and what was done

| Finding | Disposition |
| --- | --- |
| **B1** Holder changes: no adjudicator, no suspensive effect, the emergency exception lets the Chartered Party install and entrench a holder; §4.7 created no substitution power | **Fixed.** Chapter Seven §4.5: notice at once to subjects, claimants, and challengers; contest goes to a forum, not only the party's amendment path; a pending contest holds the change back; the Chartered Party must show the tests are met; a holder change set aside is treated as never effective. §4.7 now defines an emergency substitution (empty seat only, temporary, takes the seat only after the Backup Record Authority or a forum confirms the tests, lapses at the short window) and says anyone may log a gap. §5 verification no longer lets an incoming holder check itself. |
| **B2** Tests apply only to custodians and nobody applies them | **Fixed.** CI-3.6.3 field 10: tests apply to the record-opening authority and contest seat too; new Disclosure test; new *Checked before it acts* test (Backup Record Authority or a forum confirms, burden on the Chartered Party, published with the map version); reciprocity covers any exchange within the same periodic review; pooled funding tested for practical power; a new kind of eligible body is an amendment. |
| **S1** Return of custody triggered by the Chartered Party's own lodging | **Fixed** in CF-5.9, CF-5.7, Chapter Ten §3.7, Chapter Seven §4.7, CI-3.6.3 field 10: custody returns only after confirmation and after notice and a chance to contest. |
| **S2** Gap scope splits versions, "then" undefined, no freeze, no one logs | **Fixed.** Each record stays whole with one custodian; the trigger day is the day notice reaches a forum, a registrar, or the Backup Record Authority; the inside-line holder keeps the record read-only and gives a sealed copy at once; a forum may find that an "outside" custodian is not outside; anyone may log a gap. |
| **S3** Possible Chapter Fifteen regression: "independent route" trigger narrowed | **Fixed.** The route also applies when the named authority or custodian is itself the subject or sits inside the subject's Material Control Line (Chapter Seven §4.6.1, CI-3.6.3 field 10, Chapter Ten §3.7), matching *No self-custody*. The earlier wording "when the Chartered Party is itself the subject" is not restored, because every operator record is about the Chartered Party. |
| **S4** Possible regression: forum replaced as default custodian; forum as custodian and as contest venue | **Fixed in part.** CF-5.9 is bound by CF-7 recusal and anti-self-judging rules and publishes reasons; parties may go to the forum at once; the antecedent is fixed; a forum that holds a record or designates its holder does not hear a contest of it; a designated holder must pass the tests. The forum-kept office is still a lesser standard than a full forum; see dissent 1. |
| **S5** Concentration in one keeping family; single store; privacy | **Fixed in part.** Contests of records handled by either backup office go outside the keeping family (such as the Integrity family); hash and sealed second copy with an independent assurance body; restricted-information handling (CF-5.8). **Capacity and surge** (follow-up, same day): CF-5.7 and CF-5.9 now publish capacity, queue, and the age of the oldest open request by tier, and send surge to a forum at once, with a continuing shortfall handled under CF-5.4 and the funding floor in CI-27. **Not done:** a neutral cost-recovery fund. See dissent 6. |
| **S6** Tests conflict with the Material Control Line definition and Chapter Eight §6 | **Fixed.** Membership alone no longer fails; discipline, funding, and common control count where they give practical power; the professional-association rule is stated as a consequence of that power and is limited to standing-record seats; the shared-host list item no longer fails for ordinary co-op membership. |
| **S7** Chapter Nine sentence: false cross-reference, no verifier, no clock, no way to review the label | **Fixed.** Names the verifier (the forum that found the cause or the next forum under §6.2), a clock (the intake target of the system's class), allows verification at the first provisional recertification, says the count "stays at zero", adds a request for review of the cause finding, and adds a line to *Verification, not assertion*. Follow-up, same day: the Class A reliance paragraph now says the hold on the count never by itself interrupts a system that sentients depend on, and the forum states interim protection, conditions on reliance, and notice to dependents while the hold lasts. |
| **S8** Stale cross-references and inconsistencies | **Fixed:** stale *Two kinds of change* reference; Reader-guidance bullet for §4.5; CI-3.6.3 field 11; CF-5.7 custody sentence; §4.6.1 default wording; stakeholder-record default in §4.6.2. **Not changed:** Chapter Ten's "cannot change those entries on its own" (Chapter Ten §3.7) is broader than Chapter Seven §4.2; left as the stricter wording. |
| **S9** CF-5.9 clock and routing | **Fixed:** the clock runs from the authorization or the transfer request; the challenger may go to a forum; a challenge with no named contest seat goes to the supervising forum; "captured" is a forum finding. |
| **Minor** plain-terms glosses; challenger; "chooses or funds"; "disinterested"; Tier P | **Fixed** (glosses, challenger, "chooses, appoints, or funds", "disinterested" defined); Tier P confirmed in Chapter Thirteen §6. The "Which version applies" layout is left as is. |

## 5. Things the review could not verify

- Some referenced files were not given to the reviewer (the other Chapter Five bands, CF-11, CF-7, CF-9, CI-4, Chapter Thirteen §3 and §6). Findings that depend on them were marked by the reviewer.
- The reviewer was not shown this record's reasons or alternatives; the burden section above is the drafter's account.
- The fixes in section 4 were made after the review and were not themselves independently reviewed. They are open to contest below.

## 6. Recorded dissent and open questions

Dissent a reasonable reviewer could hold, kept for the record:

1. A forum-kept administrative office as default custodian versus the forum itself versus a third-party escrow (concentration and a lesser independence standard against speed and specialization).
2. An open list with tests versus a closed register of cleared custodians (flexibility for small adopters against certainty and an ex-ante check). The fix adds a check before first action, which moves toward the register.
3. How strict the professional-association rule should be (independence against the burden on small practices).
4. Notice and contest on every holder change versus only on operator-record seats.
5. One family keeping both backup offices (simplicity against a common principal).
6. No fee and no Chartered Party funding (protects against purchased independence, but a defaulting Chartered Party pays nothing for the Backup Record Custodian).
7. The gap carve-out for records held outside the line.
8. A rigid hold on the clean-recertification count versus verifying at the next recertification.
9. Bundling the Chapter Nine sentence with a custody patch; it has its own reasons above.

Open questions: none carried from the review except the fixes not being independently re-reviewed. The team has no further reviewer (author and steward are one sentient), so the steward accepted the AI review with the open contest period.

## 7. Publication and contest

This record is committed in the repository with the change. Anyone may contest it, or any finding or fix, by opening a Finding or Proposal issue or a pull request comment under [CONTRIBUTING.md](../../CONTRIBUTING.md). The lane gates are not enforced before the announcement (custodian decision, 2026-10-07), so the contest period stays open until the steward adopts the text at the announcement. The steward decided the fixes in session on 2026-10-20 (B1 full fix, B2 full fix, S1 and S2 fixed, the rest applied).
