# Archived TODO — P3 holistic redundancy sweep

**Archived:** 2026-06-15 (consolidated cut). **Active checklist:** [`TODO.md`](../TODO.md).

## Status

- [x] **User acceptance gate:** Accept, repurpose, or continue the holistic redundancy / definitions-first sweep after a final grep-per-theme dedup across the four companion corpus files.

Closed as of 2026-05-06; continuation narratives preserved below. Further companion routing work after 2026-05-07 is tracked under [TODO_COMPLETED_CI_CJS_CS_RELOCATION_2026-06.md](TODO_COMPLETED_CI_CJS_CS_RELOCATION_2026-06.md).

## Engineer closure narrative

**Engineer status as of 2026-04-30 cleanup:** Many 2026-04-29 non-regression passes corrected stale chapter, article, anchor, and terminology routing without flipping this user-owned checkbox. Full detail is archived in [TODO_SNAPSHOT_2026-04-30.md](TODO_SNAPSHOT_2026-04-30.md).

**2026-04-30 continuation:** The non-regression redundancy sweep continued across the four companion corpus files and was committed as `ad3f704` (`Tighten companion corpus ownership pointers`). Detailed pass notes are archived in [TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md](TODO_SNAPSHOT_2026-04-30_POST_COMMIT.md).

**2026-04-30 continuation addendum:** Normalized remaining **Protocol A**, subsection **G** continuity pointers in `corpus_forum.md`, `corpus_institutions.md`, and `corpus_systems.md` so forum, institutional, and steward-continuity references use the established owner phrasing instead of the stale **Protocol A G** shorthand. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`.

**2026-04-30 continuation addendum 2:** Completed another targeted non-regression grep pass for owner-phrasing drift across the companion corpus. Normalized `corpus_institutions.md` S2/S3 references, tightened a **Sentient Constitution Chapter Ten, Article XV-A** pointer, restored **Article X-C**/**Article X-A** to the CI-15 rights-owner boundary, and tightened `corpus_systems.md` **Article XXV-A** transition routing to **Sentient Constitution Chapter Ten**. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`. Regression testing remained intentionally omitted.

**2026-05-06 continuation addendum:** Continued the non-regression companion-corpus redundancy sweep for remaining owner-phrasing drift. Tightened `corpus_institutions.md` **CI-1.5**, **CI-6**, and **CI-9.1B** into pointer-first applications of Chapter Eight, `corpus_joint_structure.md` **CJS-3.12**, and delegated-body owner language; tightened `corpus_forum.md` **CC-6.1** and **CC-10.0** into pointer-first applications of **CJS-3.3**, **CJS-3.33**, and existing rights owners; tightened `corpus_systems.md` **Protocol S4** and **Protocol S5** so Article XXI-A and due-process rights stay in their owner layers while the systems companion preserves only allocation, cause-mapping, funding-record, and incentive-governance mechanics. Also corrected local Markdown emphasis and sentence-wrap defects found during the sweep. Ran non-regression checks only: `make reference-audit`, `make corpus-markdown-audit`, and `make lexical-vocabulary-audit`. Regression testing remained intentionally omitted.

**Suggested acceptance check:** run targeted theme greps across `corpus_joint_structure.md`, `corpus_systems.md`, `corpus_institutions.md`, and `corpus_forum.md`; convert duplicative companion prose to pointers where it repeats Chapter Five definitions or Chapter Ten rights without adding implementation detail.

## MEMLOG cross-reference

Long-form session narrative for 2026-04-30 and 2026-05-06 continuation passes: [MEMLOG_SNAPSHOT_2026-06-15.md](MEMLOG_SNAPSHOT_2026-06-15.md) (Active Threads section, archived layer).
