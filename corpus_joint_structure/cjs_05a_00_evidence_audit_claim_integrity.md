## CJS-5A: Evidence, audit, and claim integrity

This family collects the operational clusters that make cross-implementation claims reviewable: integrity assurance, audit records, tiered access, and independent verification.

| Cluster | Section |
|---|---|
| **CJS-5A.1** | Cross-implementation integrity assurance and resilience operations |
| **CJS-5A.2** | Cross-implementation auditability and reconstructability terms |
| **CJS-5A.3** | Cross-implementation tiered transparency and audit-access terms |
| **CJS-5A.4** | Cross-implementation independent verification and claim-integrity terms |

---

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

## CJS-5A.2 Cross-implementation auditability and reconstructability terms
Use this rule when records, access pathways, or verification design depend on combined system, dependency, or implementation-layer behavior. It is read with **PRIM9 — Auditability**, **PRIM4 — Transparency and Disclosure**, **PRIM10 — Tiered Transparency and Audit Access**, **Article XV-A**, and **Article VII-B**.

Cross-implementation auditability and reconstructability terms
- OP-O: Records must be verifiable, independently reviewable, and adequate for reconstructing harm or disputes.
- OP-E: Evaluation must apply all component entries together.
- OP-C: It is non-compliant to claim auditability when a material component is absent or unusable.

Auditability floor and record sufficiency
- OP-O: Systems must keep records sufficient to evaluate compliance, reconstruct material behavior, and verify material claims.
- OP-E: Evaluation must verify record scope, quality, and retention in practice.
- OP-C: Recordkeeping is non-compliant when records lack the scope, provenance, intelligibility, continuity, or retention needed for a qualified reviewer to evaluate compliance, reconstruct material behavior, or verify material claims.

Operational transparency and structured logging requirements
- OP-O: Systems must provide impact-proportional operational transparency and structured audit logs.
- OP-E: Evaluation must verify logs are intelligible, attributable, and navigable.
- OP-C: Unstructured, inaccessible, or insufficient logging is non-compliant.

Forensic-depth access proportionality
- OP-O: Deeper forensic access must be available when harm, credible risk, or investigation needs require full reconstruction.
- OP-E: Evaluation must verify escalation from ordinary records to forensic depth is real and timely.
- OP-C: Forensic access is non-compliant when escalation produces records, tools, permissions, or reviewer conditions that are too incomplete, delayed, constrained, or unintelligible to support the required reconstruction.

Article VII-B boundary and anti-concealment rule
- OP-O: **Article VII-B** protects private internal states, but that protection does not excuse systems from showing what they did, why it mattered, who or what was responsible, and what external effects followed.
- OP-E: Evaluation must verify that privacy limits protect internal states without preventing lawful audit of actions, outputs, decisions, effects, responsibilities, or control pathways.
- OP-C: It is non-compliant to invoke internal-state protection in a way that conceals accountability-relevant system behavior or prevents lawful reconstruction of external facts.

---

## CJS-5A.3 Cross-implementation tiered transparency and audit-access terms
Use this rule when public visibility, qualified review, or forensic reconstruction depends on how multiple systems, dependencies, institutions, or implementation layers work together. It is read with **PRIM10 — Tiered Transparency and Audit Access**, **PRIM9 — Auditability**, **PRIM12 — Reversibility and Containment**, **Article XV-A**, and **Article VII-B**.

Cross-implementation tiered transparency and audit-access terms
- OP-O: Access to information must be tiered so systems can be transparent, auditable, protective of lawful internal-state boundaries, and open to challenge.
- OP-E: Evaluation must review the access tiers, audit routes, protection limits, and challenge paths together.
- OP-C: A system cannot claim tiered transparency if a required part is missing, unreachable, or too unclear to use.

Tier structure and baseline accessibility
- OP-O: Baseline access must let materially affected stakeholders understand what the system does, what risks it creates, what dependencies it has, and how they can participate.
- OP-E: Evaluation must verify that baseline access works for ordinary use, not only in theory.
- OP-C: Access tiers are non-compliant if the baseline is too thin for meaningful participation or risk review.

Class A/B/C public-interest visibility
- OP-O: For Class A, Class B, and Class C systems, public baseline access must cover the system purpose, classification, dependency structure, operational status, material risks, performance, failures, governance, audit outcomes, stakeholder effects, and constitutional compliance, subject to `corpus_systems.md` Chapter S1 data handling.
- OP-E: Evaluation must verify that protected data limits are handled through the maximum feasible public substitute, such as aggregation, de-identification, summary disclosure, delayed disclosure, or qualified audit access.
- OP-C: It is non-compliant to use privacy, security, confidentiality, proprietary interest, or investigation status to suppress public-interest visibility where a narrower substitute would preserve accountability.

Qualified audit pathways and non-exclusive eligibility
- OP-O: When full public access is inappropriate, qualified independent audit paths must still exist, and eligibility rules must be public and non-exclusive.
- OP-E: Evaluation must verify that qualified reviewers can realistically enter those paths and that no actor controls access unfairly.
- OP-C: Qualification rules are non-compliant if they hide exclusion or make independent audit unreachable in practice.

Restriction scope and justification discipline
- OP-O: Access restrictions must be narrow, justified, tied to time or review points, and open to audit.
- OP-E: Evaluation must verify the reason for each restriction, what it covers, how long it lasts, and how it is reviewed.
- OP-C: Restrictions are non-compliant when they are broad, indefinite, or shielded from review.

Forensic escalation and reconstruction sufficiency
- OP-O: Harm, dispute, or credible risk must trigger enough access to reconstruct what happened when reconstruction is necessary and feasible.
- OP-E: Evaluation must verify that escalation to forensic-depth review works within the time needed for the issue.
- OP-C: Forensic pathways are non-compliant if they are blocked when material reconstruction is required.

Access-control integrity and anti-concealment
- OP-O: Access controls must be understandable in design, auditable in operation, and open to challenge.
- OP-E: Evaluation must verify that the controls preserve accountability across implementation boundaries.
- OP-C: Access design is non-compliant if it hides systemic behavior or blocks meaningful challenge.

---

## CJS-5A.4 Cross-implementation independent verification and claim-integrity terms
Use this rule when evidence quality, verification routes, or trust claims depend on how multiple systems, dependencies, or implementation layers work together.

It is read with **PRIM11 — Independent Verification and Integrity of Claims**, **PRIM9 — Auditability**, and **PRIM10 — Tiered Transparency and Audit Access**. It is also read with Chapter Fourteen and rights-layer protections where material claims shape rights-relevant decisions.

Cross-implementation independent verification and claim-integrity terms
- OP-O: Material claims must be independently checkable where doing so is feasible.
- OP-E: Evaluation must review the claim, evidence, access route, reviewer independence, and verification limits together.
- OP-C: A system cannot treat material claims as reliable if required verification paths are missing, blocked, or too weak to use.

Material-claim verification scope
- OP-O: Material claims about behavior, compliance, impact, safety, reliability, environmental effects, information integrity, governance, or algorithms must be independently verifiable where feasible. Reproducible testing is required where feasible.
- OP-E: Evaluation must match each claim family with the verification path and evidence standard needed to test it.
- OP-C: Consequential claims are non-compliant if they are exempted from verification without lawful technical-feasibility grounds.

Reproducibility and external evaluation viability
- OP-O: Evidence and methods must let qualified independent reviewers reproduce results and compare them with alternative evaluations.
- OP-E: Evaluation must verify that documentation, data access, assumptions, and limits are sufficient for external review.
- OP-C: Methods are non-compliant if they are opaque or non-reproducible where reproducibility is feasible.

Anti-single-authority verification constraint
- OP-O: Material verification should not depend on a single authority, model, vendor, institution, or framework.
- OP-E: Evaluation must verify at least one practical independent path beyond the controlling authority where feasible.
- OP-C: Claims are non-compliant if they are monopoly-gated when independent verification is technically feasible.

Class-scaled template floor mapping
- OP-O: Class-scaled templates must preserve reconstructable audit records, qualified deeper audit access, and at least one independent verification path for material claims.
- OP-E: Evaluation must verify that simplification changes only volume, format, or cadence, not the required verification capability.
- OP-C: A simplified template is non-compliant if it removes a required verification floor.

---

**Next file:** [cjs_05b_00_participation_comprehension_disclosure.md](cjs_05b_00_participation_comprehension_disclosure.md)
