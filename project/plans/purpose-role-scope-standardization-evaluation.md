# Standardizing §1 on Purpose, Role, and Scope: evaluation

Date: 2026-11-13. Follows `claude/final-chapter-structure-plan.md` (decision 5 and the "Purpose and Role drafting list") and `claude/ch14-section-0-purpose-and-role-implementation.md` (now Chapter Twenty-One, the model §1). Read against `main` at `ba5314de` (PR #208). Evaluation only; nothing was edited. The drafts for the 16 stub chapters are in `purpose-role-scope-drafts-for-review.md` (same folder).

Note on paths: this file is also kept in the Sentient Constitution Project on claude.ai. Paths starting `claude/` name Project docs, not repository files.

## Settled with the steward (2026-11-13)

1. **Retitle every §1 to "Purpose, Role, and Scope."** Done in the same scripted pass that inserts the approved drafts.
2. **Long explanatory material in §1 stays as §1.x subsections** (Chapters 2, 8, 9, 12). Nothing moves out.
3. **"Chapter scope" is the label for the Scope component in §1.** It is used only for the chapter itself, never for adoption scope, charter scope, or the scope of an article.
4. **"Layer Scope" and "Layer Boundary" are retired as names.** Chapter 6 §1.2 and Chapter 30 §13 become "Owner Non-Relocation." Chapter 27 §1 takes the standard heading, and its four bullets become the chapter scope. **Chapter 28 §5's title is deferred** (the steward will revisit it).
5. **The corpus files are in this pass** (see "Corpus files" below).

## Recommendation (as first given)

**Adopt Purpose, Role, and Scope as the required content of every chapter's §1, and title the section "Purpose, Role, and Scope."** Define Scope narrowly so it stays a pointer and never becomes a second statement of the rule.

## What is on `main` today

| §1 heading on `main` | Chapters |
|---|---|
| "Purpose and Role" (exact) | 1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27 |
| "Purpose and Role — Participation Architecture" | 23 |
| "Purpose, Scope, and Owner Boundary" | 8 |
| "Layer Boundary for This Chapter" | 24 |
| "Role of This Chapter" | 28 |
| No Purpose section (§1 is something else) | 0 (The Model), 5 (Independent Definitions) |

Of the 24 chapters with a Purpose and Role heading, **16 are stubs** (about 35 words, "Draft pending steward review"): 3, 4, 7, 10, 11, 13, 14, 15, 16, 18, 19, 20, 22, 25, 26, 27. Eight are written, and they vary from 685 words (Chapter 21) to 2,307 (Chapter 9).

**Scope already exists in the corpus, with no fixed home and no fixed name:**

- Chapter 8 §1 states scope in its heading and body: applies to every Materially Binding Act; does not apply to a Class P Operating Party.
- Chapter 27 §1, "Layer Boundary," is in substance a scope statement.
- Chapter 31 states scope late, in §4 "Adoption Framing and Scope of Authority."
- Chapter 12 §1.1 "Who Is Certified" and Chapter 6 §1.2 "Layer Scope" carry it as subsections of §1.
- Chapters 28 §5 and 27 §13, both "Layer Scope," are binding owner non-relocation rules ("non-compliant under this section"), not description.
- Chapter 15 §2.1 "Purpose and Scope" and Chapter 16 §2.3 "Question 2 Only — Scope and Routing" are scope statements outside §1.
- Chapter 21's §1 has it as the "This chapter does not" list, trimmed from seven items to two as boilerplate and duplication.

Every chapter also already opens with a placement box that names the constitutional owner and usually a boundary or anti-relocation line.

## Why adopt it

1. **The variety is the problem Scope names.** Seven different §1 headings exist today.
2. **Chapter 21 already has all three, with the middle one unnamed.** Paragraphs 1–2 are Purpose, "This chapter works in this order" plus "does not" is Scope, "Where this chapter sits" is Role.
3. **It gives the "does not" list a defined limit.** A "leaves to others" item stays only if it names the owner and is not already stated at that owner.
4. **Cheapest moment.** The 16 §1s are placeholders, and the translations are paused on old numbering.

## Why be careful

1. **"Scope" is overloaded here** ("scope misalignment," "adoption scope," Article XIX-A "Sandboxed Scope"). The "chapter scope" label answers this.
2. **Scope is the most duty-bearing of the three.** A loosely written Scope paragraph could add or narrow a duty. The drafts restate only existing rules.
3. **Two scopes in one chapter** (Chapters 28, 30 and 6). Answered by the Owner Non-Relocation renames.
4. **Role and Scope overlap.** Answered by the definitions below.
5. **Churn right after the 492nd move.** The slug changes from `#1-purpose-and-role`. I counted 596 references to `#1-purpose-and-role` in 224 files (excluding archive, evidence and generated indexes; translation files are included). The migration engine in `tools/final_chapter_structure_migration/` can retarget them, and the generated indexes must be regenerated.

## Definitions (each is a pointer, none adds a duty)

- **Purpose:** the question this chapter answers, and what it produces. One or two short paragraphs.
- **Role:** where it sits in the whole. What it takes as fixed from upstream chapters, and what it hands downstream.
- **Chapter scope:** what the chapter covers (the order of work, as pointers to sections) and what it leaves to other chapters. Each "leaves to" item names the owning chapter. Three items or fewer is the working limit.

Form: *In plain terms* gloss, then prose and bullets with bold lead-ins. Short §1s take no new subheadings; chapters whose §1 already has §1.x material keep it. Target 300 to 700 words for the three parts, with Chapter 21 as the model.

## Layer Scope renames

The three "Layer Scope" sections are not scope statements. Their text is the owner non-relocation rule, which Chapter Five already names and anchors (`#owner-non-relocation`, in *Authority Stack and Internal Hierarchy*). Renaming them "Chapter Scope" would put a §1 chapter scope and a binding "Chapter Scope" section in the same chapter. So: Chapter 6 §1.2 and Chapter 30 §13 become "Owner Non-Relocation." Chapter 28 §5 also lists the validity-protection controls the chapter may impose (heightened review, provisional suspension, evidence preservation, remediation publication), so it needs a two-part title or a split; deferred.

**Footprint:** four headings (Chapter 6 §1.2, Chapter 27 §1, Chapter 28 §5, Chapter 30 §13) and 15 anchor links (6 to `#5-layer-scope`, 4 to `#13-layer-scope`, 4 to `#12-layer-scope`, 1 to `#1-layer-boundary-for-this-chapter`). Prose mentions: Chapter 5 *Authority Stack* Downstream line (core_05.045, about line 1111), Chapter 30 about lines 24, 187, 331 and 351, and the Chapter 4 non-operative line "states a layer boundary only" (core_04, about line 219). Tools: one advisory rule summary (`tools/architecture/rule_registry.json`, about line 276), a docstring in `tools/ch5_nested_list_candidate_audit.py`, and a test fixture in `tools/test_external_link_audit.py`. None is a gate. I did not run the audits.

The word "layer" stays in the rule text itself ("another constitutional owner layer," "cross-layer drift") and elsewhere ("governance-layer scope," the defined term *Constitutional Contract Layer*). A sweep of "owner layer" to "owner chapter" is a separate terminology decision and is not in this pass.

## Corpus files

78 files sit under `corpus_forum/` (17), `corpus_institutions/` (28), `corpus_joint_structure/` (15) and `corpus_systems/` (18), plus four aggregate files. **Only 16 have a purpose-type first section.** All are in `corpus_systems/` (15 of its 18 files) and `corpus_joint_structure/` (one):

| Current heading | Files |
|---|---|
| "§1 Purpose and Role" (11) | cs_06.315, .320, .325, .330, .335, .340, .345, .350, .355; cs_09.315, .320 |
| "§1 Purpose and Scope" (3) | cs_06.305, cs_09.305, cs_24.305 |
| "§0: Purpose and Role" (1) | cs_00.310 |
| "§0: Purpose of This Layer" (1) | cjs_00.110 |

The other 62 corpus files open with a topical rule as §1 (for example "§1 Basic Rule," "§1 Minimum Record Set") and have no purpose section.

**Proposed for this pass:** retitle the 16 to "Purpose, Role, and Scope" and check each body against the three definitions. CS-0.310 and CJS-0.110 use §0, and CJS-0.110 already has a §1 ("Section Identifiers and Article References"), so renumbering §0 to §1 would shift every section and cite in those files. Retitle them in place ("§0: Purpose, Role, and Scope"). CJS-0.110's current heading uses "Layer," which the "Layer Scope" decision suggests changing.

**Not proposed:** adding a new §1 to the other 62 files. That would be 62 new drafts of implementation text. Decision below.

## What changes when adopted

| Item | Change |
|---|---|
| 16 stubs | Insert the approved drafts; replace the stub sentence. |
| Chapter 21 | Retitle. Regroup existing text under the three lead-ins. No content change. |
| Chapters 8, 27, 31, 23 | Retitle. Chapter 27's four bullets become chapter scope, with Purpose and Role added. Chapter 8's scope paragraph moves under the Chapter scope lead-in. Drop the "— Participation Architecture" suffix from 23, or keep it as a deliberate exception. |
| Chapters 9, 12, 17 (and 2, 6) | Retitle. Add the three lead-ins above the existing material. |
| Chapters 28, 30 and Chapter 6 §1.2 | Rename per above; Chapter 28 §5 deferred. |
| Chapters 0 and 5 | Exempt, as the plan already has it. |
| Corpus | Retitle the 16 files above. |
| `tools/ch10_duplication_audit.py` | Its exemption for the stub sentence (line ~151) must follow the new wording or the parallel Chapters 9–11 and 12–14 will start failing. |
| Plan decision 5 | Rewrite. It still uses old numbers ("Chapters 8 and 20 keep their current §1 headings"). On the new map those are 8 and 28, and 24 is also non-standard. |
| New check | An audit that §1 carries the exact heading and the three lead-ins. |

## Still open

1. **Chapter 28 §5 title** (deferred by the steward).
2. **Chapter 15 §2.1 and Chapter 16 §2.3** (scope statements outside §1). Leave and point (as drafted), retitle, or fold into §1 chapter scope.
3. **The other 62 corpus files:** leave without a Purpose, Role, and Scope section (recommended), or draft one for each.
4. **Stale cites found while drafting** (Chapter 28 §5, Chapter 22, six placement boxes). Listed in the drafts document.

## Not checked

I read the §1 text for Chapters 1, 2, 6, 8, 12, 17, 21, 23, 27, 28 (§5), 27 (§13) and 28, and the placement boxes and outlines of the 16 stub chapters. I did not read the bodies of the stub chapters. No audits were run.
