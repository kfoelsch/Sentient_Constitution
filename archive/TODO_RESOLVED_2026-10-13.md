# Resolved TODO items — archived 2026-10-13

This archive records completed items removed from the active [TODO.md](../TODO.md) on 2026-10-13, kept verbatim and grouped by their original section. Normative meaning remains in the binding corpus; this file is a process-history record. The paths in the items below are written as in TODO.md (repo root).

## 2026-10-04 — Process-level granularity: Option A drafted, Option B outlined (completed items)

- [x] **Review CS-3 §7.10** (component findings under the system's class). Lane C: `make regression`, readability, obligation diff in `evidence/2026-10-04/`. Decide whether the §7.1 pointer and the §7 table row stay. **Decided 2026-10-07:** keep the §7.1 pointer and the §7 table row as they are; `make regression` green.
- [x] **Define Process in Chapter Five** with a test (placeholder tests in `project/PROCESS_SYSTEM_INSTITUTION_CROSSWALK.md`). Prerequisite for B. Institution has no standalone definition either. **Drafted 2026-10-07** in `core_05_band_continuity.md` (#### Process; three-part test; held to its system's class; no separate certification). Awaiting author review; `make regression` green. Translations not yet synced. **Institution** drafted the same day (`#### Institution`, same band). **Signed off by the steward 2026-10-13.**

## 2026-10-13 — Steward sign-off of drafted defaults (completed)

The steward signed off all of the drafted defaults below on 2026-10-13. Section titles are as in TODO.md.

### 2026-10-13 — Institutional alignment certification (Chapter Nine Part D): drafted on a branch, awaiting steward sign-off

- [x] **Sign off the eight defaults** now drafted: (1) composition by link, many to many; (2) Part D inside Chapter Nine, no rename and no new chapter; (3) one system means one pass and one record with an institutional findings block; (4) no go-live gate on the institution, with a class-scaled window for a provisional first certification; (5) the Integrity forum leads and Institutional forums hold the mandate and duty-compliance components; (6) cascade: a failed, withdrawn, or expired System certification is an indicator, and current misalignment where the cause is institutional; (7) forums, certifiers, and record offices are institutions, with no certification circle; (8) terms "Institutional Alignment Certification" and "Institutional Certification Record". **Signed off 2026-10-13.**

### 2026-10-13 — Formation check (Chapter Seven §7) and remediation readiness with denial and revocation (Chapter Nine Part B §7.1–§7.2, Part D §12.2 item 7 and §13.5): drafted on the same branch, awaiting steward sign-off

- [x] **Sign off the defaults** now drafted: (1) covered offices are the governing authority, Role Map seats, and offices that bind others or hold records, keys, or funds, and other staff get a structural check only; (2) standing counts only from verified records, and authenticity is found from control, interests and rewards, conduct, and protected voice, and holding a belief or belonging to a group does not count by itself; (3) the check is a published statement and not a gate; (4) "denial" and "revocation" are plain names for non-certification and withdrawal, with no new outcome word; (5) the five revocation grounds in Part B §7.2; (6) conditions may not carry a plan the readiness check did not find ready; (7) a Not Certified Institution may not hold a seat in another body's certification or host a forum; (8) a denied or revoked Institution's status is adverse evidence in each of its Systems' certifications. **Signed off 2026-10-13.**

### 2026-10-13 — Article XI-E two narrow gates and the Institutional Authority Standing Lock: drafted on the same branch, awaiting steward sign-off and heightened review

- [x] **Sign off the defaults** now drafted: (1) the gates attach to a named sentient's authority and reach the body only as vehicle, successor, controlled entity, or nominee-held form; (2) the interim hold standard is more likely than not, on specific verified facts disclosed to the sentient, with a real risk of serious harm or of defeating the body's checks and a narrower safeguard not enough; (3) the hold is not a finding, lock, standing record, or standing effect, and only a forum with jurisdiction may issue it, never the body itself; (4) the Institutional Authority Standing Lock is mandatory when its verified trigger is met and never attaches from probable cause; (5) its restoration record includes a verified authenticity finding; (6) the party imposing a gate bears the burden; (7) authentic formation is a condition of the right and not a licence, judged on conduct, control, and rewards, with a no-record founder presumed authentic and probable cause of intent to mislead or to harm handled by the same Interim Hold (intent to harm means harm this Constitution forbids, not ordinary competition, criticism, or dissent); a verified statement that others deserve harm or discriminatory treatment counts against a founder or holder, with the Chapter Seven §7 safeguards; (8) the belief rule is threaded, not absolute: holding a belief or belonging to a group does not count by itself, but a religious, political, or ideological label is no shield for statements or acts that harm others or violate Article VI-C, which are judged on what they state, call for, or do; (9) Chapter One §7.5 Expression and the Harm Line is a restatement and adds no restriction; the same test for sentients and institutions; criticism of an institution called bullying is a limit that carries the burden; evidence use is distinct from limiting expression. **Signed off 2026-10-13.**

### 2026-10-13 — Interim Hold standard: built on the same branch, awaiting steward sign-off and heightened review

- [x] **Sign off the drafted defaults:** the ground and its evidence tier; the closed list of applications; the never-reached list; the five-rung ladder; one extension only; time counts toward a later lock's bound but not its corrective conditions; a hold needs no open remedy record. **Signed off 2026-10-13.**

## 2026-10-13 — Checks completed (second pass)

Items verbatim from TODO.md, each with the result of the check.

- [x] **Check Article XI-E** against Part D §11.3 (no licence, no gate) and the Class L scaling in §12.4.

  **Result:** Checked 2026-10-13: Part D §11.3 states that certification is not a licence or gate and names the two narrow gates in Article XI-E as the only gates, attached to a named sentient and never to the Institution. §12.4 requires all seven items for Class L, simplified, with none omitted, and adds no gate.

- [x] **Check `adoption/ANNOUNCEMENT.md`** so Part D never reads as a promised feature, as for Option B below.

  **Result:** Checked 2026-10-13: `implementation/adoption/ANNOUNCEMENT.md` does not mention Part D, institutional alignment certification, the formation check, or the Interim Hold. It says it certifies nothing (line 32), and its only certification mention is system alignment certification. Part D is not presented as a promised feature.

- [x] **Check Article XI-E** against Chapter Seven §7 and Part D §13.5 (no gate on forming or operating a body; the only gates are the two narrow gates on a named sentient's authority, see the next entry).

  **Result:** Checked 2026-10-13: Chapter Seven §7 and Part D §13.5 each say no gate on the body, no licence, and no new lock or hold, and each limits the gates to the two narrow gates in Article XI-E on a named sentient's authority.

- [x] **Chapter Thirteen interim-protection text** was not edited; confirm that the existing interim-relief grounds cover the hold or add a routing sentence.

  **Result:** Checked 2026-10-13: the text was in fact edited. Chapter Thirteen §5 *Interim protection* now routes relief against a named sentient's named pathway on less than a verified finding to the Interim Hold subsection, and the Interim Hold subsection says other interim relief stays available for what it already covers. No further routing sentence needed.

- [x] **Run `make ai-manifest-regenerate`** now that source changes are committed.

  **Result:** Done 2026-10-13: ran `make ai-manifest-regenerate` after the last source edits; `make ai-manifest-validate` reports the manifests valid and fresh.

