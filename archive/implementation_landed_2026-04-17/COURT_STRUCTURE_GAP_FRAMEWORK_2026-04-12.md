# Court structure gap framework

Status: implementation review artifact (non-authoritative).  
Date: 2026-04-12.  
Scope: constitutional court-family design, routing, review, integrity protections, specialist chambers, and court-adjacent investigative / evidentiary support.

## Purpose

This document defines a dedicated framework for gap analysis on the constitution's court structure.

It is narrower than the general best-practices check. Its job is to answer questions like:
- are the court families well differentiated;
- do routing and escalation rules avoid self-judging and capture;
- are recusal, panel formation, transfer, and backup-forum rules specific enough;
- do specialist technical courts stay accountable;
- can the court system actually perform under stress, complexity, and conflict.

## Primary internal anchors

Start with these constitutional homes:

- `core_constitution.md` Chapter Eight
- `core_constitution.md` Article XII-B
- `core_constitution.md` Article XIV
- `core_constitution.md` Article XXI
- `core_constitution.md` Article XXII
- `corpus_institutions.md` CI-6 through CI-8
- `corpus_institutions.md` CI-7A and CI-7A.1
- `corpus_institutions.md` CI-7B
- `core_constitution.md` Chapter Six and Chapter Seven where classification, due process, and review intensity affect courts

## Standard source set for court review

Use these sources in this order.

### Tier 1: Core judicial structure benchmarks

1. **UN Basic Principles on the Independence of the Judiciary (1985)**
   - Review sections / principle ranges:
   - `1-7` independence of the judiciary
   - `8-9` expression and association
   - `10-15` qualifications, selection, and training
   - `16-20` conditions of service and tenure
   - `17-20` assignment and security of tenure
   - `21-22` professional secrecy and immunity
   - `17-20` and `26-29` discipline, suspension, and removal

2. **Bangalore Principles of Judicial Conduct**
   - Review values and application sections:
   - `Value 1: Independence`
   - `Value 2: Impartiality`
   - `Value 3: Integrity`
   - `Value 4: Propriety`
   - `Value 5: Equality`
   - `Value 6: Competence and Diligence`
   - Especially application provisions on disqualification / recusal, bias appearance, diligence, and public confidence.

3. **Venice Commission, Updated Rule of Law Checklist (2025)**
   - Review sections:
   - `E. Access to justice`
   - `1. Independence and impartiality`
   - `a. Independence of the judiciary`
   - `b. Independence of individual judges`
   - `c. Impartiality of the judiciary`
   - `d. Constitutional justice`
   - `2. Fair trial`
   - `3. Review of constitutionality`
   - Use this as the most court-structure-like checklist source.

4. **CEPEJ quality / efficiency tools**
   - Review:
   - `Checklist for promoting the quality of justice and the courts`
   - `Measuring the quality of justice`
   - `Revised SATURN guidelines for judicial time management`
   - Use these mainly for performance, timeliness, accessibility, backlog, and user-facing quality.

### Tier 2: Court-adjacent institutional benchmarks

5. **OHCHR / UN Guidelines on the Role of Prosecutors**
   - Review principles:
   - `10-20`
   - Especially impartiality, expeditious handling, exculpatory disclosure, and fairness to suspects and victims.
   - Use where court design depends on prosecutorial or investigative interface.

6. **OHCHR / UN Guiding Principles on Business and Human Rights**
   - Review:
   - `III. Access to remedy`
   - Use when testing whether remedy pathways are practical, reviewable, and accessible to affected persons rather than merely formal.

## Court-specific scoring axes

Use `0-3` on each axis.

- `Structural clarity`
  - `0` confused or missing
  - `1` broad idea only
  - `2` explicit but with unresolved boundary problems
  - `3` explicit, bounded, and conflict-aware
- `Independence protection`
  - `0` little or no anti-capture protection
  - `1` principle stated without mechanism
  - `2` mechanism exists but leaves major failure paths
  - `3` mechanism exists with recusal, transfer, backup, and review safeguards
- `Operational readiness`
  - `0` structure not practically usable
  - `1` usable only with large adopting-law assumptions
  - `2` mostly usable
  - `3` specific enough for implementation and audit
- `Performance / observability`
  - `0` no measurable performance path
  - `1` review idea only
  - `2` some measurable requirements or evidence artifacts
  - `3` measurable requirements plus demonstrated drills, logs, or review outputs

## Standard court review matrix

| Court domain | External source and exact section(s) | What to test | Primary internal anchors |
|---|---|---|---|
| Court-family architecture | UN Basic Principles `1-7`; Venice Checklist 2025 `E.1`, `E.3` | Are court families distinct enough to preserve competence and independence without fragmentation into unaccountable parallel bodies? | `core_constitution.md` Chapter Eight sections 1-3 |
| Jurisdiction allocation and dominant-purpose routing | Venice Checklist 2025 `E.1`, `E.2`, `E.3`; Bangalore `Value 1`, `Value 2` | Are jurisdiction rules intelligible, reviewable, and resistant to forum manipulation? | `core_constitution.md` Chapter Eight sections 3-5 |
| Anti-self-judging protections | Venice Checklist 2025 `E.1.a-c`; Bangalore `Value 1`, `Value 2`; UN Basic Principles `2`, `4`, `17-20` by analogy | Can no court family remain sole merits judge of its own capture, bias, recusal failure, or concealment claims? | `core_constitution.md` Chapter Eight sections 4-5; `corpus_institutions.md` CI-7.3, CI-8 |
| Transfer, certification, consolidation, and representative treatment | Venice Checklist 2025 `E.2`; CEPEJ quality tools on process quality | Are transfer and certification rules specific enough to avoid duplicate merits adjudication, inconsistent rulings, and remedy fragmentation? | `core_constitution.md` Chapter Eight sections 4-5; `corpus_institutions.md` CI-6 |
| Panel formation, recusal, and backup-forum activation | Bangalore `Value 2`, `Value 4`; UN Basic Principles `17-20`, `26-29`; Venice Checklist 2025 `E.1.a-c` | Are panel independence, recusal triggers, inability-to-constitute rules, and backup activation defined enough to be lawful in practice? | `core_constitution.md` Chapter Eight sections 4-5; Article XXI-B through XXI-D; `corpus_institutions.md` CI-4, CI-5, CI-8 |
| Due process, contestability, and secondary review | Venice Checklist 2025 `E.2`; UN Basic Principles `1`, `6`; OHCHR BHR `III. Access to remedy`; CEPEJ quality tools | Do litigants have understandable notice, rationale, records, review, and access pathways proportionate to impact? | `corpus_institutions.md` CI-6; `core_constitution.md` Article XI-D, Article XII-B, Article XXII |
| Constitutional court boundary discipline | Venice Checklist 2025 `E.1.d`, `E.3`; UN Basic Principles `1-4` | Is the constitutional family bounded to structural / validity questions instead of becoming a general super-court? | `core_constitution.md` Chapter Eight sections 3-5; Article XXI; `core_amendment.md` Chapters Eleven-Thirteen |
| Integrity court design | Bangalore `Value 1-4`; Venice Checklist 2025 `E.1`; UN Basic Principles `26-29` | Are integrity courts independent enough to hear capture, conflict, concealment, and process-abuse claims without collapsing into the same structures they police? | `core_constitution.md` Chapter Eight; Chapter Seven; `corpus_institutions.md` CI-5, CI-7.3, CI-8 |
| Institutional court design | Venice Checklist 2025 `E.1`, `E.2`; CEPEJ process / quality tools | Can institutional courts hear mandate, procedural, and governance disputes without forcing all such claims into sentient or constitutional routes? | `core_constitution.md` Chapter Eight sections 2-5; `corpus_institutions.md` CI-2 through CI-8 |
| Sentient court asymmetry protections | OHCHR BHR `III`; Venice Checklist 2025 `E.2`; Bangalore `Value 5` | Where dependency or monopoly power materially disadvantages a sentient party, do routing rules preserve a non-captured institutional or integrity forum? | `core_constitution.md` Chapter Eight section 3; Article V; Article XII-B |
| Court forensic and analytical support | CEPEJ quality tools on experts / process quality; UN Basic Principles `6`; Bangalore `Value 6` | Is there independent, contestable, non-merits forensic support for technical opacity, causation, and evidence reconstruction? | `corpus_institutions.md` CI-7A; `core_constitution.md` Chapter Eight section 3; Article XIV |
| Independent investigative service | UN Prosecutors Guidelines `10-20`; Venice Checklist 2025 `E.1`, `E.2`; Bangalore `Value 3-4` | Are investigations independent enough when courts, police, prosecutors, or aligned actors are implicated? | `corpus_institutions.md` CI-7A.1; CI-8 |
| Technical courts / specialist chambers | Bangalore `Value 6`; Venice Checklist 2025 `E.1.d`; CEPEJ quality tools; court-expert guidance by analogy | Do specialist chambers add expertise without becoming parallel unaccountable judiciaries or ideological bottlenecks? | `core_constitution.md` Chapter Eight section 3; `corpus_institutions.md` CI-7B, CI-15B |
| Evidence stewardship and restricted evidence handling | UN Basic Principles `6`; Venice Checklist 2025 `E.2`; CEPEJ quality tools | Are chain of custody, method logs, restricted-access review, and contestability strong enough for reliable adjudication? | `core_definitions.md` Chapter Four; `core_constitution.md` Article XIV; `corpus_institutions.md` CI-7, CI-7A |
| Timeliness, backlog, and court usability | CEPEJ `Measuring the quality of justice`; `SATURN guidelines`; Venice Checklist 2025 `E.2`; Bangalore `Value 6` | Are time bounds, backlog controls, accessibility, and user-facing process quality explicit enough to make justice practical? | `corpus_institutions.md` CI-6, CI-7.3, CI-12; `core_constitution.md` Article XII-B, Article XXII |
| Emergency, incapacity, and continuity of adjudication | UN Basic Principles `1-7`; Venice Checklist 2025 `E.1`, `E.2`; CEPEJ continuity / quality materials | Can courts remain lawful and reviewable under emergency, deadlock, incapacity, or capture conditions? | `core_constitution.md` Article XXII, Article XXIV; `corpus_institutions.md` CI-8, CI-14; `corpus_systems.md` Protocol D, Protocol R |

## Court-specific mandatory review questions

Answer these for each row:

1. Is the relevant court family or function expressly named?
2. Is its jurisdiction bounded by a clear decision rule?
3. Is there a rule for mixed-stakes cases?
4. Is there a rule for transfer, certification, or consolidation?
5. Is there a rule for recusal failure, panel failure, or inability to form an independent bench?
6. Is backup routing stated, or only implied?
7. Is there a review path that does not require self-judging?
8. Are specialist chambers constrained from becoming parallel sovereign courts?
9. Are evidence support and investigation independent from merits determination?
10. Is there a measurable timeliness or backlog expectation?
11. Is there a publication or recordkeeping requirement for routing, transfer, recusal, or panel formation decisions?
12. Is there an evidence artifact, drill, or procedure map proving the rule works in practice?

## Common court-structure gap categories

Use these tags when recording findings.

- `boundary ambiguity`
- `forum-shopping risk`
- `self-judging risk`
- `panel-formation gap`
- `recusal gap`
- `backup-routing gap`
- `specialist-court overreach risk`
- `investigative dependence`
- `forensic-support gap`
- `timeliness / backlog gap`
- `recordkeeping / publication gap`
- `continuity / emergency adjudication gap`

## Performance analysis for courts

Do not score only on text design. Courts need operational proof.

### Minimum performance evidence

For `Performance / observability = 3`, point to at least one of:
- a tabletop or drill involving routing, transfer, or emergency adjudication;
- a published procedure map for due process and review;
- a contest-integrity monitoring output;
- a recusal / transfer / backup activation log format;
- a forensic or investigative scope-order template;
- a panel-formation or lawful-quorum checklist;
- a backlog or timeliness dashboard;
- an external assurance or independent review artifact.

### Suggested court performance indicators

- median time to initial routing decision;
- time to constitute a lawful independent panel;
- backlog aging by court family and case class;
- rate of recusal and rate of recusal challenge;
- number of cross-court anti-self-judging activations;
- percentage of high-impact decisions with independent review route actually available;
- time to produce reasoned transfer or certification record;
- forensic-support turnaround time in technical-evidence disputes;
- investigative independence exceptions and how often backup mechanisms were invoked.

## Suggested output template

| Court domain | External source section | Internal anchor | Structural | Independence | Operational | Performance | Current state | Gap | Proposed close | Priority |
|---|---|---|---:|---:|---:|---:|---|---|---|---|

## Immediate application to the current corpus

Based on the current text, the strongest existing material appears to be:
- court-family differentiation and dominant-purpose routing;
- anti-self-judging logic;
- technical-court boundary discipline;
- forensic support and investigative independence hooks;
- cross-institution escalation requirements.

The likeliest areas to pressure-test for gaps are:
- panel-formation mechanics;
- more explicit recusal abuse and backup activation procedure;
- timeliness / backlog / court-performance metrics;
- appeal-lane specificity inside and across court families;
- published record formats for transfer, certification, and independent-panel formation.

## Relationship to the general best-practices check

Use this file when the question is specifically about court design.

Use `implementation/BEST_PRACTICES_CHECK_STANDARD_2026-04-12.md` when the question is broader and includes institutional governance, systems governance, or whole-constitution benchmarking.

## Source links

- UN Basic Principles on the Independence of the Judiciary: <https://searchlibrary.ohchr.org/record/18419>
- Bangalore Principles of Judicial Conduct: <https://www.unodc.org/res/ji/import/international_standards/bangalore_principles/bangaloreprinciples.pdf>
- Venice Commission, Updated Rule of Law Checklist (2025): <https://www.coe.int/en/web/venice-commission/-/cdl-ad-2025-002-e>
- CEPEJ quality of justice tools hub: <https://www.coe.int/en/web/cepej/cepej-work/quality-of-justice>
- CEPEJ, Measuring the quality of justice: <https://edoc.coe.int/en/efficiency-of-justice/7500-measuring-the-quality-of-justice-guide.html>
- UN Guidelines on the Role of Prosecutors: <https://www.ohchr.org/sites/default/files/prosecutors.pdf>
- OHCHR, Guiding Principles on Business and Human Rights: <https://www.ohchr.org/sites/default/files/Documents/Publications/GuidingPrinciplesBusinessHR_EN.pdf>
