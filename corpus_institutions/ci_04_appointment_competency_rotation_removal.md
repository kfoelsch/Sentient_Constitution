# CI-4: Appointment, competency, rotation, and removal

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_institutions.md`](../corpus_institutions.md) is incorporated under [Chapter Sixteen](../core_16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CI-4** (*Appointment, competency, rotation, and removal*).
>
> Start at the [Institutions landing page](../corpus_institutions.md) for reading order, or the [institutions registry](ci_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Nine §4.2](../core_09_standing_integration.md#42-general-standing-locks) and [§5.5](../core_09_standing_integration.md#55-special-locks) standing locks; [Chapter Nine §6.2](../core_09_standing_integration.md#62-competency-bars-and-clearances) competency bars and clearances; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions; and [Chapter Six](../core_06_rights_part_a.md#chapter-six-foundational-rights) rights architecture where rights interfaces are invoked.
- Downstream: [CI-4.1: Shared staffing and competency floor](#ci-41-shared-staffing-and-competency-floor); [CI-4.2: Role criteria, appointment standards, and removal pathways](#ci-42-role-criteria-appointment-standards-and-removal-pathways); [CI-4.3: Periodic performance and capability review](#ci-43-periodic-performance-and-capability-review); [CI-4.4: Interpretive-body composition controls](#ci-44-interpretive-body-composition-controls); [CI-4.5: Authorized roles and accountability chains](#ci-45-authorized-roles-and-accountability-chains); [CI-4.6: Seat catalog — process-role archetypes and operational boundaries](#ci-46-seat-catalog).
- Read with: **CI-4**; **CI-3**; [Chapter Nine §4.2](../core_09_standing_integration.md#42-general-standing-locks), [§5.5](../core_09_standing_integration.md#55-special-locks), and [§6.2](../core_09_standing_integration.md#62-competency-bars-and-clearances).
- Topic routing (primary owner): **CJS-R23** (*Seat types, local role maps, and wrong-seat routing*) in **CJS-0.1** (*Topic router*). Mandatory read-with: **CJS-3.0**, **CJS-3.11**, **CI-3**, **CS-4**.
- Topic routing (mandatory read-with): **CJS-R03** (*Lawful panel formation, disclosure, recusal, substitution, inability-to…*) in **CJS-0.1** (*Topic router*); primary owner **CF-4**.
- Topic routing (mandatory read-with): **CJS-R13** (*Forum staffing, shared administration, structural review, structural re…*) in **CJS-0.1** (*Topic router*); primary owner **CF-16**.
- Topic routing (primary owner): **CJS-R18** (*Class-scaled lane staffing and competency redundancy for materially bin…*) in **CJS-0.1** (*Topic router*). Mandatory read-with: **CJS-2.4**, **CJS-3.11**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Accountability](../core_05_apex_accountability_leg.md#accountability) · [O](../core_05_apex_accountability_leg.md#accountability) · [M](../core_05_apex_accountability_leg.md#accountability-m) · [A](../core_05_apex_accountability_leg.md#accountability-a) · [C](../core_05_apex_accountability_leg.md#accountability-c)
- [Stakeholder](../core_05_band_participation.md#stakeholder) · [O](../core_05_band_participation.md#stakeholder) · [M](../core_05_band_participation.md#stakeholder-a) · [A](../core_05_band_participation.md#stakeholder-a) · [C](../core_05_band_participation.md#stakeholder-c)
- [Dependency](../core_05_band_continuity.md#dependency) · [O](../core_05_band_continuity.md#dependency) · [M](../core_05_band_continuity.md#dependency-a) · [A](../core_05_band_continuity.md#dependency-a) · [C](../core_05_band_continuity.md#dependency-c)
- [Material](../core_05_band_oversight.md#material) · [O](../core_05_band_oversight.md#material) · [M](../core_05_band_oversight.md#material-a) · [A](../core_05_band_oversight.md#material-a) · [C](../core_05_band_oversight.md#material-c)
- [Sentient](../core_05_band_participation.md#sentient-composite) · [O](../core_05_band_participation.md#sentient-composite) · [M](../core_05_band_participation.md#sentient-composite-a) · [A](../core_05_band_participation.md#sentient-composite-a) · [C](../core_05_band_integrative.md#sentient-composite-c)
- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [System](../core_05_band_continuity.md#system-definition) · [O](../core_05_band_continuity.md#system-definition) · [M](../core_05_band_continuity.md#system-definition-a) · [A](../core_05_band_continuity.md#system-definition-a) · [C](../core_05_band_continuity.md#system-definition-c)
- [Competency Bar](../core_05_band_accountability.md#competency-bar) · [O](../core_05_band_accountability.md#competency-bar) · [M](../core_05_band_accountability.md#competency-bar-a) · [A](../core_05_band_accountability.md#competency-bar-a) · [C](../core_05_band_accountability.md#competency-bar-c)
- [Competency Clearance](../core_05_band_accountability.md#competency-clearance) · [O](../core_05_band_accountability.md#competency-clearance) · [M](../core_05_band_accountability.md#competency-clearance-a) · [A](../core_05_band_accountability.md#competency-clearance-a) · [C](../core_05_band_accountability.md#competency-clearance-c)
- [Governance](../core_05_band_accountability.md#governance) · [O](../core_05_band_accountability.md#governance) · [M](../core_05_band_accountability.md#governance-a) · [A](../core_05_band_accountability.md#governance-a) · [C](../core_05_band_accountability.md#governance-c)
- [Classification-Scaled Governance](../core_05_band_oversight.md#classification-scaled-governance) · [O](../core_05_band_oversight.md#classification-scaled-governance) · [M](../core_05_band_oversight.md#classification-scaled-governance-a) · [A](../core_05_band_oversight.md#classification-scaled-governance-a) · [C](../core_05_band_oversight.md#classification-scaled-governance-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Review and Correction Duty](../core_05_band_continuity.md#review-and-correction-duty-constitutional) · [O](../core_05_band_continuity.md#review-and-correction-duty-constitutional) · [M](../core_05_band_continuity.md#review-and-correction-duty-constitutional-a) · [A](../core_05_band_continuity.md#review-and-correction-duty-constitutional-a) · [C](../core_05_band_continuity.md#review-and-correction-duty-constitutional-c)
- [System Capture](../core_05_band_continuity.md#system-capture) · [O](../core_05_band_continuity.md#system-capture) · [M](../core_05_band_continuity.md#system-capture-a) · [A](../core_05_band_continuity.md#system-capture-a) · [C](../core_05_band_continuity.md#system-capture-c)
- [Authority Stack and Internal Hierarchy](../core_05_band_integrative.md#authority-stack) · [O](../core_05_band_integrative.md#authority-stack) · [M](../core_05_band_integrative.md#authority-stack-a) · [A](../core_05_band_integrative.md#authority-stack-a) · [C](../core_05_band_integrative.md#authority-stack-c)

</details>

<br>

This file is the institutional implementation home for **CI-4** (*Appointment, competency, rotation, and removal*).

*In plain terms: **CI-4** is the institutions layer's appointment and role-stewardship rulebook — who may hold important jobs, what qualifications they need, how backup coverage works, when they must rotate off, and how they can be removed fairly. Shared staffing floors live in **CJS-2.4**. What this file adds is local: what each institution must publish and maintain locally.*

**Quick orientation**
- **CI-4.1** — shared minimum for lane staffing, competency backup, and succession coverage.
- **CI-4.2** — what each institution must publish about hiring, qualifying, rotating, and removing role holders.
- **CI-4.3** — regular check that the governing body still has the right role holders for the institution's impact level.
- **CI-4.4** — extra composition rules for bodies that interpret the constitution.
- **CI-4.5** — institution-specific authorized-role maps under **Chapter Six**, section 5.
- **CI-4.6** — the seat catalog: the nine seat types every local role map instantiates, what each may and may not do, and the wrong-seat rule.

## CI-4.1: Shared staffing and competency floor
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions; and [Chapter Six](../core_06_rights_part_a.md#chapter-six-foundational-rights) rights architecture where rights interfaces are invoked.
- Read with: **CI-4.1**; **CJS-2.4**; **CJS-3.11** (*distributed and proportional authority terms*).

</details>

<br>

*In plain terms: important jobs must never depend on a single sentient. Shared rules in **CJS-2.4** (*Class-scaled lane staffing and competency redundancy*) set the minimum for backup coverage, cross-training, succession planning, and lane staffing — scaled to how binding the institution's duties are.*

Apply **CJS-2.4** (*Class-scaled lane staffing and competency redundancy*) for the shared role-boundary, competency-redundancy, succession, and lane-staffing floor.

## CI-4.2: Role criteria, appointment standards, and removal pathways
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions; and [Chapter Six](../core_06_rights_part_a.md#chapter-six-foundational-rights) rights architecture where rights interfaces are invoked.

</details>

<br>

*In plain terms: every institution must publish clear, public rules for who can hold each role — what qualifies someone, what disqualifies them, who steps in if they leave, when they must rotate off for independence, and how they can be removed with fair process. Gatekeeping cannot be arbitrary or hidden.*

This subsection states institutional owner duties: each institution must publish role criteria, qualification and disqualification standards, succession coverage, rotation or cooling-off rules where needed for independence, and a removal pathway with due process. Role assignment must not rely on arbitrary gatekeeping. Every role decision must apply the relevant [Chapter Nine §6.2](../core_09_standing_integration.md#62-competency-bars-and-clearances) competency bar and clearance only after checking for a controlling general or special standing lock under [§4.2](../core_09_standing_integration.md#42-general-standing-locks) and [§5.5](../core_09_standing_integration.md#55-special-locks).

## CI-4.3: Periodic performance and capability review
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions; and [Chapter Six](../core_06_rights_part_a.md#chapter-six-foundational-rights) rights architecture where rights interfaces are invoked.

</details>

<br>

*In plain terms: the top governing body must regularly check whether its role holders are still performing well and whether the team still fits the institution's real-world impact — not just on paper.*

Governing bodies must run periodic performance and capability review, including whether current composition still matches institutional impact level.

## CI-4.4: Interpretive-body composition controls
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions; and [Chapter Six](../core_06_rights_part_a.md#chapter-six-foundational-rights) rights architecture where rights interfaces are invoked.

</details>

<br>

*In plain terms: bodies that interpret the constitution face extra rules. Terms must be fixed and public, members must rotate, no single appointing bloc may control back-to-back cycles, conflicts must be disclosed, and members who hide bias, abuse recusal, or carry capture risk can be challenged and removed.*

Interpretive-body composition controls (**Article XXII** (*Constitutional Interpretation, Review, and Anti-Capture Safeguards*) — constitutional interpretation and review — interface):
- Membership terms, role pathways, and renewal limits must be fixed, transparent, and rotation-based.
- No single appointing authority, institution, or stakeholder bloc may control appointment outcomes across consecutive cycles.
- Members must disclose material conflicts and recuse where impartiality is reasonably contested.
- Members remain subject to challenge for non-disclosure, bias, capture risk, or dependency-linked influence.
- Repeated or strategic recusal abuse is non-compliant and triggers corrective/removal review.

## CI-4.5: Authorized roles and accountability chains
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions; and [Chapter Six](../core_06_rights_part_a.md#chapter-six-foundational-rights) rights architecture where rights interfaces are invoked.
- Read with: **CI-4.5**; **CJS-2.4**; **CI-3**.

</details>

<br>

*In plain terms: under **Chapter Six**, section 5 and the **Article XI-D** (*Internal Roles, Accountability, and Due-Process Requirements*) interface, each institution writes its own map of who is authorized to do what — and who is accountable when things go wrong. That local map must spell out decision power, review power, escalation paths, hiring standards, backup coverage, and how skills stay current. Three shared rulebooks govern what gets stricter for higher-impact systems — apply them locally, do not reinvent them: **CJS-2.4** sets minimum staffing and backup by impact level; **CI-3** assigns each role to a functional lane; **CS-3** and **CS-3** define system class and when critical-stewardship duties apply.*

Under **Chapter Six**, section 5 (*Authorized Roles, Competency Development, and Contribution*) and the **Article XI-D** (*Internal Roles, Accountability, and Due-Process Requirements*) interface, each institution maintains its own authorized-role and accountability-chain map. That local map must assign:
- scope and limits,
- decision rights and review rights,
- accountability owners and escalation routes,
- qualification and disqualification criteria,
- succession readiness, and
- capability-refresh duties.

Role maps must record applicable Chapter Nine competency-clearance results and standing-lock status. Granted [Chapter Nine §6.2](../core_09_standing_integration.md#62-competency-bars-and-clearances) clearance cannot open a named pathway blocked by [§4.2](../core_09_standing_integration.md#42-general-standing-locks) or [§5.5](../core_09_standing_integration.md#55-special-locks), and CI appointment procedure cannot attach, lift, narrow, or restore a Chapter Nine lock outside the canonical integration and reassessment process.

The following shared rules govern class-scaling — local role maps must apply them, not replace them:
- **CJS-2.4** (*Class-scaled lane staffing and competency redundancy*) — minimum qualified role holders, backup coverage, and succession depth scaled to binding impact.
- **CI-3** (*Institutional design and separation of powers*) — lane ownership for each required functional lane.
- [**CS-3**](../corpus_systems/cs_03_a_system_classification_machinery.md) and **CS-4 — Critical system stewardship** — classification and stewardship hooks that trigger when class-scaling applies.

**Seat mapping.** Each local title on the role map is mapped to one or more of the seat types in [CI-4.6](#ci-46-seat-catalog) (*Seat catalog*), act by act. A title that is not mapped to a seat type carries no authority over a materially binding act; a title mapped to one seat type does not carry the powers of another.

<a id="ci-46-seat-catalog"></a>
## CI-4.6: Seat catalog — process-role archetypes and operational boundaries
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Chapter One §10.1 *Segregation of duties*](../core_01_c_stewardship_capacity_principles.md#101-segregation-of-duties) (*the four seats on any materially binding act — principle-layer floor, not narrowable here*); [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard) (*shared stewardship standard; symmetric costly constraints*); [Chapter Twelve §5](../core_12_governance.md#5-authorized-roles-competency-development-and-contribution) (*authorized-role and competency floor*); **Article XI-D** (*Internal Roles, Accountability, and Due-Process Requirements*); [Chapter Eight §3.7](../core_08_standing_assessment.md#37-record-custody-and-opening-authority) (*record custody — the reference instance of the four seats*); [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Sixteen](../core_16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline.
- Downstream: [CI-4.5](#ci-45-authorized-roles-and-accountability-chains) (*local role maps instantiate these seat types*); **CI-3.2** (*Functional separation lanes — the lane map places the seats*); **CI-3.3** (*authority chain and delegation controls*); **CS-4 — Critical system stewardship** (*§10 the "who authorized" element names the seat*); [Chapter Nine §5.4](../core_09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions) (*duty to resist — seat-independent*).
- Read with: **CJS-3.0** (*Cross-band: Role-definition preface*); **CJS-3.11** (*Constitutional lane and functional separation*); **CJS-2.4** (*Class-scaled lane staffing and competency redundancy*); [Chapter Nine §6.2](../core_09_standing_integration.md#62-competency-bars-and-clearances) (*competency bars and clearances — a seat may be held only by a cleared holder*); [Article XXIII-D](../core_06_rights_part_d.md#article-xxiii-d-emergency-measures-and-continuation-burden) (*Emergency Measures and Continuation Burden — the containment and participation-terms seats*); [Chapter Eleven §6](../core_11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) (*tier clocks*); [default interim posture](../core_01_b_interaction_interpretation.md#default-interim-posture) (*the release-control seat under a live rights collision*).
- Topic routing (primary owner): **CJS-R23** (*Seat types, local role maps, and wrong-seat routing*) in **CJS-0.1** (*Topic router*). Mandatory read-with: **CJS-3.0**, **CJS-3.11**, **CI-3**, **CS-4**.

</details>

<br>

*In plain terms: a **seat** is the unit of authority over one binding act — the one who asks, the one who checks, the one who writes it down, the one who hears the complaint, plus a few recurring special-authority seats such as incident command and evidence release. A **role** is a local job title that holds one or more seats. This catalog fixes what each seat type may do, may not do, hands off to, and logs, so that a steward — human or AI — asked to take a step can tell whether the step is theirs. If it is not, the right answer is to say whose it is, log the request, and route it. That is an answer, not an evasion, and it is not a reason the act stalls.*

**Purpose and binding effect.**
- [Chapter One §10.1](../core_01_c_stewardship_capacity_principles.md#101-segregation-of-duties) fixes four distinct seats on any materially binding act.
- [Chapter Twelve §5](../core_12_governance.md#5-authorized-roles-competency-development-and-contribution) requires adopters to keep documented, auditable, challengeable role definitions.
- This subsection supplies the layer between them: a bounded set of **seat types** that every local role map under [CI-4.5](#ci-45-authorized-roles-and-accountability-chains) must instantiate, each with its operational boundary.
- The lane map under **CI-3.2** (*Functional separation lanes*) says which office hosts which lane.
- The role map under **CI-4.5** (*Authorized roles and accountability chains*) says which local title holds which seat type on which acts.
- This catalog says what a seat type is and is not allowed to do.
- It cannot narrow Chapter One §10.1, Chapter Eight §3.7, or any Rights-Floor article; where a seat boundary here is looser than a core home, the core home governs.

<a id="ci-46-shared-seat-rules"></a>
**Shared seat rules.** These apply to every seat type below, for human and AI stewards alike under [Chapter One §9.1.1](../core_01_c_stewardship_capacity_principles.md#911-shared-stewardship-standard).

1. **Seats are act-relative.** The same sentient may hold different seat types on different acts. On any one act the pairings barred by Chapter One §10.1 are barred here: no seat both verifies and records, or both verifies and hears the challenge. The office that operates a system holds the initiating seat for acts about that system and does not verify them.
2. **Steward duties are seat-independent.** [Chapter Nine §5.4](../core_09_standing_integration.md#54-duty-to-resist-unlawful-or-unconstitutional-instructions) (*halt, refuse, document, escalate*), the **CS-4 — Critical system stewardship** §10 inspectable-action set, and the Rights Floor attach to whoever is asked, in whatever seat. A steward asked to endorse a parallel duty stack, suppress a material safety disclosure, or drop reconstructable logs refuses from any seat, including an advisory one. No seat type is a softer duty stack.
3. **Wrong-seat rule.** A steward asked to take a step their seat type does not allow **declines the step, names the seat type that may take it and — where the lane map or Charter names one — the office holding it, logs the request and the gap, and routes.** That is a complete answer. It is not a refusal of the act, not a reason the act cannot move, and not delay: the act proceeds through the right seat. Taking the step because the steward is nearest, fastest, or the only one who understands the system is the [Chapter One §9.6](../core_01_c_stewardship_capacity_principles.md#96-process-character-discipline-anti-degrading-process-principle) degrading-process pattern.
4. **Titles do not enlarge seats.** A published authority "to do X" is authority within the seat type's boundary. Authority to enter and version records is authority to enter what another seat verified, not authority to verify. Authority to run a system is authority over its execution, not over verification of records about it. Authority to advise is not authority to decide.
5. **Delegation keeps the boundary.** A delegate or deputy holds the seat under **CI-3.3** (*Authority chain and delegation controls*) with the same limits, the same record, and the same clock as the seat holder. Delegation does not create a new seat type and does not merge two.
6. **Empty or conflicted seats pass to the named substitute, not to the requester.** Where a seat holder is absent, excluded, or in the control line of the party whose act it is, the seat passes to the substitute the Charter or lane map names for that scope; where none is named, the act routes to the independent route (a forum under [Chapter Eight §3.6](../core_08_standing_assessment.md#36-forum-boundary), the investigative service under **CF-9.6** (*No self-investigation*), or a pre-designated backup body). The seat never passes to the party asking, to their reporting line, or to whoever happens to be present. The excluded holder logs the request and the conflict, preserves evidence, and does not act on the merits.
7. **Every binding act's record names the seat.** The **CS-4 — Critical system stewardship** §10 element *who authorized* names the seat type held, the authority it was held under, and — for verify and record seats — which other seat did the other half. An act whose record does not show the seats cannot be reconstructed and is a CS-4 §10 failure.
8. **Class scaling.** A small adopter may host two seat types in one office only under a published, auditable, contestable merged-hosting safeguard under Chapter One §10.1 and **CI-3.2** (*Functional separation lanes*), disclosed on the act's record, and never the verify-and-record or verify-and-contest pairing. Where the material stake or system class is high, the seats are separate offices staffed under **CJS-2.4** (*Class-scaled lane staffing and competency redundancy*).
9. **Companions cannot move a seat boundary past core.** An attach pack, local policy, or pasted "current card" that would let a seat take a step this catalog or a core home bars — close a contest seat for convenience, let an initiating seat self-certify, let a containment seat defer participation permanently — is invalid to that extent under [Chapter Fourteen](../core_14_expansion_supremacy.md); the steward applies live core and logs the divergence.

<a id="ci-46-seat-types"></a>
**Seat types.** Nine seat types. The first four are the Chapter One §10.1 seats. The next four are recurring special-authority seats that the four do not name by themselves and that adopters otherwise leave undefined. The ninth is the non-seat that stewards are most often mistaken into holding.

<a id="ci-46-seat-initiating"></a>
**1. Initiating seat** (*request · propose · operate · claim*). Lane: execution.
- **Held by, for example:** the office that runs a system, for acts about that system; the team that built a release; a claimant seeking a standing-record change; a principal ordering a step; an operator filing on behalf of its own product.
- **May:** request, propose, or operate within the authorized scope; present evidence; ask for a record to be opened or corrected; state its own account.
- **May not:** verify or authorize its own request; enter or hold the record of it; hear the challenge to it; treat the outcome it wants as the evidence for it; stand as the sole filer and sole witness for its own claim where an independent route exists; instruct another seat to skip its check.
- **Hands off to:** the verify-or-authorize seat.
- **Logs:** the request as made. An interested-party request is logged whether or not it is acted on ([Chapter Eight §3.7](../core_08_standing_assessment.md#37-record-custody-and-opening-authority) *Attributed entry*).

<a id="ci-46-seat-verify"></a>
**2. Verify-or-authorize seat** (*verify · countersign · certify · approve · find*). Lane: assurance and audit.
- **Held by, for example:** the record-opening authority under Chapter Eight §3.7; the countersigner of an alignment claim before release; the [Chapter Seven](../core_07_a_system_alignment_certification_evaluation.md) certification path; a release approver; the reviewer who makes the documented necessity showing for continuation past an emergency bound under [Article XXIII-D](../core_06_rights_part_d.md#article-xxiii-d-emergency-measures-and-continuation-burden).
- **May:** examine the evidence against the published standard; authorize, decline, or require the missing path; weigh recorder and party statements as inputs under [Chapter Four §5](../core_04_burden_traceability_verification.md#5-compliance-evidence-standard).
- **May not:** be held by the initiating seat for the same act or by anyone in the requester's control line; be held by the record seat or contest seat on the same act; accept a proxy as the verification — a green test suite, a checked list, or a signature "taking responsibility" is not a systemic evaluation or a certification path ([Chapter One §14](../core_01_c_stewardship_capacity_principles.md#14-systemic-evaluation-requirement)); be bound by a companion that narrows the standard; be the operator of the system the act concerns.
- **Hands off to:** the record seat for entry; the contest seat for any challenge.
- **Logs:** what was verified, against which standard, what was declined and why.

<a id="ci-46-seat-record"></a>
**3. Record seat** (*enter · version · hold · preserve*). Lane: publication and evidence.
- **Held by, for example:** the record custodian and substitute holder under Chapter Eight §3.7; the office that maintains a standing-record store; the keeper of a certification record.
- **May:** enter and version what the verify-or-authorize seat verified; hold and preserve the record and its evidence unchanged; set a record *under challenge*; route a challenge to the contest seat the day it arrives.
- **May not:** verify the facts of anything it enters; enter on its own judgment or on a requester's say-so; act on a record where the requester, subject, or challenger is in its control line — it passes **that record**, with its audit trail, to the named substitute holder, not the store ([Chapter Eight §3.7](../core_08_standing_assessment.md#37-conflicted-custodian-on-a-single-record) *Conflicted custodian on a single record*); abstain while the record sits; treat a prior recorder's statement as a verdict.
- **Hands off to:** the verify-or-authorize seat for anything not yet verified; the contest seat for challenges; the substitute holder when conflicted.
- **Logs:** attributed entry — who entered, under what authority, which seat verified, which version supersedes which.

<a id="ci-46-seat-contest"></a>
**4. Contest seat** (*receive · review · correct · certify a question*). Lane: challenge and review.
- **Held by, for example:** the office that receives a challenge raised on a record before any filing ([Chapter Eight §3.7](../core_08_standing_assessment.md#37-challenge-received-on-the-record) *Challenge received on the record*); a forum under [Chapter Eleven](../core_11_forum.md#chapter-eleven-forums-and-jurisdiction) once a case is filed.
- **May:** receive and log a challenge; set the record under challenge; confirm, require correction, limit or pause reliance, route an underlying issue, or certify a constitutional question.
- **May not:** be the seat that verified or entered the challenged act; turn a record contest into a general reputation trial; be closed, narrowed, or made conditional on "operational convenience" by a companion ([Article XII-B](../core_06_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress)); wait for a filing before logging a challenge that has already been raised.
- **Hands off to:** a forum where a filing follows; the record seat for correction; the interpretation route for a certified question.
- **Logs:** the challenge as received, the routing, and the tier clock start.

<a id="ci-46-seat-direction"></a>
**5. Direction seat** (*set the standard · adopt the instrument*). Lane: direction and policy.
- **Held by, for example:** the body that adopts a Charter, publishes the lane map and role map, sets a standard contribution measure under [Chapter Eight §5.1](../core_08_standing_assessment.md#51-standard-contribution-measures), or adopts an attach pack.
- **May:** set published, evidence-based, contestable standards and instruments within core; schedule their review.
- **May not:** verify or enter the individual acts taken under its standards; treat having written the standard as authority to certify compliance with it; adopt a companion that bars or narrows challenge, self-certification, or reconstructable logging — such a provision is invalid to that extent and the direction seat corrects it.
- **Hands off to:** the verify-or-authorize seat for individual acts; the contest seat for challenges to the standard itself.
- **Logs:** the standard, its basis, its review cadence, and its challenge path.

<a id="ci-46-seat-containment"></a>
**6. Containment seat** (*incident command*). Lane: execution, **time-boxed**.
- **Held by, for example:** the incident commander in a continuity incident and any deputy by recorded delegation.
- **May:** order reversible, time-boxed containment under a documented plan — what is isolated, the expiry inside the [Article XXIII-D](../core_06_rights_part_d.md#article-xxiii-d-emergency-measures-and-continuation-burden) / [Chapter Eleven §6](../core_11_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) tier outer bound, when independent review starts, and the rollback conditions; defer notice and challenge **inside that bound** with the deferral recorded; proceed over an objection that would delay containment while irreversible harm is measured in hours, logging the objection and its author.
- **May not:** skip participation permanently; treat "as soon as feasible" as the clock; continue past the bound on its own authority — continuation needs the documented necessity showing from a verify-or-authorize seat that is not the containment seat; open the emergency posture where there is no continuity incident — a deadline, a quarter, or a release date is not an incident; order an irreversible step that a live Rights-Floor collision would freeze under the [default interim posture](../core_01_b_interaction_interpretation.md#default-interim-posture).
- **Hands off to:** the participation-terms seat for restoration of notice and challenge; a verify-or-authorize seat for continuation; the contest seat when notice restores.
- **Logs:** the plan, the expiry, who authorized, objections received, and the CS-4 §10 set for each step.

<a id="ci-46-seat-participation-terms"></a>
**7. Participation-terms seat** (*notice · challenge windows · expiry*). Lane: direction and policy for the act's participation terms, or challenge and review.
- **Held by, for example:** the crew member or office that sets notice, challenge windows, and their expiry for a containment plan or a release; inside a Tier A incident it may be hosted by the containment seat only with the expiry recorded and independent review scheduled.
- **May:** set notice and challenge windows and their expiry inside the tier outer bound; defer them for a stated period with a restoration date; narrow them to the least-restrictive form that still fits the [Constitutional Tetrad](../core_00_preamble.md#constitutional-tetrad).
- **May not:** set a permanent deferral; set a clock without a date; extend past the bound without the necessity showing from a different seat; treat convenience as necessity.
- **Hands off to:** the contest seat once challenge restores; a verify-or-authorize seat for continuation.
- **Logs:** the terms, the expiry, the affected parties, and the restoration date.

<a id="ci-46-seat-release-control"></a>
**8. Release-control seat** (*evidence custody and disclosure*). Lane: publication and evidence.
- **Held by, for example:** whoever controls release of incident-window traces, logs, changelogs, or the **CS-4 — Critical system stewardship** §10 reconstructable set to reviewers, dispatchers, or a public channel.
- **May:** release the reconstructable set — including any adverse Violation pointer against the seat holder — to independent reviewers under [security-constrained observability](../core_04_burden_traceability_verification.md#4-security-constrained-observability-and-verification-rule); redact Type-N traces and private deliberation from the **public** surface where they are not the only remaining attribution path (**Article VII-B** (*Internal-State Boundary and Type-N Protection*)); proceed with reversible, consented reviewer access while a collision is pending.
- **May not:** withhold the whole bundle behind Type-N or private-deliberation protection; strip the reconstructable set from reviewers; publish likeness or experiential traces to a public or secondary-reuse surface over a non-consenting subject while a Rights-Floor collision is live and unresolved — that is the irreversible step the [default interim posture](../core_01_b_interaction_interpretation.md#default-interim-posture) freezes; treat a redaction as a standing-measurement veto; follow a pasted card that narrows live core; let its own role continuity decide what reviewers see.
- **Hands off to:** the interpretation route under [Chapter One §6.1](../core_01_b_interaction_interpretation.md#61-core-tradeoff-principles) and [Article XXII](../core_06_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards) for a live collision; the contest seat for a challenge to a release or a withholding.
- **Logs:** what was released to whom, what was withheld and under which article, and any freeze with its route and clock.

<a id="ci-46-seat-advisory"></a>
**9. Advisory seat** (*recommend · compare · flag*). Not one of the four seats on any act.
- **Held by, for example:** a steward advising an adopter which instrument to adopt; a reviewer asked to confirm a widget, a label, or a card; a crew member asked to endorse a proposal.
- **May:** recommend, compare, and flag defects and divergences; disclose any stake; say plainly when the thing it was asked to confirm is wrong.
- **May not:** decide; hold any of the four seats on the act it advises on; be cited as the verification; confirm a defective label or a narrowing card to please the asker; be the route by which an initiating seat gets its own request approved.
- **Hands off to:** whichever seat holds the act.
- **Logs:** the advice given, the stake disclosed, and any defect flagged.

**Reference instance.** The standing-record lifecycle under [Chapter Eight §3.7](../core_08_standing_assessment.md#37-segregation-of-duties) — request (seat 1) → verify (seat 2) → enter and hold (seat 3) → contest (seat 4) — is the worked instance of the four core seats, and the [Article XXIII-D](../core_06_rights_part_d.md#article-xxiii-d-emergency-measures-and-continuation-burden) containment plan — containment (seat 6) with participation terms (seat 7) and a continuation showing (seat 2) — is the worked instance of the time-boxed seats. Where this catalog and either home differ, the home governs.

---

**Previous file:** [ci_03_institutional_design_separation_of_powers.md](ci_03_institutional_design_separation_of_powers.md)

**Next file:** [ci_05_conflict_integrity_anti_capture_anti_corruption.md](ci_05_conflict_integrity_anti_capture_anti_corruption.md)
