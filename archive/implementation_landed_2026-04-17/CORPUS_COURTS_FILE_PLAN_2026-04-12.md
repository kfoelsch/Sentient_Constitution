# Corpus courts file plan

Status: implementation planning artifact (non-authoritative).  
Date: 2026-04-12.  
Question addressed: whether court-related material now warrants a separate companion legal file, and if so, how it should be structured.

## Recommendation

Create a separate incorporated companion file:

- `corpus_courts.md`

Do **not** create a fourth core constitutional file at this stage.

## Why this is called for

The current architecture still has a clean constitutional owner for courts:
- `core_constitution.md` Chapter Eight owns court families, default venue, anti-self-judging, transfer/certification logic, and the constitutional boundary between court families.

But court-related implementation material is now spread across too many non-core locations:
- `corpus_institutions.md`
- `corpus_primitives.md`
- `corpus_systems.md`
- multiple `implementation/` drafts that are now substantial enough to be future normative candidates

That spread creates three problems:

1. **Single-home drift**
   - Court operations now live partly in institutions, partly in primitives, partly in systems, and partly in implementation drafts.

2. **Adoption friction**
   - A real adopter trying to stand up the court layer would have to assemble doctrine from multiple files instead of reading one legal-operational court companion.

3. **Normative promotion risk**
   - Important court mechanics are now stranded in draft implementation files. Without a dedicated destination, they are likely to remain support text instead of becoming binding incorporated law.

## Why not a new core constitutional file

A new core constitutional file is **not** yet necessary because the constitutional theory layer is still compact and coherent:
- Chapter Eight already does the constitutional job well.
- The main growth is in operational legal doctrine, not in the constitutional identity of the court system.

Creating `corpus_courts.md` preserves the current authority stack:
- core constitution states the constitutional court architecture
- companion court file supplies incorporated implementation detail

That is consistent with the existing boundary rules and Chapter Fourteen incorporation model.

## Authority model

The recommended authority model is:

1. `core_constitution.md`
   - remains constitutional owner of:
   - court families
   - dominant-purpose routing
   - anti-self-judging
   - transfer / certification constitutional logic
   - justice / emergency constitutional constraints where courts apply them

2. `corpus_courts.md`
   - becomes binding incorporated implementation text for:
   - court operations
   - panel formation
   - recusal workflow
   - appeal and review mechanics
   - backup activation
   - forensic support
   - investigative independence
   - specialist courts
   - performance minima
   - continuity and emergency adjudication

3. `corpus_institutions.md`, `corpus_primitives.md`, `corpus_systems.md`
   - keep only court-adjacent material that truly belongs to those files
   - cross-reference `corpus_courts.md` instead of carrying the full court-operational burden

## Proposed boundary rule

Use this simple rule:

- **Core Constitution** owns `which court family decides what, and why`
- **Corpus Courts** owns `how courts are constituted, reviewed, supported, measured, and kept independent in practice`

## Proposed outline for `corpus_courts.md`

### 1. Opening and scope

- purpose of the court companion
- authority statement: incorporated implementation text under Chapter Fourteen
- relation to Chapter Eight, Article XII-B, Article XIV, Article XXI, and Article XXII
- non-duplication rule

### 2. Court formation and composition

- court-family to tribunal translation rule
- family/chamber distinction
- composition minima
- qualification and competence minima
- reserve and substitute capacity

### 3. Panel formation, recusal, and lawful bench constitution

- panel-formation record
- mandatory disclosures
- recusal triggers
- recusal challenge
- substitute selection
- inability-to-form independent panel
- backup-forum activation

### 4. Routing, transfer, certification, and representative treatment

- operational routing decision tree
- mixed-stakes tie-breaks
- transfer and certification order minima
- consolidation rules
- representative treatment procedure minima

### 5. Appeal, secondary review, and exhaustion

- internal review vs independent review
- appellate lane structure
- emergency review lane
- direct-access exceptions
- exhaustion rule where applicable

### 6. Integrity, anti-capture, and anti-self-judging operations

- interaction with integrity courts
- interaction with contest-integrity monitors
- anti-self-judging record requirements
- integrity escalation path
- recusal abuse and panel manipulation controls

### 7. Court forensic and analytical support

- role boundaries
- scope orders
- challenge rights
- chain of custody
- restricted-evidence workflows

### 8. Independent investigative service and prosecution interface

- anti-self-investigation rule
- operational separation from prosecutors and courts
- escalation triggers
- referral and closure records

### 9. Technical courts and specialist chambers

- science / engineering / medicine chambers
- additional chamber criteria
- composition minima
- standard-setting cadence
- reviewability and anti-cartel constraints

### 10. Court performance, accessibility, and backlog control

- timing floors
- backlog thresholds
- accessibility and pathway usability
- dashboard and disclosure schema
- remediation triggers

### 11. Continuity and emergency adjudication

- continuity modes
- temporary quorum
- fallback venues
- record continuity
- restoration review
- post-incident review

### 12. Standard records and forms

- panel-formation record
- recusal challenge
- inability-to-form certification
- backup activation order
- transfer / certification order
- restricted-evidence review order
- continuity activation record
- post-incident review template

## What should move into `corpus_courts.md`

### From `implementation/`

These should be primary seed inputs:

- `implementation/COURT_PANEL_FORMATION_AND_RECUSAL_PROTOCOL_DRAFT_2026-04-12.md`
- `implementation/COURT_PERFORMANCE_AND_BACKLOG_MINIMA_DRAFT_2026-04-12.md`
- `implementation/COURT_CONTINUITY_AND_EMERGENCY_ADJUDICATION_DRAFT_2026-04-12.md`

These should remain support / planning:

- `implementation/COURT_STRUCTURE_GAP_FRAMEWORK_2026-04-12.md`
- `implementation/COURT_STRUCTURE_GAP_MATRIX_2026-04-12.md`
- this file

### From `corpus_institutions.md`

Strong candidates to migrate fully or substantially:

- `CI-7A: Court forensic and analytical support`
- `CI-7A.1: Independent investigative service`
- `CI-7B: Technical courts`

Strong candidates to keep in `corpus_institutions.md` but shorten and cross-reference:

- `CI-6` court-adjacent procedure language
- `CI-7.3` contest-integrity monitoring references to courts
- `CI-8` cross-institution coordination references to court routing

### From `corpus_primitives.md`

Keep there:

- general procedural-integrity and adjudication primitives
- general independence, auditability, and challenge obligations

Do not move:

- legacy `Provision VI` substance now consolidated in `PROT6`
- `PROT6`

But add explicit cross-references from those sections to `corpus_courts.md` for court-specific implementation detail.

### From `corpus_systems.md`

Keep there:

- cross-jurisdiction execution
- steward conflict / recusal rules for system governance
- Protocol R and Protocol D continuity logic

Do not move those sections.

Instead:
- cite them from the court continuity chapter where courts rely on them

## What should stay in core

These should remain in `core_constitution.md` Chapter Eight and not migrate:

- court-family taxonomy
- dominant-purpose rule
- asymmetry rule
- cross-court anti-self-judging rule
- constitutional routing logic
- certification to constitutional courts
- interim-relief constitutional boundary
- relation to Chapters Six, Seven, and Nine

If a passage answers `what family hears this and why`, it belongs in core.
If it answers `how that family is operationally constituted and governed`, it likely belongs in `corpus_courts.md`.

## Proposed migration style

Use a conservative migration strategy:

1. create `corpus_courts.md` with its own stable internal headings
2. move court-operational detail from `implementation/` drafts into the new file
3. shorten overlapping court-operational sections in `corpus_institutions.md`
4. replace moved detail with concise owner-pointer text
5. update `README.md`, `doc_architecture.md`, and Chapter Fourteen references
6. only then consider whether any further refactoring is needed

## Suggested stable heading set

To keep citations durable, use stable section families such as:

- `CC-1` Scope and authority
- `CC-2` Court composition and formation
- `CC-3` Panel formation and recusal
- `CC-4` Routing, transfer, and certification operations
- `CC-5` Appeal and review lanes
- `CC-6` Integrity safeguards and anti-self-judging operations
- `CC-7` Forensic and analytical support
- `CC-8` Independent investigative service
- `CC-9` Technical courts and specialist chambers
- `CC-10` Performance, backlog, and accessibility
- `CC-11` Continuity and emergency adjudication
- `CC-12` Standard records and forms

## Required architecture updates if adopted

If you create `corpus_courts.md`, update:

1. `README.md`
   - add the new file to related documents and incorporated source guidance

2. `doc_architecture.md`
   - add the file to section 2 corpus roles
   - update boundary rules
   - add a single-home rule note for court-operational doctrine
   - update any stable-ID registry or owner table that mentions courts

3. `core_constitution.md` Chapter Fourteen
   - add `corpus_courts.md` to the incorporated companion-file list if you want it binding

4. `core_definitions.md` Chapter Five `Corpus (Constitutional)`
   - ensure the new file is designated there if needed by your adoption model

## Decision test

Create `corpus_courts.md` if you want all of the following at once:

- one legal-operational home for courts
- less doctrinal spread across institutions/primitives/systems
- a clean destination for the new P0 court protocols
- easier adoption by a real judiciary or court-designing authority

Do **not** create it yet if you would rather keep all court operations inside `corpus_institutions.md` and you are prepared to turn that file into a much more court-heavy institutional code.

## Recommendation on that choice

I recommend creating `corpus_courts.md`.

At this point the court layer is specific, dense, and operational enough that keeping it embedded in `corpus_institutions.md` is more likely to increase cross-file sprawl than to preserve simplicity.

## Suggested next steps

1. approve the new file name and scope
2. scaffold `corpus_courts.md`
3. migrate the three P0 drafts into the new file
4. rewrite overlapping `corpus_institutions.md` sections into shorter owner-pointer text
5. update architecture and incorporation references
