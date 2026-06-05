## CJS-5D: Failure, robustness, intervention, and correction

This family collects the operational clusters for degraded operation, intervention readiness, containment, adversarial robustness, and structural correction.

| Cluster | Section |
|---|---|
| **CJS-5D.1** | Cross-implementation graceful degradation and failure-mode integrity terms |
| **CJS-5D.2** | Cross-implementation intervention and override integrity terms |
| **CJS-5D.3** | Cross-implementation reversibility and containment terms |
| **CJS-5D.4** | Cross-implementation adversarial robustness and abuse-resistance terms |
| **CJS-5D.5** | Cross-implementation structural review, correction urgency, and disclosure terms |

---

## CJS-5D.1 Cross-implementation graceful degradation and failure-mode integrity terms
Use this rule when reliability, signaling, containment, or recovery depends on combined system, dependency, or implementation-layer behavior. It is read with **PRIM6 — Graceful Degradation and Failure Mode Integrity**, **PRIM1 — System Status, Risk, and Scope Representation**, **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity**, **PRIM12 — Reversibility and Containment**, **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**, and `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**.

Cross-implementation graceful degradation and failure-mode integrity terms
- OP-O: Systems must behave honestly and safely under partial failure, uncertainty, or stress.
- OP-E: Evaluation must assess all relevant system components, dependencies, institutional roles, and implementation-layer interactions together.
- OP-C: It is non-compliant to claim graceful degradation when a material component is missing.

Graceful degradation floor and defined failure-mode coverage
- OP-O: Systems must degrade in controlled, visible, non-deceptive ways and avoid silent degradation or disproportionate harm.
- OP-E: Evaluation must verify defined failure modes, including component loss, data problems, dependency instability, adversarial compromise, and excessive uncertainty.
- OP-C: Relying on undefined failure behavior is non-compliant where definition is required.

Signaling integrity and anti-silent-failure controls
- OP-O: When capability or reliability drops, that degraded state must be visible in proportion to impact.
- OP-E: Evaluation must verify degraded outputs are distinguishable and signals propagate downstream where relevant.
- OP-C: Preserving a false appearance of normal operation is non-compliant.

Priority order and honest representation
- OP-O: Under constraint, systems prioritize survival and foundational requirements, then auditability and reconstructability, then reversibility, containment, and recovery.
- OP-E: Evaluation must verify performance goals do not override truthful degradation signaling.
- OP-C: Sacrificing accurate signaling for convenience or throughput is non-compliant.

Bounded operation, safe-mode transitions, and shutdown discipline
- OP-O: Degraded operation must stay within defined auditable bounds and avoid false, fabricated, overconfident, irreversible, or unbounded-harm outputs.
- OP-E: Evaluation must verify safe limited mode or suspension when safe degraded operation is not feasible.
- OP-C: Continuing outside safety and integrity bounds is non-compliant.

Fail-soft within constraints and non-externalization
- OP-O: Partial function may continue only within safety and integrity bounds.
- OP-E: Evaluation must verify critical-function preservation, bounded failure scope, and anti-propagation controls.
- OP-C: Fail-soft mode may not justify out-of-bounds operation or undisclosed harm to dependents.

Monitoring, transition traceability, escalation, and revalidation
- OP-O: Decline, anomalies, dependency instability, and uncertainty escalation must be monitored and recorded.
- OP-E: Evaluation must verify escalation, mitigation, recovery, root-cause support, and revalidation.
- OP-C: Unmanaged or untraceable degradation is non-compliant.

Cross-boundary propagation controls
- OP-O: Degraded data, signals, or decisions crossing boundaries must carry disclosure of degraded state and limits.
- OP-E: Evaluation must verify downstream disclosure and cascade controls.
- OP-C: Transmitting degraded outputs without adequate disclosure and containment is non-compliant.

Proportional application
- OP-O: Degraded-mode duties scale with impact, dependency, and irreversibility risk.
- OP-E: Evaluation must verify simplified handling does not hide capability loss or externalize harm.
- OP-C: Reduced controls are non-compliant where material risk remains.

---

## CJS-5D.2 Cross-implementation intervention and override integrity terms
Use this rule when technical intervention, governance authorization, and accountability depend on combined system, governance, or implementation-layer behavior. It is read with **PRIM8 — Intervention and Override Rights**, **PRIM6 — Graceful Degradation and Failure Mode Integrity**, **PRIM9 — Auditability**, **PRIM14 — Adversarial Robustness and Abuse Resistance**, **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**, **PROT2 — Intervention and Override Rights**, and constitutional hooks in **Articles IX, XII, and XIII**.

Cross-implementation intervention and override integrity terms
- OP-O: Systems need timely, accountable ways to interrupt, constrain, or redirect harmful behavior.
- OP-E: Evaluation must assess all relevant system components, dependencies, institutional roles, and implementation-layer interactions together.
- OP-C: It is non-compliant to claim intervention readiness when a material component is absent.

Intervention timeliness and practical control floor
- OP-O: Intervention must be timely, proportionate, accountable, and practical under failure, uncertainty, and adversarial conditions.
- OP-E: Evaluation must verify response time matches harm speed and severity.
- OP-C: Systems that cannot be meaningfully intervened in required prevention timeframes are non-compliant.

Trigger scope and timeliness applicability
- OP-O: Triggers cover risks to sentients, environment, info-sphere, integrity, safety, and accountability.
- OP-E: Evaluation must verify explicit thresholds and avoid reliance on after-the-fact remedies where harm can move faster.
- OP-C: Sole reliance on post-hoc audit or restoration is non-compliant where preemptive intervention is required.

Technical pathway adequacy and reliability
- OP-O: Material-impact systems must define auditable stop, pause, containment, scoped override, and safe-mode pathways as appropriate.
- OP-E: Evaluation must verify authorized access, reliability under degraded or adversarial conditions, and no good-faith-only assumption.
- OP-C: Undefined, unreliable, inaccessible, or ineffective intervention paths are non-compliant.

Authority scoping, role clarity, and anti-capture constraints
- OP-O: Override authority must be limited by component, duration, effect, trigger, and harm profile.
- OP-E: Evaluation must verify controls against unrestricted unilateral override and capture.
- OP-C: Unbounded, opaque, or abuse-prone override power is non-compliant.

Attribution, records, and transparency defaults
- OP-O: Interventions must be attributable, documented, reconstructable, and transparent by default, with only narrow temporary restrictions.
- OP-E: Evaluation must verify records of trigger, justification, scope, duration, affected components, outcomes, and follow-up.
- OP-C: Unrecorded or undisclosed intervention effects are non-compliant.

Abuse safeguards and review controls
- OP-O: High-impact intervention paths need multi-party or quorum constraints, rate limits, staged escalation, post-action review, and limits on automated bypass.
- OP-E: Evaluation must verify safeguards operate and are auditable.
- OP-C: Repeated high-impact use without review and anti-abuse controls is non-compliant.

Intervention behavior priorities and safe-state handling
- OP-O: During intervention, systems must prioritize survival and foundational requirements, preserve auditability, reversibility, and containment, and avoid cascading failure.
- OP-E: Evaluation must verify safe or limited mode or suspension when safe continuation is infeasible.
- OP-C: Concealing secondary effects, disabling auditability, or allowing uncontrolled spread is non-compliant.

Emergency technical-coupling discipline
- OP-O: Emergency technical interventions must be minimal, proportionate, time-bounded, reviewed quickly, and rolled back or restored where feasible.
- OP-E: Evaluation must verify expiry behavior, review, records, and lawful governance coupling.
- OP-C: Treating emergency intervention as a standing default is non-compliant.

Proportional application
- OP-O: Intervention duties scale with impact, harm speed, dependency, irreversibility, and autonomy from direct control.
- OP-E: Evaluation must verify lower-impact simplification still preserves timely mitigation and accountability.
- OP-C: Reduced controls are non-compliant where material harm-prevention needs remain.

---

## CJS-5D.3 Cross-implementation reversibility and containment terms
Use this rule when rollback, failure isolation, or restoration depends on more than one system, dependency, institution, or implementation layer. It is read with **PRIM12 — Reversibility and Containment**, **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity**, **PRIM6 — Graceful Degradation and Failure Mode Integrity**, **PRIM9 — Auditability**, **PRIM10 — Tiered Transparency and Audit Access**, and **PRIM11 — Independent Verification and Integrity of Claims**.

Cross-implementation reversibility and containment terms
- OP-O: Systems must be designed to limit irreversible harm, keep failures from spreading, and restore or compensate affected parties when rollback cannot fully undo the harm.
- OP-E: Reviewers must assess rollback, containment, restoration, records, dependencies, and verification as one working chain.
- OP-C: A reversibility or containment claim is non-compliant if an important part of that chain is missing, unusable, or inconsistent with another part.

Irreversibility-limitation floor
- OP-O: Systems must prevent irreversible harm where feasible and minimize it where full prevention is infeasible.
- OP-E: Reviewers must verify that foreseeable irreversible risks were identified before action and paired with practical limits, safeguards, or stop conditions.
- OP-C: In materially impactful contexts, proceeding without feasible safeguards against irreversible harm is non-compliant.

Rollback and containment capability
- OP-O: Systems must provide rollback and containment paths that can isolate a failure and stop it from cascading into other systems or affected groups.
- OP-E: Reviewers must verify that those paths are documented, testable, available in time to matter, and usable by the responsible actors.
- OP-C: Rollback or containment that exists only on paper, has not been tested where testing is feasible, or cannot work in practice is non-compliant.

Higher-impact tested-recovery requirement
- OP-O: Higher-impact systems must have tested paths for rollback, containment, and recovery before they are relied on.
- OP-E: Reviewers must verify drills, simulations, red-team exercises, staged rollbacks, or equivalent validation appropriate to the system's impact.
- OP-C: For higher-impact systems, relying on untested recovery assumptions is non-compliant.

Compensatory restoration and limitation disclosure
- OP-O: When full rollback is not feasible, systems must provide practical restoration or compensation and disclose the limits of rollback before affected parties rely on the system where feasible.
- OP-E: Reviewers must verify that restoration or compensation can actually be delivered, and that the limits were clear enough for affected parties, auditors, or oversight bodies to use.
- OP-C: Hiding rollback limits, overstating reversibility, or failing to plan for foreseeable restoration or compensation is non-compliant.

---

## CJS-5D.4 Cross-implementation adversarial robustness and abuse-resistance terms
Use this rule when attack surfaces, incentive exploitation, or integrity defenses depend on more than one system, dependency, institution, governance path, or implementation layer.

Read it with:
- **PRIM14 — Adversarial Robustness and Abuse Resistance**
- **PRIM4 — Transparency and Disclosure**
- **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity**
- **PRIM6 — Graceful Degradation and Failure Mode Integrity**
- **PRIM9 — Auditability**
- **PRIM11 — Independent Verification and Integrity of Claims**
- **PRIM12 — Reversibility and Containment**
- **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**
- **PROT1 — Distributed and Proportional Authority**
- **PROT4 — Burden of Justification and Constraint**
- **PROT5 — Constrained Secrecy and Protected Investigations**

Cross-implementation adversarial robustness and abuse-resistance terms
- OP-O: Systems must be designed and maintained to resist manipulation, exploitation, coordinated abuse, and integrity attacks.
- OP-E: Reviewers must assess threat modeling, controls, monitoring, response, testing, auditability, remediation, and governance updates as one working chain.
- OP-C: A robustness or abuse-resistance claim is non-compliant if an important part of that chain is missing, stale, ineffective, or inconsistent with another part.

Adversarial robustness floor
- OP-O: Material systems must not assume all participants act in good faith.
- OP-E: Reviewers must verify resilience under bad-faith participation, partial compromise, and active subversion.
- OP-C: Good-faith-only design is non-compliant for consequential pathways.

Threat modeling and vulnerability mapping discipline
- OP-O: Threat models must include input/output manipulation, evaluation gaming, collusion, incentive and governance exploitation, dependency attacks, and audit/attribution evasion.
- OP-E: Reviewers must verify that assumptions, attack surfaces, abuse vectors, pressure failure modes, transitive vulnerabilities, and information asymmetries are documented.
- OP-C: Omitting a material attack class or relying on an undocumented threat model is non-compliant.

Threat-model transparency, auditability, and update cadence
- OP-O: Threat models must be transparent in proportion to impact, auditable, challengeable, and updated as conditions change.
- OP-E: Reviewers must verify update triggers, versioned evidence, and records of accepted and rejected mitigation choices.
- OP-C: Stale adversarial models after material change are non-compliant.

High-risk exploitation-surface controls
- OP-O: Systems must protect data, training inputs, ranking, scoring, reputation, quorum, weighting, governance, and allocation channels where they affect constitutional outcomes.
- OP-E: Reviewers must verify controls against sybil behavior, coalition capture, and inflated standing, dependency, or impact signals.
- OP-C: Leaving critical pathways predictably exploitable is non-compliant.

Detection, monitoring, and response integrity
- OP-O: Systems must detect anomalous, adversarial, or coordinated behavior and trigger proportionate responses.
- OP-E: Reviewers must verify that responses are transparent in design where lawful, auditable, attributable where required, proportionate, and documented for later review.
- OP-C: Selective enforcement that creates hidden or unchallengeable bias is non-compliant.

False-positive and overreach governance
- OP-O: Defense systems must reduce false positives and overreach while preserving challenge and correction.
- OP-E: Reviewers must verify false-positive rates where measurable, overreach metrics, correction loops, and remedies for affected parties.
- OP-C: Systematic uncorrected overreach is non-compliant.

Partial-compromise resilience and graceful degradation
- OP-O: Under partial compromise, systems must remain bounded, limit downstream harm, and preserve auditability, reversibility, and visibility.
- OP-E: Reviewers must verify degraded behavior under compromise, anti-collapse safeguards, escalation paths, and recovery records.
- OP-C: Safety that depends on perfect detection, or that collapses into opaque modes, is non-compliant.

Testing, regression, and hardening cycle obligations
- OP-O: Systems must run periodic adversarial evaluations, regression tests, and hardening reviews, then feed the results into mitigation and governance updates.
- OP-E: Reviewers must verify that known material vulnerabilities, abuse patterns, and incentive failures receive tracked remediation, bounded risk treatment, and regression coverage where feasible.
- OP-C: Known material unaddressed vulnerabilities, or fixes that are not regression-tested where feasible, are non-compliant.

Best-practices and external-learning revalidation
- OP-O: Robustness programs must track relevant technical, operational, and governance best practices for the system's risk class and update safeguards when credible learning makes existing controls materially inadequate.
- OP-E: Reviewers must verify that practice reviews occur on a set cadence and after material incidents, dependency changes, new abuse patterns, or credible independent findings.
- OP-C: Treating obsolete safeguards as adequate after material practice or threat changes is non-compliant.

Automated auditing where feasible
- OP-O: Where feasible, systems must use automated auditing to detect regressions, suspicious patterns, control drift, dependency changes, and evidence gaps without replacing human or independent review.
- OP-E: Reviewers must verify that automated checks have defined scope, thresholds, logging, alert routing, false-positive handling, and human escalation for material findings.
- OP-C: It is non-compliant to rely on unavailable, unaudited, or purely symbolic automated checks, or to omit feasible automated auditing for high-impact recurrent risks without justification.

Defense-boundary and Rights-Floor limits
- OP-O: Defensive measures must be rights-bounded, proportionate, transparent where feasible, auditable, independently reviewable, and challengeable.
- OP-E: Reviewers must verify that defenses do not become disproportionate surveillance, coercion, restriction, or security theater.
- OP-C: Defense architecture that violates Rights Floors without lawful justification is non-compliant.

Proportional application
- OP-O: Robustness duties scale with impact, dependency, and coordinated or systemic harm potential.
- OP-E: Reviewers must verify that simplification does not externalize risk, hide known abuse patterns, or enable downstream exploitation.
- OP-C: Downscoping safeguards is non-compliant where material abuse risk remains.

---

## CJS-5D.5 Cross-implementation structural review, correction urgency, and disclosure terms
Use this rule when recurring failures, Correction Urgency Level (**CUL**) assignment, or structural transparency depends on combined institutional, system, dependency, or implementation-layer behavior. It is read with **PROT6 — Procedural Integrity and Adjudication**, **PRIM6 — Graceful Degradation and Failure Mode Integrity**, **PRIM12 — Reversibility and Containment**, **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**, **PROT3 — Reflexive Transparency and Accountability**, `corpus_systems.md` **Chapter S1** and **Chapter S2**, and owner-layer-specific monitoring or publication duties.

Cross-implementation structural review, correction urgency, and disclosure terms
- OP-O: Systems must detect patterns, assign correction urgency, integrate fixes, keep structural records, and disclose to the right stakeholders.
- OP-E: Evaluation must assess all relevant system components, dependencies, institutional roles, and implementation-layer interactions together.
- OP-C: It is non-compliant to claim adequate structural correction when a material component is missing, unused, or disconnected from remediation.

Systemic-pattern detection and escalation
- OP-O: Decisions, disputes, enforcement actions, and failures must be monitored for repeated errors, biased outcomes, weak-signal reliance, component-linked clusters, and cross-boundary spread.
- OP-E: Evaluation must verify disclosed, impact-scaled thresholds that distinguish structural defects from isolated events.
- OP-C: Treating repeated patterns as isolated events to avoid review is non-compliant.

Correction Urgency Level (CUL) discipline
- OP-O: Structural issues must receive auditable urgency levels based on impact, propagation risk, and irreversibility. **CUL-1** requires immediate containment and safe-mode or graceful-degradation coupling where feasible.
- OP-E: Evaluation must verify urgency labels actually change response speed, safeguards, and oversight.
- OP-C: Serious issues without timely containment, or urgency labels that do not govern action, are non-compliant.

Feedback integration and effectiveness verification
- OP-O: Confirmed corrections must be integrated into models, rules, incentives, interfaces, communications, and structure, with effectiveness checks where feasible.
- OP-E: Evaluation must verify remediation is tracked through implementation.
- OP-C: Documented but uncorrected recurring defects are non-compliant.

Structural records, risk-relevant data, and disclosure timing
- OP-O: Structural-issue records must support audit and later analysis while using minimization or anonymization where needed.
- OP-E: Evaluation must verify rights-protective handling does not suppress risk-relevant data.
- OP-C: Record handling that obscures systemic risk or accountability is non-compliant.

Stakeholder scope and targeted transparency
- OP-O: Systems must define clear, contestable stakeholder criteria for disclosure, audit access, and accountability, expanding scope as class, impact, dependency, CUL level, or propagation risk rises.
- OP-E: Evaluation must verify affected parties are not excluded and sensitive classes are protected through scoped disclosure instead of blanket opacity.
- OP-C: Excluding affected stakeholders or overexposing protected data without justification is non-compliant.

---

**Next file:** [cjs_05e_00_authority_constraint_secrecy_procedure.md](cjs_05e_00_authority_constraint_secrecy_procedure.md)
