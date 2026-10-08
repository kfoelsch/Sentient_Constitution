# Chapter Eight: certification status vocabulary (2026-10-08)

Decision (editor): the outcome statuses of Chapter Eight are **Full Certification**, **Provisional Certification** and **Not Certified**. "Recognition" no longer names a certification status.

## Vocabulary map

| Before | After |
|--------|-------|
| provisional recognition | Provisional Certification |
| full recognition | Full Certification |
| conditional recognition | conditional certification (an overlay on either status, as before) |
| deferred recognition | deferred certification |
| non-recognition | non-certification |
| deferral, refusal, withdrawal, expiration (no status held) | **Not Certified** (new umbrella term, defined in Part B §5) |
| recognized system / recognized scope | certified system / certified scope |
| official constitutional alignment recognition | official constitutional alignment certification |
| "No go-live before recognition" | "No go-live before certification" |

## Renamed headings, anchors and titles

| Item | Old | New |
|------|-----|-----|
| Part B §7.2 heading and anchor | Provisional and full recognition (`#72-provisional-and-full-recognition`) | Provisional and full certification (`#72-provisional-and-full-certification`) |
| Chapter Five definitions | Full Recognition, Provisional Recognition (`#full-recognition`, `#provisional-recognition`, and their `-a` / `-c` entry ids) | Full Certification, Provisional Certification (`#full-certification`, `#provisional-certification`, `-a` / `-c`) |
| CF-7.2 | Constitutional alignment recognition and review (`#cf-72-constitutional-alignment-recognition-and-review`) | Constitutional alignment certification and review |
| CF-7.2.3 | Minimum Recognition Record | Minimum Certification Record |
| CS-3 §1.4 | Alignment-status recognition and ambiguity default (`#14-alignment-status-recognition-and-ambiguity-default`) | Alignment-status certification and ambiguity default |
| CS-5 label | *Forum recognition and lifecycle review* | *Forum certification and lifecycle review* |

Alphabetical positions in the Chapter Five directory and in the independent-terms cluster do not change (Full C… still precedes Fullest; Provisional C… still sits between Protected… and Proxy…).

## Chart (Part A §1.1)

The Decide node now branches to three purple status boxes (Full Certification, Provisional Certification, Not Certified), all flowing into Phase V Record, with Phase VI Operate downstream. After Record, a publication and go-live gate (§5, §7.1; drawn as a gate, not a phase) comes first: the outcome is published, the challenge path opens, and a certified system may then go live within the limits on the record. Full or Provisional Certification goes live; Not Certified does not, and goes to remedy. Phase VI Operate follows the gate: the §7.1 challenge path stays open while the outcome stands and the system operates, then recertification, reopening or fresh review (§7). No seventh phase was added: going live is a permission set by the §5 gate, not a stage of work with its own section. The Chapter Nine box sits level with the recertification box. Rendered with Mermaid 10.9.1; no crossing links.

## New wording

Part B §5 now says: "A system that holds neither status — because certification is deferred or refused, or has been withdrawn or has expired — is **Not Certified**." The go-live gate says a Not Certified system, including one whose certification is deferred or refused, may not go live. Part B §8 ("Certified systems only") says a system that is Not Certified supplies no standing input. These are the only places the umbrella term is operative; the rest of the change renames existing terms.

## Left as "recognition" (other senses)

Standing recognition pathways and Chapter One §3.2 (Recognition, Reinforcement, and Aspiration); recognition in the Chapter Five Accountability, Integrative and Participation bands (standing effects, refuge and movement recognition); Chapter Six rights text ("certified, officially recognized" in Part C); Chapters Nine, Ten (other lines) and Eleven; CF-6 and CF-10 cross-jurisdiction recognition (CF-10.11); CS-7, CS-9, CS-11, CS-12 recognition and fallback enforcement; "recognizably identifiable" likeness; the adopter guide's recognition of a shared standard process (`MINIMUM_VIABLE_ADOPTER.md`); evaluation packets; and the legacy alias id `chapter-eight-system-alignment-certification-and-recognition` in Part A (an alias nothing links to).

Historical records were not rewritten: `steward_box_review.md`, `evidence/` older directories, `archive/`, `evaluation/results/`, and the earlier MEMLOG entry for 2026-10-07. Translations remain paused.

## Tooling

`tools/ch8_certification_status_rename.py` applied the mechanical rename: global title and anchor literals, plus a line-scoped conversion limited to the lines and files listed in the script. Hand edits followed for the go-live and Not Certified wording (Part B §5, §8), the chart, the hub run sheet and reader guide, the steward door card and its JSON clock note, `doc_architecture.md` (new "Fourth move" paragraph) and `project/MEMLOG.md`. The generated hierarchy and rollout-status tables had only the two term names edited by hand.

Generated files regenerated: plain-terms edition, boundary chunks, human definition lookup, print pack, and the `ai_corpus/indexes/` files (section manifest, definition registry, id resolver, crossref matrix, section crossref).

## Verification

See the run recorded below.

## Follow-ups for the steward

- Sign off the new wording (Part B §5 "Not Certified" and go-live lines, Part B §8, and the Part A §1.1 chart text), together with the five places listed in `ch08_go_live_gate_reorder.md`.
- Decide whether to add a standstill period between publication of an outcome and go-live (still not added).
- Translations are paused; renamed terms will need a pass when they resume.
