# Sibling audit modes: one owner map (2026-10-07)

## Problem

The Chapter 5 definition of System Alignment Certification, the Article XVI neighbors note, and Chapter 8 Part A §1 each listed "sibling audit modes" in different words ("complexity and stewardship audits", "claim verification", "continuous-audit pathways"). Only the CJS-3.3 owner map named owners, and it had no row for stewardship audits or continuous audit. Part A §1 also said certification "draws on" the modes, while Chapter 5 says it "does not absorb or replace" them.

## Decision

No new Chapter 5 definitions. Each mode keeps one operative home, named in the CJS-3.3 owner map, and the three lists use the same names and point to that map.

| Mode (list name) | Owner |
|---|---|
| System Data Types Record audits | CS-2 §8.3 (unchanged) |
| System Classification Record audits | CS-3 §7.3 (unchanged) |
| Steward assurance reviews (new name) | CS-4.8, CS-4.11 |
| Continuous audit (systems layer) | CS-5 ACA |
| Complexity audits | CS-6.3, Article XXIII-B; steward organization under CS-4.5 |
| Claim verification | CJS-3.5, Article XVI-C |

The mode lists are ordered by owner section number (CS-2, CS-3, CS-4, CS-5, CS-6, then CJS-3.5).

"Stewardship audits" had two readings. Complexity stewardship is the complexity audit. Steward conduct and governance had no mode name, so CS-4 now names it "steward assurance review."

## Changes

- CJS-3.3 owner map: rows added for steward assurance review and continuous audit; complexity and claim rows named to their operative homes. Continuous audit of eligibility criteria and restriction review (Articles XIX-B, XIX-C) is stated as a separate Rights Floor practice.
- CS-6.3: complexity audit scaling by class (taken from the CS-3 Application Profile row), triggers, and output. This resolves CS-4's reference to "Class A audits under CS-6," which had no cadence to point to.
- CS-5 (ACA): "ACA as an audit mode" paragraph. Monitoring alone is not a complete audit; ACA and certification do not replace each other; ACA output may be offered as evidence for the §7.2.1 monitoring indicators.
- CS-4.11: "Steward assurance review" paragraph naming the mode from checks that already exist.
- Chapter 5 SAC definition, Article XVI neighbors, Chapter 8 Part A §1: common names, pointer to the owner map. Part A §1 now says certification "may integrate the results of" the modes and does not absorb or replace them.

## Verification

- `make -k regression`: the same five targets fail as before this change (`ch5-measurement-coverage-audit`, `corpus-markdown-audit`, `prose-continuity-audit`, `lexical-vocabulary-audit`, `ai-manifest-validate`), with no new findings after one rewording (a bare "drift" in the CS-5 paragraph).
- Obligation inventory over the seven touched files: no clause lost. Additions are the new CS-6 scaling and output duties, the CS-5 ACA paragraph, and the reworded Part A §1 sentence.
- Regenerated: `plain_terms_edition.*`, `boundary_chunks.json`, reader-accessibility files.

## Open items

- `ai-manifest-validate` was already failing; its stale list now also includes `ai_corpus/indexes/definition_registry.json` because the Chapter 5 definition text changed. `make ai-corpus-sync` clears all of it.
- Translations still carry the old list wording until the translation restart.
- The new CS-6 class cadence restates the CS-3 profile row. If an adopted instrument sets numeric cadences, they belong there, not in CS-6.
