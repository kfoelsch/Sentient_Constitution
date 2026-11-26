# Chapters 0–1 translation resynchronization inventory

**Status:** AI-assisted draft set exists for all 38 locale/source pairs. The documented source-coverage and destination-aware link issues are repaired; the drafts still require independent fluent review before synchronization.

## Pinned English source

- Edition: `SC-Corpus-2026.11.25`
- Source commit: `6e0b6c663dde01b5dea731fe33d87725c7174930`
- `core_00.000_preamble.md` SHA-256: `90799cb8019b41356fa5dd90565e3f9540fc346e8c77e2c321b841654f39b274`
- `core_01.000_constitutional_map.md` SHA-256: `aca759b394f10784ab1a2eef4e9e2ca12e369ef0ca8ee797298c6af00d2950aa`

The source files still match these hashes and edition. Each locale draft records the source pin and language variety.

## Structural crosswalk

| Current destination | Previous translated Preamble material | Draft disposition |
| --- | --- | --- |
| Chapter 0 opening and §§1–2 | Opening and former measurement overview | Existing translated passages retained and compared structurally; current §2 replaced with translated §§2.1–2.4, table and current anchors. |
| Chapter 0 §3.1 | Previous §3.1 | Retained in Chapter 0. Full prose/link fidelity review remains outstanding. |
| Chapter 0 §3.2 Governance Layers | Previous §3.3 | Moved and renumbered; current English anchor retained. |
| Chapter 1 §§1–4 | No equivalent in the former Preamble | Newly translated from the pinned current English source in all 19 locales. |
| Chapter 1 §5 Key Governance Processes | Previous §3.2 | Moved from Chapter 0 and renumbered. |
| Chapter 1 §§6–11 | Previous §§4–9 | Moved and renumbered; where the old locale source lacked current material, the missing current sections were newly translated. |

Old Chapter 1 Values and Principles material is Chapter 2 and is outside this pilot.

## Pair-by-pair draft status

Every row below has both current destination files in this folder. `Draft present` means a structural, AI-assisted translation draft exists; it does not certify fluent review, complete semantic fidelity, or publication readiness.

| Locale | Chapter 0 draft | Chapter 1 draft | Status |
| --- | --- | --- | --- |
| `ar` | Present | Present | Unreviewed; fidelity/link review required. |
| `bn` | Present | Present | Unreviewed; fidelity/link review required. |
| `es` | Present | Present | Unreviewed; fidelity/link review required. |
| `fa` | Present | Present | Unreviewed; fidelity/link review required. |
| `fr` | Present | Present | Unreviewed; fidelity/link review required. |
| `hi` | Present | Present | Unreviewed; fidelity/link review required. |
| `id` | Present | Present | Unreviewed; fidelity/link review required. |
| `ja` | Present | Present | Unreviewed; fidelity/link review required. |
| `ko` | Present | Present | Unreviewed; fidelity/link review required. |
| `mr` | Present | Present | Unreviewed; fidelity/link review required. |
| `pt` | Present | Present | Unreviewed; fidelity/link review required. |
| `ru` | Present | Present | Unreviewed; fidelity/link review required. |
| `ta` | Present | Present | Unreviewed; fidelity/link review required. |
| `te` | Present | Present | Unreviewed; fidelity/link review required. |
| `th` | Present | Present | Unreviewed; fidelity/link review required. |
| `tr` | Present | Present | Unreviewed; fidelity/link review required. |
| `ur` | Present | Present | Unreviewed; fidelity/link review required. |
| `vi` | Present | Present | Unreviewed; fidelity/link review required. |
| `zh` | Present | Present | Unreviewed; fidelity/link review required. |

## Checks completed

- All 38 locale/source draft files exist and record the source commit, edition, both source hashes, model, language variety, and unreviewed status.
- Each draft has one H1 and all current English HTML IDs, with no duplicate HTML IDs.
- All 19 Chapter 0 drafts contain current §§2.1–2.4, including the seven-row measurement-category table; the Japanese and Korean drafts now include the current complexity-orientation paragraph.
- All 19 Chapter 1 drafts contain §§1–11 and the current placement/Trace blocks. Chapters 1 §§1–4 were translated from the current source; sections that were absent from older locale material were newly translated.
- The old 2026.08.09 / 2026.10.21 Preamble widget pins and obsolete non-binding source wording were removed from the Chapter 0 drafts.
- `translations/` was not modified. No synchronization or independent fluent review is claimed.

## Resolved issues and remaining gate

AI subagents compared Chapter 1 §§5–11 in all 19 locale drafts against the pinned English source and repaired the identified source-coverage gaps. Repairs included current §§5–6 mappings, the seven-stage §8.2 chain, current owner registers in §§9–10, §11 corpus/subcore explanations, diagrams, anchors, localized chapter labels, and Mermaid formatting.

Destination-aware link checks covered all 38 draft files from their planned `translations/<locale>/` locations. Current targets and anchors were repaired where they had exact source-backed mappings. Where a current file was known but no unique heading matched, the stale fragment was removed and the verified file-level destination retained. Final checks report zero unresolved destination files and zero unmatched fragments. See the locale-specific reports:

- [`REVIEW_COVERAGE_AR_BN_ES_FA_FR_HI_CH01_SECTIONS_5_11.md`](REVIEW_COVERAGE_AR_BN_ES_FA_FR_HI_CH01_SECTIONS_5_11.md)
- [`REVIEW_B_ID_JA_KO_MR_PT_RU.md`](REVIEW_B_ID_JA_KO_MR_PT_RU.md)
- [`REVIEW_C_TA_TE_TH_TR_UR_VI_ZH.md`](REVIEW_C_TA_TE_TH_TR_UR_VI_ZH.md)
- [`REVIEW_LINK_MAPPING_AR_BN_ES_FA_FR_HI.md`](REVIEW_LINK_MAPPING_AR_BN_ES_FA_FR_HI.md)

The PT/MR/RU §8.1 stale splice was removed based on the English source history. Its four-seat disclaimer was retained under §7.1, matching the current English placement. PT’s documented splice ambiguity is resolved.

The translations are still AI-assisted drafts. Independent fluent-reader review of every passage in each pair is the remaining gate before synchronization; AI agents cannot provide that human review or attestation. Accordingly, `translations/`, locale READMEs, and review-status metadata were not changed.

## Remaining before synchronization

1. Obtain independent fluent-reader review for all 19 language pairs against the pinned English sources; resolve findings and record reviewer status.
2. Update locale README inventories, `translations/README.md`, and `translations/review_status.json` consistently, then synchronize only after the review gate is satisfied.
