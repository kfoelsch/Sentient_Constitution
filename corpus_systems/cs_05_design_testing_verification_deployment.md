# CS-5: Design, testing, verification, and deployment

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **binding incorporated implementation text** where [`corpus_systems.md`](../corpus_systems.md) is incorporated under [Chapter Seventeen](../core_17_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It holds **CS-5** (*Design, testing, verification, and deployment*). User-reachable capability surfaces for in-scope systems are in [`cs_05_a_user_facing_capabilities.md`](cs_05_a_user_facing_capabilities.md) (**CS-5, Part A**).
>
> Start at the [Systems and data landing page](../corpus_systems.md) for reading order, or the [systems registry](cs_00_registry_and_reading_rules.md) for identifier rules and the family map. Most readers reach this file from a citation rather than reading the folder front to back.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Article XVII](../core_06_rights_part_c.md#article-xvii-system-lifecycle-environments-and-reversibility) (*System Lifecycle, Environments, and Reversibility*); [Article XVIII](../core_06_rights_part_c.md#article-xviii-innovation-experimentation-and-creative-freedom) (*Innovation, Experimentation, and Creative Freedom*); [Article XIII-F](../core_06_rights_part_c.md#article-xiii-f-resilience-and-self-healing-baseline) (*Resilience and Self-Healing Baseline*); [Chapter One §10](../core_01_a_values_principles.md#10-resilience-and-self-healing-design); [Chapter Four](../core_04_burden_traceability_verification.md); [Chapter Seventeen](../core_17_incorporation.md#chapter-seventeen-incorporation-bridge); and [Chapter Five](../core_05__definitions_home.md#chapter-five-foundational-definitions) canonical definitions.
- Downstream: [§1](#cs-51-purpose-and-role); [§2](#cs-52-personal-isolated-and-experimental-systems); [§7](#cs-57-non-experimental-systems); [§8](#cs-58-governance-continuity-crisis-communications-and-exercises-high-impact-systems); [§9](#cs-59-self-healing-and-recovery-path-integrity); [§10](#cs-510-recertification-regression-testing-and-certification-defects); [CS-5, Part A](cs_05_a_user_facing_capabilities.md#cs-5-part-a-user-facing-capability-surfaces).
- Read with: **CS-5** (*User-facing capability surfaces*); **CS-5** (*User-facing capability surfaces*), **Part A**; **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship**; **CS-6** (*Comprehensibility and complexity stewardship*); **CJS-3.19** (*Continuity: graceful degradation and failure-mode integrity terms*); **CJS-3.20** (*Continuity: reversibility and containment terms*); **CJS-3.21** (*Continuity: adversarial robustness and abuse-resistance terms*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [System](../core_05_band_continuity.md#system) · [O](../core_05_band_continuity.md#system) · [M](../core_05_band_continuity.md#system-definition-a) · [A](../core_05_band_continuity.md#system-definition-a) · [C](../core_05_band_continuity.md#system-definition-c)
- [Dependency](../core_05_band_continuity.md#dependency) · [O](../core_05_band_continuity.md#dependency) · [M](../core_05_band_continuity.md#dependency-a) · [A](../core_05_band_continuity.md#dependency-a) · [C](../core_05_band_continuity.md#dependency-c)
- [Reversibility](../core_05_band_continuity.md#reversibility) · [O](../core_05_band_continuity.md#reversibility) · [M](../core_05_band_continuity.md#reversibility-constitutional-a) · [A](../core_05_band_continuity.md#reversibility-constitutional-a) · [C](../core_05_band_continuity.md#reversibility-constitutional-c)
- [Self-Healing](../core_05_band_continuity.md#self-healing) · [O](../core_05_band_continuity.md#self-healing) · [M](../core_05_band_continuity.md#self-healing-constitutional-a) · [A](../core_05_band_continuity.md#self-healing-constitutional-a) · [C](../core_05_band_continuity.md#self-healing-constitutional-c)
- [Emergency and Contingency](../core_05_band_continuity.md#emergency-and-contingency-constitutional) · [O](../core_05_band_continuity.md#emergency-and-contingency-constitutional) · [M](../core_05_band_continuity.md#emergency-and-contingency-constitutional-a) · [A](../core_05_band_continuity.md#emergency-and-contingency-constitutional-a) · [C](../core_05_band_continuity.md#emergency-and-contingency-constitutional-c)
- [System Alignment Certification](../core_05_band_continuity.md#system-alignment-certification) · [O](../core_05_band_continuity.md#system-alignment-certification) · [M](../core_05_band_continuity.md#system-alignment-certification-constitutional-a) · [A](../core_05_band_continuity.md#system-alignment-certification-constitutional-a) · [C](../core_05_band_continuity.md#system-alignment-certification-constitutional-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Force Majeure](../core_05_band_accountability.md#force-majeure) · [O](../core_05_band_accountability.md#force-majeure) · [M](../core_05_band_accountability.md#force-majeure-constitutional-a) · [A](../core_05_band_accountability.md#force-majeure-constitutional-a) · [C](../core_05_band_accountability.md#force-majeure-constitutional-c)

</details>

<br>

This file is the systems implementation home for **CS-5** (*Design, testing, verification, and deployment*).

*In plain terms: **CS-5** (*User-facing capability surfaces*) is the engineering lifecycle profile: how a constitutional system must be designed, tested, verified, separated across environments, rolled out in stages, exercised against crises, and re-certified after change. It states required outcomes rather than fixed technology, so implementations may evolve while staying auditable.*
<a id="cs-5-1-purpose-and-role"></a>
## CS-5.1 Purpose and role

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Article XVII](../core_06_rights_part_c.md#article-xvii-system-lifecycle-environments-and-reversibility) (*System Lifecycle, Environments, and Reversibility*); [Article XVIII](../core_06_rights_part_c.md#article-xviii-innovation-experimentation-and-creative-freedom) (*Innovation, Experimentation, and Creative Freedom*); [Article XIII-F](../core_06_rights_part_c.md#article-xiii-f-resilience-and-self-healing-baseline) (*Resilience and Self-Healing Baseline*).
- Downstream: [§2](#cs-52-personal-isolated-and-experimental-systems) through [§10](#cs-510-recertification-regression-testing-and-certification-defects).
- Read with: **CS-5** (*User-facing capability surfaces*); **CS-3 — System classification and handling**; **CS-4 — Critical system stewardship**; **CJS-3.19** (*Continuity: graceful degradation and failure-mode integrity terms*); **CJS-3.20** (*Continuity: reversibility and containment terms*); **CJS-3.21** (*Continuity: adversarial robustness and abuse-resistance terms*).

</details>

<br>

*In plain terms: what this file owns — design, test, verify, deploy, exercise, and recertify — and what stays in Chapter Six, Chapter Five, and **CJS-3** (*operational cluster library*).*

**What this file owns**

- the systems-layer operational profile for design, testing, verification, environment separation, progressive deployment, crisis continuity exercises, self-healing path testing, and recertification regression;
- engineering evidence readiness for forum recognition and lifecycle review.

**What this file does not own**

- Rights Floors in **Article XVII** (*System Lifecycle, Environments, and Reversibility*), **Article XVIII** (*Innovation, Experimentation, and Creative Freedom*), and **Article XIII-F** (*Resilience and Self-Healing Baseline*) — this file implements those articles and does not replace or narrow them;
- Chapter Five meanings (*Reversibility*; *Self-Healing*; *Emergency and Contingency*; *Force Majeure*);
- shared operational detail in **CJS-3.19** (*graceful degradation and failure-mode integrity*), **CJS-3.20** (*reversibility and containment*), and **CJS-3.21** (*adversarial robustness and abuse resistance*);
- process recognition mechanics in **CF-7.2** (*Constitutional alignment recognition and review*) and Chapter Eight;
- user-reachable in-scope capability surfaces — those are in **[CS-5, Part A](cs_05_a_user_facing_capabilities.md#cs-5-part-a-user-facing-capability-surfaces)**.

**Implements.** Sentient Constitution Chapter Six, **[Article XVII](../core_06_rights_part_c.md#article-xvii-system-lifecycle-environments-and-reversibility) (*System Lifecycle, Environments, and Reversibility*)** (*System Lifecycle, Environments, and Reversibility*), **[Article XVIII](../core_06_rights_part_c.md#article-xviii-innovation-experimentation-and-creative-freedom) (*Innovation, Experimentation, and Creative Freedom*)** (*Innovation, Experimentation, and Creative Freedom*), and **[Article XIII-F](../core_06_rights_part_c.md#article-xiii-f-resilience-and-self-healing-baseline) (*Resilience and Self-Healing Baseline*)** (*Resilience and Self-Healing Baseline*), read with [Chapter One §10](../core_01_a_values_principles.md#10-resilience-and-self-healing-design) (*Resilience and Self-Healing Design*), Chapter Five, and **[Chapter Four](../core_04_burden_traceability_verification.md)** where evidence and verification claims are material.

This file supplies engineering and deployment profiles that implement, rather than restate, Articles XVII, XVIII, and XIII-F. It is an operational profile, not a second home for those floors. This constitution defines required capabilities and outcomes. Specific technical implementations may evolve, provided they remain auditable and aligned with constitutional principles. System categories in this file are functional and may overlap. Where multiple classifications apply, the safeguards with the [Fullest Protective Effect](../core_05_band_integrative.md#fullest-protective-effect) govern.
Creating new systems, tools, and environments is an act of stewardship. New deployments must be designed for the holistic wellbeing of the constitutional community and must **not** introduce avoidable harm. Requirements in this file must be applied proportionally to system scope, impact, and dependency under **CS-3 — System classification and handling** and **CS-4 — Critical system stewardship**.
Where this file is silent, Sentient Constitution Chapters Two through Five govern. Where this file and `corpus_joint_structure.md` conflict, the applicable requirement with the [Fullest Protective Effect](../core_05_band_integrative.md#fullest-protective-effect) governs.

**Forum recognition and lifecycle review.** New systems with material impact, and existing systems whose scope, behavior, dependency, autonomy, incentive structure, or risk profile materially changes, must be prepared for official **constitutional alignment recognition or review** through the forum pathways in `core_12_forum.md` **Chapter Twelve** and [**CF-7.2**](../corpus_forum/cf_07_integrity_safeguards_anti_capture_anti_self_judging.md#cf-72-constitutional-alignment-recognition-and-review) (*Constitutional alignment recognition and review*). System owners must maintain evidence packages sufficient for the forum to evaluate scope, classification, testing, stakeholder impact, residual risk, remediation readiness, and ongoing monitoring. Where a system has material ecological exposure, environmental-precondition dependency, lifecycle burden, restoration duty, or reasonably foreseeable ecological risk, the evidence package must also support **Environment** forum environmental-alignment component review, including ecological baseline, lifecycle and resource-flow analysis, foreseeable failure modes, restoration or remediation plan, monitoring cadence, uncertainty, and contest path. Forum recognition is scope-bound and does **not** replace operator responsibility, CS-3 (*System classification machinery*) classification, CS-4 (*Critical system stewardship*) stewardship, **Article XVI-A** (*Auditability and Observable Evidence*) auditability, **Article XIII-A** (*Reliability and Trustworthiness Baseline*) challenge rights, or Environment forum authority over ecological merits. Process recognition mechanics live in CF-7.2 (*Constitutional alignment recognition and review*) and Chapter Eight; this file owns engineering evidence readiness.

<a id="cs-5-2-personal-isolated-and-experimental-systems"></a>
## CS-5.2 Personal, isolated, and experimental systems

*In plain terms: The reduced-requirement track: sandboxed operation, no shared-infrastructure dependencies, and no material effect on anyone else.*

Rights-floor eligibility, reduced-requirement conditions, disclosure, containment, and prohibited externalization are owned by **[Article XVIII-A](../core_06_rights_part_c.md#article-xviii-a-sandboxed-scope) (*Sandboxed Scope*)** (*Sandboxed Scope*) and **[Article XVIII-B](../core_06_rights_part_c.md#article-xviii-b-containment-disclosure-and-opt-in) (*Containment, Disclosure, and Opt-In*)** (*Containment, Disclosure, and Opt-In*), read with valid **Class P** treatment under **CS-3 — System classification machinery**. This subsection does not restate those floors.

**Systems-layer profile (does not narrow XVIII):** sandboxed or controlled operation; no downstream dependencies on shared production infrastructure; no material effect on other sentients, shared infrastructure, or ecosystem stability. Where those conditions hold, environment separation, deployment rigor, and audit depth under **§7** (*Non-experimental systems*) may be lighter. Such systems may prioritize simplicity and rapid iteration and need not maintain full multi-environment deployment structures. Misrepresentation of isolation or impact is governed by **§4** (*Misclassification and evasion*) and **Article XVII-C** (*Misclassification and Evasion Consequences*).

<a id="cs-5-3-creative-entertainment-and-expressive-systems"></a>
## CS-5.3 Creative, entertainment, and expressive systems

*In plain terms: Creative and expressive systems get wider latitude on features, subject to containment, disclosure, and opt-in.*

Rights-floor creative freedom, containment, disclosure, opt-in, and transition triggers are owned by **Article XVIII-A** (*Sandboxed Scope*) through **XVIII-C**. This subsection does not restate those floors.

**Systems-layer profile (does not narrow XVIII):** systems primarily for creative expression, entertainment, artistic production, or stakeholder-driven experiential environments may use higher feature velocity and simplified environment structures only while risk remains demonstrably contained. Transition toward **§7** (*Non-experimental systems*) compliance is required when any of the following is present and not already covered by **Article XVIII-C** (*Transition to Higher-Obligation Regimes*)'s impact, dependency, irreversibility, or shared-system integration tests:

- persistent stakeholder identity, value, or reputation data that is transferable, interoperable, or materially impactful outside the originating system or closely scoped artistic environments;
- autonomous or semi-autonomous agents acting for stakeholders that may affect external systems (including gaming or simulation environments used for agent testing or training);
- measurable influence on external systems, markets, or collective behavior beyond defined scope.

<a id="cs-5-4-misclassification-and-evasion"></a>
## CS-5.4 Misclassification and evasion

*In plain terms: Claiming the light track while exerting real outside impact. The tell-tale signs are concealed dependencies, concealed stakeholders, and 'experimental' labels used as cover.*

The prohibition on claiming reduced lifecycle or sandbox obligations while exerting undisclosed or material external impact, and the consequence chain under **Articles XV**, **XVI-A**, **XIX-A**, and **XX-A**, are owned by **[Article XVII-C](../core_06_rights_part_c.md#article-xvii-c-misclassification-and-evasion-consequences) (*Misclassification and Evasion Consequences*)** (*Misclassification and Evasion Consequences*). This subsection does not restate that Article.

**Systems-layer indicators (non-exhaustive):** concealed dependencies; concealed stakeholders; concealed risk exposure; **Class P** or "experimental" labeling used to evade CS-4 (*Critical system stewardship*) class-scaled assurance, CS-4 (*Critical system stewardship*) stewardship, or **§7** (*Non-experimental systems*) environment and promotion controls. Detection and evidence packaging for forum or certification review remain operator duties under *Forum recognition and lifecycle review* and the closing recertification block.

<a id="cs-5-5-transition-to-higher-impact-systems"></a>
## CS-5.5 Transition to higher-impact systems

*In plain terms: When a system's impact, dependency, or shared-infrastructure integration grows, it must move up to the full track — openly and on time.*

Transition floors — transparent, timely move toward **Article XVII-A** (*Lifecycle Governance and Environment Separation*) and **CS-5** (*User-facing capability surfaces*) **Non-experimental systems** when impact, dependency, irreversibility, or shared-system integration grows — are owned by **[Article XVIII-C](../core_06_rights_part_c.md#article-xviii-c-transition-to-higher-obligation-regimes) (*Transition to Higher-Obligation Regimes*)** (*Transition to Higher-Obligation Regimes*). This subsection does not restate that Article.

**Systems-layer triggers and duties (implement XVIII-C; do not narrow it):**

- Triggers include stakeholders beyond the original operator; measurable growth in dependency, usage, or resource impact; downstream production dependencies; shared-infrastructure interaction; non-trivial risk; and increasing irreversibility of impactful failure modes.
- Transitions must be documented, completed within a reasonable timeframe proportionate to impact, and remain subject to audit and challenge under **Articles XVI-A** and **XIII-A**.
- Interim safeguards during transition must meet **§7** (*Non-experimental systems*) environment-isolation and progressive-deployment controls proportionate to current risk.

<a id="cs-5-6-experimental-substrate-features-and-systems"></a>
## CS-5.6 Experimental substrate features and systems

*In plain terms: Experiments close to foundational infrastructure carry stricter containment, rollback, and opt-in requirements than ordinary experiments.*

Opt-in, disclosure, rollback, and containment floors for elevated-risk or substrate-proximate experimentation are owned by **Article XVIII-B** (*Containment, Disclosure, and Opt-In*), read with **Article XVII-A** (*Lifecycle Governance and Environment Separation*) boundary integrity. This subsection does not restate those floors.

**Systems-layer profile (does not narrow XVII/XVII):**

- **Risk profile:** proximity to foundational infrastructure requires stricter containment, transparency, and reversibility than ordinary sandbox scopes under **§2** (*Personal, isolated, and experimental systems*) or **§3** (*Creative, entertainment, and expressive systems*).
- **Innovation controls:** higher-velocity innovation is permitted with mandatory snapshot and restoration so stakeholders can revert to a verified stable state without data loss where feasible.
- **Deployment contexts:** opt-in environments, isolated stakeholder groups, and reversible contexts; per-environment disclosure of risk levels; rollback capability; prevention of unintended systemic impact.
- **Boundary and presentation integrity:** do not route production activity through non-production environments to bypass safeguards; do not fragment systems across environments to obscure real operational impact; accurately label experimental or unvalidated systems as not production-ready; never bypass required environment progression for high-impact changes.
- **Documentation:** document environments and transitions under **Article XVII-A** (*Lifecycle Governance and Environment Separation*), and expose deployment pathways, testing results (where feasible), and known risks and assumptions. Verification of those claims remains subject to **Chapter Four** and **Article XVI-A** (*Auditability and Observable Evidence*).

<a id="cs-5-7-non-experimental-systems"></a>
## CS-5.7 Non-experimental systems

*In plain terms: The default track for everything that does not qualify above. Requirements scale with impact: a system affecting only its builder may stay simple.*

Systems that do not qualify under **Articles XVIII-A** and **XVIII-B** (and **§2** (*Personal, isolated, and experimental systems*), **§3** (*Creative, entertainment, and expressive systems*), or **§6** (*Experimental substrate features and systems*) where applicable) must comply fully with this subsection. This subsection implements **[Article XVII-A](../core_06_rights_part_c.md#article-xvii-a-lifecycle-governance-and-environment-separation) (*Lifecycle Governance and Environment Separation*)** (*Lifecycle Governance and Environment Separation*) and **[Article XVII-B](../core_06_rights_part_c.md#article-xvii-b-progressive-deployment-and-reversibility) (*Progressive Deployment and Reversibility*)** (*Progressive Deployment and Reversibility*). It does **not** restate those Articles. Shared reversibility and containment mechanics also read with **CJS-3.20** (*Continuity: reversibility and containment terms*).

**Guiding principles — proportional responsibility:** Requirements scale with impact under **CS-4** (*Critical system stewardship*) and **CS-4** (*Critical system stewardship*). Systems that affect only the builder may remain simple. Systems that affect others bear the full burden of stewardship.

**Guiding principles — safe iteration:** Design must enable rapid learning and improvement without exposing sentients, shared infrastructure, or the ecosystem to unnecessary risk.

**Systematic assessment:** Categorize systems by impact on sentient survival and ecological integrity (**Articles I–III and VI**), read with **CS-3** (*System classification machinery*) class profiles.

**Substrate** systems (energy, connectivity, foundational data) require maximum stability and slower, audited rollout.

**Sentient-facing** systems (creative tools, social interfaces, small-scale internal corporate software, games, and similar) may prioritize high-velocity innovation only when sandboxed from material harm to survivability and natural ecology.

**Automated Constitutional Auditing (ACA):** Implement independent, auditable constitutional monitoring appropriate to scope and criticality, including system class where assigned. Monitoring must be sufficient to detect, document, and respond to violations of foundational requirements (**Articles I–III and VI**). Where technically feasible, incorporate automated detection and response, including **reversible** interventions under defined, auditable thresholds. ACA evidence remains subject to **Chapter Four** and **Article XVI** (*Audit, Transparency, and Independent Verification*).

**Open-source integrity:** Foundational designs and deployment logs should be transparent and accessible to the constitutional community. That access supports auditability and meaningful consent. Avoid black-box systems that bypass consent.

**Open hardware, open software, open systems:** Operational design and stewardship should **align** with **CJS-3.17** (*interoperability, portability, and exit-integrity terms*) — *Open hardware, open software, and open systems* — and **CJS-3.17** (*Continuity: interoperability, portability, and exit-integrity terms*) open data-format and protocol discipline, so that **preference** for **open** stacks scales with **material impact**, **dependency**, and **stewardship tier** under **CS-4** (*Critical system stewardship*) and **CS-4** (*Critical system stewardship*). Classification and tier rules may set stronger disclosure, inspectability, substitutability, format, schema, API, or interchange-protocol expectations for **Class A**, **Class B**, and high-tier systems than for bounded or experimental scopes, without narrowing **CJS-3.12** (*burden-of-justification and constraint terms*) justification paths where proprietary or closed choices are auditably required. Comprehensibility and complexity stewardship for modular design route to **CS-6** (*Comprehensibility and complexity stewardship*) and **Article XXIII** (*Comprehensibility and Complexity Stewardship*); this file only requires that innovation in one verified module must not force alteration of other verified modules in a way that disrupts baseline requirements.

**Pre-deployment stress testing:** Before high-impact systems enter the info-sphere or the natural world, require rigorous simulation. Simulation must surface sentient-driven threats and ecological degradation. It must include worst-case modeling for biological and synthetic effects and for info-sphere integrity, read with **CJS-3.19** (*Continuity: graceful degradation and failure-mode integrity terms*) and **CJS-3.21** (*Continuity: adversarial robustness and abuse-resistance terms*).

**Iterative, transparent deployment:** High-impact rollout must be gradual and auditable under **Article XVII-B** (*Progressive Deployment and Reversibility*). Stakeholders retain the right to provide feedback and to challenge deployment or reliance under **Article XIII-A** (*Reliability and Trustworthiness Baseline*) at every stage.

**Reversibility:** Implement **Article XVII-B** (*Progressive Deployment and Reversibility*), Chapter Five (*Reversibility*), and **CJS-3.20** (*reversibility and containment terms*). Non-experimental systems must support rollback, containment, or compensatory restoration where full rollback is infeasible. Where deployment would violate foundational requirements, reversion to a prior stable state is required to the extent **Article XVII-B** (*Progressive Deployment and Reversibility*), **Chapter One**, and **Chapter Five** demand. That reversion must avoid lasting harm to sentients or the natural environment.

**Design for agentic wellbeing:** Architecture should favor stakeholder autonomy: clarity over engagement, and stakeholder-directed goals over platform-defined metrics.

**Development and test environments:** Systems must use clearly defined, separable operational environments. At minimum, maintain clearly labeled environments along this progression (implements **Article XVII-A** (*Lifecycle Governance and Environment Separation*); adds engineering detail):
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

**Progressive deployment and escalation:** Where feasible, changes move **development -> testing and validation -> staging -> pilots (when present) -> production**. Escalation between environments must be justified, documented, evaluated against constitutional requirements, and include rollback and containment consistent with **Article XVII-B** (*Progressive Deployment and Reversibility*), Chapter Five (*Reversibility*), and **CJS-3.20** (*Continuity: reversibility and containment terms*).

**Simulation and stress testing:** Testing environments must support expected and adversarial simulation, including system failures, stakeholder behavior, ecosystem interactions, and worst-case scenarios.

**High-impact systems** must demonstrate resilience under stress before production, document limitations and known risks, and inform adaptive allocation decisions where applicable.

**Root cause analysis (**Article XXIV-A** (*Diagnostic Rigor and Causal Attribution*)):** RCA in these environments must satisfy **Article XXIV-A** (*Diagnostic Rigor and Causal Attribution*). Environments must support reproduction of failures, isolation of root causes, and validation of corrective interventions. Where feasible, conduct RCA in controlled environments before production changes. Validate corrective measures before deployment. Evidentiary sufficiency for RCA claims remains subject to **Chapter Four**.

<a id="cs-5-8-governance-continuity-crisis-communications-and-exercises-high-impact-systems"></a>
## CS-5.8 Governance continuity, crisis communications, and exercises (high-impact systems)

*In plain terms: For Class A and Class B systems and the stewards behind them: keep governance running through a crisis, and rehearse it before you need it.*

This subsection states governance-side business continuity and recovery expectations. It applies to **Class A** and **Class B** systems, and to materially affecting **Critical System Stewards** (CS-4 — Critical system stewardship). It complements technical resilience, environment separation, and testing elsewhere in this file, and it complements **CJS-3.19** (*Graceful Degradation and Failure Mode Integrity*), incorporated via **Sentient Constitution Chapter Seventeen**. It does **not** create constitutional Rights Floors.

Crisis and emergency definitional homes remain in **Sentient Constitution Chapter Five** (*Emergency and Contingency*; *Force Majeure*). Procedural emergency controls, conflict resolution, proportionality, continuation burden, and review of restrictions and emergency measures remain governed by [**Article XXVI** (*Timely Retrospective Review and Restorative Alignment*)](../core_06_rights_part_e.md#article-xxvi-timely-retrospective-review-and-restorative-alignment) (*Timely Retrospective Review and Restorative Alignment*) and **[Chapter Twelve §6.1 Emergency measures and continuation burden](../core_12_forum.md#61-emergency-measures-and-continuation-burden)** (*Emergency measures and continuation burden*). They also remain governed by Chapter Thirteen decision-resolution requirements and **CJS-3.14** (*intervention governance and override-authorization terms*) and **CJS-3.23** (*intervention and override integrity terms*).

**Crisis governance:** Use documented succession and delegation for binding governance decisions when primary authorities are impaired.

Define pre-authorized boundaries for expedited action where **Article XX** (*Justice After Verified Violation*), **Chapter Twelve §6.1** (*Emergency measures and continuation burden*), and Chapter Thirteen decision-resolution requirements permit.

Require post-action review, documentation, and **Article XVI-A** (*Auditability and Observable Evidence*) auditability of stress-time decisions.

**Interpretive authority continuity and anti-capture checks:** For **Class A** and **Class B**, continuity plans must preserve **bounded and contestable** constitutional interpretation during crisis operation.

Plans must include:
- **(a)** temporary role pathways that a single authority cannot monopolize across consecutive cycles
- **(b)** conflict disclosure and recusal controls for emergency decision-makers
- **(c)** mandatory publication of constitutional reasoning for emergency interpretive determinations once immediate safety constraints permit
- **(d)** independent secondary review after stabilization

That review must be consistent with **Chapter Six, **Article XX-A** (*Justice Objective and Scope*)** and **CJS-3.13** (*procedural integrity and adjudication terms*).

**Emergency lifecycle controls (expiry, reauthorization, restoration):** Open emergency actions with predefined **default expiry timestamps**, **independent review intervals**, and **restoration/rollback trigger criteria**.

Tie those criteria to observable conditions.

Continuation past default expiry requires documented reauthorization under **Chapter Twelve §6.1** (*Emergency measures and continuation burden*). That record must show ongoing necessity and proportionality (**CJS-3.11** (*distributed and proportional authority terms*) and **CJS-3.7** (*quorum and participatory legitimacy terms*); **Chapter One** and **Chapter Five** where definitional or scaling detail applies). It must also show why less-restrictive feasible alternatives are insufficient.

Crisis records must capture trigger evidence, alternatives considered, review outcomes, extension rationale, and rollback/restoration execution status for retrospective audit.

**Emergency closure and restoration completion evidence:** Close emergency status when predefined termination criteria are met or when continuation burden fails at review under **Chapter Twelve §6.1** (*Emergency measures and continuation burden*).

Closure records must:
- show objective evidence that **(a)** emergency predicates no longer materially justify extraordinary measures;
- show that **(b)** rollback or compensatory restoration was completed or is on a time-bound completion plan;
- show that **(c)** residual risks are disclosed with monitoring owners and cadence;
- show that **(d)** deferred rights, access, or participation were restored, or have auditable restoration timelines with accountable owners.

**Crisis communications:** Use designated roles and channels for **accurate, timely** stakeholder-facing communications during incidents and degradations.

**Materially misleading** crisis messaging is inconsistent with **Article XVI-A** (*Auditability and Observable Evidence*).

Maintain **audit trails** sufficient to reconstruct what was communicated, to whom, when, and on what evidential basis (**Article XVI-A** (*Auditability and Observable Evidence*)).

Apply **[corpus_systems.md](../corpus_systems.md), CS-2 — Information types and handling** to sensitive data in those trails.

**Exercises and drills:** Run tabletop, simulation, or live exercises on cadences proportional to system class and stewardship tier.

Cadence is most demanding for **Class A** and **CSS-A**.

Coverage includes degraded operation, security and integrity failures, governance unavailability, and cross-system dependency breakdown.

Findings must be **recorded** and **remediated**. Where applicable, feed findings into **Article XXIV-A** (*Diagnostic Rigor and Causal Attribution*) RCA and into **simulation and stress testing** requirements elsewhere in this file.

<a id="cs-5-9-self-healing-and-recovery-path-integrity"></a>
## CS-5.9 Self-healing and recovery-path integrity

*In plain terms: Test, verify, and deploy self-healing as a designed path — not an emergent one — without masking the fault that triggered it.*

This subsection specifies **test, verify, and deploy** expectations for self-healing behavior. Normative recovery floors — detection, containment, safe-failure preference, non-masking, Rights-Floor continuity, autonomy scaling, and root-cause closure — are owned by **[Article XIII-F](../core_06_rights_part_c.md#article-xiii-f-resilience-and-self-healing-baseline) (*Resilience and Self-Healing Baseline*)** (*Resilience and Self-Healing Baseline*), [Chapter One §10](../core_01_a_values_principles.md#10-resilience-and-self-healing-design) (*Resilience and Self-Healing Design*), and **Chapter Five** [*Self-Healing*](../core_05_band_continuity.md#self-healing). This subsection does **not** restate or narrow those homes. Where this subsection is silent, they govern. It applies proportionally to system class and impact, most rigorously for **Class A** and **Class B** systems and to **Critical System Stewards** under **CS-4** (*Critical system stewardship*).

**Recovery-path design records:** Self-healing behavior must be a designed capability, not an emergent one. Design records must identify the fault classes the recovery path addresses, the disclosed degradation paths it traverses, the pre-fault authority envelope it operates within, and the restoration targets it is expected to reach. Expansions of tool access, data access, credential scope, or cross-system reach during recovery are **prohibited unless pre-authorized in the pre-fault envelope** and independently reviewable, implementing **Article XIII-F** (*Resilience and Self-Healing Baseline*)'s Containment bullet. For self-healing tie-breaking under uncertainty, safe failure, quarantine, or controlled handoff preference and [Reversibility](../core_05_band_continuity.md#reversibility) preference are governed by **Article XIII-F** (*Resilience and Self-Healing Baseline*) and **Article XXIV-B** (*Auditability, Challenge, and Reversibility Preference*). Deploy-time rollback and containment for lifecycle change remain under **Article XVII-B** (*Progressive Deployment and Reversibility*) and **CJS-3.20** (*Continuity: reversibility and containment terms*).

**Recovery-path testing and verification:** Self-healing behavior must be **testable as a path**, not only as a steady-state property. Testing must cover detection latency, containment scope, graceful-degradation paths, safe-failure preference under uncertainty, reversibility of recovery actions, observability of recovery attempts including suppressed attempts, dependency and cascading-failure propagation, accountability for recovery decisions, and autonomy-scaling under **Article XIII-E** (*High-Autonomy Systems and Tool-Mediated Process Integrity*).

Testing must include adversarial scenarios in which the recovery path is the attack surface (for example, triggering recovery to suppress an emerging fault signal; triggering recovery to expand authority; triggering recovery to re-route contestability).

For **Class A** and **Class B** systems, recovery-path testing must include at least one scenario under each of **CJS-3.19** (*Continuity: graceful degradation and failure-mode integrity terms*) (graceful degradation and failure-mode integrity) and **CJS-3.21** (*Continuity: adversarial robustness and abuse-resistance terms*) (adversarial robustness and abuse resistance). Findings feed into **Article XXIV-A** (*Diagnostic Rigor and Causal Attribution*) RCA and into simulation and stress testing elsewhere in this file. Evidentiary sufficiency remains subject to **Chapter Four**.

**Recovery-path observability (non-masking ops):** Recovery actions, recovery attempts, and suppressed recovery attempts are auditable events under **Article XVI-A** (*Auditability and Observable Evidence*) as **Article XIII-F** (*Resilience and Self-Healing Baseline*) requires. Observability of the recovery path must be at least as strong as observability of the steady state. Log compression, event deduplication, or evidence-retention windows that reduce evidential fidelity of recovery behavior below the **Article XVI-A** (*Auditability and Observable Evidence*) baseline are non-compliant. Independent verification must be able to reconstruct **both** the recovery path and what the recovery path handled or suppressed.

**Rights-Floor continuity in degraded and recovering states (ops disclosure):** Where degraded-mode designs curtail contestability intake, **Article XVI-A** (*Auditability and Observable Evidence*) audit fidelity, **Article XIII-A** (*Reliability and Trustworthiness Baseline*) challenge acknowledgment, or comparable floor protections, treat that curtailment as **Article XXVIII** (*Transition Governance, Continuity, and Re-Baselining*) transition-governance territory and disclose it accordingly. Participant-facing disclosure during degraded and recovering operation must accurately describe the state as a Rights-Floor-affected state where it is one, consistent with **Article XIII-C** (*Prohibition of False Trust and Misleading Reliance*) and **Article XVI-A** (*Auditability and Observable Evidence*). Silent narrowing remains non-compliant under **Article XIII-F** (*Resilience and Self-Healing Baseline*).

**Root-cause closure discipline (ops register):** Operators must maintain an **open root-cause obligations register** recording recurring fault classes, confidence levels, material uncertainties, and disclosed expected-closure timeline per **Article XVI-A** (*Auditability and Observable Evidence*), implementing **Article XIII-F** (*Resilience and Self-Healing Baseline*)'s root-cause closure bullet. Recurrence of the same fault class across cycles must be treated as a single open root-cause obligation and not as closure of each incident. Reducing operator burden consistent with **Avoidable Burden** under **Chapter One §13.3** (*Minimization of Avoidable Burden*) must not be used to defer indefinite closure of defects that materially affect safety or the Rights Floor.

**High-autonomy recovery (**Article XIII-E** (*High-Autonomy Systems and Tool-Mediated Process Integrity*) pointer):** Autonomous recovery by high-autonomy systems remains subject to **Article XIII-E** (*High-Autonomy Systems and Tool-Mediated Process Integrity*) as **Article XIII-F** (*Resilience and Self-Healing Baseline*) states. Recovery authority must not be used to bypass [Contestability](../core_05_band_accountability.md#contestability), challenge under **Article XIII-A** (*Reliability and Trustworthiness Baseline*), or independent verification under **Article XVI-A** (*Auditability and Observable Evidence*) and **Article XVI** (*Audit, Transparency, and Independent Verification*). Internalization of contestability intake, audit-event emission, or external-review pathways during recovery is prohibited; such channels must remain materially external or independently verifiable.

This subsection is an operational profile. It does not create rights and must not be read to narrow **Article XIII-F** (*Resilience and Self-Healing Baseline*), **Chapter One §10** (*Resilience and Self-Healing Design*), or **Chapter Five** *Self-Healing*. **CS-8** (*Adaptive sustainability and ecosystem resilience*) **§9** (*Self-healing and recovery-path integration*) and **CS-12** (*Decentralized continuity and partition resilience*) **§9** (*Self-healing under decentralized continuity*) apply this subsection by reference for protocol-specific cross-checks; they are not second self-healing profiles.

<a id="cs-5-10-recertification-regression-testing-and-certification-defects"></a>
## CS-5.10 Recertification, regression testing, and certification defects

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: [Chapter Eight §4 System Certification Record](../core_08_b_system_alignment_certification_record_process.md#4-system-certification-record) (*record contents*); [Chapter Eight §2 System Class Evaluation](../core_08_a_system_alignment_certification_evaluation.md#2-system-class-evaluation) (*certification verification hook*); **CS-3 — System classification and handling** (*class scaling*); **CJS-3.21** (*Continuity: adversarial robustness and abuse-resistance terms*) (*adversarial robustness and abuse-resistance terms*, including regression and hardening cycle obligations).

</details>

<br>

*In plain terms: Every recertification must rerun regression coverage so previously verified behavior still holds, or the break is on the record.*

Every recertification of a system alignment certification record must include **regression testing** showing that previously verified behavior, controls, and safeguards still hold — or that any break is identified, remediated, bounded by conditions, or reflected in the certification outcome. The certification record must state the regression scope, standard test suites run, custom tests run, results, known failures, remediations, and any accepted residual risk with justification.

For **Class A**, **Class B**, and **Class C** systems, regression testing on each recertification must include both:

- **Standard tests:** baseline suites appropriate to the assigned class and domain, including baseline security, abuse-resistance, and failure-mode coverage under **CJS-3.21** (*Continuity: adversarial robustness and abuse-resistance terms*) and data types in scope under **CS-2 — Information types and handling**; and
- **Custom tests:** system-specific tests for the system's threat model, dependencies, and known failure or abuse modes that standard suites alone would not cover.

For **Class L** and **Class P** systems where recertification applies, regression depth remains proportionate under **CS-3 — System classification and handling**, but recertification without regression coverage where feasible is a certification defect.

**Initial recognition** may rely on pre-deployment evidence prepared under this file, including:

- **Forum recognition and lifecycle review:** evidence packages for scope, classification, testing, residual risk, remediation readiness, and monitoring;
- **Pre-deployment stress testing;**
- **Development and test environments;**
- **Progressive deployment and escalation;**
- **Simulation and stress testing.**

For **Class A** and **Class B** systems, that evidence must also cover:

- **Recovery-path testing and verification;** and
- remediated **Exercises and drills** findings where this file requires them.

**Each later recertification** must rerun or extend regression coverage for material changes since the prior record, read with *Forum recognition and lifecycle review* (ongoing alignment review), *Root cause analysis*, and the requirement to validate corrective measures before deployment.

Missing regression testing, stale results, unfixed regressions, or material fixes accepted without regression confirmation where feasible must be treated as certification defects.

---

**Previous file:** [cs_04_critical_system_stewardship.md](cs_04_critical_system_stewardship.md)

**Next file:** [cs_05_a_user_facing_capabilities.md](cs_05_a_user_facing_capabilities.md)
