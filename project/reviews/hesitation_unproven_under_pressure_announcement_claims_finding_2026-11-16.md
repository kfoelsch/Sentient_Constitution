# Finding record: "Unproven under pressure", announcement claims audit — 2026-11-16

This page is **process support**, not constitutional text. It cannot change or narrow any numbered `core_*` file, and it edits no announcement copy. It is the record for the hesitation *Unproven under pressure* in [TODO.md](../../TODO.md), following the method in the [identification plan](../plans/evaluation_hesitations_identification_2026-11-15.md) (§2: audit the announcement copy line by line and mark each claim as evidenced, designed, or aspirational).

## 1. Question and pass condition

**Question.** Does each claim in the announcement copy ([ANNOUNCEMENT.md §1](../../implementation/adoption/ANNOUNCEMENT.md#1-the-announcement)) and its say / do-not-say table (§2) say no more than the corpus and the evidence support?

**Pass.** Every claim is one of: **evidenced** (the text or a record shows it now), **designed** (the core requires it, but no adopter or human operator has run it), or **aspirational** (not yet backed). A "designed" claim passes if the copy says "designed" or "requires", not "does" or "is". Nothing aspirational appears as fact.

## 2. Sources read

[ANNOUNCEMENT.md](../../implementation/adoption/ANNOUNCEMENT.md) in full; [VISION §2](../VISION.md#where-it-stands); the Preamble Two Fundamental Questions; Chapter One §17.1; Chapter Fifteen (record kinds, no-offset bridge); Chapter Twenty (final effect); Chapter Twenty-Five §2 (clocks); Chapter Twenty-Eight §5.1 (voting); Chapter Eleven (expiry, recertification); `ai_corpus/indexes/definition_registry.json`; [evaluation/results/](../../evaluation/results/). Not done: the independent cold-reader step (plan step 4).

## 3. Claim-by-claim result

| # | Claim (announcement §1 unless noted) | Class | Basis | Wording risk |
|---|---|---|---|---|
| 1 | "a draft model constitution", pre-release, edition pinned | Evidenced | README, edition file | None |
| 2 | Four duties that "grow with how much is at stake" | Designed | Preamble; Chapter Five legs; materiality tiers in Chapter Twenty-Five §2 | Present tense is fine for a description of the text |
| 3 | Human and AI stewards "are held to the same standard" | Designed | Chapter One §17.1 ("anti-special-pleading rule") | **Overstated.** No adopter exists, and [VISION §2](../VISION.md#where-it-stands) says the shared-standard claim is untested with human operators. "Must be held to" or "are to be held to" is accurate. |
| 4 | The two questions, quoted | Evidenced | Preamble lines match word for word | None |
| 5 | Defines "every term it relies on — more than two hundred — once, in one place" | Designed, audited | `definition_registry.json` counts **310** definitions; single-home audits run in `make regression` | **Understated.** "More than two hundred" is true but stale; "more than three hundred" matches the registry. Do not freeze a figure that the registry moves. |
| 6 | Certification: independent forum, scaled to impact, written down, time-limited, repeated on a risk schedule | Designed | Chapters Nine to Eleven (expiry, recertification due date, midpoint audit) | Passes as a description. Only AI sittings exist, so no "has been shown to work" wording may be added. |
| 7 | Standing records: verified help and verified harm kept as separate entries, "so neither erases the other" | Evidenced in text | Chapter Fifteen §3.1 and §3.4 (no-offset bridge); schema split into separate snapshots (556th move) | None |
| 8 | "Consequences follow from the record, not from reputation or a popularity score" | Designed | Chapter Twenty bars a merged score or reputation label; Chapter Eighteen bars reputation substitution | The adopter-reach limit applies: it binds only a body that adopts. |
| 9 | Contestability: challenge, independent review, correction "within set time limits" | Designed, evidenced | Chapter Twenty-Five §2: tier outer bounds of 7, 14, 30, 60 and 90 days | None |
| 10 | "The core text … is the binding source and the most complete part" | Evidenced | VISION §2 | The core is now 50 files and about 545,000 words (see §4 below) |
| 11 | "What it is not" block: not law, not adoption, no supersession, binds no outsider | Evidenced | Chapters Thirty-One §6 and Thirty-One §4 | None |
| 12 | Open questions: one entry, who counts as one voter (one year in residence, own memory and choices means own sentient, creator who sustains many has made that many voters) | Evidenced | Chapter Twenty-Eight §5.1 residence period of one continuous year, with branch and merge dates; Chapter Five *Sentient* | None |
| 13 | §2 row: "Describe the working parts … as verified, written down, time-limited, and challengeable" | Designed | Same as 6, 7 and 9 | Fine, because the same row says "No adopter has run them yet" |
| 14 | §2 row: "AI handoff trials remain open" | Evidenced | [PRE_PUBLICATION_SPEC §6.5](../../implementation/PRE_PUBLICATION_SPEC.md) | None |

**Result.** No aspirational claim presented as fact. Two wording points (rows 3 and 5), both small. The copy's strongest protection is already in place: the say / do-not-say table forbids "Simple, proven, and effective."

## 4. A stale figure found on the way

The **Scale against comprehensibility** item in `TODO.md` says the core runs to about 300,000 words. The current count (`core_*.md`, 50 files) is **544,568 words**. The figure comes from [VISION §2](../VISION.md#where-it-stands), which is dated 2026-09-09 and says 36 files and about 300,000 words. The companion layers have grown the same way (word counts today):

| Layer | Files | Words | VISION §2 (2026-09-09) |
|---|---|---|---|
| Core (`core_*`) | 50 | 544,568 | 36 files, ~300k |
| Joint structure (CJS) | 15 | 88,778 | 14 files, ~66k |
| Systems (CS) | 18 | 86,332 | 15 files, ~50k |
| Institutions (CI) | 28 | 58,400 | 27 files, ~34k |
| Forum (CF) | 17 | 50,471 | 17 files, ~36k |

The whole binding-plus-companion corpus is about 830,000 words. This sharpens the comprehensibility question: Article XXIII promises that affected sentients can understand what governs them, and the corpus is close to three times the size of the figure the TODO assumed. VISION §2 is a dated statement, so it is not wrong for its date, and is left as it is.

## 5. Classification

**Mostly handled; two wording points; the open-questions block is incomplete by design.** The announcement already states the lack of adopters and operator results, and the §2 table backs it. What stays open is the invitation half of the item: entries for the other hesitations.

Open-questions block status:

- Who counts as one voter: **in** (534th move).
- Derived sentients and AI correction: **not yet in**. Draft wording is in [that finding record, decision 5](hesitation_derived_sentients_ai_correction_finding_2026-11-15.md); it depends on decisions 2 to 6 there.
- Standing records: **not yet in**. Decision 8 in [that finding record](hesitation_standing_records_measurement_infrastructure_finding_2026-11-15.md) is open.
- Entrenched policy: **no entry**, custodian decision 2026-11-15 ([project/SHELVED.md](../SHELVED.md)).
- Scale against comprehensibility: not started, and it is the natural entry that this finding sharpens.

## 6. Decisions for the custodian

1. **Row 3 wording. Decided and entered 2026-11-16 (571st move, custodian):** "must be held to the same standard" in the §1 copy (v0.8). The same sentence in README.md line 43 ("are held to the same standard") was not changed; the custodian has not been asked.
2. **Row 5 wording. Decided and entered 2026-11-16 (571st move, custodian):** "more than three hundred" (v0.8).
3. **Comprehensibility. Decided and entered 2026-11-16 (570th move, custodian):** the announcement does not state the size of the text, because it will be obvious on reading. It gains a "Why it is this thorough" paragraph instead: the Constitution takes on hard questions humanity faces sooner rather than later and prefers comprehensive solutions to gestures at possible ones. The adaptation adds that a comprehensive answer is testable and challengeable, not settled, and points to the Open questions block, so the paragraph does not conflict with the say / do-not-say row "Every hard case is solved." For the custodian to confirm or strike.
4. **Open-questions entries. Decided and entered 2026-11-16 (572nd move, custodian):** two entries added (derived sentients in the revised form; cross-adopter records), none for comprehensibility. Block status in §5 above is now: voter, derived sentients and standing records in; entrenched policy no entry; scale covered by the "Why it is this thorough" paragraph.

## 7. Not done

- The independent read (a fresh session on another model family and one human reader, plan step 4) for this audit.
- The cold-reader test for *Scale against comprehensibility*: three readers, the 15-minute path, five questions.
