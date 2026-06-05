## CJS-5C.3 Cross-implementation data-retention and lifecycle-integrity terms
Use this rule when accountability, privacy, reversibility, or classification depends on how data is kept, changed, linked, or deleted across more than one system or implementation layer.

Read it with:
- **PRIM9 — Auditability**
- **PRIM10 — Tiered Transparency and Audit Access**
- **PRIM11 — Independent Verification and Integrity of Claims**
- **PRIM12 — Reversibility and Containment**
- **PRIM15 — Evolution, Revalidation, and Non-Entrenchment**
- `corpus_systems.md` **Chapter S1**, including Types **C**, **G**, **H**, **I**, **N**, and **S**
- **CJS-3.5**

Cross-implementation data-retention and lifecycle-integrity terms
- OP-O: Data may be kept only for a justified reason, within clear limits, and with regular review from collection through deletion or de-identification.
- OP-E: Reviewers must assess purpose, S1 data type or types, duration, detail, access, deletion, reclassification, disclosure, and audit needs together.
- OP-C: A retention-integrity claim is non-compliant if an important part of that lifecycle is missing, unusable, or inconsistent with another part.

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

Classification and S1 data-type alignment
- OP-O: If accumulated, linked, or inferred data changes S1 type or becomes more sensitive in practice, stricter protections apply.
- OP-E: Reviewers must verify alignment with **S1** data-type duties and **CJS-3.5** where supervision and systems classification overlap.
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
