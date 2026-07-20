#!/usr/bin/env python3
"""Audit MEAS-DEF-01 measurement tier placement on Chapter Five definitions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_APEX  # noqa: E402

# Letter-form O/M/A/C heads (aims and Tetrad legs) live in apex files without #### titles.
APEX_HEAD_LOCATORS: dict[str, tuple[str, str]] = {
    "Flourishing": ("core_05apex_flourishing_aim.md", "flourishing-constitutional"),
    "Continuity (Constitutional Aim)": (
        "core_05apex_continuity_aim.md",
        "continuity-aim-constitutional",
    ),
    "Oversight": ("core_05apex_oversight_leg.md", "oversight-constitutional"),
    "Participation": ("core_05apex_participation_leg.md", "participation-constitutional"),
    "Accountability": ("core_05apex_accountability_leg.md", "accountability"),
    "Timeliness": ("core_05apex_accountability_leg.md", "timeliness-constitutional"),
}

LETTER_M_RE = re.compile(r"^- M:", re.MULTILINE)

# Legacy interim marker (still valid for un-migrated terms).
MEASUREMENTS_RE = re.compile(r"^\s*(?:-\s+)?\*Measurements:\*\s*$", re.MULTILINE)
MEASUREMENTS_IN_E_RE = re.compile(r"^  -\s*\*Measurements:\*\s*$", re.MULTILINE)
E_LINE_RE = re.compile(r"^- \*\*E:\*\*|^- E:", re.MULTILINE)
# Guidepost header for the evaluation component on measurement-migrated terms.
GUIDEPOST_E_RE = re.compile(r"^- \*\*How to measure and assess\*\*", re.MULTILINE)
# Measurement (M) tier labels. Three accepted forms:
#   - legacy         **Primary:**
#   - interim O/M/E/C **M-Primary:**
#   - guidepost       **Primary measure:** (bold run-in label, colon)
PRIMARY_MEAS_RE = re.compile(
    r"^\s*(?:-\s+)?\*\*(?:M-)?Primary:\*\*"
    r"|\*\*Primary measure:\*\*",
    re.MULTILINE,
)
SECONDARY_MEAS_RE = re.compile(
    r"^\s*(?:-\s+)?\*\*(?:M-)?Secondary:\*\*"
    r"|\*\*Secondary measure:\*\*",
    re.MULTILINE,
)
TERTIARY_MEAS_RE = re.compile(
    r"^\s*(?:-\s+)?\*\*(?:M-)?Tertiary:\*\*"
    r"|\*\*Tertiary measure:\*\*",
    re.MULTILINE,
)
MPRIMARY_LABEL_RE = re.compile(r"\*\*(?:M-Primary:|Primary measure:)\*\*", re.MULTILINE)
# Assessment (E) tier labels — legacy, interim, or guidepost forms. The
# guidepost form is a bold run-in label with a colon (**Primary assessment:**),
# sitting on its own continuation line beneath the tier's measure.
PRIMARY_E_RE = re.compile(
    r"\*\*(?:Primary assessment\.|E-Primary Assessment:|Primary assessment:)\*\*",
    re.MULTILINE,
)
SECONDARY_E_RE = re.compile(
    r"\*\*(?:Secondary co-assessment\.|E-Secondary Assessment:|Secondary assessment:)\*\*",
    re.MULTILINE,
)
TERTIARY_E_RE = re.compile(
    r"\*\*(?:Tertiary integrity check\.|E-Tertiary Integrity Check:|Tertiary assessment:)\*\*",
    re.MULTILINE,
)
PRIMARY_C_RE = re.compile(r"\*\*Primary failure[.:]\*\*", re.MULTILINE)
SECONDARY_C_RE = re.compile(r"\*\*Secondary failure[.:]\*\*", re.MULTILINE)
TERTIARY_C_RE = re.compile(r"\*\*Tertiary failure[.:]\*\*", re.MULTILINE)
HEADING_RE = re.compile(r"^#{4,5}\s+(.+)$")

# MEAS-DEF-01 E-placement pilot terms (enforce in-E placement).
E_PLACEMENT_PILOT_TERMS = frozenset(
    {
        "Wellbeing",
        "Transparency",
        "Cascading Failure",
        "Adversarial, Scaled, and Exploited Conditions",
    }
)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--seeds",
        default="tools/architecture/measurement_tier_seeds.json",
        help="Measurement tier seed path.",
    )
    p.add_argument(
        "--registry",
        default="ai_corpus/indexes/definition_registry.json",
        help="Definition registry JSON path.",
    )
    p.add_argument(
        "--enforce-approved",
        action="store_true",
        help="Exit non-zero when approved seeds fail checks.",
    )
    return p.parse_args()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_apex_omac_body(text: str, anchor: str) -> str | None:
    """Extract letter O/M/A/C body following ``<a id="{anchor}">`` in an apex file."""
    marker = f'<a id="{anchor}"></a>'
    start = text.find(marker)
    if start < 0:
        return None
    # Prefer the first letter O: block after the anchor.
    o_match = re.search(r"^- O:", text[start:], re.MULTILINE)
    if not o_match:
        return None
    body_start = start + o_match.start()
    rest = text[body_start:]
    # End at the first thematic break after the C: line.
    c_match = re.search(r"^- C:.*$", rest, re.MULTILINE)
    if not c_match:
        return rest
    after_c = rest[c_match.end() :]
    hr = re.search(r"\n---\s*\n", after_c)
    if hr:
        return rest[: c_match.end() + hr.start()]
    return rest[: c_match.end()]


def extract_definition_body(text: str, term: str) -> str | None:
    lines = text.splitlines()
    for idx, raw in enumerate(lines):
        match = HEADING_RE.match(raw.strip())
        if not match or match.group(1).strip() != term:
            continue
        depth = len(raw.strip()) - len(raw.strip().lstrip("#"))
        body: list[str] = []
        for j in range(idx + 1, len(lines)):
            stripped = lines[j].strip()
            m2 = HEADING_RE.match(stripped)
            if m2 and len(m2.group(0)) - len(m2.group(0).lstrip("#")) <= depth:
                break
            body.append(lines[j])
        return "\n".join(body)
    # ## Timeliness (and similar apex co-leg heads)
    for idx, raw in enumerate(lines):
        if raw.strip() == f"## {term}":
            body: list[str] = []
            for j in range(idx + 1, len(lines)):
                stripped = lines[j].strip()
                if stripped.startswith("## ") or stripped.startswith("# "):
                    break
                body.append(lines[j])
            return "\n".join(body)
    return None


def find_term_body(root: Path, term: str, registry: dict) -> tuple[str, str] | None:
    if term in APEX_HEAD_LOCATORS:
        file_name, anchor = APEX_HEAD_LOCATORS[term]
        path = root / file_name
        if path.is_file():
            body = extract_apex_omac_body(path.read_text(encoding="utf-8"), anchor)
            if body:
                return file_name, body
    for entry in registry.get("definitions", []):
        if entry.get("term") == term and entry.get("category") != "principle_layer":
            path = root / entry["source_file"]
            body = extract_definition_body(path.read_text(encoding="utf-8"), term)
            if body:
                return entry["source_file"], body
    for file_name in CH5_ALL:
        path = root / file_name
        if not path.is_file():
            continue
        body = extract_definition_body(path.read_text(encoding="utf-8"), term)
        if body:
            return file_name, body
    return None


def tier_checks(body: str, tier_depth: str) -> list[str]:
    errors: list[str] = []
    # Apex aim/leg heads use letter-form ``- M:`` link-only rollups.
    if LETTER_M_RE.search(body) and tier_depth == "primary_only":
        return errors
    if not MEASUREMENTS_RE.search(body) and not PRIMARY_MEAS_RE.search(body):
        errors.append("missing measurement register (legacy *Measurements:* or M-Primary)")
        return errors
    if tier_depth == "full":
        for label, pattern in (
            ("Primary measurement", PRIMARY_MEAS_RE),
            ("Secondary measurement", SECONDARY_MEAS_RE),
            ("Tertiary measurement", TERTIARY_MEAS_RE),
            ("Primary assessment in E", PRIMARY_E_RE),
            ("Secondary co-assessment in E", SECONDARY_E_RE),
            ("Tertiary integrity check in E", TERTIARY_E_RE),
            ("Primary failure in C", PRIMARY_C_RE),
            ("Secondary failure in C", SECONDARY_C_RE),
            ("Tertiary failure in C", TERTIARY_C_RE),
        ):
            if not pattern.search(body):
                errors.append(f"missing {label}")
    elif tier_depth == "primary_secondary":
        for label, pattern in (
            ("Primary measurement", PRIMARY_MEAS_RE),
            ("Secondary measurement", SECONDARY_MEAS_RE),
            ("Primary assessment in E", PRIMARY_E_RE),
            ("Secondary co-assessment in E", SECONDARY_E_RE),
            ("Primary failure in C", PRIMARY_C_RE),
            ("Secondary failure in C", SECONDARY_C_RE),
        ):
            if not pattern.search(body):
                errors.append(f"missing {label}")
    elif tier_depth == "primary_only":
        if not PRIMARY_MEAS_RE.search(body):
            errors.append("missing Primary measurement")
    return errors


def placement_checks(body: str, term: str) -> list[str]:
    """Enforce guidepost O/M/E/C presentation for pilot terms.

    Pilot terms drop the letter markers and the legacy ``*Measurements:*``
    header in favour of the reader-facing guidepost headers, with each tier's
    measure and assessment stated as bold run-in labels (``**Primary measure:**``
    on the tier bullet, ``**Primary assessment:**`` on the continuation line)
    beneath the ``How to measure and assess`` header.
    """
    errors: list[str] = []
    if term not in E_PLACEMENT_PILOT_TERMS:
        return errors

    if MEASUREMENTS_RE.search(body):
        errors.append("pilot term must not use the legacy *Measurements:* header")
    if E_LINE_RE.search(body):
        errors.append("pilot term must not use a bare '- E:' marker (use guidepost headers)")

    e_match = GUIDEPOST_E_RE.search(body)
    if not e_match:
        errors.append("pilot term missing 'How to measure and assess' guidepost header")
        return errors

    m_match = PRIMARY_MEAS_RE.search(body)
    if not m_match:
        errors.append("pilot term missing a **Primary measure:** label")
    elif m_match.start() < e_match.start():
        errors.append("Primary measure must appear under 'How to measure and assess'")
    return errors


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    seeds = load_json(root / args.seeds)
    registry_path = root / args.registry
    registry = load_json(registry_path) if registry_path.is_file() else {"definitions": []}

    findings: list[str] = []
    approved = 0
    passed = 0

    for term, meta in sorted(seeds.get("terms", {}).items()):
        status = meta.get("status", "pending")
        if status != "approved":
            continue
        approved += 1
        located = find_term_body(root, term, registry)
        if not located:
            findings.append(f"{term}: definition body not found")
            continue
        source_file, body = located
        errors = tier_checks(body, meta.get("tier_depth", "full"))
        errors.extend(placement_checks(body, term))
        if errors:
            findings.append(f"{source_file} ({term}): " + "; ".join(errors))
        else:
            passed += 1

    print(f"ch5-measurement-tier-audit: {passed}/{approved} approved terms pass")
    if findings:
        for line in findings:
            print(f"  - {line}", file=sys.stderr)
        if args.enforce_approved:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
