# Protocol D — Decentralized Constitutional Continuity and Partition Resilience

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_systems.md`](../corpus_systems.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **Protocol D — Decentralized Constitutional Continuity and Partition Resilience**.
>
> Start at the [Systems and data landing page](../corpus_systems.md) for reading order, or the [systems registry](cs_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<br>

This file is the systems implementation home for **Protocol D — Decentralized Constitutional Continuity and Partition Resilience**.

<br>

*In plain terms: **Protocol D** covers operating when the network splits or goes dark. Systems must define the modes they can run in — normal, partitioned, fully offline, and rejoining — and preserve the Rights Floor in every one of them, including how conflicting records are reconciled once the parts reconnect.*

Constitutional tracing: This protocol operationalizes **operational** constitutional continuity under prolonged network disruption, partition, and adversarial connectivity conditions (including LAN-level compromise or sustained denial) — distinct from the constitutional **Continuity aim** in [Chapter One §1](../core_00_preamble.md#two-constitutional-aims). It implements Sentient Constitution [Chapter One](../core_01_c_stewardship_capacity_principles.md#chapter-01-principles-and-constraints) constraints (Safety, Truth, proportionality, necessity) and the [Constitutional Tetrad](../core_00_preamble.md#constitutional-tetrad). It implements **Chapter Five** definitions where materially relevant ([*Governance Architecture…*](../core_05_band_accountability.md#governance-architecture-oversight-decentralization-and-concentration-cluster) *Governance Architecture… — Systemic Lock-In*, *Dependency*, *Oversight*, and related hubs where partition or coupling analysis applies jointly; **[Chapter One §8.24](../core_05_band_oversight.md#movement-refuge-semi-independent)** *Movement, Refuge, Non-Statelessness, and Exit Integrity* where partition or exit implicates movement, refuge, or recognition jointly; **[§11.3](../core_05_band_integrative.md#accountability-contestability-and-collective-accountability-failure-cluster)** *Accountability* and collective-accountability routing where materially relevant; **[§3.32](../core_05_band_participation.md#collective-harm-boundary-and-harm-cluster)** *Resilience*, *Reversibility*, *Safety*, *Cascading Failure*, and systemic-harm containment where materially relevant; **[Chapter One §8.17](../core_05_band_continuity.md#emergency-and-contingency-semi-independent)** *Emergency and Contingency* where prolonged disruption or contingency predicates apply). It implements **Chapter Six, **Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*)** (conflict and emergency proportionality). It implements **Article XIX** (*Interoperability, Portability, Movement, Refuge, and Exit Integrity*) (interoperability, portability, and exit integrity). It implements **Article XXV** (*Constitutional Evolution and Non-Entrenchment*) (constitutional evolution and non-entrenchment). It implements **Article XI** (*Stakeholder System Participation, Representation, and Due Process*) (stakeholder governance, participation, and due process). It implements **Article XXVI-C** (*Failure Off-Ramps, Re-Baselining, and Traceability*) where continuity-mode failure handling, off-ramps, or rejoin re-baselining are implicated. It also applies **CJS-3.19** (*graceful degradation and failure-mode integrity terms*), **CJS-3.3** (*auditability and reconstructability terms*), **CJS-3.4** (*tiered transparency and audit-access terms*), **CJS-3.5** (*independent verification and claim-integrity terms*), **CJS-3.20** (*reversibility and containment terms*), **CJS-3.18** (*data-retention and lifecycle-integrity terms*), **CJS-3.11** (*distributed and proportional authority terms*), **CJS-3.2** (*reflexive transparency and accountability terms*), and **CJS-3.13** (*procedural integrity and adjudication terms*). This protocol does not narrow Rights Floors.

<a id="1-continuity-modes-and-rights-floor-invariants"></a>
## 1. Continuity modes and Rights-Floor invariants

*In plain terms: Four named operating modes — Normal, Degraded-Partitioned, Offline-Sovereign, and Rejoin-Reconciliation — and the protections that hold in every one of them.*

Systems must define and publish at least four operational continuity modes: **Normal**, **Degraded-Partitioned**, **Offline-Sovereign**, **Rejoin-Reconciliation**.

For every mode, systems must preserve non-regression constitutional floors. Those floors include Safety, Truth (Constitutional Constraint), dignity-equality protections, meaningful agency constraints, and challengeability to the maximum feasible extent under conditions.

**Mode transitions must**:
- be trigger-defined and auditable;
- be independently reviewable at class-appropriate cadence;
- be reversible when trigger conditions clear.

<a id="2-local-first-governance-execution-under-disconnection"></a>
## 2. Local-first governance execution under disconnection

*In plain terms: When wide-area coordination is unavailable, the constitutional minimums must still run locally rather than stopping.*

High-impact systems must support local execution of constitutional minimums when wide-area coordination is unavailable.

That execution includes:
- safety and harm-containment actions;
- **Rights-Floor protection and standing triage**;
- temporary dispute handling with recorded rationale;
- protected reporting and escalation intake.

Local execution authority must be scope-limited, time-bounded, and constrained by least-restrictive and reversibility requirements.

<a id="3-partition-safe-decision-constraints"></a>
## 3. Partition-safe decision constraints

*In plain terms: Decisions made while disconnected need a scope cap, an expiry, and a restoration trigger. Irreversible action needs a higher bar.*

During Degraded-Partitioned or Offline-Sovereign modes: **binding decisions must include explicit scope caps, expiry, and restoration triggers**.

**Irreversible actions require elevated burden and independent review where feasible**.

**Default preference is reversible or compensably restorable interventions**.

**Anti-capture checks must account for reduced oversight diversity under partition**.

Decisions taken under partition remain challengeable and must be revalidated during Rejoin-Reconciliation.

<a id="4-offline-audit-integrity-and-reconciliation"></a>
## 4. Offline audit integrity and reconciliation

*In plain terms: Keep a tamper-evident local record while disconnected, marked with what was uncertain, so it can be reconciled honestly on rejoin.*

Systems must maintain tamper-evident local audit chains while disconnected.

Those chains use **append-only event records with integrity proofs**. They use **explicit local clock/confidence metadata and uncertainty markers**. They use **immutable linkage between decisions, evidence references, and authority basis**.

**Upon reconnection**, systems must:
- execute reconciliation that preserves lineage and conflict visibility;
- identify and flag inconsistent histories or unverifiable segments;
- apply predeclared conflict-resolution rules with independent review for high-impact divergence.

<a id="5-decentralized-trust-anchor-and-credential-continuity"></a>
## 5. Decentralized trust anchor and credential continuity

*In plain terms: No single credential authority may be the thing everything depends on, and rotating keys in an emergency must be time-bounded and revocable.*

Systems must avoid single-anchor dependence for constitutional continuity.

They must:
- support threshold or multi-party trust recovery pathways;
- rotate/revoke compromised credentials with local fallback procedures;
- maintain node exclusion and re-admission criteria under compromise suspicion;
- prevent isolated authorities from permanently entrenching trust state without post-rejoin validation.

**5A. Threshold recovery and emergency trust-anchor rotation safeguards.** Threshold recovery and emergency rotation procedures must include anti-seizure and anti-replay controls.

**Trust-state changes and rotation:**
- **Emergency trust-state changes require threshold approval from independently controlled parties.** No single operator or jurisdictional endpoint may unilaterally re-anchor binding authority.
- **Emergency rotation events must use** time-bounded authorization windows, one-time activation artifacts, and explicit scope limits.
- **Replay protection is mandatory** for recovery and rotation messages (unique event identifiers, nonce or challenge mechanisms, monotonic sequence or equivalent freshness guarantees).
- **Stale, duplicated, or out-of-window recovery artifacts are invalid** and must trigger incident review.
- **Each rotation or recovery event must produce an auditable chain** linking initiating trigger, approving parties, artifacts used, and resulting trust-state.

**Anti-seizure constraints:**
- **Trust-anchor custodianship must be distribution-preserving during emergency mode** (no durable consolidation into a single steward plane).
- **If threshold participants are unavailable,** temporary degraded trust operation may continue only with reduced binding scope, strict expiry, and mandatory post-rejoin revalidation.
- **Any emergency trust state established under degraded conditions is provisional** and cannot permanently override predeclared constitutional trust-baseline rules without independent post-incident review.

<a id="6-performance-and-reliability-under-decentralized-operation"></a>
## 6. Performance and reliability under decentralized operation

*In plain terms: Publish measurable targets for how the system performs while partitioned, and never let those targets become a reason to lower a protection.*

Class-scaled continuity profiles must define measurable decentralized performance targets (for example, local decision latency, offline survivability duration, and reconciliation convergence bounds).

Targets must be auditable and periodically reviewed, and must scale with the **CS-3** (*System classification and handling*) class and the **CS-4** (*Critical system stewardship*) stewardship tier where applicable. Targets must never justify weakening constitutional Rights Floors or verification integrity.

<a id="7-rejoin-de-escalation-and-anti-normalization"></a>
## 7. Rejoin, de-escalation, and anti-normalization

*In plain terms: Coming back means staged restoration of normal governance, so that emergency operation does not quietly become the new baseline.*

Rejoin-Reconciliation mode must include **staged restoration of normal governance pathways**.

It must:
- include retrospective review of partition-period decisions and harms;
- include correction, reversal, or remediation for decisions that fail post-rejoin validation;
- include publication of lessons, control updates, and recurrence-reduction actions.

Persistent operation in degraded modes without renewed necessity and independent review is non-compliant and must trigger structural oversight escalation.

<a id="8-self-healing-under-decentralized-continuity"></a>
## 8. Self-healing under decentralized continuity

*In plain terms: How automatic detection, containment, and recovery apply across the four modes — without masking the failure that triggered them.*

This section is the **Article XII-F** (*Resilience and Self-Healing Baseline*) implementation profile. It applies **Protocol A**, subsection **H** (*Self-healing and recovery-path integrity*), to the four continuity modes defined in section **1**: **Normal**, **Degraded-Partitioned**, **Offline-Sovereign**, and **Rejoin-Reconciliation**. It is not a second self-healing profile.

Detection, containment, safe-failure preference, non-masking, Rights-Floor continuity, autonomy scaling, and root-cause closure remain governed by **Sentient Constitution Chapter Six, Article XII-F** (*Resilience and Self-Healing Baseline*), **Chapter One §4.1**, and **Chapter Five** [*Self-Healing*](../core_05_band_continuity.md#self-healing-constitutional). Protocol A subsection **H** supplies the test, verify, and deploy profile. This section adds only the decentralized-continuity cross-checks below.

- Offline and partitioned modes must maintain tamper-evident local recovery-event chains consistent with section **4** (offline audit integrity), and must reconcile recovery events on rejoin rather than treating mode-internal recovery as closed.
- Recovery across partitions must not alter persistent state, credentials, obligations, or configurations attributed to sentients, operators, or other systems **in other partitions** that fall **outside** the declared fault-and-recovery scope except through changes that satisfy **Article XV-A** (*Auditability and Observable Evidence*) [Auditability](../core_05_band_oversight.md#auditability) for observability and attribution and that, where parties in those partitions are materially affected, include proportionate notice, authorization, or contestable handoff consistent with **Chapter Six**.
- Recovery authority must not expand beyond the pre-fault envelope in any partition and must not propagate failure through [Cascading Failure](../core_05_band_continuity.md#cascading-failure) pathways exposed by partition topology.
- Recovery actions taken under partition that prove invalid on rejoin must be subject to section **7**'s correction, reversal, or remediation pathway.
- Mode transitions, provisional trust states under section **5A**, and emergency-authority invocations must not suppress, overwrite, or delay evidence needed for root-cause analysis under **Article XXI-A** (*Diagnostic Rigor and Causal Attribution*). Reconciliation on rejoin must treat masked or under-logged recovery as a post-rejoin validation failure under section **7**.
- Where Rights-Floor capacity is genuinely constrained by partition topology, narrowing must be explicit, time-bound, and restoration-triggered, and must be treated as **Article XXVI** (*Transition Governance, Continuity, and Re-Baselining*) transition-governance territory at rejoin.
- Partition-local contestability intake, audit emission, or external-review pathways must remain materially external or independently verifiable within the partition and must reconcile on rejoin.
- Self-healing that succeeds operationally in a partitioned or offline mode but leaves a known defective condition in place must carry the Protocol A open root-cause obligation into Rejoin-Reconciliation mode. Recurrence across partition cycles or rejoin cycles remains a single open obligation, not closure of each incident.

Where this section is silent, Protocol A subsection **H**, Chapter One §4.1, **Article XII-F** (*Resilience and Self-Healing Baseline*), and the Chapter Five definition govern. This section does not create rights and must not be read to narrow those homes.

---

---

*Corpus alignment:* edition `SC-Corpus-2026.04.33`, effective **2026-04-24**; edition and custody in [README.md](../README.md) and [Chapter Five *Corpus*](../core_05_band_integrative.md#corpus).

---

**Previous file:** [cs_protocol_r_subversion_response_replacement_reconstitution.md](cs_protocol_r_subversion_response_replacement_reconstitution.md)

**Next file:** [corpus_institutions.md](../corpus_institutions.md)
