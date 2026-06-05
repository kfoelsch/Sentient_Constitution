## CJS-5B.4 Cross-implementation disclosure sufficiency and observability terms
Use this rule when informed participation, independent verification, or attribution depends on disclosure across systems, dependencies, institutions, or implementation layers. It is read with **PRIM4 — Transparency and Disclosure**, **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity** where dependencies matter, **Article XV-A**, and **Article VII-B**.

Cross-implementation disclosure sufficiency and observability terms
- OP-O: Affected parties must be given enough clear information to understand what is happening, why it matters, who or what is responsible, and how the claim can be checked.
- OP-E: Reviewers must look at the whole disclosure path, including summaries, detailed records, audit routes, privacy limits, and dependency information where relevant.
- OP-C: A system is non-compliant if it claims transparency while leaving out information affected parties reasonably need for consent, participation, oversight, challenge, or independent verification.

Impact- and dependency-proportional disclosure sufficiency
- OP-O: The more a decision can affect sentients, communities, institutions, the environment, or other systems, the more complete the disclosure must be.
- OP-E: Reviewers must check whether the level of detail fits the real stakes, including how dependent affected parties are on the system and how hard it would be for them to avoid or challenge the result.
- OP-C: Small, vague, or decorative disclosures are non-compliant when the impact or dependency is serious enough to require more.

Minimum disclosure content set
- OP-O: When the information is material, disclosures must explain the system's purpose, major assumptions, methods, criteria, classification choices, decision logic, known risks, limits, uncertainty, and important dependencies.
- OP-E: Reviewers must check whether those pieces are present, accurate enough to use, and connected to the actual records or behavior of the system.
- OP-C: Leaving out a material assumption, risk, limit, dependency, criterion, or decision factor is non-compliant if the omission would make affected parties less able to understand, verify, participate, or challenge.

Verification and comparative interpretation enablement
- OP-O: Disclosure must make it practically possible to check the system's claims, compare alternatives, and notice important blind spots or failures.
- OP-E: Reviewers must verify at least one realistic path for qualified independent checking, including access to enough records, methods, samples, logs, or explanations to test the claim.
- OP-C: A disclosure is non-compliant if it sounds informative but cannot actually be used to verify what happened, compare options, find errors, or assign responsibility.

Private internal-state boundary and external observability attribution
- OP-O: Transparency does not give anyone a right to expose protected private internal states under **Article VII-B**. But actions, outputs, external effects, decisions, and responsibility must still be observable and attributable.
- OP-E: Reviewers must check both sides of the boundary: privacy must be protected, and accountability for external behavior must remain possible.
- OP-C: It is non-compliant either to force unlawful exposure of private internal states or to use privacy as an excuse to hide observable conduct, impacts, decision paths, or responsible actors.

---

**Next file:** [cjs_05c_00_dependency_exit_lifecycle_integrity.md](cjs_05c_00_dependency_exit_lifecycle_integrity.md)
