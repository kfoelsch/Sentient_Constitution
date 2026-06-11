## CI-7: Oversight, assurance, controls, and evidence

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4.

Institutions must operate a three-lines assurance model:
- operational ownership line,
- independent risk/compliance challenge line,
- independent assurance line.

Role concentration across lines must be limited and justified where unavoidable.

Institutions must maintain record and evidence custody sufficient for audit, contest, correction, and continuity transfer under [Evidence Preservation](../core_05-05_definitions_c_dependent_clusters.md#evidence-preservation).

### CI-7.1: Controls declaration
At least annually, each institution must publish a declaration on whether material controls are operating effectively.

If material controls fail, the declaration must include:
- failure description,
- impact estimate,
- immediate safeguards,
- remediation plan,
- progress status against prior remediation commitments.

Minimum disclosure bundle (**`INST-PROTO-11`** and **`INST-PROTO-17`** interface):
- reporting period, accountable publishing authority, and publication date;
- institutional scope, affected class/tier coverage, and affected control lane or protocol family;
- whether the failure is ongoing, contained, remediated, or reopened after prior closure;
- affected decisions, services, rights pathways, records, or supervised systems, including whether contestability or continuity duties were materially impaired;
- detection date, earliest known onset if different, and whether delayed detection or concealment occurred;
- immediate containment actions, temporary operating limits, and whether independent review or external assurance has been invoked;
- remediation owner, target dates, dependency risks, and any conditions that would require rollback, suspension, or escalation;
- comparison against prior declarations where the same control family, root cause, or remediation commitment has recurred.

Institutions must not use the controls declaration as a narrative substitute for current operational reality. If a material failure remains unresolved at publication time, the declaration must say so plainly and must identify the interim constitutional safeguard **mode**.

For supervised systems, institutions should require a supporting system-level packet proportionate to class and dependency. See `implementation/SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md` for reusable implementation templates covering system cards, model cards, post-deployment monitoring cadence, incident reporting bundles, and material control-failure disclosure packets.

### CI-7.2: External assurance triggers
Independent external assurance is mandatory when trigger thresholds are met.

Trigger criteria must be documented and published, and must include:
- class/tier threshold triggers,
- severe-incident triggers,
- repeated-control-failure triggers,
- anti-constitutional misconduct triggers.

Minimum mandatory trigger floor:
- **Class/tier floor:** institutions with governed scope that materially includes **Class A** systems, or **Class B** systems operated by or materially dependent on **Critical System Stewards**, must obtain independent external assurance on a fixed cadence defined in the published assurance protocol;
- **Severe-incident floor:** external assurance must trigger after any severe incident that materially affects rights, survival-relevant access, contestability, evidence integrity, continuity, lawful authorization, or constitutional truthfulness;
- **Repeated-control-failure floor:** external assurance must trigger where the same material control family fails repeatedly within the published review window, where remediation commitments are materially overdue, or where prior declared remediation proves ineffective;
- **Integrity-failure floor:** external assurance must trigger where substantiated corruption, fraud, concealment, retaliation against protected escalation, grave disclosure breach, or systemic conflict-control failure raises credible doubt about internal review independence;
- **Structural-change floor:** external assurance must trigger after major restructuring, authority transfer, merger, dissolution-preparation, or continuity activation where control ownership, evidence custody, or review independence materially changes.

Published trigger criteria must also state:
- the maximum time to commission assurance after a trigger is met;
- who may invoke the trigger and whether affected parties, contest-integrity monitors, or assurance-line actors may demand review;
- the minimum scope of the assurance engagement, including affected controls, records, and remediation claims;
- publication expectations for outcomes, limits, and unresolved exceptions;
- when escalation through **CI-11** (*Cross-institution coordination and escalation*) is required because local commissioning authority is conflicted, captured, unavailable, or non-responsive.

### CI-7.3: Contest-integrity monitoring (Class A and Class B)
Where institutional governed scope includes **Class A** or **Class B** systems (`corpus_systems.md` **Chapter S2**), institutions must maintain **contest-integrity** capacity as part of the **independent assurance line**, or through an equivalent documented arrangement with the same **independence** expectations. Contest-integrity functions must **not** report to the **operational ownership line** for the same contested scope. **CI-4** (*Appointment, competency, rotation, and removal*) and **CI-5** (*Conflict integrity, anti-capture, and anti-corruption*) govern appointments, conflicts, and recusal.

**Purpose.** Assess whether **contest, secondary review, audit access, and protected escalation** pathways **function in practice**. This includes **timeliness**, **accessibility**, **backlogs**, **evidence availability** within **security-constrained observability** (`core_02-04_definition_mechanics.md` **Chapter Four**), and **patterns** suggestive of **chill**, **capture**, or **retaliation**. Monitors do this without substituting for **merits adjudication** on individual disputes under `core_10-10_rights_part_c.md` **Article XII-B**, **Chapter Five** (*Procedural Fairness*, *Contestability*, *Redress and Remediation*), and **CI-6** (*Procedure integrity, contestability, and secondary review*). Monitors **escalate** structural failures to remediation, **CI-11** (*Cross-institution coordination and escalation*) where cross-institution deadlock applies, and **external assurance** triggers in this chapter.

**Dual scope.**
- **Institutional:** materially impactful decisions, contest pathways, procedure maps, and records under **CI-6** (*Procedure integrity, contestability, and secondary review*); **protected escalation** **path** under **CI-15** (*Transparency, participation, and accessible pathways*) and **`INST-PROTO-12`** where applicable.
- **System-supervised:** operator-published challenge routes, observability and verification access, and classification or **misclassification** handling under **`corpus_systems.md` Chapter S2** and **Chapter S3** and **Sentient Constitution Chapter Ten, Article XV-A** plus Article XV's verification-access provisions, within the institution’s constitutional mandate.

**Roles and constitutional mandate.** Institutions must designate one or more **contest-integrity monitors** (titles may include inspector, ombud, or equivalent). Each must have a **published constitutional mandate**. That mandate must state the role, any **explicit exclusions** from binding **merits** decisions unless a **separate** lawful role authorizes them, the **reporting line** into **independent assurance**, the **cadence** scaled to class or tier, and the **interface** to **three-lines** attestation (**`INST-PROTO-11`**). For **Class A**, at least one monitor, or a **mandatory external** participant in the function, must be **independent** or **functionally independent** of the sole operational appointing chain for the contested scope where **feasible**.

**Outputs.** Findings must be **auditable**; **material** contest-integrity failures must feed **remediation** and may invoke **`INST-PROTO-17`**. Operational pattern and evidence expectations for this subsection are referenced as **`INST-PROTO-24`**.

**Article XIII-A monitoring emphasis.** Where institutions exercise or supervise covert, secrecy-constrained, intelligence-like, or politically sensitive security powers, contest-integrity monitoring must explicitly test whether the Article XIII-A and **CF-8** (*Independent investigative service and prosecution interface*) pathways identified above function in practice. The monitor record must be sufficient to detect independence failure, protected-activity chill, secrecy-duration drift, unavailable lawful notice or disclosure pathways, and foreign, contractor, or inter-agency bypass of applicable limits without restating the underlying Article XIII-A rule set.

Where `core_09-09_forum.md` **Chapter Nine** requires **cross-forum anti-self-judging** routing, contest-integrity functions must preserve records sufficient to support **reasoned** transfer, recusal, and backup-forum activation. They must also preserve enough record to review whether the designated forum could form an **independent** panel. They must do so without displacing the assigned merits forum. See also **`corpus_joint_structure.md` CJS-3.3** (*Boundary Between Support Roles and Merits Decisions*).

---

---

**Previous file:** [ci_06_procedure_integrity_contestability_secondary_review.md](ci_06_procedure_integrity_contestability_secondary_review.md)
**Next file:** [ci_08_forum_forensic_analytical_support.md](ci_08_forum_forensic_analytical_support.md)
