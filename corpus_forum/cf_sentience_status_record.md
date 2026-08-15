# Sentience-Status Adjudication Record (implementation protocol)

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations in this file or elsewhere.
>
> This file is **designated implementation text** for the [Sentience-Status Adjudication Record](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional) format. It is binding incorporated implementation text where enumerated under [Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the Sentient Constitution and does not override or narrow it. It implements, and does **not** narrow, [Article V-E](../core_06-06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor) (*Sentience-Status Adjudication Floor*).
>
> Machine-checkable form: [`implementation/schemas/sentience_status_adjudication_record.schema.json`](../implementation/schemas/sentience_status_adjudication_record.schema.json). Start at the [Forums landing page](../corpus_forum.md) for the numbered CF families; this file is the dedicated record-format protocol, not a CF family replacement.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Article V-E](../core_06-06_rights_part_b.md#article-v-e-sentience-status-adjudication-floor) (*Sentience-Status Adjudication Floor*); [Sentience-Status Adjudication Record](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional) (Def.P1); [Chapter Eleven §5](../core_11-11_forum.md#5-escalation-and-certification) (*Sentience-status adjudication* hook); [Chapter Sixteen](../core_16-16_incorporation.md#chapter-sixteen-incorporation-bridge) incorporation discipline.
- Downstream: [`implementation/schemas/sentience_status_adjudication_record.schema.json`](../implementation/schemas/sentience_status_adjudication_record.schema.json).
- Read with: [Sentience Status Adjudication](../core_05_band_participation.md#sentience-status-adjudication-constitutional); [Contested-Sentient Life](../core_05_band_participation.md#contested-sentient-life-constitutional); [Chapter Eleven §5](../core_11-11_forum.md#5-escalation-and-certification); **CF-15** (*Standard records, forms, and evidence artifacts*) — appointments and filing forms stay out of this file.
- Topic routing (mandatory read-with): **CJS-R12** (*Standard forum records, forms, and evidence artifacts*) in **CJS-0.1** (*Topic router*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Assessment · Compliance</span></strong></summary>

- [Sentience-Status Adjudication Record](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional) · [O](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional) · [M](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional-a) · [A](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional-a) · [C](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional-c)
- [Contested-Sentient Life](../core_05_band_participation.md#contested-sentient-life-constitutional) · [O](../core_05_band_participation.md#contested-sentient-life-constitutional) · [M](../core_05_band_participation.md#contested-sentient-life-constitutional-a) · [A](../core_05_band_participation.md#contested-sentient-life-constitutional-a) · [C](../core_05_band_participation.md#contested-sentient-life-constitutional-c)
- [Forum Family, Technical](../core_05_band_accountability.md#forum-family-technical) · [O](../core_05_band_accountability.md#forum-family-technical) · [M](../core_05_band_accountability.md#forum-family-technical-a) · [A](../core_05_band_accountability.md#forum-family-technical-a) · [C](../core_05_band_accountability.md#forum-family-technical-c)
- [Contestability](../core_05_band_accountability.md#contestability) · [O](../core_05_band_accountability.md#contestability) · [M](../core_05_band_accountability.md#contestability-a) · [A](../core_05_band_accountability.md#contestability-a) · [C](../core_05_band_accountability.md#contestability-c)
- [Auditability](../core_05_band_oversight.md#auditability) · [O](../core_05_band_oversight.md#auditability) · [M](../core_05_band_oversight.md#auditability-a) · [A](../core_05_band_oversight.md#auditability-a) · [C](../core_05_band_oversight.md#auditability-c)
- [Standing Record](../core_05_band_accountability.md#standing-record-chapter-six) · [O](../core_05_band_accountability.md#standing-record-chapter-six) · [M](../core_05_band_accountability.md#standing-record-chapter-six-a) · [A](../core_05_band_accountability.md#standing-record-chapter-six-a) · [C](../core_05_band_accountability.md#standing-record-chapter-six-c)
- [Forum Case Record](../core_05_band_accountability.md#forum-case-record) · [O](../core_05_band_accountability.md#forum-case-record) · [M](../core_05_band_accountability.md#forum-case-record-a) · [A](../core_05_band_accountability.md#forum-case-record-a) · [C](../core_05_band_accountability.md#forum-case-record-c)

</details>

<br>

This file is the designated implementation text for the [Sentience-Status Adjudication Record](../core_05_band_participation.md#sentience-status-adjudication-record-constitutional) format.

*In plain terms: this is the inspectable status-file format — who or what was reviewed, what status was found or left contested, on what evidence, under which forum route, with what end-dates or review triggers, and how the case can be reopened. It does not decide who counts, and it is not a standing record.*

This protocol implements, and does **not** narrow, **Article V-E** (*Sentience-Status Adjudication Floor*). The Rights Floor remains in Chapter Six. Process meaning remains in Chapter Five. Venue and minimum fields remain in the [Chapter Eleven §5](../core_11-11_forum.md#5-escalation-and-certification) (*Sentience-status adjudication* hook).

**Record format.** Machine-checkable form: [`implementation/schemas/sentience_status_adjudication_record.schema.json`](../implementation/schemas/sentience_status_adjudication_record.schema.json). That schema is validating form, **not** who-counts and **not** a [Standing Record](../core_05_band_accountability.md#standing-record-chapter-six).

When [Sentience Status Adjudication](../core_05_band_participation.md#sentience-status-adjudication-constitutional) runs, the record must state at least:

- the subject entity;
- the status determination or live contested posture (including affirmed, narrowed, revoked, restored, or still contested);
- the lead forum family and any Chapter Eleven–warranted special route;
- the indicators and expert evidence relied on, with material uncertainty noted;
- interim [Contested-Sentient Life](../core_05_band_participation.md#contested-sentient-life-constitutional) treatment while status remains live;
- any narrowing's declared expected-closure timeline and mandatory periodic-review trigger; and
- the reopening evidence standard — new verified evidence, not calendar-only reopening.

**Out of scope.** This file does **not**:

- decide who counts as a sentient;
- open, update, or substitute for a [Standing Record](../core_05_band_accountability.md#standing-record-chapter-six) or standing measurement;
- replace the whole [Forum Case Record](../core_05_band_accountability.md#forum-case-record); or
- hold appointments schedules, filing-form libraries, or sequencing manuals — those stay out of this file.
