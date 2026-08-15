# CF-9: Independent investigative service and prosecution interface

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_forum.md`](../corpus_forum.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CF-9** (*Independent investigative service and prosecution interface*).
>
> Start at the [Forums landing page](../corpus_forum.md) for reading order, or the [forums registry](cf_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven §7](../core_11-11_forum.md#7-forum-support-before-during-and-after-review) (*forum support before, during, and after review — inspection and investigative interfaces*); [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CF-9.1 Basic rule](#cf-91-basic-rule); [CF-9.2 Why independence matters](#cf-92-why-independence-matters); [CF-9.3 Where the investigative service belongs](#cf-93-where-the-investigative-service-belongs); [CF-9.4 What investigators may do](#cf-94-what-investigators-may-do); [CF-9.5 Required separations](#cf-95-required-separations); [CF-9.6 No self-investigation](#cf-96-no-self-investigation); [CF-9.7 Rights, secrecy, and protected activity](#cf-97-rights-secrecy-and-protected-activity); [CF-9.8 Records, referrals, and backup routes](#cf-98-records-referrals-and-backup-routes).
- Read with: **CF-9**; **CF-9.1**; **CF-9.2**; **CF-9.3**; **CF-9.4**; **CF-9.5**; **CF-9.6**; **CF-9.7**; **CF-9.8**.
- Topic routing (primary owner): **CJS-R08** (*Independent investigative service and prosecution interface*) in **CJS-0.1** (*Topic router*). Mandatory read-with: **CI-8**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Evidence Preservation](../core_05_band_oversight.md#evidence-preservation) · [O](../core_05_band_oversight.md#evidence-preservation) · [M](../core_05_band_oversight.md#evidence-preservation-a) · [A](../core_05_band_oversight.md#evidence-preservation-a) · [C](../core_05_band_oversight.md#evidence-preservation-c)
- [Proportionality](../core_05_band_accountability.md#proportionality) · [O](../core_05_band_accountability.md#proportionality) · [M](../core_05_band_accountability.md#proportionality-a) · [A](../core_05_band_accountability.md#proportionality-a) · [C](../core_05_band_accountability.md#proportionality-c)
- [Accountability](../core_05_apex_accountability_leg.md#accountability) · [O](../core_05_apex_accountability_leg.md#accountability) · [M](../core_05_apex_accountability_leg.md#accountability-m) · [A](../core_05_apex_accountability_leg.md#accountability-a) · [C](../core_05_apex_accountability_leg.md#accountability-c)
- [Transparency](../core_05_band_oversight.md#transparency) · [O](../core_05_band_oversight.md#transparency) · [M](../core_05_band_oversight.md#transparency-a) · [A](../core_05_band_oversight.md#transparency-a) · [C](../core_05_band_oversight.md#transparency-c)
- [Necessity](../core_05_band_accountability.md#necessity) · [O](../core_05_band_accountability.md#necessity) · [M](../core_05_band_accountability.md#necessity-a) · [A](../core_05_band_accountability.md#necessity-a) · [C](../core_05_band_accountability.md#necessity-c)
- [Oversight](../core_05_apex_oversight_leg.md#oversight-constitutional) · [O](../core_05_apex_oversight_leg.md#oversight-constitutional) · [M](../core_05_apex_oversight_leg.md#oversight-constitutional-m) · [A](../core_05_apex_oversight_leg.md#oversight-constitutional-a) · [C](../core_05_apex_oversight_leg.md#oversight-constitutional-c)
- [Material](../core_05_band_oversight.md#material) · [O](../core_05_band_oversight.md#material) · [M](../core_05_band_oversight.md#material-a) · [A](../core_05_band_oversight.md#material-a) · [C](../core_05_band_oversight.md#material-c)
- [Unified Incident Record](../core_05_band_accountability.md#unified-incident-record) · [O](../core_05_band_accountability.md#unified-incident-record) · [M](../core_05_band_accountability.md#unified-incident-record-a) · [A](../core_05_band_accountability.md#unified-incident-record-a) · [C](../core_05_band_accountability.md#unified-incident-record-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Adjudication and Dispute Resolution](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [O](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [M](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [A](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [C](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-c)
- [Procedural Fairness](../core_05_band_participation.md#procedural-fairness-constitutional) · [O](../core_05_band_participation.md#procedural-fairness-constitutional) · [M](../core_05_band_participation.md#procedural-fairness-constitutional-a) · [A](../core_05_band_participation.md#procedural-fairness-constitutional-a) · [C](../core_05_band_participation.md#procedural-fairness-constitutional-c)
- [Dependency](../core_05_band_continuity.md#dependency) · [O](../core_05_band_continuity.md#dependency) · [M](../core_05_band_continuity.md#dependency-a) · [A](../core_05_band_continuity.md#dependency-a) · [C](../core_05_band_continuity.md#dependency-c)
- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [System Capture](../core_05_band_continuity.md#system-capture) · [O](../core_05_band_continuity.md#system-capture) · [M](../core_05_band_continuity.md#system-capture-a) · [A](../core_05_band_continuity.md#system-capture-a) · [C](../core_05_band_continuity.md#system-capture-c)
- [System](../core_05_band_continuity.md#system-definition) · [O](../core_05_band_continuity.md#system-definition) · [M](../core_05_band_continuity.md#system-definition-a) · [A](../core_05_band_continuity.md#system-definition-a) · [C](../core_05_band_continuity.md#system-definition-c)
- [Forum Family, Constitutional](../core_05_band_accountability.md#forum-family-constitutional) · [O](../core_05_band_accountability.md#forum-family-constitutional) · [M](../core_05_band_accountability.md#forum-family-constitutional-a) · [A](../core_05_band_accountability.md#forum-family-constitutional-a) · [C](../core_05_band_accountability.md#forum-family-constitutional-c)
- [Forum Family, Institutional](../core_05_band_accountability.md#forum-family-institutional) · [O](../core_05_band_accountability.md#forum-family-institutional) · [M](../core_05_band_accountability.md#forum-family-institutional-a) · [A](../core_05_band_accountability.md#forum-family-institutional-a) · [C](../core_05_band_accountability.md#forum-family-institutional-c)
- [Forum Family, Technical](../core_05_band_accountability.md#forum-family-technical) · [O](../core_05_band_accountability.md#forum-family-technical) · [M](../core_05_band_accountability.md#forum-family-technical-a) · [A](../core_05_band_accountability.md#forum-family-technical-a) · [C](../core_05_band_accountability.md#forum-family-technical-c)
- [Incentive Alignment](../core_05_band_integrative.md#incentive-alignment) · [O](../core_05_band_integrative.md#incentive-alignment) · [M](../core_05_band_integrative.md#incentive-alignment-a) · [A](../core_05_band_integrative.md#incentive-alignment-a) · [C](../core_05_band_integrative.md#incentive-alignment-c)
- [Primary-Stakes Routing](../core_05_band_accountability.md#primary-stakes-routing) · [O](../core_05_band_accountability.md#primary-stakes-routing) · [M](../core_05_band_accountability.md#primary-stakes-routing-a) · [A](../core_05_band_accountability.md#primary-stakes-routing-a) · [C](../core_05_band_accountability.md#primary-stakes-routing-c)
- [Sentient](../core_05_band_participation.md#sentient-composite) · [O](../core_05_band_participation.md#sentient-composite) · [M](../core_05_band_participation.md#sentient-composite-a) · [A](../core_05_band_participation.md#sentient-composite-a) · [C](../core_05_band_integrative.md#sentient-composite-c)
- [Systemic](../core_05_band_accountability.md#systemic) · [O](../core_05_band_accountability.md#systemic) · [M](../core_05_band_continuity.md#systemic-a) · [A](../core_05_band_continuity.md#systemic-a) · [C](../core_05_band_continuity.md#systemic-c)

</details>

<br>

This file is the forum implementation home for **CF-9** (*Independent investigative service and prosecution interface*).

## CF-9.1 Basic rule
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: **CF-9** (*Independent investigative service*) requires investigators independent enough to follow the facts wherever they lead, and keeps investigating a matter separate from deciding to charge, sanction, or close it. No body may investigate itself.*

Any institution that uses or supervises **local enforcement**, **constitutional enforcement**, or comparable public enforcement power must have access to investigators who are independent enough to follow the facts. This applies to criminal cases, civil enforcement, constitutional complaints, protective orders, administrative sanctions, and comparable public-law matters.

The investigators must have lawful authority to:

- collect and preserve evidence;
- interview witnesses, subjects, complainants, and affected parties;
- develop the factual record;
- prepare material for the body that will decide whether to charge, sue, sanction, protect, remediate, or close the matter.

## CF-9.2 Why independence matters
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: The reasoning in one line: whoever may have caused the problem must not control the investigation into it.*

The point is simple: the actors who may have caused the problem must not control the investigation into the problem.

Investigation must be institutionally separate from ordinary **local enforcement**, **constitutional enforcement**, **security**, or **operational enforcement** command, and it must also be separate from the forum or panel that will make the final merits decision. This separation keeps the facts contestable, auditable, and harder to bury.

## CF-9.3 Where the investigative service belongs
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: Investigators must sit in a protected line of their own, not under the same command as the enforcement or prosecution they may need to examine.*

- **Independent home.** Investigative services should sit in an **independent assurance**, **integrity**, or similarly protected constitutional line. They must not be housed under the same ordinary command chain that carries out local enforcement, constitutional enforcement, security operations, prosecution, or final merits decision-making.
- **Accredited service model.** Adopting instruments may allow independent investigative or security-support providers to serve forums, institutions, communities, or individuals, provided the provider is lawfully accredited, qualified, and subject to published constitutional operating rules.
- **Disclosure and conflicts.** Every engagement must disclose the hiring relationship, funding source, scope of work, material dependencies, conflicts, prior related work, and any limits on independence. Disclosure is a floor, not a cure: conflicted or dependency-shaped engagements must be screened, narrowed, externally supervised, recused, or rejected where independence would otherwise fail.
- **Own mandate and reporting line.** An investigative service must have a published mandate, identifiable leadership, and reviewable assignment rules. It must also have a reporting line that is not controlled by the operational actor, party, funder, forum, prosecutor, or institution whose conduct is materially at issue.
- **Technical standards, not technical command.** **Technical** forums and specialist chambers maintain the reviewable standards for investigative methods, forensic protocols, evidence preservation, security protocols, expert qualifications, chain of custody, testing, measurement, and uncertainty treatment. They do not become the ordinary employer, dispatcher, or command hierarchy for investigators or security-support providers.
- **Integrity oversight.** The following remain governed by the independent assurance or **Integrity** line, together with [**CI-4**](../corpus_institutions/ci_04_appointment_competency_rotation_removal.md) (*Appointment, competency, rotation, and removal*) and **CI-5** (*Conflict integrity, anti-capture, and anti-corruption*):
  - independence and conflict control;
  - anti-capture protection;
  - misconduct complaints and retaliation risk;
  - backup activation;
  - anti-self-investigation safeguards.
- **Sensitive matters.** For sensitive or high-impact matters, the design should use the following, sufficient to reduce dependence on any single operational appointing chain, funder, forum, or institution:
  - mixed appointment and fixed terms;
  - transparent qualifications;
  - external participation;
  - backup assignment rules.

## CF-9.4 What investigators may do
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: The authority to take complaints, gather and preserve evidence, interview, and prepare a reasoned packet for whoever decides what happens next.*

Within lawful scope, the independent investigative service may:
- receive complaints, protected disclosures, referrals, and self-initiated matters within lawful scope;
- gather, preserve, and analyze evidence;
- interview witnesses and subjects;
- prepare reasoned investigative records and referral packets for charging, civil filing, remediation, or adjudicative use;
- request judicial or otherwise lawful authorization for coercive or secrecy-constrained investigative steps;
- coordinate with external or cross-jurisdiction bodies where jurisdiction, conflict, or capacity requires;
- provide or coordinate independent security-support assessment, protective planning, scene stabilization advice, custody-risk analysis, access-control review, or comparable support where lawful and necessary to preserve safety, evidence, or forum access.

Investigative or security-support providers must not:
- exercise arrest, detention, search, seizure, surveillance, force, compulsory-process, or secrecy-constrained authority without the lawful authorization that would be required for the same step if performed by a public body;
- convert a private retainer, institutional contract, forum assignment, or technical certification into coercive public authority;
- become the final charging authority, final merits authority, or unreviewable gatekeeper of the evidentiary record;
- suppress exculpatory, mitigating, inculpatory, impeachment, or chain-of-custody material because of funder preference, institutional pressure, forum convenience, or litigation strategy;
- use investigative or security work to intimidate protected activity, burden lawful participation, or evade rights safeguards that would apply to equivalent public action.

## CF-9.5 Required separations
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CF-9.5.1 Non-forum investigative, security-support, and enforcement roles](#cf-951-non-forum-investigative-security-support-and-enforcement-roles).
- Read with: **CF-9.5**; **CF-3.6**; **CF-9.5.1**; **CJS-2.1**; [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router.

</details>

<br>

*In plain terms: Several bodies may contribute to one matter, but each stays in its lane — investigating, charging, and deciding must not collapse into a single hand.*

Different actors may help the investigation, but each role must stay in its lane:

Where investigative, security-support, or enforcement-adjacent bodies exercise materially binding delegated authority, their authorizing instruments must publish the local and nonlocal participation design that protects independence, continuity, and capture resistance. For Chapter Eleven forums, chambers, divisions, and designated panels, apply the forum composition rule in **CF-3.6** (*Chamber authority composition and service mechanics*) read with **CJS-2.1** (*Hybrid delegated authority (delegated binding bodies)*). For non-forum security-support or enforcement-adjacent bodies, apply **CJS-2.1**, [**CI-3**](../corpus_institutions/ci_03_institutional_design_separation_of_powers.md) (*Institutional design, separation of powers, and authority custody*), and [**CI-9.3**](../corpus_institutions/ci_09_classification_linked_institutional_obligations.md) (*Delegated subunits, institutional design class, and attachment discipline*) where the body is a delegated binding body, with stricter independence, external-participation, or backup-route requirements where local independence is not credible.

### CF-9.5.1 Non-forum investigative, security-support, and enforcement roles
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

- **Investigators** develop, preserve, analyze, and explain facts. They may recommend referral, closure, remediation, or further lawful process, but they do not decide charges, sanctions, final liability, final constitutional meaning, or final standing effects.
- **Independent security-support providers** may protect sentients, evidence, records, facilities, or forum access; assess security risk; advise on stabilization; and support lawful protective measures. They must not become ordinary local enforcement, constitutional enforcement command, detention command, private coercive enforcement, or a way to bypass public authorization and review.
- **Local enforcement** may secure scenes, stabilize emergencies, execute lawful custody or access-control steps, serve process, carry out immediate protection, execute forum orders within local scope, or provide comparable local operational support. It must not have exclusive control over the investigation, especially when local enforcement personnel, detention personnel, security services, charging authorities, alignment enforcement authorities, forums, or closely aligned actors may be subjects, witnesses, or materially interested participants.
- **Constitutional enforcement** may execute forum orders, preservation duties, Rights-Floor safeguards, system-alignment conditions, institutional-compliance measures, anti-capture remedies, and cross-jurisdiction enforcement steps within lawful scope. Because constitutional enforcement often depends on technical records, audit trails, forensic methods, system controls, and compliance architecture, it must remain especially tied to Technical standards, Integrity oversight, and forum-review safeguards.
- **Charging authorities** may decide, within lawful scope, whether to bring charges, file civil or public-law claims, take settlement positions, or choose litigation strategy. They must not monopolize the underlying fact-development, suppress independent preservation, or make continued investigation depend on a desired litigation outcome.
- **Alignment enforcement authorities** may decide, within lawful scope, whether to seek alignment conditions, pursue remediation or constraint orders, take remediation positions, or choose alignment-enforcement strategy. They may present or pursue alignment-enforcement matters before **Integrity** forums, but they do not become the **Integrity** forum, the final merits panel, or the final constitutional-alignment recognition authority. They must not monopolize the underlying fact-development, suppress independent preservation, or make continued investigation depend on a desired enforcement outcome.

### CF-9.5.2 Forum and forum-adjacent roles
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

- **Forums** may authorize warrants, compulsory process, preservation orders, secrecy limits, and comparable intrusive steps. They may resolve disputes about scope, privilege, rights, standards compliance, admissibility, and the finished record. They must not become the routine managers of investigators or quietly turn executive fact-development into chamber work.
- **Technical forums** may set, revise, and review investigative and security standards, including forensic quality, evidentiary sufficiency, expert qualifications, security protocols, testing methods, chain of custody, uncertainty treatment, and standards conformance. They may answer certified technical questions, but they must not displace primary-stakes routing or become the merits forum merely because investigative or security standards are involved.
- **Integrity or independent assurance bodies** monitor independence, conflicts, capture, retaliation, disclosure completeness, provider misconduct, and backup-route activation. They do not become case prosecutors or final merits panels unless another lawful rule independently gives them that role.

## CF-9.6 No self-investigation
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: No body keeps sole control of an inquiry into its own misconduct. Where the allegations reach the usual investigators, the matter must go elsewhere.*

No body may keep sole control over an investigation into its own misconduct, capture, concealment, retaliation, corruption, recusal failure, evidence tampering, or comparable integrity breach.

If the allegations materially involve **local enforcement**, **constitutional enforcement**, **charging authorities**, **alignment enforcement authorities**, **forums**, detention personnel, executive leadership, or the investigative service itself, a published backup mechanism must activate. That mechanism must provide transfer, co-assignment, or external participation sufficient to make the investigation functionally independent.

## CF-9.7 Rights, secrecy, and protected activity
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Read with: **CF-9.7**; **CF-9**.

</details>

<br>

*In plain terms: Investigations may sometimes need sealed steps and delayed notice, but secrecy stays bounded by necessity, proportionality, and oversight — it is not a blanket exemption.*

Investigations sometimes need restrictions, delayed notice, sealed steps, compartmentalization, or special handling of protected activity. Those measures remain governed by `core_06-06_rights_part_c.md` **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **Chapter Five** (*Necessity*, *Proportionality*, *Oversight*, *Accountability*, *Transparency*), [Evidence Preservation](../core_05_band_oversight.md#evidence-preservation), and any applicable secrecy-implementation rules.

CF-9 adds a forum-interface record rule. When a secrecy-constrained or intrusive measure is requested, authorized, reviewed, renewed, narrowed, or found defective, the record must explain:
- the lawful objective;
- the scope;
- the duration, expiry, or review point;
- the minimization or segregation method;
- the protected-activity analysis, when material;
- the available exclusion, deletion, notice, derivative-use, or later-challenge path, where lawful.

## CF-9.8 Records, referrals, and backup routes
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.3](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-13-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: The record must state scope, steps, evidence, uncertainty, and reasons — including evidence that cuts against the investigators' own theory — so a closure decision can be checked.*

The investigative service must produce records that an ordinary affected sentient, a prosecutor, a forum, and a later reviewer can follow. The record must state the scope, steps taken, evidence relied on, uncertainty, preserved exculpatory and inculpatory material, and the reasons for referral or closure.

Those records must support:
- prosecutorial or civil-enforcement decisions without making the investigators the final charging or merits authority;
- forum review without turning the forums into the investigators' command hierarchy;
- contest-integrity monitoring under [**CI-7.3**](../corpus_institutions/ci_07_oversight_assurance_controls_evidence.md) (*Contest-integrity monitoring (Class A and Class B)*) without collapsing structural oversight into case management.

Where local independence is not credible because of concentration, emergency incapacity, deadlock, or systemic capture indicators, institutions must escalate to one of these:

- [**CI-8**](../corpus_institutions/ci_08_transparency_participation_accessible_pathways.md) (*Cross-institution coordination and escalation*);
- external assurance;
- another pre-designated backup body with lawful authority and practical capacity to investigate.

---

**Previous file:** [cf_08_forum_forensic_analytical_support.md](cf_08_forum_forensic_analytical_support.md)

**Next file:** [cf_10_technical_specialist_forums_specialist_chambers.md](cf_10_technical_specialist_forums_specialist_chambers.md)
