# Markdown Details Widget Test

Purpose: quick local rendering test for collapsible trace blocks in Markdown preview.

Open this file in Markdown preview in Cursor or VS Code and test whether the `Trace` sections expand and collapse cleanly.

## Plain text baseline

This section should always render as normal Markdown text.

## Details test

<details>
<summary>Trace</summary>

- Definitions: Wellbeing; Materiality; Dependency; Foreseeability.
- Upstream: Principles: Wellbeing as the objective layer.<br>
  Downstream: Safety, Truth, and conflict rules.
- Articles: Read with the Chapter Nine rights floor where restrictions are justified by claimed wellbeing.

</details>

## Details test with emphasis

<details>
<summary><strong>Trace</strong></summary>

- Definitions: Harm; Risk; Epistemic Integrity; Necessity; Proportionality.
- Upstream: Principles: Non-negotiable constitutional constraints.<br>
  Downstream: Safety and Truth remain controlling limits.
- Articles: Most directly implicates Articles XIII, XIV, XXI, and XXII.

</details>

## Open-by-default test

<details open>
<summary>Trace (open by default)</summary>

- Definitions: Incentive Alignment (Constitutional); Proxy Divergence.
- Upstream: Principles: Constitutional value protection.<br>
  Downstream: Incentives must not undermine constitutional values.
- Articles: Most directly implicates Articles IX, XI, XII-D, XIII, and XXI.

</details>

## Interpretation notes

What we want:
- the summary line is visible when collapsed,
- clicking the summary expands and collapses the block,
- bullets inside the block render normally,
- wrapped prefix lines under a bullet still read cleanly,
- surrounding headings and spacing still look clean.

Failure modes to watch for:
- raw HTML shown literally,
- block refuses to collapse,
- spacing looks broken,
- preview strips content entirely.
