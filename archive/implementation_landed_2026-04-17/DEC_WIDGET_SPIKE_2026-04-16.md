# D/E/C Widget Spike (2026-04-16)

> **Status (2026-04-16 EOD): superseded by live rollout.** The widget design prototyped below was approved and rolled out the same day across `core_05-05_definitions_a_independent.md` (Phase 0 anchors) and the five consumer files (`core_00-01_principles.md`, `core_09-09_rights_part_a..d.md` — 94 mechanical conversions). Live rules now live in `doc_architecture.md` rule 12 and the dated **2026-04-16, D/E/C split** architecture note. Implementation tooling: `tools/add_oec_anchors.py`, `tools/convert_definitions_to_dec_widget.py`, `tools/verify_dec_anchors.py`. Pre-conversion backups: `implementation/dec_rollout_backup_2026-04-16/`. This file is retained as the design record; do not edit further.

Purpose: prototype the **per-section Definitions · Evaluation · Compliance (D/E/C) widget**, which surfaces the defined concepts materially invoked by a given operative section and lets the reader jump directly to that concept's **O**, **E**, or **C** line in `core_05-05_definitions_a_independent.md`. This file is a rendering test only; it is non-operative and does not modify any core constitutional file.

## Design the spike is testing

- The widget lives **only next to consuming sections** — principles, rights articles, compliance, governance, courts, and so on — never inside `core_05-05_definitions_a_independent.md` itself.
- It is **per-section**, scoped to exactly the defined concepts that section invokes. Sections that invoke no defined concepts get no widget.
- There is **no** chapter-wide or global index.
- Row shape is `Concept · O · E · C`, all four live. The concept name and **O** target the same anchor (the concept's heading in Chapter Five); **E** and **C** target `...-e` and `...-c` anchors under that concept. The redundant **O** link is kept so the triad reads symmetric on the page.
- **Single-concept degradation rule:** if a section invokes exactly one defined concept, the collapsible widget is dropped and replaced with a single inline line of the same row shape, prefixed by a bold-blue **Definition:** label so the navigational metadata is visually keyed to the widget summaries (for example, **Definition:** `Foreseeability · O · E · C`). Note the singular "Definition:" here versus the plural "Definitions" in the widget summary title — the prefix agrees with the count. The widget only materializes when two or more concepts are invoked.
- Consistent with Chapter Four's Definition Traceability Requirement: tracing is surfaced at the point of invocation, where that requirement already lives doctrinally.

## Spike self-containment

In a real rollout the widget's jumps go cross-file into `core_05-05_definitions_a_independent.md`. For the spike, target stubs are included near the bottom of this file so every jump resolves inside the spike and the click-through can be exercised end-to-end without touching any core file.

---

## Case 1 — Greenfield: section has no existing Trace widget

The passage below is taken verbatim from `core_00-01_principles.md` §6.1.4 (Minimization of Avoidable Burden). That subsection does not currently carry a Trace widget. The new D/E/C widget is attached directly.

##### 6.1.4 Minimization of Avoidable Burden

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Avoidable Burden](#avoidable-burden) · [O](#avoidable-burden) · [E](#avoidable-burden-e) · [C](#avoidable-burden-c)
- [Proportionality](#proportionality) · [O](#proportionality) · [E](#proportionality-e) · [C](#proportionality-c)
- [Necessity](#necessity) · [O](#necessity) · [E](#necessity-e) · [C](#necessity-c)
- [Safety (Constraint)](#safety-constraint) · [O](#safety-constraint) · [E](#safety-constraint-e) · [C](#safety-constraint-c)
- [Truth (Constitutional Constraint)](#truth-constitutional-constraint) · [O](#truth-constitutional-constraint) · [E](#truth-constitutional-constraint-e) · [C](#truth-constitutional-constraint-c)

</details>

<br>

Where multiple options satisfy Safety, Truth, the rights floor in **Chapter Nine**, sections 6.1.1 through 6.1.3, and the other applicable constraints in this Constitution, systems must prefer the option that imposes the **least avoidable burden** on sentient time, attention, effort, and shared resources.

For this subsection:
- **Avoidable burden** is process, compliance, coordination, or implementation cost that is not traceable to a constitutional outcome under **Proportionality** and **Necessity**, and whose imposition is not required by a rights-floor protection, Safety, or Truth obligation.
- Ordinary transaction costs, costs required by proportionate audit, contestability, or due-process guarantees, and costs required by rights-protective process are **not** avoidable burden for this subsection.

---

## Case 2 — Transformation: section already has a Trace widget with a `Definitions:` line

The passage below is taken verbatim from `core_00-01_principles.md` §6.2.1 (Preservation of Epistemic Integrity). It currently carries a Trace widget whose final bullet is `Definitions: Epistemic Integrity; Truth (Constitutional Constraint); Materiality; Foreseeability; Necessity; Proportionality.` Under the proposed design, that bullet is extracted into the new D/E/C widget and Trace keeps only its principle / article / upstream / downstream pointers.

##### 6.2.1 Preservation of Epistemic Integrity

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: Principles: 3.1 Safety, 3.2 Truth, 4. Trust, and 6. Interaction and Conflict Resolution.
- Downstream: 6.2.2 Trust-Truth Alignment and 8. Prohibition on Absolute Override.
- Downstream: Protects the rights surface for info-sphere integrity, auditability, retrospective review, and informed contestability when disclosure is limited; especially Article XIII, Article XIV, Article XXI, and Article XXII-E, plus any rights context where disclosure limits affect contestability or informed participation.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Epistemic Integrity](#epistemic-integrity) · [O](#epistemic-integrity) · [E](#epistemic-integrity-e) · [C](#epistemic-integrity-c)
- [Truth (Constitutional Constraint)](#truth-constitutional-constraint) · [O](#truth-constitutional-constraint) · [E](#truth-constitutional-constraint-e) · [C](#truth-constitutional-constraint-c)
- [Materiality](#materiality) · [O](#materiality) · [E](#materiality-e) · [C](#materiality-c)
- [Foreseeability](#foreseeability) · [O](#foreseeability) · [E](#foreseeability-e) · [C](#foreseeability-c)
- [Necessity](#necessity) · [O](#necessity) · [E](#necessity-e) · [C](#necessity-c)
- [Proportionality](#proportionality) · [O](#proportionality) · [E](#proportionality-e) · [C](#proportionality-c)

</details>

<br>

Truth must not be suppressed or distorted except where:
- its disclosure would directly and materially enable imminent or reasonably foreseeable harm, including systemic or cascading risk
- no less-restrictive mitigation is available

Such restrictions must be:
- narrowly scoped
- time-limited
- subject to audit and review

Where transparency conflicts with Safety constraints, disclosure must be limited in accordance with the above while preserving maximum possible epistemic integrity.

All restrictions on disclosure must include provisions for retrospective audit and, where feasible, eventual disclosure once the conditions justifying restriction no longer apply.

---

## Case 3 — Single-concept degraded form: inline line, no widget

When a section invokes exactly one defined concept, the collapsible widget is overkill. Replace it with a single inline line of the same row shape, prefixed by a bold-blue **Definition:** label so the line reads as navigational metadata keyed to the widget summaries used elsewhere. Note the singular "Definition:" here — the prefix agrees with the single concept. The illustrative passage below is synthetic — just enough text to show the line in context — because genuine single-concept sections are rare and deserve a deliberate rollout pick.

##### Illustrative subsection title

<strong><span style="color: #2563eb;">Definition:</span></strong> [Foreseeability](#foreseeability) · [O](#foreseeability) · [E](#foreseeability-e) · [C](#foreseeability-c)

<br>

Systems must account for foreseeable consequences, including delayed and aggregate effects, when evaluating permissible action under this section.

---

## What to look for

- **Is the stacked pair clean?** In Case 2 the section now carries two blue `<details>` blocks back-to-back. Does that read as orderly or heavy? If heavy, option is to merge: one blue widget with two summary sections inside, or keep Trace and add the D/E/C list as a second bullet group.
- **Is the greenfield widget (Case 1) justified on sections that have no Trace?** Or should the widget only appear where a section is dense enough to have warranted a Trace in the first place? Principled answer: the widget should follow the invocation pattern, not the Trace pattern — i.e., any section that materially invokes two or more defined concepts.
- **Does the single-concept inline form (Case 3) read cleanly with the bold-blue "Definition:" prefix?** The prefix keys the line to the widget summaries used elsewhere and carries the singular/plural distinction (singular "Definition:" for one concept, plural "Definitions" in the multi-concept widget title).
- **Is the `Concept · O · E · C` separator readable?** Alternatives: `Concept [O] [E] [C]`, `Concept — O / E / C`, `Concept (O, E, C)`.
- **Is the redundant O link valuable?** The concept name and O both jump to the same target. Reading §6.1.4, §6.2.1, and the Case 3 line above, does the visible `O` pull its weight, or does the repetition feel like clutter?

## Rollout checklist (not executed in this spike)

1. Add `<a id="...-e">` and `<a id="...-c">` anchors next to every E and C bullet in `core_05-05_definitions_a_independent.md`. The heading anchor already serves as the O target.
2. Scope the widget's use in `doc_architecture.md`: per-section only, only on sections that materially invoke two or more Chapter Five defined concepts, never inside Chapter Five itself. Record the single-concept degradation rule (one invocation → inline line, no collapsible widget).
3. Attach the widget to consuming sections in an agreed order (candidates: Chapter One principles sections already carrying a `Definitions:` line; Chapter Six compliance; Chapter Nine rights articles; Chapter Ten governance; Chapter Eight courts).
4. Where a section currently has a Trace widget with a `Definitions: ...` line, remove that line from Trace and move its content into the new D/E/C widget.
5. Extend `make reference-audit` (or a sibling check) to verify that every D/E/C widget row — and every single-concept inline line — resolves to live `...`, `...-e`, `...-c` anchors in Chapter Five.
6. Log in `MEMLOG.md`; reflect in `TODO.md`.

---

## Chapter Five target stubs (spike only)

These stubs exist so the links above resolve inside this single file. In the real rollout all these targets live in `core_05-05_definitions_a_independent.md` and are cross-file jumps; no stubs are added anywhere.

<a id="avoidable-burden"></a>
### Avoidable Burden (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="avoidable-burden-e"></a>**E:** stub anchor for spike navigation.
- <a id="avoidable-burden-c"></a>**C:** stub anchor for spike navigation.

<a id="proportionality"></a>
### Proportionality (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="proportionality-e"></a>**E:** stub anchor for spike navigation.
- <a id="proportionality-c"></a>**C:** stub anchor for spike navigation.

<a id="necessity"></a>
### Necessity (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="necessity-e"></a>**E:** stub anchor for spike navigation.
- <a id="necessity-c"></a>**C:** stub anchor for spike navigation.

<a id="safety-constraint"></a>
### Safety (Constraint) (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="safety-constraint-e"></a>**E:** stub anchor for spike navigation.
- <a id="safety-constraint-c"></a>**C:** stub anchor for spike navigation.

<a id="truth-constitutional-constraint"></a>
### Truth (Constitutional Constraint) (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="truth-constitutional-constraint-e"></a>**E:** stub anchor for spike navigation.
- <a id="truth-constitutional-constraint-c"></a>**C:** stub anchor for spike navigation.

<a id="epistemic-integrity"></a>
### Epistemic Integrity (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="epistemic-integrity-e"></a>**E:** stub anchor for spike navigation.
- <a id="epistemic-integrity-c"></a>**C:** stub anchor for spike navigation.

<a id="materiality"></a>
### Materiality (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="materiality-e"></a>**E:** stub anchor for spike navigation.
- <a id="materiality-c"></a>**C:** stub anchor for spike navigation.

<a id="foreseeability"></a>
### Foreseeability (stub)

- **O (heading target):** see Chapter Five entry.
- <a id="foreseeability-e"></a>**E:** stub anchor for spike navigation.
- <a id="foreseeability-c"></a>**C:** stub anchor for spike navigation.
