# Draft Chapter Five entry: Record-Opening Authority

**Archived record. Applied 2026-10-20 (sixty-ninth move in [doc_architecture.md](../doc_architecture.md)); the live entry is in `core_05_band_accountability.md`.**

**Status when drafted:** draft for the custodian and steward. Not applied to `core_05_band_accountability.md`. It is core text (a new Chapter Five definition), so it needs sign-off before it goes in.

## Why this entry

Chapters Seven, Eight, Ten and Thirteen and CI-3.6 field 10 rely on the **record-opening authority**, and CF-5.7 builds a body to fill the role. Chapter Five defines the *Verify-or-Authorize Seat*, the *Record Seat* and the *Contest Seat*, but not the record-opening authority itself, so the standing-record role has no home entry. This draft defines the role and does not create a new body. The Backup Record Authority (CF-5.7) stays the implementation-layer body that fills the role by default.

**Where it would go:** `core_05_band_accountability.md`, right after the *Standing Record* entry (the seats it sits beside are in the same band). Name follows TERM-BODY-01 (authority: verifies, authorizes, or decides a question for others).

**If approved, the follow-through is:** add the entry; point to it from Chapter Seven §4.6.1, Chapter Ten §3.7 and the Trace lists that now cite the term unlinked; add it to the Chapter Five measurement and definition indexes; run `make ai-corpus-sync`, `make plain-terms-edition` and `make audit-report`. A *Record Custodian* entry is the natural companion and can be drafted the same way.

---

<a id="record-opening-authority"></a>

#### Record-Opening Authority

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Downstream: [Chapter Ten §3.7 Record custody and opening authority](core_10_standing_assessment.md#37-record-custody-and-opening-authority); [Chapter Seven §4 The Charter Role Map and Standing-Record Custody](core_07_charters.md#4-the-charter-role-map-and-standing-record-custody); [Chapter Eight §2 Four-seat constitutional floor](core_08_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-floor); **CI-3.6** (*System and Institutional Charter contents, review, and formation template*); and **CF-5.7** (*Backup Record Authority*).
- Cluster component: [Governance architecture, decentralization, and concentration](core_05_band_accountability.md#governance-architecture-decentralization-and-concentration).
- Read with: [Standing Record](core_05_band_accountability.md#standing-record), [Verify-or-Authorize Seat](core_05_band_accountability.md#verify-or-authorize-seat), [Record Seat](core_05_band_accountability.md#record-seat), [Contest Seat](core_05_band_accountability.md#contest-seat), [Material Control Line](core_05_band_accountability.md#material-control-line), [Charter Role Map](core_05_band_continuity.md#charter-role-map), and [Evidence Preservation](core_05_band_oversight.md#evidence-preservation).
- Layer: applies within both the **Constitutional Contract Layer (CCL)** and **Stakeholder System Participation (SSP)** under [Preamble §3.3](core_00_preamble.md#33-governance-layers).

</details>

<br>

*In plain terms: the Record-Opening Authority is the body that checks the facts and decides whether a Standing Record may be opened, corrected, ended, or replaced. It holds the Verify-or-Authorize Seat for that record. It does not keep the record, which is the record custodian's job, and it does not hear a challenge to the record, which is the Contest Seat's job. It cannot be the record's subject, the party claiming or accusing, or anyone those parties control. If a Chartered Party's own map names none, or cannot fill the seat, the Backup Record Authority does the job, so nobody's record waits on the Chartered Party.*

- **What it is**
  - **In scope:** The body that holds the [Verify-or-Authorize Seat](core_05_band_accountability.md#verify-or-authorize-seat) for a [Standing Record](core_05_band_accountability.md#standing-record). It is named and its authority published before it acts. It verifies the factual basis of an opening, correction, expiry, or supersession and authorizes it, and it names itself on the record with its reason. It may be an office or role placed by a [Charter Role Map](core_05_band_continuity.md#charter-role-map), a forum acting as a record-opening authority, a disinterested body that relies on the record, or the Backup Record Authority (**CF-5.7**), which is the default where a System Charter or Institutional Charter names none or has a gap.
  - **Out of scope:** The record custodian that enters and holds the record. The Contest Seat that hears a challenge. A registrar that files and receipts. A body that only supplies inputs such as a recorder's statement, a log, or a photograph. A forum's merits decision. Any body that only requests the record.
<a id="record-opening-authority-a"></a>
- **How to measure and assess**
  - **Primary measure:** [Oversight measurement family](core_05_apex_oversight_leg.md#measuring-oversight-preamble-measurement-family) and [Accountability measurement family](core_05_apex_accountability_leg.md#measuring-accountability) — used together to test whether each change to a Standing Record was authorized by a named body that is independent of the record's subject, claimant, and challenger.

    **Primary assessment:** Identify who authorized each opening, correction, expiry, or supersession. Check that the authority was named before it acted, that it sits outside the [Material Control Line](core_05_band_accountability.md#material-control-line) of the subject, the claimant, and the challenger, that the facts were verified to the standard the governing process sets, and that it gave reasons.
  - **Secondary measure:** [Auditability](core_05_band_oversight.md#auditability), [Attribution Integrity](core_05_band_accountability.md#attribution-integrity), [Contestability](core_05_band_accountability.md#contestability), and [Evidence Preservation](core_05_band_oversight.md#evidence-preservation) — co-measures for traceability and correction.

    **Secondary assessment:** Test whether the record names the authority, its reason, and the version of the System Charter or Institutional Charter in force; whether an authority with an interest in the record declined and routed it; and whether delay or refusal by the authority was treated as a defect to log and correct, not as a gate on anyone's right to form or operate.
<a id="record-opening-authority-c"></a>
- **What must hold**
  - **Primary failure:** The record's subject, a claimant, a challenger, or anyone in their Material Control Line acts as the authority; the authority also enters and holds the record or hears the contest of a record it authorized; or it authorizes a change without verifying the facts.
  - **Secondary failure:** The authority is not named before it acts, or is named only by the party it checks; the record omits the authority, its reason, or the charter version in force; a conflicted authority does not decline and route; or the Chartered Party chooses, appoints, or funds a backup authority through a channel it controls.

---
