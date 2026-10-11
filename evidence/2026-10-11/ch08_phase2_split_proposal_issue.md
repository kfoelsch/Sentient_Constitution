<!-- Draft of the Lane D Proposal issue (CONTRIBUTING.md § Lane D), written to the .github/ISSUE_TEMPLATE/proposal.md form.
     Not filed: the drafting session had no GitHub access to the repository. File it at
     https://github.com/kfoelsch/Sentient_Constitution/issues/new?template=proposal.md
     Title: [Proposal] Chapter Eight: split Phase II (Evaluate) into IIa, IIb, IIc; renumber Part A §3.5–§3.8 and Part B §4–§8
     Then put the issue number in the PRE_PUBLICATION_SPEC §8 row v0.29 and in the pull request body. -->

## Lane

- [ ] C — Adopted implementation maturation (CS / CI / CF / CJS / Remedy / Emergency)
- [x] D — Core text change (numbered `core_*` file)
- [ ] E — Tooling and audits

## Target

- File(s) / stack: `core_08_a_system_alignment_certification_evaluation.md`, `core_08_b_system_alignment_certification_record_process.md`, `core_08_c_system_alignment_certification_illustrations.md`, `core_08_system_alignment_certification.md`; link and cite updates in `core_01_a`, `core_01_b`, `core_01_c`, `core_03`, `core_04`, `core_05_*`, `core_06_*`, `core_09`, `core_12`, and CS-2, CS-3, CS-5, CI-3, CJS-3A.
- Section(s) / anchor(s): Part A §3.5–§3.7 → §4.1–§4.3 (new grouping §4); §3.8 → §5 (§3.8.1–§3.8.6 → §5.1–§5.6); Part C §3.8.k.1 → §5.k.1; Part B §4–§8 → §6–§10.
- Open item advanced (`implementation/PRE_PUBLICATION_SPEC.md` §4.2, §4.3, or §5 step): none. Navigation and structure, before the announcement (CH8-PROCESS-ORDER-01 in `doc_architecture.md`).
- Edition pin: `SC-Corpus-2026.08.09`

## Problem

Part A §3.8 (*Rights-Floor and Domain Evaluations*) holds about half of Part A and sits five levels deep (Part C cites it as §3.8.3.1). The §3 introduction already sorts whole-system evaluation into three tiers (always, when implicated, when triggered), but only in a table, so the structure a reader needs is not in the numbering. Numbers are cheapest to change now: once outside readers cite sections, a later renumber costs every citation, and pre-release anchors cannot be redirected (NAV-PRE-RELEASE-FRAGMENT-01).

This is a navigation and size problem, not a conflict or a Rights-Floor hole. It is filed in Lane D because it renumbers numbered core files and widens a few duty-bearing cites.

## Proposed change

1. Split Phase II into three sub-phases, one section each: **IIa** always (§3.1–§3.4, unchanged), **IIb** when implicated (§3.5–§3.7 → §4.1–§4.3 under a new grouping §4 that adds no obligation), **IIc** when triggered (§3.8 → §5). The six phases stay six.
2. Move Part B by two (§4–§8 → §6–§10) so the numbers stay continuous. One simultaneous mapping pass (`tools/ch8_phase2_split_remap.py`), so old and new numbers cannot collide.
3. Keep the §3 title. State in the §3 introduction that Phase II runs through §3, §4, and §5. Relabel about 100 routing cites of "Chapter Eight §3" to "§3 through §5" so each reaches what it reached before.
4. Widen five duty-bearing cites to §3–§5, §3–§4, or §5.5 where the duty or coverage they state lives in a moved tier: Chapter One §15.1.1 (anti-segmentation for a jointly invoked cluster), Chapter Five Oversight (class scaling of whole-system review; evaluation-coverage check), CS-3 (mandatory depth by class), Part A §1 (the same clause), Part B (record contents; record completeness; Upstream), and one Chapter Five accessibility cite.
5. Update the §1.1 chart, the phase tables, the run sheet, the file blurbs, and the CH8-PROCESS-ORDER-01 decision log.

This pull request should travel with, or after, an earlier same-day change that trimmed repeated scaffolding in §3.8 (now §5) and moved its shared scope-limit statement into the §5 introduction. That change adds five obligation-diff flags, all explained in the evidence record. Split it into its own commit.

## What is NOT changing

- No duty, trigger, class-scaling rule, defect list, or Chapter Six Rights Floor is added, dropped, or reworded.
- The six phases, Sections 1 through 3.4, Part C §3.4.8, and the §3 title do not change.
- The edition label and **pre-release** status are untouched.
- Translations stay paused; their link fragments are not retargeted.

## Owner routing

- Chapter One §12 *Systemic Evaluation Requirement* and §15.1.1 *Anti-Segmentation Principle*; Chapter Five Oversight (*System Boundary Integrity*, evaluation coverage); Chapter Five Continuity (*System Alignment Certification*).
- Downstream files that cite the sections: the files listed under Target, plus the generated indexes (regenerated, not edited).

## Lane D — Test 1 non-regression self-check

- **No Rights Floor narrowed.** The renumber changes only labels, anchors, and link targets. Every cite that reached a duty in the moved tiers still reaches it (Part A §1 "mandatory at full depth for Class A, B, and C" now names §3, §4, and §5; CS-3 says the same).
- **Obligation diff** (`make obligation-snapshot` / `make obligation-diff`) on the 23 core and CS files touched by the renumber: 3029 → 3025 obligations, 5 flags, all from the §3.8 trim, none from the renumber. A second diff over the 14 files touched by the routing relabel: 2009 → 2009, matched 1:1.
- **Full-depth rule read:** the "mandatory at full depth" clause for Classes A, B, and C was the one place where the split could have narrowed what a cite reaches. It is widened in Part A §1 and CS-3, and every other "Chapter Eight §3" cite was reviewed (evidence record).

## Gates you expect to run

- [x] `make regression` (81 targets run one by one: all pass except `lexical-vocabulary-audit`, which fails identically on the unchanged tree)
- [ ] `make readability-audit`
- [x] `make obligation-snapshot` / `make obligation-diff`
- [ ] `make steward-door-lockstep-audit` (included in `make regression`; passes)
- [x] Alignment audit(s): `section-label-anchor-audit`, `local-markdown-fragment-audit`, `section-cite-name-audit`, `corpus-ref-name-audit`, `article-cite-gloss-audit`, `anchor-heading-drift-audit`, `fossil-anchor-audit`
- [ ] New `test_*.py` (Lane E): not applicable; `tools/ch8_phase2_split_remap.py` is a one-shot migration script like the earlier `tools/ch8_*` ones

## Attribution

AI agent (Claude Sonnet 5.5) directed by human — kfoelsch. The AI touched the files listed under Target, the generated indexes, `doc_architecture.md`, `implementation/PRE_PUBLICATION_SPEC.md` (change log row v0.29), `TODO.md`, `implementation/adoption/MINIMUM_VIABLE_ADOPTER.md`, `guides/RECORD_OVERVIEW.md`, `evaluation/external_audit_2026-08/FINDINGS.md` (link targets only), and `evidence/2026-10-11/`.
