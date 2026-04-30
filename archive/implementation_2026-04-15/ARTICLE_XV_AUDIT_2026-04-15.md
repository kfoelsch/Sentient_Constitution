# Article XV audit

Status: implementation review artifact (non-authoritative).  
Date: 2026-04-15.  
Scope: application of the Article-Principle-Definition audit rubric to `Article XV: System Lifecycle, Environments, and Reversibility`.

## Overall assessment

Article XV is constitutionally well aimed and already tracks the larger lifecycle architecture in `Protocol A`, `PRIM12`, and the Chapter One safety-truth discipline. Its main weakness was not doctrinal mismatch, but surface underexposure: too much of the continuity, restoration, and anti-evasion logic still had to be supplied from incorporated materials rather than read directly from the article text.

The main issues were publication-shape and anti-evasion visibility issues rather than substantive error:
- the chapeau correctly established disciplined lifecycle governance, but it did not show quite clearly enough that the protected object is continuous stewardship across design, deployment, operation, and restoration;
- `Article XV-A` had the correct environment-separation rule, but it left cross-environment state, credential, and promotion integrity more implicit than ideal for publication reading;
- `Article XV-B` properly required progressive deployment and reversibility, yet it did not make auditable restoration criteria and continuity after partial rollback visible enough on the page;
- `Article XV-C` identified misclassification and evasion, but it still named too narrow a failure mode and did not directly capture fragmentation, relabeling, or sandbox-style obligation avoidance.

Overall judgment: `publishable after targeted edits`.

## Worksheet

| Article unit | Operative claim | Principle anchor | Definition anchors | Ch. 2-4 mechanics | Principle | Definition | Logic | Constraints | Publish | Severity | Finding type | Drafting close |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| Article XV (chapeau) | Materially affecting systems owe impact-scaled lifecycle stewardship that preserves safety, epistemic integrity, and challenge rights through the full functional lifecycle | Chapter One `3.1`, `3.2`, `6.1`, `6.2.1` | Safety (Constraint); Epistemic Integrity; Dependency; Reversibility | systemic evaluation; burden and traceability; anti-evasion; lifecycle continuity | 3 | 2 | 2 | 2 | 2 | Moderate | Underreach | Make full-lifecycle continuity and restoration visibility explicit in the lead |
| Article XV-A | High-impact and non-experimental systems must maintain separable environments with controlled promotion and no bypass from non-production into production safeguards | Chapter One `3.1`, `6.1`, `7.1` | System Boundary Integrity; Risk; Auditability; Transparency | same-scope application; observability; traceability; anti-fragmentation | 3 | 2 | 2 | 2 | 2 | Moderate | Burden/trace error | Surface promotion integrity and cross-environment bypass controls more directly |
| Article XV-B | Deployment must be progressive, documented, and reversible, with restoration pathways proportionate to harm and irreversibility risk | Chapter One `3.1`, `6.1`, `6.2.1` | Reversibility; Dependency; Risk; Safety and Non-Degradation Baseline (Constitutional) | precaution under uncertainty; documentation sufficiency; restoration traceability; challengeability | 3 | 2 | 2 | 2 | 2 | Moderate | Underreach | Make restoration criteria and auditable continuity after incomplete rollback explicit |
| Article XV-C | Lifecycle obligations may not be avoided by misclassification, fragmentation, relabeling, or sandbox claims when full functional effects trigger higher duties | Chapter One `3.1`, `3.2`, `6.1`, `9` | Classification-Scaled Governance; Material Impact; Dependency; Accountability | anti-evasion; anti-fragmentation; full-functional evaluation; burden of proof | 3 | 2 | 2 | 3 | 2 | Moderate | Ambiguity risk | Expand the anti-evasion clause to include fragmentation and relabeling, not only reduced-obligation claims |

## Findings

### Article XV (chapeau)

- Operative claim: Article XV establishes a right to lifecycle stewardship for materially affecting systems, scaled to impact, dependency, and irreversibility.
- Principle anchor: Chapter One `3.1 Safety`, `3.2 Truth`, `6.1 Core Tradeoff Principles`, and `6.2.1 Preservation of Epistemic Integrity`.
- Definition anchors: `Safety (Constraint)`, `Epistemic Integrity`, `Dependency`, and `Reversibility (Constitutional)`.
- Mechanics: the article lead should signal that the constitutional concern is not just careful launch posture, but preservation of safety, truth, and challengeability across the whole functional lifecycle, including restoration when systems degrade or must be rolled back.
- Scores: Principle `3` / Definition `2` / Logic `2` / Constraints `2` / Publish `2`
- Finding: [Moderate] [Underreach] The lead was directionally correct, but it left continuity across deployment, operation, incident response, and restoration more implicit than ideal for publication.
- Why it matters: lifecycle governance can be underread as a pre-launch engineering rule if the article does not clearly show that stewardship duties persist after deployment and through rollback or restoration.
- Smallest close: add a short clause making the protected stewardship continuous across the functional lifecycle, including restoration and retirement where material.

### Article XV-A

- Operative claim: high-impact and non-experimental systems must maintain meaningful operational separation between environments.
- Principle anchor: Chapter One `3.1 Safety`, `6.1 Core Tradeoff Principles`, and `7.1 Required Evaluation Factors`.
- Definition anchors: `Risk`, `Auditability`, `Transparency`, and `System Boundary Integrity`.
- Mechanics: environment separation must remain observable and traceable in practice, which means promotion, state transfer, and cross-environment access cannot remain merely assumed.
- Scores: Principle `3` / Definition `2` / Logic `2` / Constraints `2` / Publish `2`
- Finding: [Moderate] [Burden/trace error] The subsection required separable environments and documented promotion paths, but it did not make clear enough that promotion, persistent state, and cross-environment authorization integrity must be controlled so non-production cannot functionally bypass production safeguards.
- Why it matters: many real lifecycle failures arise not from nominal absence of environments, but from shared credentials, reused state, or informal promotion paths that dissolve the separation in practice.
- Smallest close: add explicit language on validated promotion and environment-specific control over state or access capable of bypassing production protections.

### Article XV-B

- Operative claim: deployment and change management must be progressive, documented, and reversible, with restoration pathways proportionate to harm.
- Principle anchor: Chapter One `3.1 Safety`, `6.1 Core Tradeoff Principles`, and `6.2.1 Preservation of Epistemic Integrity`.
- Definition anchors: `Reversibility (Constitutional)`, `Dependency`, `Risk`, and `Safety and Non-Degradation Baseline (Constitutional)`.
- Mechanics: reversibility includes rollback, containment, and compensatory restoration where full rollback is infeasible, and those pathways must remain documented, reviewable, and challengeable under the audit-and-trace structure.
- Scores: Principle `3` / Definition `2` / Logic `2` / Constraints `2` / Publish `2`
- Finding: [Moderate] [Underreach] The subsection already required rollback, containment, and compensatory restoration, but it did not show clearly enough that restoration criteria and incomplete-rollback continuity plans must remain auditable and stakeholder-visible.
- Why it matters: without visible restoration criteria, reversibility can degrade into a vague aspiration even where rollback is partial, delayed, or impossible in the strongest sense.
- Smallest close: tie deployment escalation and reversibility mechanisms to documented restoration or containment criteria and auditable continuity planning where rollback is incomplete.

### Article XV-C

- Operative claim: systems may not evade lifecycle obligations by understating or disguising their true impact profile.
- Principle anchor: Chapter One `3.1 Safety`, `3.2 Truth`, `6.1 Core Tradeoff Principles`, and `9. Interpretive Role`.
- Definition anchors: `Classification-Scaled Governance`, `Material Impact`, `Dependency`, and `Accountability`.
- Mechanics: Chapters Two through Four require full-functional, anti-fragmentation, anti-evasion reading rather than local labels, declared system class, or selectively bounded scope.
- Scores: Principle `3` / Definition `2` / Logic `2` / Constraints `3` / Publish `2`
- Finding: [Moderate] [Ambiguity risk] The current wording barred claims of reduced obligations while exerting undisclosed or material external impact, but it did not yet directly name fragmentation, relabeling, or sandbox-style reframing as prohibited evasion pathways.
- Why it matters: readers may otherwise underread the anti-evasion rule as applying only to blunt misclassification rather than to common structural workarounds that achieve the same result.
- Smallest close: expand the clause so it bars lifecycle-obligation avoidance through misclassification, fragmentation, relabeling, or similar functional disguise.

## Cross-cutting conclusion

Article XV does not need expansion into a full systems manual. It needs a clearer constitutional surface so readers can see that lifecycle governance is continuous, that reversibility includes auditable restoration when rollback is incomplete, and that environment or classification labels cannot be used to evade stronger duties required by full functional effects.

Most important close points:
- make the chapeau show full-lifecycle continuity more directly;
- make `Article XV-A` show that environment separation must hold in practice, not just nominally;
- make `Article XV-B` surface auditable restoration and continuity criteria;
- make `Article XV-C` identify fragmentation and relabeling as anti-evasion failures.

## Suggested next-step edits

If this audit is used as a drafting basis, the smallest likely edits are:

1. tighten the chapeau so continuous lifecycle stewardship, including restoration, is visible up front;
2. add practical promotion and cross-environment integrity language to `Article XV-A`;
3. add restoration-criteria and continuity language to `Article XV-B`;
4. expand `Article XV-C` so anti-evasion coverage clearly includes fragmentation and relabeling.
