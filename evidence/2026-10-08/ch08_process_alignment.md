# Chapter Eight chart and process alignment (2026-10-08)

## Authorization and scope

The editor requested a review of the Part A §1.1 certification process chart and its text, then explicitly instructed: "Please implement your suggestions." This pass implements that review in Part A, Part B, the Chapter Eight reading index, and the architecture and session records. The six phases, section numbers, and anchors remain.

This is a substantive process change. It does not claim that obligations are conserved. No adoption or release is performed by this change.

## Changes

- The redundant challenge-path box now covers monitoring and response within certified scope and conditions. Publication opens the record challenge path; later challenges remain possible while the system has stakeholders, including challenges to completed earlier records.
- The chart separates permitted operation from protection and correction. Correction evidence returns through independent review before authorization of the affected scope or release from conditions. The text preserves the Article XXVIII-A transition exception and survival-essential interim protection.
- Part B §4.2 distinguishes unfinished work necessary for authorization from a completed component finding supporting bounded conditional operation. Required findings and disposition of material objections cannot be bypassed.
- Participation during evaluation and review is explicit. Actual and reasonably foreseeable effects and dependency identify affected sentients before deployment; the ordinary published-record path still opens with publication.
- Part B §5 distinguishes conditions before go-live, continuing operating conditions, and corrective work under bounded authorization. Conditions name owners, deadlines or cadences, completion evidence, independent verifying authority, and consequences. Necessary Rights-Floor protection cannot be deferred.
- First deployment and material expansion require a forum-set notice interval, earliest permitted go-live, and a practicable opportunity to seek interim protection. No universal numerical wait is invented; filing a challenge does not automatically stay operation. Existing response deadlines remain.
- Defects require protection, correction, and independent verification, including regression confirmation where CS-5 requires it. The initial evaluation now uses the same misalignment response-clock bridge as later reviews.
- Part B §6.1 gathers an operating plan on the same record: scope, dates, conditions, monitoring owners and indicators, response authority and clocks, corrective work, and verification. Not Certified records do not imply operating permission. Later evidence is linked without editing completed records.
- Part B §7 requires carrying out monitoring and response; material incidents, unmet conditions, and credible challenges do not wait for the scheduled recertification.
- Chart corrections: §3.8 covers applicable Rights-Floor checks and six domain evaluations; Full Certification requires consecutive clean provisional checks; Provisional Certification includes continuing and stepped-down status; Not Certified includes expiration without an automatic universal reset to provisional. Gate uses a decision diamond and input a terminator.
- One standing arrow applies §8's gate. The text preserves eligibility of verified facts arising during earlier certification after withdrawal or expiration, and excludes never-certified systems from this chapter's bridge.
- Part A §2.1 points to the assigned forum-family roles rather than assigning every Class A Rights-Floor question to Sentient forums. The hub phase table, run sheet, record checklist, and failure-status row match the operative text.

## Verification

- `make regression` passes on a temporary copy containing tracked source plus this evidence record. The copy has a baseline Git commit, so changed-line audits evaluate the edits against the pre-change source.
- `make plain-terms-edition-check` and `make boundary-chunks-check` pass. `make ai-corpus-sync` regenerated navigation and cross-reference artifacts, and regression includes successful `ai-manifest-validate` freshness validation. Timestamp-only changes were not copied back.
- New references pass section-name, corpus-name, Article-title, and local-fragment audits. No section or anchor renumbering was needed.
- `git diff --check` passes.
- The chart was rendered locally with Mermaid 10.9.1 and inspected at full-page size. It runs top to bottom, all labels are legible, the gate uses a decision diamond, and the paths do not cross. Matching A connectors return a new pass to framing; B returns satisfied prerequisites to the same gate without requiring recertification; C sends non-certification to correction.
- Unrelated untracked duplicate files and the Git bundle in the user's workspace were preserved. Verification uses a clean copy to avoid the duplicate-file problems documented in earlier Chapter Eight evidence.

Manual process checks against the operative provisions:

| Situation | Result |
|-----------|--------|
| First provisional certification, notice still running | No go-live; satisfy notice and independently verified prerequisites, then return to the same gate. |
| Never-certified system refused certification | No go-live; protect and correct, with independent review before any authorization. No standing input through this chapter's bridge. |
| Conditional certification with work left to do | Necessary protections precede authorization; continuing conditions and later corrective work have owners, evidence, clocks, and consequences. Only the supported bounded scope operates. |
| Material design or operating defect during operation | Timely protection and reopened review; new linked record and independent verification of correction before affected-scope authorization or condition release. |
| Scheduled recertification of unchanged scope | New linked record and required regression testing; a new first-deployment notice interval is not automatically imposed. |
| Withdrawal or expiry after certified operation | No new go-live; verified facts arising during certification remain eligible for the §8 gate. |
| Survival-essential system under corrective review or adoption transition | Applicable forum interim protection and Article XXVIII-A transition duties govern continued reliance; the correction box does not itself require abrupt interruption. |

## Files

- `core_08_a_system_alignment_certification_evaluation.md`
- `core_08_b_system_alignment_certification_record_process.md`
- `core_08_system_alignment_certification.md`
- `doc_architecture.md`
- `project/MEMLOG.md`
- this evidence record and generated navigation artifacts listed in the final diff

Translations remain paused under the editor's standing decision. Branch: `fix/ch08-process-alignment`.
