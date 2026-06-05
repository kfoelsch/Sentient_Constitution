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

**Next file:** [cjs_05d_04_adversarial_robustness_abuse_resistance_terms.md](cjs_05d_04_adversarial_robustness_abuse_resistance_terms.md)
