# Record Integrity: draft principle (2026-10-27)

**Status (2026-10-27):** adopted as **Record Integrity** in `core_05.035_band_accountability.md` (Accountability band, after Attribution Integrity); see move 155 in `doc_architecture.md`. The entry in the corpus is the source and has since been changed from the draft below (scaling added, "Not edited in place" elaborated). This file is the original draft and source table. Correction to the table: Chapter Ten §3.4 already requires standing records to be versioned with the prior audit trail kept, so "not edited in place" generalizes an existing pattern rather than creating one from nothing.

**Why.** While rewording Chapter Nine Part B §8.1 the same idea turned up under four different names: "integrity-preserving" (Act Record, Chapter Eight §8), "integrity-protected" (Part B), "tamper-evident where feasible" (Evidence Preservation), and "tampered with" (Attribution Integrity). No entry says, once, what it takes for an official record to be reliable as a record.

## 1. Where the pieces are today

| Element | Where it is stated now | Beyond the existing owners? |
|---|---|---|
| Attributable (who entered or changed it, in what role, under what authority) | [Attribution Integrity](../core_05.035_band_accountability.md#attribution-integrity); [Chapter Eight §8](../core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs) (seat holders, authority, "attributable" record); Part B §8.2 | No |
| Versioned, with changes visible | Chapter Eight §8 (current version, change timestamps, "superseded versions, and corrections"); Act Record entry ("versioned"); Record Seat assessment ("version history"); Part B §8.2 ("what changed between versions") | No |
| Not edited in place once complete | Part B §8 ("do not edit a completed certification record in place"); Chapter Ten §3.7 ("the record stays inspectable, its prior versions stay in place") | **Yes**, if stated for every official record |
| Preserved | [Evidence Preservation](../core_05.050_band_oversight.md#evidence-preservation) (no deletion, alteration, selective retention); Act Record entry ("identifies and preserves") | No (but it covers evidence, not every record) |
| Reconstructable | Act Record entry; Chapter Eight §8 closing test; Evidence Preservation ("loss of reconstructability"); Part B §8.2 | No |
| Reachable by those entitled; privacy never erases the trail | Chapter Eight §8 ("accessible through the authorized official record path"; privacy paragraph); Part B §8.2 (Type O) | No |
| Independent of the subject of the act | Chapter Eight §8 (a log, signature, or attestation by the actor "cannot replace" the Act Record); Act Record out-of-scope; Part B §8.1.6 control-line information | No |
| Tamper-evident where feasible | Evidence Preservation assessment; Attribution Integrity secondary failure | No |

The one real generalization is "not edited in place once complete". Today it is stated for the System Certification Record and, in different words, for standing records. Everything else already binds Act Records, so a general entry mostly collects and names what exists.

## 2. Draft entry (Chapter Five format, Oversight band)

Proposed place: `core_05.050_band_oversight.md`, a cluster component of Def.O1 *Transparency, Auditability, and Verification*, beside Evidence Preservation.

#### Record Integrity

- Cluster component: Def.O1 *Transparency, Auditability, and Verification*.
- Downstream: [Chapter Eight §8](../core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs); [Chapter Nine Part B §8](../core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record); Chapter Nine Part D; Chapter Ten standing records; [Chapter Thirteen §2.3](../core_13.000_forum.md#23-forum-case-records-standing-records-and-contests).
- Read with: Attribution Integrity, Attributable Action, Evidence Preservation, Auditability, Transparency, Contestability, Materially Binding Act Record, Record Seat.

*In plain terms: a record can be relied on only if you can tell who made it, what it said at each point, that nothing was quietly changed or dropped, and that the people entitled to check it can reach it.*

- **What it is**
  - **In scope:** The requirement that an official record a constitutional process relies on stays reliable as a record. That covers an Act Record, a System Certification Record, a Standing Record, a Forum Case Record, and any other process record. It has six parts:
    - **Attributable:** each entry and change shows who made it, in what role, and under what authority.
    - **Versioned:** a change or correction is made as a new version. Earlier versions are kept and the difference is visible. A completed record is not edited in place; later events are linked to it.
    - **Preserved:** the record and its prior versions are kept for as long as review, contest, remedy, or standing assessment can need them.
    - **Reconstructable:** the act or decision, the evidence relied on, the handoffs, refusals, and objections, and the clocks can be rebuilt from the record and its links.
    - **Reachable:** authorized reviewers can get to it through the official record path, and the public can as disclosure rules require. Privacy, confidentiality, and security rules decide who sees what. They never justify erasing the trail or making it unusable.
    - **Independent:** the sentient or system whose act is recorded does not control the record of that act. Its own logs, signatures, and attestations are inputs, not the record.
  - A process may keep the record as one record or as a linked set. No duplicate record is required. Care scales with the materiality of the act and, for a System, its class.
  - **Out of scope:** A demand for one technical mechanism, for records that can never change, for identity exposure in every context, or for disclosure beyond what the disclosure rules require. A correction made as a visible new version is not alteration. What a given record must contain stays with its owner (for an Act Record, Chapter Eight §8). Evidence that is not itself a record stays with Evidence Preservation.
- **How to measure and assess**
  - **Primary measure:** [Oversight measurement family](../core_05.020_apex_oversight_leg.md#measuring-oversight-preamble-measurement-family) and Accountability measurement family, used together.

    **Primary assessment:** Ask whether a reviewer who is not the operator can rebuild, from the record and its links alone, what was decided, by whom, on what evidence, and what changed between versions. Check who can enter or change the record, whether a change leaves a visible trace, whether prior versions are kept and reachable, whether custody is clear, and whether the record is tamper-evident where feasible.
  - **Secondary measure:** Proxy Divergence, Auditability, and Contestability.

    **Secondary assessment:** Tell real integrity from paper-only integrity: a log that can be edited without trace, a version label with no kept prior version, a hash with no clear custody, or a record split across places so that no one can rebuild it.
- **What must hold**
  - **Primary failure:** To alter, backdate, replace, delete, withhold, split, relabel, or make unreachable an official record or any prior version of it, so that a reviewer cannot rebuild what was decided, by whom, and on what basis; or to let the subject of an act control the record of that act.
  - **Secondary failure:** Records exist, but their integrity is nominal: they can change without a visible trace, prior versions are not kept, authorship or custody is unclear, or they can be reached only through the subject of the act.

## 3. What adopting it would touch

- `core_05.050_band_oversight.md`: the new entry; `core_05.000`: directory line; `tools/architecture/measurement_tier_seeds.json`: one seed (Oversight, primary), as for Certification Denial and Revocation in move 153.
- One "Read with" link each from Act Record, Attribution Integrity, Evidence Preservation, and Auditability.
- Chapter Eight §8: a one-line pointer. Its own minimum contents stay.
- Part B §8.1 intro and §8.2: link the entry. If "not edited in place" is generalized, the Part B sentence in §8.1.8 becomes an application of it.
- Chapter Ten and Chapter Thirteen §2.3: only if the custodian wants "not edited in place" stated for standing and forum case records. They were not read in full for this draft.
- Then: move-log entry, regenerated indexes, ch5-entry-format and related audits, `make audit-report`.

## 4. Decisions

1. **Placement.** Oversight band beside Evidence Preservation (recommended: the guiding question is "can sentients see, verify, and rely on what systems represent?"), or Accountability band beside Attribution Integrity and the Act Record.
2. **Name.** "Record Integrity" matches Attribution Integrity and Epistemic Integrity. "Official Record Integrity" is narrower.
3. **Generalize "not edited in place once complete"?** This is the only new duty. If yes, it reaches standing records and forum case records. If no, drop that sentence from "Versioned" and leave it in Part B.
4. **A principle-level statement in Chapter One?** Evidence Preservation already hangs off Chapter One §2.1 and §13.2.1 (Truth and epistemic integrity). A short sentence there could name Record Integrity as part of that constraint. I did not read Chapter One §5 or §13.2.1 in this pass.
5. **Scaling.** The draft scales care to materiality and class, as Evidence Preservation does. Say if you want a flat rule instead.
