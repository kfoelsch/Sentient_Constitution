# Court structure gap matrix

Status: implementation review artifact (non-authoritative).  
Date: 2026-04-12.  
Method baseline: `implementation/COURT_STRUCTURE_GAP_FRAMEWORK_2026-04-12.md`.  
Scope baseline: current text in `core_constitution.md` Chapter Eight and `corpus_institutions.md` CI-4 through CI-8, CI-7A, CI-7A.1, and CI-7B.

## Summary assessment

The court structure is already **strong in constitutional design logic**. The corpus clearly differentiates court families, uses a dominant-purpose routing rule, bars self-judging through an explicit cross-court rule, and gives unusually good attention to technical courts, forensic support, and investigative independence.

The main gaps are **operational rather than conceptual**. The court structure still needs more explicit implementation-grade rules for:
- panel formation and lawful bench constitution;
- appeal-lane specificity within and across court families;
- recusal workflow and abuse handling;
- backup-forum activation records and thresholds;
- timeliness, backlog, and user-facing court performance metrics.

## Scoring scale

- `Structural`: clarity and boundedness of the court design
- `Independence`: protection against capture, self-judging, and conflicted control
- `Operational`: readiness for implementation without heavy unstated assumptions
- `Performance`: measurable observability and evidence that the structure works in practice

Scores use `0-3`.

## Matrix

| Court domain | Internal anchor | Structural | Independence | Operational | Performance | Current state | Gap | Proposed close | Priority |
|---|---|---:|---:|---:|---:|---|---|---|---|
| Court-family architecture | `core_constitution.md` Chapter Eight sections 1-3 | 3 | 3 | 2 | 1 | Four core families are expressly named and functionally distinguished; technical courts are constrained to chamber status rather than separate sovereign families. | Family architecture is clear, but adopter-facing translation into concrete court maps is still implicit. | Add an implementation annex or procedure map showing minimum family-to-tribunal translation and prohibited collapse patterns. | P1 |
| Jurisdiction allocation and dominant-purpose routing | Chapter Eight sections 3-5 | 3 | 3 | 2 | 1 | Dominant-purpose routing is one of the strongest parts of the design and is resilient against caption-based forum gaming. | Borderline mixed cases will still need more explicit examples and tie-break logic for operators. | Add a routing decision tree with worked examples and a short tie-break hierarchy for mixed-stakes cases. | P1 |
| Anti-self-judging protections | Chapter Eight sections 4-5; `corpus_institutions.md` CI-7.3, CI-8 | 3 | 3 | 2 | 1 | Cross-court anti-self-judging is explicit, with lead/backup family assignments and activation conditions. | Activation still depends on later operational detail for how independence failure is documented and who certifies panel impossibility. | Add a mandatory anti-self-judging activation record, lawful-panel checklist, and designated certifier role. | P0 |
| Transfer, certification, consolidation, and representative treatment | Chapter Eight sections 4-5; CI-6 | 3 | 2 | 2 | 1 | The text distinguishes transfer, certification, and scope expansion well and avoids conflating them. | No concrete procedural floor yet for who issues transfer orders, when, and with what publication format. | Add minimum transfer/certification order fields, time bounds, and a conflict-resolution rule for dueling forum claims. | P1 |
| Panel formation, recusal, and backup-forum activation | Chapter Eight sections 4-5; Article XXI-B to XXI-D; CI-4, CI-5, CI-8 | 2 | 3 | 1 | 0 | The corpus clearly requires independence, recusal, and backup routing. | It does not yet specify enough about lawful panel constitution, quorum, substitute selection, recusal challenge workflow, or when inability to form an independent bench is officially declared. | Add a panel-formation protocol with quorum rules, replacement hierarchy, recusal decision-maker, challenge path, and declaration-of-inability form. | P0 |
| Due process, contestability, and secondary review | CI-6; Article XI-D; Article XII-B; Article XXII | 3 | 2 | 2 | 1 | Notice, rationale, records, and independent review are clearly required. | The review lane is explicit, but appellate layering and timing expectations are still broad rather than court-specific. | Add court-facing minima for appeal deadlines, emergency review windows, publication latency, and high-impact secondary review triggers. | P1 |
| Constitutional court boundary discipline | Chapter Eight sections 2-5; Article XXI; `core_amendment.md` Chapters Eleven-Thirteen | 3 | 3 | 2 | 1 | Constitutional courts are bounded to structural validity, meaning, supremacy, and certified questions; this is unusually disciplined. | Need stronger guardrails to prevent constitutional-family creep through repeated certifications or emergency framing. | Add a rule that published certification records must state why non-constitutional families could not fully resolve the issue. | P2 |
| Integrity court design | Chapter Eight; Chapter Seven; CI-5, CI-7.3, CI-8 | 3 | 3 | 2 | 1 | Integrity courts are well differentiated and linked to capture, process abuse, disclosure, and conflict failures. | The relationship between integrity courts, internal integrity processes, and sanctions/removal pathways could still be easier to operationalize. | Add an integrity-lane workflow map covering internal process, independent merits forum, referral, and sanction/removal interfaces. | P1 |
| Institutional court design | Chapter Eight sections 2-5; CI-2 through CI-8 | 3 | 2 | 2 | 1 | Institutional courts are properly positioned for mandate, scope, classification, and supervised-duty disputes. | Need more explicit treatment of internal agency review versus court review and when exhaustion is or is not required. | Add an exhaustion / direct-access rule for institutional disputes, especially where urgency, capture risk, or rights-floor harm is present. | P1 |
| Sentient court asymmetry protections | Chapter Eight section 3; Article V; Article XII-B | 3 | 3 | 2 | 1 | The asymmetry rule is strong and prevents monopoly or dependency disputes from being trapped in a nominally private forum. | Needs more explicit examples so adopters do not under-route dependency-heavy cases back into sentient courts. | Add examples involving platform dependency, institutional monopoly inputs, and community-level coercion. | P2 |
| Court forensic and analytical support | CI-7A; Chapter Eight section 3; Article XIV | 3 | 3 | 2 | 1 | The corpus is ahead of most frameworks here: independent forensic support is explicit, bounded, and contestable. | Still lacks standard templates for scope orders, method logs, and challenge procedures. | Add standard scope-order, chain-of-custody, and expert-challenge templates. | P1 |
| Independent investigative service | CI-7A.1; CI-8 | 3 | 3 | 2 | 1 | Anti-self-investigation protections are strong, especially where courts, police, prosecutors, or investigators themselves are implicated. | The escalation trigger to external participation or co-assignment is conceptually strong but not yet reduced to a trigger matrix. | Add an investigative independence trigger matrix keyed to subject type, conflict level, and institutional concentration. | P1 |
| Technical courts / specialist chambers | Chapter Eight section 3; CI-7B, CI-15B | 3 | 2 | 2 | 1 | Technical courts are tightly bounded and explicitly prevented from becoming separate sovereign families or ideological censors. | Chamber composition, review of technical standards, and sunset/revision cadence for expert-evidence standards could be more operational. | Add technical-chamber composition minima, periodic standard review cadence, and contest route for expert-guidance documents. | P1 |
| Evidence stewardship and restricted evidence handling | `core_definitions.md` Chapter Four; Article XIV; CI-7, CI-7A | 3 | 3 | 2 | 1 | Evidence custody, security-constrained observability, and challenge rights are well integrated. | The court structure does not yet specify a standard restricted-evidence review workflow for judges, parties, and independent reviewers. | Add a restricted-evidence handling protocol with access tiers, summaries, preservation duties, and post-hoc reconstruction requirements. | P1 |
| Timeliness, backlog, and court usability | CI-6, CI-7.3, CI-12; Article XII-B; Article XXII | 2 | 2 | 1 | 0 | Timeliness and accessibility are recognized, and contest-integrity monitoring is told to watch backlogs. | There are no explicit court performance floors, aging thresholds, or publication timing standards. | Add court performance minima: routing-time target, panel-formation target, decision-publication target, and backlog aging alerts by case class. | P0 |
| Emergency, incapacity, and continuity of adjudication | Article XXII; Article XXIV; CI-8, CI-14; `corpus_systems.md` Protocol D, Protocol R | 2 | 3 | 1 | 1 | Emergency review and continuity logic exist at the constitutional level, and coordination / backup concepts are present. | The adjudication-specific continuity plan is still high-level: not enough on fallback venues, record continuity, emergency quorum, or restoration sequence. | Add a court continuity protocol for emergency incapacity, record transfer, fallback venue, temporary quorum, and restoration review. | P0 |

## Priority close list

1. **P0:** Add a court panel-formation and recusal protocol, including lawful bench constitution, recusal challenge path, inability-to-form declaration, and backup activation record.
2. **P0:** Add court performance minima and monitoring metrics for routing speed, backlog aging, panel formation time, and publication timeliness.
3. **P0:** Add an adjudication continuity protocol for emergency, incapacity, deadlock, and capture conditions.
4. **P1:** Add standardized order / record formats for transfer, certification, anti-self-judging activation, and restricted-evidence handling.
5. **P1:** Add workflow maps for integrity court routing, investigative independence triggers, and institutional-review exhaustion vs direct access.

## Strongest current features

- Explicit court-family differentiation with no silent collapse.
- Dominant-purpose routing rather than party-label formalism.
- Strong anti-self-judging rule with named lead/backup families.
- Good boundary discipline for technical courts.
- Strong separation of merits, forensic support, and investigative functions.

## Most likely failure modes if left unresolved

- adoptive systems improvise panel-formation rules inconsistently;
- recusal failures are recognized in principle but not resolved quickly in practice;
- anti-self-judging backup routes exist on paper but stall for lack of trigger records;
- backlog and delay degrade contestability without breaching a named performance floor;
- emergency or capture scenarios force ad hoc continuity decisions.

## Suggested next drafting package

If you want to close the top gaps efficiently, the next drafting package should probably include:

1. `court_panel_formation_and_recusal.md` or equivalent annex text
2. `court_performance_and_backlog_minima.md`
3. `court_continuity_and_emergency_adjudication.md`
4. standard forms for:
   - transfer / certification order
   - anti-self-judging activation
   - inability to form independent panel
   - restricted-evidence review order

## Evidence note

I did not find existing court-specific drill artifacts or performance dashboards in the current repository analogous to the stronger institutional continuity evidence elsewhere in `evidence/`. That is a notable part of the performance gap.
