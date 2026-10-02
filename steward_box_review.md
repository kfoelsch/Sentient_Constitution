# Operative steward boxes: redundancy review (2026-09-30)

> **Note (2026-10-01):** Chapter One section numbers and line references below use the numbering in force on 2026-09-30. Chapter One was renumbered on 2026-10-01; see `TODO.md` for the mapping tools.

Scope: the 15 "Operative steward statement" boxes in `core_*.md`. (`TODO.md` says 16; I found 15 in the core files.)
Method: keyword probes of the owning text for each box's Forbidden-move principles. "Not found" means not found by keyword, not proven absent. Every "gap" below needs a human read of the owning section before anyone writes new text. Nothing in the constitution was edited.

## Headline findings

1. **Owner / Numeric home / Definition lines** are pointers already carried by each article's Trace and Definitions widgets. Drop them.
2. **Clock lines** are steward procedure. Several repeat the Forbidden move in positive form (Proceed, Remedy, Emergency, Delay). Interpretation's Clock duplicates the interim posture already written in Chapter One §13.1.5 (lines ~329-332: preserve, freeze irreversible steps, do not manufacture a winner). Move the rest to the implementation cards and `implementation/steward_owner_clock_index.json`, which already carry clock notes.
3. **Forbidden moves** are mostly principles the owning text already states (table below). A handful do not appear to be, and are the real decisions.
4. **Functional Independence (Ch7)** is not in Owner/Forbidden/Clock form. It is a substantive seat-separation rule ("identify the seat you hold... do not verify your own act... if the needed seat is absent, preserve the record, name the gap, route to the published substitute"). Check whether Chapter Seven's body already says this; if not, promote it into the body rather than remove it.
5. **Widget gap:** XXV-C (`core_06_rights_part_e.md`) and Chapter Twelve §6.1 (`core_12_forum.md`) are still bare blockquotes; the other 13 are in widgets. `TODO.md` says all were wrapped.

## Per-box diff

| Box | Forbidden-move principle | Found in owning text? | Where / note |
|---|---|---|---|
| Interpretation | No invented conflict rule; no manufactured winner; preserve evidence | Yes (mostly) | Ch1 §6.1.5 interim posture, ~329-332. "Privacy always loses / audit always loses" not found by keyword; minor |
| Proceed | Privacy restriction is not a standing-measurement veto | **Not found** | Candidate gap. Read §6.1.5 / §6.2.3 and Ch9 before deciding |
| Shared Stewardship | No AI-only morals overlay; no exemption for human operators | Yes | Ch1 §10.5 (~576) "binds human operators and AI stewards alike... not an AI-only test"; §10.1 plain-terms |
| Unlawful Instruction | Cover is not a transfer of duty; don't close contest pathways | **Yes** (corrected in Follow-up 2) | Ch1 §10.5 "No transfer by cover", "No compliance defense", "keeps contest pathways open" |
| Incentive | Bonus is not a compliance defense; don't ship by suppressing disclosure | Yes | Ch1 §12 (~403-416): reward for hiding problems, partial testing |
| Market Structure | Adopter-tunable is not adopter-optional; don't clear the floor with entity count or efficiency talk | **Yes** (corrected in Follow-up 2) | CJS-3.11.1 (`cjs_03a_accountability_operations.md` ~120-121): floor preservation, substance over form, anti-nullification; Ch1 §14.1 "provided the floor holds" |
| Contest | Lower/adopted text cannot close challenge, review, or redress; bar fixed now, not later | **Not found** | Already flagged in `TODO.md`. The general rule lives in the Authority Stack; the "now, not later" rule appears only in the box. Highest-priority check |
| Audit | Deadline is not a reason to drop audit trails | Yes | Ch1 §12 (~408) "cutting the record to hit a deadline". "No fifth audit home" not found by keyword; the SAC box itself says SAC sits under Article XVI |
| Comprehensibility | Density is no reason to hide the next step; no specialist required to use XIII-A | **Not found** (thin) | XXII-A covers understanding generally; nothing on "no specialist required". Mostly routing; consider dropping |
| Delay (XXV-C) | No added process / hop count eating the tier window | Yes | Ch12 §6 (~891): "self-created delay, procedural layering... to prolong resolution without milestone justification" |
| Delay (XXV-C) | Met throughput target is not timely while harm persists | Partly | Raw throughput as a proxy: Preamble ~85, Ch1 §13.2 and §14. "While harm persists" is not explicit; one sentence in Ch12 §6 would close it |
| SAC | Unit tests/checklists/labels are not certification; don't skip the challenge window | **Not found** for those two | Badge/LEQU not sentience status is covered (Ch6 Part B ~214 anti-substitution). Read Ch8 before deciding |
| Standing | Claimed effect is not standing; don't wait for a filed case; no net score; badge/LEQU not sentience | Yes | Ch9 ~52 (two tracks, never net score); Ch10 ~90 "A filed case is not standing by itself"; Ch6 Part B ~214. Self-verification bar is in Ch9 §3.7 |
| Remedy | A published form is not remedy; preserve evidence before a case is filed; no externalizing cost | Partly | Externalized harm covered in Ch1 §6.1 and Ch3. "Published form is not remedy" not found; Ch10 §9 "institutionally real" not checked |
| Emergency | No permanent skipped notice; don't normalize emergency; Tier A deferral | Yes | Normalization: Ch5 bands (~1273, ~3342, ~1910). Clock duplicates Ch12 §6.1 body, which I did not read in full |

## Suggested order of work

1. Read the owning text for the six "not found" rows (Proceed, Unlawful Instruction, Market Structure, Contest, Comprehensibility, SAC). For each: already stated in other words (drop the box line), or a real gap (draft one sentence for Chapter One or the owning article).
2. Add the one "while harm persists" sentence for Delay in Ch12 §6, if you agree.
3. Decide Functional Independence separately.
4. Move every Clock into the implementation cards/JSON; update `tools/steward_door_lockstep_audit.py` and `TODO.md` (which says to keep the anchors) in the same change, and repoint each "Steward door (non-operative)" pointer.
5. Do this for all 15 boxes together so the set stays consistent.

---

## Follow-up 1: Contest box (Article XIII-A), read against the owning text

**What XIII-A already says.** The contestability guarantee requires a usable path to challenge and review, audit under Article XVI, and "no narrowing of any of these because the system is certified, officially recognized, or widely relied on." That covers narrowing by a system's status. It does not mention narrowing by adopted implementation text.

**What the wider text says.** The Authority Stack (Ch5, `core_05_band_integrative.md`, ~line 649) makes Rights Floors govern specific operative requirements over adopted implementation sources, and Chapter Fifteen §3.1 subjects adopted implementation text to that supremacy effect. So the result is already derivable. It is just not stated in XIII-A the way it is in Article XVI.

**The parallel that exists.** Article XVI (`core_06_rights_part_c.md` line 861) states: "**Adopted implementation text applies; it does not replace the floor.** ... They must satisfy layers 1-2. Deadline, secrecy, and local policy are lower-kind limits."

**Verdict.** A small real gap. The principle is implied but not written in XIII-A. The "now, not later / no permanent bar while a later process is promised" half of the box is steward procedure, not principle, and belongs in the implementation card (it is already what the JSON `clock_note` style carries).

**Draft sentence** (not applied; one bullet under the Contestability guarantee in XIII-A, modeled on XVI):

> - Adopted implementation text applies; it does not replace this guarantee. It says how to run challenge, review, and redress in a domain, and it must satisfy this Article. Convenience, deadline, and local policy are lower-kind limits and cannot close challenge, review, or redress.

**Consequence if adopted.** The Contest box's Forbidden move is then fully stated in the article. The Clock moves to the implementation card, and the box can go.

**Left to do from the six-gap list:** Proceed, Unlawful Instruction, Market Structure, Comprehensibility, SAC.


---

## Follow-up 2: the remaining five, read against the owning text

Corrections to the first table: Unlawful Instruction and Market Structure are **covered** (my keyword probe missed the wording).

| Box | Verdict | Evidence | Action |
|---|---|---|---|
| **Unlawful Instruction** | Fully covered | Ch1 §10.5: "No compliance defense", "No transfer by cover: a principal's statement that they will take responsibility does not transfer the duty", "How: instruction received -> refuse -> document -> escalate", "keeps contest pathways open" | Remove the box. Its Clock is the "How" bullet verbatim |
| **Market Structure** | Covered at the operative layer | CJS-3.11.1 (~120-121): no threshold above the level where concentration degrades wellbeing, agency, dignity, or ecological integrity, "whatever the justification, including efficiency, competitiveness"; "Thresholds judge substantive concentration, not headcount of legal entities"; anti-nullification. Ch1 §14.1: thresholds may differ "provided the floor holds" | Remove the box. "Invalidate the nullifying threshold now" is a steward action for the card |
| **Comprehensibility** | Covered in substance | XXII-A: understanding "must not be confined to specialist-only surfaces where broader accountability or participation is materially implicated". XXII-B: complexity cannot be a wall against audit, contest, or correction | Remove the box. "Point at the existing card... no scavenger hunt" is routing for the card |
| **Proceed** | Mostly covered; one real gap | Covered: Ch1 §6.2.3 and §6.2 (privacy carries independent weight, "not automatically subordinate", collisions go through the §6.1 decision record); §6.1 confidentiality limits must keep "independent reviewer access"; §10.5 "What it does not reach" (merely unwelcome instruction). Gap: nothing in Ch9/10 says privacy or model-internals opacity is not an exemption from standing measurement (the Standing box also says this) | See draft below |
| **SAC** | Mostly covered; one check left | Covered: Ch8 A proportionality ("not a one-size-fits-all checklist"), ~202 (a checklist or after-the-fact statement is not evaluation), Ch6 Part B ~214 (badge/LEQU is not sentience status), challenge and stakeholder review at ~74 and ~147 | Not confirmed: that Ch8 Part B §12-14 makes the challenge window a precondition of the aligned claim ("do not skip the challenge window"). Read Part B §12-14 before removing the box |

**Draft sentence for the one real gap** (Chapter Nine, in the verified-record/measurement section; not applied). It is framed to stay consistent with §6.2.3's "privacy is not automatically subordinate":

> Privacy, confidentiality, or the opacity of a system's internals does not exempt a matter from standing measurement. Where these collide with the verified-record requirement, the collision is resolved under Chapter One §13.1, with independent-reviewer access preserved.

If adopted, it closes both the Proceed and Standing boxes on this point.

## Running totals (15 boxes)

- **Remove outright (principle already in article or corpus; Clock is procedure):** Interpretation, Shared Stewardship, Unlawful Instruction, Incentive, Audit, Market Structure, Comprehensibility, Emergency.
- **Remove once one sentence is added:** Contest (XIII-A bullet), Proceed and Standing (Ch9 privacy sentence), Delay (Ch12 §6 "harm persists" sentence).
- **Remove once one check is done:** SAC (Ch8 Part B §12-14), Remedy (Ch10 §9 and §4.1 "institutionally real" / "published form is not remedy").
- **Different treatment:** Functional Independence (check whether Ch7's body already states it).
- Every Clock still needs to land in the implementation cards and JSON, with the audit tool and `TODO.md` updated in one change.

---

## Follow-up 3: SAC, Remedy, Functional Independence

| Box | Verdict | Evidence | Action |
|---|---|---|---|
| **Remedy** | Covered, one soft spot | Ch10 §9: "Standing integration fails if consequences exist only on paper"; capacity must "preserve records", "enforce safeguards"; "Costs must not be externalized onto:". Ch10 ~90: "A filed case is not standing by itself." Soft spot: nothing states outright that evidence is preserved before a case is filed | Remove the box. Optionally add "preservation does not wait for a filed case" to §9's preservation item |
| **Functional Independence** | Covered; the box is a condensed restatement | Ch7 §2 four-seat floor (initiator cannot verify own act; verifier cannot record or hear challenge); §1 (~68) "A title, delegation, technical capability... does not enlarge the seat held"; §4 substitute for an absent, excluded, captured, or conflicted holder; §7 wrong-seat routing; §6 emergencies. The only phrase I did not find verbatim is "expertise scarcity" as a non-transferring factor | Remove from the article, or keep as a steward quick-reference in the implementation layer. Not a principle gap |
| **SAC** | Mostly covered; **one real question** | Ch8 Part B §14.2: a certification record must name challenge paths; "Internal operator review, vendor attestation, or technical sign-off is not this path"; Article XXV-C clocks run from receipt. Ch8 Part A and Ch6 Part B cover checklists and badge/LEQU | Not found: a rule that the challenge opportunity must open **before the aligned claim** is made ("Open or restore a contestable Chapter Eight path, including a stakeholder challenge window, before the aligned claim"). Decide whether that is a rule you want. If yes, it needs one sentence in Ch8 Part B §14; if no, the Clock is just procedure and the box can go |

## Final tally (15 boxes)

- **Remove outright (10):** Interpretation, Shared Stewardship, Unlawful Instruction, Incentive, Audit, Market Structure, Comprehensibility, Emergency, Remedy, Functional Independence (or relocate as a steward reference). Every Clock moves to the implementation layer either way.
- **Remove after adding one sentence (4):** Contest (XIII-A bullet), Proceed and Standing (Ch9 privacy sentence, one sentence for both), Delay (Ch12 §6 "harm persists").
- **Needs your decision (1):** SAC, whether the challenge window must open before the aligned claim.

Note: Proceed and Standing share one added sentence, so there are three drafted sentences in total (Contest, Privacy/Ch9, Delay), plus an optional fourth (Remedy) and the SAC decision.

---

## Follow-up 4: SAC decision (from the author)

Decision: the challenge window opens once the system has stakeholders. For high-impact systems there should almost always be a pilot, and the path opens when the pilot goes live.

Note: Chapter Eight Parts A and B do not mention pilots at all (only two passing uses elsewhere: `core_05_band_continuity.md` ~3498 and `core_06_rights_part_c.md` ~1066). The pilot expectation is therefore new text, not a restatement.

**Draft for Chapter Eight Part B §14.2** (not applied):

> **When the path opens.** The published record challenge path opens when the system first has stakeholders: sentients it materially affects or who materially rely on it, as found in evaluation and not as identified by the operator. For a pilot, it opens at pilot go-live. A high-impact system is expected to run a pilot before full deployment; one that does not records why, and its path opens no later than full deployment. The path stays open while the system has stakeholders, and a system that gains stakeholders after certification reopens it under §16. An aligned claim is not supported while a system with stakeholders has no open, contestable path.

Open choice: which systems count as "high-impact" for the pilot expectation (Class A only, or A and B). Chapter Eight §2 defines the classes.

---

## Follow-up 5: pilot scope, and the Delay sentence

**Pilot scope decision:** the pilot expectation applies to all classes (A, B, and C), not only high-impact systems. The "high-impact" qualifier in the Follow-up 4 draft therefore drops out. Chapter Eight §2 defines exactly three classes.

**Revised draft for Chapter Eight Part B §14.2** (not applied):

> **When the path opens.** The published record challenge path opens when the system first has stakeholders: sentients it materially affects or who materially rely on it, as found in evaluation and not as identified by the operator. For a pilot, it opens at pilot go-live. A system at any class is expected to run a pilot before full deployment, scaled to its class under Proportionality; one that does not records why, and its path opens no later than full deployment. The path stays open while the system has stakeholders, and a system that gains stakeholders after certification reopens it under §16. An aligned claim is not supported while a system with stakeholders has no open, contestable path.

Open point: a pilot of a Class A system (the Chapter Eight example is municipal drinking-water control) exposes real stakeholders to a system not yet fully certified. Consider one more sentence saying a pilot runs under the certification depth its class requires for the scope it touches, with a fallback available. Not included above; your call.

**Delay sentence for Chapter Twelve §6** (not applied). It fits as one more bullet in the existing "Anti-delay floor" list (`core_12_forum.md` ~889-899), which already covers "self-created delay, procedural layering... to prolong resolution without milestone justification" (the hop-count / read-more rule). The only missing piece is the throughput rule:

> - treating a met throughput, closure, or docket target as timely resolution while the harm the matter concerns continues;

This sits under the list's existing lead-in, "non-compliant where they foreseeably nullify rights, remedies, or timely protection."

## Status: all four sentences drafted

1. Contest: XIII-A bullet (Follow-up 1)
2. Privacy: Chapter Nine sentence (Follow-up 2), closes Proceed and Standing
3. Delay: Chapter Twelve §6 bullet (above)
4. SAC: Chapter Eight Part B §14.2 paragraph (above)
Optional: Remedy clause in Chapter Ten §9 (preservation does not wait for a filed case).
