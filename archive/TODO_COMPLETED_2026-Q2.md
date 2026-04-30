# Archived TODO (completed work)

**Archived:** 2026-Q2 (first hygiene archive). **Active checklist:** [`TODO.md`](../TODO.md).

Preserved material is **process history only**. Authoritative rules live in [`core_constitution.md`](../core_constitution.md), [`corpus_primitives.md`](../corpus_primitives.md), and [`corpus_systems.md`](../corpus_systems.md).

**Operational pointers (unchanged location):** [`CONSTITUTIONAL_REGRESSION_SCENARIOS.md`](../CONSTITUTIONAL_REGRESSION_SCENARIOS.md), [`evidence/`](../evidence/), [`TRUST_UNDER_ATTACK_DELTA_REPORT.md`](../TRUST_UNDER_ATTACK_DELTA_REPORT.md).

---

## Landscape-Scale Subversion Hardening (New)

- [x] Draft `Protocol R` in `corpus_systems.md` for system-wide subversion response, replacement, and reconstitution.
- [x] Define landscape compromise declaration criteria and activation thresholds (including multi-system simultaneous attack conditions).
- [x] Define class-prioritized triage and dependency-aware containment choreography for concurrent compromise.
- [x] Define steward-of-last-resort continuity rules when multiple governance nodes are compromised.
- [x] Define trusted baseline rebuild/replacement procedure (credential revocation/re-issuance, clean-state restoration, phased re-entry).
- [x] Define supply-chain compromise handling and cross-jurisdiction coordination under active evasion pressure.
- [x] Define crisis communications protocol for simultaneous attacks with anti-disinformation controls.
- [x] Add dedicated regression scenarios and at least one evidence-backed operational drill for `Protocol R`.

## Decentralized Continuity and Partition Resilience (New)

- [x] Draft `Protocol D` in `corpus_systems.md` for decentralized constitutional continuity under prolonged partition/LAN disruption.
- [x] Define constitutional continuity modes (`normal`, `degraded-partitioned`, `offline-sovereign`, `rejoin-reconciliation`) with rights-floor invariants.
- [x] Define local-first governance execution requirements for safety, rights protection, standing, and dispute triage during disconnection.
- [x] Define partition-safe decision constraints (scope caps, time bounds, reversibility defaults, anti-capture safeguards).
- [x] Define tamper-evident offline audit chain and reconciliation protocol with lineage/conflict transparency.
- [x] Define decentralized trust-anchor and credential continuity (rotation, threshold recovery, compromised-node exclusion).
- [x] Define class-scaled performance/reliability targets for decentralized operation that cannot override constitutional floors.
- [x] Add dedicated `RS-DECP-*` scenarios and at least one evidence-backed operational partition drill.

## Constitutional-Level Concerns (Under-Addressed)

- [x] Ticket 1: Institutional architecture and anti-capture
- [x] Ticket 2: Emergency powers hard limits
- [x] Ticket 3: Democratic legitimacy and representation
- [x] Ticket 4: Enforcement realism framework
- [x] Ticket 5: Rights-collision procedure
- [x] Ticket 6: Proportional compliance templates
- [x] Ticket 7: Transition constitution framework
- [x] Ticket 8: Anti-concentration guardrails

## External Framework and Embedding Gaps (gap-analysis follow-up)

**Superseded checklist snapshot.** The open items that appeared here in the 2026-Q2 archive copy were **completed** by **2026-04-08** under corpus edition **`SC-Corpus-2026.04`**. Full closed narratives (checkboxes and done notes) are preserved in **[TODO_COMPLETED_SC-Corpus-2026.04.md](TODO_COMPLETED_SC-Corpus-2026.04.md)**.

## Prioritization and Drafting Targets

## Critical Path (recommended order)

1. Ticket 1: Institutional architecture and anti-capture
2. Ticket 2: Emergency powers hard limits
3. Ticket 5: Rights-collision procedure
4. Ticket 4: Enforcement realism framework
5. Ticket 3: Democratic legitimacy and representation
6. Ticket 8: Anti-concentration guardrails
7. Ticket 6: Proportional compliance templates
8. Ticket 7: Transition constitution framework

## Drafting Target Labels

- Ticket 1: Institutional architecture and anti-capture
  - Primary: Constitution Core
  - Secondary: Primitives
- Ticket 2: Emergency powers hard limits
  - Primary: Constitution Core
  - Secondary: Systems Annex
- Ticket 3: Democratic legitimacy and representation
  - Primary: Constitution Core
  - Secondary: Primitives
- Ticket 4: Enforcement realism framework
  - Primary: Primitives
  - Secondary: Constitution Core, Systems Annex
- Ticket 5: Rights-collision procedure
  - Primary: Constitution Core
  - Secondary: Primitives
- Ticket 6: Proportional compliance templates
  - Primary: Systems Annex
  - Secondary: Primitives
- Ticket 7: Transition constitution framework
  - Primary: Systems Annex
  - Secondary: Constitution Core, Primitives
- Ticket 8: Anti-concentration guardrails
  - Primary: Constitution Core
  - Secondary: Primitives, Systems Annex

## Drafting Sprint Plan (6 weeks)

### Sprint 1 (Weeks 1-2): Constitutional decision backbone

- Scope: Ticket 1, Ticket 2, Ticket 5
- Outcome: Stable constitutional decision architecture before expanding enforcement and participation machinery.
- Exit criteria:
  - Draft text for final-arbiter and anti-capture architecture
  - Emergency powers limits with sunset/review/restoration language
  - Rights-collision procedure with documented burden and review triggers

### Sprint 2 (Weeks 3-4): Enforcement and legitimacy layer

- Scope: Ticket 4, Ticket 3, Ticket 8
- Outcome: Practical enforceability and democratic legitimacy, with anti-concentration constraints to prevent structural drift.
- Exit criteria:
  - Enforcement ladder and remediation financing draft
  - Representation and standing mechanics for high-impact decisions
  - Concentration thresholds and intervention mechanisms draft

### Sprint 3 (Weeks 5-6): Operationalization and migration

- Scope: Ticket 6, Ticket 7
- Outcome: Scaled implementation pathways plus transition sequencing from current institutions.
- Exit criteria:
  - Class-scaled compliance templates mapped to annex classes
  - Phased transition framework with continuity and fallback mechanisms

## Proposed Insertion Points by Ticket

- Ticket 1: Institutional architecture and anti-capture
  - `core_constitution.md`: Chapter Four (governance rights/procedures) and Chapter Three (`Adjudication and Dispute Resolution (Constitutional)`, `System Capture`, `Accountability`)
  - `corpus_primitives.md`: PROT6 adjudication/oversight implementation language

- Ticket 2: Emergency powers hard limits
  - `core_constitution.md`: Chapter One, section 6 — *Interaction and Conflict Resolution* interaction rules (cross-reference to emergency limits) and Chapter Three (`Emergency and Contingency (Constitutional)`, `Force Majeure (Constitutional)`)
  - `corpus_systems.md`: Protocol A emergency deployment, rollback, reauthorization, and retrospective review clauses

- Ticket 5: Rights-collision procedure
  - `core_constitution.md`: Chapter One, section 6 — *Interaction and Conflict Resolution* (new explicit decision test subsection), Chapter Two burden/traceability requirements
  - `corpus_primitives.md`: PROT-DRP procedural implementation of collision adjudication

- Ticket 4: Enforcement realism framework
  - `core_constitution.md`: Chapter Three violation and enforceability definitions (sanction/remediation anchors)
  - `corpus_primitives.md`: PROT3/PROT6 operational enforcement and remediation process
  - `corpus_systems.md`: Annex execution pathways for cross-jurisdiction and anti-evasion handling

- Ticket 3: Democratic legitimacy and representation
  - `core_constitution.md`: Chapter Four participation rights and Chapter Three participant standing/procedural fairness definitions
  - `corpus_primitives.md`: PROT1 proportional authority and participation-weight implementation constraints

- Ticket 8: Anti-concentration guardrails
  - `core_constitution.md`: Chapter One freedom/trust constraints and Chapter Three dependency/lock-in/system capture definitions
  - `corpus_primitives.md`: PRIM7 portability/exit and PROT1 anti-dominance governance constraints
  - `corpus_systems.md`: Classification-linked concentration triggers and mitigation pathways

- Ticket 6: Proportional compliance templates
  - `corpus_systems.md`: Chapter S2 class handling profiles and protocol checklists
  - `corpus_primitives.md`: PRIM9-PRIM11 minimum auditability and verification floors by class
  - `core_constitution.md`: Chapter Two anti-evasion guardrail language for template scaling

- Ticket 7: Transition constitution framework
  - `corpus_systems.md`: Dedicated transition protocol with phases, gates, fallback, and continuity requirements
  - `core_constitution.md`: Chapter Four rights-floor continuity and Chapter Three reversibility/emergency cross-reference language
  - `corpus_primitives.md`: Governance implementation obligations for transition oversight and review cadence

## Ticket 1: Institutional architecture and anti-capture

**Status**
Completed.
Progress update:
- Completed: Constitutional section defining final-arbiter scope limits, anti-capture controls, independent challenge pathway, periodic external review, and removal-for-cause (`Article XX`).
- Completed: Supporting Chapter Three interdependent definition added (`Constitutional Review Body (Constitutional)`).
- Completed: PROT6 governance-layer implementation language added in `corpus_primitives.md` (Provision VI) for bounded mandate, appointments/rotation, recusal integrity, public reasoning, independent challenge, and external structural review.
- Completed: `corpus_systems.md` alignment added for anti-capture operational checks in Protocol A crisis governance continuity and Protocol C review metrics/escalation triggers (Article XX and PROT6-linked).
- Verification: Acceptance criteria checked and satisfied across constitution core, primitives, and systems annex.

**Problem**
Current constitutional language is strong on constraints, but under-specifies who has final interpretive authority and how that authority remains capture-resistant over time.

**Proposed mechanism**
Define a multi-layer interpretive architecture with:
- a constitutional review body with bounded mandate
- transparent appointment and rotation rules
- conflict-of-interest and recusal requirements
- independent challenge pathways and periodic structural review

**Acceptance criteria**
- A dedicated section defines final-arbiter authority, scope limits, and reviewability.
- Anti-capture controls are explicit (term limits, recusals, disclosure, removal for cause).
- At least one independent external review mechanism is codified.
- Interpretive decisions are auditable and publicly reasoned, with narrow confidentiality exceptions.
Acceptance checklist:
- [x] Dedicated final-arbiter and scope/reviewability section present (`core_constitution.md` Article XX).
- [x] Explicit anti-capture controls present (appointments/rotation, disclosure, recusal, removal for cause) in core and PROT6 implementation.
- [x] Independent external review codified (Article XX + Provision VI external structural review).
- [x] Auditable public reasoning with narrow confidentiality constraints codified (Article XX + Provision VI traceability requirements).

**Dependencies**
- Chapter Three entries on accountability, adjudication, system capture, and contestability
- PROT6 governance/adjudication mechanisms
- Existing supremacy and enforceability provisions

## Ticket 2: Emergency powers hard limits

**Status**
Completed.
Progress update:
- Completed: Strengthened `core_constitution.md` Chapter Three `Emergency and Contingency (Constitutional)` evaluation requirements with default sunset, non-optional independent review intervals, explicit reauthorization burden, and auditable restoration/rollback triggers.
- Completed: Expanded `core_constitution.md` Article XVI emergency controls to require default expiry, documented reauthorization burden, and post-emergency retrospective review/disclosure with narrow confidentiality exceptions.
- Completed: Added `corpus_systems.md` Protocol A emergency lifecycle controls for expiry timestamps, independent review cadence, reauthorization criteria, and retrospective audit records.
- Completed: Added Protocol A emergency closure criteria and restoration-completion evidence requirements, including residual-risk disclosure and accountable restoration timelines.
- Verification: Acceptance criteria checked and satisfied across constitution core and systems annex.

**Problem**
Emergency and contingency allowances exist, but durable safeguards against normalization or indefinite extension need stronger constitutional precision.

**Proposed mechanism**
Codify emergency powers as strictly temporary and threshold-bound, including:
- automatic expiration (sunset by default)
- mandatory independent review intervals
- explicit restoration criteria and rollback obligations
- prohibition on emergency use for routine governance convenience

**Acceptance criteria**
- Every emergency measure has a default expiry and reauthorization burden.
- Independent review timing and authority are defined and non-optional.
- Restoration triggers are concrete, testable, and auditable.
- Post-emergency retrospective review and disclosure are required.
Acceptance checklist:
- [x] Default expiry and reauthorization burden codified (`core_constitution.md` Chapter Three + Article XVI; `corpus_systems.md` Protocol A).
- [x] Independent review cadence is mandatory and non-optional (`core_constitution.md` + Protocol A lifecycle controls).
- [x] Restoration/rollback triggers and closure evidence are concrete and auditable (`core_constitution.md` + Protocol A closure criteria).
- [x] Retrospective review and disclosure requirements are explicit with narrow confidentiality limits (`core_constitution.md` Article XVI + Protocol A retrospective audit records).

**Dependencies**
- Chapter One necessity/proportionality constraints
- Chapter Three emergency and force majeure definitions
- Protocol A deployment, rollback, and containment requirements

## Ticket 3: Democratic legitimacy and representation

**Status**
Completed.
Progress update:
- Completed: Expanded `core_constitution.md` Article XXIII with explicit high-impact representation and standing rules, weighted-participation anti-dominance constraints, pre-binding legitimacy checks, and token-participation prohibition.
- Completed: Expanded `corpus_primitives.md` PROT1 with representation/participation legitimacy controls including stakeholder class mapping, standing access, anti-dominance weighting safeguards, and mandatory legitimacy records.
- Verification: Acceptance criteria checked and satisfied across constitution core and governance primitives.

**Problem**
The framework affirms meaningful agency but leaves representation mechanics across stakeholder classes and dependency asymmetries insufficiently operationalized.

**Proposed mechanism**
Specify constitutional participation design, including:
- stakeholder class mapping and participation rights by impact/dependency
- weighted participation constraints with anti-oligarchic limits
- minimum guarantees for minority and high-risk affected groups
- transparent decision procedures and documented dissent handling

**Acceptance criteria**
- Representation and participation rules are explicit for high-impact decisions.
- Dependency-affected stakeholders receive guaranteed procedural standing.
- Decision legitimacy checks are required before binding adoption.
- Non-functional participation (token consultation) is classified as non-compliance.
Acceptance checklist:
- [x] High-impact representation and participation rules are explicit (`core_constitution.md` Article XXIII).
- [x] Dependency-affected and high-risk groups have guaranteed procedural standing in high-impact decisions.
- [x] Legitimacy checks are required and recorded before binding adoption (core + PROT1 implementation).
- [x] Token/non-functional participation is explicitly non-compliant (`core_constitution.md` + `corpus_primitives.md`).

**Dependencies**
- Chapter One freedom/agency and systemic evaluation requirements
- Chapter Three participant standing, dependency, and procedural fairness entries
- PROT1 distributed/proportional authority and PROT-DRP

## Ticket 4: Enforcement realism framework

**Status**
Completed.
Progress update:
- Completed: Added `core_constitution.md` Chapter Four `Enforcement Realism Anchors` defining sanction-ladder coupling, remediation financing obligation, cross-jurisdiction enforcement continuity, and anti-evasion via entity relabeling/forum shopping.
- Completed: Added `corpus_primitives.md` Provision VI implementation clauses for enforcement ladder mapping, remediation financing duties, non-payment escalation, and cross-jurisdiction continuity controls.
- Completed: Added `corpus_systems.md` Protocol C section `Cross-Jurisdiction Execution and Anti-Evasion Controls` with mutual-recognition packages, fallback pathways, entity continuity checks, and forum-shopping response.
- Verification: Acceptance criteria checked and satisfied across constitution core, primitives, and systems annex.

**Problem**
Constitutional obligations are extensive, but practical enforcement design (sanctions, remediation financing, and cross-jurisdiction pathways) remains incomplete.

**Proposed mechanism**
Add an enforcement ladder that couples:
- graduated sanctions to severity and recurrence
- mandatory remediation plans with financing rules
- cross-jurisdiction mutual recognition and escalation protocols
- anti-evasion safeguards for shell entities and forum shopping

**Acceptance criteria**
- Sanction levels map clearly to violation classes.
- Remediation funding obligations are binding and time-bound.
- Cross-jurisdiction cooperation triggers and fallback processes are defined.
- Evasion through relabeling/reincorporation is explicitly prohibited.
Acceptance checklist:
- [x] Sanction levels mapped to violation/severity classes (`core_constitution.md` Chapter Four anchors + `corpus_primitives.md` enforcement ladder).
- [x] Remediation funding obligations are binding and escalation-backed (`core_constitution.md` remediation financing + non-payment escalation in Provision VI).
- [x] Cross-jurisdiction cooperation and fallback execution are defined (`corpus_primitives.md` + `corpus_systems.md` Protocol C section 8).
- [x] Entity relabeling/reincorporation/forum-shopping evasion is explicitly prohibited and aggravating.

**Dependencies**
- Chapter Three violation classification model
- Supremacy and enforceability provisions
- PROT3 accountability and auditability primitives

## Ticket 5: Rights-collision procedure

**Status**
Completed.
Progress update:
- Completed: Added `core_constitution.md` Chapter One, section 6.4.1 — *Rights-Collision Decision Test* with mandatory alternatives analysis, risk-tiered burden, least-restrictive selection, and review/reversal triggers.
- Completed: Added `core_constitution.md` Article XVI cross-link requiring section 6.4.1 procedure records for rights-conflict adjudication.
- Completed: Added `corpus_primitives.md` PROT-DRP subsection (`6A. Rights-Collision Procedure`) with required decision-record fields and independent review conditions for high-impact/high-uncertainty cases.
- Verification: Acceptance criteria checked and satisfied across constitution core and DRP implementation layer.

**Problem**
The constitution recognizes interacting constraints, but recurring collisions (safety/truth/agency) need a repeatable jurisprudential procedure under uncertainty.

**Proposed mechanism**
Define a formal rights-collision test requiring:
- documented alternatives analysis
- uncertainty treatment and burden of proof by risk level
- least-restrictive option selection
- periodic re-evaluation as evidence changes

**Acceptance criteria**
- A standard decision test is codified for rights tradeoffs.
- Decision records include rejected alternatives and rationale.
- Time-limited restrictions are mandatory where feasible.
- Review/reversal triggers are specified for new evidence.
Acceptance checklist:
- [x] Standard rights-collision decision test codified (`core_constitution.md` Chapter One, section 6.4.1 — Rights-Collision Decision Test).
- [x] Decision records require rejected alternatives and rationale (`core_constitution.md` section 6.4.1 + `corpus_primitives.md` PROT-DRP 6A).
- [x] Time-limited restrictions are required where feasible (`core_constitution.md` section 6.4.1; DRP 6A time limits).
- [x] Review/reversal triggers for new evidence and outcome divergence are specified (core and DRP 6A).

**Dependencies**
- Chapter One sections on proportionality, necessity, and harm minimization
- Chapter Two evaluative/compliance burden requirements
- Chapter Three materiality and foreseeability clusters

## Ticket 6: Proportional compliance templates

**Status**
Completed.
Progress update:
- Completed: Added `corpus_systems.md` Protocol C section `Proportional Compliance Templates (Class-Scaled)` with invariant core controls, class-profile evidence packages, objective escalation triggers, and anti-evasion template rule.
- Completed: Added `corpus_primitives.md` PRIM9-PRIM11 template-floor mapping to preserve minimum auditability, tiered audit access, and independent verification across all templates.
- Verification: Acceptance criteria checked and satisfied across systems annex and primitive floors.

**Problem**
Verification and audit rigor are essential, but implementation burden can become impractical for smaller actors unless explicitly tiered.

**Proposed mechanism**
Create class-scaled compliance templates with:
- minimum non-negotiable controls for all systems
- simplified evidence packages for low-impact contexts
- escalation paths as impact/dependency increase
- shared reference tooling/checklists for small operators

**Acceptance criteria**
- Templates exist for at least low-, medium-, and high-impact profiles.
- Core protections are invariant across all templates.
- Escalation triggers are objective and anti-evasion aligned.
- Small-actor pathways remain auditable without excessive overhead.
Acceptance checklist:
- [x] Low/medium/high impact template profiles are explicitly defined (`corpus_systems.md` Protocol C section 9).
- [x] Core protections are invariant across all templates (invariant core controls + PRIM9-PRIM11 floors).
- [x] Escalation triggers are objective and anti-evasion aligned (measurable trigger list + anti-evasion template rule).
- [x] Small-actor pathways remain auditable with reduced burden (`Class L/P` concise evidence checklist with functional auditability preserved).

**Dependencies**
- Constitutional Systems class taxonomy (S2)
- PRIM9/PRIM10/PRIM11 auditability and verification requirements
- Anti-evasion constraints in Chapter Two

## Ticket 7: Transition constitution framework

**Status**
Completed.
Progress update:
- Completed: Added `core_constitution.md` transition article (**then numbered Article XXI**; **now Article XX: Transition Governance, Continuity, and Re-Baselining** after 2026-04-10 renumber) with phased gate criteria, rights-floor continuity, interim-authority limits, failure handling/off-ramps, and auditable public traceability.
- Completed: Expanded `corpus_primitives.md` Provision 3 with phased gates/review cadence, interim-authority constraint, and failure-handling/re-baselining requirements.
- Completed: Added `corpus_systems.md` `Protocol T — Transition Constitution and Migration Governance` with phase structure, advancement gates, fallback/re-baselining, and challengeable audit/disclosure requirements.
- Verification: Acceptance criteria checked and satisfied across constitution core, primitives, and systems annex.

**Problem**
The target-state constitution is advanced, but migration from current institutions is under-specified and risks governance vacuum or transitional lock-in.

**Proposed mechanism**
Define phased transition governance with:
- staged adoption milestones and constitutional minimum floors
- interim safeguards against rollback/capture
- continuity plans for critical services and rights protections
- explicit off-ramps for failed transition mechanisms

**Acceptance criteria**
- A phased timeline with gate criteria is documented.
- Critical-rights continuity is guaranteed at each phase.
- Transitional authorities are time-bounded and reviewable.
- Failure-handling and re-baselining protocols are defined.
Acceptance checklist:
- [x] Phased transition timeline and gate criteria are documented (`corpus_systems.md` Protocol T + **Article XX**).
- [x] Rights-floor continuity is required at each phase (**Article XX** + Protocol T phase controls).
- [x] Transitional authorities are scope-limited, sunset-bounded, and reviewable (**Article XX**, Provision 3, Protocol T).
- [x] Failure handling, off-ramps, and re-baselining procedures are explicitly defined (core + primitives + systems).

**Dependencies**
- Chapter Four rights floors
- Emergency/contingency and reversibility definitions
- Protocol A operational transition and environment controls

## Ticket 8: Anti-concentration guardrails

**Status**
Completed.
Progress update:
- Completed: Strengthened `core_constitution.md` Chapter Three `System Capture` evaluative/compliance language with concentration indicators and explicit hidden beneficial-control non-compliance treatment.
- Completed: Added `corpus_primitives.md` PROT1 `Anti-Concentration Guardrails` with auditable thresholds, mandatory mitigation activation, beneficial-control disclosure, and escalation for persistent concentration.
- Completed: Added `corpus_systems.md` Chapter S2 `Concentration Thresholds and Mitigation Triggers` tying class-scaled concentration indicators to trigger thresholds and mitigation playbooks.
- Verification: Acceptance criteria checked and satisfied across constitution core, primitives, and systems annex.

**Problem**
A system may remain formally compliant while allowing accumulation of economic/governance power that weakens meaningful agency and constitutional contestability.

**Proposed mechanism**
Add constitutional anti-concentration limits, including:
- concentration indicators and intervention thresholds
- structural separation or divestment triggers for dominant control
- interoperability/portability mandates to reduce lock-in
- transparency rules for beneficial control and influence pathways

**Acceptance criteria**
- Quantitative or clearly testable concentration thresholds are specified.
- Intervention options and triggers are defined and reviewable.
- Lock-in reducing requirements are tied to dependency/materiality.
- Hidden control structures are treated as constitutional non-compliance.
Acceptance checklist:
- [x] Clearly testable concentration thresholds and indicators are specified (`corpus_primitives.md` PROT1 + `corpus_systems.md` Chapter S2).
- [x] Intervention options and trigger pathways are defined and reviewable (mandatory mitigation activation + class-scaled trigger escalation).
- [x] Lock-in reducing controls are tied to dependency/materiality (portability/interoperability expansion and dependency-linked concentration indicators).
- [x] Hidden beneficial/proxy control structures are explicitly non-compliant (`core_constitution.md` System Capture + PROT1 disclosure rule).

**Dependencies**
- Chapter One freedom, trust, and systemic evaluation constraints
- Chapter Three dependency, lock-in, system capture, and accountability definitions
- PRIM7 portability/exit integrity and PROT1 governance proportionality

## Trust Under Active Attack Audit (Top 5 Risks)

Purpose: assess whether the constitution remains trustworthy under coordinated adversarial pressure before and after delivery of `Protocol R` and `Protocol D`.

### Risk 1 - Coordinated Multi-System Compromise (highest)

- [x] Before `Protocol R`: run a tabletop where 3+ critical systems are compromised simultaneously and verify current controls cannot silently normalize emergency authority.
- [x] After `Protocol R`: validate compromise declaration thresholds, dependency-prioritized containment, and clean-state reconstitution gates with evidence artifacts.
- [x] Add at least 3 dedicated `RS-SUBV-*` scenarios for concurrent compromise, credential revocation/re-issuance, and phased re-entry failure.

### Risk 2 - Partition Exploitation and Governance Fork Drift

- [x] Before `Protocol D`: run a prolonged partition simulation and measure decision divergence, rights-floor drift, and dispute backlog behavior.
- [x] After `Protocol D`: verify continuity modes, local-first constraints, and rejoin/reconciliation conflict handling under adversarial timing.
- [x] Add at least 3 dedicated `RS-DECP-*` scenarios for partition capture attempts, offline audit tampering, and rejoin lineage conflicts.

### Risk 3 - Epistemic Capture During Crisis

- [x] Stress-test legitimacy checks and rights-collision burden scaling under coordinated disinformation and synthetic consensus attacks.
- [x] Define hard evidence-quality gates and emergency information-integrity escalation triggers for high-impact decisions.
- [x] Add one red-team drill demonstrating reversible decision handling when critical evidence is later invalidated.

### Risk 4 - Steward and Credential Plane Capture

- [x] Define steward-of-last-resort quorum continuity and compromised-node exclusion criteria across simultaneous node compromise conditions.
- [x] Define threshold recovery and emergency trust-anchor rotation with explicit anti-seizure and anti-replay controls.
- [x] Validate appointment-pipeline concentration detection remains effective under long-horizon infiltration pressure.

### Risk 5 - Cross-Jurisdiction and Supply-Chain Evasion Under Attack

- [x] Define `Protocol R` supply-chain compromise branch with mandatory dependency blast-radius mapping and containment choreography.
- [x] Add cross-jurisdiction crisis coordination triggers when operators attempt legal or infrastructure arbitrage during active incident response.
- [x] Run one evidence-backed operational drill for concurrent supply-chain compromise plus jurisdictional evasion.

## Trust Audit Exit Criteria

- [x] Pre-`R`/`D` baseline report completed with explicit residual-risk scoring for the 5 risks above.
- [x] Post-`R` implementation validation completed with scenario evidence and operational drill records.
- [x] Post-`D` implementation validation completed with partition/rejoin evidence and rights-floor continuity checks.
- [x] Comparative "before vs after" trust-under-attack delta documented and linked to scenario IDs.
