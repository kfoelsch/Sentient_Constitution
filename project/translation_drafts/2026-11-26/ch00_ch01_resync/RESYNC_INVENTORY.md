# Chapters 0–1 translation resynchronization inventory

**Status:** AI-assisted draft set exists for all 38 locale/source pairs. The documented Chapter 1 coverage gaps were repaired against the pinned English source; the drafts remain unreviewed by fluent readers and unsynchronized.

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

## Coverage repair and remaining gates

AI subagents compared Chapter 1 §§5–11 in all 19 locale drafts against the pinned English source and repaired the identified source-coverage gaps. Repairs included current §§5–6 mappings, the seven-stage §8.2 chain, current owner registers in §§9–10, the §11 corpus/subcore explanation, diagram and anchor corrections, localized chapter labels, and Mermaid fence repairs. A second coverage pass caught additional stale §8 framing and missing chart content; those items were also corrected. Locale-specific changes and checks are recorded in:

- [`REVIEW_COVERAGE_AR_BN_ES_FA_FR_HI_CH01_SECTIONS_5_11.md`](REVIEW_COVERAGE_AR_BN_ES_FA_FR_HI_CH01_SECTIONS_5_11.md)
- [`REVIEW_B_ID_JA_KO_MR_PT_RU.md`](REVIEW_B_ID_JA_KO_MR_PT_RU.md)
- [`REVIEW_C_TA_TE_TH_TR_UR_VI_ZH.md`](REVIEW_C_TA_TE_TH_TR_UR_VI_ZH.md)
- [`REVIEW_LINK_MAPPING_AR_BN_ES_FA_FR_HI.md`](REVIEW_LINK_MAPPING_AR_BN_ES_FA_FR_HI.md)

These checks establish source coverage and structure only. The translations are still AI-assisted drafts; independent fluent-reader review and meaning-sensitive review remain required before synchronization. PT retains ambiguous legacy §8 material whose disposition was not source-clear. Historical cross-file link and fragment mappings remain unresolved in the link-review notes and need destination-aware audit/reconciliation before the drafts can be copied into `translations/`.

The synchronization plan requires independent fluent review of every passage in each pair, glossary decisions, destination-context link checks, and consistent README/review metadata. Accordingly, `translations/`, locale READMEs, and review-status metadata were not changed.

## Remaining before synchronization

1. Resolve PT's ambiguous legacy §8 material with the custodian; do not remove or merge it by inference.
2. Resolve historical link and fragment destinations against current English and locale mappings, then run the translation link audit in final destination context.
3. Obtain independent fluent-reader review for all 19 language pairs against the pinned English sources; resolve findings and record reviewer status.
4. Update locale README inventories, `translations/README.md`, and `translations/review_status.json` consistently, then synchronize only after all gates are satisfied.
