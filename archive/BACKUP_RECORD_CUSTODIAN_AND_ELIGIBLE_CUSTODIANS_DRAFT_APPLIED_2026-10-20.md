# Draft: Backup Record Custodian (CF-5.9) and eligible record custodians

**Archived record. Applied 2026-10-20 (sixty-ninth move in [doc_architecture.md](../doc_architecture.md)) with the custodian decisions: gap scope as drafted (versions opened during the gap plus operator records held inside the Chartered Party's Material Control Line), Institutional family keeps both backup bodies, open list, reciprocal hosting banned outright, apply now. The live text is in `cf_05` (CF-5.9), CI-3.6.3 field 10, Chapter Ten §3.7 and Chapter Seven §4.**

**Status when drafted:** draft for the custodian and steward. Not applied to any live file. It adds a new implementation section, changes the fallback in Chapter Ten §3.7 and touches Chapter Seven §4.6.1 and Chapter Five, so the wording is core text and needs sign-off.

**Why.** Operator standing records need three independent seats: a record-opening authority, a record custodian, and a contest seat. The Backup Record Authority (**CF-5.7**) covers only the first, and the contest seat has forums. For the custodian seat the only fallback today is "the supervising forum", which holds the record or designates a holder ([Chapter Ten §3.7](../core_10_standing_assessment.md#37-record-custody-and-opening-authority), *Record custodian* and *Conflicted custodian on a single record*). That makes a forum the custodian of last resort. Two additions close the gap:

1. a forum-kept **Backup Record Custodian**, the custody twin of the Backup Record Authority; and
2. a published list of **eligible record custodians** a System Charter or Institutional Charter may name, each held to the same independence tests.

## 1. CF-5.9 Backup Record Custodian (proposed text)

*Placement: `corpus_forum/cf_05_routing_operations_transfer_certification_representative_treatment.md`, after CF-5.8. Modeled on CF-5.7 (same keeper, funding, reporting, and clock).*

> ## CF-5.9 Backup Record Custodian
>
> *In plain terms: when a Chartered Party has no custodian that can hold a record without a conflict, someone outside it has to keep the record. The **Backup Record Custodian** is that custodian. It enters and holds a record that an authority has authorized, and nothing else. It does not check the facts (that is the Backup Record Authority or another record-opening authority) and it does not hear a challenge. If it is slow, the record goes to a forum, which holds it or names a holder.*
>
> This subsection implements, and must not narrow, Chapter Ten §3.7 Record custody and opening authority (*Record custodian*; *Conflicted custodian on a single record*; *No self-custody*) and Chapter Seven §4 The Charter Role Map and Standing-Record Custody. It stays outside the intake triage body (**CF-5.2** (*Intake triage body*)), the registrars (**CF-5.5** (*Institutional and local registrars*), **CF-5.6** (*Integrity registrar*)), which file and receipt and do not hold records, the merits panels, and the Backup Record Authority (**CF-5.7** (*Backup Record Authority*)).
>
> **Where it sits:** The **Institutional** forum family, or the local forum where the Chartered Party acts and the sentients it affects live, keeps one Backup Record Custodian, or a functionally equivalent arrangement, with the same independence and contest expectations as an intake triage body. It is a separate authority from the Backup Record Authority. Staff of one do not staff the other, and nobody supervises both on the same record, because no body may both verify and enter a record.
>
> **When it acts:**
> - **A gap in the System Charter or Institutional Charter:** From the day the gap is logged, for operator standing records in the affected scope, it enters and holds each version that a record-opening authority authorizes, until the Chartered Party lodges a version that names every required seat and the named custodian takes custody by a logged transfer.
> - **An excluded custodian with no substitute:** Where the named custodian is excluded for one record under *Conflicted custodian on a single record* and the System Charter, Institutional Charter, or lane map names no substitute holder, it holds that record.
> - **A custodian that cannot continue:** Where the named custodian is dissolved, captured, or unable to hold a record, and no successor is named, it holds the record so custody does not lapse.
> - **No route named:** It is the default custodian where *No self-custody* sends a record to independent verification and the System Charter or Institutional Charter or designation names none. A forum under Chapter Ten **section 3.6** stays available.
>
> **What it does:**
> - It logs the request and routes it the day it arrives.
> - It enters each authorized version, holds it with the full audit trail under Evidence Preservation, and publishes the challenge path.
> - It names itself on the record as custodian, with the reason it acts and the version of the System Charter or Institutional Charter in force.
> - It logs a challenge when received, sets the status to *under challenge*, notifies the subject and any claimant, and routes the challenge to the contest seat.
> - It returns custody by a logged transfer when the conflict or the gap ends.
>
> **What it does not do:**
> - It does not verify or authorize a record, and it does not hear a contest of a record it holds. A contest goes to the contest seat or a forum under Chapter Ten **section 3.6** and **CF-6** (*Appeal, secondary review, and exhaustion pathways*).
> - It does not take over the Chartered Party's whole store. It holds the records named above, one at a time, and the rest stay where they are, preserved unchanged.
> - It does not apply a Chapter Eleven standing effect, decide a merits question, or measure how good or bad the record is.
> - It does not rule on class, on scope, or on whether a System Charter or Institutional Charter is valid.
> - It does not grant or withhold permission to form or operate.
> - It charges no fee to the subject or a claimant.
> - It takes no instruction on a record from the Chartered Party or from the forum family that funds it.
>
> **Funding and accountability:** As **CF-5.7** (*Backup Record Authority*): funded by the keeping family or local forum from a published budget, no fee for a record, subject, or claimant, no withholding of funds over a decision, and the Chartered Party cannot fund it. It answers to the keeping family for its budget, aggregate reports, and conduct, never for an individual decision, and publishes aggregate figures by tier: records received, whether each came from a gap, an excluded custodian, a lapse, or no named route, time taken, and missed targets.
>
> **Time and fallback:**
> - **Answer:** It accepts custody, or refers the record, within the **intake target** of the Tier that matches the Chartered Party's class, counted from the day the request is logged, and inside the matter's tier window, never on top of it.
> - **Silence:** If it has not answered by then, the record goes to a forum under Chapter Ten **section 3.6**, which holds it or names a holder, and the subject or a claimant may take it there at once. A missed target is published as the custodian's own failure under **CF-11** (*Forum performance, backlog requirements, publication timeliness, and accessibility*).
> - **Unavailable or in capacity failure** (**CF-5.4** (*Capacity-failure routing*)): the record goes to a forum under Chapter Ten **section 3.6**.
> - **Conflict of its own:** It declines the seat, logs the conflict, and routes the record to a forum.
> - **Family capture:** As **CF-5.7** (*Backup Record Authority*): the keeping family does not appoint, staff, fund, or instruct it, and the body named under **CF-13.4** (*Family-capture fallback operation*) names the keeper until restoration.
>
> **Safeguards:** Outside the line (the Chartered Party cannot choose, appoint, or fund it through a channel it controls); not an endorsement of the System Charter or Institutional Charter; no gate (its delay, error, or refusal never stops a Chartered Party from operating); no steering; no self-judging (**CF-7** (*Integrity safeguards, anti-capture operations, and anti-self-judging support*)); oversight by Integrity or independent assurance bodies under **CF-9.5** (*Required separations*).

## 2. Eligible record custodians (proposed text)

*Placement: **CI-3.6.3** field 10 (*Standing-record custody*) in `corpus_institutions/ci_03_institutional_design_separation_of_powers.md`, as a new bullet after **Naming them**. Chapter Ten §3.7 *Record custodian* and Chapter Seven §4.6.1 point to it.*

> - **Who may be named record custodian:** A System Charter or Institutional Charter may name any of these as record custodian, or as the substitute holder for one record, if it passes every test below:
>   - the Backup Record Custodian (**CF-5.9** (*Backup Record Custodian*)), named by reference;
>   - a public archive, library, registry, or records service;
>   - a separate Institution with no control relationship to the subject, a claimant, or a challenger;
>   - a host, cooperative, or association that holds seats in common for the scope under [Chapter Eight §6 Proportional Scaling and Merged Hosting](../core_08_functional_independence_segregation_of_duties.md#6-proportional-scaling-and-merged-hosting), for records about the Chartered Party and not about the host's own members; or
>   - a records service paid under published terms by a fund the Chartered Party does not control.
>
>   The list is not closed. The tests are what decide.
> - **The tests:**
>   - **Outside the line:** It sits outside the [Material Control Line](../core_05_band_accountability.md#material-control-line) of the subject, each claimant, and each challenger. Appointment, funding, membership, discipline, a shared governing body, and common control all count. A body that admits, disciplines, or is funded by the subject or a claimant fails. A professional association therefore fails for a record about its own member's practice.
>   - **Separate from the authority:** It is not the record-opening authority for the same record. No body both verifies and enters.
>   - **No reciprocal or circular hosting:** Two adopters may not hold each other's records, and a ring of three or more that returns control to the subject fails for the same reason.
>   - **Continuity:** It publishes how long it keeps records, preserves the audit trail under [Evidence Preservation](../core_05_band_oversight.md#evidence-preservation), and transfers custody with the full trail if it ends, leaves, or is replaced.
>   - **Challenge path:** It publishes the challenge path and routes a challenge to the contest seat on the day it is received.
>   - **No fee:** It charges the subject and any claimant nothing for a record.
>   - **Named in advance:** It is named in the Charter Role Map before it acts, and a change of custodian is a new dated version of the map.

## 3. Edits that follow, if approved

| File | Change |
| --- | --- |
| `core_10_standing_assessment.md` §3.7 *Record custodian* | "to the successor the System Charter, Institutional Charter, or designation names, or, where none is named, to the Backup Record Custodian (**CF-5.9** (*Backup Record Custodian*)), or the supervising forum under **section 3.6**". |
| `core_10_standing_assessment.md` §3.7 *Conflicted custodian on a single record* | Same change: where no substitute is named, the Backup Record Custodian, with the supervising forum as the fallback if it cannot act. |
| `core_10_standing_assessment.md` §3.7 *No self-custody* | Add the Backup Record Custodian beside the Backup Record Authority as the default pair. |
| `core_07_charters.md` §4.6.1 | Bullet 2 adds "where none can act, the Backup Record Custodian (**CF-5.9**)"; add a pointer to the eligible-custodian tests in CI-3.6.3. |
| `core_07_charters.md` §4.7 | The "until it is resolved" bullet names the Backup Record Custodian with the Backup Record Authority. |
| `core_13_forum.md` §2.3 | No change expected (a contest still never goes back to the authority that opened the record). |
| `corpus_forum/cf_05_*.md`, `cf_00_*` registry, footer and family map | Add CF-5.9; update CF-5 Trace and the CF-5.7 sentence that says it "does not enter or hold" the record to point to CF-5.9. |
| `corpus_institutions/ci_03_*.md` CI-3.6.3 field 10 | Add the two bullets in section 2; update the "If silent" bullet to name both backup bodies. |
| Chapter Five | Add *Record-Opening Authority* (separate draft) and *Record Custodian* (below). |
| Generated files | `make plain-terms-edition`, `make ai-corpus-sync`, TIME-REF-01 registry entries for the new clock, `make audit-report`. |

## 4. Companion Chapter Five entry: Record Custodian (proposed text)

*Placement: `core_05_band_accountability.md`, after *Record-Opening Authority*.*

> #### Record Custodian
>
> *In plain terms: the Record Custodian is the body that enters, keeps, and versions a Standing Record after an authority has authorized it. It keeps what was verified. It does not verify, and it does not hear a challenge. It cannot be the record's subject, a claimant, or anyone they control.*
>
> - **What it is**
>   - **In scope:** The body that holds the [Record Seat](core_05_band_accountability.md#record-seat) for a [Standing Record](core_05_band_accountability.md#standing-record): it enters each authorized version, holds it, controls versioning, publishes the challenge path, and answers for the record's continuity. It may be placed by a [Charter Role Map](core_05_band_continuity.md#charter-role-map), be a substitute holder for one record, or be the Backup Record Custodian (**CF-5.9**).
>   - **Out of scope:** The [Record-Opening Authority](core_05_band_accountability.md#record-opening-authority) that verifies and authorizes. The Contest Seat. A registrar that files and receipts. Incidental storage or a copy held without authority over the official record.
> - **How to measure and assess**
>   - **Primary measure:** [Accountability measurement family](core_05_apex_accountability_leg.md#measuring-accountability) and [Oversight measurement family](core_05_apex_oversight_leg.md#measuring-oversight-preamble-measurement-family): whether each Standing Record is held by a named body that is independent of its subject, claimants, and challengers, with the full audit trail.
>
>     **Primary assessment:** Identify who holds each record and each version. Check that the custodian was named before it acted, sits outside the Material Control Line of the subject, claimant, and challenger, is not the authority for the same record, and keeps version history and the published challenge path.
>   - **Secondary measure:** [Evidence Preservation](core_05_band_oversight.md#evidence-preservation), [Attribution Integrity](core_05_band_accountability.md#attribution-integrity), [Auditability](core_05_band_oversight.md#auditability), and [Contestability](core_05_band_accountability.md#contestability).
>
>     **Secondary assessment:** Test whether a challenge was logged on receipt, whether custody passed with its full trail when a conflict or gap arose, and whether the custodian applied no effect and withheld no path.
> - **What must hold**
>   - **Primary failure:** The custodian is the subject, a claimant, a challenger, or in their Material Control Line; it also verifies or hears the contest of the same record; or it enters a version no authority authorized.
>   - **Secondary failure:** Custody lapses, a challenge is not logged on receipt, the audit trail is lost in a transfer, the custodian conditions entry on the subject's cooperation, or the Chartered Party chooses or funds a backup custodian through a channel it controls.

## 5. Open questions for the custodian and steward

1. **Scope of backup custody during a gap.** The draft has the Backup Record Custodian hold only the versions opened during the gap and leave the existing store in place. The alternative is to take the whole operator store until the gap closes. The draft follows Chapter Ten's rule that a single-record conflict moves the record and not the store.
2. **One keeper, two bodies.** The Backup Record Authority and the Backup Record Custodian are kept by the same forum family with separate staff and no shared supervisor on a record. A different keeper for each is stronger but needs more forum capacity.
3. **Closed or open list.** The draft says the tests decide and the list is examples. A closed list is easier to audit but could shut out a good custodian type.
4. **Reciprocal hosting.** The draft bans two-way and circular hosting outright. A softer rule (allowed with an outside review) is possible, but it reintroduces the capture risk.
5. **Timing.** The 2026-10-04 precedent held new core additions until after the announcement. Drafting now and applying after the announcement is an option.
