## CJS-5D.1 Cross-implementation graceful degradation and failure-mode integrity terms
Use this rule when reliability, signaling, containment, or recovery depends on combined system, dependency, or implementation-layer behavior. It is read with **PRIM6 — Graceful Degradation and Failure Mode Integrity**, **PRIM1 — System Status, Risk, and Scope Representation**, **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity**, **PRIM12 — Reversibility and Containment**, **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**, and `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**.

Cross-implementation graceful degradation and failure-mode integrity terms
- OP-O: Systems must behave honestly and safely under partial failure, uncertainty, or stress.
- OP-E: Evaluation must apply all component entries together.
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

**Next file:** [cjs_05d_02_intervention_override_integrity_terms.md](cjs_05d_02_intervention_override_integrity_terms.md)
