# Draft: Process-ownership disputes (proposal, not adopted text)

**Status:** working draft for author review. Not part of the numbered `core_*` files. Nothing here has been run through the audits (`make plain-language-audit`, lexical guardrails).

**Problem.** Once the Constitution is in use, stewards who own how and when a process runs will collide with stewards who own what affected sentients are owed. Chapter Twelve routes disputes about forums, jurisdiction and standing, but no rule says who decides a dispute about *who owns a process or may change it*. This draft closes that gap without adding a third governance layer to Preamble §3.3.

**Placeholder terms.** "Process steward" and "stakeholder steward" below are descriptive placeholders. They need mapping to whatever roles the Corpus actually names (check `corpus_institutions.md` and `STEWARD_ENTRY_DOORS.md`) before adoption.

---

## Part 1. Proposed text for Chapter Twelve §3

Insert after **Cross-forum anti-self-judging rule**, same section, same house style.

*In plain terms: stewards who run a process may change how and when it runs, in the open and with a chance to object. They may not change what affected sentients are owed. When the two sides disagree about which kind of change this is, an independent forum decides, not either steward group.*

**Process-ownership disputes.** A dispute over who owns an operating procedure, or whether a procedure change was within the owner's authority, is a **process-ownership dispute**.

- **Owner envelope.** An owner of a procedure may change how, when, by whom, on what record, and on what clock a duty is carried out. An owner may not change what is owed, to whom, or at what threshold.
- **Floor-touching change.** A procedure change is **floor-touching** if it would, in practice, do any of the following:
  - delay a remedy or lengthen a clock beyond the **Article XXV-C** tier outer bounds;
  - narrow who may participate, be represented, or contest;
  - remove, hide, or make costlier a published challenge path;
  - reduce the record available to an affected sentient or to a reviewing forum.
- **Floor-touching changes are constitutional questions.** They are not decided by the procedure's owner alone. They go to certification under **section 5**.
- **Change record and contest window.** A material procedure change must carry a public change record (reasons, expected effects, and the clocks or paths it touches) under the **Material-change record** floor in **Article XXVI-B**. It takes effect only after a published contest window. Retroactive change of a pending matter's procedure is not allowed unless the affected sentient consents or an interim order under **section 5** permits it.
- **Lead forum.**
  - Disputes about ownership or scope of a procedure go first to the **Institutional** forum, which already applies **section 4.7** operational law.
  - A dispute whose primary issue is that the owner's own process is biased, captured, or abusive is covered by the **cross-forum anti-self-judging rule** and routes as that rule assigns.
  - Where the dispute turns on whether a change is floor-touching, the Institutional forum certifies the question to the **Constitutional** forum under **section 5**. It keeps the operational remainder.
- **No self-judging by the rule-writer.** The steward group that wrote or changed a procedure may not be the sole final decider of a challenge to that change. Role-separation lanes **CI-3** and **CI-6** apply.
- **Interim rule.** While a process-ownership dispute is pending, the prior published procedure stays in force unless an interim order under **section 5** says otherwise. One coordinating forum or rule resolves conflicting interim orders, as **section 5** already requires.

## Part 2. Companion text for the implementation corpus (outline only)

To sit in `corpus_institutions.md` near **CI-6** (procedure), not in the core:

1. **Change-record template.** Fields: what changed, who owns it, which clocks and paths it touches, floor-touching self-assessment, contest window dates.
2. **Floor-touching self-assessment.** The owner states yes or no for each of the four triggers above. A "no" can be challenged.
3. **Contest window length.** Scaled to the **material stake** tiers already in **Chapter Twelve §6**, not a new set of numbers. (Open question 3.)
4. **Emergency changes.** Allowed, but sunset to the prior procedure unless ratified within the contest window. This mirrors the continuation burden in **section 6.1**.

## Part 3. Integration notes

**What this reuses.** Institutional forums and **section 4.7**, certification under **section 5**, the anti-self-judging assignments, interim protection and coordinating-forum language, the **Article XXV-C** anti-delay floor and material-change record, and role-separation lanes **CI-3** and **CI-6**.

**What is new.** The term *process-ownership dispute*, the *floor-touching* test, the contest window, and the "prior procedure stays in force" interim default.

**What it does not do.** It does not add a governance layer to Preamble §3.3 and does not change who may govern. It stays on the Stakeholder System Participation side and relies on forum review.

**Likely edit footprint.** Chapter Twelve §3 (new subsection), one pointer from §2.2 (mixed stakes), `corpus_institutions.md` (CI-6 companion), the Chapter Twelve Trace widgets, and the generated indexes. Translations would follow after English is settled.

## Part 4. Open questions for the author

1. **Is "floor-touching" the right test?** It is deliberately narrow, tied to Article XXV-C, Participation and Contestability. Too narrow lets process stewards erode rights through small steps. Too broad turns every form change into a constitutional case.
2. **Who files?** Any materially affected sentient, or only designated stakeholder stewards? Steward-only filing risks a new gatekeeper.
3. **Contest window length** and whether it should differ by tier.
4. **Pattern abuse.** Many small non-floor changes can add up to a floor-touching one. Should the forum be able to treat a series as one change?
5. **Standing of process stewards.** Can they bring a dispute against stakeholder stewards, for example over an unfunded or open-ended demand? Probably yes, which implies a symmetric rule.
6. **Pre-release stance.** Adopt now, or announce it as a known open design item and adopt with the first amendment cycle?
