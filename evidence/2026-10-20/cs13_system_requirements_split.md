# CS-5 split into CS-5 System lifecycle and CS-13 System requirements: implementation note (2026-10-20)

Status: done, uncommitted, on branch `docs/ownership-statements-sweep`. Logged as the Sixty-seventh move in `doc_architecture.md`. Translations were not touched. The same note is in the folder at `evidence/2026-10-20/cs13_system_requirements_split.md`.

## Request (custodian)
After the ownership sweep, the steward found the title of CS-5 poor and wanted it fixed. CS-5 carried two unrelated topics under one number and two titles: design, testing, verification, and deployment, and the catalog of user-reachable capability surfaces (Part A). Agreed: Part A becomes its own family, CS-13 *System requirements*, and the rest of CS-5 is retitled *System lifecycle* (the steward floated "System Governance Processes"; the shorter, plainer name was proposed and approved).

## New structure
- **CS-5: System lifecycle** (`cs_05_design_testing_verification_deployment.md`, name unchanged). Sections CS-5.1 to CS-5.10 unchanged. The old title survives as the description in its owner line.
- **CS-13: System requirements** (`cs_13_system_requirements.md`, renamed from `cs_05_a_user_facing_capabilities.md`). CS-5.11 Purpose and role is now CS-13.1, CS-5.12 In-scope catalog is CS-13.2, CS-5.13 Analog, digital, and channel class is CS-13.3, CS-5.14 What this file does not own is CS-13.4. Anchors and the Trace "Downstream" list were renumbered with them.
- **Reading chain:** CS-13 stays between CS-5 and CS-6, where Part A was (the same placement as CI-28 after CI-13). The Previous and Next links only changed their target name.

## Finding that changed the plan
The earlier plan was to retarget the 46 citations that call CS-5 "User-facing capability surfaces" to CS-13. Reading each one showed that was wrong: 74 citations carried that label, and nearly all point at lifecycle sections (§8 governance continuity, crisis communications, and exercises; §9 self-healing and recovery-path integrity; regression testing and certification defects; forum certification and lifecycle review; safety profiles). The label was a mislabel on lifecycle citations, not a pointer to Part A. Retargeting them would have sent readers to the wrong file.

## What was done to citations
| Group | Count | Result |
| --- | --- | --- |
| Label "User-facing capability surfaces" on a lifecycle citation | 74 | Now **CS-5** (*System lifecycle*). Same target |
| Old long title "Design, testing, verification, and deployment" | 28 | Now *System lifecycle*. Same target |
| Citations that truly mean the catalog of user-reachable surfaces | 8 | Moved to **CS-13** (*System requirements*): the CS-D04 and CS-D12 rows and trace lines in CS-0, the CS-1 scope list, the Chapter Four trace line, and the CS-5 owner and trace lines |
| Range statements "CS-1 through CS-12", "CS-2–CS-12", "CS-5–CS-12" that list the systems families | 13 | End at CS-13 (CS-0, CS-1, landing page, CJS-1, CJS reader guide) |

Sorted by what each citation points at, not by the label it carried. The two CS-5 files, CS-0, CS-1, Chapter Four, Chapters Five, Six, and Nine, CJS-0, CJS-3, CF-7, CF-12 to CF-14, CI-11, CI-14, CS-3, CS-4, CS-8, CS-10, CS-11, and CS-12 were edited.

## One sentence changed
The old Part A closing paragraph said "No CS-13 … Do not mint a 'required software' family." CS-13 now exists, so the paragraph reads: "Not a software list. This family catalogs user-reachable in-scope surfaces and nothing more. … Do not extend it into a list of required software." The point of the old rule is kept. Nothing else in the Part A text changed.

## Files touched
Moved and edited: the two CS-5 files; `cs_06` (Previous link). Retitled, relabelled, or range-extended: files listed above. Tooling: `tools/footer_audit.py` (reading chain), `tools/architecture/family_map.json` (family id `CS-5A` is now `CS-13`; section homes 13.1 to 13.4; CS-5 label), `tools/section_glosses.json` and `tools/glosses_cs_cjs.json` (key and the one gloss sentence). Regenerated: the grouped family index in `corpus_systems.md`, `ai_corpus/indexes/`, and the four derived files. `doc_architecture.md`: new Sixty-seventh move; the "one family number spans several files" rule no longer lists CS-5 and CS-5 Part A; the "CS-5–CS-12" lighter-structure line now ends at CS-13.

## Left alone on purpose
Translations (paused), `evidence/` and `archive/` folders, dated records, earlier moves in `doc_architecture.md`, and the former protocol-letter alias table (Protocol A is still CS-5). The test fixture in `tools/test_adopted_implementation_filename_audit.py` still uses the old file name as an example of a home-plus-part-letter pair; it tests the audit, not the corpus, and the real corpus keeps that pattern in CS-2 and CS-3.

## Verification
- `make audit-report`: 105 of 105 pass. It first ran 104 of 105: `ch1-cjs3-alignment-audit` could not prune old evidence because file deletion was off in the connected folder. After the steward allowed deletion, the retention rule removed the oldest run (9 files: the 2026-10-04 alignment run and `evidence/2026-10-03/REFERENCE_INTEGRITY_AUDIT_2026-10-03.md`) and the gate passed. `ch1_cjs3_audit_log_2026-10-20.json` was restored to its committed content.
- `make owner-line-audit`: PASS (43 core files, 75 implementation files). `make corpus-ref-name-audit` (changed-only), `make footer-audit` (118 files in the chain), `make family-map-audit`, `make adopted-implementation-filename-audit`, `make adopted-implementation-anatomy-audit`, and `make adopted-implementation-cite-audit` pass.
- `make ai-corpus-sync` and the four derived-file regenerations ran after the edits.
- No leftover "User-facing capability surfaces", `cs_05_a_`, "CS-5, Part A", or "CS-5A" in the live corpus outside translations, evidence, archive, and dated move history.

## Open
- The steward may want to read the CS-13 owner line and the CS-5 owner line once; both give the new title and say what the other holds.
- 116 translation files mention CS-5 (paused until after the announcement). None link to the old Part A file name or use the old English label, but their CS-5 titles will need the new name when translation work resumes.
- Changes are uncommitted. Suggested commit message: "CS-5: split into CS-5 (System lifecycle) and CS-13 (System requirements)".
