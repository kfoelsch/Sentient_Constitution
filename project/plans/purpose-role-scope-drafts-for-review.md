# Purpose, Role, and Scope: drafts of the 16 stub sections, for steward review

Date: 2026-11-13. Follows `purpose-role-scope-standardization-evaluation.md` (same folder; retitle approved; "chapter scope" label approved; Owner Non-Relocation renames approved; Chapter 28 §5 title deferred; corpus files in this pass). Written against `main` at `ba5314de`. **All 16 are inserted on a separate local branch, `purpose-role-scope-ch3`, off `main` (commit `382fa9f7`; not pushed, not merged; `make preflight` passes 80/80).** The inserted text differs from these drafts only where audits required it: section cites become bold "**section N**" in the Chapter Twenty-One style, first mentions of chapters are linked, chapter-scope "covers" lists are bulleted, and a few lines were reworded (bare "record", "Charter", "designation", and "pathway" terms; near-copies between Chapters Ten/Thirteen and Eleven/Fourteen; the Chapter Twenty-Eight "title pending" note was dropped). These are the drafts the plan's step 2 asks the steward to approve before the scripted pass.

This file is also kept in the Sentient Constitution Project on claude.ai. Paths starting `claude/` name Project docs, not repository files.

## How the drafts are built

Each draft follows the Chapter Twenty-One model, under the standard heading **"Purpose, Role, and Scope"**: an *In plain terms* gloss, then three bold lead-ins, **Purpose**, **Role**, and **Chapter scope**.

- **Purpose** is the question the chapter answers and what it produces.
- **Role** is what the chapter takes as fixed from upstream and what it hands downstream.
- **Chapter scope** is what the chapter covers, in order, as pointers, and what it leaves to other chapters. Each "leaves to" item names the owner and appears only because it matters here.

Every sentence restates something already in the chapter, its placement box, or the chapter it points to. No duty, authority, threshold, clock or scope changes. Cites are written in plain text here. At insertion they become links with section titles, and the lead-in and list-intro audits (MD-SECTION-LEAD-01, MD-LIST-INTRO-01, SECTION-CITE-NAME-01) get applied then. The chapter-scope label is used only for the chapter itself, never for adoption scope, charter scope, or the scope of an article.

Chapter 7 needs care: a Charter is itself a scope document, so its draft says "chapter scope" for the chapter and "Charter" for the document throughout.

Chapters 15 and 16 already carry scope statements outside §1 (Chapter Fifteen §2.1 "Purpose and Scope" and Chapter Sixteen §2.3 "Question 2 Only — Scope and Routing"). Their drafts point to those subsections and do not restate them. See "Needs a decision" at the end.

---

## Chapter Three: Definition Integrity, Evasion, and Non-Compliance

*In plain terms: this chapter says when a system fails a definition in practice: when what it does or produces would violate the definition, or when the definition is weakened at the point where it is applied. It sets what counts as failing. It does not say who must prove it.*

**Purpose.** Chapter Two sets how every definition is built. Chapter Three answers what it means to fail one. A system is non-compliant when its actual behavior or output would violate a definition, judged under full functional conditions and not only on paper (§3). Weakening a definition when it is applied is also non-compliance, whatever the intent, awareness, or claim (§2; Chapter Two §2.2 *Non-Compliance by Structural or Applied Weakening*). The chapter also provides finding profiles, optional labels that name the kind of constitutional problem for routing and audits (§4).

**Role.** The chapter sits between how definitions are built and how compliance is proved:

- Chapter Two says how every definition is built. This chapter starts from that and does not change it.
- Chapter Four picks up from here and says who has to prove compliance, and how.
- Some verified violation findings also feed standing, the record of a party's verified help and harm. §4.1 to §4.3 say when: for systems that are already certified, for systems at their first certification, and for sentients and institutions, who are tagged only when the link to the violation finding is verified.

**Chapter scope.** The chapter covers:

- the integrity and anti-evasion constraints (§2);
- non-compliance from observable behavior, with its evasion patterns and constraints (§3); and
- finding profiles (§4), which never change the pass or fail result.

The chapter leaves:

- burden of proof, traceability, and verification to Chapter Four;
- how a definition is structured to Chapter Two; and
- standing records and their effects to the standing pipeline, Chapters Fifteen through Twenty.

---

## Chapter Four: Burden of Proof, Traceability, and Verification

*In plain terms: if you claim compliance, you prove it, through one five-step check. The proof has to be real, open to inspection in practice, and checkable by others, even where security narrows how or when it is shown.*

**Purpose.** Chapter Four answers who must prove compliance and how the proof must look:

- the party claiming compliance carries the burden through one five-step check (§2);
- it must show a map from each definition's parts, Ontological, Measurement, Assessment, and Compliance, to what the system actually does (§3), and must expose enough of itself for that map to be checked in practice (§4);
- security can narrow how, when, and to whom disclosure happens but cannot erase the duty to trace and verify (§5); and
- evidence must be tied to the map, independent where possible, complete, and sustained (§6).

**Role.** Chapters Two through Four together set the rules every compliance claim must meet:

- It takes definition mechanics from Chapters Two and Three, and definitions from Chapter Five, as fixed.
- It hands those rules to Chapter Nine, where System Alignment Certification applies them, and to Chapter Fifteen, where standing records rest on verified facts.
- A current certification is not a way around Chapters Two through Four (§7).

**Chapter scope.** The chapter covers burden allocation (§2), traceability (§3), observability (§4), security-constrained verification (§5), the compliance evidence standard (§6), and the relationship to System Alignment Certification (§7). It leaves:

- the certification process itself to Chapters Nine through Fourteen;
- the meaning of each definition to Chapter Five; and
- standing records and their effects to Chapters Fifteen through Twenty.

---

## Chapter Seven: System and Institutional Charters

*In plain terms: before anyone can judge whether a system or institution stayed within its limits, the limits have to be written down where everyone can read them. This chapter says who must publish a System Charter or an Institutional Charter, what each must state, and how it is checked and kept true. Nobody needs permission to form.*

**Purpose.** Chapter Seven decides when a system must publish a System Charter and when an institution must publish an Institutional Charter (required at Class L or higher, voluntary at Class P), the minimum each must state, how each changes and is reviewed, and the formation check on the standing and authenticity of the holders of covered offices.

**Role.** The chapter follows the Chapter Six Rights Floor and comes before the seats in Chapter Eight:

- It applies the terms System Charter, Institutional Charter, Charter Role Map, Chartered Party, and Operating Party, which Chapter Five defines. It does not redefine them.
- Chapter Eight §5 *Published Placement, Vacancy, and Substitution* requires the Charter Role Map this chapter describes.
- Chapter Nine reads the System Charter for scope and boundary findings, and Chapter Twelve tests the formation check statement for an Institution.
- Chapter Fifteen §6 applies the Charter Role Map to standing records, and Chapter Twenty-Three §4.3 hears disputes about the Institutional Charter.
- CI-8.205 (*Institutional Design, Separation of Powers, and Authority Custody*) §6 holds the full field template, review checklist, and formation procedure. It may be stricter and may not narrow this chapter.

**Chapter scope.** The chapter covers, in order: when Charters are required (§2), the right to form and five narrow limits (§3), what they must state (§4), the Charter Role Map and standing-record custody (§5), the formation check (§6), when a holder fails it (§7), and amendment, review, and scope misalignment (§8). It leaves:

- the seats and separation of duties to Chapter Eight;
- the definitions to Chapter Five; and
- disputes about an Institutional Charter to Chapter Twenty-Three §4.3.

---

## Chapter Ten: System Alignment Certification — Forum Process and Outcomes

*In plain terms: once a system has been evaluated, independent forums review the result in a set order and publish an outcome. This chapter says how the forums work and what outcomes they can reach, including the gate before go-live.*

**Purpose.** Chapter Ten states the forum process for System Alignment Certification (SAC): component roles, the supervisory sequence, the contestability chain, and the anti-bypass rule (§2). It then states the certification outcomes: the go-live gate, certification defects and correction, remediation readiness, denial and revocation, and their effects (§3).

**Role.** The chapter is jointly owned with Chapters Nine and Eleven, which together own forum-supervised SAC and the related System Certification Records:

- It takes the evaluation outputs of Chapter Nine §2 through §5 as the inputs the forums review and the outcome rests on.
- It rests on Chapter Eight (functional independence), Chapter Twenty-Three (forum supervision), and Chapters Two through Four (verification discipline).
- It hands the System Certification Record, recertification, challenge, and the standing bridge to Chapter Eleven.
- Under the oversight leg of the Tetrad, SAC is one especially large, high-stakes audit process among others. The auditing floors stay at Article XVI and Chapter Five *Auditability*.

**Chapter scope.** The chapter covers the forum process (§2) and the certification outcomes (§3). It leaves:

- evaluation mechanics to Chapter Nine and canonical definitions to Chapter Five;
- standing measurement to Chapter Sixteen and standing effects to Chapter Seventeen; and
- ownership of auditing to Article XVI, Def.O1, and CJS-5.110 (*Oversight Leg Operations (oDef.2–oDef.6)*) and CJS-5.115 (*Audit Process Home (oDef.3)*).

The standing bridge is Chapter Eleven §5.

---

## Chapter Eleven: System Alignment Certification — Records, Recertification, Challenge, and Standing

*In plain terms: a certification only works if it is kept where it can be checked, re-checked on a schedule, challenged when it is wrong, and kept separate from standing. Certification can feed standing, but it is not standing.*

**Purpose.** Chapter Eleven states what happens after the outcome. It sets the minimum contents, transparency, and auditability of the System Certification Record (§2), recertification on a schedule set by system class, reopening triggers, provisional and full certification, and non-evasion (§3), the path for challenging a certification (§4), and the relationship to standing (§5).

**Role.** The chapter closes the System Alignment Certification sequence:

- It takes the outcome from Chapter Ten, and the evaluation and class framing from Chapter Nine, as fixed.
- It hands verified facts to Chapter Fifteen only through the verified-input gate (§5.3).
- Standing records and their effects are decided in Chapters Fifteen and Twenty, not here.

**Chapter scope.** The chapter covers the System Certification Record (§2), recertification and reopening (§3), challenge (§4), and the standing bridge (§5). It leaves:

- the forum process and outcomes to Chapter Ten;
- evaluation to Chapter Nine; and
- standing measurement and standing effects to Chapters Sixteen and Seventeen.

---

## Chapter Thirteen: Institutional Alignment Certification — Forum Process and Outcomes

*In plain terms: the same independent forums, in the same order, review the institution, and the institution never chooses its own reviewer. A published outcome never decides whether the institution may exist or operate.*

**Purpose.** Chapter Thirteen states how forums supervise institutional alignment certification: the four seats in an institutional certification, forum roles and sequence, and forums, certifiers, and record offices treated as institutions (§2). It then states the outcomes: go-live for an Institution, defects and correction, remediation readiness, denial and revocation, and their effects (§3). An outcome decides what the Institution may say about itself, who is warned, and how much the outcome counts when the Institution's Systems are reviewed. The forums can also limit the specific practice or authority the review found at issue.

**Role.** Institutional certification and System Alignment Certification are two certifications joined by a link, not one inside the other (Chapter Twelve §1):

- It takes the evaluation from Chapter Twelve as fixed.
- It runs the same forum process as Chapter Ten, applied to an Institution.
- It cites System Certification Records by link and does not redo them.
- Chapter Fourteen takes over from here, with the Institutional Certification Record, recertification, challenge, and the standing bridge.

**Chapter scope.** The chapter covers the forum process (§2) and the outcomes (§3). It leaves:

- evaluation to Chapter Twelve;
- the Institutional Certification Record, recertification, challenge, and standing bridge to Chapter Fourteen; and
- every System-level decision to Chapters Nine through Eleven.

---

## Chapter Fourteen: Institutional Alignment Certification — Records, Recertification, Challenge, and Standing

*In plain terms: the outcome is kept on an Institutional Certification Record held by an office the institution does not control. The certification is re-checked on a schedule and when something material changes, and it can be challenged. It may feed standing, but it is a separate thing from standing.*

**Purpose.** Chapter Fourteen states what happens after an institutional outcome. It sets the contents, transparency, and auditability of the Institutional Certification Record (§2), monitoring and recertification with reopening triggers, provisional and full certification, non-evasion, the cascade from System certifications, and the reopening of the Institution's Systems (§3), the challenge path (§4), and the relationship to standing (§5). If one of an Institution's Systems loses its certification, the Institution answers for what that says about the Institution, and no more. If the Institution is found to have governed badly, its Systems are looked at again.

**Role.** The chapter is the Institution's counterpart to Chapter Eleven:

- It takes the outcome from Chapter Thirteen as fixed.
- It cites System Certification Records by link and does not copy or re-decide them.
- Chapter Fifteen accepts verified facts from this chapter only at the verified-input gate (§5.3), and what they do to standing is decided there and in Chapter Twenty.

**Chapter scope.** The chapter covers the Institutional Certification Record (§2), recertification and reopening (§3), challenge (§4), and the standing bridge (§5). It leaves:

- evaluation to Chapter Twelve and forum process and outcomes to Chapter Thirteen;
- System certification records and recertification to Chapter Eleven; and
- standing measurement to Chapter Sixteen, and the later standing steps to Chapters Seventeen through Twenty.

---

## Chapter Fifteen: Standing Records — Question 1, What Happened?

*In plain terms: standing is worked out by answering three questions in order. This chapter sets out the three questions and answers the first: what happened? Do not infer facts from a desired rating, and do not choose a rating to justify a desired consequence.*

**Purpose.** Chapter Fifteen opens the standing pipeline. It states the three questions (§2) and answers Question 1: it establishes a bounded, contestable account of what happened, identifying the subject, the event or pattern, the time period, the verified facts, and the standing record's status before any rating or consequence is considered (§3). Verified help and verified violations use separate standing records, so one cannot erase the other.

**Role.** The chapter produces the verified standing record that the rest of the pipeline takes as fixed:

- Chapter Sixteen measures it (Question 2), and Chapter Seventeen decides what follows (Question 3), with review limited to the anti-constitutional-misconduct designation in Chapter Twenty-One for qualifying Violation Axis slot 7 to 9 findings.
- Certification outcomes reach it only as verified inputs, through the gate in Chapter Eleven §5 and Chapter Fourteen §5.
- Chapter Eight's four-seat rule is applied to standing records in §6.

**Chapter scope.** The chapter covers:

- the three questions (§2);
- Question 1 (§3);
- the event-type guide (§4);
- verification and record requirements (§5);
- record custody and opening authority (§6); and
- handling a standing record (§7).

Chapter scope for the standing frame itself, including what it does not measure, is stated in §2.1. The chapter leaves:

- how good or bad a verified fact was to Chapter Sixteen;
- what follows to Chapters Seventeen through Twenty; and
- forum supervision of standing records to Chapter Twenty-Three (§3.7, *Forum Boundary*).

---

## Chapter Sixteen: Standing Measurement — Question 2, How Good or Bad Was It?

*In plain terms: Question 2 measures the verified facts from Question 1. It asks how good the contribution was or how bad the violation was. The Contribution Axis and the Violation Axis stay separate; they are not two sides of a net score.*

**Purpose.** Chapter Sixteen answers Question 2. It gives the LEQU baseline and its limits (§2), the magnitude and severity input dimensions (§3), the route descriptor catalogs (§4), slot grammar and shared scaling (§5), the constitutional inputs to axis assignment (§6), the unified proportional LEQU scale (§7), standard contribution measures (§8), and the hand-off to Question 3 (§10). For each axis it writes a slot from 1 to 9, the route descriptors that apply, the inputs handed to Question 3, and one LEQU total (§3.1).

**Role.** The chapter sits in the middle of the standing pipeline:

- It takes the facts already verified under Chapter Fifteen §3 and written into the standing record under Chapter Fifteen §5 as fixed.
- It hands the slot and descriptors to Chapter Seventeen, starting at §4 *Descriptor Integration and Attachment Normalization*.
- Chapter Sixteen alone assigns the numeric slot. Chapter Twenty-One adds an anti-constitutional-misconduct designation to a qualifying slot and does not move it.
- The common scale compares magnitude, not moral worth, and never lets help cancel harm.

**Chapter scope.** Chapter scope for Question 2, and how it routes to the harm side and the benefit side, is stated in §2.3. The chapter covers §2 through §10 in order. It leaves:

- what happened to Chapter Fifteen;
- what follows from a measurement to Chapters Seventeen through Twenty; and
- the anti-constitutional-misconduct designation to Chapter Twenty-One.

---

## Chapter Eighteen: Contribution Consequences

*In plain terms: this chapter asks what verified contribution may do. It may support recognition and readiness for gated pathways that are not locked. It never offsets a verified harm, cancels a lock, or opens a blocked gated pathway.*

**Purpose.** Chapter Eighteen decides the effect, if any, of verified contribution at Question 3. It does so in two steps: recency and currentness, then competency bars and clearances for gated pathways that are not locked (§2).

**Role.** The chapter is one of four that together own Question 3, with Chapters Seventeen, Nineteen, and Twenty:

- It decides from the contribution standing record only.
- It takes the decision order from Chapter Seventeen §3.4 *Processing Order*. The contribution track and the violation track do not wait for each other.
- Its result meets the violation track only at the final standing effect in Chapter Twenty, where a lock controls.

**Chapter scope.** The chapter covers contribution consequences (§2.1 and §2.2). It leaves:

- the decision order to Chapter Seventeen;
- remedy, correction, and lock rules to Chapter Nineteen; and
- the final standing effect to Chapter Twenty.

It points to them and does not restate them.

---

## Chapter Nineteen: Violation Consequences — Remedy, Correction, and Locks

*In plain terms: something bad happened. This chapter says how to make a durable fix: remedy and correction first, then prevention locks, then voluntary public accountability expression where a restorative pathway uses it, and the remedy-parity rule that keeps the cheap half from outrunning the expensive half.*

**Purpose.** Chapter Nineteen decides what follows from a verified violation. It sets remedy and correction, general standing locks, voluntary public accountability expression, and remedy parity and lock preconditions (§2). It then says how a lock is designed and enforced: definition and attachment, proportionality and calibration, record visibility and escalation, special violation rules, special locks, and interim holds (§3).

**Role.** The chapter is the violation track of Question 3:

- It decides from the violation standing record alone, and takes the verified violation record and the slot as fixed. It does not reopen Chapter Sixteen measurement.
- It follows the decision order in Chapter Seventeen §3.4. A lock controls: no contribution result opens a gated pathway a lock blocks.
- It hands its result to the final standing effect in Chapter Twenty.

**Chapter scope.** The chapter covers §2 and §3 in order. It leaves:

- contribution consequences to Chapter Eighteen;
- the decision order to Chapter Seventeen and the final standing effect to Chapter Twenty; and
- the anti-constitutional-misconduct designation for qualifying slot 7 to 9 findings to Chapter Twenty-One.

---

## Chapter Twenty: Final Standing Effect, Restoration, and Enforcement

*In plain terms: when the earlier steps are done, the system must state, one gated pathway at a time, what is open, limited, or blocked. That statement is not a dignity rank or a merged score. A lock that is not permanent must have a real way back.*

**Purpose.** Chapter Twenty states one final standing effect for each applicable gated pathway (§2). It then sets restoration and reassessment (§3) and confirms that standing consequences and redress can be delivered by real institutions (§4), applying the Chapter One §6.1 *Correction and Remedy* principle.

**Role.** The chapter is where the two tracks of Question 3 meet:

- It takes the contribution result from Chapter Eighteen and the violation result from Chapter Nineteen as fixed, in the order Chapter Seventeen §3.4 sets.
- Gated-pathway effects are never aggregated (§2.1). A gated pathway a lock blocks stays closed, whatever the contribution track found.
- Restoration is not automatic forgiveness, record erasure, or letting past help cancel verified harm.

**Chapter scope.** The chapter covers the final effect (§2), restoration and reassessment (§3), and enforcement realism and remedy systems (§4). It leaves:

- the decision order to Chapter Seventeen;
- how contribution and violation results are reached to Chapters Eighteen and Nineteen; and
- day-to-day staffing, funding, backlog, and succession rules to adopted implementation text.

---

## Chapter Twenty-Two: Anti-Constitutional Misconduct — Pattern Applications and Criteria Routing

*In plain terms: this chapter applies Chapter Twenty-One's decision model to recurring patterns of anti-constitutional conduct. It names how each pattern attacks accountability. It creates no new criteria and no new lock types.*

**Purpose.** Chapter Twenty-Two routes named patterns into the decision model in Chapter Twenty-One §§3 to 5. The patterns are: attacks on participation and accountability-pathway integrity (§2); blocking contest, review, and verification (§3); corrupting and commanding duty-holders (§4); shielding misconduct and failing to enforce (§5); structural control through concentration and dependency (§6); and obstruction of accountability (§7). Each is judged by what the conduct actually does.

**Role.** The chapter is jointly owned with Chapter Twenty-One, which owns the final ACMD for Violation Axis slot 7, 8, or 9 findings:

- It takes the ACMD criteria and safeguards from Chapter Twenty-One as fixed.
- After a final ACMD, Chapter Seventeen integrates the standing effect, and Chapter Twenty-Three routes the case and certifies the forum.

**Chapter scope.** The chapter covers the named patterns (§2 to §7). It adds no ACMD criteria and no Chapter Seventeen lock types. It leaves:

- ACMD criteria, attachment rules, and due-process safeguards to Chapter Twenty-One; and
- operational forum, systems, and institutional mechanics to their owner chapters.

---

## Chapter Twenty-Eight: Non-Regression and Substantive Amendment Validity

*In plain terms: a change that weakens the protections this Constitution depends on is invalid, even if the words say otherwise and even if it is done through procedure, definitions, or an emergency label. This chapter is Test 1, the substance test.*

**Purpose.** Chapter Twenty-Eight states Test 1, substantive non-regression validity. It sets the non-regression floor (§2), the Test 1 checklist against Chapter One constraints, Chapters Two through Four integrity, Chapter Six Rights Floors, and Chapter Twenty-Seven legitimacy (§3), and the anti-evasion clause with referral of serious bad-faith conduct (§4). Amendment validity must preserve both aims, Flourishing and Continuity, and must not hollow the Tetrad below material stake.

**Role.** The chapter is the substance half of change validity:

- Chapter Thirty states the procedural tests, Tests 2 to 4, and Chapter Twenty-Nine states what additive expansion is permitted.
- Serious bad-faith conduct is flagged to the bodies that own labels and sanctions, not relabeled here.

**Chapter scope.** The chapter covers §2 through §4. §5 states the validity-protection controls the chapter may impose and the owner non-relocation rule; its title is pending a steward decision. The chapter leaves:

- numeric standing measurement to Chapter Sixteen;
- anti-constitutional-misconduct designation to Chapter Twenty-One; and
- procedural validity to Chapter Thirty.

---

## Chapter Twenty-Nine: Expansion, Supremacy, and External Legal Orders

*In plain terms: forward is fine, and new rights, stronger safeguards, and broader inclusion are welcome when they increase protection. This chapter also says how this Constitution relates to other binding norms and to outside law: it is not a secret override, and it cannot be turned off during amendment.*

**Purpose.** Chapter Twenty-Nine states what is permitted and what holds when this Constitution meets other rules. It permits additive expansion (§2), keeps supremacy and challenge rights in force during amendment (§3), sets supremacy relative to other binding norms, stricter external protections, and conflict disclosure (§4), covers disputes involving external legal orders (§5), and states how this Constitution relates to applicable external law, including non-displacement and limited binding effect (§6).

**Role.** The chapter works with its two neighbors on change and adoption:

- The guardrail on expansion is Chapter Twenty-Eight.
- A body can bind itself only by adopting through Chapter Thirty, and only as far as it already has lawful authority to bind itself.
- Chapter Thirty-One §4 applies where partial adoption could shrink duties an entity already bears.

**Chapter scope.** The chapter covers §2 through §6 in order. It leaves:

- the test for whether a change is valid to Chapters Twenty-Eight and Thirty; and
- the incorporation bridge, custody, and operative effect of adopted text to Chapter Thirty-One.

---

## Chapter Thirty: Amendment, Ratification, and Procedural Validity

*In plain terms: a change can be substantively fine and still fail because of how it was made. This chapter holds amendments to a procedure that is real: a published proposal, a clear chain of authority and custody, and a contest path that works.*

**Purpose.** Chapter Thirty states Tests 2 to 4 and the rules around them. Heightened review for rights-affecting changes (§2), the burden of justification and public traceability (§3), and the validity floor (§4) frame three tests: procedural validity and publication integrity (§5), authority-chain and custody validity (§6), and contestability and independent review validity (§7). Review triggers (§8), the provisional effect rule (§9), and invalid-change handling and remediation continuity (§10) say what happens when review is needed or a change fails. Ratification and adoption (§11) and amendment procedure requirements (§12) state how a body adopts and how it amends. §13 states the owner non-relocation rule for this chapter.

**Role.** The chapter is the procedural half of change validity:

- Chapter Twenty-Eight states Test 1, the substance test. Procedural steps cannot save a change that fails it (§4).
- A body binds itself to this Constitution only by adopting through this chapter (Chapter Twenty-Nine §6).
- Chapter Thirty-One holds custody, editions, and operative effect.

**Chapter scope.** The chapter covers §2 through §12, and §13 states the owner non-relocation rule. Escalation wording in this chapter is routing, not a second accountability code. The chapter leaves:

- numeric Contribution and Violation slots to Chapter Sixteen;
- anti-constitutional-misconduct designations to Chapter Twenty-One; and
- substantive non-regression to Chapter Twenty-Eight.

---

## Basis and confidence

| Chapters | What I read | Not read |
|---|---|---|
| 3, 4 | Placement box, full outline, each section's plain-terms line | Section bodies |
| 7, 10 | Full placement box (owner, definition home, implementation owner, downstream consumers), outline | Section bodies |
| 11, 13, 14 | Outline, plain-terms lines; box for 11 only to its first 600 characters | Section bodies; Chapter 11's owner line |
| 15, 16 | Box, outline, plain-terms lines, Chapter Fifteen §2.1, Chapter Sixteen §2.3 and §3.1 | Remaining bodies |
| 18, 19, 20 | Box (owner and anti-relocation lines for 18), outline, plain-terms lines | Section bodies |
| 22, 25, 26, 27 | Box, outline, plain-terms lines; Chapter Twenty-Eight §5 and Chapter Thirty §13 in full | Remaining bodies |

Statements about neighboring chapters were taken from the placement boxes and plain-terms lines of those chapters, not from their bodies. The steward should spot-check any cite that matters to a duty before approving.

## Found while reading (not fixed)

1. **Stale chapter list in a binding rule, Chapter Twenty-Eight §5** (about line 185). It says other owners hold "final offense classification, sanction taxonomy, standing measurement, adjudicative workflow, or procedural amendment validity" in "Chapters Sixteen, Thirteen, Fourteen, and Eighteen respectively." Before the move it read "Twelve, Thirteen, Fourteen, and Eighteen." The move rewrote only the first number. Old Twelve, Thirteen, and Fourteen were standing measurement, standing integration, and misconduct designation (now 16, 17, 21), and old Eighteen was expansion and supremacy (now 26). Five items against four chapters did not line up before the move either. It needs hand review.
2. **Same pattern, Chapter Twenty-Two about line 1548:** "relocate standing measurement, ordinary locks, or forum supervision from Chapters Fifteen, Thirteen, or Fifteen." Only the first item appears to have been remapped.
3. **Garbled ranges and "Parts" wording in placement boxes** of Chapters 10, 11, 17, 18, 19 and 20. Examples: "Chapter Seventeen §§1–Chapter Seventeen 4", "Chapter Eleven §2–Chapter Eleven §5", "The other Parts are…", "Section numbers run continuously across the four Parts", and Chapter Ten's "continuing from Chapter Nine §1–§5." Chapter Five core_05.035 about line 3890 has "Chapter Seventeen §§2–Chapter Twenty 3." These look like the range-end rewrite (154 range ends) adding a chapter name to each end. Comma-list chapter mentions are few (6 lines in 6 core files), so the check is small.
4. **Chapter Seventeen §1** links "§2 Chapter Seventeen Records Do Not Change" to a heading that now reads "Chapter Fifteen Records Do Not Change." The heading is the right one; the link text is stale.

## Needs a decision

1. **Approve, edit, or reject each draft.** After approval, the scripted pass inserts them, retitles all §1 headings, renames the Layer Scope sections, and handles the corpus files.
2. **Chapter Fifteen §2.1 "Purpose and Scope" and Chapter Sixteen §2.3 "Question 2 Only — Scope and Routing."** Both are scope statements outside §1, and Chapter Fifteen's heading now sits beside a §1 titled "Purpose, Role, and Scope." Options: leave them and point (as drafted), retitle them (for example "The Standing Frame" and "Question 2 Only: Routing"), or fold them into §1 chapter scope.
3. **Chapter Twenty-Eight §5 title** (deferred by the steward).
4. **The six stale items above.** Fix in the same scripted pass, or leave as a separate small fix? I would fix 1 and 2 by hand (they sit in binding text) and the rest by script.
