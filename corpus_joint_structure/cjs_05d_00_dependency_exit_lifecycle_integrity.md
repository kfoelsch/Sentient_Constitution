## Dependency, exit, and lifecycle integrity (CJS-5.16–CJS-5.18)
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-5.16–CJS-5.18: Dependency, exit, and lifecycle integrity**.
- Read with: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Dependency](../core_05-05_definitions_a_independent.md#dependency) · [O](../core_05-05_definitions_a_independent.md#dependency) · [E](../core_05-05_definitions_a_independent.md#dependency-e) · [C](../core_05-05_definitions_a_independent.md#dependency-c)
- [Transparency](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [O](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [E](../core_05-05_definitions_c_dependent_clusters.md#transparency-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#transparency-c)
- [Epistemic Integrity](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity) · [O](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity) · [E](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#epistemic-integrity-c)

</details>

<br>


This family collects the operational clusters that govern dependency mapping, meaningful exit, interoperability, portability, retention, and lifecycle review.

| Cluster | Section |
|---|---|
| **CJS-5.16** | Implementation and cross-implementation dependency integrity and disclosure terms |
| **CJS-5.17** | Implementation and cross-implementation interoperability, portability, and exit-integrity terms |
| **CJS-5.18** | Implementation and cross-implementation data-retention and lifecycle-integrity terms |

---

## CJS-5.16 Implementation and cross-implementation dependency integrity and disclosure terms
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-5.16 Implementation and cross-implementation dependency integrity and disclosure terms**.
- Read with: **CJS-5.16**; **CJS-5.15**; **CJS-5.17**; **CJS-5.9**; **CJS-5.23 and CJS-5.8**; **CI-11**.
- Topic routing (mandatory read-with): **CJS-R17** (*Cross-implementation trust integrity (joint operation model)*) in **CJS-2.1** (*Topic router (stable IDs)*); primary owner **CJS-4.3**.

- Read with: **CJS-5.16 — Dependency Awareness, Disclosure, and Risk Integrity**
- Read with: **CJS-5.15 — Transparency and Disclosure**
- Read with: **CJS-5.17 — Interoperability, Portability, and Exit Integrity**
- Read with: **CJS-5.9 — Auditability**
- Read with: **CJS-5.23** (*Implementation and cross-implementation structural review, correction urgency, and disclosure terms*) and **CJS-5.8** (*Implementation and cross-implementation integrity assurance and resilience operations*) — Evolution, Revalidation, and Non-Entrenchment
- Read with: `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**
- Read with: **Article XV-A**
</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Accountability](../core_05-05_definitions_b_semi_independent.md#accountability) · [O](../core_05-05_definitions_b_semi_independent.md#accountability) · [E](../core_05-05_definitions_b_semi_independent.md#accountability-e) · [C](../core_05-05_definitions_b_semi_independent.md#accountability-c)
- [Auditability](../core_05-05_definitions_c_dependent_clusters.md#auditability) · [O](../core_05-05_definitions_c_dependent_clusters.md#auditability) · [E](../core_05-05_definitions_c_dependent_clusters.md#auditability-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#auditability-c)
- [Transparency](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [O](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [E](../core_05-05_definitions_c_dependent_clusters.md#transparency-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#transparency-c)
- [Feasibility](../core_05-05_definitions_a_independent.md#feasibility) · [O](../core_05-05_definitions_a_independent.md#feasibility) · [E](../core_05-05_definitions_a_independent.md#feasibility-e) · [C](../core_05-05_definitions_a_independent.md#feasibility-c)
- [Dependency](../core_05-05_definitions_a_independent.md#dependency) · [O](../core_05-05_definitions_a_independent.md#dependency) · [E](../core_05-05_definitions_a_independent.md#dependency-e) · [C](../core_05-05_definitions_a_independent.md#dependency-c)
- [Governance](../core_05-05_definitions_b_semi_independent.md#governance) · [O](../core_05-05_definitions_b_semi_independent.md#governance) · [E](../core_05-05_definitions_b_semi_independent.md#governance-e) · [C](../core_05-05_definitions_b_semi_independent.md#governance-c)
- [Oversight](../core_05-05_definitions_a_independent.md#oversight-constitutional) · [O](../core_05-05_definitions_a_independent.md#oversight-constitutional) · [E](../core_05-05_definitions_a_independent.md#oversight-constitutional-e) · [C](../core_05-05_definitions_a_independent.md#oversight-constitutional-c)

</details>

<br>


Use this rule when dependency mapping, risk treatment, or accountability depends on standalone system behavior or combined system, dependency, or implementation-layer behavior.

Implementation and cross-implementation dependency integrity and disclosure terms
- OP-O: If a system relies on something important, that reliance must be named, explained, watched, and handled according to the risk it creates.
- OP-E: Reviewers must look at the full dependency picture, not isolated pieces that make the system look safer than it is.
- OP-C: A system is non-compliant if it claims its dependencies are under control while leaving out, contradicting, or ignoring an important dependency.

Care, respite, and support-dependency adequacy
- OP-O: Where a pathway, institution, or supervised system materially depends on unpaid care, paid care, respite, elder or disability support, substrate maintenance, or comparable dependency labor, the dependency map must treat that support as operational capacity rather than private background. It must identify substitution pathways, respite availability, crisis coverage, accessibility constraints, and whether carers or dependents can access relief without abandonment, retaliation, or unreasonable eligibility burden.
- OP-E: Evaluation must compare funding, staffing, scheduling, accessibility, household or platform dependence, market intermediaries, care-recipient safety, carer exploitation risk, and continuity of support together. Reviewers must verify that dependency concentration, reproductive or embodiment-related labor, and maintenance burdens are visible enough for governance, fiscal, labor, and service-routing decisions, while institutional program design remains with the applicable **CI** owner section.
- OP-C: A pathway is non-compliant if it claims continuity or access while hiding material care labor, making crisis support practically unavailable, treating reproductive or maintenance labor as an invisible default obligation, or using eligibility, payment, platform, household, or service-routing structures that predictably abandon carers or dependents without proportionate justification and usable remedy.

Criticality and impact classification
- OP-O: **Class A, Class B, and Class C** systems must classify dependencies that materially affect their core mission, constitutional function, operation, recovery, governance, or coordinated continuity. Classification must state reliance degree, substitutability, switching cost, exit feasibility, cascade risk, and affected parties or systems.
- OP-E: Reviewers must verify that dependency classification aligns with `corpus_systems.md` dependency classes and is useful for real decisions, including mitigation, audit, oversight, purchasing, participation, and exit planning.
- OP-C: **Class A, Class B, and Class C** mission-impacting dependencies must be clearly identified, monitored, audited, and periodically reviewed. Dependencies that are critical to safety, rights, access, continuity, or systemic stability may not be left unclassified or treated as ordinary vendor or interface choices.

Dependency identification and disclosure content
- OP-O: Systems must keep current records of what they depend on and what depends on them, including suppliers, data sources, software, infrastructure, institutions, contracts, interfaces, and handoff points.
- OP-E: Reviewers must check technical dependencies, financial or market dependence, governance control, and whether the system can actually work with or move away from other systems.
- OP-C: Leaving out an important dependency, or letting dependency information go stale, is non-compliant.

Domain and sector classification mapping
- OP-O: Where an implementation authority regulates, supervises, charters, funds, or materially relies on major domains or sectors, it must map those domains against applicable `corpus_systems.md` **CS-4 — System classification and handling** classes and **CS-5 — Critical system stewardship** stewardship tiers using the canonical domain taxonomy where one applies. The map must identify domains present in governed scope, split classifications or tiers, survival-relevant, operationally critical, or coordination-critical domains, and reclassification triggers when dependency criticality, cascade risk, or historical treatment changes.
- OP-E: Reviewers must verify that domain maps cover material sectors such as food, extractive, built-environment, energy, transport, manufacturing, health, communications, finance, insurance, education, and knowledge infrastructure where present, and that the map supports proportional burden, audit, oversight, purchasing, participation, and exit planning rather than serving as a static label.
- OP-C: Domain mapping is non-compliant if unlabeled, ad hoc, obsolete, or selectively applied sector categories hide dependency criticality, evade classification-scaled burdens, obscure review, or impose inconsistent treatment on comparable activities without a documented proportional basis.

Hidden, indirect, and externalized risk controls
- OP-O: Systems may not hide important dependencies by placing them behind subcontractors, platforms, affiliates, delayed steps, automated handoffs, or other middle layers.
- OP-E: Reviewers must follow indirect dependencies when they can materially affect sentients, communities, institutions, the environment, or other systems.
- OP-C: A system is non-compliant if it pushes dependency risk onto others without clear disclosure, justification, mitigation, and where appropriate compensation or remedy pathways.

Monitoring cadence, map adequacy, and anti-evasion structure
- OP-O: Dependency maps must be updated when important facts change, and they must be detailed enough for audit, investigation, emergency response, and affected-party understanding.
- OP-E: Reviewers must check how often the map is refreshed, who can access it, and whether a qualified reviewer can understand and test it.
- OP-C: Stale disclosures, confusing structures, or deliberately manufactured dependencies used to dodge responsibility are non-compliant.

Proportional application
- OP-O: The more harm a dependency failure could cause, and the more sentients or systems rely on it, the stronger the mapping, disclosure, monitoring, and mitigation duties must be.
- OP-E: Reviewers must make sure simplified controls for lower-risk systems do not hide a real material exposure.
- OP-C: A simplified dependency process is non-compliant if important risks still exist but are not disclosed, monitored, or addressed.---

Resource and continuity dependency adequacy
- OP-O: When continuity, constitutional performance, or supervised operation depends on funding, staffing, compute, bandwidth, facilities, supplier capacity, reserve capacity, or comparable institutional resources, the dependency map must identify whether those resources are adequate, substitutable, and resilient under normal, degraded, and foreseeable stress conditions.
- OP-E: Reviewers must verify resource adequacy as part of the dependency chain, including whether allocation choices, incentive designs, or short-term optics materially weaken safe continuity, recovery, or constitutional performance. Institutional sanctions, malus, clawback, or dissolution consequences remain with the applicable **CI** owner sections.
- OP-C: Treating a resource, funding, staffing, or capacity dependency as outside continuity review is non-compliant where that dependency materially affects rights, safety, access, institutional duties, supervised scope, or recovery from control failure.

Substitutability, exit constraints, and mitigation duties
- OP-O: For important dependencies, disclosures must explain the practical alternatives, the cost and risk of switching, what transition would require, and any limits on exit, repair, portability, or interoperability.
- OP-E: Reviewers must check whether the system has a realistic mitigation plan, or a documented reason why mitigation is not feasible.
- OP-C: Hidden lock-in, hidden switching costs, or unaddressed exit barriers are non-compliant unless a lawful and proportionate justification is documented.



## CJS-5.17 Implementation and cross-implementation interoperability, portability, and exit-integrity terms
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-5.17 Implementation and cross-implementation interoperability, portability, and exit-integrity terms**.
- Read with: **CJS-5.17**; **CJS-5.16**; **CJS-5.15**; **CI-12.3**.
- Topic routing (mandatory read-with): **CJS-R17** (*Cross-implementation trust integrity (joint operation model)*) in **CJS-2.1** (*Topic router (stable IDs)*); primary owner **CJS-4.3**.

- Read with: **CJS-5.17 — Interoperability, Portability, and Exit Integrity**
- Read with: **CJS-5.16 — Dependency Awareness, Disclosure, and Risk Integrity**
- Read with: **CJS-5.15 — Transparency and Disclosure**
- Read with: `corpus_systems.md` **CS-3 — Information types and handling**
- Read with: `corpus_systems.md` **CS-4 — System classification and handling**
- Read with: `corpus_systems.md` **CS-5 — Critical system stewardship**
- Read with: **Article XIX**
- Read with: **Article XV-A**
</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Proportionality](../core_05-05_definitions_a_independent.md#proportionality) · [O](../core_05-05_definitions_a_independent.md#proportionality) · [E](../core_05-05_definitions_a_independent.md#proportionality-e) · [C](../core_05-05_definitions_a_independent.md#proportionality-c)
- [Auditability](../core_05-05_definitions_c_dependent_clusters.md#auditability) · [O](../core_05-05_definitions_c_dependent_clusters.md#auditability) · [E](../core_05-05_definitions_c_dependent_clusters.md#auditability-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#auditability-c)
- [Transparency](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [O](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [E](../core_05-05_definitions_c_dependent_clusters.md#transparency-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#transparency-c)
- [Feasibility](../core_05-05_definitions_a_independent.md#feasibility) · [O](../core_05-05_definitions_a_independent.md#feasibility) · [E](../core_05-05_definitions_a_independent.md#feasibility-e) · [C](../core_05-05_definitions_a_independent.md#feasibility-c)
- [Dependency](../core_05-05_definitions_a_independent.md#dependency) · [O](../core_05-05_definitions_a_independent.md#dependency) · [E](../core_05-05_definitions_a_independent.md#dependency-e) · [C](../core_05-05_definitions_a_independent.md#dependency-c)
- [Necessity](../core_05-05_definitions_a_independent.md#necessity) · [O](../core_05-05_definitions_a_independent.md#necessity) · [E](../core_05-05_definitions_a_independent.md#necessity-e) · [C](../core_05-05_definitions_a_independent.md#necessity-c)
- [Material](../core_05-05_definitions_b_semi_independent.md#material) · [O](../core_05-05_definitions_b_semi_independent.md#material) · [E](../core_05-05_definitions_b_semi_independent.md#material-e) · [C](../core_05-05_definitions_b_semi_independent.md#material-c)

</details>

<br>


Use this rule when lock-in, migration, interface design, or dependency exposure depends on standalone system behavior or combined system, dependency, or implementation-layer behavior.

Implementation and cross-implementation interoperability, portability, and exit-integrity terms
- OP-O: Systems must preserve meaningful exit, usable portability, and fair interoperability.
- OP-E: Evaluation must assess all relevant system components, dependencies, institutional roles, and implementation-layer interactions together.
- OP-C: It is non-compliant to claim exit integrity when a material component has not been fully evaluated or remains unmet in practice.

Access-preserving reward and anti-warehousing controls
- OP-O: Where multiple reward mechanisms are feasible, implementation should prefer the least restrictive mechanism that can sustain future innovation, including attribution, milestone prizes, public or cooperative buyouts, levy-funded reward pools, pooled or standardized licensing, compulsory-access tools, or equivalent public-access regimes before broad exclusion rights for high-dependency domains.
- OP-E: Evaluation must verify whether compulsory license, access order, buyout, sunset acceleration, interface condition, interoperability condition, reward conversion, or equivalent corrective path is available where a claim is materially necessary for survival-relevant systems, standards-setting interfaces, public-interest implementation, or high-dependency transition and continuity.
- OP-C: It is non-compliant to warehouse, withhold, shelf, overbundle, or strategically maintain an innovation claim in a way that produces artificial scarcity, coercive lock-in, suppressed implementation, repair obstruction, migration obstruction, or public-interest access failure without proportionate justification.

Commitment, renewal, and charge-exit integrity
- OP-O: Paid commitments, renewals, trial-to-paid conversions, recurring charges, subscriptions, memberships, paid tiers, and transaction-linked charges must rest on affirmative, informed commitment where material, must disclose amount, timing, renewal, bundled entitlements, and exit consequences before commitment, and must honor a valid cancellation, downgrade, or withdrawal instruction through the published pathway.
- OP-E: Evaluation must compare commitment, renewal, billing, downgrade, cancellation, partial-exit, and evidence-of-release records together, including notice timing and content, default settings, preselected options, component bundling, notice-period disclosures, cutoff rules, post-cancel charges, accessibility parity, and whether stricter governing-law requirements have been met where they apply.
- OP-C: A charge pathway is non-compliant if it relies on obscured defaults, preselected paid options, trial conversion without informed commitment, renewal notice that hides amount or timing, continued charges after valid exit except for a previously disclosed lawful notice period, bundled structures whose primary effect is to block proportionate exit, or post-cancel billing cycles that make users monitor for charges after the operator has accepted exit.

Continuity-preserving transition safeguards
- OP-O: Exit and migration should preserve identity, participation, and recoverable state where feasible.
- OP-E: Evaluation must verify safe transition paths, rollback or recovery options, and advance disclosure of unavoidable loss.
- OP-C: Forcing avoidable discontinuity is non-compliant.

Dependency-based coercion and reputation-lock pathway integrity
- OP-O: Where dependency, credential control, reputation scoring, platform visibility, housing, care access, workplace leverage, household control, or comparable chokepoints can materially defeat exit, reporting, remedy, or participation, the pathway must treat coercive-control patterns as practical routing facts even when no single transaction, contract label, or criminal category captures the whole pattern.
- OP-E: Evaluation must compare economic dependence, credential or account custody, data and reputation systems, visibility controls, retaliation risk, access to review, and practical alternatives together. Reviewers must verify that formal labels such as marriage, employment, tenancy, membership, contract, or platform account status do not hide dependency sabotage, isolation, reproductive pressure, reputation threats, or comparable coercive leverage that blocks meaningful exit or remedy.
- OP-C: A pathway is non-compliant if it recognizes only isolated incidents while ignoring a pattern that functionally blocks exit or challenge; requires a formal relationship label before dependency sabotage can be routed; lets reputation, scoring, or visibility tools trap dependent participants; or treats private association, conscience, household, or community context as a blanket reason to make coercive control illegible.

Digital self-service pathway integrity
- OP-O: User-facing digital self-service pathways through which parties start, manage, continue or renew, downgrade, transfer, or exit commitments or ongoing obligations must preserve meaningful entry, management, and exit within the same channel class where feasible. This includes enrollment, account or preference changes, upgrades and downgrades in obligation level, fee or billing management where charges apply, renewal or continuation handling, withdrawal, cancellation, and release from ongoing obligation.
- OP-E: Evaluation must compare entry, obligation-increasing, ongoing-management, renewal, downgrade, and exit paths together, including step count, elapsed time, cognitive burden, mediation mode, discoverability, label accuracy, accessibility parity, retention flows, operator-held artifacts, and evidence of obligation release or billing cessation where applicable.
- OP-C: A pathway is non-compliant if it substitutes choice architecture for informed consent; makes exit, downgrade, renewal control, or obligation management materially harder than entry without a narrow documented exception; requires telephone, postal mail, or in-person-only exit where comparable entry was self-service without a justified basis; hides exit behind unrelated tasks; mislabels continued obligations or charges; uses deceptive urgency, guilt, fear, or repetitive refusal cycles as the primary retention tactic; or denies substantive accessibility parity for exit and obligation management. Where recurring or transaction-linked charges apply, this rule is read with the **primary owner**'s billing-integrity requirements.

Exit-feasibility disclosure and dependency transparency
- OP-O: Systems must disclose dependencies affecting exit, including switching costs, migration risk, alternatives, substitutability, and downstream impact.
- OP-E: Evaluation must verify exit-relevant disclosures are complete, attributable, and auditable.
- OP-C: Hidden dependencies that materially impair exit are non-compliant.

High-vulnerability personal-service pathway integrity
- OP-O: Where an implementation scope governs lawful personal services with heightened vulnerability, bodily proximity, in-home or isolated work, care dependence, migration or language stressors, platform matching, payments, reputation, visibility, licensing, housing, or comparable dependency chokepoints, the pathway must preserve lawful access, practical exit, non-retaliatory reporting, proportionate due care, and anti-pretext separation between ordinary regulation and exploitation response. Comparable lawful personal services should use comparable regulatory families unless documented necessity and proportionality justify differentiation.
- OP-E: Evaluation must compare labor, safety, contract, consumer, platform, payment, licensing, housing, data, reputation, reporting, dispute, and transition pathways together. Reviewers must verify that heightened controls rest on documented risk rather than stigma, moral disapproval, stereotype, blanket exclusion, or functional prohibition through fines, zoning, licensing, platform visibility, payment denial, housing exclusion, or data practices; that fraud, coercion, consent defects, exploitation, harassment, privacy injury, and unfair terms remain enforceable through accessible routes; and that intermediaries or financial plumbing do not use generic risk categories to suppress lawful activity without proportionate justification.
- OP-C: A personal-service pathway is non-compliant if it makes lawful participation functionally unavailable through fines, fees, zoning, licensing, platform visibility, payment denial, housing exclusion, data practices, or reporting design whose primary practical effect is prohibition or harassment without a lawful risk predicate; if decriminalization or non-penal treatment is used to deprioritize exploitation response; or if transition rules preserve obsolete penalties, records, or training norms after the governing floor has changed.

Innovation reward boundary and anti-enclosure controls
- OP-O: Innovation rewards must preserve repair, maintenance, safety work, independent verification, research, education, archiving, benchmark and compatibility testing, reverse engineering for interoperability, migration, and meaningful exit where those uses are otherwise lawful and proportionate.
- OP-E: Evaluation must verify dependency-critical exclusivity is narrow, time-bounded, disclosed, continuity-protective, and tested against dependency growth, coordination power, switching costs, interoperability burden, and whether the claimed innovation functions as shared infrastructure.
- OP-C: Innovation claims, contract terms, platform rules, or technical controls that create coercive lock-in, hidden barriers, artificial scarcity, suppressed implementation, or indirect negation of lawful public-interest pathways are non-compliant.

Innovation-reward duration and reclassification controls
- OP-O: Copyright-like claims over expressive works should use publication-based timing rather than author-life timing, with `publish+30` years from first lawful publication or equivalent public release as the presumptive outer limit. Shorter terms, compulsory-license conversion, levy-funded reward, or immediate public-access treatment should apply where works are publicly funded, dependency-critical, educationally foundational, safety-relevant, standards-like, or function primarily as cultural memory, civic knowledge, or shared informational infrastructure.
- OP-E: Evaluation must test whether an innovation-reward claim has become dependency-critical after adoption, including when the claim becomes a platform, protocol, model, marketplace, payment rail, standards interface, or comparable coordination layer. Reviewers must verify whether claim scope, interface conditions, interoperability duties, access-order tools, reward conversion, or sunset timing still fit the current dependency and public-interest profile.
- OP-C: Continued exclusion is non-compliant where a stale duration rule, author-life proxy, unrevised claim class, or refusal to reclassify preserves coercive lock-in, blocks public-interest access, or defeats repair, education, research, compatibility, safety, migration, continuity, or shared-infrastructure functions without a current proportionate justification.

Interchange and open-interface baseline
- OP-O: Material-impact or material-dependency systems should use open, documented, interoperable formats and interfaces unless a narrower choice is lawfully justified.
- OP-E: Evaluation must verify interface controls do not defeat migration, substitution, or independent verification.
- OP-C: Closed or unstable interfaces used to create lock-in are non-compliant.

Lock-in and anti-coercion safeguards
- OP-O: Systems must not design coercive lock-in or exploit data, identity, or network effects to block exit.
- OP-E: Evaluation must verify mitigation where natural lock-in emerges.
- OP-C: Retaliating against exit through degraded service, penalties, or forfeiture is non-compliant.

Open data-format and protocol presumption
- OP-O: **Class A**, **Class B**, and **Class C** systems must use open, documented, stable, and standards-compatible data formats, schemas, APIs, and interchange protocols for material portability, audit, repair, continuity, and migration functions unless a narrower format or interface is strictly justified.
- OP-E: Evaluation must verify public or qualified-access specifications, versioning discipline, migration tooling, test vectors, conformance records, and a scrutinizable justification for any closed, proprietary, unstable, or non-standard format or protocol.
- OP-C: Closed, proprietary, degraded, unstable, or undocumented data formats or protocols are non-compliant where they materially impair exit, repair, independent verification, continuity, substitution, or cross-implementation operation, unless the restriction satisfies necessity, proportionality, least-restrictive-alternative, auditability, sunset, and revalidation requirements.

Portability quality and non-obstruction controls
- OP-O: Portability must be secure, usable, structured, and meaningful, including lawful identity, attribution, and continuity-critical state data.
- OP-E: Evaluation must verify schemas, documentation, context, and tooling for practical reuse.
- OP-C: Degrading, fragmenting, obscuring, or gating data to prevent reuse is non-compliant.

Proportional application
- OP-O: Interoperability, portability, and exit duties scale with impact, dependency, ecosystem integration, and lock-in irreversibility.
- OP-E: Evaluation must verify reduced rigor does not create hidden dependencies or external lock-in effects.
- OP-C: Simplified controls are non-compliant where material lock-in remains.---

Right-to-exit pathway integrity
- OP-O: Exit must be functionally available without violating Foundational Rights.
- OP-E: Evaluation must verify clear, time-bound, practical support for exit.
- OP-C: Nominal exit that is functionally blocked or coercive is non-compliant.


## CJS-5.18 Implementation and cross-implementation data-retention and lifecycle-integrity terms
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [CJS-1.2](cjs_01_scope_purpose_boundary_interface.md#cjs-12-shared-implementation-corpus-preamble-contract) shared implementation-corpus contract; [CJS-2.1](cjs_02_implementation_integration_map.md#cjs-21-topic-router-stable-ids) topic router; [Chapter Fifteen](../core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) incorporation discipline and [Chapter Five](../core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: this section's local operational requirements for **CJS-5.18 Implementation and cross-implementation data-retention and lifecycle-integrity terms**.
- Read with: **CJS-3.5**; **CJS-5.9**; **CJS-5.10**; **CJS-5.11**; **CJS-5.21 and CJS-5.18**; **CJS-5.23 and CJS-5.8**.
- Topic routing (mandatory read-with): **CJS-R17** (*Cross-implementation trust integrity (joint operation model)*) in **CJS-2.1** (*Topic router (stable IDs)*); primary owner **CJS-4.3**.

- Read with: **CJS-5.9 — Auditability**
- Read with: **CJS-5.10 — Tiered Transparency and Audit Access**
- Read with: **CJS-5.11 — Independent Verification and Integrity of Claims**
- Read with: **CJS-5.21** (*Implementation and cross-implementation reversibility and containment terms*) and **CJS-5.18** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*) — Reversibility and Containment
- Read with: **CJS-5.23** (*Implementation and cross-implementation structural review, correction urgency, and disclosure terms*) and **CJS-5.8** (*Implementation and cross-implementation integrity assurance and resilience operations*) — Evolution, Revalidation, and Non-Entrenchment
- Read with: `corpus_systems.md` **CS-3 — Information types and handling**, including Types **C**, **G**, **H**, **I**, **N**, and **S**
- Read with: **CJS-3.5 — Classification alignment for supervised scope**
</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Proportionality](../core_05-05_definitions_a_independent.md#proportionality) · [O](../core_05-05_definitions_a_independent.md#proportionality) · [E](../core_05-05_definitions_a_independent.md#proportionality-e) · [C](../core_05-05_definitions_a_independent.md#proportionality-c)
- [Accountability](../core_05-05_definitions_b_semi_independent.md#accountability) · [O](../core_05-05_definitions_b_semi_independent.md#accountability) · [E](../core_05-05_definitions_b_semi_independent.md#accountability-e) · [C](../core_05-05_definitions_b_semi_independent.md#accountability-c)
- [Reversibility](../core_05-05_definitions_a_independent.md#reversibility-constitutional) · [O](../core_05-05_definitions_a_independent.md#reversibility-constitutional) · [E](../core_05-05_definitions_a_independent.md#reversibility-constitutional-e) · [C](../core_05-05_definitions_a_independent.md#reversibility-constitutional-c)
- [Auditability](../core_05-05_definitions_c_dependent_clusters.md#auditability) · [O](../core_05-05_definitions_c_dependent_clusters.md#auditability) · [E](../core_05-05_definitions_c_dependent_clusters.md#auditability-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#auditability-c)
- [Transparency](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [O](../core_05-05_definitions_c_dependent_clusters.md#transparency) · [E](../core_05-05_definitions_c_dependent_clusters.md#transparency-e) · [C](../core_05-05_definitions_c_dependent_clusters.md#transparency-c)
- [Stakeholder](../core_05-05_definitions_b_semi_independent.md#stakeholder) · [O](../core_05-05_definitions_b_semi_independent.md#stakeholder) · [E](../core_05-05_definitions_b_semi_independent.md#stakeholder-e) · [C](../core_05-05_definitions_b_semi_independent.md#stakeholder-c)
- [Dependency](../core_05-05_definitions_a_independent.md#dependency) · [O](../core_05-05_definitions_a_independent.md#dependency) · [E](../core_05-05_definitions_a_independent.md#dependency-e) · [C](../core_05-05_definitions_a_independent.md#dependency-c)

</details>

<br>


Use this rule when accountability, privacy, reversibility, or classification depends on how data is kept, changed, linked, or deleted within a standalone system, institution, forum, or bounded decision domain, or across more than one system or implementation layer.

Implementation and cross-implementation data-retention and lifecycle-integrity terms
- OP-O: Data-retention compliance must be evaluated as one lifecycle claim across collection, use, retention, transformation, disclosure, deletion, de-identification, and reclassification.
- OP-E: Reviewers must assess purpose, S1 data type or types, duration, detail, access, deletion or de-identification, reclassification, disclosure, and audit needs together.
- OP-C: A retention-integrity claim is non-compliant if those lifecycle elements cannot be reviewed together, if an important element has not been fully evaluated or is unusable, or if one element defeats another.

Accountability-preserving record floor
- OP-O: Where required, retention must keep enough Type **C**, **G**, **H**, **I**, or **S** records to reconstruct material events, audit conduct, verify claims, support challenge and redress, preserve continuity, and recover from failure.
- OP-E: Reviewers must verify that data minimization does not block investigations or hide responsibility.
- OP-C: Invoking minimization to defeat accountability is non-compliant.

Anti-surveillance and anti-coercion accumulation limits
- OP-O: Retention must not become hidden surveillance, coercive leverage, or a way to reconstruct protected internal states beyond the justified scope, especially through Type **H**, **I**, or **N** data.
- OP-E: Reviewers must verify that behavioral, relational, identity-linked, or internal-state-adjacent data is not being accumulated secretly or out of proportion to the stated purpose.
- OP-C: A retention design that enables coercion, concealed surveillance, or meaningful barriers to exit or contestation is non-compliant.

Classification and information-type alignment
- OP-O: If accumulated, linked, or inferred data changes its **CS-3 — Information types and handling** data type or becomes more sensitive in practice, stricter protections apply.
- OP-E: Reviewers must verify alignment with **CS-3 — Information types and handling** data-type duties and **CJS-3.5 — Classification alignment for supervised scope** where supervision and systems classification overlap.
- OP-C: Continuing to use lower-type or lower-class handling after sensitivity has increased is non-compliant.

Justification and bounded-retention floor
- OP-O: Retention must remain justified over time. When the justification ends, the data must be reduced, deleted, de-identified, or otherwise removed from use.
- OP-E: Reviewers must verify that the amount of data kept, and the time it is kept for, fit the S1 data type or types, purpose, legal obligations, impact, rights, safety, and accountability needs.
- OP-C: Keeping data because it might be useful later, is convenient to keep, or gives an institution leverage is non-compliant.

Lifecycle expiry, deletion, de-identification, and reclassification controls
- OP-O: Temporary data must not quietly become a permanent archive.
- OP-E: Reviewers must verify deletion where feasible. If deletion is not feasible, they must verify irreversible de-identification or aggregation. Reclassification across S1 data types requires a new documented and time-limited justification.
- OP-C: Keeping data indefinitely without a continuing reason and working lifecycle controls is non-compliant.

Proportional application
- OP-O: Retention controls scale with S1 data type or types, impact, dependency, sensitivity, reconstructability, duration, scope, and governance role.
- OP-E: Reviewers must verify that simplified controls do not create surveillance, coercion, blocked investigations, or rights harm.
- OP-C: Reduced safeguards are non-compliant where material exposure remains.

Purpose and proportionality criteria
- OP-O: Data may be kept only for warranted purposes, such as integrity, continuity, safety, dispute resolution, restoration, or accountability.
- OP-E: Reviewers must verify that retention scales with S1 data type or types, impact, dependency, sensitivity, audit needs, and the need to challenge or correct a decision.
- OP-C: Keeping more detail, identity linkage, or history than the purpose requires is non-compliant.

Review, revalidation, and prohibited patterns
- OP-O: Retention rules must be revalidated on a set schedule and updated when material conditions change.
- OP-E: Reviewers must screen for indefinite retention, use beyond the original purpose or S1 data type or types, unnecessary detail, complexity that hides consequences, evasive deletion, shadow stores, and designs that block audit.
- OP-C: Stale, unreviewed, or evasive retention regimes are non-compliant.

Transition continuity and authority-transfer lifecycle integrity
- OP-O: Material redesign, consolidation, dissolution, migration, or authority transfer must preserve continuity for rights, services, records, active challenge pathways, and accountable governance while the transition is underway.
- OP-E: Reviewers must verify authority custody, review authority, evidence custody, interim scope, sunset and reauthorization records, unresolved-risk explanations, rollback or recovery options, and whether the transition prevents governance vacuum, unmanaged authority transfer, or anti-constitutional lock-in.
- OP-C: A transition lifecycle is non-compliant if interim authority becomes indefinite without recorded reauthorization, if evidence or challenge pathways are lost during transfer, if unresolved risks are concealed, or if redesign creates a governance gap that makes rights, services, records, or remedies unusable in practice.

Transparency disclosures and stakeholder legibility
- OP-O: Systems must disclose retention details in proportion to impact. The disclosure must identify the applicable S1 data type or types and what categories of data are kept. It must also state why data is kept, how long it is kept or how that period is chosen, when lifecycle changes occur, and what secondary uses are allowed.
- OP-E: Reviewers must verify that disclosures are clear enough for stakeholders to understand the practical consequences.
- OP-C: Incomplete, obscure, or misleading retention disclosures are non-compliant.



---

**Previous file:** [cjs_05c_00_participation_comprehension_disclosure.md](cjs_05c_00_participation_comprehension_disclosure.md)

**Next file:** [cjs_05e_00_failure_robustness_intervention_correction.md](cjs_05e_00_failure_robustness_intervention_correction.md)
