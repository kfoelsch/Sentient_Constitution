# Standard best-practices check for constitutional gap and performance analysis

Status: implementation review artifact (non-authoritative).  
Date: 2026-04-12.  
Scope: full constitutional corpus, with primary focus on the Sentient Constitution numbered `core_*.md` files (for example `core_00-01_principles.md`, `subcore_03.010_definition_structure.md`, `core_03.000_definitions_home.md`, `core_12.000_forum.md`, `core_06.0*_rights_part_*.md`, `core_13.000_governance.md`, `core_14.000_non_regression.md`, `core_17.000_incorporation.md` — see [README.md](../README.md)), `corpus_institutions.md`, `corpus_systems.md`, and `corpus_joint_structure.md` (implementation layer and joint integration rules).

## Purpose

This document defines a repeatable "best practices check" for reviewing where the constitution stands against widely used real-world governance, integrity, assurance, and AI-risk benchmarks.

Use it for:
- quarterly or edition-cut gap analysis;
- pre-adoption assurance review;
- post-change regression review when major governance text changes;
- performance analysis, not only design analysis.

This is a benchmark-and-gap tool. It does **not** change constitutional meaning.

## Review method

For each benchmark row below:

1. review the named external source and the specific section(s) listed;
2. inspect the mapped constitutional sections;
3. assign scores on four axes;
4. record gaps, evidence, and follow-up actions.

## Scoring axes

Use a `0-3` scale for each axis.

- `Design coverage`
  - `0` absent
  - `1` implied only
  - `2` explicit but incomplete
  - `3` explicit and well-structured
- `Operationalization`
  - `0` no usable mechanism
  - `1` mechanism exists but is vague
  - `2` mechanism is workable
  - `3` mechanism is specific, assigned, and testable
- `Evidence`
  - `0` no evidence path
  - `1` evidence path implied
  - `2` evidence path defined
  - `3` evidence path defined and already exercised
- `Performance`
  - `0` no performance standard or drill
  - `1` standard exists without measurable trigger
  - `2` measurable trigger or cadence exists
  - `3` measurable trigger exists and has evidence from drills, audits, or review artifacts

Recommended outputs per row:
- `Gap`
- `Current anchor`
- `Needed drafting close`
- `Needed evidence close`
- `Priority`

## Standard source set

Run every standard review against these sources in this order.

### Level 1: Core public benchmarks

1. **OECD (2023), G20/OECD Principles of Corporate Governance 2023**
   - Review sections:
   - `About the Principles`
   - `I. Ensuring the basis for an effective corporate governance framework`
   - `IV. Disclosure and transparency`
   - `V. The responsibilities of the board`
   - `VI. Sustainability and resilience`
   - Use `II` by analogy when reviewing participation, equal treatment, and contestability.
   - Notes:
   - Treat this as an analogy benchmark, not a corporate-charter template.

2. **FRC (2024), UK Corporate Governance Code 2024**
   - Review sections:
   - `Section 1 – Board leadership and company purpose`
   - `Section 2 – Division of responsibilities`
   - `Section 3 – Composition, succession and evaluation`
   - `Section 4 – Audit, risk and internal control`
   - `Provision 29`
   - Also review FRC guidance:
   - `Audit, Risk and Internal Control`
   - `Maintaining the Effectiveness of the Risk Management and Internal Control Framework`
   - `Reporting in the Annual Report`

3. **The IIA (2020; public access, updated glossary note 2024), The IIA’s Three Lines Model**
   - Review sections:
   - `Principle 1: Governance`
   - `Principle 2: Governing body roles`
   - `Principle 3: Management and first and second line roles`
   - `Principle 4: Third line roles`
   - `Principle 5: Third line independence`
   - `Principle 6: Creating and protecting value`
   - `Key roles in the Three Lines Model`
   - `Relationships among core roles`
   - `Applying the model`

4. **OECD (2020), OECD Public Integrity Handbook**
   - Review sections:
   - `1. Commitment`
   - `2. Responsibilities`
   - `3. Strategy`
   - `4. Standards`
   - `9. Openness`
   - `10. Risk management`
   - `11. Enforcement`
   - `12. Oversight`
   - `13. Participation`

5. **OHCHR (2011), Guiding Principles on Business and Human Rights**
   - Review sections:
   - `General principles`
   - `I. The State duty to protect human rights`
   - `II. The corporate responsibility to respect human rights`
   - `III. Access to remedy`
   - Use especially when reviewing remedy pathways, abuse prevention, vulnerable sentients, and non-state operators.

6. **NIST (2023), AI Risk Management Framework 1.0**
   - Review sections:
   - `AI risks and trustworthiness characteristics`
   - `Govern`
   - `Map`
   - `Measure`
   - `Manage`
   - Use when reviewing AI/system governance, testing, monitoring, explainability, and incident response.

7. **NIST (2024), AI RMF: Generative AI Profile**
   - Review sections:
   - executive summary
   - lifecycle/application guidance relevant to:
   - misuse and abuse resistance
   - human-AI interaction and disclosure
   - content provenance / synthetic media risks
   - testing and monitoring
   - Use when reviewing constitution sections that govern synthetic content, publication integrity, and high-autonomy systems.

### Level 2: Controlled or licensed standards

Use these when a licensed copy is available or when a formal attestation-oriented crosswalk is needed.

8. **ISO 37000:2021, Governance of organizations — Guidance**
   - Review the published principle structure at minimum:
   - purpose
   - value generation
   - strategy
   - oversight
   - accountability
   - stakeholder engagement
   - leadership
   - data and decisions
   - risk governance
   - social responsibility
   - Notes:
   - exact clause wording should be confirmed against a licensed copy.

9. **ISO/IEC 42001:2023, AI management systems**
   - Review clauses:
   - `4 Context of the organization`
   - `5 Leadership`
   - `6 Planning`
   - `7 Support`
   - `8 Operation`
   - `9 Performance evaluation`
   - `10 Improvement`
   - Notes:
   - best used when mapping to an auditable management-system shape.

10. **ISO 37001:2025 and/or ISO 37301:2021**
   - Review only if the review scope includes anti-bribery, anti-corruption, or formal compliance-program maturity.
   - Suggested focus:
   - policy and leadership
   - due diligence
   - financial and non-financial controls
   - reporting and investigation
   - corrective action and improvement

## Standard review matrix

Use the matrix below as the default working checklist.

| Review domain | External source and exact section(s) | What to test in the constitution | Primary internal anchors |
|---|---|---|---|
| Legitimacy, purpose, and constitutional authority | OECD 2023 `About the Principles`, `I`; FRC 2024 `Section 1`; ISO 37000 `purpose`, `strategy` | Is governing authority clearly justified, bounded, and tied to stated purpose and stakeholder-facing legitimacy? | the Sentient Constitution `core_*.md` files Chapter Two sections 1-9; Chapter Twenty sections 1-5; Chapter Twenty-Seven sections 3-5; `core_14.000_non_regression.md` Chapters Twenty-One-Twenty-Three |
| Rights, equitable treatment, and protected sentients | OECD 2023 `II`; OHCHR 2011 `General principles`, `I`, `II`, `III` | Are Rights Floors explicit, non-discretionary, and connected to remedy? Are vulnerable sentients and abuse pathways covered? | the Sentient Constitution `core_*.md` files Articles V-XII, XVIII, XXIII; `subcore_03.010_definition_structure.md` / `core_03.000_definitions_home.md` Chapter Three, including its subcore |
| Separation of powers, role clarity, and anti-self-judging | FRC 2024 `Section 2`; IIA 2020 `Principles 1-5`, `Key roles`, `Relationships among core roles`; OECD Public Integrity `2. Responsibilities`, `12. Oversight` | Are governing, operating, review, and independent assurance roles separated clearly enough to resist capture and self-judging? | the Sentient Constitution `core_*.md` files Chapter Fifteen; Article XXIII; Chapter Twenty section 6; `corpus_institutions.md` CI-6.205, CI-13.205, CI-6.210, CI-24.210, CI-6.215, and CI-4.205 |
| Composition, competency, succession, and removal | FRC 2024 `Section 3`; IIA 2020 `Applying the model`; OECD Public Integrity `6. Leadership`, `8. Capacity` | Are competency, rotation, succession, removal, and independence requirements explicit and proportional to risk? | the Sentient Constitution `core_*.md` files Article XXIV-B through XXII-D; Chapter Twenty section 6; `corpus_institutions.md` CI-13.205, CI-4.275; `corpus_forum.md` CF-12.440 |
| Conflict integrity, anti-corruption, and anti-capture | OECD Public Integrity `4. Standards`, `10. Risk management`, `11. Enforcement`; ISO 37001/37301 if in scope | Are conflicts, corruption, concealed interests, and capture patterns prohibited, monitored, and sanctionable? | the Sentient Constitution `core_*.md` files Chapter Two section 7.2; Articles XI-E, XIII-A, XXII; Chapter Fifteen; `corpus_institutions.md` CI-6.210, CI-4.215, CI-10.210 |
| Risk governance and internal controls | FRC 2024 `Section 4`, `Provision 29`; IIA 2020 `Principles 1-6`; OECD Public Integrity `10. Risk management`; NIST AI RMF `Govern`, `Map` | Does the corpus require an explicit risk/control framework, ownership, review cadence, and material-control failure disclosure path? | the Sentient Constitution `core_*.md` files Chapter Two section 7; Articles XII-XVI, XX-XXI; `corpus_institutions.md` CI-6.205, CI-6.215; `corpus_systems.md` CS-4.345, CS-4.305 and CS-4.310, CS-4.305 and CS-4.310 |
| Transparency, disclosure, and public intelligibility | OECD 2023 `IV`; OECD Public Integrity `9. Openness`, `13. Participation`; NIST AI RMF `Govern`, `Measure`; OHCHR `II`, `III` | Are material decisions, system status, explanations, and disclosure obligations timely, contestable, and accessible? | the Sentient Constitution `core_*.md` files Articles VIII, XIV, XV, XX, XXII-C, XXIII-E; `subcore_03.030_burden_traceability_verification.md` Subcore 3-C; `corpus_institutions.md` CI-18.210, CI-0.215; **CJS-3.110 §3 and CJS-3.115 §3** (*auditability and reconstructability terms*), **CJS-3.110 §4** (*transparency levels and audit-access terms*), **CJS-3.110 §5** (*independent verification and claim-integrity terms*), **CJS-3.120 §9** (*salience integrity and attention-allocation terms*), **CJS-3.120 §10** (*disclosure sufficiency and observability terms*) |
| Independent assurance and verification | IIA 2020 `Principles 4-5`, `Between internal audit and the governing body`, `Oversight and assurance`; OECD Public Integrity `12. Oversight`; FRC 2024 `Section 4` | Are audit, independent review, external assurance triggers, and evidence custody specified enough to verify high-impact claims? | the Sentient Constitution `core_*.md` files Articles XV and XXII; Chapter Fifteen; `subcore_03.030_burden_traceability_verification.md` Subcore 3-C; `corpus_institutions.md` CI-6.215, CI-4.205; `corpus_forum.md` CF-12.430, CF-12.435, CF-12.440; `doc_architecture.md` sections 15-17 |
| AI and system lifecycle governance | NIST AI RMF `Govern`, `Map`, `Measure`, `Manage`; ISO/IEC 42001 clauses `4-10`; NIST GenAI Profile 2024 | Does the corpus cover classification, testing, deployment control, monitoring, rollback, synthetic-content risk, and adaptive-system oversight? | the Sentient Constitution `core_*.md` files Articles XII-XVII, XX-XXI; `corpus_systems.md` CS-4.345, CS-4.315, CS-4.305, CS-4.310, CS-8.305, CS-8.310, CS-13.305, CS-4.355, CS-4.330 |
| Remedy, redress, contestability, and restorative closure | OHCHR 2011 `III. Access to remedy`; OECD 2023 `II`; OECD Public Integrity `11. Enforcement`, `13. Participation` | Are challenge rights real, reviewable, timely, and connected to restoration rather than only punishment? | the Sentient Constitution `core_*.md` files Articles XII-B, XV, XVIII-B, XXIII, XXV; Chapter Eleven; `corpus_institutions.md` CI-24.210, CI-10.210; `corpus_systems.md` CS-4.320 |
| Continuity, resilience, transition, and emergency discipline | OECD 2023 `VI`; FRC 2024 `Section 4`; NIST AI RMF `Manage`; ISO 37000 `risk governance`, `social responsibility` | Are emergency powers bounded, continuity preserved, and restoration / re-baselining governed by time limits and review triggers? | Sentient Constitution **Articles XXIII–XXVII** (transition in **Article XXVII**); Chapters **Ten through Twelve** in `core_14.000_non_regression.md`; `corpus_institutions.md` **CI-4.275** / **CI-4.275 §2**; `corpus_systems.md` CS-4.350, CS-4.355, CS-4.330, CS-4.325 |
| Amendment validity, non-regression, and controlled change | OECD 2023 `I`, `V`, `VI`; FRC 2024 `Section 1`, `Section 4`; ISO/IEC 42001 `9-10` by analogy | Does the constitution itself require traceable, reviewable, non-regressive change control with invalid-change handling? | `core_14.000_non_regression.md` Chapters Seventeen-Twenty-Three; the Sentient Constitution `core_*.md` files Article XXVI, Article XXVII, Chapter Twenty-Seven |

## Mandatory review questions per row

Record explicit answers to these questions:

1. Is the norm explicit, or only inferable?
2. Is there a named decision-maker or role owner?
3. Is there a required evidence path?
4. Is there an independent review path?
5. Is there a measurable cadence, trigger, threshold, or time bound?
6. Is there an anti-evasion clause or equivalent?
7. Is there a failure-handling path?
8. Is there a restoration or remedy path?
9. Is there a publication or disclosure obligation?
10. Is there an already-existing evidence artifact in `evidence/` or `implementation/`?

## Performance analysis layer

Do not stop at "the text exists." Score actual operational maturity.

### Minimum evidence set

For any row to receive `Performance = 3`, the reviewer should be able to point to at least one of:
- a dated drill artifact in `evidence/`;
- a regression scenario tied to the control;
- a published audit or review artifact;
- a standing registry, disclosure schema, or decision log;
- a completed remediation record after a detected failure.

### Suggested performance indicators

- review cadence is stated and met;
- evidence artifacts exist for the current edition;
- escalation path was exercised at least once in a tabletop or drill;
- failures produce tracked remediation, not only narration;
- disclosure fields are standardized enough to compare over time;
- role independence can be demonstrated from records, not only prose.

## Default output template

Use this row format for the actual review memo or spreadsheet.

| Domain | External source section | Internal anchor | Design | Oper. | Evidence | Perf. | Current state | Gap | Proposed close | Priority |
|---|---|---|---:|---:|---:|---:|---|---|---|---|

## Current repository fit

This repository already contains useful precursors:

- `doc_architecture.md` section `15. External framework crosswalk`
- dated drill artifacts under `evidence/2026-q2/drills/`
- `implementation/AUTOMATED_REFERENCE_CHECKING.md`

Those artifacts are helpful inputs, but they do **not** yet form a single standard review method. This file is the standard method.

## Recommended cadence

- Run a light pass on every material corpus edition cut.
- Run a full pass quarterly.
- Run a focused pass after any major changes to:
- Chapter Four
- Articles XI-XVI
- Articles XXII-XXV
- Chapters Seventeen-Twenty-Three
- `corpus_institutions.md` institutional implementation corpus
- `corpus_systems.md` CS-4.345, CS-4.305 and CS-4.310, CS-4.355, CS-4.330

## Source links

- OECD 2023, G20/OECD Principles of Corporate Governance 2023: <https://www.oecd.org/en/publications/g20-oecd-principles-of-corporate-governance-2023_ed750b30-en/full-report.html>
- FRC, UK Corporate Governance Code 2024: <https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/uk-corporate-governance-code/>
- FRC guidance, Corporate Governance Code Guidance: <https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/corporate-governance-code-guidance/>
- The IIA, The IIA’s Three Lines Model: <https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/>
- OECD Public Integrity Handbook: <https://www.oecd.org/en/publications/oecd-public-integrity-handbook_ac8ed8e8-en/full-report.html>
- OHCHR, Guiding Principles on Business and Human Rights: <https://www.ohchr.org/sites/default/files/Documents/Publications/GuidingPrinciplesBusinessHR_EN.pdf>
- NIST AI RMF 1.0 overview: <https://www.nist.gov/itl/ai-risk-management-framework>
- NIST AI RMF trustworthiness / functions resource center: <https://airc.nist.gov/airmf-resources/>
- NIST AI RMF Generative AI Profile: <https://doi.org/10.6028/NIST.AI.600-1>
- ISO 37000 overview: <https://www.iso.org/standard/65036.html>
- ISO/IEC 42001 overview: <https://www.iso.org/standard/81230.html>
- ISO 37001 overview: <https://www.iso.org/standard/85816.html>
