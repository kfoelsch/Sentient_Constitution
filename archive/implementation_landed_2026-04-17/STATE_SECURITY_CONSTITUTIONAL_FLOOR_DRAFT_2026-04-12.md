# State security constitutional floor draft

Status: Drafting artifact (non-authoritative).  
Date: 2026-04-12.  
Purpose: propose narrow constitutional-floor language for state security, intelligence, covert investigation, and secrecy-governed powers without relocating operational detail out of owner layers.

## Drafting intent

This draft is intentionally narrow.

It is designed to:

- add explicit constitutional prohibitions and limits where the current corpus relies mostly on implication;
- preserve the current architecture in which operational mechanics remain in companion corpus files;
- avoid normalizing intelligence or security services as a free-standing constitutional entitlement of the state.

This draft does **not** itself decide whether a future adopter should maintain a distinct intelligence service. It instead states the floor that would govern any such service or any analogous covert security function.

## Recommended insertion shape

Best fit in `core_constitution.md`:

- primary home: **Chapter Nine** as a new Article adjacent to **Article IX** and **Article XIV**, because the core issue is rights-protective limits on surveillance, secrecy, coercive observation, and hidden power;
- companion hooks: **Chapter Eight** and companion corpus files for authorization workflow, forum design, oversight bodies, secrecy review, and evidence handling.

## Candidate constitutional text

### Article IX-E: Security, Intelligence, and Covert-Power Limits

- **No secret-police or ideological-enforcement power:** No institution, steward, or coordinated body may operate as a **secret police**, ideological-enforcement organ, or hidden political-security authority. No body may use covert monitoring, infiltration, threat scoring, or secret record accumulation to suppress lawful dissent, protected reporting, journalism, labor organization, protected association, lawful belief, or constitutional contest.
- **Exceptional status of covert power:** Covert, secrecy-constrained, or intelligence-like powers are constitutionally exceptional. They are valid only where a lawful and published authority exists, the objective is constitutionally legitimate and materially serious, less intrusive means are not reasonably sufficient, and the use remains necessary, proportionate, time-bounded, and independently reviewable.
- **No generalized population surveillance:** Persistent or population-scale surveillance, tracking, pattern extraction, or cross-context identity linkage is prohibited absent a demonstrated and extraordinary justification satisfying this chapter, Chapter One, Chapter Five, and Constitutional Systems, **Chapter S1 — Information Types and Handling** and **Chapter S2 — System Classification and Handling** where applicable.
- **Protected activity shield:** Political participation, lawful opposition, journalism, protected reporting, associational life, belief, research, and constitutional challenge activity receive heightened protection. They must not be made subjects of covert collection, infiltration, or analysis absent a specific, independently reviewable showing of constitutionally sufficient necessity tied to material harm prevention or investigation of materially serious unlawful conduct.
- **Independent authorization:** Intrusive covert measures, including secrecy-constrained investigative steps, require prior authorization through a lawful independent process except where immediate action is necessary to prevent imminent and material harm and delayed authorization would defeat that purpose. Emergency use must trigger prompt post hoc review, record preservation, and automatic lapse absent timely reauthorization.
- **No anti-bypass evasion:** No institution may obtain, request, purchase, receive, launder, or use information through foreign partners, intermediaries, private actors, or parallel domestic bodies in order to evade constitutional limits that would have applied had it collected or derived the information directly.
- **No hidden internal-state reconstruction:** Security or intelligence functions must not infer, reconstruct, simulate, or represent protected internal states except under the same or stricter constitutional limits that would govern direct access to such data. Behavioral, predictive, or analytic models must not be used to bypass internal-state protections through proxy inference.
- **Secrecy does not erase accountability:** Secrecy may protect only what is necessary to prevent material and unjustified harm from disclosure. It must not erase auditability, independent review, reasoned authorization, preservation of exculpatory or mitigating material, or eventual accountability. Where secrecy no longer remains justified, disclosure, declassification, or notice must occur within a lawful and reviewable process.
- **No sole control by operational security bodies:** Bodies exercising police, security, intelligence, detention, or comparable coercive functions must not retain sole control over authorization, collection, classification, review, and legality assessment for their own covert activities. Independent oversight, challenge pathways, and anti-self-investigation protections must remain functionally real.
- **Remedy and taint rule:** Information obtained or used in violation of this Article must be subject to exclusion, segregation, deletion, reclassification, notice, remediation, or other lawful corrective action sufficient to restore rights and deter recurrence. Secrecy must not be used to defeat remedy where material constitutional violation is shown.

### Reader note on implementation owner

If adopted, this Article should remain a constitutional floor only.

Operational detail should be assigned as follows:

- `corpus_courts.md`: authorization forum, secrecy-constrained application handling, use of secret evidence, notice timing, and taint/remedy pathways in adjudication;
- `corpus_institutions.md`: oversight bodies, reporting lines, anti-capture separations, inspector or ombud access, and review triggers;
- `corpus_systems.md`: classified-system handling, data-type interactions, retention, linking, model constraints, and declassification or reclassification triggers for system-governed records.

## Optional narrower variant

If the project wants a more cautious insertion, the constitutional floor could be reduced to four bullets:

- no secret-police or ideological-enforcement institutions;
- no domestic political surveillance or protected-activity targeting absent the highest constitutional threshold;
- covert and secrecy-constrained powers require independent authorization, necessity, proportionality, records, and time bounds;
- no foreign or inter-agency bypass of constitutional surveillance limits.

That version would close the most dangerous gaps while leaving most structure to companion corpus text.

## Drafting notes

- The phrase **secret police** is included on purpose rather than left implicit. The current anti-surveillance and anti-manipulation language is strong, but this concept does distinct constitutional work and should likely be named directly if adopted.
- The anti-bypass clause is included because many surveillance regimes evade domestic limits through foreign collection, private contractors, or inter-agency routing.
- The text avoids asserting a broad positive state entitlement to intelligence collection. It instead frames such powers as exceptional and legitimacy-burdened.
- The draft deliberately points back to existing owners for operational mechanics to preserve single-home discipline under `doc_architecture.md`.
