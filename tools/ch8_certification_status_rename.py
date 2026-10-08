#!/usr/bin/env python3
"""Rename the Chapter Eight status vocabulary from "recognition" to "certification".

Statuses become Provisional Certification, Full Certification and Not Certified.
Only the certification-status sense of "recognition" is changed. Other senses
(standing recognition pathways, refuge and movement recognition,
cross-jurisdiction recognition, recognizably identifiable, the adopter guide's
recognition of a shared process) are left alone.

Run from the repo root:  python3 tools/ch8_certification_status_rename.py [--dry-run]
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(".")
DRY = "--dry-run" in sys.argv

PROTECTED = re.compile(
    r"^(archive/|translations|evaluation/results|evidence/|ai_corpus/|doc_architecture/generated/|"
    r"steward_box_review\.md|tools/ch8_certification_status_rename\.py)"
)

# Phase 0: titles and anchors, applied to every tracked text file outside PROTECTED.
GLOBAL_LITERALS = [
    ("72-provisional-and-full-recognition", "72-provisional-and-full-certification"),
    ("cf-72-constitutional-alignment-recognition-and-review", "cf-72-constitutional-alignment-certification-and-review"),
    ("cf-723-minimum-recognition-record", "cf-723-minimum-certification-record"),
    ("14-alignment-status-recognition-and-ambiguity-default", "14-alignment-status-certification-and-ambiguity-default"),
    ("Constitutional alignment recognition and review", "Constitutional alignment certification and review"),
    ("Minimum Recognition Record", "Minimum Certification Record"),
    ("Alignment-status recognition and ambiguity default", "Alignment-status certification and ambiguity default"),
    ("alignment-status recognition and ambiguity default", "alignment-status certification and ambiguity default"),
    ("Forum recognition and lifecycle review", "Forum certification and lifecycle review"),
    ("Provisional and full recognition", "Provisional and full certification"),
    ("provisional and full recognition", "provisional and full certification"),
    ("Full Recognition", "Full Certification"),
    ("Provisional Recognition", "Provisional Certification"),
]
GLOBAL_REGEX = [
    (re.compile(r"(?<=#)(full|provisional)-recognition"), r"\1-certification"),
    (re.compile(r'(?<=id=")(full|provisional)-recognition'), r"\1-certification"),
]

# Phase 1: line-scoped conversion of the certification-status sense.
def conv(s):
    s = re.sub(r"\bnon-recognition\b", "non-certification", s)
    s = s.replace("recognition-and-review", "certification-and-review")
    s = s.replace("recognition-bearing", "status-granting")
    for a, b in (("Recognized", "Certified"), ("recognized", "certified"),
                 ("recognises", "certifies"), ("recognizes", "certifies"),
                 ("Recognize", "Certify"), ("recognize", "certify"),
                 ("recognizing", "certifying"),
                 ("Recognition", "Certification"), ("recognition", "certification")):
        s = re.sub(r"\b" + a + r"\b", b, s)
    return s

FULL_FILES = {
    "core_08_a_system_alignment_certification_evaluation.md": set(),
    "core_08_b_system_alignment_certification_record_process.md": set(),
    "core_08_system_alignment_certification.md": set(),
    "corpus_forum/cf_07_integrity_safeguards_anti_capture_anti_self_judging.md": set(),
    "corpus_systems/cs_03_a_system_classification_machinery.md": {454},
    "core_12_forum.md": {251},
}
LINE_FILES = {
    "core_05_band_continuity.md": set(range(1, 561)),
    "core_03_definition_integrity.md": {231, 235},
    "core_04_burden_traceability_verification.md": {193, 199, 210, 214},
    "core_05_band_oversight.md": {791},
    "core_06_rights_part_c.md": {1028},
    "core_00_preamble.md": {280, 373, 382},
    "core_10_standing_integration.md": {369, 372, 503},
    "corpus_forum/cf_00_registry_and_reading_rules.md": {64, 66},
    "corpus_forum/cf_06_appeal_secondary_review_exhaustion_pathways.md": {242},
    "corpus_forum/cf_10_technical_specialist_forums_specialist_chambers.md": {76},
    "corpus_systems/cs_02_a_information_types_and_handling.md": {686},
    "corpus_systems/cs_05_design_testing_verification_deployment.md": {62, 69, 78, 109, 162, 319, 321, 332},
    "corpus_institutions/ci_14_transitional_governance_institutional_evolution.md": {325},
    "corpus_joint_structure/cjs_03u_audit_process.md": {142},
    "corpus_joint_structure/cjs_03a_accountability_operations.md": {1196, 1197},
    "guides/CONCEPTUAL_OVERVIEW.md": {963},
    "implementation/STEWARD_ENTRY_DOORS.md": {159},
    "implementation/steward_owner_clock_index.json": {128, 131},
}

# Phase 2: hand edits, written against the post-conversion text. (file, old, new, expected count)
HAND = []  # filled from tools/ch8_certification_status_rename_hand.py when present

def tracked():
    out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True, check=True).stdout
    return [f for f in out.split("\0") if f]

def main():
    changed = {}
    files = [f for f in tracked() if f.endswith((".md", ".json", ".py")) and not PROTECTED.match(f)]
    for f in files:
        p = ROOT / f
        try:
            t = p.read_text(encoding="utf-8")
        except Exception:
            continue
        o = t
        for a, b in GLOBAL_LITERALS:
            t = t.replace(a, b)
        for rx, rep in GLOBAL_REGEX:
            t = rx.sub(rep, t)
        if f in FULL_FILES or f in LINE_FILES:
            lines = t.split("\n")
            skip = FULL_FILES.get(f)
            only = LINE_FILES.get(f)
            for i, l in enumerate(lines, 1):
                if "ecogni" not in l and "ECOGNI" not in l:
                    continue
                if f in FULL_FILES and i in skip:
                    continue
                if f in LINE_FILES and i not in only:
                    continue
                lines[i - 1] = conv(l)
            t = "\n".join(lines)
        if t != o:
            changed[f] = t
    # tools JSON keys
    for f in ("tools/architecture/measurement_tier_seeds.json", "tools/glosses_cf_sections.json"):
        pass  # covered by GLOBAL_LITERALS (titles) above
    for f, t in changed.items():
        print(("would change " if DRY else "changed ") + f)
        if not DRY:
            (ROOT / f).write_text(t, encoding="utf-8")

if __name__ == "__main__":
    main()
