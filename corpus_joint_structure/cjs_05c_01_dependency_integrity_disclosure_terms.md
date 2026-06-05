## CJS-5C.1 Cross-implementation dependency integrity and disclosure terms
Use this rule when dependency mapping, risk treatment, or accountability depends on combined system, dependency, or implementation-layer behavior. It is read with **PRIM5 — Dependency Awareness, Disclosure, and Risk Integrity**, **PRIM4 — Transparency and Disclosure**, **PRIM7 — Interoperability, Portability, and Exit Integrity**, **PRIM9 — Auditability**, **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**, `corpus_systems.md` **Protocol A — System Design, Testing, Verification, and Deployment**, and **Article XV-A**.

Cross-implementation dependency integrity and disclosure terms
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

**Next file:** [cjs_05c_02_interoperability_portability_exit_integrity_terms.md](cjs_05c_02_interoperability_portability_exit_integrity_terms.md)
