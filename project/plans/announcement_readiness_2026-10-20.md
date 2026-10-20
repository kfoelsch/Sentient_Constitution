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

Main is current at `34810bf6` after PR #100. This work is on `codex/announcement-readiness`. The inherited Chapter Seven changes and translation work are preserved and excluded from this editing batch.

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

Suggested implementation order: classification and shared interlocks (CS-3, CJS); formation and independence (CI-3/4/5, CF-3/4/7/16); operational handoffs and clocks (CF-5/6/11/12/13, CI-6/7/8/12); remedy and failure (CI-13/27/28, CF-9/14, CS-7/10/11/12); remaining systems and domain companions. Read the necessary dependency sources even if their full editing batch comes later. Review guides and templates alongside their owners, then perform a final cross-stack pass.

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
| D01 | Chapter Fourteen §1.1, Non-Usurpation, names “Chapter Eighteen (Ratification and Adoption)” for deliberate adoption | Replace that citation with linked **Chapter Seventeen §10 (Ratification and Adoption)**; retain Chapter Eighteen for the incorporation bridge where relevant. See [source](../../core_14_governance.md#11-mechanism-families-auditability-and-pluralism). Core wording stays with steward | Proposed; core unchanged |
| D02 | Publication spec §6.5 requires a human-operator costly-case sample for AI handoff-readiness claims; none was found in the examined result folders | Recruit someone with operational authority and use the existing [human-operator protocol](../../evaluation/HUMAN_OPERATORS.md). If unavailable at candidate review, explicitly decide timing or claims against the existing spec | Open evidence dependency; no waiver |
| D03 | Which chapter next enters translation under the new settled-chapter workflow? | Use an explicit English revision after steward sign-off and dependency review; preserve current translation edits until their owner reconciles them | Await chapter readiness; no translation mutation in this batch |

The core audit failures are already in the steward's active Chapter Seven work, not new design questions. Record their exact diagnostics with validation results; do not weaken the audits to clear them.

## Batch and evidence log

| Batch | Scope | Result | Limits |
|---|---|---|---|
| B00, Oct 20 | Plan, tracked-file inventory, review-note pointer, backlog grouping | Working plan and inventory persisted; prior examination retained | No claim of full corpus review; no release gate closed |
| B01, Oct 20 | CI-27.5 funding bullet; minimum-viable-adopter §2, estimate convention and Class B example | Carry core's documented-departure conditions into CI-27 and sizing guidance; state parity as the profiles' estimate assumption | Targeted alignment correction only; core unchanged; whole-file reviews still pending |

## Validation record — October 20 batch

- `git diff --check` passed.
- Local Markdown target and fragment validation passed for all seven files edited or created in this batch. Two pre-existing custom-anchor links in TODO and MEMLOG were updated to their actual heading anchors.
- Inventory coverage reconciles to 1,377 tracked paths: 523 inventoried plus 854 separated as core, translations, or preserved history/working evidence; no duplicate inventory rows. The four implementation families account for 75 entries.
- Final `make audit-report` completed at **101/105** targets passing. Links/citations, generated outputs, cross-chapter alignment, and all audit unit tests passed. Remaining failing targets: `heading-runin-echo-audit`, `section-bullet-lead-audit`, `lexical-vocabulary-audit`, and `time-reference-audit`.
- Chapter Seven changed concurrently during this work. The structure and time diagnostics point into that ongoing core edit. This batch made no core edits, does not claim a frozen core baseline, and does not restore earlier versions over the current work. Translation files checked against the start-of-batch hashes were unchanged.
- Changes remain uncommitted. No push, external invitation, publication, or adoption was performed.

## Next session entry point

1. Read this plan's batch log and decision queue, then current TODO and MEMLOG. Check branch and sync main without losing unrelated work.
2. Complete the small-agent formation desk walkthrough and record the first unavailable authority or capacity, if any.
3. Use those findings to run the first full classification/interlock editing batch. Measure scope and effort before updating November forecasts.
4. Review the trial with fresh sessions or participants, record substantive choices, and continue core-dependent translation scheduling.

Publication still requires the existing spec's criteria, completed planned reviews, resolved or explicitly assessed material failures, faithful translations at the agreed scope, green checks, accurate public claims, and the steward's final decision. This file supplies a route to that assessment; it does not declare it achieved.
