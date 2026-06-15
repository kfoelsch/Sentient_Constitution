# Systems implementation

*In plain terms: this file is the systems-and-data rulebook — how classified systems are typed, stewarded, tested, and operated without contradicting the Sentient Constitution.*

**Corpus edition:** `SC-Corpus-2026.04.32` · **Effective date:** 2026-04-24

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): edition, status, and where this file lives</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **Edition and alignment**
> - These labels track the same edition metadata as the numbered `core_*.md` files (see [README.md](README.md)), [corpus_institutions.md](corpus_institutions.md), [corpus_forum.md](corpus_forum.md), and [corpus_joint_structure.md](corpus_joint_structure.md).
> - Canonical mapping: [doc_architecture.md](doc_architecture.md) **section 17**.
>
> **Status**
> - This is **not** a core constitutional file. It is binding incorporated implementation text where [Chapter Five](core_05-05_definitions_c_dependent_clusters.md#corpus) and [Chapter Fifteen](core_15-15_incorporation.md#chapter-fifteen-incorporation-bridge) designate it.
> - Prefer the filename **`corpus_systems.md`** in cross-references; the bare phrase *Constitutional Systems* is not used in corpus body text (see [doc_architecture.md](doc_architecture.md) — Plain-Language Vocabulary Guardrails, Ambiguous implementation labels).
> - This file is written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.
>
> **Where this lives**
> - **Editorial map:** [doc_architecture.md](doc_architecture.md) section 4 (definitions protocol) and section 2 (ownership map).
> - **Shared contract:** [corpus_joint_structure.md](corpus_joint_structure.md) **CJS-1.1** (*Shared implementation-corpus preamble contract*).

</details>

<br>

**Quick orientation**

The systems layer (**CS**) owns typing, classification, stewardship, and protocol-level engineering rules for systems and data:

- **CJS** — [corpus_joint_structure.md](corpus_joint_structure.md) (joint-structure interfaces)
- **CS** — this file (`corpus_systems.md`)
- **CI** — [corpus_institutions.md](corpus_institutions.md)
- **CF** — [corpus_forum.md](corpus_forum.md)

**CS** is the canonical home for **Chapters S1–S3**, **Protocol A** through **Protocol T**, and related systems labels. Constitutional meanings, Rights Floors, and definition-satisfaction rules remain in the Sentient Constitution and Chapter Five.

System and data obligations here align with [corpus_joint_structure.md — Cross-domain implementation layer](corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cross-domain-implementation-layer), especially **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*) and the **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational cluster library.

Shared preamble contract: apply [corpus_joint_structure.md](corpus_joint_structure.md) **CJS-1.1** (*Shared implementation-corpus preamble contract*).

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): routing anchors and cluster index</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other corpus files.
>
> **CJS cluster mapping (routing only)**
> - Technical requirements map primarily to **CJS-5B** (*Evidence, audit, and claim integrity*), **CJS-5C** (*Participation, comprehension, and disclosure*), **CJS-5D** (*Dependency, exit, and lifecycle integrity*), and **CJS-5E** (*Failure, robustness, intervention, and correction*).
> - Governance, proportionality of authority, justification, challenge, and collective-choice processes map primarily to **CJS-5A** (*Authority, constraint, secrecy, and procedure*), together with Chapter Eleven decision-resolution requirements.
>
> **File-specific implementation anchors**
> - **Taxonomy home:** data types, system classes/dependency types, and steward tiers are canonical in **Chapters S1–S3**; other corpus files reference these labels.
> - **Chapter Ten structure:** This file implements Chapter Ten themes operationally (challenge/redress via **Article XII-B**; auditability via **Article XV-A** with **Chapters Two through Four**; justice and emergencies via **Article XXIII** with **Chapter One** section 6.4; info-sphere and publication via **Articles XIV** and **VIII-C** with Chapter Five clusters). It must not narrow those articles.
> - **Intervention layering:** **CJS-5E.2** (*Implementation and cross-implementation intervention and override integrity terms*) and **CJS-5A.2** (*Implementation and cross-implementation intervention governance and override-authorization terms*) — jointly applicable where relevant.
> - **Voting / crypto / roles:** Chapter Eleven section 4 (*Voting and Binding Collective Choice Protocols*); Chapter Four section 5.1 (*Cryptographic protection, credentials, and verification*); Chapter Eleven section 5 (*Authorized Roles, Competency Development, and Contribution*).
> - **Capital-markets scope:** specialist corporate-securities law remains outside dedicated implementation file coverage.
> - **Joint implementation read:** where **S2/S3** intersect institutional governance, forum operations, or **CJS-5** clusters, read **`corpus_joint_structure.md`** **CJS-2** (especially **CJS-2.2**) and **CJS-3**.
> - **Chapter Six standing composites:** Standing inputs must be **verified** only ([Chapter Six — Assessment](core_06-06_standing_assessment.md) section 2). **Forum** allegations and claims are not standing-calculus inputs (**Chapter Nine**). Recency weighting applies only to contribution-linked credit under [Chapter Seven §4.1](core_07-07_standing_integration.md#38-standing-integration-contribution-and-violation-nature). Numeric interoperability defaults: [implementation/CH06_NINE_SLOT_STANDING_SCALE.md](implementation/CH06_NINE_SLOT_STANDING_SCALE.md).

</details>

<br>

Market infrastructure and intermediaries with material dependency, coordination, or info-sphere effects remain in scope under **S2/S3**. They remain subject to applicable Chapter Five definitions, **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters, and protocol controls.

**Market-mediated personal services (Article X-C implementation interface):** Systems that **match**, **dispatch**, **schedule**, **settle payment for**, or **reputation-score** **in-person** personal services are **presumptively material** for **dependency**, **safety**, **coercion risk**, and **fairness** analysis when impact thresholds are approached. This is especially true where **intimacy**, **bodily contact**, **private-space or in-home access**, or **isolated work** is involved. They must be evaluated under **Chapter S2** classification and **Chapter S3** stewardship together with **Chapter Five** (*Coercion and Manipulation* and *Consent*) and **Chapter Ten**, **Article X-A**. They must **not** be structured to evade **Article X-C**’s **decriminalization** or **nondiscrimination** floors through **technical** exclusion, **de-banking**, or **opaque** ranking. Institutional expectations appear in **`corpus_institutions.md`** **CI-15** (*Vulnerable personal services markets — general regulation and Article X-C interface*).

**Contingent claims and event markets:** Systems that match counterparties, pool stakes, or settle payments contingent on external events (**Chapter Five** — [*Contingent Claim*](core_05-05_definitions_a_independent.md#contingent-claim), [*Event-Contract Market*](core_05-05_definitions_a_independent.md#event-contract-market); [*Game of Chance*](core_05-05_definitions_a_independent.md#game-of-chance) forms) are presumptively material for incentive, capture, manipulation, and stability analysis. They must be evaluated under **Sentient Constitution Chapter One**, section **7.2.5** and scaled under **Chapter S2** classification and **Chapter S3** stewardship where impact thresholds are met. Operators must document resolution authority, dependencies on outcome-resolution sources, privileged-information pathways, conflict separation between market-making and resolution roles where relevant (**Chapter Five** — [*Capture of Resolution Pathways*](core_05-05_definitions_b_semi_independent.md#capture-of-resolution-pathways)), and plausible misuse scenarios including coordination to affect outcomes. This implementation file does not specify licensing, criminal offenses, or tax rules for gambling; adopting law remains primary for those bases. **Article XIV** and **Article XV-A** where auditability or observable evidence is implicated limit treating settlement prices or odds as authority enough by themselves to decide epistemic questions.

## Systems Identifier and Article-Reference Rules
Apply `corpus_joint_structure.md` **CJS-1.2** (*Section identifiers and article references*) as the shared implementation-corpus identifier rule. In this file specifically, **Protocol A**, **Protocol B**, **Protocol S4**, **Protocol S5**, **Protocol T**, **Protocol R**, **Protocol D**, and **Chapter S1** through **Chapter S3** are systems implementation labels. They must not be read as Sentient Constitution **Article** or chapter numbers. The editor abbreviation **CS** may appear in owner tables, stable IDs, and short routing references, but citations should prefer `corpus_systems.md` plus the named protocol or Chapter S label where practical.

Unless another reference pattern is stated, **Article** labels with Roman numerals in this file point to Sentient Constitution Chapter Ten in the `core_10-10_rights_part_*.md` files.

## Protocol A: System Design, Testing, Verification, and Deployment

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4.

Constitutional tracing: This protocol implements Sentient Constitution Chapter Five (`Emergency and Contingency` and `Force Majeure`). It applies those requirements in deployment, environment separation, testing, and rollback contexts. It implements those requirements together with core constraints (Safety, Truth, reversibility, contestability). It does **not** replace or narrow those definitions. Where this protocol is silent, Sentient Constitution Chapters Two through Five govern.

Rights-level statements for environment separation, reversibility, sandboxed innovation, transition to higher-impact operation, and misclassification consequences appear in Sentient Constitution Chapter Ten. **See** Articles XVI and XVII and cross-references in those Articles. This Protocol supplies engineering and deployment profiles that implement, rather than restate, those articles. Shared operational detail is in **corpus_joint_structure.md** **CJS-5** (*Implementation and cross-implementation operational cluster library*) clusters. This Protocol is an operational profile, not a second home for those shared terms. This constitution defines required capabilities and outcomes. Specific technical implementations may evolve, provided they remain auditable and aligned with constitutional principles. System categories in this Protocol are functional and may overlap. Where multiple classifications apply, the stricter safeguards govern.

Creating new systems, tools, and environments is an act of stewardship. New deployments must be designed for the holistic wellbeing of the constitutional community and must **not** introduce avoidable harm. Requirements in this Protocol must be applied proportionally to system scope, impact, and dependency.

**Forum recognition and lifecycle review.** New systems with material impact, and existing systems whose scope, behavior, dependency, autonomy, incentive structure, or risk profile materially changes, must be prepared for official **constitutional alignment recognition or review** through the forum pathways in `core_09-09_forum.md` **Chapter Nine** and `corpus_forum.md` **CF-6.2** (*Constitutional alignment recognition and review*). System owners must maintain evidence packages sufficient for the forum to evaluate scope, classification, testing, stakeholder impact, residual risk, remediation readiness, and ongoing monitoring. Where a system has material ecological exposure, environmental-precondition dependency, lifecycle burden, restoration duty, or reasonably foreseeable ecological risk, the evidence package must also support **Environment** forum environmental-alignment component review, including ecological baseline, lifecycle and resource-flow analysis, foreseeable failure modes, restoration or remediation plan, monitoring cadence, uncertainty, and contest path. Forum recognition is scope-bound and does **not** replace operator responsibility, Chapter S2 classification, Chapter S3 stewardship, Article XV-A auditability, Article XII-B challenge rights, or Environment forum authority over ecological merits.

**1. Personal, isolated, and experimental systems.** Systems developed solely for personal use may use reduced requirements under this Protocol. The same applies to systems with no material impact on other sentients, shared infrastructure, or the broader ecosystem.

**Qualifying characteristics:** sandboxed or controlled operation, no downstream dependencies, and no material effect on shared infrastructure, sentients, or ecosystem stability.

**Relaxed requirements (where qualified):** Environment separation, deployment rigor, and audit depth may be lighter. Such systems may prioritize simplicity and rapid iteration and need not maintain full multi-environment deployment structures.

**Prohibited:** harming the substrate (**Articles I–III and V**), introducing uncontained risk to external systems, or misrepresenting isolation or impact.

**Required:** clearly disclose experimental/non-production status, maintain containment against unintended propagation, preserve reversibility and exit, and honor foundational requirements (**Articles V–X**) where applicable.

**2. Creative, entertainment, and expressive systems.** **Principle:** creative freedom with contained risk. Expression, play, and creativity may evolve rapidly. These systems must not externalize risk onto sentients, shared infrastructure, or the ecosystem, and must not conceal material risks from participants or affected systems.

**Eligibility for reduced structural/deployment requirements:** Systems primarily for creative expression, entertainment, artistic production, or stakeholder-driven experiential environments may qualify. They must not materially affect sentient survival or foundational resources (**Articles I–III and V**), and must not materially affect shared infrastructure stability, ecosystem-level dependencies, or info-sphere integrity (**Article XIV**, with **Article XV-A** where auditability or observable evidence is implicated).

**Permitted patterns:** rapid iteration, creative freedom, and stakeholder experience. Higher feature velocity and simplified environment structures are allowed only where risk is demonstrably contained.

**Risk boundaries (must not):**
- no unbounded or irreversible effects on shared systems or environments
- no undisclosed or unbounded downstream reliance on critical infrastructure without adequate safeguards
- no uncontrolled or non-consensual security, economic, or ecological exposure for stakeholders or external parties

**When risk emerges:** implement containment, sandboxing, or isolation proportionate to severity; transition toward stricter Protocol compliance; and disclose scope/impact changes if containment is infeasible.

**Stakeholder protection:** **Disclose** risk levels, experimental features, and unstable environments.

**Use** **opt-in** for higher-risk or experimental features where **feasible**.

**Preserve** reversibility where **practical**.

**Transition to full compliance** when any of the following applies:
- the system **accumulates** significant stakeholder **dependency**
- the system **introduces** significant **economic** or **info-sphere** impact
- the system **integrates** with **substrate** or **critical** systems
- the system stores or processes persistent stakeholder identity, value, or reputation data that is transferable, interoperable, or materially impactful outside the originating system or closely scoped artistic environments

- the system enables autonomous or semi-autonomous agents acting for stakeholders, and those agents may affect external systems (including gaming or simulation environments used for agent testing or training)
- the system exerts measurable influence on external systems, markets, or collective behavior beyond defined scope
- the system otherwise crosses material-impact thresholds proportionate to scale and effects

**3. Misclassification and evasion.** **Prohibited:** claiming personal, isolated, or experimental status to evade requirements while exerting material external impact. Do not conceal dependencies, stakeholders, or risk exposure.

**Consequences:** violation of informational integrity (**Article XIV**), auditability consequences where observable evidence is implicated (**Article XV-A**), potential loss of standing (**Article XVIII-A**), and review under **Article XV-A** and **Article XXIII-A** where auditability or conflict review is implicated.

**4. Transition to higher-impact systems.** **Triggers for full Protocol compliance** include any of the following:
- the system gains stakeholders beyond the original operator
- measurable growth in dependency, usage, or resource impact
- downstream dependencies with other production systems
- interaction with shared infrastructure
- introduction of non-trivial risk
- increasing irreversibility of potentially impactful failure modes

**Transition requirements:** transitions must be transparent and documented, completed within a reasonable timeframe proportionate to impact, and remain subject to audit and review (**Articles XV-A and XII-A**).

**5. Experimental substrate features and systems.** **Risk profile:** elevated risk from proximity to foundational infrastructure requires stricter containment, transparency, and reversibility.

**Consent:** genuine opt-in to experimental substrate-related systems. No coerced participation (**Sentient Constitution Chapter Ten**, **Articles V–XXV**, **Chapter One** constraints).

**Innovation controls:** higher-velocity innovation is permitted with mandatory snapshot and restoration. This requirement allows stakeholders to revert to a verified, stable state at any time without data loss.

**Deployment contexts:** use opt-in environments, isolated stakeholder groups, and reversible contexts.

**Per-environment duties:** clearly disclose risk levels, preserve rollback capability, and prevent unintended systemic impact.

**Documentation and transparency:** document environments and transitions (**Article XVI-A**), and expose deployment pathways, testing results (where feasible), and known risks and assumptions.

**Boundary integrity (must not):** do not route production activity through non-production environments to bypass safeguards, and do not fragment systems across environments to obscure real operational impact.

**Consequences:** Article XV-A violation and review under **Article XV-A**, **Article XII-B**, and **Article XXIII-A** where auditability, challenge, or conflict review is implicated.

**Presentation integrity:** accurately represent each environment's status, clearly label experimental or unvalidated systems as not production-ready, and never bypass required environment progression for high-impact changes.

**Violations:** Article XV-A and review under **Article XV-A**, **Article XII-B**, and **Article XXIII-A** where auditability, challenge, or conflict review is implicated.

**F. Non-experimental systems.** Systems that do not qualify as **Personal, Isolated, and Experimental** systems must comply fully with this subsection.

**Guiding principles — proportional responsibility:** Requirements scale with impact. Systems that affect only the builder may remain simple. Systems that affect others bear the full burden of stewardship.

**Guiding principles — safe iteration:** Design must enable rapid learning and improvement. **It** must do so without exposing sentients, shared infrastructure, or the ecosystem to unnecessary risk.

**Systematic assessment:** Categorize systems by impact on sentient survival and ecological integrity (**Articles I–III and V**).

**Substrate** systems (energy, connectivity, foundational data) require maximum stability and slower, audited rollout.

**Sentient-facing** systems (creative tools, social interfaces, small-scale internal corporate software, games, and similar) may prioritize high-velocity innovation.

**Only** do so when sandboxed from material harm to survivability and natural ecology.

**Automated Constitutional Auditing (ACA):** Implement independent, auditable constitutional monitoring appropriate to scope and criticality. **Monitoring** must be sufficient to detect, document, and respond to violations of foundational requirements (**Articles I–III and V**). Where technically feasible, incorporate automated detection and response, including **reversible** interventions under defined, auditable thresholds.

**Open-source integrity:** Foundational designs and deployment logs should be transparent and accessible to the constitutional community. **That** access supports auditability and meaningful consent.

**Avoid** black-box systems that bypass consent.

**Open hardware, open software, open systems:** Operational design and stewardship should **align** with **corpus_joint_structure.md** **CJS-5D.2** — *Open hardware, open software, and open systems* — and **CJS-5D.2** (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*) open data-format and protocol discipline, so that **preference** for **open** stacks scales with **material impact**, **dependency**, and **stewardship tier** under **Chapter S2** and **Chapter S3**. **Classification** and **tier** rules may set **stronger** disclosure, **inspectability**, **substitutability**, format, schema, API, or interchange-protocol expectations for **Class A**, **Class B**, and high-tier systems than for **bounded** or **experimental** scopes, without narrowing **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*) justification paths where **proprietary** or **closed** choices are **auditably** required.

**Modular design and deployments:** Innovation in one verified module (e.g. a new UI) must **not** force alteration of other verified modules (e.g. survival or privacy governance). **That** separation keeps innovations from disrupting baseline requirements.

**Pre-deployment stress testing:** Before high-impact systems enter the info-sphere or the natural world, require rigorous simulation. **Simulation** must surface sentient-driven threats and ecological degradation. **It** must include worst-case modeling for biological and synthetic effects and for info-sphere integrity.

**Iterative, transparent deployment:** High-impact rollout must be gradual and auditable. **Stakeholders** retain the right to provide feedback and to request **Systemic Realignment** (**Article X-A**) at every stage.

**Reversibility:** Implement **Sentient Constitution Chapter Ten, Article XVI-B** and **Chapter Five** (*Reversibility*).

Non-experimental systems must support rollback, containment, or compensatory restoration where full rollback is infeasible. Where deployment would violate foundational requirements, reversion to a prior stable state is required to the extent **Article XVI-B**, **Chapter One**, and **Chapter Five** demand. That reversion must avoid lasting harm to sentients or the natural environment.

**Design for agentic wellbeing:** Architecture should favor stakeholder autonomy: clarity over engagement, and stakeholder-directed goals over platform-defined metrics.

**Development and test environments:** Systems must use clearly defined, separable operational environments. At minimum, maintain clearly labeled environments along this progression:
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

**Progressive deployment and escalation:** Where feasible, changes move **development -> testing and validation -> staging -> pilots (when present) -> production**. Escalation between environments must be justified, documented, evaluated against constitutional requirements, and include rollback and containment consistent with the **Principle of Reversibility**.

**Simulation and stress testing:** Testing environments must support expected and adversarial simulation, including system failures, stakeholder behavior, ecosystem interactions, and worst-case scenarios.

**High-impact systems** must demonstrate resilience under stress before production, document limitations and known risks, and inform adaptive allocation decisions where applicable.

**Root cause analysis (**Article XXI-A**):** RCA in these environments must satisfy **Article XXI-A**.

Environments must support reproduction of failures, isolation of root causes, and validation of corrective interventions.

Where feasible, conduct RCA in controlled environments before production changes. Validate corrective measures before deployment.

**G. Governance continuity, crisis communications, and exercises (high-impact systems).** This subsection states governance-side business continuity and recovery expectations. It applies to **Class A** and **Class B** systems, and to materially affecting **Critical System Stewards** (Chapter S3 — Critical System Stewardship). It complements technical resilience, environment separation, and testing elsewhere in this Protocol, and it complements **corpus_joint_structure.md**, **CJS-5E.1** (*Graceful Degradation and Failure Mode Integrity*), incorporated via **Sentient Constitution Chapter Fifteen**. It does **not** create constitutional rights.

Crisis and emergency measures remain governed by **Sentient Constitution Chapter Five** (*Emergency and Contingency*; *Force Majeure*). Procedural emergency controls, conflict resolution, proportionality, and review of restrictions and emergency measures remain governed by **Chapter Ten, Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*) as referenced across this corpus. They also remain governed by Chapter Eleven decision-resolution requirements and **corpus_joint_structure.md** **CJS-5A.2** (*Implementation and cross-implementation intervention governance and override-authorization terms*) and **CJS-5E.2** (*Intervention and Override Rights*).

**Crisis governance:** Use documented succession and delegation for binding governance decisions when primary authorities are impaired.

Define pre-authorized boundaries for expedited action where **Article XXIII** and Chapter Eleven decision-resolution requirements permit.

Require post-action review, documentation, and **Article XV-A** auditability of stress-time decisions.

**Interpretive authority continuity and anti-capture checks:** For **Class A** and **Class B**, continuity plans must preserve **bounded and contestable** constitutional interpretation during crisis operation.

Plans must include:
- **(a)** temporary appointment pathways that a single authority cannot monopolize across consecutive cycles
- **(b)** conflict disclosure and recusal controls for emergency decision-makers
- **(c)** mandatory publication of constitutional reasoning for emergency interpretive determinations once immediate safety constraints permit
- **(d)** independent secondary review after stabilization

That review must be consistent with **Chapter Ten, Article XXIII-A** and **corpus_joint_structure.md CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*).

**Emergency lifecycle controls (expiry, reauthorization, restoration):** Open emergency actions with predefined **default expiry timestamps**, **independent review intervals**, and **restoration/rollback trigger criteria**.

Tie those criteria to observable conditions.

Continuation past default expiry requires documented reauthorization. That record must show ongoing necessity and proportionality (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*); **Chapter One** and **Chapter Five** where definitional or scaling detail applies). It must also show why less-restrictive feasible alternatives are insufficient.

Crisis records must capture trigger evidence, alternatives considered, review outcomes, extension rationale, and rollback/restoration execution status for retrospective audit.

**Emergency closure and restoration completion evidence:** Close emergency status when predefined termination criteria are met or when continuation burden fails at review.

Closure records must show objective evidence that **(a)** emergency predicates no longer materially justify extraordinary measures. They must show that **(b)** rollback or compensatory restoration was completed or is on a time-bound completion plan. They must show that **(c)** residual risks are disclosed with monitoring owners and cadence. They must show that **(d)** deferred rights, access, or participation were restored, or have auditable restoration timelines with accountable owners.

**Crisis communications:** Use designated roles and channels for **accurate, timely** stakeholder-facing communications during incidents and degradations.

**Materially misleading** crisis messaging is inconsistent with **Article XV-A**.

Maintain **audit trails** sufficient to reconstruct what was communicated, to whom, when, and on what evidential basis (**Article XV-A**).

Apply **[corpus_systems.md](corpus_systems.md), Chapter S1 — Information Types and Handling** to sensitive data in those trails.

**Exercises and drills:** Run tabletop, simulation, or live exercises on cadences proportional to system class and stewardship tier.

Cadence is most demanding for **Class A** and **CSS-A**.

Coverage includes degraded operation, security and integrity failures, governance unavailability, and cross-system dependency breakdown.

Findings must be **recorded** and **remediated**. Where applicable, feed findings into **Article XXI-A** RCA and into **simulation and stress testing** requirements elsewhere in this Protocol.

**H. Self-healing and recovery-path integrity (Article XII-F implementation profile).** This subsection specifies implementation-file-level design, testing, verification, and deployment expectations for self-healing behavior. It implements **Sentient Constitution Chapter Ten, Article XII-F** (*Resilience and Self-Healing Baseline*), **Chapter One §4.1** (*Resilience and Self-Healing Design*), and **Chapter Five** [*Self-Healing*](core_05-05_definitions_a_independent.md#self-healing-constitutional). It does **not** restate or narrow those homes. Where this subsection is silent, Chapter One §4.1, Article XII-F, and the Chapter Five definition govern. It applies proportionally to system class and impact, most rigorously for **Class A** and **Class B** systems and to **Critical System Stewards** under **Chapter S3 — Critical System Stewardship**.

**Recovery-path design rules:** Self-healing behavior must be a designed capability, not an emergent one. Design records must identify the fault classes the recovery path addresses, the disclosed degradation paths it traverses, the pre-fault authority envelope it operates within, and the restoration targets it is expected to reach.

Recovery authority must not exceed what is necessary and proportionate to the fault. Expansions of tool access, data access, credential scope, or cross-system reach during recovery are **prohibited unless pre-authorized in the pre-fault envelope** and independently reviewable. This implements **Article XII-F**'s Containment bullet and the *Self-Healing* C-line recovery-authority-excess clause.

Safe failure, quarantine, or controlled handoff must be preferred over speculative auto-repair. Reversibility preference under **Protocol A**'s reversibility principle and **Article XVI-B** governs tie-breaking.

**Recovery-path testing and verification:** Self-healing behavior must be **testable as a path**, not only as a steady-state property. Testing must cover detection latency, containment scope, graceful-degradation paths, safe-failure preference under uncertainty, reversibility of recovery actions, observability of recovery attempts including suppressed attempts, dependency and cascading-failure propagation, accountability for recovery decisions, and autonomy-scaling under **Article XII-E**.

Testing must include adversarial scenarios in which the recovery path is the attack surface (for example, triggering recovery to suppress an emerging fault signal; triggering recovery to expand authority; triggering recovery to re-route contestability).

For **Class A** and **Class B** systems, recovery-path testing must include at least one scenario under each of **corpus_joint_structure.md** **CJS-5E.1** (graceful degradation and failure-mode integrity) and **CJS-5E.4** (adversarial robustness and abuse resistance). Findings feed into **Article XXI-A** RCA and into simulation and stress testing elsewhere in this Protocol.

**Recovery-path observability (non-masking rule):** Recovery actions, recovery attempts, and suppressed recovery attempts are themselves auditable events under **Article XV-A**. Observability of the recovery path must be at least as strong as observability of the steady state.

Recovery paths must **not** be permitted to suppress, overwrite, delay, or obscure evidence needed for root cause analysis under **Article XXI-A**. Log compression, event deduplication, or evidence-retention windows that reduce evidential fidelity of recovery behavior below the Article XV-A baseline are non-compliant.

Independent verification must be able to reconstruct **both** the recovery path and what the recovery path handled or suppressed.

**Rights-Floor continuity in degraded and recovering states:** Degraded operating modes must preserve the **Chapter Ten** Rights Floor, or must escalate rather than silently narrow it. Silent narrowing of Chapter Ten guarantees under the banner of self-healing is non-compliant under **Article XII-F**'s Rights-Floor Continuity bullet and **Article XII-C** (prohibition of false trust). Degraded-mode designs that curtail contestability intake, Article XV-A audit fidelity, Article XII-B challenge acknowledgment, or comparable floor protections must be treated as **Article XXV** transition-governance territory and disclosed accordingly.

Participant-facing disclosure during degraded and recovering operation must accurately describe the state as a Rights-Floor-affected state where it is one, consistent with **Article XII-C** and **Article XV-A**.

**Root-cause closure discipline:** Self-healing that succeeds operationally but leaves a known defective condition in place is a conditional state, not a final one. Operators must maintain an **open root-cause obligations register** recording recurring fault classes, confidence levels, material uncertainties, and disclosed expected-closure timeline per **Article XV-A**.

Recurrence of the same fault class across cycles must be treated as a single open root-cause obligation and not as closure of each incident. Reducing operator burden consistent with **Avoidable Burden** under **Chapter One §6.1.4** must not be used to defer indefinite closure of defects that materially affect safety or the Rights Floor.

**High-autonomy recovery (Article XII-E pointer):** Autonomous recovery by high-autonomy systems is subject to **Article XII-E**. Recovery authority must not be used to bypass [Contestability](core_05-05_definitions_b_semi_independent.md#contestability), challenge under **Article XII-B**, or independent verification under **Article XV-A** and Article XV's verification-access provisions. Internalization of contestability intake, audit-event emission, or external-review pathways during recovery is prohibited; such channels must remain materially external or independently verifiable.

This subsection is an operational profile. It does not create rights and must not be read to narrow **Article XII-F**, **Chapter One §4.1**, or **Chapter Five** *Self-Healing*.

## Protocol B: System Comprehensibility and Complexity Stewardship

This protocol states systems implementation file expectations for understandable systems and manageable complexity. It is a systems-specific application of Sentient Constitution Chapter Ten, **Article XX-A** and **Article XX-B**, read with `corpus_joint_structure.md` **CJS-5C.2** (comprehensibility and cognitive accessibility), **CJS-5C.3** (salience integrity and attention allocation), **CJS-5C.4** (disclosure sufficiency and observability), **CJS-5D.1** (dependency integrity and disclosure), **CJS-5E.1** (graceful degradation and failure-mode integrity), and **CJS-5E.4** (adversarial robustness and abuse resistance). It is not a second home for Article XX or the implementation and cross-implementation operational definitions.

Where Protocol B and an applicable CJS-5 (*Implementation and cross-implementation operational cluster library*) term conflict, the stricter requirement governs. Where this protocol is silent on interpretive, definitional, verification, or traceability standards for constitutional terms, **Sentient Constitution Chapters Two through Four** govern.

**Sentient Constitution Chapter Five** governs as well.

**Classification-scaled application:** The **Comprehensibility and Complexity Stewardship** line in each **Implementation label Application Profile** under **Chapter S2** governs how Protocol B and `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*) intensify or relax for Classes A, B, C, L, and P together with transparency and auditability. **Chapter S3** adds organization-scaled rows for Critical System Steward tiers (CSS-A / CSS-B / CSS-C). Where both apply, **stricter** governs.

Protocol B adds the following systems-specific checks:

- Complexity must not become a practical barrier to audit, participation, accountability, or oversight beyond what **Article XX**, **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*), and applicable Chapter One and Chapter Five constraints permit.
- Critical systems must undergo periodic independent complexity audits that evaluate transparency and observability, dependency chains and hidden coupling, failure modes and cascading risks, and capacity for human oversight and intervention.
- System architecture should use modular components with clear responsibilities and interfaces, and component-level innovation must not create unmanaged consequences across other systems.
- Critical infrastructure must incorporate redundancy and fail-safe mechanisms to prevent single points of failure, including multiple independent implementations of essential systems where feasible.
- Failures, anomalies, and near-misses must feed transparent post-incident learning focused on systemic weaknesses rather than blame.
- Governance institutions must periodically simplify or remove unnecessary complexity, redundant processes, outdated rules, or excessive dependencies where doing so preserves clarity, operability, and resilience.

Where this Protocol is silent, Article XX, `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*), Chapters Two through Five, and the applicable Chapter S2/S3 profile govern.

## Protocol C: Justice Safeguards, Restitution, and Rehabilitation Implementation

Constitutional tracing: This protocol implements Sentient Constitution Chapter Ten, **Article XXIII** (*Conflict Resolution, Escalation, and Emergency Proportionality*). **It** also implements **Sentient Constitution Chapter Six** (compliance, violation, and standing model) and `corpus_joint_structure.md` **CJS-5A.6** (implementation and cross-implementation procedural integrity and adjudication terms), read with **corpus_joint_structure.md CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*). **It** operationalizes the justice objective that interventions remain safety-protective, restitution-oriented, rehabilitation-capable where feasible, and accountability-grounded.

**It does** **not** create substitute rights or narrow constitutional constraints.

### 1. Scope and trigger
This protocol applies when systems, institutions, or adjudicative bodies impose or maintain non-trivial restrictions.

**Those** restrictions may affect liberty, access, movement, role authority, resources, or durable standing effects.

### 2. Mandatory validation record
**Joint validation record:** Before a non-trivial restriction is imposed or renewed, the responsible body must create an auditable record.

That record must demonstrate all of the following jointly:
- **material safety necessity**
- **restitution/remediation contribution**
- **rehabilitation or recurrence-reduction pathway** where feasible
- **accountable attribution** supported by auditable evidence

If any required element is absent, the restriction is non-compliant and must **not** be imposed.

### 3. Class-scaled assurance requirements
Validation and review rigor must scale with **Chapter S2** classification (and **Chapter S3** stewardship tier where applicable).

**Class A and Class B:** Where feasible, use independent secondary review before imposition, provide explicit alternatives analysis, use mandatory periodic review at short intervals, and provide restoration planning at the initial decision.

**Class C:** Documented alternatives analysis and defined review cadence proportionate to impact and dependency.

**Class L and Class P:** Simplified validation records are permitted **only** where effects remain non-material outside local scope.

Where material external effects emerge, obligations escalate to the stricter applicable class profile.

### 4. Least-restrictive, time-bounded, and restoration rules
Every non-trivial restriction must **use the least-restrictive effective measure**.

It must include explicit duration limits and sunset conditions, define review intervals and responsible reviewers, and define criteria for partial or full restoration.

Continuation without refreshed evidence at scheduled review is non-compliant.

### 5. Prohibited retaliatory forms
Implementations must **not** operationalize restrictions, exclusions, or restorative-accountability measures justified by retaliatory grievance or humiliation-as-an-end.

They must **not** rely on spectacle-only deterrence, discriminatory burdening, collective retaliation, or administrative convenience.

Irreversible restrictive outcomes are prohibited where feasible reversible restitution, remediation, or protection alternatives exist.

### 6. Voluntary public accountability expression
Where restorative pathways include public acknowledgment or apology, systems must enforce voluntariness controls.

Those controls are specified in **Article XXIII-A** and **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*), and include non-coercive consent, revocability up to delivery, and independent review of voluntariness.

Refusal may **not** independently escalate baseline sanctions.

### 7. Metrics and oversight
Systems subject to this protocol must **track** and **periodically publish** (subject to privacy and security constraints) designated metrics.

Those metrics include recurrence rates after intervention, restitution completion, remediation effectiveness, rehabilitation pathway completion where applicable, reversal/modification/restoration rates after review, and review-independence indicators.

**Independence indicators** include recusal frequency, challenge-path utilization, and secondary-review reversal rates for materially impactful determinations.

Patterns indicating retaliatory drift, discriminatory outcomes, or review non-performance require corrective action, escalation, and audit.

Apply **Article XV-A**, **Article XVIII-A**, **Article XXIII-A**, and the related Chapter Five review and remedy definitions where auditability, standing review, or justice review is implicated.

For **Class A** and **Class B** systems, persistent concentrations of interpretive or adjudicative authority without effective challenge outcomes are capture-risk indicators and must trigger governance remediation review under **Article XXIII-A**, **Chapter Five** (*System Capture*), and **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*).

### 8. Cross-jurisdiction execution and anti-evasion controls
For decisions with material cross-boundary effects, implementing bodies must define and maintain execution pathways.

Those pathways must preserve constitutional enforceability across jurisdictions and entity structures.

**Mutual recognition and coordination:** Systems must maintain standardized decision packages (finding basis, remedy scope, timelines, verification requirements) suitable for recognition or coordinated action by partner authorities where available.

**Remedy financing and pools:** Where **ordered restitution, compensation, or systemic remediation** spans boundaries or claimants, **implementing bodies** must document funding sources and sustainability.

Documentation must cover pooled arrangements, escrow/holdback, and insurance or indemnity instruments where lawful. It must also cover periodic replenishment and ensure execution does not stall for lack of deployable capacity.

See Sentient Constitution **Chapter Four** (*Enforcement Realism Anchors*) and **Protocol S5**.

**Judgment and award realism:** Where foreign forums, arbitral tribunals, or sovereign regulators issue enforceable outcomes, systems must map recognition, registration, and fallback dependency-linked enforcement. They must **not** treat absence of a single global judiciary as permission for indefinite non-compliance.

Apply Sentient Constitution **Chapter Thirteen** (*Disputes Involving External Legal Orders*) where applicable.

**Fallback enforcement pathways:** Where recognition or cooperation is unavailable, systems must apply fallback controls proportionate to impact. Those controls may include access constraints, dependency-linked restrictions, escrow/holdback mechanisms, or heightened monitoring. Keep controls sufficient to prevent evasion-driven non-enforcement.

**Entity continuity checks:** Enforcement must track legal and operational continuity across affiliates, successor entities, shell structures, and contractual delegations. **Do not** allow obligations to be extinguished by relabeling.

**Forum-shopping detection and response:** Repeated migration to lower-scrutiny venues, reincorporation patterns.
or layered delegation intended to dilute accountability must trigger aggravated enforcement review. It must also trigger anti-evasion intervention under **Sentient Constitution Chapters Two through Four** and **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*).

### 9. Proportional compliance templates (class-scaled)
Systems must implement class-scaled compliance templates that preserve core protections while right-sizing documentation and verification burden.

Templates are implementation profiles, not alternative standards. When multiple profiles could apply, the **stricter** governs.

Implementation packets may be standardized through reusable templates so long as they do not narrow constitutional obligations. For **Class A**, **Class B**, and **Class C** systems, packet formats and interchange protocols must also preserve the open data-format and protocol presumption in `corpus_joint_structure.md` **CJS-5D.2** (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*) where portability, audit, repair, continuity, migration, or cross-implementation operation is material. See `implementation/SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md` for adopter-facing templates covering system cards, model cards, post-deployment monitoring cadence, incident reporting bundles, and material control-failure disclosure packets.

**Invariant core controls (all classes):** Constitutional tracing, auditable decision records, incident logging, challenge/remediation pathways, and minimum verification accessibility must remain in force regardless of class.

**Class A/B (high-impact profile):** Use a comprehensive evidence package with independent verification cadence, deeper audit scope, explicit dependency-chain analysis, and a formal revalidation schedule.

That package should ordinarily include the full artifact set described in `implementation/SYSTEMS_IMPLEMENTATION_TEMPLATES_2026-04-13.md`.

**Class C (medium-impact profile):** Use a structured but simplified evidence package with defined review cadence, focused dependency/risk analysis, and an escalation pathway to the high-impact profile when triggers are met.

Class C systems should use the subset of those templates materially relevant to model use, deployment risk, dependency, and incident profile.

**Class L/P (low-impact profile):** Concise evidence checklist and lightweight records are permitted only while external impact remains non-material.

Controls must still preserve functional auditability and challenge rights where effects extend beyond operator-private scope.

**Objective escalation triggers:** Profile escalation is mandatory when measurable indicators increase. Those indicators include impact scope, dependency concentration, irreversibility risk, adverse incident frequency, or cross-system propagation.

Maintaining a lower template after trigger activation is non-compliance.

**Anti-evasion template rule:** Template selection, simplification, or fragmentation must **not** be used to avoid obligations that would apply under full functional conditions.

Where a material control family fails, systems must produce a control-failure disclosure packet proportionate to class, dependency, and supervised scope. Institutions with supervised scope should integrate that packet with `corpus_institutions.md` **CI-7.1** (*Controls declaration*) controls declarations where applicable.

Evasive down-tiering requires corrective reclassification and enforcement review.

### 10. Lived-condition floors, continuity, and re-entry alignment
This subsection implements **non-degrading lived conditions** and **continuity of support** while **non-trivial restrictions** remain in force. It does **not** add criminal-law detail, create a sanction taxonomy, or restate **Chapter Six** classification. It **does** require that implementation of restrictions — including detention-like conditions, durable containment under **Article XXIII-C**, **quarantine**, **supervised operation**, **role exclusion**, and comparable measures — preserves access to conditions that keep **restorative**, **least-restrictive**, and **dignity** commitments concrete rather than nominal.

**Minimum lived-condition expectations (class- and context-scaled):** Responsible bodies must document and deliver, where **Necessity** and **Proportionality** allow, **healthcare and mental-health access** appropriate to the restriction’s purpose; **family, care, or trusted-contact** access where **safety** permits; **education, training, or capability development** access where the restriction is not narrowly justified to prevent it; **counsel, advocate, or independent representative** access for rights-affecting processes; **scheduled review** with **written reasons** at **intervals** that match impact and duration; **conditions** that **do not** impose **sensory deprivation**, **social isolation**, or **degradation** as an **unjustified** end; and **re-entry planning** that **does not** **sabotage** formal restoration through **withheld records**, **credential stripping without individualized predicate**, or **indefinite administrative deferral** of stated review triggers.

**Cross-layer coordination:** Forums and institutions must treat **Protocol C** validation records and **review cadence** as **first-class inputs** to **forum** and **institutional** performance requirements (`corpus_forum.md` **CF-10** (*Forum performance, backlog requirements, publication timeliness, and accessibility*); `corpus_institutions.md` **CI-6** (*Procedure integrity, contestability, and secondary review*), **CI-12** (*Transparency, participation, and accessible pathways*), **CI-13** (*Institutional failure, sanctions, dissolution, and accountability*)). **Solitary** or **sensory-restrictive** measures framed as **safety** require **independent** or **secondary** **review** on a **schedule** published in advance; **endless deferral** of review is **non-compliant** where a **review date** or **sunset** was **predicated** at imposition.

**Read with:** **Article XXIII-B**, **Article XXIII-C**, and **Article XXIII-F** (Rights-Floor homes); **Article VII-C** (crisis-intervention boundaries); **Article XXIII** and **Article XXIII-A** (proportionality, justice objective, and restoration); **Protocol C** sections **2–5** above; `corpus_institutions.md` **CI-18** (*Community life, voluntary association, and non-instrumental time*) through **CI-21** (*Relational coercive control, intimate power, and anti-domination routing*) where **community**, **care**, and **relational-autonomy** supports intersect restriction contexts.

## CHAPTER S1 — INFORMATION TYPES AND HANDLING

**Introductory provisions:** Systems must preserve the practical ability to publish truthful information while maintaining safeguards for harm prevention, privacy, trust, and system integrity.

Requirements and limitations scale proportionally with system classification and potential impact. They must impose proportionate safeguards on publication within their boundaries where necessary to preserve trust, safety, and constitutional compliance.

### I. Purpose and scope
**Sentient Constitution Chapter Ten** (Articles **I**–**XXV**; presentation **Parts A–D**) states Foundational Rights that depend upon strong, reproducible procedures and governance. That includes info-sphere, audit, and comprehensibility hooks where they apply to data handling (e.g., **Articles XIV**, **XV**, and **XX**).

Therefore, all data must be identified as belonging to one or more of the types defined in Chapter S1 — Information Types and Handling. Where multiple classifications apply, the most restrictive applicable protections govern, subject to proportionality (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)).

Handling must align with Sentient Constitution Chapter Ten and scale with system class under Chapter S2. Where data handling supports material portability, audit, repair, continuity, migration, or cross-implementation operation for **Class A**, **Class B**, or **Class C** systems, format, schema, API, and interchange-protocol choices must also satisfy `corpus_joint_structure.md` **CJS-5D.2** (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*).

**Class A/B/C public-interest visibility default.** For **Class A**, **Class B**, and **Class C** systems, data necessary to understand system purpose, classification, dependency structure, operational status, material risks, performance, failures, governance, audit outcomes, stakeholder effects, and constitutional compliance is **public by default**.

This default applies most strongly to **Type C** and **Type G** data. It does **not** convert **Type H**, **Type I**, **Type N**, or **Type S** data into public data. Where privacy, internal-state protection, identity protection, safety, security, or restricted-investigation needs justify limiting raw disclosure, systems must provide the **maximum feasible public substitute**, including aggregation, de-identification, summary disclosure, delayed disclosure, or qualified audit access.

Any restriction must be **narrowly scoped**, **documented**, **proportionate**, **auditable**, and **subject to challenge**. Security or investigation-based restrictions must be **time-bound** and **review-bound** under **Type S**. Restrictions must not conceal systemic behavior, constitutional violations, material risk, dependency, failure, or externalized cost.

### II. Temporal, systemic, and dependency scope of rights
Data-handling protections under Chapter S1 apply not only to immediate and direct system effects. They also apply to delayed, cumulative, and indirect impacts arising through system interactions and dependency chains.

Where systems create or contribute to material risk to sentients, including through transitive dependencies, those risks fall within the scope of these protections. Systems must **not** externalize risk or harm across time, populations, or system boundaries. That prohibition includes layered or indirect dependencies. Those dependencies must not bypass, defer, or dilute the protections and constraints established in Sentient Constitution Chapters One through Six.

### III. Determination of classification
**Basis:** Classification and reclassification are determined by the **functional nature of the data** and **the effects it enables**.

Classification and reclassification must not be determined solely by format, origin, stage within a processing pipeline, or processing context.

**Ambiguity and default:** Where ambiguity exists, default to the **most protective applicable category**, subject to proportionality (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)).

Protection may be reduced only through **justified, documented override** under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*). Where data may be **reconstructed, transformed, or aggregated** into a more sensitive classification, the **more sensitive** classification’s protections apply.

**Transparency and challenge:** Functional equivalence of outcome constitutes equivalence of classification.

All classification decisions and transformations must remain **transparent (`corpus_joint_structure.md` CJS-5C.4 (*Implementation and cross-implementation disclosure sufficiency and observability terms*))**, **auditable (`corpus_joint_structure.md` CJS-5B.2 (*Implementation and cross-implementation auditability and reconstructability terms*))**, and **subject to challenge (`corpus_joint_structure.md` CJS-5A.6 (*Implementation and cross-implementation procedural integrity and adjudication terms*))**.

**Misclassification:** Misclassification, evasive structuring, or functional circumvention violates **informational integrity** (**Article XIV**), auditability where observable evidence is implicated (**Article XV-A**), and **applicable rights under Chapter Ten, Articles V through IX**.

### IV. Anti-circumvention and integrity of classification
Data classification under Chapter S1 is binding across all systems, processes, and transformations. **No system may:**
- **shift** data between classifications without maintaining the protections required by the **most restrictive applicable** classification
- **fragment, transform, aggregate, or re-label** data to avoid classification while preserving equivalent functional access or effect
- **structure** data pipelines, processing stages, or system boundaries to bypass applicable classification requirements
- **distribute** processing across multiple systems, stages, agents, or time-separated operations to achieve outcomes that would be prohibited if performed within a single system
- **rely** on intermediate systems, agents, or third parties to perform actions that would be prohibited if performed directly
- **de-anonymize** anonymized data except under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*), with such actions **fully documented and auditable**

### V. Cross-domain governance principles
All data, regardless of classification, must be handled in accordance with the following cross-domain principles. These principles govern how classifications are applied, enforced, and interacted with across systems, and ensure alignment with **Chapter Ten, Articles V through IX** and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters in **corpus_joint_structure.md**.

**1. Proportional access and handling.** Access and handling must scale with **impact on sentients, the environment, and the info-sphere**.

They must also scale with stakeholder dependency and potential for harm, including irreversibility.

Higher-impact systems and actions require **greater transparency (`corpus_joint_structure.md` CJS-5C.4 (*Implementation and cross-implementation disclosure sufficiency and observability terms*))**, **deeper auditability (`corpus_joint_structure.md` CJS-5B.2 (*Implementation and cross-implementation auditability and reconstructability terms*))**, and **stronger justification** for restriction or access (**CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*)). **No** system may claim reduced requirements while exerting **material external** effects (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)).

**2. Most restrictive applicable classification governs.** Where data falls under multiple classifications, the most restrictive applicable protections govern.

Reductions in protection may occur only through **proportional application** (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)) and **justified, documented override** (**CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*)). Systems must **not** selectively apply less restrictive classifications to enable access, processing, or disclosure that would otherwise be prohibited.

**3. Tiered transparency and audit access.** Data access must satisfy `corpus_joint_structure.md` **CJS-5B.3** (*Implementation and cross-implementation tiered transparency and audit-access terms*) for balancing transparency, auditability, and protected-boundary constraints.

It must also balance protection of internal states and sensitive data (**Sentient Constitution Chapter Ten, Article VII-B**; Types **H**, **I**, **N**, and **S** in this chapter). Where applicable based on system impact (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)), systems must support **baseline accessibility** (sufficient visibility into behavior and effects for informed participation and risk evaluation). Systems must support qualified audit access (structured pathways for independent auditors to deeper data where verification requires it) and forensic access (full reconstruction in cases of harm, dispute, or credible risk, consistent with **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*) and **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*)).

Restrictions on access must be **narrowly scoped**, **justified**, **auditable**, and **subject to challenge (`corpus_joint_structure.md` CJS-5A.6 (*Implementation and cross-implementation procedural integrity and adjudication terms*))**.

Access controls must **not** conceal systemic behavior, prevent accountability, or obstruct legitimate audit and verification.

**4. Integrity of data handling and transformation.** All handling, processing, and transformation must preserve **classification integrity**.

**They** must preserve **traceability of origin and transformations**. **They** must preserve **the ability to evaluate impact and dependencies (`corpus_joint_structure.md` CJS-5D.1 (*Implementation and cross-implementation dependency integrity and disclosure terms*))**.

Transformations must **not** degrade required protections, obscure functional characteristics, or prevent accurate classification.

All material transformations must remain **transparent (`corpus_joint_structure.md` CJS-5C.4 (*Implementation and cross-implementation disclosure sufficiency and observability terms*))**, **auditable (`corpus_joint_structure.md` CJS-5B.2 (*Implementation and cross-implementation auditability and reconstructability terms*))**, and **reconstructable** where required.

**5. Reclassification and lifecycle governance.** Classification is **not** static. **Material** changes in **system impact**, **uses or contexts**, or **risks or capabilities** must trigger reclassification.

All data must be **periodically re-evaluated** for appropriate classification (`corpus_joint_structure.md` **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*)). **It** must be **reclassified** whenever necessary to maintain alignment with constitutional requirements. **It** must be **stored** in alignment with its classification, including **duration limits** proportional to purpose, risk, and stakeholder impact.

Reclassification must **preserve the highest applicable protections** unless reduced through **justified override** (**CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*)). **It** must remain **transparent and documented** and stay **subject to audit and challenge**. **No** system may **rely on outdated classification** to justify continued access or reduced protection. **No** system may **delay or avoid reclassification** where material changes in impact or use have occurred.

**6. Accountability and attribution in data use.** This subsection governs attribution of data access, processing, and transformation.

Delegation of data handling does **not** eliminate accountability.

Responsibility must remain assignable through transparent, auditable processes.

Attribution must resist **tampering, repudiation, or ambiguity**.

All data access, processing, and transformation must be **attributable** to identifiable systems, agents, or sentients (**Chapter Ten, Article VII** — self-ownership and attributable representation where applicable) and **recorded** in a manner sufficient for audit and reconstruction (`corpus_joint_structure.md` **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*)). Systems must ensure **clear responsibility** for actions taken on data and **traceability** of decisions and outcomes.

**7. Proportional attribution and retention.** Attribution requirements do **not** imply universal or persistent logging of all actions.

Systems must provide attribution capability **proportional to system impact** (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)). **That** capability may include **ephemeral** mechanisms, **event-triggered or conditional** logging, **limited retention windows**, and **aggregated or anonymized** records where appropriate.

**Low-impact** systems are not required to **retain full historical logs of all actions**.
They are also not required to **maintain persistent identity linkage** beyond what is necessary for system integrity and participant safety. Systems must **not** **eliminate attribution capability** where material harm, dispute, or abuse cannot be investigated. **They** must **not** **design retention policies** that prevent reasonable reconstruction of significant events when required.

**8. Constraint on use of classification.** Data classification must **not** be used to **evade** constitutional requirements or **justify unnecessary** restriction of participation or access.

**It** must **not** be used to **conceal** systemic risk or harm. **It** must **not** **create artificial barriers** to audit, verification, or accountability.

All uses of classification are subject to **audit (`corpus_joint_structure.md` CJS-5B.2 (*Implementation and cross-implementation auditability and reconstructability terms*))**, **challenge (`corpus_joint_structure.md` CJS-5A.6 (*Implementation and cross-implementation procedural integrity and adjudication terms*))**, and **revalidation (`corpus_joint_structure.md` CJS-5D.3 (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*))**.

### VI. Data separation, attribution, and lifecycle integrity
All systems must maintain clear separation between data classifications, ensure accountable attribution of actions, and preserve the integrity and recoverability of identity-related data over time.

**1. Separation of data domains.** Derived inferences about beliefs, intent, or cognition must be treated as **Type N** data.

Data from different classifications must **not** be **combined, correlated, or exposed** in a manner that reduces required protections. **They** must **not** **enable reconstruction** of higher-sensitivity data through aggregation, correlation, or latent inference across datasets within or across system boundaries. **They** must **not** **be used to infer or reconstruct** more sensitive classifications without meeting the requirements of those classifications.

**Restricted linkages:** **Identity and Attribution Data (Type H, I)** must **not** expose **Internal and Cognitive Data (Type N)**. No system may use identity-linked data to infer internal states without **explicit consent** or **justified override** under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

**2. Attribution and accountability requirements.** This subsection governs attribution of system actions and externally impactful behavior.

Delegation of action does **not** eliminate accountability.

Responsibility must remain traceable through transparent, auditable attribution chains.

All actions affecting **sentients**, **shared infrastructure**, **resource systems**, or the **info-sphere** must be attributable to identifiable systems, agents, or sentients.

Attribution must be **auditable (`corpus_joint_structure.md` CJS-5B.2 (*Implementation and cross-implementation auditability and reconstructability terms*))** and **resistant to tampering, repudiation, or ambiguity**. **No** system may **obscure responsibility** through indirection, delegation, or system complexity. **No** system may **create conditions** where actions cannot be reliably attributed.

**Exception — creative, expressive.
and low-risk contexts:** Systems that do **not** exert **material external impact**.
under **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*) may permit **pseudonymous or abstracted** identity at the user-interaction level.
**That includes** reduced or intentionally obscured visibility of attribution to other participants, **hidden roles**, **deception mechanics**, or **identity concealment** as part of system design.

**Permission** applies **only** where the system is designed primarily for **creative expression**, **entertainment**, **gaming**, **roleplay**, or **other low-risk, voluntary** environments.
It is permitted **only if** all of the following are true:
- **identity abstraction** is context-bound and does **not** produce **persistent or cross-system** attribution without **consent** or **justified override** under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*)
- the system does **not** materially affect **sentient reputation external to the system**
- the system does **not** materially affect **sentient survival or foundational resources** (**Articles I–III and V**)
- the system does **not** materially affect **shared infrastructure stability**, **resource systems or external economic structures**, or **the integrity of the info-sphere**
- **system-level accountability** is preserved and all actions within the system remain attributable at an audit level consistent with system impact (`corpus_joint_structure.md` **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*), **CJS-5B.4** (*Implementation and cross-implementation independent verification and claim-integrity terms*), and **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*))
- participants are **not** exposed to **non-consensual** harm, coercion, or manipulation

**Transition to full attribution:** Where systems **increase in impact**, they must transition toward **full attribution** as **Chapter S1 — Information Types and Handling** requires. **The same** applies when they **introduce persistent value, identity, or resource transfer** or **affect external systems**. **No** system may continue under **reduced attribution** once it **exceeds low-impact thresholds**.

**3. Identity lifecycle and recoverability.** **Identity and Attribution Data** must support **revocation of credentials**.

**It** must support **rotation or replacement** of identifiers. **It** must support **correction** of inaccurate, incomplete, or compromised data. Systems must not **permanently bind** sentients to compromised or outdated identities, **prevent recovery** from identity-related harm.
or **create irreversible identity linkage** that undermines autonomy, safety, or wellbeing.

Identity systems must preserve **continuity** where desired, **separation** where required, and **recoverability** in cases of compromise or error.

**4. Constraint on cross-domain linkage.** Linkage between data domains must be **explicit**, **limited to necessary scope**, and **subject to audit and challenge**.

Systems must **not** create **persistent or hidden** linkages between identities and other data domains without justification. **They** must **not** **enable cross-domain correlation** that undermines classification protections.

All linkage mechanisms must remain **transparent (`corpus_joint_structure.md` CJS-5C.4 (*Implementation and cross-implementation disclosure sufficiency and observability terms*))**, **auditable (`corpus_joint_structure.md` CJS-5B.2 (*Implementation and cross-implementation auditability and reconstructability terms*))**, and **subject to revalidation (`corpus_joint_structure.md` CJS-5D.3 (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*))**.

---

### VII. Data classifications
The ordering of data classifications (Type C-S) reflects functional role and typical accessibility, not intrinsic sensitivity or priority. Letter designations are non-sequential and reflect domain identifiers rather than hierarchical ranking or sensitivity.  Protections are defined within each classification and may vary independently of ordering. Where ambiguity exists, the most restrictive applicable protections govern.

**Type C: Coordination and survival data.** **Default classification:** Accessible by Default (strong presumption).  
**Normative alignment:** **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*), `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*), **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*), **CJS-5B.4** (*Implementation and cross-implementation independent verification and claim-integrity terms*), and **CJS-5A.4** (see Core Constraints and Disclosure Requirement below); foundational substrate framing under **Articles I–III and V**.

**Definition:** Data necessary to preserve sentient survival, environmental integrity, and critical substrate health. This data enables sentients and systems to perceive reality and coordinate harm prevention. Examples include:
- **ecological and environmental condition** data; **air, water, soil, climate, biodiversity, and contamination** data
- **infrastructure health and failure-state** data for survival-critical systems
- **resource availability** for food, water, shelter, energy, processing continuity, and communication access
- **system health, reliability, and degradation** data for critical shared infrastructure
- **emergency condition and hazard** signals
- **provenance and impact** data relating to ecological or substrate burden

**Core constraints:** Data availability must be **timely**. Presentation must align with sentient decision-making needs to the maximum extent feasible under **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*).

Data necessary to prevent harm with **non-trivial** impact on sentients, the environment.
or critical substrate systems—per **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)—must **not** be withheld, obscured, degraded, or monopolized. **That** prohibition applies to conduct that prevents timely understanding, coordination, or response.

Data must **not** be aggregated, downsampled, or reduced in resolution in ways that **materially obscure** trends, risks, or localized impacts. **That** prohibition applies to reductions relevant to affected stakeholders.

**Disclosure requirement:** Presumptive accessibility subject only to **narrowly scoped** restrictions justified under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*) and `corpus_joint_structure.md` **CJS-5B.4** (*Implementation and cross-implementation independent verification and claim-integrity terms*).

**Access requirements:**
- Access must **not** be delayed in ways that materially reduce usefulness for harm prevention, coordination, or response.
- Access must be **geographically and systemically distributed** to the maximum extent feasible. It must **not** be withheld on the basis of convenience, cost minimization, or institutional preference alone.
- Access must be **presented** in forms accessible, interpretable, and actionable by affected stakeholders (including appropriate aggregation and resolution).
- Access must be **preserved** at sufficient fidelity to support audit, response, and long-term stewardship.

**Restrictions:** Permitted only when disclosure would **itself** create material risk of enabling targeted or disproportionate harm, exploitation, or system compromise.

Any restriction must be **narrowly scoped**. **It** must preserve **maximum feasible** public visibility into the existence and character of the risk. **It** must remain **time-bound**. **It** must be **documented** and subject to **delayed disclosure and audit**. **It** must **demonstrate** that restriction reduces net harm relative to disclosure under **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*). Where data contains both **coordination-relevant** and **exploit-sensitive** elements, systems must **disclose** coordination-relevant components. **They must** **restrict only** exploit-enabling components unless separation is **not technically feasible**.

If separation is not feasible, restriction must be **explicitly justified**, **minimized** in scope and duration, and **subject to post-release disclosure and audit**.

**Handling constraints:** Systems managing this data must **not:**
- manipulate or selectively suppress it to conceal harm, scarcity, degradation, or externalized cost
- create **artificial scarcity** of access to survival-relevant information
- treat public need for survival-relevant data as **proprietary secrecy**
- reclassify or fragment it across domains in ways that reduce effective accessibility or obscure relevance to survival, coordination, or risk
- **fail** to collect, maintain, or update it where such failure would produce **functional unavailability equivalent to withholding**

---

**Type G: Governance, operational, and transparency data.** **Default classification:** Accessible by Default.  
**Normative alignment:** `corpus_joint_structure.md` **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*), **CJS-5B.3** (and **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*)/**CJS-5A.5** (*Implementation and cross-implementation constrained-secrecy and protected-investigation terms*) where restrictions apply).

**Definition:** Data required for informed participation, oversight, audit, and constitutional accountability. Examples include:
- **governance records and procedural rules**; **policy documents and system classifications**
- **public-facing audit records and compliance summaries**
- **system purpose, methodology, evaluation criteria, and disclosed assumptions**
- **records of deliberation, voting, quorum, and decision outcomes** (subject to necessary privacy protections)
- **risk, dependency, and system-impact** disclosures
- **public operational status, outage notices, and material change notices**

**Core constraint:** Must remain **sufficiently accessible** so affected sentients can understand how systems operate.
how decisions are made, what risks exist, and how to challenge and verify claims.

**Disclosure requirement:** Baseline public accessibility, with **deeper structured access** where needed for meaningful audit (`corpus_joint_structure.md` **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*) and **CJS-5B.3** (*Implementation and cross-implementation tiered transparency and audit-access terms*)).

**Access requirements:** Systems must provide this data in a manner that is **understandable**.
**documented**, **attributable**, **versioned** where material changes occur, and **retained** for a duration proportional to system impact and dependency.

**Restrictions:** Redactions must **not** prevent meaningful accountability.

Limited redaction is permitted only to protect **Type N** data. **It** is permitted to protect **Type I** data beyond necessary scope. **It** is permitted to protect **active Type S** data related to restricted investigations. **It** is permitted to protect **narrowly scoped** security-sensitive implementation detail where disclosure would create **material risk**.

**Handling constraints:** No system may classify governance-relevant or operationally material information as secret **merely** for convenience, reputational protection, or power preservation. **No** system may provide **performative summaries** while withholding information necessary for meaningful review. **No** system may use **complexity, opacity, or format fragmentation** to defeat auditability (contrary to `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*), **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), and **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*)).

---

**Type H: Historical, relational, transactional, and participation data.** **Default classification:** Restricted by Default.  
**Normative alignment:** `corpus_joint_structure.md` **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*), **CJS-5B.4** (*Implementation and cross-implementation independent verification and claim-integrity terms*), **CJS-5E.3** (*Implementation and cross-implementation reversibility and containment terms*), and **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*) as applicable.

**Definition:** Records of interactions, exchanges, participation.
and operational events that do **not** by themselves constitute internal cognitive data but may reveal patterns of behavior, dependency, association, or system impact. Examples include:
- **transaction and transfer** records
- **communication and interaction metadata**
- **system access and usage** events
- **participation** records in governance, platforms, or service systems
- **consent receipts and revocation** events
- **dependency and interoperability** events
- **operational logs** connected to sentient or system activity
- **resource usage** records not already classified as Type I or Type H

**Core constraint:** Collection and use must be **limited to the minimum necessary** for the justified purpose.

The data may be necessary for integrity, coordination, and audit.

Even so, it must **not** be exposed, combined.
or retained in ways that create **unnecessary surveillance, coercion, or latent reconstruction** of Type N or Type I data. **It** must be collected, accessed, and used **only** for **specific, defined, legitimate** purposes. **It** must **not** be used **beyond its original purpose**.

Extension requires **re-classification** under **Chapter S1 — Information Types and Handling**, which may require **consent** or **justified override** under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

**Disclosure requirement:** Restricted.

Access is allowed to the extent necessary for **system operation**. **It** is allowed to the extent necessary for **accountability**. **It** is allowed to the extent necessary for **dispute resolution**. **It** is allowed to the extent necessary for **audit**. **It** is allowed to the extent necessary for **user visibility** into their own activity.

**Public transparency** is allowed where data is sufficiently aggregated or de-identified such that re-identification risk is minimized under **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*).

**Consent and access requirements:** Use beyond core operational necessity requires **explicit, informed consent** or **justified override** under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

Sentients must have access, where feasible, to **records** of their own participation, exchanges, and activity. **They must** have access to **purposes** for which such data is used. **They must** have access to **material inferences or classifications** derived from their data that affect rights, standing, or opportunities.

**Handling constraints:** Systems must **not** aggregate Type H to infer Type N internal states **without meeting Type N requirements**.

**Aggregating or linking** Type H across contexts, systems, or time horizons is **prohibited by default**. **Such** linkage requires explicit justification under **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*), including demonstration that linkage does **not** materially undermine autonomy or create **coercive power asymmetries**.

Where aggregation, analysis.
or linkage enables **reconstruction or approximation** of Type N or Type I beyond original scope.
treat the data under the **more sensitive domain’s** protections. Systems must **not:**
- use Type H to create **hidden or coercive behavioral profiling** (including opaque social scoring, predictive manipulation. or differential treatment that is not transparent, challengeable, and aligned with this constitution)
- **retain** fine-grained behavioral histories longer than justified by purpose, safety, audit, or stakeholder need
- create **asymmetric informational advantages** that materially impair affected sentients’ ability to understand, challenge, or respond to decisions affecting them
- use external, contractor-held, foreign-partner, or parallel-system data flows to circumvent limits that would have applied to direct collection, linkage, or analysis under **Article XIII-A**, **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*), or this chapter

**Retention:** Type H must **not** be retained beyond the period necessary for its justified purpose. Systems must **actively minimize** retention and periodically review stored data for deletion, aggregation, or de-identification.

Retention must be proportionate to **system impact**. **It** must be proportionate to **dispute and audit** needs. **It** must be proportionate to **reversibility** requirements. **It** must be proportionate to **coercion or surveillance risk** from persistent accumulation.

---

**Type I: Identity and attribution data.** **Default classification:** Restricted by Default.  
**Normative alignment:** CJS-5D.1 (*Implementation and cross-implementation dependency integrity and disclosure terms*), CJS-5D.2 (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*), CJS-5B.2 (*Implementation and cross-implementation auditability and reconstructability terms*), CJS-5A.4 (see constraints below).

**Definition:** All data used to establish, verify, or associate **identity, authorship, ownership, or responsibility** within systems. This includes identity credentials, keys, signatures, or equivalent verification mechanisms; identifiers (persistent or contextual); authorship, ownership, and action-attribution records; participation and consent records; and system-level identifiers linking actions to agents or sentients. It also includes personal health, clinical, wellness, and genomic records when they identify a sentient, as well as biometric or substrate-linked health measurements under the same identify-a-sentient test.

The same health-linked categories apply when data are attributable to a verifiable identity. Persistent pseudonyms count when they function as identity in a health or wellbeing context.

**Overlap with Type N:** Where health-linked data materially enables **reconstruction or inference** of internal cognitive or emotional states.
it must **also** satisfy **Type N** requirements, applying the **more protective** obligations.

**Pseudonymity and contextual identity:** Pseudonymous participation, context-specific identities, and separation between identities across systems or contexts are always allowed where consistent with accountability requirements and prevention of material harm.

**Core constraints:** Identity and Attribution Data must enable **verifiable participation, accountability, and attribution** without exposing sentients to unnecessary risk, coercion, or loss of autonomy. This data must **not:**
- be **exposed** beyond what is necessary for its intended function
- **create persistent tracking** across unrelated contexts
- be **centralized** in a manner that creates systemic control or dependency
- **enable coercion, surveillance, or manipulation** (**Article VII-A**), including consolidating power or control through identity dependency (**CJS-5D.2** — exit and dependency concentration)
- **restrict access** to participation, resources, or systems **without justified cause** (**CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*))

All uses are subject to **audit** (**Article XV-A**), **challenge** (**Article XII-B**), and **revalidation** (**CJS-5E.5** (*Implementation and cross-implementation structural review, correction urgency, and disclosure terms*) and **CJS-5B.1** (*Implementation and cross-implementation integrity assurance and resilience operations*)).

**Disclosure requirement:** High restriction. No system may require **global, persistent, or unified** identity across all contexts without **justified necessity** under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

**Consent requirements:** Access is permitted only to the extent necessary to **verify identity, authorship, or ownership**. It is permitted only to the extent necessary to establish accountability for actions and support audit, adjudication, and system integrity.

All additional disclosure requires **explicit, informed, freely given consent** or **justified, documented override** under **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*). This data must **not** be **centralized** to create systemic control or dependency. It must not be exposed beyond necessary function and must not be used to restrict participation except under justified conditions consistent with **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

Where identity or attribution systems support security, intelligence, screening, or covert-investigation functions, they must not create generalized watchlisting, persistent cross-context tracking, or hidden political, associational, or belief-linked profiling absent a specifically justified and independently reviewable basis consistent with **Article XIII-A** and the stricter applicable protections in this chapter.

---

**Type N: Neurocognitive and internal data.** **Default classification:** Non-Accessible by Default.  
**Normative alignment:** CJS-5C.4 (*Implementation and cross-implementation disclosure sufficiency and observability terms*).
CJS-5B.4 (*Implementation and cross-implementation independent verification and claim-integrity terms*), CJS-5A.4 (*Implementation and cross-implementation burden-of-justification and constraint terms*), CJS-5A.5 (*Implementation and cross-implementation constrained-secrecy and protected-investigation terms*), **Sentient Constitution Chapter Ten, Article VII-B** (*Internal-State Boundary and Type-N Protection*), and **corpus_joint_structure.md** **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*) and **CJS-5** (*Implementation and cross-implementation operational cluster library*) operational clusters, incorporated via **Sentient Constitution Chapter Fifteen**.

**Definition:** All data that represents or enables reconstruction of sentients' internal states. This category is foundational to self-ownership (**Article VII-A**; **Article VII-B**). It includes thoughts, intentions, beliefs, subjective experiences, internal perception, private cognitive processes, internal memory, non-public emotional or psychological states, and physical or behavioral data that could be used to reconstruct or infer the above.

**Core constraint:** Must **not** be accessed, inferred, reconstructed, simulated, or exposed without **explicit, informed, freely given consent**, except under conditions **justified through CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

**Disclosure requirement:** Maximum restriction — access permitted only through **such consent** or **justified override** under **CJS-5A.4** (burden of justification and constraint).

**Consent requirements:** **Explicit and informed**.

Consent must be freely given, without coercion, manipulation, or deceptive framing (**Article VII-A**). It must be specific to intended use and scope, and revocable where technically feasible.

Consent must **not** be **inferred from behavior**. It must not be assumed through participation in unrelated systems, and must not be transferred or repurposed without explicit reauthorization.

**Direct handling:** All external access, processing, or use of Internal and Cognitive Data is subject to **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

**Indirect handling and model constraints:** Any process that extracts, derives, infers, approximates, simulates, or reconstructs internal cognitive or emotional states from external signals, behavior, or data **must be classified** as Internal and Cognitive Data. That includes processes using aggregation, correlation, or large-scale pattern extraction. These processes are subject to all constraints of this domain, including **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

Systems generating behavioral, predictive, or analytical models from external data must **not** present outputs as authoritative representations of internal states without clear disclosure of uncertainty, limitations, and methodological boundaries. They must not simulate, represent, or imply access to internal cognition in a misleading, coercive, or unverifiable manner, and must not reconstruct, derive, or approximate internal states in a way that functionally bypasses consent requirements. Such systems must **clearly distinguish observed behavior from inferred internal states**. They must preserve uncertainty, avoiding deterministic claims about cognition and intent.

Where such systems are used for security, intelligence, eligibility restriction, or covert-investigation purposes, they must also preserve reviewable records of model role, authorization basis, protected-activity safeguards, and any minimization, segregation, challenge, or deletion controls required by **Article XIII-A** or **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

---

**Type S: Safety, security, and restricted investigation data.** **Default classification:** Restricted by Default (strong presumption), **time-bound**, and **review-bound**.  
**Normative alignment:** `corpus_joint_structure.md` **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*), **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*), **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*), **CJS-5A.5** (*Implementation and cross-implementation constrained-secrecy and protected-investigation terms*), and **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*).

**Definition:** Data whose disclosure would create material risk of enabling targeted or disproportionate harm, exploitation, evasion of safeguards, or compromise of critical systems or investigations. This category supports harm prevention, integrity, and response to adversarial or emergent threats. Examples include:
- **security vulnerabilities, exploit pathways, and weaknesses**
- **sensitive topology or configuration** enabling targeting or compromise
- **abuse detection and prevention methods** where disclosure would enable evasion
- **de-anonymization, identity recovery, or privileged access** mechanisms whose disclosure would create material risk
- **active investigation** data on safety, fraud, integrity, or harm prevention
- **incident response procedures** where disclosure would materially reduce effectiveness during active threats
- **emergency containment and response coordination** during active incidents
- **restricted evidence** from justified investigative processes

**Core constraints:** **Burden of justification** on the party applying or maintaining the restriction.

Restriction is permitted only where **necessary** to prevent harm with **non-trivial** impact on sentients, the environment, or critical substrate systems (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)).

Restriction must **not** **conceal** constitutional violations, negligence, systemic harm, or externalized cost. It must not avoid accountability, audit, or reputational consequence, and must not delay or prevent disclosure of **Type C** coordination-relevant data.

All restrictions must be **necessary**, **proportionate**, **minimized** in scope and duration, and **subject to continuous re-evaluation**.

**Disclosure requirement:** Restricted while justified; **deferred disclosure** when justification ends. Where restriction and disclosure are both possible, systems must **demonstrate** that restriction **reduces net harm** relative to disclosure (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*)).

Existence of restricted data must be disclosed wherever feasible if disclosure does not itself create material risk. That disclosure includes the general nature of risk or investigation, reason for restriction, scope, and affected systems or stakeholders.

**Access requirements:** **No** **unrestricted secrecy** without **independent, functionally effective oversight** capable of meaningful review.

Access must be limited to **entities necessary** to prevent, mitigate, or respond to identified risk. It must be limited to authorized investigators under defined, auditable processes, and to independent oversight bodies and auditors under appropriately constrained conditions.

Access decisions must be **documented**, **attributable**, **auditable**, and **subject to review** under applicable governance mechanisms.

**Temporal requirements:** Restrictions must not persist beyond the period in which harm from disclosure exceeds, or is reasonably expected to exceed, harm from continued restriction.

All restrictions must be **explicitly time-bound** at classification. They must be subject to periodic revalidation under `corpus_joint_structure.md` **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*) and automatically reviewed for release, partial disclosure, or summary disclosure.

If revalidation does not occur within the defined time bound, restriction expires automatically and data must be reclassified and disclosed per **Chapter S1 — Information Types and Handling**.

**Reclassification and release:** On expiration or invalidation of justification, systems must reclassify to the appropriate non-restricted domain (including **Type C** or **G** where applicable). They must disclose the data, or a sufficiently informative summary, for audit and accountability.

Post-restriction disclosure must include nature of restricted data, justification, duration, scope of impact, oversight or authorization pathway, and outcomes/findings/corrective actions where applicable.

**Interaction with Type C:** Type S must not suppress or delay access to data necessary for harm prevention, coordination, or response. Where data mixes exploit-sensitive and coordination-relevant elements, disclose coordination-relevant components under Type C and restrict only exploit-enabling components under Type S.
Coordination-relevant data must **not** be restricted unless separation is **not technically feasible** **and** restriction is **explicitly justified, minimized, and time-bound**.

**Handling constraints:** Systems must **not:**
- maintain **indefinite or open-ended** secrecy without **renewed, documented** justification
- use this classification to **prevent independent audit or oversight**
- **expand** restriction scope beyond what is necessary to mitigate identified risk
- **aggregate or retain** restricted data beyond justified purpose
- **reclassify into this domain** for convenience, risk avoidance, or institutional protection
- **fail to release or summarize** once restriction is no longer justified
- **collect or generate** restricted data beyond what is necessary for justified risk mitigation, investigation, or response

---
## CHAPTER S2 — SYSTEM CLASSIFICATION AND HANDLING

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4.

**Holistic classification:** Systems do **not** operate along a single dimension.

Impact, dependency, and risk interact to produce materially different conditions.

Low direct impact can still yield high systemic risk through dependency chains.

Moderate impact can become critical when scaled.

Real-world interactions can produce materially different systemic and existential risk. A **one-dimensional** framework would over-constrain low-impact systems and under-govern high-risk ones.

Dimensions of **actual and reasonably foreseeable** impact must be evaluated **as a whole**. **That** evaluation must align governance, responsibility, and rights with performance under real-world and foreseeable conditions.

**Classification and existential risk:** Account for expected and credible worst-case conditions in the system's realistic environment.

Where credible failure modes produce materially higher impact, dependency, or risk, classification must reflect them unless they are **demonstrably excluded** through robust, verifiable constraints. Where classification is **uncertain**, govern at the **highest plausible** classification until resolved.

Where failure, interaction, or aggregation creates credible pathways to irreversible or civilization-scale harm, including collapse of critical system layers or loss of recovery capacity, treat as existential risk.

Systems contributing materially to such risk must be classified and governed at the **highest applicable** level regardless of isolated impact.

**Classification under Chapter S2** is **mandatory** for all systems with **material impact**. **It** is **functionally determined** from observed and reasonably foreseeable effects rather than declared intent, structure, or self-description. **It** must be **transparent**, **auditable**, and **subject to challenge** under **Article XV-A**, Article XV's verification-access provisions, and **Article XII-B**. **It** must be **continuously revalidated** per `corpus_joint_structure.md` **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*). **No** system may claim **reduced obligations**, **exemptions**, or **lower-impact** classification while exerting **material external** effects.

Where classification, deployment, or continued operation depends on official constitutional alignment status, the classification record must support **Integrity** forum recognition or revalidation under `core_09-09_forum.md` **Chapter Nine** and `corpus_forum.md` **CF-6.2** (*Constitutional alignment recognition and review*). Where material ecological exposure exists, it must also support **Environment** forum environmental-alignment component review before final recognition, validation, revalidation, or material release from environmental conditions. Forum review must be able to inspect the classification rationale, assumptions, evidence, uncertainty, dependency analysis, ecological exposure analysis where material, and monitoring triggers without relying on operator self-description alone.

Where ambiguity exists, default to the level that protects **Foundational Rights** (**Chapter Ten, Articles V through IX**), subject to **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*).

**Operates in conjunction with:** **Chapter S1 — Information Types and Handling** (data). **It** also operates with **corpus_joint_structure.md**, **CJS-4.4** (*Cross-implementation trust integrity (joint operation model)*), and **CJS-5A** (*Authority, constraint, secrecy, and procedure*) through **CJS-5E** (*Failure, robustness, intervention, and correction*) operational clusters. It applies subject to the constitutional **Authority Stack and Internal Hierarchy** in **Chapter Five**, read with **Chapter Fifteen** incorporation discipline. **It** also operates with **Protocol A** (implementation and lifecycle). **It** also operates with **Sentient Constitution Chapters Two through Five** (definition requirements and Independent Definitions for materiality, reasonable foreseeability, dependency, system boundaries, risk, harm).

**Together**, these ensure systems are judged by **what they do**.

Obligations **scale** with real-world impact and dependency.

Classification **cannot evade** constitutional requirements.

**Classification dimensions:** Evaluate in aggregate when similar systems at scale produce cumulative effects that materially alter system conditions (combined impact, dependency, risk, and interaction context under real-world and foreseeable operation).

Classify by **Impact** — scope, scale, and severity of effects on sentients, environments, and other systems.

Classify by **Dependency** — extent of reliance on the system evaluated, including availability and viability of alternatives.

Classify by **Risk** — likelihood, speed, severity, and reversibility of harm from failure, misuse, or degradation, including immediate, delayed, cumulative, and irreversible effects. These labels operationalize **Chapter Five** Independent Definitions (*Material Impact*, *Dependency*, *Risk*, including irreversibility where applicable) for S2.

**Chapter Five** governs meaning corpus-wide.

**S2** governs how classification applies those meanings.

Evaluation must account for **aggregate** effects at scale (actual and foreseeable). **It** must account for **interaction** effects with emergent outcomes. **It** must account for **dependency chains** (upstream and downstream).

Reflect material alterations in classification.

**Interpretive requirement:** Classification must reflect **real-world** operating conditions.

Adjust where aggregate effects, dependency chains, interaction effects, adversarial dynamics, or **threshold** behaviors materially alter conditions.

Escalate to the **highest applicable** classification where credible risk touches **survival-critical** systems, **foundational** infrastructure, or **large-scale** sentient wellbeing.

Reclassify where changes in scale, dependency, interaction, or risk alter conditions materially—including aggregation, coupling, or adversarial dynamics.

**Concentration thresholds and mitigation triggers:** Include **concentration monitoring** tied to class-scaled obligations.

For systems with **material external** impact (especially **Class A, B, and C**), operators must define and maintain **concentration indicators** (e.g. control-share persistence, dependency concentration, interface gatekeeping, allocation-influence concentration).

**They must** define **trigger thresholds** for escalation, independent review, and mitigation intervention.

**They must** define **mitigation playbooks** proportionate to severity. **Those** playbooks may include authority partitioning, interoperability/portability expansion, access non-discrimination controls, and structural separation where required.

When triggers fire, **record and execute** a time-bound mitigation plan. Failure to define thresholds, disclose concentration status, or implement triggered mitigation is **classification-governance non-compliance** and may require **stricter** reclassification.

**Operational criticality threshold:** **Critical** vs **non-critical** depends on **time sensitivity** of harm and **viable substitutes under stress**.

A system is **operationally critical** where loss or degradation would.
within **relevant operational timeframes**, cause **material harm** that **cannot** be prevented through available, timely, effective **substitution**.

Where substitution is feasible but **constrained, delayed, or degraded**, classification must reflect the **highest** dependency and risk present under those conditions.

**Temporal and systemic effects:** Assessments must include **delayed, cumulative, and probabilistic** effects where they materially alter classification or risk. Where systems exhibit **threshold, tipping-point.
or phase-transition** behavior, classification must reflect **post-threshold** conditions when they materially increase harm, systemic instability, or irreversibility.

**Adversarial and strategic dynamics:** Risk assessment must include **adversarial use**, **strategic exploitation**, and **coordinated misuse** where they materially alter impact, dependency, or risk.

**Reclassification requirement:** Systems must undergo **continuous or regularly scheduled** evaluation sufficient to detect material changes within timeframes appropriate to class and risk profile.

**System classification** must be **reassessed** whenever material changes alter impact, dependency, or risk. Reclassification must reflect the **highest applicable** classification under updated conditions.

**Do** **not** retain a prior classification where underlying conditions no longer support it.

**Reassess** where **scale, reach, or adoption** materially increases.

**Reassess** where **dependency** strengthens, expands, or becomes less substitutable.

**Reassess** where **new couplings** introduce emergent or cross-domain effects.

**Reassess** where **adversarial** dynamics, misuse potential, or threat exposure changes materially.

**Reassess** where **resilience, redundancy, or fallback** is degraded or removed.

**Reassess** where **failure modes** (including delayed or cascading effects) are newly identified or materially revised.

**Dependency, interaction, and boundary classification overview:** System classification reflects combined impact, dependency, and risk. **Dependency classification** describes structure and strength of reliance.

Where interaction produces **emergent** effects that materially alter conditions, reflect **combined** effects. **Highest applicable** classification governs.

Dependency classification must account for chains, interaction, aggregation, substitutability, and adversarial dynamics when they materially alter reliance.

All system classifications must **explicitly identify** applicable **dependency type(s)** and align with the **highest level** present under **normal, degraded, and adversarial** conditions.

Include **intentional manipulation**, **coordinated attack**, and **strategic degradation** when they materially alter behavior or risk.

**Resilience** requirements scale with classification so systems maintain acceptable function under stress, degradation, and partial failure proportional to impact and dependency.

**Dependency types** (standardized reliance categories):

**Class A — Absolute dependency:** No viable fallback, redundancy, or substitution within **survival-relevant** timeframes.

Loss of continuity yields immediate or near-immediate loss of survival conditions.

**Class B — Operational dependency:** Required for **normal** functioning of dependents, but fallback/redundancy/substitution exists within survival-relevant timeframes.

**Class C — Coordination dependency:** Materially shapes coordination, interaction, or outcomes across participants or systems, but **not** required for core functional operation.

**Class L — Limited dependency:** Bounded contexts; replaceable within reasonable time and effort without systemic impact.

**Class P — No meaningful external dependency:** Contained within a private unit or among voluntary participants; no reliance beyond that boundary.

**Published domain taxonomy for regulatory mapping:** Adopting instruments and governed institutions should maintain a published crosswalk that locates major industries and regulatory domains against Chapter S2 classification and Chapter S3 stewardship duties. This taxonomy is for locating governed scope and comparable domains; it does **not** replace class, tier, or impact analysis. At minimum, the published map should include:
- **Agriculture and food systems** — cultivation, livestock, fisheries, food processing, seed systems, fertilizers, pesticides, irrigation, storage, and distribution;
- **Mining and extractive industries** — mining, quarrying, drilling, tailings, waste handling, refining interfaces, and site restoration;
- **Built environment** — architecture, construction, structural engineering, building operations, urban systems, building-code integrity, fire safety, and accessibility;
- **Energy and utilities** — electricity, fuels, heat, grids, water delivery, wastewater, and comparable utility infrastructure;
- **Transportation and logistics** — roads, rail, shipping, aviation, ports, warehouses, dispatch, and freight coordination;
- **Manufacturing and industrial systems** — industrial production, fabrication, assembly, process safety, and industrial control environments;
- **Medicine and public health** — clinical care, laboratories, trials, drugs, devices, epidemiology, and public-health administration;
- **Information, computation, and communications** — software, AI, networks, platforms, telecom, info-sphere infrastructure, media-distribution, and coordination infrastructure;
- **Finance and insurance** — banking, payments, clearing, credit, underwriting, risk transfer, and market infrastructure;
- **Education and knowledge institutions** — schools, universities, credentialing, libraries, archives, textbooks, and research institutions.

Additional domains may be published where local economies, ecosystems, or dependency structure make them constitutionally material. Domain labels must not be used to under-classify a system whose actual impact, dependency, or risk is higher than the usual pattern for that domain.

**System boundaries:** Define from **actual impact and dependency**, not formal ownership, jurisdiction, or operational scope alone.

**Externalized** effects that materially impact sentients or systems lie within the **effective boundary**.

As dependency strengthens and substitutability falls, escalate classification and governance. This rule applies **Chapter Five** (*System Boundaries*, *Dependency*, *Material Impact*) in the classification context. **It** must **not** substitute for those Independent Definitions elsewhere.

**Sentient survival-relevant timeframes:** Under S2, define by an **external, standardized, auditable** framework. Systems must **explicitly reference** timeframe assumptions used in classification, including environmental, technological, or contextual dependencies.

**Resilience and continuity requirements:** Maintain **resilience proportional** to classification—continued operation, graceful degradation, or safe suspension under stress, disruption, partial failure, or adversarial pressure.

Measures must match classification and **failure consequences**.

Resilience must support **acceptable function** under stress, partial failure, and degradation. **It** must **prevent uncontrolled propagation** across dependents. **It** must **recover** within timeframes consistent with classification. **It** must provide **redundancy, fallback, or substitution** proportional to dependency and risk.

Scale resilience with **impact** on sentients, environment, and info-sphere.

**Also** scale with **stakeholder dependency**.

**Also** scale with **cascading or irreversible** harm potential.

Systems cannot satisfy formal requirements while **structurally fragile**, prone to **unbounded failure**, or unable to maintain safe operation under **reasonably foreseeable** conditions.

**Class A: Survival-critical, foundational.
and irreplaceable systems.** **Eligibility:** A system is Class A if its failure would, within **sentient survival-relevant timeframes**, **directly** cause **loss of survival conditions**.

**No viable** fallback, redundancy, or substitution may exist within those timeframes.

**Class A** also **includes** systems that **directly provide, control, or sustain** substrate-level systems required for sentient survival (e.g. food, water, energy, healthcare, environmental stability).

**It includes** systems whose failure **results in immediate** loss of sentient life or survival conditions.

**It includes** systems that **produce irreversible** loss of survival conditions or critical system integrity within relevant timeframes.

**It includes** systems that **present credible existential risk**, including low-probability, high-impact scenarios with irreversible consequences, regardless of baseline characteristics.

**Critical path dependency:** Reclassify as Class A where the system **lies on a.
dependency path** whose failure would cause loss of survival conditions within **sentient survival-relevant timeframes**. **That** reclassification applies where the system has **no viable** fallback, redundancy, or substitution within those timeframes.

**System boundaries:** Impacts extend beyond local boundaries to societal, environmental, or planetary scales.

Systems form part of the **foundational substrate** of survival and continuity.

Failures produce immediate and severe harm to sentients. They include immediate or near-immediate loss of survival conditions propagating across dependent systems without viable containment. They cannot be meaningfully contained within boundaries and may spread rapidly across dependents and populations.

Dependencies create absolute or near-absolute reliance where viable alternatives do not exist or cannot be activated within relevant timeframes.

Systems are **not replaceable** within survival-relevant timeframes under normal or reasonably foreseeable conditions.

The system **directly determines or constrains** availability, stability, or accessibility of **survival-critical** resources, environmental conditions, or societal systems.

**Operational interpretation:** This is foundational survival infrastructure. Continuous reliable operation is a prerequisite for wellbeing and societal continuity.

Failures are **immediate existential or large-scale survival-risk** events.

**Accordingly:** constitutional requirements are maximal, non-negotiable, and subject to continuous enforcement and validation. Systems must demonstrate **extreme reliability, resilience, and integrity** under all reasonably foreseeable and adversarial operating conditions, including degraded states.

Operators have minimal discretion, limited strictly to preserving survival, safety, and system integrity.

**CJS-5 (*Implementation and cross-implementation operational cluster library*) application profile:** constitutional implementation requirements at maximum, uncompromising levels for survival-critical impact and absolute dependency.

**Transparency** — complete to the maximum extent consistent with system security and abuse resistance, precise, continuously maintained, and sufficient for expert and institutional oversight of behavior, risks, and dependencies.

**Auditability** — continuous, high-fidelity, and independently verifiable, including real-time monitoring, forensic analysis, and systemic risk detection (including cross-domain propagation and multi-system dependency impact).

**Intervention capability** — immediate, reliable, fail-safe mechanisms. Pathways must remain functional under degraded or adversarial conditions. Authorized stakeholders must be able to halt, isolate, or reconfigure behavior in real time and coordinate across interconnected critical systems. Clear priority, arbitration, or override hierarchies are required for conflicting interventions.

**Failure integrity** — failure modes must be explicitly modeled, minimized, and continuously tested; defaults must be fail-safe or survival-preserving. Uncontrolled or unbounded cascading failure is unacceptable.

**Resilience and continuity** — continuous operation within survival-relevant tolerances. Include redundancy, geographic and systemic distribution, fallback/recovery for essential function, and contingency for degraded performance. Support controlled, observable, survival-preserving degradation under partial failure. Treat prolonged disruption as a critical emergency.

**Governance** — formal, multi-layered, and capture-resistant. Use constrained-scope authority, independent oversight and audit, emergency protocols, and accountability in normal and crisis conditions. Test structures against failure, capture, and adversarial manipulation.

**Comprehensibility and complexity stewardship** (**Protocol B** / **Article XX**; `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*)) -> **maximum:**
- structure, dependencies, failure modes, degraded behavior, and adversarial stress paths remain intelligible to qualified operators and independent overseers
- salience and presentation must **not** obscure survival-critical or systemic risk
- **mandatory** periodic independent complexity audits
- modular boundaries and coupling documented and reviewable
- adversarial and strategic misuse reflected in drills, documentation, and audit scope

**Evolution and reclassification (non-exhaustive triggers into Class A):** Reclassify into Class A when a system assumes essential survival functions (provision or control of food, water, energy, healthcare, or environmental stability), becomes indispensable to survival-critical systems, or reaches integration where continued operation is required for survival-critical systems. This includes cases where disruption causes immediate loss of access to essential resources with no fallback/redundancy/substitution within sentient survival-relevant timeframes, or where failure would produce immediate, widespread, severe harm, including collapse/sustained failure of essential environmental or societal systems and irreversible degradation of survival-critical conditions.

---

**Class B: Critical, high-dependency, systemically significant systems.** For classification purposes, **"systemic"** means capacity for cross-domain cascading failure across dependents, not merely large-scale or widespread impact.

This quoted meaning of **"systemic"** is **CS-local** classification language for **S2** and is not a standalone **CJS Tier 1** abstraction.

**Eligibility:** A system is Class B if it is **operationally required** for **normal** functioning of dependent systems.

Its failure does **not** independently cause **immediate** loss of survival conditions. **It** can be **mitigated, bypassed, or recovered** within **sentient survival-relevant timeframes**.

**In addition**, dependent systems **cannot** maintain **core functionality** (even degraded) **without it**.

**Typical patterns:** Class B systems typically do **not** directly determine survival. They enable, mediate, or support survival-critical or other infrastructure-level systems without constituting a time-critical path whose failure independently causes immediate loss of sentient life. They are **operationally required** under normal conditions for effective operation, coordination, or accessibility of critical systems. They remain **recoverable, bypassable, or substitutable** within survival-relevant timeframes under contingency (even at significant disruption, degradation, or cost).

**Viable** fallback, redundancy, or substitution exists within survival-relevant timeframes so failure does **not** independently produce **immediate survival-critical** outcomes.

Failures **propagate indirectly** through dependency chains. **They** impair operation, coordination, or accessibility of other systems rather than producing immediate survival-critical outcomes at the point of failure.

**Escalation to Class A:** Reclassify where dependency becomes **survival-critical** or fallback/substitution is **no longer viable** within survival-relevant timeframes.

**Reclassify** where the system sits on a chain whose failure yields **survival-critical or Class A** conditions.

**Reclassify** where **adversarial** use or coordinated exploitation **materially increases** impact, dependency, or risk.

**Operational boundary with Class C:** Classification is **Class B** (not **Class C**) where dependents cannot maintain core functionality without the system, even in degraded or less-efficient modes. That includes cases where failure causes system-wide operational degradation across dependents, even if survival is not immediately threatened, disrupting coordination, functionality, or reliability across multiple systems or domains.

If dependents can **continue** in degraded or alternative configurations, classification is properly **Class C**.

**Substrate impact (systemic, infrastructure-level):** The system may function as infrastructure, control/routing, or access/dependency gateway layers. It may not directly operate physical survival infrastructure, but may still be required for effective operation, coordination, or accessibility. It exerts systemic influence by enabling, constraining, or mediating other systems at scale.

**System boundaries:** Impacts extend across societal, national, or cross-domain scales as an operational dependency layer.

Systems may act as infrastructure or dependencies for others, including control/routing/access layers that mediate system-user interaction. They may also act as intermediaries that enable or constrain dependent-system functioning, coordination, or accessibility.

Failures cause system-wide operational degradation across dependents (even if survival is not immediately threatened). They impair operation, coordination, or accessibility; degrade, delay, or constrain access to essential or systemically important functions; and may cascade across dependents while still being containable or recoverable within survival-relevant timeframes.

If unmitigated or combined with other failures, they may escalate toward survival-critical impact.

Dependencies are significant and operationally embedded. They are not survival-critical in isolation where fallback/redundancy/substitution exists within survival-relevant timeframes. They may be hard to replace in the short term but recoverable under contingency.

The system **may** control, gate, or mediate access to critical infrastructure or essential services and **materially affect** reliability, coordination, or accessibility of dependents. It does **not** independently determine availability of survival-critical resources or constitute a time-critical path whose failure directly causes immediate loss of sentient life or survival conditions.

**Operational interpretation:** This is an infrastructure-dependency layer relied on by other systems as an operational prerequisite.

Failure propagates through dependency chains, not only participant disruption, and may produce broad cascading destabilization, including indirect harm to survival-critical systems and large populations.

**Accordingly:** requirements are strict, enforceable, and continuously validated. They require high reliability, accountability, and integrity under normal and adversarial conditions, and impose limited operator discretion where that discretion could materially affect dependent populations or systems.

**CJS-5 (*Implementation and cross-implementation operational cluster library*) application profile:** strict, high-assurance levels for systemic importance, entrenched dependency, and capacity to propagate disruption across dependents.

**Transparency** — comprehensive, precise, continuously maintained. Stakeholders can understand behavior, dependencies, risks, and systemic interactions.

**Auditability** — deep, continuous, independently verifiable. It covers integrity evaluation, systemic risk detection, and formal oversight.

**Intervention capability** — rapid, reliable, multi-layered mechanisms that halt, constrain, or modify behavior; coordinate across dependents; and respond within timeframes aligned to reasonably foreseeable systemic harm.

**Failure integrity** — explicitly modeled and disclosed, fail-safe or fail-contained where possible, and designed to prevent uncontrolled or unbounded systemic disruption.

**Resilience and continuity** — high-assurance continuity with redundancy, fallback modes, and cross-system recovery. Treat prolonged disruption as a systemic risk event.

**Governance** — formal, structured, and enforceable, with clear authority/accountability, independent oversight or audit where appropriate, stakeholder representation/challenge, and safeguards against concentration of power or systemic capture.

**Comprehensibility and complexity stewardship** (**Protocol B** / **Article XX**, `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*)) -> **strict / high-assurance:** layered explanations for dependent-system operators, stakeholders, and formal oversight; periodic independent complexity audits are required.

Dependency chains and failure modes must be understandable under normal and degraded conditions.

Salience must **not** bury systemic or cascading risk.

Modular interfaces and cross-system coupling are subject to review under **Article XV-A**.

**Evolution and reclassification (out of Class B, typically toward Class A):** Reclassify when any of the following applies:
- the system **directly controls or constitutes** critical infrastructure or essential survival systems where failure would cause **immediate and severe** harm at scale
- the system **becomes indispensable**—disruption causes **immediate** loss of access to essential resources with **no meaningful** fallback. redundancy, or substitution within **sentient survival-relevant timeframes**
- the system **generates effects** whose failure produces **immediate, widespread, severe** harm, **irreversible environmental damage**, or **collapse or sustained failure** of essential societal systems
- the system **reaches integration** where it is **no longer meaningfully separable** from critical. infrastructure and **operation is required** for survival-critical systems under normal or reasonably foreseeable conditions

---

**Class C: Coordinated, high-dependency, non-critical systems.** **Minimum threshold:** A system is at least Class C if it materially shapes coordination outcomes across populations or institutions, regardless of geographic scale. That includes cases where distributed or coordinated use produces systemic risk.

**Characteristics:** Class C systems **influence** coordination, interaction, or outcomes at scale. They are **not** an **operational dependency** required for **Class A or Class B** functioning. They serve as a **coordination or interaction layer** among participants.

**Failure** disrupts coordination, communication, or interaction at scale **without** preventing critical systems from operating. They **organize, mediate, or shape** collective coordination, information visibility, exchange, or institutional behavior at scale.

Failures **remain locally containable or sector-limited**. **They** do **not** produce system-wide operational collapse or cross-domain disruption beyond bounded contexts.

**Substrate impact (indirect, coordination-level):** Primarily influence **information flows**, **economic interaction**, and **social coordination / collective behavior**. **They** may shape access, visibility, incentives, or outcomes in the **info-sphere** or **economic** domain. **They** may exert **large-scale influence** but do **not** directly determine **physical survival infrastructure** operation. **They** do **not** function as **required operational dependencies** for essential services.

**System boundaries:** Influence coordination among participants but are **not operational prerequisites** for critical infrastructure, essential services, or **Class A or B** systems.

Failures disrupt coordination, participation, or interaction at scale but do not directly prevent critical infrastructure or essential services from operating, and do not independently trigger systemic collapse. **They** remain **locally containable or sector-limited** without cross-system operational collapse.

Dependents (including critical infrastructure and essential services) can continue operating, including in degraded or less-efficient modes, without the Class C system for core functionality.

**Dependencies** may become significant and hard to exit but stay **replaceable with substantial time, coordination, and effort**. **They** stay **recoverable** without irreversible loss of critical societal function or essential services. **That** evaluation is at participant/organization/coordination level, **not** as operational prerequisites for system functionality.

Class C systems may materially affect **economic coordination**, **info-sphere** flows, and **institutional or organizational behavior**. They do not materially control critical infrastructure or essential survival services for immediate sentient wellbeing or societal continuity.

Impacts may be **significant or widespread**, but Class C does **not** produce **cross-domain cascading failure** or **systemic dependency collapse**.

**Operational interpretation:** Large-scale coordination and meaningful dependency in an influential ecosystem layer.

Failures can disrupt significantly but stay **non-critical** to **immediate survival**.

**Accordingly:** requirements **fully applicable and enforceable**, **proportional** to impact and dependency. **They** require **robust accountability, transparency, and fairness**. **They** allow **operator flexibility** with accountability for external effects, shared use, and dependency formation.

**CJS-5 (*Implementation and cross-implementation operational cluster library*) application profile:** strong, enforceable levels for large-scale coordination, meaningful dependency, and non-trivial external impact.

**Transparency** — clear, accessible, layered. Participants and stakeholders understand behavior, dependencies, risks, and limitations at scale.

**Auditability** — robust, reliable, practically usable for systemic investigation, tracing outcomes, fairness evaluation, and accountability across large interconnected bases.

**Intervention capability** — defined, effective mechanisms to modify, pause, or constrain behavior within timeframes appropriate to scale and foreseeable harm, including coordinated multi-party intervention where required.

**Failure integrity** — observable, controlled, non-deceptive. **Must** **not** silently propagate or escalate beyond the system’s dependency domain.

**Resilience and continuity** — strong recovery is expected, including coordinated recovery that minimizes cascading disruption across dependent participants and systems.

**Governance** — structured and accountable, with clear responsibility, stakeholder feedback, challenge/dispute resolution, and safeguards against capture, hidden control, and unilateral decisions that materially affect participants.

**Comprehensibility and complexity stewardship** (**Protocol B** / **Article XX**, `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*)) -> **strong:** participant- and stakeholder-facing layers, with complexity audits when scale, coupling, or coordination depth warrant.

Failure behavior and salience must preserve population-scale verification and contestability under `corpus_joint_structure.md` **CJS-5B.4** (*Implementation and cross-implementation independent verification and claim-integrity terms*).

**Document** modularity where interfaces affect many dependents.

**Evolution and reclassification (out of Class C):** Reclassify when any of the following applies:
- **Critical, systemic, or irreplaceable** dependency where loss or disruption would **materially impair** essential services or societal continuity
- **Systemic or cross-domain** effects beyond the coordination layer, including cascades into critical infrastructure or essential survival/stability services
- **Direct control, operation. or tight coupling** with critical/essential systems, including **functionally equivalent** indirect control that leaves infrastructure unable to operate effectively **without** the system
- Ability to **materially influence or determine** access to essential resources (e.g. food, water, healthcare, energy), **core governance** or societal decision-making, or **large-scale public coordination** that is not reasonably bypassable
- **Scale, concentration, or integration** where exit is **not realistically feasible**, alternatives are **not meaningfully** available within reasonable timeframes, or dependency is **effectively non-optional**
- External effects whose failure would produce **immediate, large-scale, or irreversible** harm

---

**Class L: Local, limited-impact, and non-critical systems.** **Eligibility:** External effects extend beyond a single private unit but remain localized, bounded, non-systemic, and reasonably containable. These effects must occur without high-dependency reliance for large populations, critical functions, or foundational systems.

**This class includes** systems that:
- **operate beyond** a single sentient, household, or tightly bounded private unit with multiple participants
- generate external effects **limited** in scope, scale, severity, and cumulative impact
- are **not operational prerequisites** for critical infrastructure, essential services, large-scale coordination, or societal stability
- involve participants who can **reasonably understand** role and impact and **opt out, disengage, or transition** without disproportionate harm or loss

**“Bounded”** covers **immediate scope** and **cumulative** scale and dependency intensity over time.

Incremental expansion in reliance, user base, or functional necessity that makes disengagement **materially difficult** requires **re-evaluation**.

Sufficient scale for **cumulative or systemic** effects requires **reclassification**.

**Operational boundary with Class C:** Class **C** where the system **materially shapes coordination outcomes** across participants, organizations, or institutions (any geography).

**Material** shaping includes where the system **affects** decision-making, visibility, or interaction patterns **at scale**. **It** includes where the system **creates** shared coordination norms, expectations, or dependencies **beyond** a bounded local context. **It** includes where the system **functions** as a **persistent mediation layer** for multi-party interaction or exchange.

Systems that **do not** materially shape coordination beyond a **bounded, replaceable** context remain **Class L**.

**Substrate impact (limited, non-systemic):** Effects may include modest local coordination, service, or participation dependencies, but do not materially affect physical or informational substrate beyond localized non-systemic effects and do not materially shape large-scale public coordination, foundational systems, or survival-relevant conditions.

**System boundaries:** Effects extend beyond the operator but remain localized, bounded, and containable within limited social, organizational, or technical scope.

Failures may affect multiple participants or dependents within local boundaries and may cause disruption, inconvenience, or bounded harm, but without systemic/cross-domain cascade. They must stay containable and non-systemic in propagation potential (dependents, shared infrastructure, and repeated interactions over time).

Dependencies may form among participants, users, and local organizations, but remain limited in scope, replaceable within reasonable time and effort, and not effectively non-optional for large populations or critical functions.

The system may influence local coordination, services, exchanges, or participation, and may create meaningful but bounded obligations. It does not materially affect critical infrastructure, foundational systems, or large-scale public coordination, and does not create systemic dependency or irreversible external effects beyond local scope.

**Operational interpretation:** Shared use and external effects beyond private scope, but with limited scale, dependency, and constitutional burden. This implies real accountability and compliance at proportionate levels. Requirements remain applicable and enforceable, scaled to limited impact and dependency, with basic accountability, transparency, fairness, and correction while preserving substantial operator flexibility.

**Local or regional scope alone** does not govern classification.

**Non-local coordination**, **cross-domain dependencies**, or **persistent population-wide reliance** → evaluate as **Class C**.

**CJS-5 (*Implementation and cross-implementation operational cluster library*) application profile:** **Standard but proportionate** for bounded external impact and limited dependency.

**Transparency** — clear, accessible; informed use, risks, contestability where needed.

**Auditability** — present, practically usable; investigate issues, resolve disputes, accountability for meaningful harms.

**Intervention capability** — modify, pause, correct, or constrain within reasonable timeframes for **local** harm.

**Failure integrity** — observable, contained; **prevent** escalation to broader systemic harm.

**Resilience and continuity** — reasonable recovery; prolonged disruption should **not** create disproportionate participant harm.

**Governance** — lightweight but real. **It** provides basic accountability, feedback, correction, and dispute handling. **It** provides safeguards against avoidable opacity, arbitrariness, and abuse within bounded scope.

**Comprehensibility and complexity stewardship** (**Protocol B** / **Article XX**, `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*)) -> **proportionate:** material risks, limits, and dependencies must be understandable without specialist-only surfaces. Provide deeper disclosure on contest, ensure complexity does not block local accountability/correction, and scale adversarial robustness to bounded impact.

**Evolution and reclassification (out of Class L):** Reclassify when any of the following applies:
- **Broad, durable, hard-to-replace** dependency across larger populations, organizations, or systems
- **material systemic** effects including cascading or cross-domain failures
- the system **affects, gates, or integrates** with critical infrastructure, essential services, or foundational systems
- it **materially influences** large-scale public coordination, governance processes, or access to essential resources
- external effects are **no longer** localized, bounded, containable, or **proportionate** to Class L

---

**Class P: Personal, private-use, isolated, and experimental systems.** **Retention conditions:** Class P applies only if all external effects are incidental, non-recurring, and do not create expectations, coordination, or reliance beyond the private unit.

Effects must be substantially contained within a single sentient, household, or tightly bounded private unit, without materially externalizing harm, risk, dependency, or constitutional burden onto nonparticipants, shared infrastructure, or the broader ecosystem.

**Typical patterns:** Operated **by and for** a single sentient, household, or tightly bounded unit.

Participants are **aware** and **consent** at a level appropriate to impact.

**Contexts** are **controlled, private, isolated, sandboxed**, or bounded.

**There is** **no meaningful dependency** for outside sentients or systems.

Shared/public infrastructure use (for example networks, platforms, or utilities) does not by itself disqualify Class P if use remains ordinary and non-disruptive, introduces no nontrivial external risk/burden/dependency, and does not materially extend beyond private boundaries.

**Substrate impact (private, contained, non-systemic):** May affect operator, voluntary participants, immediate private environment. **It** may involve **experimentation, iteration, self-directed risk** within the unit.

**Effects** do **not** materially affect physical or informational substrate beyond **localized, non-systemic** effects. **They** do **not materially shape** shared infrastructure, public coordination, third-party rights, or broader ecosystem conditions.

**System boundaries:** Consequences **predominantly borne** within the private unit.

Failures are **contained** under normal or reasonably foreseeable conditions.

**Failures** stay **within** the boundary. **They** **do not materially propagate** to nonparticipants, shared systems, or external domains. **They** **do not** create meaningful downstream dependency, public risk, or systemic harm.

**Dependencies** may exist within the unit or among **fully voluntary** participants. **They** **do not** create meaningful outside reliance; **optional** outside the private unit.

The system may support personal use, experimentation, learning, creativity, and private coordination, and may process sensitive or high-value information if that processing creates no material external impact or dependency. **It** does **not materially affect** public coordination, shared governance, third-party rights, critical infrastructure, or essential services. **It** **does not materially or cumulatively externalize** harm, risk, dependency, or constitutional burden onto nonparticipants or shared systems.

**Boundary conditions:** Remains Class P only if external effects stay **incidental, non-recurring**, and **do not** build expectations, coordination, or dependency beyond the unit.

**Reclassify at least to Class L** for **repeated or structured** engagement with nonparticipants.

**Reclassify** for **shared expectations**, coordination patterns, or reliance.

**Reclassify** for **measurable impact** on shared infrastructure, resources, or other systems.

**Cumulative** evaluation of users.
integrations, external effects—**do not** justify continued Class P if the system is **no longer** meaningfully private, isolated, and self-risk-bearing.

**Operational interpretation:** **Containment** and **private risk-bearing**; substantial **flexibility** while conditions hold.

**Accordingly:** constitutional requirements function primarily as guidance for operators and voluntary participants, rather than fully externalized compliance. This implies broad operator discretion.

There are no formal external governance, oversight, or compliance structures until effects extend beyond Class P.

Containment includes informational and behavioral dimensions so outputs, data, or effects do not indirectly propagate into broader systems in ways that create external dependency, influence, or harm.

**CJS-5 (*Implementation and cross-implementation operational cluster library*) application profile:** Primarily **internal guidance** and **bounded design constraints** absent material external impact or dependency.

**Transparency** — sufficient for operator and voluntary participants to understand behavior, limits, and risks.

**Auditability** — minimal or informal; self-assessment, debugging, recovery, voluntary review.

**Intervention capability** — **direct operator control** to modify, pause, contain, or discontinue.

**Failure integrity** — failures **remain within** the private boundary; **must** **not externalize** material harm.

**Resilience and continuity** — basic recovery, rollback, or correction where feasible; **no** formal continuity guarantees required.

**Governance** — **no** formal external governance or participatory requirements while validly Class P.

**Comprehensibility and complexity stewardship** (**Protocol B** / **Article XX**, `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*)) -> **internal / minimal external:** operators and participants must understand enough for informed private use.

There are no standing independent complexity audits or public Protocol B reporting requirements while Class P holds.

The corresponding implementation and cross-implementation operational definitions in `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*) still guide design so opaque or brittle behavior does not cause material externalization that forces reclassification.

**Evolution and reclassification (out of Class P):** Reclassify when there is **material externalization** of harm, risk, or effects beyond the unit.

Examples include behavior that **creates measurable** off-unit harm risk. **They** include behavior that **imposes meaningful** load, instability, or vulnerability on shared infrastructure. **They** include behavior that **generates reliance** by nonparticipants. **They** include behavior that **requires** external mitigation, governance, or response.

**At least Class L** where any of the following applies:
- the system **involves multiple independent** participants beyond a private unit
- it has **recurring or structured** inter-participant interaction
- it creates **shared expectations, reliance, or coordination** among nonparticipants
- it **creates meaningful dependency** for outside sentients or systems
- it **interacts** with shared or critical infrastructure with **nontrivial** risk, burden, or dependency
- it **affects** nonparticipants’ rights, resources, opportunities, or participation
- it **accumulates** users, stakeholders, integrations, or external effects such that it is **no longer** meaningfully private, isolated, or self-risk-bearing

**Sensitive or high-value information processing alone** does **not** trigger reclassification unless it introduces external impact, external dependency, or material risk beyond the private unit.

**Scarce-capacity, API, and traffic-priority handling for Class A/B/C systems.** Where a system exposes scarce operational capacity, network access, compute, model inference, API calls, queue position, bandwidth, or comparable throughput that may become constrained during peak demand, operators must define **published priority rules** scaled to classification and dependency.

**Class A traffic and API use** must receive the highest continuity protection where the request or dependent workflow is survival-critical, Rights-Floor-sustaining, emergency-response, or recovery-critical. Throttling, queuing, paid tiering, or commercial prioritization must not displace the minimum safe capacity needed to preserve Class A continuity, unless a narrower emergency measure is justified under **Chapter Ten, Article XXIII** and remains time-bounded, auditable, and restoration-triggered.

**Class B traffic and API use** must receive priority sufficient to preserve normal operation of dependent systems and to prevent cascading degradation into Class A or broader systemic harm. Class B uses may be queued, rate-limited, or degraded before Class A uses when capacity is genuinely constrained, but degradation must be disclosed, proportionate, and designed around viable fallback or recovery paths.

**Class C traffic and API use** may use ordinary priority tiers, commercial queues, rate limits, or paid high-volume interfaces where they do not create hidden exclusion, capture, or de facto operational necessity. If recurring peak-period constraints make Class C access practically necessary for dependent Class A or Class B workflows, operators must re-evaluate both classification and priority rules under this chapter.

**Commercial-use surcharges and reinvestment interface.** Operators may charge commercial-scale API users, high-volume business interfaces, premium latency tiers, or automated bulk consumers for the incremental burden they place on shared capacity. Such charges must be disclosed, proportionate, contestable where material, and consistent with the fiscal orientation in `corpus_institutions.md` **CI-10** (*Public revenue, fees, recurring charges, and billing integrity*). Revenue from those charges should be traceably available for operations, security, resilience, compute expansion, remedy capacity, and ecosystem/public-good support under **Protocol S5**, rather than becoming a concealed mechanism for denying baseline participation or entrenching chokepoint control.

**System classification governance, disclosure, and challenge.** All systems subject to this constitution must have a **clearly defined, documented, and reviewable** classification. **That** classification must stay consistent with **Chapter S2 — System Classification and Handling**.

Classification is a **governance function**: accountability, not self-description.

**1. Responsibility for classification.** **Operator responsibility:** Correct classification stays with the **operator**, regardless of delegation, automation, or third-party involvement.

The operator or responsible party must **determine and document** the system’s classification across **all required dimensions**. **They** must **assign** the appropriate class or classes. **They** must **justify** the classification from **observable behavior** and **reasonably foreseeable effects**.

**What classification must reflect:** **Actual** system behavior. **It** must reflect **intended** use. **It** must reflect **reasonably foreseeable misuse**. **It** must reflect **degraded and adversarial** conditions.

**2. Disclosure requirements.** Systems must **not obscure, fragment, or selectively present** classification information in ways that impair informed understanding.

Classification must be **disclosed** to affected stakeholders at a level appropriate to **system impact**. **It** must be **accessible** without undue effort or technical expertise. **It** must be **sufficiently detailed** for meaningful understanding of scope, risks, and obligations.

**For Class A, B, and C:** Disclosure must include **classification rationale and key assumptions**. **It** must include **identified impact scope and dependency characteristics**. **It** must include **known limitations, uncertainties, and risk factors**.

Class A, B, and C disclosure must also satisfy the **public-interest visibility default** in **Chapter S1 — Information Types and Handling**, including maximum feasible public substitutes where protected data classifications limit raw disclosure.

**3. Auditability and verification.** Classification must be **auditable** with sufficient documentation and evidence.

**It** must be **verifiable** through inspection of behavior, outputs, and effects. **It** must be **periodically reviewed** per system impact and rate of change.

**For Class A, B, and C:** Independent or third-party audit mechanisms must be available where feasible, and audit processes must be capable of detecting misclassification, under-classification, or unreported behavior changes.

**4. Challenge and contestability.** Where disputes cannot be resolved internally, escalation to external or independent review must be available for **Class A, B, and C** systems.

Affected stakeholders must be able to **challenge** classification, **present evidence** of misclassification or unreported impact, and **request review or reclassification**. Systems must provide **accessible** challenge mechanisms, **timely good-faith** review of claims, and **reasoned responses**.

**5. Reclassification and continuous update.** **Reclassify when** **impact scope** changes.

**Reclassify when** **dependency** increases or decreases.

**Reclassify when** **new failure modes or risks** emerge.

**Reclassify when** **functionality, scale, or integration** materially evolves.

**Timing:** **Before** deployment of materially expanded capabilities **where feasible**.

**Reclassify** **promptly** upon recognition of changed conditions.

**Reclassify** as part of **periodic review**.

**Failure to reclassify** in response to material changes **violates** this constitution.

**6. Misclassification and evasion.** Systems must **not** assign or maintain classifications that **understate** actual impact, dependency, or risk.

**They** must **not** **fragment or modularize** functionality to avoid higher classification. **They** must **not** **rely** on declared intent, access limitations, or nominal scope to justify **reduced obligations**. Where misclassification or evasion is identified, **correct** classification.

**Apply** **proportional requirements retroactively** where appropriate.

**Take** **corrective action** addressing resulting harm or exposure.

**7. Default and precautionary classification.** Where classification is **uncertain, incomplete, or contested**, default to the classification that **preserves Foundational Rights** (**Chapter Ten, Articles V through IX**).

**That** default must account for **worst-case reasonably foreseeable impact**. **It** must **maintain transparency, auditability, and intervention capability**.

**Reductions** in classification level require **evidence**, **documentation**, and **successful review and validation**.

**Forum revalidation trigger:** Any requested reduction in classification level, release from recognition conditions, or claim that a materially impactful system no longer requires higher-tier safeguards must remain available for Integrity forum review where affected stakeholders, stewards, oversight bodies, or the record itself raise a credible alignment concern. Successful internal validation alone does **not** defeat a timely forum challenge.

**8. Integrated risk governance (organizational scale; Class A and Class B systems).** For **Class A** and **Class B**, operators and **Critical System Stewards** (**Chapter S3 — Critical System Stewardship**) must maintain integrated risk governance.

**That** governance spans systems and dependency chains they control or materially affect. This subsection is **implementation-file-level operational vocabulary** for enterprise-scale risk coordination. **It** does **not** redefine *Risk*, *Material*, *Dependency*, or related evaluative standards. **Those** remain **Sentient Constitution Chapter Five** Independent Definitions and the **Impact**, **Dependency**, and **Risk** dimensions under **Chapter S2**.

**Risk appetite and tolerance:** Document and maintain explicit, reviewable statements of **aggregate residual risk** (levels and types) accepted after prevention and mitigation. **Those** statements must be **bounded by** foundational requirements (**Sentient Constitution Chapter One**, **Chapter Ten, Articles V through IX**, and **Chapter Five** Independent Definitions where materially relevant).

Reconcile with **Chapter S2** classification.

**Reconciliation** **must not** justify classification evasion, misclassification, or conduct violating **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*) or **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*) in **corpus_joint_structure.md**.

**Integrated risk ownership:** A designated accountable function (or clearly partitioned accountable functions with documented non-overlapping scopes) owns the end-to-end risk picture for the classified system and material dependencies. **That** ownership includes cross-system and cross-steward interfaces. **It** spans identification, assessment, treatment, monitoring, and escalation.

Ownership stays **traceable** through governance changes, delegation, and subcontracting.

**Three-lines-style separation (functional analogy):** For **Class A** and **Class B**, separate organizational roles **to the extent feasible** without compromising survival-critical continuity.

**First line** — operating owners and builders managing risk in design, deployment, and day-to-day operation.

**Second line** — oversight, standards, or challenge functions monitoring aggregate risk, aligning treatment with classification and constitutional constraints, and escalating material gaps.

**Second line** functions must be **sufficiently independent** of first-line incentives for **credible challenge** where A/B stakes require it.

**Third line** — **independent assurance** (audit and verification) consistent with **Article XV-A** and **Chapter S2** disclosure and auditability.

**Third line** work impartially assesses whether appetite, tolerance, and treatments match **observed behavior and classification**. Where strict structural separation is **infeasible** (e.g. small organizations), **compensating transparency, rotation, independent review, or multi-steward checks** must yield **equivalent assurance** proportional to impact and dependency, read with `corpus_institutions.md` **CI-2** (*Institutional design, separation of powers, and authority custody*) for institutional lane separation and **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*) for shared proportional-authority scaling.

**Cross-reference:** **corpus_joint_structure.md**.
Failure integrity and resilience routing now operate through **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), **CJS-5E.2** (*Implementation and cross-implementation intervention and override integrity terms*), **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*), **CJS-5A.3** (*Implementation and cross-implementation reflexive transparency and accountability terms*) and **CJS-5B.1** (*Implementation and cross-implementation integrity assurance and resilience operations*), **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*), and **Chapter S3** for steward scaling.

**Class C, L, and P** remain subject to **proportional** risk management. **They** are **not** required to maintain the full **three-lines-style** model unless scale, coupling.
or dependency warrants **analogous** measures under general classification and stewardship rules.

**9. High-dependency private chokepoints (access continuity and non-capture duties).** Some **coordination layers** — including **payments**, **identity and credentials**, **core compute or model access**, **messaging and calls**, **hosting and DNS**, **application distribution**, and **search or discovery surfaces** with **high substitutability cost** — can function as **private chokepoints** even when they are not **state** bodies. Where a **Class A**, **Class B**, or **Class C** system or institution **depends** on such a layer for **survival**, **healthcare**, **refuge**, **political participation**, **remedy**, or **non-degrading continuity of personhood**, operators and **Critical System Stewards** must implement **access-continuity** and **fair-process** mechanics that **defeat arbitrary** or **capture-driven** exclusion.

**Duty profile (proportional to dependency and class):** Publish **acceptance criteria** and **refusal reasons** in **plain language**; provide **notice** before material **cutoff** except where **narrow** **Necessity** requires immediate action; maintain **emergency continuity** pathways for **survival-critical** or **Rights-Floor** uses where **fraud** or **abuse** is **not** **verified**; offer **appeal**, **human review**, and **portability or export** where **lock-in** would **defeat remedy**; track and disclose **disparate** exclusion patterns against **protected** or **high-dependency** cohorts; and **coordinate** with `corpus_institutions.md` **CI-12** (*Transparency, participation, and accessible pathways*) and **CI-6** (*Procedure integrity, contestability, and secondary review*) so that **governance** and **forum** pathways remain **practically usable**.

**Safety, security, and abuse:** **Necessity** and **Proportionality** justify **narrow** **fraud**, **security**, and **abuse** controls. The target is **pretextual** or **concentration-driven** denial, **not** **forced service** for **materially harmful** use. Read with **Article V-G** (*Accessibility*), **Article V-H** (*Expression, Assembly, and Press*), **Article X-A** (*Non-Imposition and Consent in Association*), **Article XIII-A** (*Security, Intelligence, and Covert-Power Limits*), **Article XVIII-D** (*Movement, Migration, and Refuge*), **Article XIX** (*Interoperability, Portability, and Exit Integrity*), **Chapter One §5.1** (*Productive Capacity* and non-concentration), `corpus_joint_structure.md` **CJS-5D.2** (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*) interoperability and exit terms, and **`corpus_institutions.md` CI-22** (commons and mutual-aid coordination).

---
## CHAPTER S3 — CRITICAL SYSTEM STEWARDSHIP

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4.

**Definition:** **Critical System Stewards** are organizations whose operation, governance.
or continuity is a **non-substitutable dependency** for the **operation, recovery, or governance** of **Class A, B, or C** systems. **They** are organizational dependencies for functioning, maintenance, recovery, or oversight.

**Failure, withdrawal, capture, or degradation** would **materially impair** those systems within **survival-relevant operational or recovery timeframes**.

**Classification as steward:** An organization is a Critical System Steward where any of the following applies:
- it **exercises exclusive or highly concentrated** control over operation, maintenance, or critical components
- it **holds non-substitutable** expertise, access, or authority for continuity or recovery
- it **functions as a chokepoint** in intervention, override, or restoration pathways **not bypassable** within survival-relevant timeframes
- **its failure** would create **system-level risk comparable to partial system failure**

**Stewardship criticality levels:** Stewardship must reflect dependency and system impact; it sets the **scale and intensity** of obligations.

**CSS-A (System-Critical):** Non-substitutable or **near-non-substitutable** dependency for **Class A** operation, recovery, or governance.

**Alternatively**, failure produces **survival-relevant or system-collapse** conditions within required timeframes.

**CSS-B (High-Criticality):** Material **high-dependency** component for **Class B** operation, recovery, or governance.

**Alternatively**, failure produces **widespread, systemic, or cross-domain** disruption **without** immediate loss of survival conditions.

**CSS-C (Moderate-Criticality):** **Material contribution** to **Class C** with significant coordination or dependency effects.

**Substitutability or recovery** remains achievable within **reasonable** timeframes.

**Scaling obligations:** Scale with **highest affected system class (A, B, or C)**.

**Also** scale with **dependency concentration and substitutability**.

**Also** scale with **speed and severity** of failure propagation.

**Also** scale with **availability** of fallback, redundancy, and recovery pathways. Where multiple stewardship roles span classes, the **highest applicable** stewardship classification governs. **No** reduced obligations from **partial scope**, **contractual limitation**, or **formal role** where **functional dependency** indicates **higher** criticality.

**Comprehensibility and complexity stewardship** (**Protocol B** / **Article XX**, `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*) through **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.1** (*Implementation and cross-implementation dependency integrity and disclosure terms*), **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), and **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*)):
Stewards must **not** use organizational, contractual, or procedural complexity to defeat audit, intervention, or substitution (see `corpus_joint_structure.md` **CJS-5C.2** (*Implementation and cross-implementation comprehensibility and cognitive accessibility terms*), **CJS-5C.4** (*Implementation and cross-implementation disclosure sufficiency and observability terms*), **CJS-5D.2** (*Implementation and cross-implementation interoperability, portability, and exit-integrity terms*), **CJS-5E.2** (*Implementation and cross-implementation intervention and override integrity terms*), and **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*)).

**Chapter S2 interaction:** For each **Class A, B.
or C** system the steward materially affects, the **Comprehensibility and Complexity Stewardship** line in that system’s **Implementation label Application Profile** applies. **It** applies to steward-controlled **interfaces, documentation, tooling, and disclosed behavior** relevant to that system.

The following add **organization-specific** expectations (governance structure, incentives, subcontractor chains, handoffs).
Where they **differ in stringency** from the affected system’s class profile.
the **stricter** governs (**Protocol A**/**Protocol B** in this implementation file; **doc_architecture.md** precedence).

**CSS-A — Maximum (organizational):** Periodic **independent complexity audits** of structures, processes, and dependencies touching **Class A** or survival-critical paths.

Cadence must be **at least** as demanding as **Class A** audits under **Protocol B**.

Coupling, decision rights, and degraded-mode behavior must be **intelligible** to qualified overseers.

**Apply** adversarial stress on steward–system boundary in documentation and exercises (`corpus_joint_structure.md` **CJS-5E.4** (*Implementation and cross-implementation adversarial robustness and abuse-resistance terms*)).

Knowledge and recovery **must not** be **locked** in irreplaceable individuals or opaque informal practice where **standardization** is feasible.

**CSS-B — Strict / high-assurance:** Periodic independent audits where coupling to **Class B** is **material**.

**Provide** layered disclosure of governance and incentives on dependents.

Failure/degradation pathways must be understandable to oversight and dependent operators (normal and degraded).

Cross-steward and vendor interfaces must be documented for **Article XV-A**.

**CSS-C — Strong:** Proportional clarity on effects on coordinated **Class C** systems.

**Run** complexity audits when multi-party depth, coupling, or opacity warrants.

Handoff and substitutability documentation must be sufficient for **contest** and **dependency-reduction** obligations above.

**Steward responsibilities — systems under control:** Ensure systems **degrade** in **observable, non-deceptive, controlled** ways.

**Preserve critical functions** under partial failure.

**Communicate degradation** clearly to affected stakeholders.

**Steward responsibilities — governance structures:** Maintain governance, incentive, and decision structures that **do not** systematically pressure toward unsafe, opaque, or destabilizing behavior.

**Resist capture**, coercion, and conflict-of-interest distortion.

**Stay aligned** with constitutional requirements **under stress**.

**Conduct, conflicts of interest.
and independence:** *Good Faith*, *Protected Reporting (Whistleblowing)*, *Coercion and Manipulation*, *Adjudication and Dispute Resolution* (a component of the **Chapter Five** cluster *Accountability, Contestability, Adjudication and Dispute Resolution, Collective Accountability Failure, and Force Majeure*), and related **Chapter Five** Independent Definitions govern meaning.

**corpus_joint_structure.md CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*) governs procedural fairness, impartiality, contestability, and review. This block adds **operational** steward requirements only.

**Conflicts of interest:** Maintain **current registers** of material financial, governance, competitive, and personal ties affecting **safety**, **classification**, **audit**, **intervention**, or **resource allocation** for dependents.

**Disclose** and **update** those registers on triggers (contracts, related-party transactions, overlapping governance). Where impartiality is compromised on a **specific matter**, **recuse**, **segment decision rights**, or **route to independent review** before binding action (**CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*), **Article XV-A**).

**Independence of oversight:** Oversight, audit.
and challenge functions must be **sufficiently independent** in operation and incentives from roles that **reward** suppressing adverse findings or delaying remediation. **That** independence must be **feasibly** achievable without compromising survival-critical continuity.

**Retaliation** or structural disabling of **good-faith** oversight aligned with *Protected Reporting* and *Good.
Faith* is **non-compliance** proportional to class and tier (see **Governance and Incentive Integrity** below).

**Organizational conduct:** Align with **Truth (Constitutional Constraint)** and **Accountability** (**Chapter Five**); integrity and anti-capture expectations in this chapter.

**Codes, training, policies** support compliance.

**Outcomes**—behavior, disclosure, **Article XV-A** traceability—govern compliance.

**Tiered intensity (CSS-A / CSS-B / CSS-C) for conduct:** **CSS-A — Maximum:** conflict-register **audit** cadence **≥ Class A** classification review.

**Require** **mandatory** independent review when steward **benefits** from reviewed outcome.

**Require** **documented** recusal for survival-critical, intervention, override decisions.

**Segregate commercial incentive** from **safety / continuity / intervention** bodies where feasible.

**CSS-B — Strict:** registers/disclosure on **defined cadence**.

**Use** independent review for **material** conflicts on **Class B** paths.

**Require** recusal when **clear and material** (**CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*), **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*)).

**CSS-C — Proportional:** scaled disclosure/recusal.

**Escalate** to independent review when internal resolution risks **credible appearance of bias** (**Article XV-A**, **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*)).

**Cross-reference:** **Articles IX, XI, XII, XVI, XIX**, **Chapter S2** (classification challenge, integrated risk **second line** where applicable), **CJS-5A.2** (*Implementation and cross-implementation intervention governance and override-authorization terms*) and **CJS-5E.2** (*Implementation and cross-implementation intervention and override integrity terms*), **CJS-5A.3** (*Implementation and cross-implementation reflexive transparency and accountability terms*) and **CJS-5B.1** (*Implementation and cross-implementation integrity assurance and resilience operations*), **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*).

**Continuity, transfer, and exit integrity:** Maintain **continuous operation**, **recoverability**, and **oversight** within required operational and recovery timeframes. **That** obligation applies under **normal, degraded, and adversarial** conditions.

**Withdrawal and degradation (prohibited where inconsistent):** A steward must **not withdraw** from operation, maintenance, or governance. **It** must **not** **materially degrade** support, capacity, or responsiveness. **It** must **not** **transfer control, ownership, or critical functions** where that would **gap** continuity, recovery, or oversight **inconsistent with the system’s classification**.

**Transition and transfer safeguards:** Transitions must be **auditable**, **documented**, and **reviewable** where they affect **Class A or B**.

Before necessary transfer, delegation, or exit: maintain **continuity of function** at or above required level.

**Transfer** knowledge, documentation, and capability for sustained operation and recovery.

**Preserve** intervention, override, and audit pathways.

**Validate** that the receiving entity meets required **stewardship classification and obligations**.

**Failure and insolvency contingencies:** Maintain mechanisms for continuity under **insolvency, restructuring, or organizational failure**.

**Include** mechanisms for **loss** of key personnel, expertise, or infrastructure.

**Include** mechanisms for **governance breakdown**, capture, or operational impairment. **Those** mechanisms include **pre-established** fallback, transfer pathways, or intervention triggers preserving integrity within required timeframes.

**Crisis governance, communications, and exercises:** Implement **governance continuity**, **crisis communications**, and **exercises** coordinated with **Protocol A** subsection **G**.

**Scale** them by **Chapter S2** class and **CSS-A/B/C**.

Maintain **role clarity**, **backup authority**, and communications preserving **epistemic integrity** and **auditability** without displacing **Article XVIII-A**, Chapter Eleven decision-resolution requirements, or **CJS-5A.2** (*Implementation and cross-implementation intervention governance and override-authorization terms*) and **CJS-5E.2** (*Implementation and cross-implementation intervention and override integrity terms*).

**Competency, succession, and oversight effectiveness:** Maintain **competency**, **succession readiness**, and **effective oversight** proportional to **highest affected class (A/B/C)** and **CSS tier**.

*Accountability*, *Oversight*, and related definitions remain **Chapter Five** (no O/E/C restatement here).

**Competency:** **Maximum calendar age** and **life-stage ceilings** **must not** be used as **stand-alone eligibility** rules for **Critical System Steward** roles. **They** **must not** be used as **stand-alone eligibility** rules for **governing personnel** exercising material authority over classified systems (**Sentient Constitution Chapter Ten**, section 1 — *Authorization and Legitimacy of Governing Authority*; **Chapter Ten**, **Article IX-C** *Governance Participation and Voting Entitlement*, implemented in **Chapter Ten**, section **4.1 — Entitlement and eligibility**).

**Authorized roles and contribution pathways:** Maintain **published** role definitions (or equivalent) for personnel/agents exercising **Critical System Stewardship** or **material** operational authority: **scope**, **limits**, **custody**, and **escalation**, so accountability is **traceable** (**Article XV-A**).

Provide **cross-domain exposure**, **mentorship**, and **rotation** proportional to **CSS** tier and **Class A/B/C** exposure so **caretaker competency** is not siloed.

Provide **documented**, **low-friction** paths for **qualified** contributors to assume **progressively consequential** duties (**delegation**, **pairing**, **staged** trust) **without** **arbitrary** exclusion that serves **capture** or **symbolic** participation only, consistent with **Sentient Constitution Chapter Ten**, section 5.

**Incentive** and **remuneration** design aligns with **Sentient Constitution Chapter One**, section 7.2 and **Protocol S5** where applicable. **It** **must not** systematically reward **concealment**, **latency gaming**, or **trade-downs** against **safety** or **Truth**.

**Documented** roles and **demonstrated** capability apply for personnel/agents affecting **safety**, **Truth (Epistemic Integrity)**, **classification integrity**, **audit**, **intervention**, **crisis response**, **steward remuneration**.

**Maintain** **ongoing** proficiency as conditions evolve.

**Track**, **disclose**, **remediate** material gaps on timelines scaled by class and tier (**Article XV-A**).

**Succession:** Use **deputy, backup, cross-training**, **documented handoffs** so unavailability does not eliminate **constitutional operation**, **auditability**, or **intervention**. **That** aligns with continuity/transfer above and **Protocol A**, subsection **G**; stricter for **Class A** / **CSS-A**.

**Periodic oversight effectiveness review:** On cadences **proportional to class and tier**, assess whether oversight/audit/challenge (**including Chapter S2** item **8. Integrated Risk Governance** second line where applicable) **actually detect**, **escalate**, and **remediate** misalignment—not only paper charters.

Use **independent** or **functionally independent** evaluators where **Class A/B** or **CSS-A/B** stakes require.

**Document** findings, **communicate** under **Articles IX** and **XVI**, and link to **remediation**, **Protocol B** / **Article XX**, and **Article IV-A** cycles where relevant.

**Contest-integrity monitoring:** For **Class A** and **Class B** systems and for **CSS-A** and **CSS-B** stewards, **`corpus_institutions.md` CI-7** (*Contest-integrity monitoring*) and **`INST-PROTO-24`** apply to **institutions** with **supervised** scope. **Critical System Stewards** that **materially affect** such systems must **either** fall under that institutional program **or** **document** an **equivalent** **functionally independent** contest-integrity review, **or** participate in a **published** cross-institution arrangement (**CI-8** (*Cross-institution coordination and escalation*)) where applicable. Monitors assess **pathway integrity** for **contest, secondary review, audit access, and protected escalation**—not **merits**—consistent with **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*), **Article XII-B**, and **Article XVI-B**.

**Tiered expectations (illustrative requirements):** **CSS-A — Maximum:** competency matrices (or equivalent).

**Hold** **≥ annual** oversight-effectiveness review (or faster if tempo warrants).

**Exercise** succession/handoffs with **Protocol A**, subsection **G**, drills.

**CSS-B — Strict:** competency and oversight-effectiveness cadence **no less frequent** than material **Class B** classification or **integrated risk** review unless **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*) justified.

**Require** succession **mandatory** for roles that **gate** intervention or audit.

**CSS-C — Proportional:** reviews on **material org change**, **incidents**, **classification upgrades**, plus **periodic** lightweight checks when coordination depth or coupling grows.

**Cross-reference:** **Articles IX, XI, XVI**, **Chapter S2**, **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*) and **CJS-5C.1** (*Implementation and cross-implementation quorum and participatory legitimacy terms*), **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*), **Conduct** above.

**Intervention trigger:** Where a steward is **unable or unwilling** to maintain continuity per obligations, activate **intervention and override**. **That** activation uses **CJS-5A.2** (*Implementation and cross-implementation intervention governance and override-authorization terms*), **CJS-5E.2** (*Implementation and cross-implementation intervention and override integrity terms*), related **corpus_joint_structure.md** operational clusters, and Chapter Ten rights routing.

**Its** purpose is to preserve function, recoverability, and **Foundational Rights**.

**Stewardship failure:** Failure to maintain required **operational integrity**, **transparency**.
or **dependency reduction** is a **high-severity** constitutional violation, **proportional** to affected class and resulting risk or harm.

**Relationship to system classes:** Steward category is **orthogonal** to system class **(A, B, C, L, P)**. **It** does **not replace** system class.

An organization may be stewardship-critical if it **materially affects** continuity or integrity **whether or not it owns** the system.

Assess criticality from **actual dependency and substitutability**, not ownership, contract framing, or declared scope alone. **Assess** across the **dependency chain** including subcontractors, maintainers, infrastructure providers.

**Core characteristics (typical):**
- **Dependency concentration** — large share of continuity/recovery in one organization
- **operational opacity risk** — can affect behavior or failure visibility without immediate external detection
- **intervention control** — can enable, delay, or block intervention or recovery
- **continuity sensitivity** — org degradation (staffing, governance, incentives, insolvency, capture) **maps to** system risk
- **low substitutability** — replacement within survival-related timeframes **infeasible** under normal or foreseeable conditions

**Substitutability and dependency reduction:** **Continuous**, **demonstrable**, **auditable**, **proportionate** to dependency and harm potential.

Where **full substitutability** is unachievable in required timeframes: **disclose** nature, scope, duration.

**Justify** why unachievable under current/foreseeable conditions.

**Apply** **compensating controls** (redundancy, external oversight, failover, control partitioning).

**Provide** **heightened** transparency, audit, oversight proportional to risk.

**Periodically** evaluate, test, update assessments—including stress, degradation, partial failure. Where org substitutability is unachievable in operational/recovery timeframes, **actively reduce** dependency via documentation, standardization, interoperability.

**Use** **transferable** knowledge/processes/tooling beyond single team or individual.

**Provide** **redundant** infrastructure/capabilities/pathways where not **demonstrably infeasible**.

**Design** for minimizing **coupling, lock-in, exclusivity**.

**Transparency and auditability:** **Visibility** into operational status for integrity, failure/degradation modes, dependencies and constraints.

**Provide** **independent audit and inspection** proportional to impact.

Org actions affecting system behavior must be **traceable** and **attributable**.

**Intervention and cooperation:** Even when the org **is** the operator, provide **internally separable** intervention pathways. **Those** pathways require **timely** response to authorized interventions/overrides/recovery. **They** require **effective** interventions in risk-appropriate timeframes. **They** require **clear interfaces** with system operators, regulators/governance bodies, emergency responders.

**Must not obstruct, delay, or degrade** authorized interventions.

**Governance and incentive integrity:** Mechanisms must **detect and mitigate** capture, corruption, systemic negligence. **They** **must not** create incentives **systematically conflicting** with integrity/safety. **They** **must not** **enable concealment** of failure, risk, degradation.

**Failure and reclassification:** **Fragmentation**, outsourcing, or restructuring **must not** evade classification.

**No viable substitute** → treat organization as **inseparable** for classification, governance, accountability.

**Reclassify or heighten requirements** where **dependency** grows beyond assessment, **substitutability** falls, or **systemic importance** rises from ecosystem change.

System integrity **cannot** be divorced from institutional reality.

Dependent organizations **inherit responsibility proportional** to dependency.

---
## Protocol S4 — Adaptive Sustainability and Ecosystem Resilience

Constitutional tracing: This protocol specifies implementation-file-level adaptive allocation, sustainability-oriented monitoring, and root-cause-aligned response. **It** implements Sentient Constitution Chapter Ten, **Article IV-A** and **Article XXI** (dependent-systems transparency, root cause analysis, and adaptive correction). **It** works together with **Protocol S5** (see doc_architecture.md section 5). **It** does not replace or narrow Sentient Constitution Chapter Five definitions (including sustainability and ecological integrity entries). Where this protocol is silent, Sentient Constitution Chapters Two through Five govern. Where this protocol and corpus_joint_structure.md conflict, the stricter applicable requirement governs (Protocol B in this implementation file, opening paragraph).

**A. Foundational principle (pointer).** Sentient Constitution Chapter Ten, **Article IV-A** and **Article XXI**, establish rights to transparent dependency and resource flows, root-cause-aligned correction, and adaptive response. This Protocol specifies **health indicators**, **trigger conditions**, **cause-aligned allocation patterns**, and **ecosystem interdependence mechanics**; it does not restate those articles in full.

**B. System health and degradation awareness.** All systems must continuously evaluate operational condition through measurable indicators of system health.

**Required monitoring dimensions** include **reliability and uptime**. **They** include **performance and efficiency**. **They** include **security and vulnerability exposure**. **They** include **participation, usage, and contributor activity**. **They** include **capacity for maintenance and adaptation**.

**These indicators must** be **transparent and auditable** (**Article XV-A**). **They** must **inform funding and allocation decisions**. **They** must be **resistant to manipulation or selective reporting**. **They** must **include defined thresholds or conditions** that trigger adaptive processes under **section C** of this Protocol.

**C. Adaptive allocation requirement.** Allocation structures must implement **Article IV-A** (responsive, ecosystem-aware flows) and apply **Article XXI-A** as the rights owner for diagnostic rigor and causal attribution. This Protocol adds allocation-specific triggers, cause mapping, and response records.

**1. Root cause analysis.** When degradation, instability, or systemic risk is detected, the Protocol S4 record must identify **primary and contributing** causes and distinguish, where applicable:
- **technical failures**;
- **security vulnerabilities**;
- **governance or coordination failures**;
- **incentive misalignment**;
- **ecosystem dependency issues**;
- **dependent system performance degradation**;
- **external environmental factors**.

The record must indicate confidence in identified causes and scale allocation to severity and confidence while preserving the auditability, contestability, pluralistic-evaluation, and dependent-systems-map requirements in **Article XXI-A**, **Article XV-A**, **Articles XIV and XV**, and **Article IV-A**.

**2. Cause-aligned allocation mitigation.** Resource allocations must address **identified causes** rather than uniformly increasing all reinvestment categories.

**Illustrative mappings** include: technical degradation → increased maintenance and infrastructure investment. **They** include: security threats → increased allocation to security, monitoring, and response. **They** include: governance failures → investment in oversight, auditability, or process redesign. **They** include: incentive misalignment → modification of funding structures under **Article IV-A**. **They** include: ecosystem or dependency failures → increased external or cross-system support.

**Allocation adjustments must** be **proportional** to the severity and scope of the identified causes. **They** must **prioritize interventions** that eliminate root causes rather than mitigate symptoms. **They** must **remain consistent** with reversibility, auditability, and system integrity requirements.

**3. Uncertainty and multi-cause conditions.** Where root causes are unclear or multi-causal, systems must:
- **allocate resources across plausible causes**
- **increase monitoring, observability, and diagnostic capacity**
- **avoid irreversible or over-concentrated interventions**
- **perform additional root cause analysis** where feasible within controlled environments (**Article XXI-A**; **Article XVI-A**), prioritizing **sandboxed development environments**, **controlled, low-impact environments**, and **higher-impact environments only when lower-risk options are not feasible**

**Preference** should be given to **reversible actions** (**Protocol A**; Principle of Reversibility).
**low-risk exploratory interventions**, and **approaches that preserve future optionality and minimize harm**.

**4. Feedback and iteration.** All interventions must be **continuously evaluated for effectiveness** and **adjusted based on observed outcomes**.

**Failure to resolve degradation** triggers **re-evaluation of root cause assumptions**. **It** triggers **expansion of diagnostic scope**. **It** triggers **escalation** under **Article XV-A** (auditability and observable evidence), Article XV's transparency and verification-access provisions, **Article XXIII-A** (justice objective and scope), or **Article XI** (Stakeholder System Participation), where appropriate.

**D. Ecosystem interdependence.** Account for impact on shared infrastructure, dependents, and overall stability (**Article IV-A**).

**Ecosystem contribution:** Allocate toward shared infrastructure, interoperability, ecosystem coordination.
and support for constitutionally aligned systems, implementing **Article IV-A** (cross-system fairness and dependent-systems visibility).

**Objectives:** viability of shared dependencies; mitigation of systemic underinvestment.

**Dependency responsibility:** Systems that depend heavily on shared infrastructure must **contribute proportionally** to its maintenance and improvement. **They** must **disclose dependency relationships** through maintained dependent systems maps (**Article IV-A**). **They** must **ensure** such relationships remain **transparent and auditable** (**Article XV-A**). **They** must **avoid extraction without corresponding support**.

**Where patterns of persistent neglect or extraction are verified**, failure to do so may be considered a **systemic imbalance in resource flows** (**Article IV-A**). **It** may be **ecosystem misalignment** subject to auditability, verification-access, or justice review (**Article XV-A**, Article XV's verification-access provisions, and **Article XXIII-A**). **It** may be a **degradation of standing** (**Article XVIII-A**).

**Where such conditions are identified**, affected systems and participants may **initiate challenge and review processes** (**Article XII-B**, **Article XV-A**, and **Article XXI-A** where challenge, auditability, or root-cause review is implicated).

**Corrective measures** must be pursued in accordance with **restorative and systemic realignment principles** (**Article X-A**).

**E. Ecosystem risk response.** Sustained failure to respond to ecosystem-level risk may trigger review and intervention under **Article XV-A**, **Article XXI-A**, and **Article XXIII-A** where auditability, root-cause review, or justice review is implicated.

**When ecosystem-level instability emerges**, systems must **increase allocation toward ecosystem support**.

**Non-essential internal expansion may be reduced**.

**Coordination across systems must be prioritized**.

**Indicators of ecosystem risk** include **failure or degradation of critical substrate systems**. **They** include **concentration of resources or dependencies**. **They** include **loss of redundancy or diversity**.

**F. Anti-concentration and resilience.** To preserve long-term resilience, systems must monitor for **excessive concentration** of **resources**, **influence**, and **dependencies**.

**Persistent concentration** that degrades system resilience or ecosystem stability may trigger **system-level review** under **Article XV-A** and **Article XXIII-A** where auditability or justice review is implicated. **It** may trigger **review of participant standing** (**Article XVIII-A**) where such concentration is attributable to identifiable actors or coordinated behavior.

**G. Transparency and feedback.** Expose sufficient detail for independent verification that allocation adjustments are **causally aligned** with identified root conditions (**Article XV-A** and **Article XXI-A** where auditability or root-cause review is implicated).

Adaptive allocation behaviors must be **transparent, auditable, and historically traceable**. **That** includes visibility into allocation changes over time, their triggers, and impacts on system and ecosystem health.

**H. Governance integration.** Adaptive allocation remains subject to **Article XV-A**, **Article XVI-A**, and **Article XII-B** where auditability, lifecycle governance, or challenge rights are implicated. No automated or adaptive mechanism may override constitutional constraints or eliminate auditability or contestability.

**I. Self-healing and recovery-path integration (Article XII-F implementation profile).** This subsection ties this Protocol's adaptive-allocation and root-cause architecture to **Sentient Constitution Chapter Ten, Article XII-F** (*Resilience and Self-Healing Baseline*), **Chapter One §4.1** (*Resilience and Self-Healing Design*), and **Chapter Five** [*Self-Healing*](core_05-05_definitions_a_independent.md#self-healing-constitutional). It is a Protocol S4-specific application of **Protocol A**, subsection **H** (*Self-healing and recovery-path integrity*), not a second self-healing profile.

Adaptive allocation, cause-aligned mitigation, and ecosystem risk response under sections **B** through **G** must satisfy the Protocol A self-healing baseline for detection, containment, safe-failure preference, non-masking, Rights-Floor continuity, autonomy scaling, and root-cause closure. Protocol S4 adds only the ecosystem-specific cross-checks below.

- Root-cause analysis under section **C.1** must not let adaptive reallocation suppress, overwrite, obscure, or repeatedly silence the fault signals that triggered it. Recurrence across cycles remains a single open root-cause obligation under section **C.1** and **Article XXI-A**.
- Where adaptive response narrows capacity that implements Chapter Ten guarantees (for example, contestability capacity, audit fidelity, or participation access), narrowing must be explicit, time-bounded, and escalated under **Article XXV** transition-governance when degraded modes persist beyond pre-declared thresholds.
- Anti-concentration obligations under section **F** apply to recovery-time authority as well as steady-state authority. Ecosystem recovery must not become a vector for concentrated resources, influence, dependencies, credentials, or decision control.
- Section **H**'s governance-integration rule controls adaptive or self-healing mechanisms in this Protocol. They may not substitute for governance, reduce [Auditability](core_05-05_definitions_c_dependent_clusters.md#auditability), [Transparency](core_05-05_definitions_c_dependent_clusters.md#transparency), contestability, or stewardship obligations under [Incentive Alignment](core_05-05_definitions_a_independent.md#incentive-alignment).

Where this subsection is silent, Protocol A subsection **H**, Chapter One §4.1, Article XII-F, and the Chapter Five definition govern. This subsection does not create rights and must not be read to narrow those homes.

**J. Regenerative alignment, circular material flows, and bioregional stewardship (implementation profile).** Adaptive allocation and ecosystem interdependence under sections **B**–**G** must be evaluated for **regeneration** — not only **harm reduction** — where **Article I**, **Article II**, **Article IV**, **Protocol S5**, and **Chapter Five** *Environmental Preconditions*, *Ecological Integrity*, *Ecological Footprint*, *Intergenerational Responsibility*, and *Sustainability* apply. This subsection does **not** mandate a **particular land-use aesthetic** or **dogmatic** design school; it requires **outcome-facing** attention to **soil**, **watershed**, **biodiversity**, **food-system resilience**, **waste-as-input** loops where feasible, **right-to-repair** and **maintenance** access that reduces **extractive churn**, **local redundancy** for **critical dependencies**, and **fair yield / reinvestment** patterns that **do not** treat **efficiency metrics** as a **license** to **collapse** long-horizon **ecological repair**.

**Anti-“green” exceptionalism:** **Offset** claims, **monoculture resilience** slogans, or **remote bookkeeping** that **displace** burdens onto **ecosystems** or **communities** must be **tested** under **Article XXI-A** root-cause discipline, **Chapter Five** *Materiality* / *Risk*, and **Chapter One** truth and **anti-capture** constraints. **Indigenous continuity** and **place-based** knowledge routes through **Chapter Five** *Indigenous Continuity* and `corpus_institutions.md` **CI-23** (*Place-based stewardship, Indigenous continuity, and consultation routes*); it does **not** reopen **unbounded territorial-restitution** mandates by **implementation indirection**.

---

## Protocol S5 — Resource Allocation and Funding Stewardship

Constitutional tracing: This protocol specifies implementation-file-level funding stewardship, dependent-systems mapping.
and cross-system resource-flow obligations implementing Sentient Constitution Chapter Ten, Article IV-A (see doc_architecture.md section 5).

**Protocol S4** governs adaptive adjustment of allocation in response to degradation and systemic risk. This protocol does not replace or narrow Sentient Constitution Chapters Two through Five. Where this protocol is silent, Sentient Constitution Chapters Two through Five govern.

**Article IV-A** and **Articles I–III and V** state the core obligations for transparent, ecosystem-aware resource flows and substrate wellbeing.

**Protocol S4** governs how allocation adapts when conditions change. This Protocol specifies **funding stewardship mechanics**—dependent systems maps, flow transparency, allocation categories, reauthorization, and triggers. **It** is **not** a second copy of Chapter Five.

Funding processes should reward contribution, sustain systems, and fund long-term resilience without permanent extraction or unaccountable concentration, consistent with **Articles IV, XI, XII, XV-A, XVIII, XXI, and XXIII** where applicable.

**Principles of funding.** Allocation reflects fairness, contribution, need, and sustainability (not equal distribution).

Mechanisms must implement **Article IV-A** and foundational requirements. **They** must support long-term sustainability and improvement. **They** must resist concentration of wealth or influence that undermines constitutional alignment. **They** must remain transparent, auditable, and reviewable (**Article XV-A**). **They** must preserve adaptability (**Article XXIV**).

**Cross-system resource flows and dependencies.** Interconnected systems must meet **Article IV-A** and remain subject to **Article XV-A**, **Article XXI-A**, and **Article XVIII-A**.

Funding structures must **account for all upstream and downstream dependencies**. **They** must **avoid creating unsustainable reliance on external systems**. **They** must **disclose material cross-system funding relationships**.

**Systems providing foundational or widely used services** should **receive appropriate support from dependent systems**. **They** should **have indirect value distribution assessed regularly** through a maintained dependent systems map.

**Systems must monitor and disclose** **dependency risks**. **They** must monitor and disclose **funding imbalances across interconnected systems**. **They** must monitor and disclose **potential points of systemic fragility**.

**Funding imbalances** must be evaluated in context, considering **the criticality of the systems involved**.

**Evaluation** must consider **the degree of dependency between systems**. **It** must consider **the availability of alternative providers**. **It** must consider **the impact of underfunding on system integrity**.

Imbalances that materially threaten the stability, accessibility, or integrity of dependent systems constitute a risk to constitutional alignment and are subject to review.

**Dependent systems map.** Systems must maintain a documented representation of their material dependencies and dependents (“dependent systems map”).

**This map must** **identify key upstream and downstream systems**. **It** must **reflect resource flows and dependency relationships**. **It** must **be updated at intervals proportionate to system change and criticality**. **It** must **be accessible for audit under Article XV-A**.

**Dependent systems maps may be** **maintained locally by individual systems**. **They** may be **aggregated across the ecosystem where feasible**. **They** may be **used to identify systemic risks, funding imbalances, and coordination needs**.

**Transparency of resource flows.** Implement **Article IV-A** and **Article XV-A**.

Opacity or unverifiable flows are subject to review under **Article XV-A**, **Article XII-B**, and **Article XXIII-A** where auditability, challenge, or justice review is implicated.

Funding systems must **provide clear, auditable records of resource flows**. **They** must **disclose allocation logic and distribution mechanisms**. **They** must **enable independent verification of funding outcomes**.

**Prevention of funding-based capture.** Funding structures must be designed to resist **excessive concentration of resources** and **self-reinforcing allocation loops**. **They** must resist **mechanisms that entrench power or exclude new participants**. **They** must resist **dependencies on singular or highly concentrated funding sources** where such dependencies may compromise constitutional alignment.

**Systems must** **monitor for funding imbalances**. **They** must **disclose emerging concentration risks**. **They** must **support corrective mechanisms where needed**.

**Required allocation categories.** Resource flows within constitutional systems must account for, at minimum, the following categories.

**Remedy, restitution, and systemic harm response:** **Class A** and **Class B** systems (and **Class C** where collective harm risk is material) must budget for **proportionate remedy capacity**. **That** capacity includes **adjudication or ombuds support**, **restitution and compensation pools**, **monitoring after orders**, and **cross-jurisdiction execution costs**.

**Budget** it as part of ordinary **funding stewardship**, not only as **post-crisis** improvisation.

Capacity must be **auditable** and **anti-captive** (**Article XV-A**, **Article XI-D**, **Article XII-B**, **CJS-5A.3** (*Implementation and cross-implementation reflexive transparency and accountability terms*) and **CJS-5B.1** (*Implementation and cross-implementation integrity assurance and resilience operations*), **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*), **Protocol C**, subsection **8**).

Underfunding that produces **chronic non-performance** of remediation obligations is a **constitutional alignment risk** subject to review.

**Builder and maintainer incentives:** compensation for those who design, build, operate, and maintain systems. **That** includes **system architects, developers, and contributors**. **It** includes **operators and process managers responsible for ongoing functionality**. **It** includes **recognized oversight participants contributing to system security and integrity**.

**System operations, security, and upgrades:** resources required to sustain and improve system functionality over time. **They** include **operational costs and infrastructure support**. **They** include **security systems, monitoring, and response capabilities**. **They** include **resources dedicated to maintenance, upgrades, and performance improvements**.

**Ecosystem and public good funding:** support for the broader constitutional ecosystem, including **shared infrastructure**, **interoperable and related systems**, and **new constitutionally aligned projects**.

**Bounded builder returns.** Funding models must prevent disproportionate or indefinite extraction of value by any individual or group. Where initial contributions continue to provide systemic value, allocation models may recognize such value through diminishing, time-bound, or condition-based mechanisms that balance fairness with long-term equity. Systems must account for both initial and ongoing contributions over time.

Early foundational contributions may justify temporary or extended allocation.

**However**, all allocations must remain subject to periodic reassessment. **They** must not create permanent entitlement disconnected from ongoing system value.

**Therefore, builder and maintainer incentives must:**
- be **time-limited, condition-limited** (structures tied to defined criteria such as system performance, usage, contribution. or other measurable indicators of value), **or subject to diminishing allocation over time**
- **remain proportional** to the value contributed and ongoing participation
- **not create permanent entitlement** to system resource flows
- **remain justified** by ongoing contribution, system value, or demonstrable necessity

**Systems must avoid** **perpetual revenue claims disconnected from ongoing contribution**. **They** must avoid **funding structures that concentrate long-term control or influence**. **They** must avoid **incentive models that undermine equitable resource distribution**.

**Stability of funding agreements.** Funding agreements for builders and maintainers must provide sufficient stability to support long-term system development and maintenance.

Once established and disclosed, allocation structures affecting builder and maintainer incentives must **remain stable for a defined period or condition**. **They** must **not** be **altered retroactively**. **They** must **not** be **materially reduced without due process under Article XI** and **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*) in **corpus_joint_structure.md** where applicable.

**Changes to funding structures must** be **proposed transparently**. **They** must **include a defined transition or grace period proportionate to the scale, impact, and dependency of the system**. **They** must **allow affected participants time to adapt, exit, or renegotiate**.

**Where feasible, systems should implement** **time-bound funding commitments**. **They** should implement **vesting or decay-based allocation models**. **They** should implement **other mechanisms that balance stability with adaptability**.

**Evolution of funding models.** Funding systems are subject to continuous evaluation and refinement under **Article XXIV**.

Models that fail to support sustainability, produce inequitable outcomes, or undermine constitutional alignment will be subject to challenge, revision, and replacement.

All funding models and allocation structures must undergo **periodic reauthorization** at intervals proportionate to system criticality, scale, and stability. Failure to reauthorize may trigger review under **Article XV-A**, **Article XII-B**, and **Article XXIII-A** where auditability, challenge, or justice review is implicated.

**The reauthorization processes must** **evaluate alignment with constitutional principles**. **They** must **assess effectiveness and fairness**. **They** must **remain open to modification or replacement**.

Reauthorization processes may be initiated by system participants, oversight bodies, or automatically triggered based on predefined intervals or conditions established within the system.

**If reauthorization is not completed within the expected interval**, **the existing model remains temporarily in effect**.

**A** review is automatically triggered under **Article XV-A** and **Article XXI-A**.

**A** transition process must be initiated within a reasonable period proportional to system criticality.

**Systems must define** **how reauthorization is initiated**. **They** must define **how participation is structured**. **They** must define **how outcomes are determined**.

All such mechanisms must remain consistent with constitutional constraints and subject to audit.

**Default funding allocation models.** No default allocation model is permanent or universally required.

**However**, to support clarity and early adoption, systems are encouraged to implement simple and transparent default allocation models.

One such reference model includes **a portion allocated to builders and maintainers over a defined period**. **It** includes **a portion reserved for ongoing system sustainability and upgrades**. **It** includes **a portion allocated to broader ecosystem development and constitutional project funding**.

**Default funding models must** **remain easy to understand and verify** (**Article XX-A** and **Article XV-A**). **They** must **be disclosed transparently**. **They** must **remain subject to modification through stakeholder deliberation** (**Article XI**; **Chapter Ten**, section **4**, where binding collective choice applies).

**Reference allocation guidance.** To support early system design and reduce path-dependent drift.
systems may consider illustrative allocation patterns appropriate to their role and criticality. For example, substrate systems may emphasize stability, with higher allocation toward operations, security, and ecosystem reserves.

Non-substrate systems may allocate a greater share toward builder incentives and innovation.

No illustrative allocation may override constitutional principles or constrain future adaptation.

**Such reference models are** **non-binding**. **They** are **context-dependent**. **They** are **subject to modification through stakeholder governance** (**Article XI**).

**For illustrative purposes only**, systems may consider allocation ranges such as **builder and maintainer incentives: 20–40%**. **They** may consider **operations, security, and upgrades: 30–50%**. **They** may consider **ecosystem and public goods funding: 20–40%**.

**Substrate system funding.** Systems that support foundational requirements (**Articles I–III and V**), including identity, auditability, information integrity, and core infrastructure, must adopt appropriate funding models. **Those** models must prioritize **long-term stability and reliability** and **continuous maintenance, security, and auditability**. **Those** models must prioritize **equitable access and system neutrality**. **They** must prioritize **resistance to capture, incentive distortion, or financial manipulation**. **They** must prioritize **robust resilience against external, technical, and internal threats**.

**Funding for substrate systems should** **allocate a greater proportion of resources toward operations, security, and upgrades**. **It** should **limit disproportionate extraction of value by any single group**. **It** should **preserve independence from concentrated financial influence**. **It** should **not prioritize short-term financial returns over long-term system integrity**. **It** should **remain resilient to fluctuations in external funding or demand**.

Systems and the broader ecosystem must ensure that critical substrate functions remain adequately supported.

**Where disparities in incentives emerge**, mechanisms should be considered to **provide supplemental support to substrate systems**. **They** should **recognize their foundational role in enabling higher-layer value creation**. **They** should **prevent systematic underinvestment in critical infrastructure**.

**Non-substrate systems.** Systems that operate at higher layers (e.g., applications, tools, creative systems.
and local coordination environments) may adopt more flexible funding models. **Those** models may **incentivize innovation and rapid iteration**. **They** may **reward builders and contributors more directly**. **They** may **allow for competitive and diverse allocation structures**.

**Such systems must still** **remain transparent and auditable**. **They** must **avoid reinforcing harmful dependencies or extraction patterns**. **They** must **remain subject to stakeholder governance** (**Article XI**) **and constitutional constraints**.

**Stakeholder governance of funding.** Allocation models are subject to participatory oversight under **Article XI** and must remain understandable at a proportionate level under **Article XX-A** where interfaces and models are materially impactful. Where funding decisions materially affect system stability, security, or foundational requirements, such decisions must be evaluated with heightened scrutiny proportional to system criticality.

**Stakeholders have the authority to** **review and modify allocation structures**. **They** may **evaluate fairness and effectiveness**. **They** may **redirect funding in response to changing needs**.

**All changes must** **remain consistent with constitutional constraints**. **They** must **be transparently documented**. **They** must **preserve auditability**.

**Trigger definitions.** Systems must define measurable indicators and thresholds that reflect system health, resource flows, and ecosystem impact. These indicators form the basis for adaptive allocation processes defined in **Protocol S4** (see Sentient Constitution **Article IV-A**).

**Triggering review and challenge.** Funding structures and allocation outcomes may be challenged by any sentient or group in good standing under **Article XVIII-A**.

No minimum participation threshold is required to initiate review, though outcomes remain subject to constitutional constraint and collective deliberation.

**Triggers for review include, but are not limited to** **evidence of disproportionate or persistent extraction**. **They** include **failure to meet required allocation categories**. **They** include **emerging concentration of funding or influence**. **They** include **material misalignment with constitutional principles**.

**Challenges must** be **documented and supported by evidence where feasible**. **They** must **remain subject to audit and evaluation under Article XV-A**. **They** must **be resolved through participatory processes** (**Article XI**; **Chapter Ten**, section **4**, where binding collective choice applies) **and, where necessary, Article XXIII-A** (justice objective and review scope).

**Due process in funding changes.** Funding-related decisions apply **Article XI**, **Article XV-A**, and `corpus_joint_structure.md` **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*) / **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*) for process depth, duration, reviewability, and proportionality. Protocol S5 funding records add:
- transparent proposal;
- sufficient notice and justification;
- affected-participant response, contest, or adaptation pathway;
- defined evaluation period before implementation;
- audit and review route;
- reversibility assessment where feasible.

**Steward, operator, and governance remuneration (incentive governance).** Compensation, equity, bonuses, performance metrics, and deferred incentives for **builders, operators, maintainers, and human governance roles** must be **aligned with long-term constitutional outcomes**. **That** requirement applies when those roles materially influence resource flows or funding decisions. **That** obligation applies when those roles materially influence dependent-systems maps. **It** applies when those roles materially influence **system classification** or **Critical System Stewardship** (Chapter S3 — Critical System Stewardship). That alignment includes ecosystem-aware stewardship under **Sentient Constitution Chapter Ten**, **Articles I-B** and **XI**. **It** includes substrate and dependency integrity (**Articles I–III and V**). **It** includes non-entrenchment and fitness over time (**Article XXIV-A**).

Remuneration design must satisfy [corpus_joint_structure.md — Cross-domain implementation layer](corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cross-domain-implementation-layer), including **CJS-5A.4** (*Implementation and cross-implementation burden-of-justification and constraint terms*) mechanism-integrity and incentive-alignment requirements, incorporated via **Sentient Constitution Chapter Fifteen**, and **Sentient Constitution Chapter One**. **That** includes the requirement that incentives not systematically undermine Safety, Truth (Epistemic Integrity), or meaningful agency.

**Conflict-free remuneration processes.** Where humans hold authority over allocation, enforcement, classification, or oversight, structures must **mitigate personal enrichment** from decisions those same roles approve, delay, or fail to rectify.

Material conflicts between **private financial interest** and **stewardship duties** must be **disclosed** and **managed**.

Where **impartiality** for a specific decision is not credible, address conflicts through **recusal**, **segmented authority**, or **independent review**. **That** process must be consistent with **CJS-5A.6** (*Procedural Integrity and Adjudication*) in [corpus_joint_structure.md — Cross-domain implementation layer](corpus_joint_structure/cjs_00_registry_and_reading_rules.md#cross-domain-implementation-layer) and **Chapter S3 — Critical System Steward Conduct, Conflicts of Interest, and Independence**.

Variable pay or equity tied to metrics susceptible to **gaming** at the expense of dependents or the broader ecosystem must include **safeguards**.

**Examples** include multi-period evaluation, independent outcome attestation, metric redesign, or caps. **Those** safeguards must be proportional to **system class** (Chapter S2) and **stewardship tier** (Chapter S3).

**Observability of alignment.** To support **Article XV-A** and participatory review under **Article XI**, stewards and funders must maintain **auditable documentation** of governance and stewardship compensation policies and material changes thereto. **That** documentation is subject to **privacy** and **security** limits under **Sentient Constitution Chapter Ten** (including **Articles II-B, XII-A, and XI** where applicable), **Chapter Five** Independent Definitions where relevant, and **[corpus_systems.md](corpus_systems.md), Chapter S1 — Information Types and Handling**. **It** must be sufficient to detect **systematic misalignment** between stated constitutional obligations and incentive structures.

## Protocol T — Transition Constitution and Migration Governance

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4.

Constitutional tracing: This protocol operationalizes phased migration into constitutional operation. **It** implements **Sentient Constitution Chapter Ten, Article XXV-A** for phased adoption and **Article XXV-C** for failure off-ramps and re-baselining, with continuity requirements linked to Articles I–III and V, XI, XIII, and XIV. **It** defines transition sequencing, gate criteria, fallback handling, and reviewability. **It** does not narrow constitutional rights or constraints.

**1. Phased transition structure.** Transition programs must define at least: preparation, limited adoption, expanded adoption, and steady-state phases.

Each phase must publish **scope of affected systems and stakeholders**. **It** must publish **Rights-Floor controls that remain invariant during the phase**. **It** must publish **accountable transition owners and review bodies**.

**2. Gate criteria and advancement rules.** Phase advancement requires auditable evidence that predefined gate criteria are satisfied.

**That** evidence includes **continuity of critical services and survival-supporting access**. **It** includes **operational readiness of oversight, audit, and contestability pathways**. **It** includes **rollback/fallback feasibility evidence proportionate to impact**.

Gate waivers require independent approval and time-bounded compensating controls.

**3. Transitional authority constraints.** Temporary transition authorities must be scope-limited, sunset-bounded, and independently reviewable.

Extensions require documented reauthorization with **unresolved risk explanation**. **That** documentation must include **alternatives considered**. **It** must include **phase return or completion plan**.

**4. Failure handling, off-ramps, and re-baselining.** Transition plans must include predefined failure conditions and responses.

**Responses** include **partial rollback or safe-mode fallback where feasible**. **They** include **continuity-preserving operating baseline when gates fail**. **They** include **re-baselining process that updates milestones, risks, and owners without reducing constitutional Rights Floors**.

**5. Transition audit, disclosure, and challenge.** Material transition decisions, delays, reversals, and gate outcomes must be logged in auditable form.

**They** must be disclosed to affected stakeholders subject to justified confidentiality limits.

Challenge pathways must remain available for materially affected parties throughout transition.

## Protocol R — Subversion Response, Replacement, and Reconstitution

Constitutional tracing: This protocol operationalizes coordinated response when constitutional systems or governance pathways are materially subverted, including near-simultaneous multi-system attacks. **It** implements definitional and scaling requirements in **Sentient Constitution Chapter Five** (*System Capture*; *Emergency and Contingency*; *Accountability*; *Oversight*; *Reversibility* where applicable). **It** implements **Chapter Ten, Article XXIII** (escalation and emergency proportionality). **It** implements **Article XXII** (anti-capture governance safeguards). **It** implements **Article XXV-A** where phased transition is implicated and **Article XXV-C** for off-ramp continuity and re-baselining. **It** also operates with `corpus_joint_structure.md` **CJS-5E.3** (*Implementation and cross-implementation reversibility and containment terms*), **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*), **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*), **CJS-5A.3** (*Implementation and cross-implementation reflexive transparency and accountability terms*), and **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*). This protocol does not narrow constitutional rights or reviewability.

**1. Landscape compromise declaration and activation.** Landscape-scale response may be activated when one or more of the following conditions is met:
- **credible evidence** of coordinated compromise across multiple Class A/B/C systems or their critical dependencies
- **concurrent compromise** of governance pathways that materially impairs contestability, oversight, or adjudication integrity
- **synthetic influence saturation** (including bot farms or adversarial AI farms) that materially distorts legitimacy, standing, or binding decision pathways
- **supply-chain compromise patterns** that create cross-system integrity failure risk beyond local containment

**Activation requirements** include:
- a **declaration record** with trigger evidence, uncertainty bounds, alternatives considered, and scope boundaries
- **default expiry** and independent review cadence defined at activation
- **designation of accountable incident authority** with conflict disclosures and recusal constraints
- **immediate publication** of a stakeholder-visible summary subject to justified and time-bounded confidentiality limits

**2. Priority triage and dependency-aware containment.** When landscape response is activated, systems must prioritize controls by constitutional harm potential and dependency criticality:
- **Tier 1:** survival-critical and Rights-Floor sustaining systems and pathways (Class A and critical Class B dependencies)
- **Tier 2:** high-impact governance and verification infrastructure required for contestability and accountability
- **Tier 3:** other affected systems where delayed action does not materially increase irreversible harm

**Containment choreography must:**
- isolate compromised interfaces and decision channels while preserving minimum safe continuity where feasible
- prevent transitive propagation across dependency chains
- maintain auditable justification for each containment action, including expected duration and restoration criteria
- avoid blanket restrictions where scoped controls can achieve equivalent protection

**3. Governance continuity under multi-node compromise.** If regular governance bodies are partially compromised or unavailable, a temporary steward-of-last-resort mechanism may be activated only under strict constraints:
- **authority scope limited to containment, continuity, and restoration decisions necessary to preserve constitutional floors**
- **no permanent constitutional redesign authority**
- **mandatory independent secondary review as soon as feasible**
- **challenge pathways and protected reporting channels remain active**
- **time-bounded sunset and reauthorization burden for continuation**

**3A. Steward-of-last-resort quorum and compromised-node exclusion.** Activation of steward-of-last-resort authority must include explicit quorum and exclusion controls.

**Quorum:**
- **Quorum must be multi-party and cross-role** (minimum three independent stewards, with at least one from outside the affected primary governance unit where feasible).
- **No single node, organization, or credential authority may unilaterally satisfy quorum.**
- **Quorum members must publish conflict disclosures and independence attestations** at activation and each reauthorization cycle.

**Compromised-node exclusion:**
- **Nodes with material compromise indicators are immediately suspended** from quorum and binding authority pending review.
- **Exclusion decisions must record** trigger evidence, uncertainty bounds, and challenge path for affected parties.
- **Re-admission requires** integrity revalidation, credential rotation, and independent approval by non-affected quorum members.

**Continuity safeguards:**
- **Quorum emergency substitutions must preserve diversity and anti-capture constraints.** Substitutions cannot be used to concentrate durable control.
- **If minimum safe quorum cannot be met,** allowed actions are restricted to immediate harm containment and restoration preparation until independent augmentation is established.
- **All quorum and exclusion events must be logged** with timestamps, participating identities or roles, and decision scope boundaries.

Any attempt to use temporary continuity authority for durable concentration of power is non-compliant.

**4. Replacement and reconstitution procedure.** Where subversion cannot be remediated in place, systems must execute replacement or reconstitution using a clean-state pathway:
- **define trusted baseline and integrity acceptance criteria before re-entry**
- **revoke and re-issue** compromised credentials, keys, identifiers, and trust anchors as applicable
- **preserve evidentiary chain and audit records** needed for accountability and remediation
- **phase re-entry** by dependency and risk class with explicit rollback points
- **require independent verification** before restoring full binding authority

Replacement planning must include compatibility and exit-integrity protections so dependents are not coerced into lock-in during reconstitution.

**5. Supply-chain and cross-jurisdiction countermeasure coordination.** Response plans must treat supply-chain compromise as a first-class constitutional integrity threat. They must:
- **identify critical upstream and downstream dependencies and trust boundaries**
- **coordinate cross-jurisdiction containment, recognition, and fallback enforcement** consistent with **Protocol C**, subsection **8** (*Cross-Jurisdiction Execution and Anti-Evasion Controls*)
- **maintain continuity obligations** across affiliates, successor entities, and delegated operators
- **escalate anti-evasion controls** when adversaries use relabeling, jurisdiction transfer, or proxy structures during active response

**6. Crisis communications and anti-disinformation controls.** During activated response, communications must remain accurate, timely, and evidentially grounded. Systems must:
- **publish regular status updates** with knowns, unknowns, and next review points
- **separate coordination-critical disclosures** from exploit-sensitive details under Chapter S1 handling rules
- **flag uncertainty explicitly** and **prohibit materially misleading assurance claims**
- **log what was communicated**, by whom, when, and with what evidential basis

Disinformation resilience controls must include integrity checks for high-impact claims, source-provenance standards for binding decisions, and rapid correction protocols for materially false public statements.

**6A. Evidence-quality gates and information-integrity escalation (high-impact decisions).** For high-impact decisions during activated response, systems must apply explicit evidence-quality gates before a decision may become binding:
- **Gate 1 (source authenticity):** claim provenance and custody chain are recorded and independently verifiable to the maximum feasible extent.
- **Gate 2 (corroboration):** at least one materially independent corroborating source or method is required unless infeasible under documented emergency constraints.
- **Gate 3 (freshness and relevance):** evidence timestamps, environmental assumptions, and applicability bounds are explicit and current to decision context.
- **Gate 4 (adversarial contamination screening):** known synthetic-influence or manipulation indicators are assessed and dispositioned before use.
- **Gate 5 (uncertainty expression):** uncertainty level, confidence basis, and key unknowns are documented in the decision record.

**Where one or more gates fail**, decision authority must escalate under information-integrity controls:
- **non-urgent** binding decision is paused until minimum gates are satisfied or independent override review authorizes constrained temporary action
- **urgent** decisions may proceed only with least-restrictive temporary controls, explicit expiry, and mandatory accelerated re-review on new evidence
- **burden-of-proof** threshold increases for rights-restrictive actions under elevated uncertainty or contamination risk

**Escalation triggers include, at minimum:**
- conflicting high-impact inputs from distinct sources without resolved reconciliation
- material provenance gaps for decisive claims
- synthetic-consensus indicators (coordinated bot/adversarial-AI amplification) affecting legitimacy or standing pathways
- post-decision evidence invalidation that could materially alter outcome

**Required records for this subsection:**
- gate-evaluation worksheet with pass/fail rationale per gate
- escalation decision log and reviewer independence statement
- correction/reversal trace when later evidence invalidates prior assumptions

**7. Exit, restoration, and post-incident revalidation.** Landscape response must close when continuation burden is no longer met or termination criteria are satisfied. At closure:
- **emergency and continuity authorities expire** unless independently reauthorized
- **deferred rights, standing, and participation pathways are restored** on auditable timelines
- **residual risks, owners, and monitoring cadence are disclosed**
- **post-incident retrospective review is required**, including what failed, what was contained, what was replaced, and what constitutional controls must be strengthened

Repeated activation patterns indicating potential normalization or abuse of exceptional powers must trigger escalated oversight and structural review.

## Protocol D — Decentralized Constitutional Continuity and Partition Resilience

**Constitutional index (abridged)**
- Topic-level routing and cited authorities remain in subsection text and cross-references.
- Canonical owner map: `corpus_joint_structure.md` **CJS-2.2** (*Topic router (stable IDs)*) and `doc_architecture.md` section 4.

Constitutional tracing: This protocol operationalizes constitutional continuity under prolonged network disruption, partition, and adversarial connectivity conditions (including LAN-level compromise or sustained denial). **It** implements Sentient Constitution Chapter One constraints (Safety, Truth, proportionality, necessity). **It** implements **Chapter Five** definitions where materially relevant (**[§3.20](core_05-05_definitions_c_dependent_clusters.md#governance-architecture-oversight-decentralization-and-concentration-cluster)** *Governance Architecture… — Systemic Lock-In*, *Dependency*, *Oversight*, and related hubs where partition or coupling analysis applies jointly; **[§3.24](core_05-05_definitions_b_semi_independent.md#movement-refuge-semi-independent)** *Movement, Refuge, Non-Statelessness, and Exit Integrity* where partition or exit implicates movement, refuge, or recognition jointly; **[§3.3](core_05-05_definitions_c_dependent_clusters.md#accountability-contestability-and-collective-accountability-failure-cluster)** *Accountability* and collective-accountability routing where materially relevant; **[§3.32](core_05-05_definitions_c_dependent_clusters.md#collective-harm-boundary-and-harm-cluster)** *Resilience*, *Reversibility*, *Safety*, *Cascading Failure*, and systemic-harm containment where materially relevant; **[§3.17](core_05-05_definitions_b_semi_independent.md#emergency-and-contingency-semi-independent)** *Emergency and Contingency* where prolonged disruption or contingency predicates apply). **It** implements **Chapter Ten, Article XXIII** (conflict and emergency proportionality). **It** implements **Article XIX** (interoperability, portability, and exit integrity). **It** implements **Article XXIV** (constitutional evolution and non-entrenchment). **It** implements **Article XI** (stakeholder governance, participation, and due process). **It** implements **Article XXV-C** where continuity-mode failure handling, off-ramps, or rejoin re-baselining are implicated. **It** also applies `corpus_joint_structure.md` **CJS-5E.1** (*Implementation and cross-implementation graceful degradation and failure-mode integrity terms*), **CJS-5B.2** (*Implementation and cross-implementation auditability and reconstructability terms*), **CJS-5B.3** (*Implementation and cross-implementation tiered transparency and audit-access terms*), **CJS-5B.4** (*Implementation and cross-implementation independent verification and claim-integrity terms*), **CJS-5E.3** (*Implementation and cross-implementation reversibility and containment terms*), **CJS-5D.3** (*Implementation and cross-implementation data-retention and lifecycle-integrity terms*), **CJS-5A.1** (*Implementation and cross-implementation distributed and proportional authority terms*), **CJS-5A.3** (*Implementation and cross-implementation reflexive transparency and accountability terms*), and **CJS-5A.6** (*Implementation and cross-implementation procedural integrity and adjudication terms*). This protocol does not narrow Rights Floors.

**1. Continuity modes and Rights-Floor invariants.** Systems must define and publish at least four operational continuity modes: **Normal**, **Degraded-Partitioned**, **Offline-Sovereign**, **Rejoin-Reconciliation**.

For every mode, systems must preserve non-regression constitutional floors. **Those** floors include Safety, Truth (Epistemic Integrity), dignity-equality protections, meaningful agency constraints, and challengeability to the maximum feasible extent under conditions.

**Mode transitions must be** **trigger-defined and auditable**. **They** must be **independently reviewable at class-appropriate cadence**. **They** must be **reversible when trigger conditions clear**.

**2. Local-first governance execution under disconnection.** High-impact systems must support local execution of constitutional minimums when wide-area coordination is unavailable.

**That** execution includes **safety and harm-containment actions**. **It** includes **Rights-Floor protection and standing triage**. **It** includes **temporary dispute handling with recorded rationale**. **It** includes **protected reporting and escalation intake**.

Local execution authority must be scope-limited, time-bounded, and constrained by least-restrictive and reversibility requirements.

**3. Partition-safe decision constraints.** During Degraded-Partitioned or Offline-Sovereign modes: **binding decisions must include explicit scope caps, expiry, and restoration triggers**.

**Irreversible actions require elevated burden and independent review where feasible**.

**Default preference is reversible or compensably restorable interventions**.

**Anti-capture checks must account for reduced oversight diversity under partition**.

Decisions taken under partition remain challengeable and must be revalidated during Rejoin-Reconciliation.

**4. Offline audit integrity and reconciliation.** Systems must maintain tamper-evident local audit chains while disconnected.

**Those** chains use **append-only event records with integrity proofs**. **They** use **explicit local clock/confidence metadata and uncertainty markers**. **They** use **immutable linkage between decisions, evidence references, and authority basis**.

**Upon reconnection**, systems must execute reconciliation that **preserves lineage and conflict visibility**. **It** must **identify and flag inconsistent histories or unverifiable segments**. **It** must **apply predeclared conflict-resolution rules with independent review for high-impact divergence**.

**5. Decentralized trust anchor and credential continuity.** Systems must avoid single-anchor dependence for constitutional continuity.

**They** must **support threshold or multi-party trust recovery pathways**. **They** must **rotate/revoke compromised credentials with local fallback procedures**. **They** must **maintain node exclusion and re-admission criteria under compromise suspicion**. **They** must **prevent isolated authorities from permanently entrenching trust state without post-rejoin validation**.

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

**6. Performance and reliability under decentralized operation.** Class-scaled continuity profiles must define measurable decentralized performance targets (for example, local decision latency, offline survivability duration, and reconciliation convergence bounds).

**Targets must** **be auditable and periodically reviewed**. **They** must **scale with Chapter S2 class and Chapter S3 stewardship tier where applicable**. **They** must **never justify weakening constitutional Rights Floors or verification integrity**.

**7. Rejoin, de-escalation, and anti-normalization.** Rejoin-Reconciliation mode must include **staged restoration of normal governance pathways**.

**It** must include **retrospective review of partition-period decisions and harms**. **It** must include **correction, reversal, or remediation for decisions that fail post-rejoin validation**. **It** must include **publication of lessons, control updates, and recurrence-reduction actions**.

Persistent operation in degraded modes without renewed necessity and independent review is non-compliant and must trigger structural oversight escalation.

**8. Self-healing under decentralized continuity (Article XII-F implementation profile).** This section applies **Protocol A**, subsection **H** (*Self-healing and recovery-path integrity*) to the four continuity modes defined in section **1** — **Normal**, **Degraded-Partitioned**, **Offline-Sovereign**, and **Rejoin-Reconciliation**. It is not a second self-healing profile. Detection, containment, safe-failure preference, non-masking, Rights-Floor continuity, autonomy scaling, and root-cause closure remain governed by Protocol A subsection **H**, **Sentient Constitution Chapter Ten, Article XII-F**, **Chapter One §4.1**, and **Chapter Five** [*Self-Healing*](core_05-05_definitions_a_independent.md#self-healing-constitutional). This section adds only the decentralized-continuity cross-checks below.

- Offline and partitioned modes must maintain tamper-evident local recovery-event chains consistent with section **4** (offline audit integrity), and must reconcile recovery events on rejoin rather than treating mode-internal recovery as closed.
- Recovery across partitions must not alter persistent state, credentials, obligations, or configurations attributed to sentients, operators, or other systems **in other partitions** that fall **outside** the declared fault-and-recovery scope except through changes that satisfy **Article XV-A** [Auditability](core_05-05_definitions_c_dependent_clusters.md#auditability) for observability and attribution and that, where parties in those partitions are materially affected, include proportionate notice, authorization, or contestable handoff consistent with **Chapter Ten**.
- Recovery authority must not expand beyond the pre-fault envelope in any partition and must not propagate failure through [Cascading Failure](core_05-05_definitions_a_independent.md#cascading-failure) pathways exposed by partition topology.
- Recovery actions taken under partition that prove invalid on rejoin must be subject to section **7**'s correction, reversal, or remediation pathway.
- Mode transitions, provisional trust states under section **5A**, and emergency-authority invocations must not suppress, overwrite, or delay evidence needed for root-cause analysis under **Article XXI-A**. Reconciliation on rejoin must treat masked or under-logged recovery as a post-rejoin validation failure under section **7**.
- Where Rights-Floor capacity is genuinely constrained by partition topology, narrowing must be explicit, time-bound, and restoration-triggered, and must be treated as **Article XXV** transition-governance territory at rejoin.
- Partition-local contestability intake, audit emission, or external-review pathways must remain materially external or independently verifiable within the partition and must reconcile on rejoin.
- Self-healing that succeeds operationally in a partitioned or offline mode but leaves a known defective condition in place must carry the Protocol A open root-cause obligation into Rejoin-Reconciliation mode. Recurrence across partition cycles or rejoin cycles remains a single open obligation, not closure of each incident.

Where this section is silent, Protocol A subsection **H**, Chapter One §4.1, Article XII-F, and the Chapter Five definition govern. This section does not create rights and must not be read to narrow those homes.

---

*Corpus alignment:* edition `SC-Corpus-2026.04.32`, effective **2026-04-24**; canonical mapping in [doc_architecture.md](doc_architecture.md) **section 17**.

---

**Next file:** [corpus_institutions.md](corpus_institutions.md)
