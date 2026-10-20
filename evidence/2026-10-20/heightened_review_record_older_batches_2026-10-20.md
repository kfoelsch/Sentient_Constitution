# Heightened review record: older batches, Clusters A, B and C (2026-10-20)

Status: review done, fixes applied, awaiting the steward's final adoption at the announcement. The contest period stays open until then.

Standard: [Chapter Seventeen §1 Heightened Review for Rights-Affecting Changes](../../core_17_amendment_ratification.md#1-heightened-review-for-rights-affecting-changes) and [Heightened Scrutiny](../../core_05_band_oversight.md#heightened-scrutiny). Non-regression: [Chapter Fifteen](../../core_15_non_regression.md). The companion record for the standing-record seats and custody batch is [heightened_review_record_2026-10-20](heightened_review_record_2026-10-20.md); the same limits (section 5) apply.

## 1. What was reviewed

Core-text changes signed off by the steward between 2026-10-13 and 2026-10-19 that were waiting on Chapter Seventeen §1 review, grouped in three clusters:

- **Cluster A, the Dissolution Reformation Lock and the dissolution ladder:** Chapter Eleven §5.5 and §8; CI-13.1, CI-13.4; CI-28.1 to CI-28.6; CF-11.4 threshold bullet; the Class P reach.
- **Cluster B, time windows:** Chapter Thirteen §6 (tier outer bounds and intake targets, time-scale routing); Article II-E ceiling; Article XVIII-C with CS-5 and CS-9 echoes; Article XXVIII-A with CI-14.4.4; the Domain-Specific Materiality answer window; Chapter Seven §1.6 windows; CJS-0.4.
- **Cluster C, authority naming, Interim Hold and speech, authenticity:** Article XI-E gates and the Institutional Authority Standing Lock; the Interim Hold standard (Chapter Thirteen §5); authority naming across Chapters Five, Seven to Eleven and Thirteen; the certification-seat clock; restricted information and evidence preservation (CF-5.8, Article XIV-A).

## 2. Burden and alternatives

The actor is the drafting work (the author and steward with Claude drafting in session). Reasons and alternatives weighed for each batch are in the sign-off archives ([TODO_RESOLVED_2026-10-13.md](../../archive/TODO_RESOLVED_2026-10-13.md), [2026-10-17](../../archive/TODO_RESOLVED_2026-10-17.md), [2026-10-19](../../archive/TODO_RESOLVED_2026-10-19.md), [2026-10-20](../../archive/TODO_RESOLVED_2026-10-20.md)) and the `doc_architecture.md` move log.

## 3. Independent review

Three fresh AI reviewers (Claude agents with read-only access, one per cluster) that had not seen the drafting conversation. They are independent of the drafting session only; they are not a human body and not independent of Anthropic or of the author and steward. Each finding was checked against the actual files before being put to the steward. One reviewer finding (Cluster C, "authenticity failure forces removal") overstated the text, which lists four remedies, and was handled as a clarification, not as a defect in the rule.

## 4. Findings and what was done

### Cluster A

| Finding | Disposition |
| --- | --- |
| **A-B1** The lock could reach a sole sentient or a group acting for itself | **Fixed** (steward: exclude and limit). Chapter Eleven §5.5 trigger excludes a single sentient and a group of sentients acting as themselves; carve-outs for good-faith purchasers and similar; a vehicle may keep operating pending the decision; Systems with a sentience indicator handled; a permanent form is re-reviewed at each review interval; §8 covers insolvency and final accounting. |
| **A-B2** Class P reach unclear | **Fixed** (steward: require a verified crossing). CI-13.1 Class P limits stated. |
| **A-B3** Forum dissolution on a CF-11.4 threshold lacked gates | **Fixed** (steward: add the gates). CI-13.1 forum-dissolution gates: verification, hearing, Tier C deadlines, receiving forum; CF-11.4 bullet aligned. |
| Should-fix and minor items (CI-13.4 separate proposer, two-keys independence and deadline, owner-fault process, item 10 designation, CI-28 rung 6 exclusion, renewal and re-expansion deadline, status forum, sealed custody review, final order definition, defiance by those with authority, clawback process, funding outside the issuing family) | **Fixed.** |

### Cluster B

| Finding | Disposition |
| --- | --- |
| Time windows keyed to the wrong class or tier in several places; a self-check record that did not match the text; lengthening without reasons | **Fixed** (steward: fix keying, redo the record, keep lengthening with reasons). Chapter Thirteen §6 time-scale routing body; a challenge does not pause a clock; overrun consequence; emergency deferral decided by the reviewer; "begin" defined for the prompt-review window; Article II-E ceiling; Article XVIII-C, CS-5, CS-9 class clauses; Article XXVIII-A and CI-14.4.4 *Clock* bullet; DSM answer window; CJS-0.4. `evidence/2026-10-18/time-window-test-1-self-check.md` corrected. |

### Cluster C

| Finding | Disposition |
| --- | --- |
| **C-B1** A statement could found an Interim Hold, in tension with Article XI-B | **Fixed** (steward: a statement alone never suffices). Chapter Thirteen §5, Chapter Seven formation-check passages and Article XI-E now say a statement alone never meets the ground; speech is shown by clear, verified evidence; open doubt counts against the hold; short forms point to the full ground in Chapter Thirteen §5. |
| **C-B2** Authenticity failure remedies unclear | **Fixed** (steward: clarify structural remedies first). Chapter Seven: replacing the holder is one choice, never required by a finding; the only consequences are the outstanding-lock gate and the Interim Hold; "authentic alignment" tied to verified conduct, control, and rewards. |
| Hold limits on sole founders; no re-issue of a hold on the same facts | **Fixed** in Chapter Thirteen §5. |
| Restricted-information silence rule; appeal scope; restricted information authority appointment | **Fixed** in CF-5.8. |
| "Less at fault" evidence wording | **Fixed** in CF-5.8, core_05_band_oversight.md and Article XIV-A echo (evidence that tends to show not at fault, less at fault, smaller harm, or doubt on other evidence). |
| Certification-seat fallback; CF-13.4 naming power; gap-log notice content | **Fixed** (CI-3.2 line on the record seat; CF-13.4; Chapter Seven §4.7). |

## 5. Limits and dissent

- The reviewers are AI. The project is a team of two sentients, so no human or institutional reviewer is planned before the announcement.
- The fixes were not independently re-reviewed. Several fixes in clusters A and C are substantive additions, not corrections.
- No reviewer dissent is unresolved. The steward's choices were the recommended options throughout.
- Deferred, with no change made now: the minor items the reviewers marked as style-only, and the translation sync (translations are paused and are not Claude's work, see `AGENTS.md`).
- Non-regression (Chapter Fifteen): none of the fixes removes a protection. The Cluster A changes narrow the lock's reach and add process; the Cluster C changes raise the bar for holds on speech.
- Contest: the contest period stays open until the announcement; the steward adopts at the announcement.
