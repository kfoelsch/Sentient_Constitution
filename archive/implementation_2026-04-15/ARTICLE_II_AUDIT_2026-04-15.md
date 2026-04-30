# Article II audit

Status: implementation review artifact (non-authoritative).  
Date: 2026-04-15.  
Scope: pilot application of the Article-Principle-Definition audit rubric to `Article II: Material Stewardship and Durable-Use Integrity`.

## Overall assessment

Article II is structurally solid and already reads like a compact constitutional floor rather than a policy manual. Its subsections generally preserve the right relationship between Chapter One principles, Chapter Five definitions, and owner-layer implementation in `corpus_systems.md` and `corpus_institutions.md`.

The main issues are not doctrinal reversals. They are:
- one subsection whose trace block omits a definition the operative sentence already relies on;
- one subsection whose subscription-conversion rule is substantively correct but under-names the Chapter Five agency/manipulation/reliance concepts doing the work;
- one subsection that uses a non-canonical label where Chapter Five uses a different definition heading.

Overall judgment: `publishable after targeted edits`.

## Worksheet

| Article unit | Operative claim | Principle anchor | Definition anchors | Ch. 2-4 mechanics | Principle | Definition | Logic | Constraints | Publish | Severity | Finding type | Drafting close |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| Article II (chapeau) | Material stewardship is a constitutional floor for durable and network-dependent products read with Article I and Chapter Five | Chapter One `6.1`, `7.1` | Ecological Footprint; Intergenerational Responsibility; Materiality Determination | same-scope application; non-narrowing by owner layers; traceability to incorporated detail | 3 | 3 | 3 | 3 | 3 | None | None | No drafting close required |
| Article II-A | Durable products must not be represented or supported in ways that drive avoidable premature discard or misrepresented longevity | Chapter One `3.2`, `6.1`, `7.1` | Ecological Footprint; Intergenerational Responsibility; Materiality Determination | disclosure integrity; auditable records; materiality scaling | 3 | 3 | 3 | 3 | 3 | None | None | No drafting close required |
| Article II-B | Covered products must preserve practicable repair and maintenance access unless justified under necessity and proportionality | Chapter One `3.1`, `3.2`, `6.1` | Necessity; Proportionality; Dependency | burden of justification; non-deceptive disclosure; class-scaled implementation | 3 | 3 | 3 | 3 | 3 | None | None | No drafting close required |
| Article II-C | Designed obsolescence and remote-update replacement pressure are prohibited absent documented necessity and proportionality | Chapter One `3.1`, `6.1`, `7.2` | Incentive Alignment; Foreseeability; Necessity; Proportionality | foreseeability burden; anti-capture; alternatives analysis | 3 | 2 | 3 | 3 | 2 | Minor | Ambiguity risk | Add `Proportionality` to the trace block because the operative exception already depends on it |
| Article II-D | Sold capabilities cannot be silently or coercively converted into subscription access and dependency must be disclosed up front | Chapter One `3.2`, `5`, `7.2` | Consent; Truth; Dependency; Meaningful Agency; Coercion and Manipulation; Trust Degradation and Misleading Reliance | informed-agreement validity; reliance integrity; anti-lock-in/anti-manipulation evaluation | 3 | 2 | 2 | 2 | 2 | Moderate | Underreach | Name the Chapter Five agency/manipulation/reliance anchors in trace and operative text |
| Article II-E | Network-dependent products require pre-commitment dependency disclosure and continuity duties that survive operator distress where feasible | Chapter One `3.1`, `6.1`, `7.1` | Dependency; Intergenerational Responsibility; Materiality Determination; Necessity; Negligence | dependency evaluation; continuity planning; anti-externalization; documented infeasibility review | 3 | 2 | 2 | 2 | 2 | Moderate | Definition substitution | Replace local `Neglect` label with canonical Chapter Five `Negligence` and expose the `Necessity` anchor in trace |

## Findings

### Article II-C

- Operative claim: deliberate or update-mediated premature replacement pressure is prohibited unless justified under documented constitutional constraints.
- Principle anchor: Chapter One `3.1 Safety`, `6.1 Core Tradeoff Principles`, and `7.2 Incentive Alignment and System Capture`.
- Definition anchors: `Incentive Alignment`, `Foreseeability Diligence`, `Necessity`, and functionally `Proportionality`.
- Mechanics: foreseeability analysis and justification burden are present in substance.
- Scores: Principle `3` / Definition `2` / Logic `3` / Constraints `3` / Publish `2`
- Finding: [Minor] [Ambiguity risk] The subsection's exception expressly depends on `Necessity` and `Proportionality`, but the trace block names only `Necessity`.
- Why it matters: the text is still defensible, but publication traceability is slightly weaker because one of the two controlling conflict filters is omitted from the subsection's own anchor list.
- Smallest close: add `Proportionality` to the trace block.

### Article II-D

- Operative claim: operators may not convert sold functionality into recurring-rent access without valid new agreement and truthful up-front dependency disclosure.
- Principle anchor: Chapter One `3.2 Truth`, `5. Governance Principle: Freedom`, and `7.2 Incentive Alignment and System Capture`.
- Definition anchors: `Consent (Constitutional)`, `Truth (Constitutional Constraint)`, `Dependency`, and functionally `Meaningful Agency`, `Coercion and Manipulation`, and `Trust Degradation and Misleading Reliance`.
- Mechanics: the subsection already invokes explicit informed agreement, induced reliance, and dependency disclosure, so the right mechanics are mostly present.
- Scores: Principle `3` / Definition `2` / Logic `2` / Constraints `2` / Publish `2`
- Finding: [Moderate] [Underreach] The subsection relies on agency, manipulation, and misleading-reliance logic without naming those Chapter Five anchors in its trace block, and its first sentence can be read as a consent-only test when Chapter Five requires a more substantive agency reading.
- Why it matters: a careful reader can recover the intended meaning, but a narrower reading could treat subscription conversion as valid after formal click-through acceptance even where dependency-forced agreement or misleading reliance defeats genuine agency.
- Smallest close: add `Meaningful Agency`, `Coercion and Manipulation`, and `Trust Degradation and Misleading Reliance` to the trace block and make the operative sentence expressly agency-aware.

### Article II-E

- Operative claim: operator-controlled service dependency must be disclosed and continuity obligations persist through shutdown, restructuring, and successor transfer within feasible constitutional limits.
- Principle anchor: Chapter One `3.1 Safety`, `6.1 Core Tradeoff Principles`, and `7.1 Required Evaluation Factors`.
- Definition anchors: `Dependency`, `Intergenerational Responsibility`, `Materiality Determination`, and functionally `Necessity` plus the Chapter Five negligence/neglect concept.
- Mechanics: continuity, migration, and infeasibility review are present, but one anchor is mislabeled.
- Scores: Principle `3` / Definition `2` / Logic `2` / Constraints `2` / Publish `2`
- Finding: [Moderate] [Definition substitution] The operative text says `Conduct evaluated under Chapter Five (Neglect)` even though the canonical definition heading is `Negligence`, with neglect described inside that definition.
- Why it matters: the current wording is understandable, but it introduces a non-canonical label at the very point where the subsection tries to anchor continuity failures back to Chapter Five. That weakens definitional precision and makes the trace slightly harder to audit.
- Smallest close: replace `Neglect` with `Negligence`, optionally preserving `neglect-mediated` language in the sentence, and add `Necessity` to the trace block because the final sentence already depends on it.

## Cross-cutting conclusion

Article II does not show major principle-definition misalignment. The pilot suggests the article is already publication-close, with the main value coming from a few trace-and-terminology corrections rather than substantive rewriting.

Most important close points:
- expose `Proportionality` in `Article II-C`;
- restore the Chapter Five agency/manipulation/reliance anchors in `Article II-D`;
- replace the non-canonical `Neglect` label and expose `Necessity` in `Article II-E`.

## Suggested next-step edits

If this audit is used as a drafting basis, the smallest likely edits are:

1. revise the `Article II-C` trace block to include `Proportionality`;
2. revise `Article II-D` trace and operative language so subscription conversion clearly remains bounded by `Meaningful Agency`, coercion/manipulation limits, and misleading-reliance discipline;
3. revise `Article II-E` to use canonical `Negligence` terminology and expose the `Necessity` anchor already doing work in the subsection.
