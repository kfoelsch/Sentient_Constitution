## CJS-5C: Dependency, exit, and lifecycle integrity

This family collects the operational clusters that govern dependency mapping, meaningful exit, interoperability, portability, retention, and lifecycle review.

| Cluster | Section |
|---|---|
| **CJS-5C.1** | Implementation and cross-implementation dependency integrity and disclosure terms |
| **CJS-5C.2** | Implementation and cross-implementation interoperability, portability, and exit-integrity terms |
| **CJS-5C.3** | Implementation and cross-implementation data-retention and lifecycle-integrity terms |

---

## CJS-5C.1 Implementation and cross-implementation dependency integrity and disclosure terms
Use this rule when dependency mapping, risk treatment, or accountability depends on standalone system behavior or combined system, dependency, or implementation-layer behavior.

Read it with:
- **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity**
- **PRIM4 — Transparency and Disclosure**
- **PRIM7 — Interoperability, Portability, and Exit Integrity**
- **PRIM9 — Auditability**
- **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**
- `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**
- **Article XV-A**

Implementation and cross-implementation dependency integrity and disclosure terms
- OP-O: If a system relies on something important, that reliance must be named, explained, watched, and handled according to the risk it creates.
- OP-E: Reviewers must look at the full dependency picture, not isolated pieces that make the system look safer than it is.
- OP-C: A system is non-compliant if it claims its dependencies are under control while leaving out, contradicting, or ignoring an important dependency.

Dependency identification and disclosure content
- OP-O: Systems must keep current records of what they depend on and what depends on them, including suppliers, data sources, software, infrastructure, institutions, contracts, interfaces, and handoff points.
- OP-E: Reviewers must check technical dependencies, financial or market dependence, governance control, and whether the system can actually work with or move away from other systems.
- OP-C: Leaving out an important dependency, or letting dependency information go stale, is non-compliant.

Criticality and impact classification
- OP-O: **Class A, Class B, and Class C** systems must classify dependencies that materially affect their core mission, constitutional function, operation, recovery, governance, or coordinated continuity. Classification must state reliance degree, substitutability, switching cost, exit feasibility, cascade risk, and affected parties or systems.
- OP-E: Reviewers must verify that dependency classification aligns with `corpus_systems.md` dependency classes and is useful for real decisions, including mitigation, audit, oversight, purchasing, participation, and exit planning.
- OP-C: **Class A, Class B, and Class C** mission-impacting dependencies must be clearly identified, monitored, audited, and periodically reviewed. Dependencies that are critical to safety, rights, access, continuity, or systemic stability may not be left unclassified or treated as ordinary vendor or interface choices.

Substitutability, exit constraints, and mitigation duties
- OP-O: For important dependencies, disclosures must explain the practical alternatives, the cost and risk of switching, what transition would require, and any limits on exit, repair, portability, or interoperability.
- OP-E: Reviewers must check whether the system has a realistic mitigation plan, or a documented reason why mitigation is not feasible.
- OP-C: Hidden lock-in, hidden switching costs, or unaddressed exit barriers are non-compliant unless a lawful and proportionate justification is documented.

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
- OP-C: A simplified dependency process is non-compliant if important risks still exist but are not disclosed, monitored, or addressed.

---

## CJS-5C.2 Implementation and cross-implementation interoperability, portability, and exit-integrity terms
Use this rule when lock-in, migration, interface design, or dependency exposure depends on standalone system behavior or combined system, dependency, or implementation-layer behavior.

Read it with:
- **PRIM7 — Interoperability, Portability, and Exit Integrity**
- **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity**
- **PRIM4 — Transparency and Disclosure**
- `corpus_systems.md` **Chapter S1 — Information Types and Handling**
- `corpus_systems.md` **Chapter S2 — System Classification and Handling**
- `corpus_systems.md` **Chapter S3 — Critical System Stewardship**
- **Article XIX**
- **Article XV-A**

Implementation and cross-implementation interoperability, portability, and exit-integrity terms
- OP-O: Systems must preserve meaningful exit, usable portability, and fair interoperability.
- OP-E: Evaluation must assess all relevant system components, dependencies, institutional roles, and implementation-layer interactions together.
- OP-C: It is non-compliant to claim exit integrity when a material component is unmet.

Lock-in and anti-coercion safeguards
- OP-O: Systems must not design coercive lock-in or exploit data, identity, or network effects to block exit.
- OP-E: Evaluation must verify mitigation where natural lock-in emerges.
- OP-C: Retaliating against exit through degraded service, penalties, or forfeiture is non-compliant.

Right-to-exit pathway integrity
- OP-O: Exit must be functionally available without violating Foundational Rights.
- OP-E: Evaluation must verify clear, time-bound, practical support for exit.
- OP-C: Nominal exit that is functionally blocked or coercive is non-compliant.

Portability quality and non-obstruction controls
- OP-O: Portability must be secure, usable, structured, and meaningful, including lawful identity, attribution, and continuity-critical state data.
- OP-E: Evaluation must verify schemas, documentation, context, and tooling for practical reuse.
- OP-C: Degrading, fragmenting, obscuring, or gating data to prevent reuse is non-compliant.

Interchange and open-interface baseline
- OP-O: Material-impact or material-dependency systems should use open, documented, interoperable formats and interfaces unless a narrower choice is lawfully justified.
- OP-E: Evaluation must verify interface controls do not defeat migration, substitution, or independent verification.
- OP-C: Closed or unstable interfaces used to create lock-in are non-compliant.

Open data-format and protocol presumption
- OP-O: **Class A**, **Class B**, and **Class C** systems must use open, documented, stable, and standards-compatible data formats, schemas, APIs, and interchange protocols for material portability, audit, repair, continuity, and migration functions unless a narrower format or interface is strictly justified.
- OP-E: Evaluation must verify public or qualified-access specifications, versioning discipline, migration tooling, test vectors, conformance records, and a scrutinizable justification for any closed, proprietary, unstable, or non-standard format or protocol.
- OP-C: Closed, proprietary, degraded, unstable, or undocumented data formats or protocols are non-compliant where they materially impair exit, repair, independent verification, continuity, substitution, or cross-implementation operation, unless the restriction satisfies necessity, proportionality, least-restrictive-alternative, auditability, sunset, and revalidation requirements.

Innovation reward boundary and anti-enclosure controls
- OP-O: Innovation rewards must preserve repair, verification, interoperability, migration, and meaningful exit.
- OP-E: Evaluation must verify dependency-critical exclusivity is narrow, time-bounded, disclosed, and continuity-protective.
- OP-C: Innovation claims that create coercive lock-in or hidden barriers are non-compliant.

Exit-feasibility disclosure and dependency transparency
- OP-O: Systems must disclose dependencies affecting exit, including switching costs, migration risk, alternatives, substitutability, and downstream impact.
- OP-E: Evaluation must verify exit-relevant disclosures are complete, attributable, and auditable.
- OP-C: Hidden dependencies that materially impair exit are non-compliant.

Continuity-preserving transition safeguards
- OP-O: Exit and migration should preserve identity, participation, and recoverable state where feasible.
- OP-E: Evaluation must verify safe transition paths, rollback or recovery options, and advance disclosure of unavoidable loss.
- OP-C: Forcing avoidable discontinuity is non-compliant.

Proportional application
- OP-O: Interoperability, portability, and exit duties scale with impact, dependency, ecosystem integration, and lock-in irreversibility.
- OP-E: Evaluation must verify reduced rigor does not create hidden dependencies or external lock-in effects.
- OP-C: Simplified controls are non-compliant where material lock-in remains.

---

## CJS-5C.3 Implementation and cross-implementation data-retention and lifecycle-integrity terms
Use this rule when accountability, privacy, reversibility, or classification depends on how data is kept, changed, linked, or deleted within a standalone system, institution, forum, or bounded decision domain, or across more than one system or implementation layer.

Read it with:
- **PRIM9 — Auditability**
- **PRIM10 — Tiered Transparency and Audit Access**
- **PRIM11 — Independent Verification and Integrity of Claims**
- **PRIM12 — Reversibility and Containment**
- **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**
- `corpus_systems.md` **Chapter S1 — Information Types and Handling**, including Types **C**, **G**, **H**, **I**, **N**, and **S**
- **CJS-3.5 — Classification alignment for supervised scope**

Implementation and cross-implementation data-retention and lifecycle-integrity terms
- OP-O: Data-retention compliance must be evaluated as one lifecycle claim across collection, use, retention, transformation, disclosure, deletion, de-identification, and reclassification.
- OP-E: Reviewers must assess purpose, S1 data type or types, duration, detail, access, deletion or de-identification, reclassification, disclosure, and audit needs together.
- OP-C: A retention-integrity claim is non-compliant if those lifecycle elements cannot be reviewed together, if an important element is missing or unusable, or if one element defeats another.

Justification and bounded-retention floor
- OP-O: Retention must remain justified over time. When the justification ends, the data must be reduced, deleted, de-identified, or otherwise removed from use.
- OP-E: Reviewers must verify that the amount of data kept, and the time it is kept for, fit the S1 data type or types, purpose, legal obligations, impact, rights, safety, and accountability needs.
- OP-C: Keeping data because it might be useful later, is convenient to keep, or gives an institution leverage is non-compliant.

Purpose and proportionality criteria
- OP-O: Data may be kept only for warranted purposes, such as integrity, continuity, safety, dispute resolution, restoration, or accountability.
- OP-E: Reviewers must verify that retention scales with S1 data type or types, impact, dependency, sensitivity, audit needs, and the need to challenge or correct a decision.
- OP-C: Keeping more detail, identity linkage, or history than the purpose requires is non-compliant.

Lifecycle expiry, deletion, de-identification, and reclassification controls
- OP-O: Temporary data must not quietly become a permanent archive.
- OP-E: Reviewers must verify deletion where feasible. If deletion is not feasible, they must verify irreversible de-identification or aggregation. Reclassification across S1 data types requires a new documented and time-limited justification.
- OP-C: Keeping data indefinitely without a continuing reason and working lifecycle controls is non-compliant.

Anti-surveillance and anti-coercion accumulation limits
- OP-O: Retention must not become hidden surveillance, coercive leverage, or a way to reconstruct protected internal states beyond the justified scope, especially through Type **H**, **I**, or **N** data.
- OP-E: Reviewers must verify that behavioral, relational, identity-linked, or internal-state-adjacent data is not being accumulated secretly or out of proportion to the stated purpose.
- OP-C: A retention design that enables coercion, concealed surveillance, or meaningful barriers to exit or contestation is non-compliant.

Accountability-preserving record floor
- OP-O: Where required, retention must keep enough Type **C**, **G**, **H**, **I**, or **S** records to reconstruct material events, audit conduct, verify claims, support challenge and redress, preserve continuity, and recover from failure.
- OP-E: Reviewers must verify that data minimization does not block investigations or hide responsibility.
- OP-C: Invoking minimization to defeat accountability is non-compliant.

Classification and information-type alignment
- OP-O: If accumulated, linked, or inferred data changes its **Chapter S1 — Information Types and Handling** data type or becomes more sensitive in practice, stricter protections apply.
- OP-E: Reviewers must verify alignment with **Chapter S1 — Information Types and Handling** data-type duties and **CJS-3.5 — Classification alignment for supervised scope** where supervision and systems classification overlap.
- OP-C: Continuing to use lower-type or lower-class handling after sensitivity has increased is non-compliant.

Transparency disclosures and stakeholder legibility
- OP-O: Systems must disclose retention details in proportion to impact. The disclosure must identify the applicable S1 data type or types and what categories of data are kept. It must also state why data is kept, how long it is kept or how that period is chosen, when lifecycle changes occur, and what secondary uses are allowed.
- OP-E: Reviewers must verify that disclosures are clear enough for stakeholders to understand the practical consequences.
- OP-C: Incomplete, obscure, or misleading retention disclosures are non-compliant.

Review, revalidation, and prohibited patterns
- OP-O: Retention rules must be revalidated on a set schedule and updated when material conditions change.
- OP-E: Reviewers must screen for indefinite retention, use beyond the original purpose or S1 data type or types, unnecessary detail, complexity that hides consequences, evasive deletion, shadow stores, and designs that block audit.
- OP-C: Stale, unreviewed, or evasive retention regimes are non-compliant.

Proportional application
- OP-O: Retention controls scale with S1 data type or types, impact, dependency, sensitivity, reconstructability, duration, scope, and governance role.
- OP-E: Reviewers must verify that simplified controls do not create surveillance, coercion, blocked investigations, or rights harm.
- OP-C: Reduced safeguards are non-compliant where material exposure remains.

---

**Next file:** [cjs_05d_00_failure_robustness_intervention_correction.md](cjs_05d_00_failure_robustness_intervention_correction.md)
