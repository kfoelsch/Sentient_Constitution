# CJS-2: Specific joint interlocks and shared abstractions

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_joint_structure.md`](../corpus_joint_structure.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CJS-2** (*Specific joint interlocks and shared abstractions*).
>
> Start at the [Joint structure landing page](../corpus_joint_structure.md) for reading order, or the [joint-structure registry](cjs_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CJS-2.1 Hybrid delegated authority (delegated binding bodies)](#cjs-21-hybrid-delegated-authority-delegated-binding-bodies); [CJS-2.1.1 Composition floor](#cjs-211-composition-floor); [CJS-2.1.2 Attachment publication](#cjs-212-attachment-publication); [CJS-2.3 Cross-implementation trust integrity (joint operation model)](#cjs-23-cross-implementation-trust-integrity-joint-operation-model); [CJS-2.4 Class-scaled lane staffing and competency redundancy](#cjs-24-class-scaled-lane-staffing-and-competency-redundancy); [CJS-2.5 Shared procedural abstractions for delegated bodies and forum routing](#cjs-25-shared-procedural-abstractions-for-delegated-bodies-and-forum-routing) and related local subsections.
- Read with: **CJS-2**; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids); **CJS-2.1**; [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-1.7.1](cjs_01_scope_purpose_boundary_interface.md#cjs-171-implementation-boundary-primary-owner-to-cjs-seam).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Trust Degradation and Misleading Reliance](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance) · [O](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance) · [M](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-a) · [A](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-a) · [C](../core_05_band_continuity.md#trust-degradation-and-misleading-reliance-c)
- [Authority Stack and Internal Hierarchy](../core_05_band_integrative.md#authority-stack) · [O](../core_05_band_integrative.md#authority-stack) · [M](../core_05_band_integrative.md#authority-stack-a) · [A](../core_05_band_integrative.md#authority-stack-a) · [C](../core_05_band_integrative.md#authority-stack-c)
- [Adjudication and Dispute Resolution](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [O](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [M](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [A](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [C](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-c)
- [Classification-Scaled Governance](../core_05_band_oversight.md#classification-scaled-governance) · [O](../core_05_band_oversight.md#classification-scaled-governance) · [M](../core_05_band_oversight.md#classification-scaled-governance-a) · [A](../core_05_band_oversight.md#classification-scaled-governance-a) · [C](../core_05_band_oversight.md#classification-scaled-governance-c)
- [Emergency and Contingency](../core_05_band_continuity.md#emergency-and-contingency-constitutional) · [O](../core_05_band_continuity.md#emergency-and-contingency-constitutional) · [M](../core_05_band_continuity.md#emergency-and-contingency-constitutional-a) · [A](../core_05_band_continuity.md#emergency-and-contingency-constitutional-a) · [C](../core_05_band_continuity.md#emergency-and-contingency-constitutional-c)
- [Incentive Alignment](../core_05_band_integrative.md#incentive-alignment) · [O](../core_05_band_integrative.md#incentive-alignment) · [M](../core_05_band_integrative.md#incentive-alignment-a) · [A](../core_05_band_integrative.md#incentive-alignment-a) · [C](../core_05_band_integrative.md#incentive-alignment-c)
- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [System](../core_05_band_continuity.md#system-definition) · [O](../core_05_band_continuity.md#system-definition) · [M](../core_05_band_continuity.md#system-definition-a) · [A](../core_05_band_continuity.md#system-definition-a) · [C](../core_05_band_continuity.md#system-definition-c)
- [System Capture](../core_05_band_continuity.md#system-capture) · [O](../core_05_band_continuity.md#system-capture) · [M](../core_05_band_continuity.md#system-capture-a) · [A](../core_05_band_continuity.md#system-capture-a) · [C](../core_05_band_continuity.md#system-capture-c)
- [Trustworthiness](../core_05_band_continuity.md#trustworthiness) · [O](../core_05_band_continuity.md#trustworthiness) · [M](../core_05_band_continuity.md#trustworthiness-a) · [A](../core_05_band_continuity.md#trustworthiness-a) · [C](../core_05_band_continuity.md#trustworthiness-c)
- [Dependency](../core_05_band_continuity.md#dependency) · [O](../core_05_band_continuity.md#dependency) · [M](../core_05_band_continuity.md#dependency-a) · [A](../core_05_band_continuity.md#dependency-a) · [C](../core_05_band_continuity.md#dependency-c)
- [Trust](../core_05_band_continuity.md#trust) · [O](../core_05_band_continuity.md#trust) · [M](../core_05_band_continuity.md#trust-a) · [A](../core_05_band_continuity.md#trust-a) · [C](../core_05_band_continuity.md#trust-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Competency Bar](../core_05_band_accountability.md#competency-bar) · [O](../core_05_band_accountability.md#competency-bar) · [M](../core_05_band_accountability.md#competency-bar-a) · [A](../core_05_band_accountability.md#competency-bar-a) · [C](../core_05_band_accountability.md#competency-bar-c)
- [Competency Clearance](../core_05_band_accountability.md#competency-clearance) · [O](../core_05_band_accountability.md#competency-clearance) · [M](../core_05_band_accountability.md#competency-clearance-a) · [A](../core_05_band_accountability.md#competency-clearance-a) · [C](../core_05_band_accountability.md#competency-clearance-c)
- [Governance](../core_05_band_accountability.md#governance) · [O](../core_05_band_accountability.md#governance) · [M](../core_05_band_accountability.md#governance-a) · [A](../core_05_band_accountability.md#governance-a) · [C](../core_05_band_accountability.md#governance-c)
- [Sentient](../core_05_band_participation.md#sentient-composite) · [O](../core_05_band_participation.md#sentient-composite) · [M](../core_05_band_participation.md#sentient-composite-a) · [A](../core_05_band_participation.md#sentient-composite-a) · [C](../core_05_band_integrative.md#sentient-composite-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Material](../core_05_band_oversight.md#material) · [O](../core_05_band_oversight.md#material) · [M](../core_05_band_oversight.md#material-a) · [A](../core_05_band_oversight.md#material-a) · [C](../core_05_band_oversight.md#material-c)

</details>

<br>

This file is the joint-structure implementation home for **CJS-2** (*Specific joint interlocks and shared abstractions*).

*In plain terms: this file names the concrete places where systems, institutions, and forum rules must connect in operation — who sits on decision bodies, how trust claims hold up across layers, minimum staffing and backup for high-impact roles, and shared procedure terms both sides use. Seam and owner-boundary drafting rules live in **CJS-1.7.1**, not here.*

- **General cross-file rules** — [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md) (including **CJS-1.7.1** primary-owner-to-CJS seam)
- **Detailed operational terms** — [cjs_03_cross_implementation_operational_terms.md](cjs_03_cross_implementation_operational_terms.md)
- **Full owner detail** — **CI** and **CF**, as **CJS-0.1** (*Topic router (stable IDs)*) directs
<a id="cjs-21-mandatory-hybrid-authority-composition-delegated-binding-bodies"></a>

## CJS-2.1 Hybrid delegated authority (delegated binding bodies)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Downstream: [CJS-2.1.1 Composition floor](#cjs-211-composition-floor); [CJS-2.1.2 Attachment publication](#cjs-212-attachment-publication).
- Read with: **CJS-2.1**; **CJS-2.1.1**; **CJS-2.1.2**; [CJS-0.1](cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids).
- Topic routing (mandatory read-with): **CJS-R01** (*Delegated binding bodies and hybrid composition (non-forum institutions)*) in **CJS-0.1** (*Topic router*); primary owner **CI-9.3**.
- Topic routing (mandatory read-with): **CJS-R02** (*Forum chambers, divisions, and designated panels (Chapter Eleven famili…*) in **CJS-0.1** (*Topic router*); primary owner **CF-3**.

</details>

<br>

*In plain terms: this package covers hybrid decision bodies for institutions and forums in two steps — **CJS-2.1.1** (*Composition floor*) says who must be on the body; **CJS-2.1.2** (*Publication mechanics*) says what the published rules must spell out about how long members serve. Both steps must be satisfied.*

A hybrid design that names home and rotating roles but omits **CJS-2.1.2** publication mechanics does not satisfy **CJS-2.1**.

- **Composition floor** — [CJS-2.1.1](#cjs-211-composition-floor)
- **Attachment publication** — [CJS-2.1.2](#cjs-212-attachment-publication)### CJS-2.1.1 Composition floor
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-2.1.1**; **CJS-2.1.2**; **CJS-2.1**; **CI-9.3.1**; **CI-9.3.2**; **CF-3.5** through **CF-3.8**; **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship**.

</details>

<br>

*In plain terms: a group that makes binding decisions cannot be all long-serving insiders or all newcomers. It must mix stable "home" members with rotating members — and home members must usually be the minority when the group decides together.*

**Who this covers**

- **Institution decision bodies** — committees, divisions, and similar bodies below a parent institution that make binding decisions; owner detail in **CI-9.3** (*Delegated subunits, institutional design class, and attachment discipline*); router topic **CJS-R01** in **CJS-0.1** (*Topic router (stable IDs)*)
- **Forum chambers and panels** — chambers, divisions, and designated panels under **CF-3.5** (*Chamber creation, identification, and family boundary*) through **CF-3.8** (*Specialist and technical chamber discipline*); router topic **CJS-R02** in **CJS-0.1** (*Topic router (stable IDs)*)

**The hybrid mix required**

Every covered body must use a **hybrid design** that includes both:

- **Home-based authority** — members who serve long enough to keep continuity and institutional memory.
- **Rotating authority** — members who rotate in to bring broader perspective, case-specific expertise, and limits on insider control.

**When a group decides together.** Home-based members must be a **minority** on the deciding group unless the rules use an equivalent published alternative across stages — for example staged roles, mandatory review, or a second review step before the decision binds.

**When one member may decide alone.** If the rules lawfully allow a single member or sole officer to decide, the overall workflow must still include both continuity and rotation somewhere in the path to that decision.

**Emergencies only.** A body that uses only home-based members or only rotating members **fails this rule** for ordinary binding decisions. The only exception is a **published emergency** plan allowed under the **primary owner**'s continuity rules. Any emergency exception must stay within the emergency, and the rules must document how the body returns to the hybrid mix afterward.

**When institution and forum rules both apply.** Where **CI** and **CF** both speak to the same body, the **stricter** clearly adopted rule governs.

## CJS-2.1.2 Attachment publication
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-2.1.2**; **CJS-2.1.1**; **CJS-2.1**; **CI-9.3.3**; **CI-9.3.4**; **CF-12** through **CF-14**.

</details>

<br>

*In plain terms: once the hybrid mix is required (**CJS-2.1.1**), the published rules must spell out how long rotating members serve, how home-member terms work, and who may not change those durations in secret.*

Where **CJS-2.1** (*Hybrid delegated authority (delegated binding bodies)*) applies, the instrument must publish:

- a bounded formula for rotating attachment that rotating authorities can understand before service;
- no undefined discretion over how long rotating attachment lasts;
- term, renewal, or stagger rules for home-based continuity; and
- any class-, forum-, institution-, emergency-, or substitution-specific safeguards required by **CI-9.3** (*Delegated subunits, institutional design class, and attachment discipline*), **CF-3.5** (*Chamber creation, identification, and family boundary*), **CF-12** (*Forum continuity*), **CF-13** (*Fallback operation*), **CF-14** (*Emergency adjudication*), or related hooks.

Sample formulas are illustrative unless a **primary owner** makes them mandatory. Home-based term rules do not need to mirror rotating attachment rules.

## CJS-2.3 Cross-implementation trust integrity (joint operation model)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-2.3**; [Chapter One §8.4.4](../core_01_b_interaction_interpretation.md#844-combined-satisfaction) (*combined satisfaction*); [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#833-incorporation-layer) (*stricter-wins*); **CJS-1.10**.
- Topic routing (primary owner): **CJS-R17** (*Cross-implementation trust integrity (joint operation model)*) in **CJS-0.1** (*Topic router*).; see that row for mandatory read-with.

</details>

<br>

*In plain terms: a trust claim is only as strong as the whole chain behind it. If one implementation file looks reassuring while another in the same chain still leaves gaps that block observation, verification, or challenge, the claim fails — and institutions must publish a map of what supports it, how to contest it, and who fixes it.*

Use this rule for **CJS-R17** (*Cross-implementation trust integrity (joint operation model)*), cross-implementation trust integrity, and for any trust claim that depends on more than one system, institution, dependency, or implementation layer working together.

The meanings of **Trust**, **Trustworthiness**, and **Trust Degradation and Misleading Reliance** remain in `core_05-05_definitions_c_dependent_clusters.md` **Chapter Five, section 3.39**. This subsection only explains the joint-operation duties.

A trustworthiness claim is non-compliant if one implementation file gives reassuring signals while another implementation file in the same chain leaves unresolved problems that defeat observable, verifiable, or contestable reliance.

For implementation routing, **Class A**, **Class B**, and **Class C** systems follow [corpus_systems.md](../corpus_systems.md) **CS-3 — System classification and handling** and **CS-4 — Critical system stewardship** for class-scaled trustworthiness assurance. **Class L** and **Class P** systems follow **CS-3** criteria and limits, apply **Chapter Seven §3** evaluation discipline at proportionate depth (**Class L**, mandatory) or as encouraged practice (**Class P**), and may not evade obligations where material external effects exist.

Where trust depends on multiple systems, institutions, dependencies, or implementation layers, institutions must maintain a published and auditable map that identifies:
- the implementation duties, classification conditions, dependencies, steward duties, and assurance burdens supporting the trust claim;
- the contest, escalation, evidence, and correction routes affected sentients can use; and
- the accountable owners for correction and restoration.

Trust claims must remain consistent with [Chapter One §8.4.4](../core_01_b_interaction_interpretation.md#844-combined-satisfaction) (*Combined satisfaction of jointly applicable incorporated obligations*), **CJS-1.10 — Classification alignment for supervised scope**, and [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#833-incorporation-layer) (*Incorporation layer*, including cross-file stricter-wins), and with the following **Implementation and cross-implementation** clusters from **CJS-3** (*Implementation and cross-implementation operational cluster library*) where those operational facts materially support the trust claim:

- **CJS-3.3** (*Oversight: auditability and reconstructability terms*)
- **CJS-3.5** (*Oversight: independent verification and claim-integrity terms*)
- **CJS-3.9** (*Participation: salience integrity and attention-allocation terms*)
- **CJS-3.10** (*Participation: disclosure sufficiency and observability terms*)
- **CJS-3.16** (*Continuity: dependency integrity and disclosure terms*)
- **CJS-3.17** (*Continuity: interoperability, portability, and exit-integrity terms*)
- **CJS-3.18** (*Continuity: data-retention and lifecycle-integrity terms*)
- **CJS-3.19** (*Continuity: graceful degradation and failure-mode integrity terms*)
- **CJS-3.20** (*Continuity: reversibility and containment terms*)

## CJS-2.4 Class-scaled lane staffing and competency redundancy
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-2.4**; **CJS-3.0**.
- Topic routing (mandatory read-with): **CJS-R18** (*Class-scaled lane staffing and competency redundancy for materially bin…*) in **CJS-0.1** (*Topic router*); primary owners **CI-3**, **CI-4**, **CI-11**, **CI-12**.

</details>

<br>

*In plain terms: high-impact roles cannot depend on one sentient. For materially binding constitutional lanes — especially under higher-risk system classes — institutions need enough qualified sentients, documented backup and succession, and real spread of knowledge so the lane stays competent without becoming fragile or captured.*

Use this rule for **CJS-R18** (*Class-scaled lane staffing and competency redundancy for materially binding stewardship*), class-scaled lane staffing and competency redundancy for materially binding stewardship. It covers roles with materially binding effect under **Chapter Six**, section **5**, where `corpus_systems.md` **CS-3 — System classification and handling** or **CS-4 — Critical system stewardship** scales the burden.

Before applying role, role-holder, stewardship, operator, accountable-role, or lane terms in this subsection, apply **CJS-3.0** (*Cross-band: Role-definition preface and standing competency bar and clearance interface*), [Chapter Nine §6.2](../core_09-09_standing_integration.md#62-competency-bars-and-clearances) (*Competency bars and clearances*), and any controlling standing lock under [Chapter Nine §4.2](../core_09-09_standing_integration.md#42-general-standing-locks) or [§5.5](../core_09-09_standing_integration.md#55-special-locks).

For **constitutional lane** and functional-separation meaning, apply **CJS-3.11** (*Constitutional lane and functional separation*) with **CI-3** (*Institutional design and separation of powers*).

For **Class A** and **Class B** systems, each institution that hosts a constitutional lane with materially binding duties must have:
- at least **three sentients** assigned to the lane;
- documented competency and succession coverage for that lane; and
- no single sentient who is the only qualified actor for the lane's materially binding duties.

Role-boundary design must balance sustained engagement with community redundancy. Role holders need enough recurring, bounded responsibility to develop and retain competence, while the lane keeps cross-training, backup coverage, and cross-functional familiarity sufficient for continuity, review, and succession.

Staffing must be real, not just numerical. Responsibility cannot be spread so thin that nobody is competent, and knowledge cannot be concentrated so tightly that the lane becomes fragile, captured, or unable to replace itself.

The constitutional floor remains in `core_12-12_governance.md` **Chapter Twelve**, section **5**. Domain detail remains in **CI-3** (*Institutional design and separation of powers*), **CI-4** (*Appointment, competency, rotation, and removal*), **CI-11** (*Resource stewardship and incentive integrity*), **CI-12** (*Transparency, participation, and accessible pathways*), and `corpus_systems.md` **CS-3 — System classification and handling** and **CS-4 — Critical system stewardship**.

## CJS-2.5 Shared procedural abstractions for delegated bodies and forum routing
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: **CJS-2.5**; **CJS-3.0**.
- Topic routing (mandatory read-with): **CJS-R01** (*Delegated binding bodies and hybrid composition (non-forum institutions)*) in **CJS-0.1** (*Topic router*); primary owner **CI-9.3**.
- Topic routing (mandatory read-with): **CJS-R02** (*Forum chambers, divisions, and designated panels (Chapter Eleven famili…*) in **CJS-0.1** (*Topic router*); primary owner **CF-3**.
- Topic routing (mandatory read-with): **CJS-R03** (*Lawful panel formation, disclosure, recusal, substitution, inability-to…*) in **CJS-0.1** (*Topic router*); primary owner **CF-4**.
- Topic routing (mandatory read-with): **CJS-R04** (*Routing, intake, transfer, certification, representative treatment*) in **CJS-0.1** (*Topic router*); primary owner **CF-5**.

</details>

<br>

*In plain terms: institutions and forums use different local rulebooks, but they need the same baseline words for delegated bodies, lawful independent forums, backup routing when a lead forum cannot act in time, and representative procedures that still preserve individual contest rights. **CJS-2.5** states those shared terms; **CI** and **CF** state the full operative detail.*

This subsection gives shared **CJS** terms for the following **primary owner** procedural scopes, as routed in **CJS-0.1** (*Topic router (stable IDs)*):

- **CI-9.3** (*Delegated subunits, institutional design class, and attachment discipline*)
- **CF-3** (*Forum formation, forum-structure mapping, and chamber structure*)
- **CF-4** (*Panel formation, disclosure, recusal, and lawful bench constitution*)
- **CF-5** (*Routing operations, transfer, certification, and representative treatment*)

Apply the operational evaluation terms in **CJS-3.13** (*Accountability: procedural integrity and adjudication terms*). This subsection does not replace **CI** or **CF** detail.

Before applying these procedural role terms, apply the role-definition preface in **CJS-3.0** (*Cross-band: Role-definition preface and standing competency bar and clearance interface*), including the competency bar, clearance, and standing interface.

- **Delegated binding body:** a standing or recurring body below a parent institution that exercises materially binding delegated authority within a published scope.
- **Lawful independent forum:** an adjudicative or equivalent merits forum formed under published authority, with required competence, quorum, and conflict-screened independence.
- **Backup activation:** documented transfer or co-routing to a designated backup forum when the lead forum cannot provide lawful independent merits determination in time.
- **Representative treatment:** procedure resolving common questions for a broader affected group only when commonality, notice, adequate representation, and contestability are preserved.

For **CI-9.3** (*Delegated subunits, institutional design class, and attachment discipline*), a **delegated subunit** is the institutional application of **Delegated binding body**: a standing or recurring internal body, including a division, chamber, committee, designated panel, or regional or functional office with decision rights, that exercises materially binding delegated authority for the parent institution and is not the institution's sole governing plenary.

Forum-specific detail, including forum families, routing, appeals, and specialist chamber doctrine, remains in `corpus_forum.md` **CF-3** (*Forum formation, forum-structure mapping, and chamber structure*) and related **CF** sections. Where **CF-3.6** (*Chamber authority composition and service mechanics*) states forum-specific delegated-authority duties or illustrations, **CF** text governs for **Chapter Eleven** forums. Where **CI** and **CF** obligations overlap, the stricter clearly adopted rule governs under [Chapter One §8.4.3](../core_01_b_interaction_interpretation.md#833-incorporation-layer) (*Incorporation layer*, including cross-file stricter-wins).

It is non-compliant to treat a body or route as valid if the records do not make lawful authority, independence safeguards, backup routes, and contest routes auditable where they materially apply.

It is also non-compliant to use common-question procedures to suppress material sentient-specific contest rights required by owner rules.

Owner detail remains in `corpus_institutions.md` including **CI-6** (*Procedure integrity, contestability, and secondary review*), **CI-8** (*Cross-institution coordination and escalation*), **CI-9.3** (*Delegated subunits, institutional design class, and attachment discipline*), and `corpus_forum.md` including **CF-4** (*Panel formation, disclosure, recusal, and lawful bench constitution*), **CF-5** (*Routing operations, transfer, certification, and representative treatment*), and **CF-6** (*Appeal, secondary review, and exhaustion pathways*).

---

**Previous file:** [cjs_01_scope_purpose_boundary_interface.md](cjs_01_scope_purpose_boundary_interface.md)

**Next file:** [cjs_03_cross_implementation_operational_terms.md](cjs_03_cross_implementation_operational_terms.md)
