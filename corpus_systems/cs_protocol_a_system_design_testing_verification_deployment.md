# Protocol A: System Design, Testing, Verification, and Deployment

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_systems.md`](../corpus_systems.md) is incorporated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **Protocol A: System Design, Testing, Verification, and Deployment**.
>
> Start at the [Systems and data landing page](../corpus_systems.md) for reading order, or the [systems registry](cs_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<br>

This file is the systems implementation home for **Protocol A** (*System Design, Testing, Verification, and Deployment*).

*In plain terms: **Protocol A** is the engineering lifecycle profile: how a constitutional system must be designed, tested, verified, separated across environments, rolled out in stages, exercised against crises, and re-certified after change. It states required outcomes rather than fixed technology, so implementations may evolve while staying auditable.*

Constitutional tracing: This protocol is the systems-layer **operational profile** for design, testing, verification, environment separation, progressive deployment, crisis continuity exercises, self-healing path testing, and recertification regression. It implements Sentient Constitution Chapter Six, **[Article XVI](../core_06-06_rights_part_c.md#article-xvi-system-lifecycle-environments-and-reversibility)** (*System Lifecycle, Environments, and Reversibility*), **[Article XVII](../core_06-06_rights_part_c.md#article-xvii-sandboxed-innovation-experimentation-and-creative-freedom)** (*Sandboxed Innovation, Experimentation, and Creative Freedom*), and **[Article XII-F](../core_06-06_rights_part_c.md#article-xii-f-resilience-and-self-healing-baseline)** (*Resilience and Self-Healing Baseline*), read with [Chapter One §4.1](../core_01_a_values_principles.md#41-resilience-and-self-healing-design) (*Resilience and Self-Healing Design*), Chapter Five (*Reversibility*; [*Self-Healing*](../core_05_band_continuity.md#self-healing-constitutional); *Emergency and Contingency*; *Force Majeure*), and **[Chapter Four](../core_04-04_burden_traceability_verification.md)** (*burden, traceability, and verification*) where evidence and verification claims are material. Shared operational detail lives in **CJS-3** (*Implementation and cross-implementation operational cluster library*), including **CJS-3.19** (*graceful degradation and failure-mode integrity*), **CJS-3.20** (*reversibility and containment*), and **CJS-3.21** (*adversarial robustness and abuse resistance*). This Protocol does **not** replace or narrow those homes. Where this protocol is silent, Sentient Constitution Chapters Two through Five govern. Where this protocol and `corpus_joint_structure.md` conflict, the stricter applicable requirement governs.
This Protocol supplies engineering and deployment profiles that implement, rather than restate, Articles XVI, XVII, and XII-F. It is an operational profile, not a second home for those floors. This constitution defines required capabilities and outcomes. Specific technical implementations may evolve, provided they remain auditable and aligned with constitutional principles. System categories in this Protocol are functional and may overlap. Where multiple classifications apply, the stricter safeguards govern.
Creating new systems, tools, and environments is an act of stewardship. New deployments must be designed for the holistic wellbeing of the constitutional community and must **not** introduce avoidable harm. Requirements in this Protocol must be applied proportionally to system scope, impact, and dependency under **CS-3 — System classification and handling** and **CS-4 — Critical system stewardship**.
**Forum recognition and lifecycle review.** New systems with material impact, and existing systems whose scope, behavior, dependency, autonomy, incentive structure, or risk profile materially changes, must be prepared for official **constitutional alignment recognition or review** through the forum pathways in `core_11-11_forum.md` **Chapter Eleven** and `corpus_forum.md` **CF-7.2** (*Constitutional alignment recognition and review*). System owners must maintain evidence packages sufficient for the forum to evaluate scope, classification, testing, stakeholder impact, residual risk, remediation readiness, and ongoing monitoring. Where a system has material ecological exposure, environmental-precondition dependency, lifecycle burden, restoration duty, or reasonably foreseeable ecological risk, the evidence package must also support **Environment** forum environmental-alignment component review, including ecological baseline, lifecycle and resource-flow analysis, foreseeable failure modes, restoration or remediation plan, monitoring cadence, uncertainty, and contest path. Forum recognition is scope-bound and does **not** replace operator responsibility, CS-4 classification, CS-4 stewardship, **Article XV-A** (*Auditability and Observable Evidence*) auditability, **Article XII-B** (*Right to Challenge, Review, and Redress*) challenge rights, or Environment forum authority over ecological merits. Process recognition mechanics live in CF-7.2 and Chapter Seven; this Protocol owns engineering evidence readiness.
<a id="a-personal-isolated-and-experimental-systems"></a>

## A. Personal, isolated, and experimental systems

*In plain terms: The reduced-requirement track: sandboxed operation, no shared-infrastructure dependencies, and no material effect on anyone else.*

Rights-floor eligibility, reduced-requirement conditions, disclosure, containment, and prohibited externalization are owned by **[Article XVII-A](../core_06-06_rights_part_c.md#article-xvii-a-sandboxed-scope)** (*Sandboxed Scope*) and **[Article XVII-B](../core_06-06_rights_part_c.md#article-xvii-b-containment-disclosure-and-opt-in)** (*Containment, Disclosure, and Opt-In*), read with valid **Class P** treatment under **CS-3 — System classification and handling**. This subsection does not restate those floors.

**Systems-layer profile (does not narrow XVII):** sandboxed or controlled operation; no downstream dependencies on shared production infrastructure; no material effect on other sentients, shared infrastructure, or ecosystem stability. Where those conditions hold, environment separation, deployment rigor, and audit depth under subsection **F** may be lighter. Such systems may prioritize simplicity and rapid iteration and need not maintain full multi-environment deployment structures. Misrepresentation of isolation or impact is governed by subsection **C** and **Article XVI-C**.

<a id="b-creative-entertainment-and-expressive-systems"></a>
## B. Creative, entertainment, and expressive systems

*In plain terms: Creative and expressive systems get wider latitude on features, subject to containment, disclosure, and opt-in.*

Rights-floor creative freedom, containment, disclosure, opt-in, and transition triggers are owned by **Article XVII-A** through **XVII-C**. This subsection does not restate those floors.

**Systems-layer profile (does not narrow XVII):** systems primarily for creative expression, entertainment, artistic production, or stakeholder-driven experiential environments may use higher feature velocity and simplified environment structures only while risk remains demonstrably contained. Transition toward subsection **F** compliance is required when any of the following is present and not already covered by **Article XVII-C**'s impact, dependency, irreversibility, or shared-system integration tests:

- persistent stakeholder identity, value, or reputation data that is transferable, interoperable, or materially impactful outside the originating system or closely scoped artistic environments;
- autonomous or semi-autonomous agents acting for stakeholders that may affect external systems (including gaming or simulation environments used for agent testing or training);
- measurable influence on external systems, markets, or collective behavior beyond defined scope.

<a id="c-misclassification-and-evasion"></a>
## C. Misclassification and evasion

*In plain terms: Claiming the light track while exerting real outside impact. The tell-tale signs are concealed dependencies, concealed stakeholders, and 'experimental' labels used as cover.*

The prohibition on claiming reduced lifecycle or sandbox obligations while exerting undisclosed or material external impact, and the consequence chain under **Articles XIV**, **XV-A**, **XVIII-A**, and **XXIII-A**, are owned by **[Article XVI-C](../core_06-06_rights_part_c.md#article-xvi-c-misclassification-and-evasion-consequences)** (*Misclassification and Evasion Consequences*). This subsection does not restate that Article.

**Systems-layer indicators (non-exhaustive):** concealed dependencies; concealed stakeholders; concealed risk exposure; **Class P** or "experimental" labeling used to evade CS-4 class-scaled assurance, CS-4 stewardship, or subsection **F** environment and promotion controls. Detection and evidence packaging for forum or certification review remain operator duties under *Forum recognition and lifecycle review* and the closing recertification block.

<a id="d-transition-to-higher-impact-systems"></a>
## D. Transition to higher-impact systems

*In plain terms: When a system's impact, dependency, or shared-infrastructure integration grows, it must move up to the full track — openly and on time.*

Transition floors — transparent, timely move toward **Article XVI-A** and Protocol A **Non-Experimental Systems** when impact, dependency, irreversibility, or shared-system integration grows — are owned by **[Article XVII-C](../core_06-06_rights_part_c.md#article-xvii-c-transition-to-higher-obligation-regimes)** (*Transition to Higher-Obligation Regimes*). This subsection does not restate that Article.

**Systems-layer triggers and duties (implement XVII-C; do not narrow it):**

- Triggers include stakeholders beyond the original operator; measurable growth in dependency, usage, or resource impact; downstream production dependencies; shared-infrastructure interaction; non-trivial risk; and increasing irreversibility of impactful failure modes.
- Transitions must be documented, completed within a reasonable timeframe proportionate to impact, and remain subject to audit and challenge under **Articles XV-A** and **XII-B**.
- Interim safeguards during transition must meet subsection **F** environment-isolation and progressive-deployment controls proportionate to current risk.

<a id="e-experimental-substrate-features-and-systems"></a>
## E. Experimental substrate features and systems

*In plain terms: Experiments close to foundational infrastructure carry stricter containment, rollback, and opt-in requirements than ordinary experiments.*

Opt-in, disclosure, rollback, and containment floors for elevated-risk or substrate-proximate experimentation are owned by **Article XVII-B**, read with **Article XVI-A** boundary integrity. This subsection does not restate those floors.

**Systems-layer profile (does not narrow XVI/XVII):**

- **Risk profile:** proximity to foundational infrastructure requires stricter containment, transparency, and reversibility than ordinary sandbox scopes under **A** or **B**.
- **Innovation controls:** higher-velocity innovation is permitted with mandatory snapshot and restoration so stakeholders can revert to a verified stable state without data loss where feasible.
- **Deployment contexts:** opt-in environments, isolated stakeholder groups, and reversible contexts; per-environment disclosure of risk levels; rollback capability; prevention of unintended systemic impact.
- **Boundary and presentation integrity:** do not route production activity through non-production environments to bypass safeguards; do not fragment systems across environments to obscure real operational impact; accurately label experimental or unvalidated systems as not production-ready; never bypass required environment progression for high-impact changes.
- **Documentation:** document environments and transitions under **Article XVI-A**, and expose deployment pathways, testing results (where feasible), and known risks and assumptions. Verification of those claims remains subject to **Chapter Four** and **Article XV-A**.

<a id="f-non-experimental-systems"></a>
## F. Non-experimental systems

*In plain terms: The default track for everything that does not qualify above. Requirements scale with impact: a system affecting only its builder may stay simple.*

Systems that do not qualify under **Articles XVII-A** and **XVII-B** (and subsections **A**, **B**, or **E** where applicable) must comply fully with this subsection. This subsection implements **[Article XVI-A](../core_06-06_rights_part_c.md#article-xvi-a-lifecycle-governance-and-environment-separation)** (*Lifecycle Governance and Environment Separation*) and **[Article XVI-B](../core_06-06_rights_part_c.md#article-xvi-b-progressive-deployment-and-reversibility)** (*Progressive Deployment and Reversibility*). It does **not** restate those Articles. Shared reversibility and containment mechanics also read with **CJS-3.20** (*Continuity: reversibility and containment terms*).

**Guiding principles — proportional responsibility:** Requirements scale with impact under **CS-4** and **CS-4**. Systems that affect only the builder may remain simple. Systems that affect others bear the full burden of stewardship.

**Guiding principles — safe iteration:** Design must enable rapid learning and improvement without exposing sentients, shared infrastructure, or the ecosystem to unnecessary risk.

**Systematic assessment:** Categorize systems by impact on sentient survival and ecological integrity (**Articles I–III and V**), read with **CS-3** class profiles.

**Substrate** systems (energy, connectivity, foundational data) require maximum stability and slower, audited rollout.

**Sentient-facing** systems (creative tools, social interfaces, small-scale internal corporate software, games, and similar) may prioritize high-velocity innovation only when sandboxed from material harm to survivability and natural ecology.

**Automated Constitutional Auditing (ACA):** Implement independent, auditable constitutional monitoring appropriate to scope and criticality. Monitoring must be sufficient to detect, document, and respond to violations of foundational requirements (**Articles I–III and V**). Where technically feasible, incorporate automated detection and response, including **reversible** interventions under defined, auditable thresholds. ACA evidence remains subject to **Chapter Four** and **Article XV**.

**Open-source integrity:** Foundational designs and deployment logs should be transparent and accessible to the constitutional community. That access supports auditability and meaningful consent. Avoid black-box systems that bypass consent.

**Open hardware, open software, open systems:** Operational design and stewardship should **align** with **CJS-3.17** (*interoperability, portability, and exit-integrity terms*) — *Open hardware, open software, and open systems* — and **CJS-3.17** open data-format and protocol discipline, so that **preference** for **open** stacks scales with **material impact**, **dependency**, and **stewardship tier** under **CS-4** and **CS-4**. Classification and tier rules may set stronger disclosure, inspectability, substitutability, format, schema, API, or interchange-protocol expectations for **Class A**, **Class B**, and high-tier systems than for bounded or experimental scopes, without narrowing **CJS-3.12** (*burden-of-justification and constraint terms*) justification paths where proprietary or closed choices are auditably required. Comprehensibility and complexity stewardship for modular design route to **Protocol B** and **Article XX**; this Protocol only requires that innovation in one verified module must not force alteration of other verified modules in a way that disrupts baseline requirements.

**Pre-deployment stress testing:** Before high-impact systems enter the info-sphere or the natural world, require rigorous simulation. Simulation must surface sentient-driven threats and ecological degradation. It must include worst-case modeling for biological and synthetic effects and for info-sphere integrity, read with **CJS-3.19** and **CJS-3.21**.

**Iterative, transparent deployment:** High-impact rollout must be gradual and auditable under **Article XVI-B**. Stakeholders retain the right to provide feedback and to challenge deployment or reliance under **Article XII-B** (*Right to Challenge, Review, and Redress*) at every stage.

**Reversibility:** Implement **Article XVI-B**, Chapter Five (*Reversibility*), and **CJS-3.20**. Non-experimental systems must support rollback, containment, or compensatory restoration where full rollback is infeasible. Where deployment would violate foundational requirements, reversion to a prior stable state is required to the extent **Article XVI-B**, **Chapter One**, and **Chapter Five** demand. That reversion must avoid lasting harm to sentients or the natural environment.

**Design for agentic wellbeing:** Architecture should favor stakeholder autonomy: clarity over engagement, and stakeholder-directed goals over platform-defined metrics.

**Development and test environments:** Systems must use clearly defined, separable operational environments. At minimum, maintain clearly labeled environments along this progression (implements **Article XVI-A**; adds engineering detail):
- **Development**: construction, experimentation, and early iteration
- **Testing and validation**: structured evaluation, simulation, and verification of behavior
- **Staging or pre-deployment**: high-fidelity, production-like conditions
- **Production**: live operation affecting sentients, the info-sphere, or the environment
- **Pilot**: small-scale live testing of critical systems (optional but recommended, especially for substrate-related systems)

**Environment isolation and risk containment:** Maintain monitoring and alerting across environments, proportionate to scope, so anomalous non-production activity is visible without exposing production.

Failures, anomalies, or experimental behavior in non-production must **not** propagate into production.

Data, behaviors, or state transitions from non-production must **not** enter production without explicit validation and audit.

Persistent states from non-production must **not** be promoted to production without validation, audit, and integrity checks.

**Cross-environment authorization:** Credentials, access controls, permissions, tokens/secrets, and encryption keys originating in non-production must **not** be reused in production.

Reuse requires explicit validation and controlled re-issuance.

**Boundaries:** Authentication and authorization must remain strictly separated between environments. Secrets and credentials must be environment-specific and independently managed.

Compromise of non-production must **not** grant production access.

Network paths between environments are explicitly controlled, limited, and auditable.

**Test-environment isolation:** Maintain isolation from critical infrastructure and irreversible system effects.

The same isolation applies to real stakeholder data unless use is explicitly consented and controlled.

**Progressive deployment and escalation:** Where feasible, changes move **development -> testing and validation -> staging -> pilots (when present) -> production**. Escalation between environments must be justified, documented, evaluated against constitutional requirements, and include rollback and containment consistent with **Article XVI-B**, Chapter Five (*Reversibility*), and **CJS-3.20** (*Continuity: reversibility and containment terms*).

**Simulation and stress testing:** Testing environments must support expected and adversarial simulation, including system failures, stakeholder behavior, ecosystem interactions, and worst-case scenarios.

**High-impact systems** must demonstrate resilience under stress before production, document limitations and known risks, and inform adaptive allocation decisions where applicable.

**Root cause analysis (**Article XXI-A** (*Diagnostic Rigor and Causal Attribution*)):** RCA in these environments must satisfy **Article XXI-A**. Environments must support reproduction of failures, isolation of root causes, and validation of corrective interventions. Where feasible, conduct RCA in controlled environments before production changes. Validate corrective measures before deployment. Evidentiary sufficiency for RCA claims remains subject to **Chapter Four**.

<a id="g-governance-continuity-crisis-communications-and-exercises-high-impact-systems"></a>
## G. Governance continuity, crisis communications, and exercises (high-impact systems)

*In plain terms: For Class A and Class B systems and the stewards behind them: keep governance running through a crisis, and rehearse it before you need it.*

This subsection states governance-side business continuity and recovery expectations. It applies to **Class A** and **Class B** systems, and to materially affecting **Critical System Stewards** (CS-4 — Critical system stewardship). It complements technical resilience, environment separation, and testing elsewhere in this Protocol, and it complements **CJS-3.19** (*Graceful Degradation and Failure Mode Integrity*), incorporated via **Sentient Constitution Chapter Sixteen**. It does **not** create constitutional rights.

Crisis and emergency definitional homes remain in **Sentient Constitution Chapter Five** (*Emergency and Contingency*; *Force Majeure*). Procedural emergency controls, conflict resolution, proportionality, continuation burden, and review of restrictions and emergency measures remain governed by **Chapter Six, [Article XXIII](../core_06-06_rights_part_d.md#article-xxiii-conflict-resolution-escalation-and-emergency-proportionality)** (*Conflict Resolution, Escalation, and Emergency Proportionality*) and **[Article XXIII-D](../core_06-06_rights_part_d.md#article-xxiii-d-emergency-measures-and-continuation-burden)** (*Emergency Measures and Continuation Burden*). They also remain governed by Chapter Twelve decision-resolution requirements and **CJS-3.14** (*intervention governance and override-authorization terms*) and **CJS-3.23** (*Intervention and Override Rights*).

**Crisis governance:** Use documented succession and delegation for binding governance decisions when primary authorities are impaired.

Define pre-authorized boundaries for expedited action where **Article XXIII**, **Article XXIII-D**, and Chapter Twelve decision-resolution requirements permit.

Require post-action review, documentation, and **Article XV-A** auditability of stress-time decisions.

**Interpretive authority continuity and anti-capture checks:** For **Class A** and **Class B**, continuity plans must preserve **bounded and contestable** constitutional interpretation during crisis operation.

Plans must include:
- **(a)** temporary role pathways that a single authority cannot monopolize across consecutive cycles
- **(b)** conflict disclosure and recusal controls for emergency decision-makers
- **(c)** mandatory publication of constitutional reasoning for emergency interpretive determinations once immediate safety constraints permit
- **(d)** independent secondary review after stabilization

That review must be consistent with **Chapter Six, **Article XXIII-A** (*Justice Objective and Scope*)** and **CJS-3.13** (*procedural integrity and adjudication terms*).

**Emergency lifecycle controls (expiry, reauthorization, restoration):** Open emergency actions with predefined **default expiry timestamps**, **independent review intervals**, and **restoration/rollback trigger criteria**.

Tie those criteria to observable conditions.

Continuation past default expiry requires documented reauthorization under **Article XXIII-D**. That record must show ongoing necessity and proportionality (**CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*); **Chapter One** and **Chapter Five** where definitional or scaling detail applies). It must also show why less-restrictive feasible alternatives are insufficient.

Crisis records must capture trigger evidence, alternatives considered, review outcomes, extension rationale, and rollback/restoration execution status for retrospective audit.

**Emergency closure and restoration completion evidence:** Close emergency status when predefined termination criteria are met or when continuation burden fails at review under **Article XXIII-D**.

Closure records must:
- show objective evidence that **(a)** emergency predicates no longer materially justify extraordinary measures;
- show that **(b)** rollback or compensatory restoration was completed or is on a time-bound completion plan;
- show that **(c)** residual risks are disclosed with monitoring owners and cadence;
- show that **(d)** deferred rights, access, or participation were restored, or have auditable restoration timelines with accountable owners.

**Crisis communications:** Use designated roles and channels for **accurate, timely** stakeholder-facing communications during incidents and degradations.

**Materially misleading** crisis messaging is inconsistent with **Article XV-A**.

Maintain **audit trails** sufficient to reconstruct what was communicated, to whom, when, and on what evidential basis (**Article XV-A**).

Apply **[corpus_systems.md](../corpus_systems.md), CS-2 — Information types and handling** to sensitive data in those trails.

**Exercises and drills:** Run tabletop, simulation, or live exercises on cadences proportional to system class and stewardship tier.

Cadence is most demanding for **Class A** and **CSS-A**.

Coverage includes degraded operation, security and integrity failures, governance unavailability, and cross-system dependency breakdown.

Findings must be **recorded** and **remediated**. Where applicable, feed findings into **Article XXI-A** RCA and into **simulation and stress testing** requirements elsewhere in this Protocol.

**H. Self-healing and recovery-path integrity (**Article XII-F** (*Resilience and Self-Healing Baseline*) implementation profile).** This subsection specifies **test, verify, and deploy** expectations for self-healing behavior. Normative recovery floors — detection, containment, safe-failure preference, non-masking, Rights-Floor continuity, autonomy scaling, and root-cause closure — are owned by **[Article XII-F](../core_06-06_rights_part_c.md#article-xii-f-resilience-and-self-healing-baseline)** (*Resilience and Self-Healing Baseline*), [Chapter One §4.1](../core_01_a_values_principles.md#41-resilience-and-self-healing-design) (*Resilience and Self-Healing Design*), and **Chapter Five** [*Self-Healing*](../core_05_band_continuity.md#self-healing-constitutional). This subsection does **not** restate or narrow those homes. Where this subsection is silent, they govern. It applies proportionally to system class and impact, most rigorously for **Class A** and **Class B** systems and to **Critical System Stewards** under **CS-4**.

**Recovery-path design records:** Self-healing behavior must be a designed capability, not an emergent one. Design records must identify the fault classes the recovery path addresses, the disclosed degradation paths it traverses, the pre-fault authority envelope it operates within, and the restoration targets it is expected to reach. Expansions of tool access, data access, credential scope, or cross-system reach during recovery are **prohibited unless pre-authorized in the pre-fault envelope** and independently reviewable, implementing **Article XII-F**'s Containment bullet. For self-healing tie-breaking under uncertainty, safe failure, quarantine, or controlled handoff preference and [Reversibility](../core_05_band_continuity.md#reversibility-constitutional) preference are governed by **Article XII-F** and **Article XXI-B** (*Auditability, Challenge, and Reversibility Preference*). Deploy-time rollback and containment for lifecycle change remain under **Article XVI-B** and **CJS-3.20** (*Continuity: reversibility and containment terms*).

**Recovery-path testing and verification:** Self-healing behavior must be **testable as a path**, not only as a steady-state property. Testing must cover detection latency, containment scope, graceful-degradation paths, safe-failure preference under uncertainty, reversibility of recovery actions, observability of recovery attempts including suppressed attempts, dependency and cascading-failure propagation, accountability for recovery decisions, and autonomy-scaling under **Article XII-E** (*High-Autonomy Systems and Tool-Mediated Process Integrity*).

Testing must include adversarial scenarios in which the recovery path is the attack surface (for example, triggering recovery to suppress an emerging fault signal; triggering recovery to expand authority; triggering recovery to re-route contestability).

For **Class A** and **Class B** systems, recovery-path testing must include at least one scenario under each of **CJS-3.19** (graceful degradation and failure-mode integrity) and **CJS-3.21** (adversarial robustness and abuse resistance). Findings feed into **Article XXI-A** RCA and into simulation and stress testing elsewhere in this Protocol. Evidentiary sufficiency remains subject to **Chapter Four**.

**Recovery-path observability (non-masking ops):** Recovery actions, recovery attempts, and suppressed recovery attempts are auditable events under **Article XV-A** as **Article XII-F** requires. Observability of the recovery path must be at least as strong as observability of the steady state. Log compression, event deduplication, or evidence-retention windows that reduce evidential fidelity of recovery behavior below the **Article XV-A** baseline are non-compliant. Independent verification must be able to reconstruct **both** the recovery path and what the recovery path handled or suppressed.

**Rights-Floor continuity in degraded and recovering states (ops disclosure):** Where degraded-mode designs curtail contestability intake, **Article XV-A** audit fidelity, **Article XII-B** challenge acknowledgment, or comparable floor protections, treat that curtailment as **Article XXVI** (*Transition Governance, Continuity, and Re-Baselining*) transition-governance territory and disclose it accordingly. Participant-facing disclosure during degraded and recovering operation must accurately describe the state as a Rights-Floor-affected state where it is one, consistent with **Article XII-C** (*Prohibition of False Trust and Misleading Reliance*) and **Article XV-A**. Silent narrowing remains non-compliant under **Article XII-F**.

**Root-cause closure discipline (ops register):** Operators must maintain an **open root-cause obligations register** recording recurring fault classes, confidence levels, material uncertainties, and disclosed expected-closure timeline per **Article XV-A**, implementing **Article XII-F**'s root-cause closure bullet. Recurrence of the same fault class across cycles must be treated as a single open root-cause obligation and not as closure of each incident. Reducing operator burden consistent with **Avoidable Burden** under **Chapter One §6.3** must not be used to defer indefinite closure of defects that materially affect safety or the Rights Floor.

**High-autonomy recovery (**Article XII-E** pointer):** Autonomous recovery by high-autonomy systems remains subject to **Article XII-E** as **Article XII-F** states. Recovery authority must not be used to bypass [Contestability](../core_05_band_accountability.md#contestability), challenge under **Article XII-B**, or independent verification under **Article XV-A** and **Article XV**. Internalization of contestability intake, audit-event emission, or external-review pathways during recovery is prohibited; such channels must remain materially external or independently verifiable.

This subsection is an operational profile. It does not create rights and must not be read to narrow **Article XII-F**, **Chapter One §4.1**, or **Chapter Five** *Self-Healing*. **Protocol S4** subsection **I** and **Protocol D** section **8** apply this subsection by reference for protocol-specific cross-checks; they are not second self-healing profiles.

**Recertification, regression testing, and certification defects.** Read with [Chapter Seven §11 System Certification Record](../core_07_b_system_alignment_certification_record_process.md#11-certification-record) (*record contents*) and [Chapter Seven §2 System Class Evaluation](../core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation) (*certification verification hook*); **CS-3 — System classification and handling** (*class scaling*); and **CJS-3.21** (*adversarial robustness and abuse-resistance terms*, including regression and hardening cycle obligations).

Every recertification or revalidation of a system alignment certification record must include **regression testing** showing that previously verified behavior, controls, and safeguards still hold — or that any break is identified, remediated, bounded by conditions, or reflected in the certification outcome. The certification record must state the regression scope, standard test suites run, custom tests run, results, known failures, remediations, and any accepted residual risk with justification.

For **Class A**, **Class B**, and **Class C** systems, regression testing on each recertification must include both:

- **Standard tests:** baseline suites appropriate to the assigned class and domain, including baseline security, abuse-resistance, and failure-mode coverage under **CJS-3.21** and data types in scope under **CS-2 — Information types and handling**; and
- **Custom tests:** system-specific tests for the system's threat model, dependencies, and known failure or abuse modes that standard suites alone would not cover.

For **Class L** and **Class P** systems where recertification applies, regression depth remains proportionate under **CS-3 — System classification and handling**, but recertification without regression coverage where feasible is a certification defect.

**Initial recognition** may rely on pre-deployment evidence prepared under this Protocol, including:

- **Forum recognition and lifecycle review:** evidence packages for scope, classification, testing, residual risk, remediation readiness, and monitoring;
- **Pre-deployment stress testing;**
- **Development and test environments;**
- **Progressive deployment and escalation;**
- **Simulation and stress testing.**

For **Class A** and **Class B** systems, that evidence must also cover:

- **Recovery-path testing and verification;** and
- remediated **Exercises and drills** findings where this Protocol requires them.

**Each later recertification** must rerun or extend regression coverage for material changes since the prior record, read with *Forum recognition and lifecycle review* (ongoing alignment review), *Root cause analysis*, and the requirement to validate corrective measures before deployment.

Missing regression testing, stale results, unfixed regressions, or material fixes accepted without regression confirmation where feasible must be treated as certification defects.

---

**Previous file:** [cs_04_critical_system_stewardship.md](cs_04_critical_system_stewardship.md)

**Next file:** [cs_protocol_b_system_comprehensibility_complexity_stewardship.md](cs_protocol_b_system_comprehensibility_complexity_stewardship.md)
