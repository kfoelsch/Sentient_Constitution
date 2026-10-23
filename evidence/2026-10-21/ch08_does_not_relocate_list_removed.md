# Chapter 8: "does not relocate" list removed: implementation note (2026-10-21)

Status: done, uncommitted, on branch `docs/ch07-three-gates-plain-language`. Logged as the Seventy-ninth move in `doc_architecture.md`. No rule changed.

## Request (custodian)
The §1 passage "It does not relocate: [five bullets]" looks like boilerplate. Do we need any of it?

## Finding
No. Every bullet was already stated elsewhere, and Chapter Eight has no scope exclusion or opt-out to guard (the reason Chapter Seven kept its Rights Floor clause).
- General non-relocation rule: Chapter Five Authority Stack entry (*Owner register and non-relocation*) and the Preamble owner register.
- Chapter Four / Five / Six: §2 ("Chapter Five supplies their canonical meanings"); Trace widgets route to Chapter Four and Article XVI.
- Chapters Nine to Thirteen: file-top note ("Process-specific application remains downstream") and §9.
- Implementation text: file-top "Implementation owner" bullet (may be stricter, may not narrow).

## Change
`core_08.000_functional_independence_segregation_of_duties.md`: deleted the lead sentence and five bullets at the end of §1. §1 heading unchanged (anchor `#1-purpose-scope-and-owner-boundary` is linked elsewhere).

## Verification
`make plain-terms-edition boundary-chunks print-pack ai-corpus-sync` regenerated; `owner-line-audit`, `owner-discipline-audit`, `plain-terms-edition-check`, `boundary-chunks-check`, `print-pack-check` pass. The full `make audit-report` was not run. `_pages_site` (git-ignored) still has the old text until rebuilt.

## Same sitting
The class-scaling paragraph at the end of §2 ("The functional four-seat floor applies at every class...") is now a lead-in, three bullets (Class C, B, A), and the closing mixed-or-uncertain-scope sentence. Wording unchanged except "it" became "full four-seat separation" in the B and A bullets. Derived files regenerated; same five checks pass.

## §4 wrong-seat routing: automation (Eightieth move)
Custodian: §4 does not say routing should be automated wherever possible; that would take care of most of the problem. Added a paragraph at the start of §4 (routing built into the process wherever practicable) with four bullets for automated routing (follows §5 placement and routes on seat; logs each route; holds and logs the gap when no seat is placed; is not a seat-holder and cannot change who holds a seat). Steward duty unchanged and now framed as the fallback. This adds one "should", no "must". Open item: CI-14.205 §6 item 3 (wrong-seat rule) does not mention automated routing. Derived files regenerated; same five checks pass.

## §5 reorganized and §4 router bullet matched (Eighty-first move)
Applied the evaluation in `claude/ch08-section5-organization-evaluation.md`: four labeled blocks in §5, Class P cut to one sentence, shared map moved to *Where the map is kept*, gap rule as three bullets, "however urgent the act", certification clock linked to Chapter Seven §4.7.4, reading-order line updated. §4 router bullet now follows the §5 substitute or independent path and holds only when none is placed. No duty changed. Derived files regenerated; same five checks pass.

## §5 broken into subsections 5.1 to 5.4 (Eighty-second move, 2026-10-22)
The four bold lead-ins are now `####` subsections (5.1 What the map must say; 5.2 Where the map is kept; 5.3 A seat the map leaves unplaced, or a holder who cannot serve; 5.4 Delegation) with `<a id>` anchors and a reader-guidance widget ahead of the §5 Trace. Section anchor unchanged. Layout only. The §4 router bullet cites §5.3 by number and name. Derived files regenerated; section-cite-name, reference, anchor-heading-drift, section-bullet-lead, owner-line, and the derived-file checks pass.

Same sitting: §5.2 split into three paragraphs (where the map is kept; shared map by reference; Class P). No wording change; checks pass.

## §5.4 Delegation made map-bound (Eighty-third move, 2026-10-22)
Custodian: delegation should not be allowed outside the role map. §5.4 now says a seat may be delegated only to a deputy or substitute the map names; anyone else leaves the seat unplaced (§5.3); naming a new deputy or substitute is a map change (Chapter Seven §4.5); the delegate keeps the same boundary and cannot hold a second seat on the act except through map-listed merged hosting (§6). The §5.1 map bullet and the Chapter Five Charter Role Map entry now say "each deputy or substitute who may act in a seat". This narrows a rule. Open: CI-14.205 §6 item 5 and CI-8.205 §3 do not yet say the delegate must be map-named; staff who only assist inside a seat are not addressed.

## Follow-ups to the Eighty-third move (2026-10-22)
- CI-14.205 §6 item 5 and CI-8.205 §3 now say a seat is delegated only to a deputy or substitute the Charter Role Map or lane map names.
- §5.4 gained a paragraph: staff or tools helping inside a seat are not delegation; the holder stays answerable; help that decides for the seat is a delegation.
- CI-14.205 §6 item 3 now mentions automated routing (the Eightieth move's open item).
- Checks pass: lexical-vocabulary, section-cite-name, reference, anchor-heading-drift, section-bullet-lead, owner-line, owner-discipline, reader-accessibility, derived-file checks, cjs-operational-cluster-audit. `ci-cjs-relocation-audit` found 45 candidates as before and then failed at its evidence-pruning step (file deletion is off in this folder). The prune had already deleted 15 tracked files under `evidence/2026-10-19` and `evidence/2026-10-20`; they were restored with `git checkout`. `evidence/2026-10-21/ch1_cjs3_traceability_matrix_2026-10-21.csv` is modified by an audit run and could not be restored here (unlink not permitted).

## §6 broken into subsections 6.1 to 6.6 (Eighty-fourth move, 2026-10-22)
6.1 How separation scales; 6.2 Merging two seats in one office; 6.3 Informal and community work; 6.4 Seats held in common (five independence bullets); 6.5 Joint professional practice (was a bullet of 6.4); 6.6 Stake, class, and what does not justify a merger (the *Stake still counts* bullet plus the closing paragraph). Reader-guidance widget added; §6 anchor unchanged; §5.2's shared-map cite retargeted to §6.4. Layout only; a word-count check against HEAD shows only the labels removed. Same checks pass.

## "Segregation of duties" renamed "separation of duties" (Eighty-fifth move, 2026-10-22)
Custodian chose "separation of duties" and the whole corpus. Chapter Eight file renamed to `core_08.000_functional_independence_separation_of_duties.md`; Chapter One §18.3, Chapter Ten §3.7, Preamble §5, and the chapter title follow; 49 live files, 206 lines; anchors changed (`#183-separation-of-duties`, `#37-separation-of-duties`, chapter and Preamble anchors). Other-sense "segregation" (escrow of funds, data handling, Chapter Six and Twelve bullets) kept. Dated records and `translations/` not touched; translation links to the English file and anchors need retargeting after the active translation run ends. Checks pass; see the Eighty-fifth move.

## "Segregation" on the do-not-use list (Eighty-sixth move, 2026-10-22)
Audit rule `avoid-segregation` in `tools/lexical_vocabulary_audit.py` (same scope as `avoid-instrument`), internal regression case, report line, and an advisory entry in `tools/architecture/lexical_guardrails.json`. Eight other-sense uses rewritten (separate holding for funds, weights, keys, rewards; isolation for information and data). `project/` live files renamed to "separation of duties"; the dated `project/trials/agent_cooperative_2026-10-20/` keeps the old wording. Audit passes.

§5.4 assistance paragraph reworded for clarity (2026-10-22): assistance (evidence, drafting, routine checks) is not delegation; the holder still makes the seat's decisions and stays answerable; if someone else makes a decision or takes a step in the seat's name, that is a delegation; assistance cannot do what the seat could not.

§5.4 assistance paragraph, last sentence extended (2026-10-22): "...could not do, including pressuring the holders of other seats to determine the outcome of an act."

§6.2 bullet clarified (2026-10-22): "verify-and-record and verify-and-contest remain prohibited" is now "the verify-or-authorize seat is never merged with the record seat or the contest seat"; CI-14.205 §6 item 8 matches. Same rule, seat names as in §2.

## "Independent" defined in Chapter Five; "disinterested" on the do-not-use list (Eighty-seventh move, 2026-10-22)
New Chapter Five `#### Independence` entry (outside the Material Control Line of the party whose act is at issue and of every Interested Party; judged act by act). Fifteen live "disinterested" uses rewritten to "independent" (Chapter Eight, Ten, Eleven, CI-6.225, CI-6.255, doc_architecture). Audit rule `avoid-disinterested` added with regression case, report line, and guardrail entry; `_DATED_RECORD` extended to dated folders.

## §6.3 Informal and community work moved after §6.4 (Eighty-eighth move, 2026-10-22)
New order: 6.3 Seats held in common, 6.4 Joint professional practice, 6.5 Informal and community work, 6.6 unchanged. Anchors, reader-guidance bullets, and the §5.2 cite follow.

## Translation links repaired; two broken checks fixed (Eighty-ninth move, 2026-10-22)
`tools/translation_link_repair.py` run over all 19 locales (link targets and anchor lines only); link audit 0 unresolved; report in `evidence/2026-10-22/translation_link_repair_report.md`. `definition-appropriateness-audit` calls updated; `copy_suffix_clean.py` size fallback; 60 sync copies removed.

## §6.3 first bullet clarified (Ninetieth move, 2026-10-22)
"Outside the control line" is now "Independent of the business": links the Chapter Five definition, keeps the control-line and no-stake tests, and gives a dispute over the supplier's own contract as the example of a dependent party that is not independent.

## §6.3 "The group's own acts" sub-bulleted (Ninety-first move, 2026-10-22)
Three sub-bullets: the four seats; its own System Charter or Institutional Charter; an independent route outside itself. No rule or sentence changed.

## §6.3 groups may set admission limits (Ninety-second move, 2026-10-22)
"No permission and no trap" replaced by No compulsion, Admission limits (capacity, fit, independence, conduct), Limits on the limits (published, even, not anti-competitive, written reason, contestable), and No trap (cost, Act Records). Regression scenario wording followed.

## §6.3 "How the limits are applied" (Ninety-third move, 2026-10-22)
"Limits on the limits" renamed; the group states its admission limits in its System Charter or Institutional Charter (Chapter Seven §3.1), which is how they are published before they are applied.

## §6.3 "How the limits are applied" sub-bulleted (Ninety-fourth move, 2026-10-22)
Five sub-bullets under "Every admission limit:". No rule changed.

## §6.3 "admitting act" clarified (Ninety-fifth move, 2026-10-22)
Last sub-bullet of "How the limits are applied" now says deciding whether to admit an applicant is a materially binding act of the group (see The group's own acts), so it is contestable through the independent route.

## §6.3 leaving a group tied to the data types (Ninety-sixth move, 2026-10-22)
"No trap" now holds only the cost rule; new Leaving bullet (full export, record seat handoff, keep only what duties require) and Data kept by the group bullet (Types I, H, G, S, Y and W per CS-6.310 §9). Regression scenario wording followed.

## §6.4 Joint professional practice bulleted (Ninety-seventh move, 2026-10-22)
Lead sentence plus six bullets. No rule changed. Open: CI-14.205 §7 "Act Records ... the member's to take when they leave" is shorter than the §6.3 Leaving rule.

## §6.4 "Only for listed acts" clarified (Ninety-eighth move, 2026-10-22)
Names the Article XI-E list, points other work to §6.3, and says a host's documents have no standing as a joint professional practice for it.

## §6.4 "no standing" and "the rules above" clarified (Ninety-ninth move, 2026-10-22)
"Only for listed acts" now says adoption does not meet the practice's class duties for other work; "The same rules" now names §6.3 and what carries over. CI-14.205 §7 reworded to match.

## Joint professional practice opened to any work (Hundredth move, 2026-10-22)
Adoption of a host's documents is open for all of a Class L or higher practice's acts; the host of last resort, forum standards, and licence/clearance check stay tied to listed acts. Edited Chapter Eight §6.4, Chapter Seven §1.1, CI-14.205 §7 (and its leaving-members sentence).

## Article XI-E aligned with the joint professional practice change (Hundred and first move, 2026-10-22)
Class-of-the-Operating-Party bullet says the route is open for all work and names what stays tied to listed acts; Implementation bullet names the route.

## §6.3 and §6.4 "meets the separation-of-duties requirement" (Hundred and second move, 2026-10-22)
§6.4 bullet renamed "Meets the requirement" and the class sentence dropped (stated in Chapter Seven §1.1 and CI-14.205 §7); §6.3 lead paragraph closes with the same phrase.

## "Separation-of-duties requirement" carried through Chapter Eight (Hundred and third move, 2026-10-22)
Header, owner block, §1, §2 plain-terms and class lines, and §9 now say "requirement" where they said "floor"; section name and cites, reading-order nickname, Rights Floors, Chapter Seven §1.1 and CI-14.205 §7 unchanged.

## Chapter Eight §2 renamed Four-Seat Constitutional Requirement (Hundred and fourth move, 2026-10-22)
"Floor" is reserved for the Chapter Six Rights Floor. Heading, anchor (`#2-four-seat-constitutional-requirement`), all cites and links, running text, Preamble lines and translation link fragments changed; `avoid-four-seat-floor` ban rule added; earlier history and translated heading text left as they were.

## "Floor" retired for Chapter Seven, the forum appointment rule and related lines (Hundred and fifth move, 2026-10-22)
Chapter Seven header, Class P paragraph and owner line; Chapter Fourteen *Forum appointment independence requirement*; Preamble §5 and §8; Chapter Nine Part A upstream line; Conceptual Overview; CI-8.205 §1 now say "requirement". Other named floors left for a separate decision.

## "Floor" inventory and Chapter Seven/Eight leftovers (Hundred and sixth move, 2026-10-22)
Inventory written to `evidence/2026-10-22/floor_term_inventory.md`; Preamble "What it owns" line, "principle-layer floor" cites, Conceptual Overview, Chapter Five "amendment and review floor" and two `project/` diagram notes now say "requirement" or "rules".

## Group C "floor" phrases renamed (Hundred and seventh move, 2026-10-22)
Time terms to registered window names, joint-structure "X floor" headings to "X minimum", Chapter Fourteen and CI-14.205 §1 floors to "requirement", Portfolio rule; anchors and link fragments updated corpus-wide. Rights Floor family and Chapter Fifteen floors kept. See `floor_term_inventory.md`.

### Hundred and seventh move: audit follow-up (2026-10-22)

Audit tooling changes (descriptor regex, reference-name fragment rule), the CS-6.310 descriptor fix, the Chapter Fourteen CI-14.205 §1–§5 cite, and the split of the translation-link repair report by locale. Full audit report: 105/105 pass.

### Hundred and eighth move (2026-10-22)

Chapter One §11 "Market Structure floor" is now "Market Structure requirements" (core_01.005 §11 and §11.1, CJS-5.125 §11.1/§12, core_05.035, core_12.010 §5.1, steward owner index); CJS-5.130 §17 "governing floor" is "governing rule". Wording only.
CS-6.310 descriptor: 59 cites in 22 files changed from *Information types and handling* to *Data classifications*; pair-level and CS-6.305 uses unchanged.
CS-9.310 descriptor corrected to *System impact classifications* in about 90 cites; four reference lists/anchors repaired where the changed-line audit surfaced older defects.
