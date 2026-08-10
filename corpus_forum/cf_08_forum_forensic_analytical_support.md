# CF-8: Forum forensic and analytical support

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_forum.md`](../corpus_forum.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CF-8** (*Forum forensic and analytical support*).
>
> Start at the [Forums landing page](../corpus_forum.md) for reading order, or the [forums registry](cf_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<br>

This file is the forum implementation home for **CF-8** (*Forum forensic and analytical support*).

<br>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven §7](../core_11-11_forum.md#7-forum-support-before-during-and-after-review) (*forum support before, during, and after review*); [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [CF-8.1 When forensic or analytical support is required](#cf-81-when-forensic-or-analytical-support-is-required); [CF-8.2 What support personnel may do](#cf-82-what-support-personnel-may-do); [CF-8.3 Independence, conflicts, and challenges](#cf-83-independence-conflicts-and-challenges); [CF-8.4 Evidence custody and method records](#cf-84-evidence-custody-and-method-records); [CF-8.5 Reports, explanations, and emergency preservation](#cf-85-reports-explanations-and-emergency-preservation); [CF-8.6 Boundary with contest-integrity monitoring](#cf-86-boundary-with-contest-integrity-monitoring).
- Read with: **CF-8**; **CF-8.1**; **CF-8.2**; **CF-8.3**; **CF-8.4**; **CF-8.5**; **CF-8.6**; [Preamble §3.1 Using Measurements in Governance](../core_00_preamble.md#from-measurement-to-evidence-and-remedy) and [Chapter Seven](../core_07_a_system_alignment_certification_evaluation.md#chapter-seven-system-alignment-certification) (*forensic and analytical methods implement constitutional measurement categories, not a separate taxonomy*).
- Topic routing (primary owner): **CJS-R07** (*Forum forensic and analytical support*) in **CJS-0.1** (*Topic router*). Mandatory read-with: **CI-7.3**.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Verifiability](../core_05_band_oversight.md#verifiability) · [O](../core_05_band_oversight.md#verifiability) · [M](../core_05_band_oversight.md#verifiability-a) · [A](../core_05_band_oversight.md#verifiability-a) · [C](../core_05_band_oversight.md#verifiability-c)
- [Evidence Preservation](../core_05_band_oversight.md#evidence-preservation) · [O](../core_05_band_oversight.md#evidence-preservation) · [M](../core_05_band_oversight.md#evidence-preservation-a) · [A](../core_05_band_oversight.md#evidence-preservation-a) · [C](../core_05_band_oversight.md#evidence-preservation-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Accessibility](../core_05_band_participation.md#accessibility-constitutional) · [O](../core_05_band_participation.md#accessibility-constitutional) · [M](../core_05_band_participation.md#accessibility-constitutional-a) · [A](../core_05_band_participation.md#accessibility-constitutional-a) · [C](../core_05_band_participation.md#accessibility-constitutional-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Constitutional Community](../core_05_band_participation.md#constitutional-community) · [O](../core_05_band_participation.md#constitutional-community) · [M](../core_05_band_participation.md#constitutional-community-a) · [A](../core_05_band_participation.md#constitutional-community-a) · [C](../core_05_band_participation.md#constitutional-community-c)
- [Material](../core_05_band_oversight.md#material) · [O](../core_05_band_oversight.md#material) · [M](../core_05_band_oversight.md#material-a) · [A](../core_05_band_oversight.md#material-a) · [C](../core_05_band_oversight.md#material-c)
- [Sentient](../core_05_band_participation.md#sentient-composite) · [O](../core_05_band_participation.md#sentient-composite) · [M](../core_05_band_participation.md#sentient-composite-a) · [A](../core_05_band_participation.md#sentient-composite-a) · [C](../core_05_band_integrative.md#sentient-composite-c)
- [System](../core_05_band_continuity.md#system-definition) · [O](../core_05_band_continuity.md#system-definition) · [M](../core_05_band_continuity.md#system-definition-a) · [A](../core_05_band_continuity.md#system-definition-a) · [C](../core_05_band_continuity.md#system-definition-c)
- [Transparency](../core_05_band_oversight.md#transparency) · [O](../core_05_band_oversight.md#transparency) · [M](../core_05_band_oversight.md#transparency-a) · [A](../core_05_band_oversight.md#transparency-a) · [C](../core_05_band_oversight.md#transparency-c)
- [Adjudication and Dispute Resolution](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [O](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional) · [M](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [A](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-a) · [C](../core_05_band_accountability.md#adjudication-and-dispute-resolution-constitutional-c)
- [Procedural Fairness](../core_05_band_participation.md#procedural-fairness-constitutional) · [O](../core_05_band_participation.md#procedural-fairness-constitutional) · [M](../core_05_band_participation.md#procedural-fairness-constitutional-a) · [A](../core_05_band_participation.md#procedural-fairness-constitutional-a) · [C](../core_05_band_participation.md#procedural-fairness-constitutional-c)
- [Unified Incident Record](../core_05_band_accountability.md#unified-incident-record) · [O](../core_05_band_accountability.md#unified-incident-record) · [M](../core_05_band_accountability.md#unified-incident-record-a) · [A](../core_05_band_accountability.md#unified-incident-record-a) · [C](../core_05_band_accountability.md#unified-incident-record-c)
- [Corpus](../core_05_band_integrative.md#corpus) · [O](../core_05_band_integrative.md#corpus) · [M](../core_05_band_integrative.md#corpus-a) · [A](../core_05_band_integrative.md#corpus-a) · [C](../core_05_band_integrative.md#corpus-c)
- [System Capture](../core_05_band_continuity.md#system-capture) · [O](../core_05_band_continuity.md#system-capture) · [M](../core_05_band_continuity.md#system-capture-a) · [A](../core_05_band_continuity.md#system-capture-a) · [C](../core_05_band_continuity.md#system-capture-c)
- [Forum Family, Technical](../core_05_band_accountability.md#forum-family-technical) · [O](../core_05_band_accountability.md#forum-family-technical) · [M](../core_05_band_accountability.md#forum-family-technical-a) · [A](../core_05_band_accountability.md#forum-family-technical-a) · [C](../core_05_band_accountability.md#forum-family-technical-c)

</details>

<br>

*In plain terms: **CF-8** (*Forum forensic and analytical support*) gives a forum access to qualified technical help when the facts are too specialized, hidden, or tangled to weigh unaided. That help explains the evidence; it does not decide the case, prosecute it, or become a second forum.*

Where a **constitutional community** establishes, adopts, or relies on **forum** families under `core_11-11_forum.md` **Chapter Eleven**, it must ensure those families maintain or can obtain access to **independent forensic and analytical support**. In ordinary terms, a forum must have access to qualified help when the facts are too technical, hidden, fragmented, or causally tangled for the parties and the panel to handle fairly on their own.

This support exists to help the forum understand evidence. It does not create another merits forum, another prosecutor, or another decision-maker.

## CF-8.1 When forensic or analytical support is required
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: The situations where a forum must be able to call for technical help: the evidence is fragmented, restricted, highly technical, or the uncertainty could change the outcome.*

Forensic or analytical support must be available when a dispute materially involves any of the following:
- uncertainty that could change the outcome, remedy, or protected status of a sentient, community, institution, system, or environment;
- evidence that is restricted, fragmented, technically complex, difficult to interpret, or held across more than one system or institution;
- disputed causation, event reconstruction, technical failure, model behavior, record integrity, or comparable fact questions;
- suspected concealment, tampering, deletion, selective disclosure, or chain-of-custody failure;
- evidence dependencies that ordinary party presentation, ordinary audit records, or judicial notice cannot fairly resolve.

The support requirement is practical, not decorative. If a case cannot be fairly decided without competent help preserving, testing, reconstructing, or explaining material evidence, the forum must have a lawful way to obtain that help.

## CF-8.2 What support personnel may do
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: Titles vary — inspector, analyst, special master — but the scope must be written down, and the record must make clear to the parties what the appointee was asked to do.*

Support personnel may be called **forum inspectors**, **forensic analysts**, **special masters**, technical reviewers, evidence custodians, or comparable titles. Whatever title is used, the record must make the support role understandable to the parties and to later reviewers.

Within a **published** or **reasoned** scope order, support personnel may:
- identify and preserve relevant evidence;
- reconstruct events, technical states, transactions, communications, model behavior, or other material facts;
- test records, artifacts, systems, samples, logs, methods, or claimed causal explanations;
- explain technical or specialized material in a form the forum and affected parties can understand;
- state uncertainty, limits, assumptions, and alternative explanations.

Support personnel must not impose sanctions, decide liability, make final credibility determinations reserved to the forum, or issue binding merits rulings unless a separate lawful role independently authorizes that action. Their job is to make the evidence more reliable and understandable, not to decide the case for the panel.

## CF-8.3 Independence, conflicts, and challenges
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: Technical helpers face the same conflict screening as decision-makers, and parties must have a real way to challenge who was appointed.*

Appointment, conflict disclosure, recusal, and challenge pathways must satisfy `corpus_institutions.md` **CI-4** (*Appointment, competency, rotation, and removal*), **CI-5** (*Conflict integrity, anti-capture, and anti-corruption*), and `core_11-11_forum.md` **Chapter Eleven**.

Parties and materially affected sentients must have a meaningful opportunity, consistent with lawful restrictions, to challenge:
- the scope of the assignment;
- the support actor's qualifications, independence, conflicts, or methods;
- material assumptions, omitted evidence, uncertainty statements, and conclusions;
- any restriction that prevents a fair chance to understand or answer the support record.

Exculpatory, mitigating, inculpatory, and impeachment evidence must be preserved under the same good-faith standard. A support process is defective if it helps one side develop technical facts while burying material evidence that would fairly assist another side or an affected sentient.

## CF-8.4 Evidence custody and method records
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: The trail a later reviewer needs: what was tested, how, by whom, what was uncertain, and where the gaps are.*

Forensic and analytical support must leave a record that later reviewers can follow. At minimum, proportionate to impact and sensitivity, the support record must include:
- chain-of-custody documentation;
- preservation steps and any known gaps;
- method logs showing what was tested, how it was tested, and by whom;
- uncertainty statements, assumptions, and limits;
- access, retention, segregation, and disclosure handling for restricted or sensitive material.

Evidence handling must satisfy Chapter Five [Evidence Preservation](../core_05_band_oversight.md#evidence-preservation). Access to restricted evidence must also satisfy **Chapter Five** (*Auditability*, *Verifiability*, *Transparency*), `core_02-03_definition_mechanics.md` **Chapters Two through Four** security-constrained observability requirements, `corpus_systems.md` restricted-data rules, and `core_06-06_rights_part_c.md` **Article XV-A** (*Auditability and Observable Evidence*) plus **Article XV** (*Audit, Transparency, and Independent Verification*)'s verification-access provisions.

## CF-8.5 Reports, explanations, and emergency preservation
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.

</details>

<br>

*In plain terms: Findings must be understandable to an ordinary affected sentient without dumbing down the technical substance. Acting without notice is allowed only when delay would destroy the evidence.*

Findings, reports, technical explanations, and preservation records must be reasoned, attributable, reviewable, and written or presented in a form an ordinary affected sentient can understand without losing necessary technical precision.

Emergency ex parte preservation steps may be permitted only when delay would foreseeably destroy, hide, alter, or materially corrupt evidence. Those steps must be narrowly scoped, promptly recorded, and made contestable after the immediate preservation need passes. Emergency preservation may secure evidence; it must not become an unreviewable merits shortcut.

## CF-8.6 Boundary with contest-integrity monitoring
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](../corpus_joint_structure/cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-0.1](../corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cjs-01-topic-router-stable-ids) topic router; [Chapter Eleven](../core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction) forum-family routing; [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline; and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Read with: **CF-8.6**; **CF-8**.

</details>

<br>

*In plain terms: Two related jobs kept separate: **CF-8** (*Forum forensic and analytical support*) builds the evidence record for one case; contest-integrity monitoring asks whether the system is working across many cases.*

Forum forensic support and contest-integrity monitoring are related but different.

`corpus_institutions.md` **CI-7.3** (*Contest-integrity monitoring (Class A and Class B)*) asks whether pathways, procedures, and institutions function in practice. **CF-8** support develops case-specific evidence records and analysis for adjudication. Institutions must not use forensic support to silently replace structural monitoring, and must not use contest-integrity monitoring to quietly decide case-specific facts that belong in the [forum case record](../core_05_band_accountability.md#forum-case-record).

---

**Previous file:** [cf_07_integrity_safeguards_anti_capture_anti_self_judging.md](cf_07_integrity_safeguards_anti_capture_anti_self_judging.md)

**Next file:** [cf_09_independent_investigative_service_prosecution_interface.md](cf_09_independent_investigative_service_prosecution_interface.md)