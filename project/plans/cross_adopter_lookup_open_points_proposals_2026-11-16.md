# Proposals for review: four open points in the cross-adopter lookup text — 2026-11-16

This page is **process support**, not constitutional text. **Status: decided by the custodian and entered in core on 2026-11-16 (567th move); the sections below are the proposals as first written, and *Outcome of the walk-through* controls where they differ.** It follows the 564th move, which entered Chapter Twenty [§2.4](../../core_20.000_final_effect_restoration_enforcement.md#24-gatekeeper-checks-across-adopters-and-levels-of-trust) and left four points open: conflict of interest, time windows, small adopters, and the Chapter Seven custody map. Each point below gives what source says now, the gap, options, and a recommended default. Companion to the [framework draft](cross_adopter_standing_lookup_framework_draft_2026-11-16.md).

**Source-check limits.** I read Chapter Twenty §2.1 and §2.4, Chapter Twenty-Three §3 (cross-forum anti-self-judging rule) and *Backup Routing under the Anti-Self-Judging Rule*, CF-23.410 §5, Chapter Seven §5.6, Chapter Fifteen §6 (opening lines only), [CJS-0.105 §4](../../corpus_joint_structure/cjs_00.105_registry_and_reading_rules.md#cjs-0105-4-time-window-names), and the [minimum-viable adopter profiles](../../implementation/adoption/MINIMUM_VIABLE_ADOPTER.md). I did not read CI-8.210, CF-23.415, or the full Chapter Twenty-Four §2 tier table. The independent read of the §2.4 text remains shelved.

## 1. Conflict of interest (answer 3 in the framework draft)

**What source says.** CF-23.410 §5 already requires a member to step aside for a material conflict under CI-8.210, a direct institutional stake, or prior involvement in the same matter. Chapter Twenty-Three §3 bars a forum family from being the sole final merits forum for a claim whose primary issue is that family's own bias, capture, conflict, or recusal failure. §2.4 adds that the forum deciding a level of trust must be separate from the record custodian seat for the records concerned, and that "no adopter is the sole final judge of a decision that concerns itself."

**The gap.** Two cases fall through.
- **Self-review on contest.** Adopter A's Institutional Forum sets the level it extends to B. If B contests, §2.4 sends the contest to "the forum with jurisdiction over the events the dispute concerns." A level-of-trust decision concerns the relationship between the adopters, not any one standing event, so that phrase does not point anywhere clear. Where the events sit at A (the usual case, since A holds the record), it points back to A's own forum family, which reviews its own decision. The §3 rule does not fire, because the contest alleges a wrong decision, not the family's bias.
- **Interested decider.** A's forum decides how far A trusts B. A may gain from lowering B's level (a competitor, a rival standard, a data-custody dispute). Recusal covers an individual member's conflict. It does not cover a forum that is structurally interested because its adopter is a party in interest.

**Options.**
- **A. Recusal only.** Rely on CF-23.410 §5. Cheapest, but it leaves the self-review case open.
- **B. Outside review (recommended).** In the *Contest* bullet of §2.4, state that a contest of a level-of-trust decision is not decided as final merits by the family that made it. First-instance review is by a different panel from the deciding panel, and final merits go to a forum outside the deciding adopter. This reuses the phrase §2.4 already applies to departures from technical advice, so the text stays consistent. Default family: the Chapter Twenty-Three §3 row for claims against Institutional forums (Constitutional first, Integrity as backup), so no new routing is invented. The custodian may prefer Integrity first, since a level-of-trust decision is mainly a custody and integrity question.
- **C. Third-adopter panel.** A and B each name a neutral adopter's Institutional Forum. Closer to a treaty model, but it needs a third adopter that exists and is willing, so it fails for the first two adopters.

**Recommended default: B**, plus a sentence that a waiver by either adopter may not route the contest back to the deciding adopter's own forum family.

**Also open under this point.** Whether "the events the dispute concerns" in the *Contest* bullet should be reworded for level-of-trust decisions, since answer 2 in the draft left that unresolved. Under B the phrase would apply only to contests about an individual answer or lock, and not to the level decision.

## 2. Time windows (draft question 8)

**What source says.** The standing decisions say "promptly" is not a length, a "reasonable" period is 14 days, new windows take a name ending in a kind word (window, target, bound, interval) and are listed in CJS-0.105 §4 with their owner, and the numbers stay with the owners. §2.4 names no window anywhere. The existing named windows include the **prompt-review window**, the **restore-challenge window**, the **response window**, and the **tier window**.

**Gaps, in order of weight.**
1. **Answering a gatekeeper check.** §2.1 says the gatekeeper "is entitled to an answer" and names no time. This gap exists at home too, and it matters more across adopters (office-level contact, other legal setting). Silence is the dangerous case: if no answer arrives, a gatekeeper may read it as "nothing found" or as a bad sign, and the subject loses the job on a non-answer.
2. **Lowering a level of trust.** §2.4 requires "notice to the other adopter and a chance to contest" with no length for either, and says lowering is on published reasons, with no say on whether it takes effect before the contest ends.
3. **Publishing a new dated version.** "Raising or lowering a level of trust is a new dated version," with no rule on when it takes effect relative to publication.
4. **Stale entries.** Chapter Five calls an Adoption Charter that is "stale" or dead a failure, and no interval defines stale. The same holds for the office-level contact.

**Options.**
- **New names, minimal.** Two additions: a **check-answer window** (owner: Chapter Twenty §2.1) and a **Adoption Charter review interval** (owner: Chapter Twenty-Nine §11.4). Everything else reuses existing names.
- **Reuse for lowering.** Treat an immediate lowering (for passing an answer on, refusing an audit, or a key failure) as a measure in force. It then falls under the **prompt-review window**, so review starts within the tier's intake length, and the **restore-challenge window** if it is handled as an emergency measure under Chapter Twenty-Four §2.1. A lowering that is not urgent takes effect on the later of publication and the end of the other adopter's notice period, with the contest handled as an ordinary matter under its tier window. This adds no new number.
- **Silence rule.** Whatever length is chosen, state that no answer by the end of the window is never the "none applies" answer and never an adverse fact about the subject. It counts as a failure of the answering custodian, and the gatekeeper decides on the gated pathway without that input, or waits, at the subject's choice.
- **Length of the check-answer window.** This is the custodian's number. Anything above 14 days would be longer than the project's own meaning of "reasonable," which hiring and appointment decisions probably cannot bear. I have not proposed a figure.

**Recommended default.** The two new names, reuse for lowering, and the silence rule. The number for the check-answer window and the Adoption Charter review interval stay with the custodian.

## 3. Small adopters (draft question 9)

**What source says.** In [MINIMUM_VIABLE_ADOPTER.md](../../implementation/adoption/MINIMUM_VIABLE_ADOPTER.md), a 2–40 person crew (Profile 1) is operations-guide use, not adoption. It has no adoption document, so it has no Adoption Charter or Adoption Transition Record and, under §2.4, can extend only the public level. Profile 3 (40–200, hosted families) adopts and maps the six forum families onto existing independent bodies. §2.4 already says an adopter without even a provisional forum authority assignment extends only the public level, and one with provisional entries extends no more than the notice level.

**The gap.** The text is already safe for the smallest crews, because they stay at the public level. The open risk is the middle: a small adopter that has adopted and wants the query level, but whose custodian and forum cannot be separated from its few staff, or whose hosted forum also serves the adopter on the other side.

**Options.**
- **A. No special rule (recommended for now).** The query level already needs a published custody and key practice, Technical Forum Domains advice, and an independent check of custodian separation. A small adopter that cannot pass those stays at the notice level. That is a cost consequence, not a rule change.
- **B. Hosted custodian route.** State that a small adopter may satisfy the separation test by naming a hosted record custodian, with the Backup Record Custodian (CF-23.415 §9) as the default where it names none. This matches Profile 3's pattern and Chapter Seven §5.6.1, which already gives backup custodians as the default for gaps.
- **C. Shared-forum conflict sentence.** If one hosted Institutional Forum serves both adopters, state that it may not decide a level-of-trust contest between them, and a forum outside both decides under point 1, option B.

**Recommended default: A for the text, with C added to point 1's sentence** so the hosted-forum case does not need its own rule. Option B is worth a line in the kit checklist as practice, not as core.

## 4. Chapter Seven custody map (draft question 6)

**What source says.** Chapter Seven §5.6.1 requires the Charter Role Map to name four seats for operator standing records, including a separate custodian. §5.6.2 says that for **stakeholder** standing records, naming offices is optional, and "a map that names none is still valid"; the default then is the Backup Record Authority and Backup Record Custodian or a forum. §2.4 sends a gatekeeper to "the office-level contact named in that adopter's Adoption Charter."

**The gap.** The draft concluded the Chapter Seven map "stays as it is." That holds for operator records. A gatekeeper check is about an individual sentient's record, which will usually be a stakeholder record. For those, the map may name no custodian at all, an adopter can have many charters with different maps, and the Adoption Charter's single "record custodian" entry may not match any of them. A gatekeeper could then reach a contact that holds nothing and cannot say who does.

**Options.**
- **A. Leave both as they are.** Leaves the mismatch.
- **B. Define the entry (recommended).** In Chapter Twenty-Nine §11.4, say the Adoption Charter's contact is a **routing contact**: it either holds the record or tells the gatekeeper which custodian does, using the maps that apply and, where a map names none for stakeholder records, the Backup Record Custodian default. The Chapter Seven map is unchanged, and no new required item is added there.
- **C. Add a required map item.** Chapter Seven would require every map to name a gatekeeper-check contact. This changes a core chapter that other work depends on and would invalidate existing maps until they are amended.

**Recommended default: B.** It keeps the earlier custodian direction (Chapter Seven unchanged) and closes the mismatch in the one chapter already changed.

## Outcome of the walk-through (custodian, 2026-11-16)

| # | Decision | Outcome |
|---|---|---|
| 1 | How a level-of-trust contest avoids self-review | **Changed:** no outside contest at all; the decision is internal to the adopter. Institutional Forum decides; reasons, advice and notice stay; Heightened Scrutiny stays; own sentients may challenge internally |
| 2 | Which family hears it first | Moot (no outside contest) |
| 3 | New window names | Check-answer window and Adoption Charter review interval |
| 4 | Lengths | 4 calendar days; 14 calendar days (non-urgent notice); 12 months |
| 5 | Silence | No inference; the subject chooses |
| 6 | Immediate lowering | Immediate if the Institutional Forum finds it urgent, otherwise after 14 days' notice |
| 7 | Small adopters | No special rule; hosted forum serving both adopters discloses the conflict in its reasons |
| 8 | Adoption Charter contact | Routing contact; Chapter Seven unchanged |

The sections above are the proposals as first written; the decisions below and this table supersede them where they differ.

## Decisions made in session (custodian, 2026-11-16)

Recorded as the walk-through goes; nothing below is entered in core yet.

- **Decision 1 (contest review): changed from my proposal.** The custodian ruled that a level-of-trust decision is "essentially a foreign policy decision" and is **internal to the adopter that lowers (or raises) the level**. The other adopter has **no right to contest** it. What stays: the Institutional Forum decides, separate from the record custodian seat, advised by Technical Forum Domains; the decision, reasons and advice are published in the Adoption Charter; notice goes to the other adopter as a courtesy; a departure from technical advice still meets Heightened Scrutiny (outside review in that one case); and sentients under the lowering adopter's authority may challenge the decision through that adopter's own forum process. §2.4's *Contest* and *Lowering a level of trust* bullets would change accordingly; the "chance to contest" for the other adopter goes. Locks already in force stay protected under Chapter Twenty §4.3 ("No relationship, no escape" is unchanged).
- **Decision 2 (which family hears it first): moot** for the other adopter. It survives only for an internal challenge, which the existing forum appeal and recusal rules cover; no new routing proposed.
- **Decision 6 (when a lowering takes effect): decided.** Situational: **immediate if urgent, after notice if not**, and the **Institutional Forum decides urgency** in its published reasons (no fixed list of urgent grounds; the three grounds in §2.4 are examples at most). Open: the length of the notice period for a non-urgent lowering, and whether urgency must be stated with reasons the other adopter receives.
- **Decision 3 (new named time limits): decided.** Add both a **check-answer window** (owner: Chapter Twenty §2.1) and a **Adoption Charter review interval** (owner: Chapter Twenty-Nine §11.4), each listed in CJS-0.105 §4. Lengths are decision 4.
- **Decision 4 (lengths): decided.** **Check-answer window: 4 calendar days** (the Tier C intake target, CF-23.445 §5.1). **Notice period for a non-urgent lowering: 14 calendar days** (the project's meaning of "reasonable"; urgent lowerings take effect at once). **Adoption Charter review interval: 12 months.** Each goes into CJS-0.105 §4 with its owner; the numbers stay with Chapter Twenty §2.1 and Chapter Twenty-Nine §11.4. The notice period is a third new name unless it is written as a plain 14-day period in §2.4 (to settle when entering the text).
- **Decision 5 (silence): decided.** Silence is **never the "none applies" answer and never an adverse fact about the subject**. It counts as a failure by the answering custodian. The gatekeeper may wait, or decide that pathway without the answer, **at the subject's choice**. No Backup Record Custodian fallback was added.
- **Decision 7 (small adopters): decided.** **No special rule** for small adopters: one that cannot meet the query-level requirements stays at the notice level. For a hosted Institutional Forum that also serves the other adopter, the forum may decide, but its **published reasons must disclose that it serves the other adopter and how the conflict was screened**; existing recusal rules (CF-23.410 §5) cover members. The hosted-custodian route was not adopted.
- **Decision 8 (Adoption Charter contact): decided.** The Adoption Charter's contact is a **routing contact**: it either holds the standing record or tells the gatekeeper which custodian does, using the maps that apply and, where a map names none for stakeholder records, the Backup Record Custodian default (CF-23.415 §9). **Chapter Seven is unchanged**; the text goes in Chapter Twenty-Nine §11.4.

## Where each would go if adopted (not decided)

Chapter Twenty §2.4 (*Contest*, *Lowering a level of trust*, *Direction*) and §2.1 (*Gatekeeper check*); Chapter Twenty-Nine §11.4 (the routing contact and Adoption Charter review interval); [CJS-0.105 §4](../../corpus_joint_structure/cjs_00.105_registry_and_reading_rules.md#cjs-0105-4-time-window-names) (the two new names); the kit checklist in [FIRST_ADOPTER_KIT.md](../../implementation/adoption/FIRST_ADOPTER_KIT.md#41-adoption-transition-record-and-adoption-charter-kit-practice); the Chapter Twenty-Three §3 table only if the custodian prefers extending it. Chapter Seven stays unchanged under every recommended default. Translations are paused.

## Not done

No core, kit, schema, or audit file was edited. No worked example or regression scenario was written. No independent read of these proposals.
