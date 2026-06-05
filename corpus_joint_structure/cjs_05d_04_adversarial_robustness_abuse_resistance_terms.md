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

**Next file:** [cjs_05d_05_structural_review_correction_urgency_disclosure_terms.md](cjs_05d_05_structural_review_correction_urgency_disclosure_terms.md)
