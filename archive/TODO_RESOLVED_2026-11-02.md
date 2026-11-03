# Resolved TODO items — 2026-11-02

## Chapter Nine and Chapter Ten cross-comparison: steward sign-off

Steward sign-off, given in session on 2026-11-02 after the final wording was shown group by group. All four groups were signed off as written. The Chapter Eighteen §1 heightened review for these core-text changes stays open in [TODO.md](../TODO.md) until the announcement: two rounds of AI review are done and their fixes applied, but the second-round fixes were not independently re-reviewed, and the contest period stays open.

Record: [heightened_review_record_chapter_ten_2026-11-02.md](../evidence/2026-11-02/heightened_review_record_chapter_ten_2026-11-02.md) (change inventory, both review rounds, dispositions) and [the diff](../evidence/2026-11-02/heightened_review_patch_chapter_ten_2026-11-02.diff). Moves 224 to 238 in [doc_architecture.md](../doc_architecture.md).

- **Group 1, Chapter Ten §9.6 *Reopening the Institution's Systems*** and the Chapter Nine Part C §9.2 bullet: three triggers (a determination that governance failed, including the §4/§5 and systemic-risk and data parts; a denial or revocation on those matters or on the governing authority's conduct; a §9.5 rule 2 institutional cause); only a material one reopens; once per determination; notice at once with a default forum; a lead forum may close a reopening that bears on nothing for its System; a review and not a verdict.
- **Group 2, the one-System evaluation and the missed first-certification window** (§1.1, §1.3, §7.3, §7.4, §8.1): System ground, institutional ground and joint ground; two status lines; a first certification with only a System ground ends provisional for the Institution; §9.5 rules 1 and 2 apply; the operating-Institution milestone failure for Class L or higher, with exceptions for a forum overrun and the one running deferral.
- **Group 3, new material authority** (§1.1 Class P, §9.2.1, §9.2.2): a pilot waits only if itself material; a Class P Institution is reclassified to at least Class L on notice; publication at clearance with notice to known affected sentients and the Systems' forums; a stay request answered inside the matching tier's intake target or the Emergency setting's bound.
- **Group 4, evaluation scope and record** (§3 items 4 and 8, §7.5 item 2, §8.1, §9.3.1, §11.5, §9.2): the eighth item; Time-Consistency; wider notice; the data types and Systems notified entries; regression results routed through §9.5; a §9.6 reopening is not a cited System event.

Also resolved: the cross-comparison evaluation items A1 to E; the duplication audit and its guard (`CH10-DUPLICATION-01`); the `GROUND-QUALIFIED-01` audit (backlog of 56 older lines stays in [TODO.md](../TODO.md)).

## The three minor points (A7, A8, B12)

Decided and signed off by the steward in session later on 2026-11-02, each on the recommended option (move 240):

- **A7, Chapter Ten §3 item 8:** a route must answer inside the times the Institution states, and those times may not be longer than the floor timing for its class (Article XXVI-C; CF-14.445 §3.1); a longer stated time is itself a finding.
- **A8 and B11, Class P reclassification:** the reclassification lasts from the notice until the notice is withdrawn before clearance or the authority is not cleared, provided nothing under it was exercised; the Institution then returns to Class P and the limited first certification ends; a new notice starts it again. The first-certification window for a reclassified Class P Institution runs from the notice, never from an Adoption Transition window that has already ended (§1.1, §1.3, §9.2.2).
- **B12, two notices:** after a denial or revocation the §7.5 item 2 notice and the §9.6 notice are one notice with two purposes; the lead forum that publishes the outcome sees that it is given, and where §9.6 applies it carries the reopening request and runs on the §9.6 giver, clock and defaults; the *Systems notified* entry covers both.

## Chapter Ten illustrations re-read

Re-read CS-9.320 §12 and Chapter Ten §9.2.2's reader-guide figure against the Chapter Nine and Ten changes (2026-11-02). The §12 multi-System walkthrough combined the general reopening rule with the exception for a System already inside a certification pass in a way that could imply both a new reopened pass and no second pass. It now states the exception as a separate condition, matching Chapter Ten §9.6. The §9.2.2 figure was consistent as a concise process summary. No rule changed.

## GROUND-QUALIFIED-01 baseline cleanup, first batch

Five clear bare-ground findings were removed by naming the Rights Floor, protected grounds, and grounds for restricting disclosure, or by replacing a vague reference with the restriction's scope (Chapter One §§12 and 16.4). The baseline was regenerated shrink-only; 51 findings remain across 21 files for contextual review. No duty or threshold changed.

## GROUND-QUALIFIED-01 baseline cleanup completed

Completed the contextual review of the remaining 51 findings across 21 files (2026-11-02). Each bare use was clarified from its source context: naming a protected characteristic, Interim Hold or permanent-lock ground, consequence trigger, reason, basis, or restriction as applicable. The shrink-only baseline now has zero entries. No duty, threshold, clock, or scope changed.

## Optional changed-file audit report

Added `python3 tools/audit_report.py --changed` with `--base` (default `origin/main`). It combines branch changes since the merge base with staged, unstaged, and untracked files. For corpus-only changes, it selects report targets by the registered audit scopes while each selected audit still reads its declared full corpus. Generator freshness checks run on corpus edits. If changes include non-corpus files or a target lacks a scope mapping, the report conservatively runs the full requested scope. The default `make audit-report` and regression gate remain full-corpus.

## Process-ownership and Option B crosswalk

The working process-ownership draft connects its floor-touching test to the **Standard Process Recognition** post-adoption outline and distinguishes forum questions for ruling under Chapter Fourteen §5 from System Alignment Certification. On 2026-11-02, the custodian resolved the six design directions for the supporting proposal: retain the narrow four-trigger floor-touching test and assess cumulative practical effects; allow any materially affected sentient to file and participate under existing participation/standing rules; allow a procedure owner to challenge demands that materially affect its assigned procedure or duties; use existing Chapter Fourteen §6/§6.1 windows without a second schedule or new emergency exception; and have a human edit any core text. The working draft records these directions. The core wording, scope and placement, and whether CI-14.205 needs a companion change-record template remain open in TODO. The crosswalk remains complete within its stated Chapter One/Chapter Eight frame; its 70 added tags await independent human review.

## Chart orientation audit

Added the whole-corpus `VIS-CHART-ORIENT-04` audit, regression target, exception-note convention, and focused tests. The translation-copy policy is to bring charts into line when each translation is next updated; translation work remains paused.

## Process/system/institution crosswalk confidence review

Reconciled the crosswalk to all 88 current Chapter One and Chapter Eight second-level headings: corrected all 68 carried-forward source references by title and added 20 missing headings. Second-read all 25 carried-forward medium- and low-confidence classifications; the three former low-confidence tags were reassessed at medium confidence, and tags/rationales were updated where the full text supported it. Added provisional tags for all 20 added second-level headings and all 50 third-level Chapter One subsections. The crosswalk now covers all 138 headings in its Chapter One/Chapter Eight frame; the 70 added rows await independent human review. Kept the crosswalk bounded to the principles-and-duties comparison in its title; extending it to the remaining corpus would be separate work.
