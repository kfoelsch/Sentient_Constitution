# Time windows: Test 1 non-regression self-check (2026-10-18)

**Scope.** The 30 / 60 / 90-day scale, the Emergency level and time-scale levels, the prompt-review window, the CUL and NUL tier columns, the calendar certification intervals, the 14-day "reasonable" period, and the record-update change in CS-2 §8.5 and CS-3 §7.5. Commits: `916b7964` (merged, PR #80), `b0c6021f` (local), and the uncommitted 2026-10-18 work (forty-first to forty-sixth moves in `doc_architecture.md`).

**Test.** [Chapter Fifteen Test 1](../../core_15_non_regression.md#2-test-1--substantive-non-regression-validity): the change must not weaken a Chapter One constraint, a Chapter Two to Four integrity rule, a Chapter Six Rights Floor, or a Chapter Fourteen legitimacy rule, including by indirect narrowing. Article XXVI-C (timely resolution) is a Chapter Six Rights Floor. It carries no numbers; its numbers live in Chapter Thirteen §6 and CF-11.3.1.

## 1. Changes that shorten or only pin a time

These pass without a note.

| Change | Direction |
| --- | --- |
| Restricted evidence no longer slows the clock | Removes a ground for extension |
| Emergency level: restore-challenge window 3 days, not 7 | Shorter |
| Prompt-review window: review of a measure in force begins inside 24 hours, 2, 4, 8 or 12 days (Tiers A, B, C, L, P), a hard line | Replaces "inside the matching tier's window" (7, 14, 30, 60 or 90 days) |
| CUL-1 to CUL-4 and NUL-1 to NUL-3 take the tier columns | Replace open wording ("without unjustified delay", "as soon as containment posture allows") with compliance lines |
| "Reasonable period / timeframe" is 14 days, the Tier B outer bound | Replaces an open phrase with a ceiling |
| CI-13.8 independent review begins inside the prompt-review window | Replaces the whole Tier A window (7 days) with 24 hours |
| CF-11.3.2 publication: "as soon as lawfully feasible" replaced by Chapter One §16.4 Document at Action | Replaces an open phrase with availability when the action is taken; where full reasons cannot be ready, the fuller record is due no later than the matter's tier outer bound. The restricted part may still be held back, and a restriction that bars even the marker is recorded at the time |
| CF-12.6 continuity-mode communications: "as lawfully feasible" replaced by Chapter One §16.4 Document at Action | Replaces an open qualifier with publication from the activation record when the mode takes effect, except what a lawful restriction holds back (a marker still shows). The CF-12.5 fallback covers impaired systems, so no condition is removed that the fallback did not already handle |

**Tiers L and P, stated once.** The prompt-review window is 8 days for Tier L and 12 days for Tier P. A reader might take a bare "promptly" as sooner than that. The numbers are still tighter than the wording they replace: the old wording allowed review any time inside the tier window, which is 60 days for Tier L and 90 days for Tier P. The figures are hard ceilings ("no later than"), not targets, and the Emergency level shortens the start of review to 24 hours at Tier A. No site where a measure is in force now allows more time than before.

## 2. Changes that lengthen a time-limited protection

| What lengthens | By how much | Reason |
| --- | --- | --- |
| Tier C outer bound; complex Tier B bound; Tier C restore-challenge window | 28 to 30 days (+2) | One scale in 30-day months, matching the 30-day resolution window |
| Tier L outer bound and restore-challenge window | 56 to 60 days (+4) | Same |
| Tier P outer bound and restore-challenge window | 84 to 90 days (+6) | Same |
| Interim Hold lapse date for a merits matter in Tier C, L or P | +2, +4, +6 days | Set from the merits matter's tier window (Chapter Thirteen §5; Chapter Eleven §5.6). A restriction on a named sentient's pathway may last that much longer. Still one extension only, still a reasoned, reviewed, lightest-measure order, and the prompt-review window now guarantees an early independent look |
| Level 3 (Heavy) | Tier A up to 30 days (was 14 at most); Tier B up to 60 days (was 28 at most) | Heaviest multi-party, cross-border or consolidated matters. Needs a renewed Chapter Thirteen §6.1 showing on top of Level 2. Interim protection stays at the tier's own floor. Core already allowed any extension length on a §6.1 showing; the level publishes a size, not a right |
| Certification intervals | Class A 91 to 89-92 days; B 182 to 181-184; C 364 to 365-366; L 728 to 730-731; P 1,092 to 1,095-1,096 | Stated as calendar periods (3 months, 6 months, 1 year, 2 years, 3 years) after the review unit was retired. De minimis. Classes C, L and P are always longer; A and B are sometimes longer |

**What the lengthenings do not weaken.** The Rights Floor stays: a time-bounded, reasoned, reviewable measure; notice and a route to challenge; and no second slower clock for emergencies. Time given to parties (the 7-day response window, challenge and appeal windows) is untouched. Intake, evidence preservation, interim protection and the restore-challenge window never lengthen with a complexity level. The outer bounds still need the same showing to extend.

## 3. A change that can read as looser: record updates

CS-2 §8.5 and CS-3 §7.5 moved from "promptly once changed conditions are recognized" (last merged wording) to a check on the system's certification interval (3 months for Class A, 6 months B, 1 year C, 2 years L, 3 years P). The sentence that the record is revised whenever types, uses or risks change stays, and certification must still verify that reassessment happened where triggers fired. The stated time to catch up is now the interval, up to 3 years for a Class P record. These are Lane C operational duties and not Chapter Six Rights Floor text, so this self-check reads Test 1 as not binding them directly. The custodian chose the simpler rule on 2026-10-18; revert CS-2 §8.5 and CS-3 §7.5 if that reading is not accepted.

## 4. Downstream files that cite the changed sections

- Chapter Thirteen §6 and §6.1: Articles VII-C, XIV, XXVI-C, XXVIII-D (cite pointers), Chapter Five (Stay, Interim Hold, measurement text), Chapter Nine Part B, Chapter Eleven §5.6.
- CF-4, CF-5, CF-6, CF-8, CF-11, CF-13, CF-14; CI-3, CI-13, CI-14; CJS-0.4, CJS-3.6, CJS-3.15; CS-2, CS-3, CS-4, CS-5, CS-9, CS-11.
- `implementation/steward_owner_clock_index.json`, `guides/CONCEPTUAL_OVERVIEW.md`.

## 5. Not covered

Translations still carry the old figures and wording. They are updated after the announcement, not here.
