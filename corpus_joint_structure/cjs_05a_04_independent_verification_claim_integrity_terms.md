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
