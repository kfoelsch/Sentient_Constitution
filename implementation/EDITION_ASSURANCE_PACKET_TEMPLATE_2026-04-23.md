# Edition assurance and change-control packet (template)

**Status:** process template (non-authoritative).  
**Use:** corpus edition cuts, adoption assurance, and controlled-change review.

## 1. Edition identity

| Field | Value |
| --- | --- |
| Edition label | (e.g. `SC-Corpus-2026.04.31`) |
| Effective date | (YYYY-MM-DD) |
| Authority basis | (instrument, board resolution, custody record ref) |

## 2. Changed files and scope

- List each `core_*.md` / `corpus_*.md` file touched with one-line substance summary.
- Adoption-scope note: what remains in force for non-adopters vs adopters (Chapter Fourteen framing).

## 3. Validity and non-regression checklist

- [ ] Chapters Eleven–Thirteen validity / non-regression checks satisfied for the change class
- [ ] No silent companion-file drift outside adoption chain
- [ ] Chapter Six / Seven classification routing unchanged in meaning where not intentionally amended

## 4. Custody and evidence

- Adoption chain identifier(s)
- Dated artifact location (`evidence/<YYYY-MM-DD>/` or adopter store)
- Custody sign-off (roles)

## 5. Audits and drills

| Audit / drill | Result | Notes (incl. deferred, suspended, pre-existing failures) |
| --- | --- | --- |
| `make regression` | | |
| `make regression-full` | | |
| Other | | |

## 6. Unresolved control exceptions

List accepted risks, waivers, or follow-up tickets with owner and target date.

## 7. Assurance debt

| Item | Priority | Next review |

## 8. Exemplar filled packet

A fully worked example should be filed after the regression catalog and evidence tree are live again; until then, use sections 1–7 for manual assurance review.
