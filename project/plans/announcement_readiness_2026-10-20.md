# Announcement readiness working plan

**Started:** 2026-10-20. **Target:** a defensible public announcement by 2026-12-31. **State:** preparation; no release decision or adoption. This is an editorial work plan. The numbered core files govern; the [publication spec](../../implementation/PRE_PUBLICATION_SPEC.md) supplies the existing publication criteria. This plan does not waive them.

## Agreed purpose and division of work

The steward wants a mature, coherent corpus that helps rebuild trust and can be used for real governance. The audience is worldwide; a new community of AI agents is the first practical setting to examine, while the Constitution's scope remains universal. Adoption and influence are objectives whose achievement cannot be promised by a date.

These decisions were recovered from the October 20 planning conversation:

- The steward has reviewed through Chapter Six, is working on Chapter Seven, and retains control of core wording. Chapters Eight–Eighteen need confirmation review, with deeper work where needed.
- Codex edits non-core material directly, checks alignment against core, and brings substantive choices and unresolved conflicts in a short decision queue. Sound material should stay intact.
- Plan around 30 steward hours per week: initially 20 for core review, 6 for decisions and focused review, 4 for trials and contingency. These are planning allocations, not obligations.
- Translations are desired at announcement. Queue them as chapters settle, then perform a final synchronization and quality review. Existing translation work stays separate from English editing.
- There are no operating agents available to participate. Begin with bounded procedural simulations in separate sessions; maintaining agent infrastructure is outside the critical path. A simulation cannot establish live adoption or independent real-world institutions.
- Recruit outside testers alongside editing. Human usability and the publication spec's human-operator evidence cannot be established by AI roleplay. Prepare outreach; sending invitations needs the steward's instruction.

## Current baseline

The plan began at `34810bf6` after PR #100. For B04, local main was fast-forwarded to `e6bbe76d` after PR #102, and work continues on `codex/announcement-interlock-review`. Inherited Chapter Seven changes, translations, generated outputs and the uncommitted B02/B03 batch were preserved. Core and translation text remain outside the English implementation edit scope.

The [review inventory](announcement_review_inventory_2026-10-20.md) enumerates **523 tracked non-core paths** for review or disposition, including **75 Markdown files across CJS, CS, CI, and CF**. These are different workloads: 242 maintenance-tool paths require risk-based validation, not a prose rewrite. Generated outputs are checked through their sources. Dated planning material is reviewed for disposition rather than automatically treated as live guidance. Historical results and evidence are preserved outside that inventory. Counts are a snapshot, not progress claims.

The [first examination](../analysis/corpus_examination_2026-10-20.md) is a cross-corpus sample, not a completed full review. Its priorities are the small-group starting path, executable handoffs, measurement disagreement, resistance to hostile administration, and fidelity between core and implementation.

The inherited checkout's October 20 baseline audit is **103/105 targets passing**. The two failing targets are terminology and time-reference checks in unfinished Chapter Seven wording. Generated-file checks pass following the merged automatic refresh change. These failures remain open for the steward's core review; this plan does not waive them.

## Completion rule for each editing batch

Use a bounded group of related files and record its exact scope. For each operative procedure, inspect the governing core and incorporated sources directly. Check who acts, the trigger and required inputs, output and recipient, applicable clock owner, contest path, missing-capacity route, and important conditions or exceptions. Distinguish readability edits, corrections of alignment, and choices that require a core decision.

A batch is complete only when its sources, changes, relevant checks, unresolved questions, and dependency baseline are recorded. A targeted fix is not a whole-file review. If its governing core changes, reopen the affected portions. Use the inventory as a checklist; do not generate a new obligation from it or from a locator gloss.

Run `make audit-report` for a substantive batch. Use focused audits during repair; run `make audit-report-all` and the existing Pages deployment gate for the release candidate. Passing structural checks alone does not close practical-use or interpretation findings.

## Schedule and milestones

Dates are targets. Re-estimate throughput after the first full editing batch and first procedural trial; do not assume an AI can complete the remaining volume in one uninterrupted run.

| Target dates | Steward focus | Codex deliverable | Evidence for completion |
|---|---|---|---|
| Oct 20–Nov 8 | Finish Chapter Seven; begin Eight onward | Persist plan and inventory; reconcile backlog; trial the formation route; begin classification and shared-role dependencies | Every release task has a workstream; first trial records concrete obstacles; first full batch establishes a measured pace |
| Nov 9–29 | Continue core review; answer substantive questions | Review implementation families in dependency order; repair support documents and templates | All 75 family files have a recorded full-review disposition, or the schedule is revised with the remaining count |
| Nov 30–Dec 13 | Finish core confirmation review and design decisions | Run contest, failed-steward, remedy, and hostile-administration cases; align settled chapters with translation work | English dependency baseline recorded; unresolved trial failures and translation gaps explicit |
| Dec 14–23 | Review release evidence and proposed claims | Finish translation verification, reader paths, announcement materials, and release checks | A release candidate assessed against the publication spec, with evidence linked and exceptions proposed explicitly |
| Dec 24–31 | Decide whether to announce | Repair remaining release defects; prepare final publication package | Steward's release decision against actual evidence; no automatic announcement merely because the date arrives |

Suggested implementation order: classification and shared interlocks (CS-9.305, CS-9.310, and CJS-5.105 through CJS-5.135); formation and independence (CI-8.205, CI-14.205, CI-8.210, CF-13.405, CF-13.410, CF-13.425, and CF-13.470); operational handoffs and clocks (CF-13.415, CF-13.420, CF-13.445, CF-13.450, CF-13.455, CI-13.205, CI-8.215, CI-6.205, and CI-13.210); remedy and failure (CI-11.205, CI-11.210, CI-11.215, CF-13.435, CF-13.460, CS-6.320, CS-6.350, CS-6.355, and CS-6.330); remaining systems and domain companions. Read the necessary dependency sources even if their full editing batch comes later. Review guides and templates alongside their owners, then perform a final cross-stack pass.

## Backlog disposition

[TODO](../../TODO.md) retains the detailed source backlog. This plan groups it without marking items completed or silently deleting old obligations.

| Workstream | Included open work | Release handling |
|---|---|---|
| Core and constitutional choices | Seven completion; Eight–Eighteen confirmation; principle/definition alignment choices; Chapter One §13 aim; ownership and process proposals | Steward controls wording. Identify what is required for a coherent release; optional proposals do not enter core by implication |
| Full implementation review | CJS/CS/CI/CF, Remedy and Emergency stacks, spine alignment, owner fit and usability | Existing publication-spec work remains open until supported by completed batch records |
| Practical-use evidence | Small-agent formation and allocation; challenge to power; failure, restoration and return; LEQU disagreement; eight ordinary-life cases; P1 draft scenario validation | Reuse existing cases, distinguish simulation from observation, and record coverage gaps. Do not call a draft scenario run or passed |
| Shared stewardship evaluation | Human I1; handoff comparison; Option B competence and costly-case samples across model families | Preserve spec §6.5, including human-operator evidence for handoff-readiness claims. Lack of a persistent agent deployment does not waive that condition |
| Formal review and decision records | October heightened-review follow-ups, open contest period, final adoption decisions noted in TODO | Preserve the records and their stated limits. Publication and constitutional adoption are separate decisions |
| Translation | Overlapping renumbering, Chapter One, rights, charter, standing and widget follow-ups | Consolidate by settled English chapter and source revision; generating text does not establish fidelity |
| Reader and public release | README/start paths, conceptual and record overviews, FAQ, announcement, outreach, Pages source setting | Verify quoted counts and claims together; demonstrate the rendered public path and deployment settings |
| Maintenance and optional work | Audit changed-mode, generated maps, widget simplification, chart audit, optional extensions | Prioritize defects that block release. Optional enhancements remain deferred unless selected or required by a demonstrated failure |

## Translation workflow

The October 20 planning preference changes the earlier blanket pause into a chapter-gated queue. No chapter is assumed settled merely because an editing pass exists. The steward identifies a settled chapter and its source revision; record that baseline, synchronize its translations separately, check links and terminology, and obtain a fidelity review suited to the language. Track later source changes for a final synchronization. Do not attribute existing work to a model without evidence.

All 629 tracked translation paths are outside this English inventory. They are not 629 independent translation assignments: plan by language and chapter. Before setting a completion forecast, inventory language coverage and establish who or what can credibly verify fidelity. If quality cannot be demonstrated, bring a concrete scope or timing decision to the steward; do not quietly claim verification or drop desired languages.

## Practical trial protocol

The first case is a newly formed agent cooperative allocating a fixed shared compute budget. It must name the party that can bind the systems, classify material effects and dependencies, separate ordinary cooperation from adoption, assign lawful review and custody, publish a resource decision, and handle a challenge from a disadvantaged member. Add a failed steward and repair phase after the initial route is mapped.

Build the dossier from the existing [first-adopter kit](../../implementation/adoption/FIRST_ADOPTER_KIT.md), [institution kit](../../implementation/adoption/INSTITUTION_FOUNDATION_KIT.md), [forum kit](../../implementation/adoption/FORUM_FOUNDATION_KIT.md), [sizing guide](../../implementation/adoption/MINIMUM_VIABLE_ADOPTER.md), and evaluation procedures. Use fictional facts explicitly labeled as such. For each step record actor, input, source, output, next recipient, clock source, and unavailable-capacity outcome. Name account control, funding, removal power, and credentials: several role prompts do not establish independence.

First produce a source-traced desk walkthrough, then a fresh-session exercise. Label who prepared and who executed each stage. Keep model/version, date, source revision, full supplied facts, outputs, assistance, elapsed effort, failures, edits, and retest results. Stop a claimed adoption path where required capacity is absent; preserve any lawful ordinary-cooperation route. Never fill a missing authority with the author's personal explanation.

A trial is useful if it exposes missing handoffs or unwritten assumptions. It does not count as real adoption, human evidence, an independent second reading, or an actual sentience finding. Separate testing sessions or external participants remain to be arranged.

## Decision queue

| ID | Concrete question or proposal | Recommendation and dependency | State |
|---|---|---|---|
| D01 | Chapter Fourteen §1.1, Non-Usurpation, names “Chapter Eighteen (Ratification and Adoption)” for deliberate adoption | Replace that citation with linked **Chapter Seventeen §10 (Ratification and Adoption)**; retain Chapter Eighteen for the incorporation bridge where relevant. See [source](../../core_14000_governance.md#11-mechanism-families-auditability-and-pluralism). Core wording stays with steward | Approved by the steward in session 2026-10-20; citation correction applied |
| D02 | Publication spec §6.5 requires a human-operator costly-case sample for AI handoff-readiness claims; none was found in the examined result folders | Recruit someone with operational authority and use the existing [human-operator protocol](../../evaluation/HUMAN_OPERATORS.md). If unavailable at candidate review, explicitly decide timing or claims against the existing spec | Open evidence dependency; no waiver |
| D03 | Which chapter next enters translation under the new settled-chapter workflow? | Use an explicit English revision after steward sign-off and dependency review; preserve current translation edits until their owner reconciles them | Await chapter readiness; no translation mutation in this batch |
| D04 | How should CJS-18.110 §1's covered-body scope and emergency-only non-hybrid allowance be read with CI-9.210 §3's Class C-and-above applicability and CI-9.210 §3.2's institutional exception route? | Clarify owner-specific applicability and preserve home/rotating authority across an ordinary workflow; retain CF-13.405 §6's forum design floor. Treat CI-9.210 §3.2 as the additional safeguard/assurance route for lawful hybrid alternatives. Any broader ordinary non-hybrid exception needs an explicit choice. [Exact findings and recommendation](../reviews/announcement_interlocks_B04_2026-10-20.md#findings-and-edits) | Approved by the steward in session 2026-10-20, including the [revised emergency clause and source references](../reviews/D04_emergency_signoff_2026-10-20.md); applied to CJS-18.110 §1.1 and CI-9.210 §3.2. Wording decision closed; independent re-review not claimed |

The core audit failures are already in the steward's active Chapter Seven work, not new design questions. Record their exact diagnostics with validation results; do not weaken the audits to clear them.

## Batch and evidence log

| Batch | Scope | Result | Limits |
|---|---|---|---|
| B00, Oct 20 | Plan, tracked-file inventory, review-note pointer, backlog grouping | Working plan and inventory persisted; prior examination retained | No claim of full corpus review; no release gate closed |
| B01, Oct 20 | CI-11.205 §5 funding bullet; minimum-viable-adopter §2, estimate convention and Class B example | Carry core's documented-departure conditions into CI-11.205 and sizing guidance; state parity as the profiles' estimate assumption | Targeted alignment correction only; core unchanged; whole-file reviews still pending |
| B02, Oct 20 | [Cooperative case packet](../trials/agent_cooperative_2026-10-20/CASE_PACKET.md), [desk walkthrough](../trials/agent_cooperative_2026-10-20/DESK_WALKTHROUGH.md), source hashes; forum kit §5 | First adoption stop is missing independent review under operator control. Expanded review-naming form captures accepted authority, control, capacity, custody, clocks and failure routes | Same-author desk analysis and form-coverage retest; no fresh-session execution or whole-file review claimed |
| B03, Oct 20 | CS-6.335 §17 plain-language line | Remove implied standing prerequisite; reflect operative text's any-sentient-or-group access and preservation of challenge despite standing locks | Gloss alignment only; operative paragraph and core unchanged; CS-6.335 full review pending |
| B04, Oct 20 | Full pass of CJS-18.110, CJS-8.105 §9–1.11 and CI-9.210; [review and checks](../reviews/announcement_interlocks_B04_2026-10-20.md) | Correct formation/adjudication pointers and term gloss; carry existing seat, hosting and exercised-handoff requirements into the interlocks. Three full passes recorded; 72 pending | One file has no remaining finding in this pass; two retain D04. No independent executor result, core edit, translation sync or throughput forecast claimed |

## Validation record — October 20 batch

- `git diff --check` passed.
- Local Markdown target and fragment validation passed for all seven files edited or created in this batch. Two pre-existing custom-anchor links in TODO and MEMLOG were updated to their actual heading anchors.
- Inventory coverage reconciles to 1,377 tracked paths: 523 inventoried plus 854 separated as core, translations, or preserved history/working evidence; no duplicate inventory rows. The four implementation families account for 75 entries.
- Final `make audit-report` completed at **101/105** targets passing. Links/citations, generated outputs, cross-chapter alignment, and all audit unit tests passed. Remaining failing targets: `heading-runin-echo-audit`, `section-bullet-lead-audit`, `lexical-vocabulary-audit`, and `time-reference-audit`.
- Chapter Seven changed concurrently during this work. The structure and time diagnostics point into that ongoing core edit. This batch made no core edits, does not claim a frozen core baseline, and does not restore earlier versions over the current work. Translation files checked against the start-of-batch hashes were unchanged.
- Changes remain uncommitted. No push, external invitation, publication, or adoption was performed.

## Continuation record — October 20 formation batch

PR #101 merged B00/B01 as `637af2f2`. Fetched origin, fast-forwarded local main, and started `codex/announcement-formation-trial`, restoring inherited Chapter Seven, generated-index and translation work without including it in this batch. The baseline and previous validation entries above are historical records, not claims that current main or current changes remain at their earlier state.

B02 supplies the previously pending source-traced desk walkthrough. Initial class and dependency findings are Class L / Dep-L on explicit fictional material-reliance and replaceability assumptions. Urgency is assessed separately; no live forum intake or adoption is claimed. Reviewer loss and a conflicted substitute leave the challenge unresolved. The packet adds a changed-urgency branch to test whether later executors reopen those assumptions. No constitutional design decision is needed to detect the initial independence defect; the first repair is a more usable support form.

The scope is two targeted document repairs and a preparatory trial dossier, not the first full classification/interlock editing batch. No whole-file inventory entry is closed, no throughput forecast is revised, and no human or fresh-session evidence is claimed. Fresh-session execution is ready to arrange using the packet without the desk answer. Chapter Seven wording and translations were not edited for this batch.

During the continuation the steward's Chapter Seven work was committed separately as `616dda15`. The final source hashes match that text; this chat made no core edit or commit. The initial 101/105 baseline became **100/105** after that concurrent core update added an unnamed §4.7.1 citation. The other failing targets are unchanged: heading-runin-echo, section-bullet-lead, lexical-vocabulary, and time-reference. The [saved report](../trials/agent_cooperative_2026-10-20/audit_report.txt) records exact diagnostics; no audit was relaxed.

The expanded vocabulary diagnostic identifies `corpus-no-bare-charter` in Chapter Seven at lines 548 ("Your Charter sets the length") and 674 ("which the Charter sets"). The compact report prints the vocabulary policy header rather than those individual findings; the expanded check confirms both failures belong to the steward's core text.

`git diff --check` and local Markdown file/fragment checks passed for all nine changed Markdown files. A focused vocabulary check passed for both new trial documents; it does not establish a whole-file vocabulary pass for inherited support text. Source-manifest hashes were checked against the current files, and a pre-final-audit content snapshot confirmed no subsequent change to Chapter Seven or any translation file, draft, or translation tool. Generated indexes were refreshed by the standard audit workflow, not edited by hand. Whole-checkout checks remain subject to concurrent source work.

No commit, push, external invitation, release or adoption was performed by this chat in this continuation.

## B04 validation and continuation

The [full B04 record](../reviews/announcement_interlocks_B04_2026-10-20.md) and [saved audit](../reviews/announcement_interlocks_B04_audit_2026-10-20.txt) record **98/105** targets passing. Seven targets retain findings in concurrently edited Chapter Seven. The three edited implementation files pass focused vocabulary checks; all nine changed Markdown files in this continuation pass local link checks. Article-title checks, cross-chapter alignment, generated-file checks and audit unit tests pass. The obsolete CI-9.210 time-reference entry was removed from the shrink-only baseline, 78 to 77, with no additions.

All 24 direct dependency hashes and three reviewed-file hashes match the final source check. The protected snapshot confirms translation/draft/tool preservation; Chapter Seven changed concurrently, and this chat made no core edit. B04 remains uncommitted. No push, publication or adoption was performed. D04 stays open, and fresh-session trial execution requires a new source baseline.

## Next session entry point

1. Read this plan's batch log and decision queue, then current TODO and MEMLOG. Check branch and sync main without losing unrelated work.
2. Rebaseline the formation case packet against current Chapter Seven before fresh execution; its original hash is historical. Execute in a fresh session without the desk answer. Preserve source differences, outputs and assistance; human-operator evidence remains a separate dependency.
3. Continue from B04: resolve D04's hybrid applicability/exception boundary, then review CS-9.305 and CS-9.310 Parts A/B. Three whole-file passes are recorded and 72 remain pending; two reviewed files still have an open finding. Full review effort was not measured, so do not extrapolate a schedule from the implementation timestamp.
4. Record substantive choices, reassess changed core dependencies, and continue chapter-readiness scheduling separately from English editing.

Publication still requires the existing spec's criteria, completed planned reviews, resolved or explicitly assessed material failures, faithful translations at the agreed scope, green checks, accurate public claims, and the steward's final decision. This file supplies a route to that assessment; it does not declare it achieved.
