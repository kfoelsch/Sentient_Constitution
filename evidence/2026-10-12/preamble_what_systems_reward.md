# Preamble: "What Systems Reward" and the Two Fundamental Questions (2026-10-12)

Edition `SC-Corpus-2026.08.09` (pre-release). Based on `origin/main` at `ba00a185`.

## Change
- `core_00_preamble.md`: new unnumbered section **What Systems Reward** (anchors `what-systems-reward`, `two-fundamental-questions`) before "1. The Model". It puts the **Two Fundamental Questions** to every system:
  1. Does it reward conduct that helps sentients flourish and endure, tells the truth, and repairs harm?
  2. Does it reward conduct that unjustifiably harms, misleads, excludes, delays, wastes, or shifts costs onto others?
  A system passes only with yes to the first and no to the second. "Unjustifiably" covers every verb in the second question; what counts as helping, harming, fair, or justified is judged by the Constitution's own standards, not the system's. "Misleads" (not "deceives") so negligent and structural misleading is covered. No new Chapter Five term; the section routes to existing definitions.
- `core_00_preamble.md` section 2: "asks two practical questions: ..." replaced by "puts the Two Fundamental Questions to what systems actually do, not to what they claim." The outcome ideas (harm, delay, exclusion, waste, hidden dependency, false trust) now live in the questions and the second-question bullet.

## Cross-references added
| Where | Change |
|---|---|
| Preamble, What Systems Reward | Links to Ch1 §19.1.1 and §19.1.2 as the operative rules behind the two questions |
| Ch1 §19 intro | Paragraph pointing back to the Preamble and naming §19.1.1 and §19.1.2 |
| Ch1 §3.2 "Three dimensions" | Sentence tying §3.2.1 (first question) and §3.2.6 (second question) to the Preamble |
| Ch5 Incentive Alignment, primary measure | "The measurement form of the Two Fundamental Questions" |
| Ch5 Measuring Accountability table, incentive alignment row | Same pointer |
| README "What is this?" | Paragraph with the two questions and the "judged by the Constitution's own standards" guard |
| `implementation/adoption/ANNOUNCEMENT.md` section 1 | Short paragraph quoting the two questions and the guard sentence (authentic spans, per section 2) |

## Small fixes found on the way
- `ANNOUNCEMENT.md` section 1: "(Chapters Nine and Nine)" corrected to "(Chapters Nine and Ten)" (standing assessment and standing integration).
- `implementation/STEWARD_ENTRY_DOORS.md`, Incentive alignment card: link text "Chapter One §18" corrected to "§19" (the target was already the §19 anchor).

## Regenerated
`ai_corpus/indexes/*` (five files), `doc_architecture/generated/` plain-terms edition, boundary chunks, print pack, rights-floor sheet. The rights-floor sheet diff is a link-ordering change that regeneration produces on this base, not content from this change.

## Checks (clean copy on `origin/main` plus this change)
- `make regression`: one failure, `lexical-vocabulary-audit` (12 "people" phrasings in `core_08_a_...`), present on `origin/main` before this change. AI manifests fresh.
- `plain-terms-edition-check`, `boundary-chunks-check`, `print-pack-check`, `reader-accessibility-check`, `pages-corpus-index-check`, `pages-site-check`, `section-cite-name-audit`, `corpus-markdown-audit`, `local-markdown-fragment-audit`, `steward-door-lockstep-audit`, `in-paragraph-link-audit`: pass.
- Readability (advisory): Preamble grade 13.53 before, about 13.2 after; target 14.0.

## Not done (deliberately)
- Translations (Lane F): the Preamble and README are translated in several languages; English governs.
- Lighter pointers from the scan (Article XIII-D, Ch8A section 3.3, overview guide, START_HERE, FAQ, AI alignment eval framework). Held until after the announcement.
- Question 1 does not say "prevents" (Ch1 section 19.1.1 rewards prevention most). Wording decision for the custodian.
- The short form in `ANNOUNCEMENT.md` section 1 is unchanged.

## Needs custodian sign-off
1. "The designers of systems that train or optimize AI, whose objectives and feedback signals are rewards in exactly this sense" extends the questions to training signals. Consistent with the Incentive Alignment scope ("comparable mechanisms acting on agents, operators, or constituent components"); not traced through the AI-facing chapters.
2. The closing bridge sentence in the Preamble section ("The four duties in section 1 are how the answers are kept honest").
3. Placement as an unnumbered `###` section ahead of section 1.
4. The announcement paragraph (public text) and the README paragraph.
