---
name: Proposal
about: Propose adopted implementation maturation work (Lane C), a core text change (Lane D), or a new gate or tool (Lane E)
title: "[Proposal] "
labels: ["proposal"]
---

<!-- CONTRIBUTING.md § Lanes C, D, E. Open this BEFORE a pull request for Lane C and D work.
     For Lane D this is the repository's notice-and-contest step: the proposal stays open long enough for others to object. -->

## Lane

- [ ] C — Adopted implementation maturation (CS / CI / CF / CJS / Remedy / Emergency)
- [ ] D — Core text change (numbered `core_*` file)
- [ ] E — Tooling and audits

## Target

- File(s) / stack:
- Section(s) / anchor(s):
- Open item advanced (`implementation/PRE_PUBLICATION_SPEC.md` §4.2, §4.3, or §5 step):
- Edition pin: `SC-Corpus-2026.11.25`

## Problem

<!-- What is wrong or missing today. Cite the passage. For Lane D: show a conflict, a gap, a Rights-Floor hole, or a failed apply-test — not a preference of phrasing. -->

## Proposed change

<!-- What the text or tool will say or do after. Keep meaning changes explicit. -->

## What is NOT changing

<!-- Owner home, Chapter Three definitions, boxed operative steward statements, edition label. -->

## Owner routing

<!-- Chapter Two principle(s) and Chapter Three definition(s) this text answers to. Downstream files that cite the section. -->

## Lane D — Substantive Test 1 non-regression self-check

<!-- Delete unless Lane D. Confirm the change does not weaken Chapter Two constraints, Subcore 3-A to 3-C integrity, the Chapter Four Rights Floor, or Chapter Twenty-Seven legitimacy — including indirect narrowing through definitions, standing gates, evidence rules, or emergency labels (core_22.000_non_regression.md § Substantive Test 1). -->

## Gates you expect to run

- [ ] `make regression`
- [ ] `make readability-audit`
- [ ] `make obligation-snapshot` / `make obligation-diff` (Lane C rewrites and all Lane D)
- [ ] `make steward-door-lockstep-audit` (Lane D)
- [ ] Alignment audit(s):
- [ ] New `test_*.py` (Lane E)

## Attribution

<!-- human — <handle>  |  AI agent (<model>) directed by human — <handle> -->
