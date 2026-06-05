## CJS-5A.1 Cross-implementation integrity assurance and resilience operations
Use this rule for **CJS-R19**, cross-implementation integrity assurance and resilience operations. It relies on, but does not replace, core definitions such as auditability, verifiability, reversibility, dependency, cascading failure, adversarial conditions, and trustworthiness.

Cross-implementation integrity assurance and resilience operations
- OP-O: Integrity claims depend on the whole chain when records, access, classification, stewardship, challenge, or adjudication are split across systems, institutions, dependencies, or implementation layers.
- OP-E: Evaluation must test the chain end to end, including normal, degraded, and adversarial conditions.
- OP-C: A chain is non-compliant if required conditions are missing, blocked, contradictory, or practically unusable. A strong control in one part of the chain cannot cure a material failure in another.

Audit reconstruction and tiered access continuity
- OP-O: Records, disclosure tiers, qualified audit access, and forensic reconstruction must work together when harm, dispute, or credible risk requires deeper inspection.
- OP-E: Evaluation must verify that records, access gates, qualification routes, and challenge routes support independent review and root-cause reconstruction.
- OP-C: It is non-compliant to keep records that cannot practically be reconstructed, or to publish audit-access criteria that block a real path to qualified independent audit.

Independent verification path integrity
- OP-O: Material claims must have practical routes for independent testing, reproduction, and comparison.
- OP-E: Evaluation must verify at least one practical independent verification path for each materially significant claim family.
- OP-C: It is non-compliant to require reliance on unverifiable, single-authority, or non-reproducible claims when independent verification is technically feasible.

Containment, reversibility, and retention lifecycle coherence
- OP-O: Failure isolation, rollback, compensatory restoration, and data-retention rules must work together.
- OP-E: Evaluation must verify that restoration keeps enough records for accountability while avoiding unjustified data accumulation or surveillance.
- OP-C: It is non-compliant to delete records needed for investigation or keep granular data that creates unjustified coercive leverage.

Adversarial response and revalidation non-entrenchment
- OP-O: Detection, mitigation, escalation, revalidation, and replacement readiness must operate together as risks change.
- OP-E: Evaluation must verify review cadence, challengeability, and update paths under changing capabilities, attacks, and dependencies.
- OP-C: It is non-compliant to preserve legacy structures by inertia when material risk, drift, or known vulnerabilities require correction, reauthorization, or replacement.

---

**Next file:** [cjs_05a_02_auditability_reconstructability_terms.md](cjs_05a_02_auditability_reconstructability_terms.md)
