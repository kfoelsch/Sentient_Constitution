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

from ch5_paths import CH5_ALL  # noqa: E402

MEASUREMENTS_RE = re.compile(r"^\*Measurements:\*\s*$", re.MULTILINE)
PRIMARY_MEAS_RE = re.compile(r"^\s*(?:-\s+)?\*\*Primary:\*\*", re.MULTILINE)
SECONDARY_MEAS_RE = re.compile(r"^\s*(?:-\s+)?\*\*Secondary:\*\*", re.MULTILINE)
TERTIARY_MEAS_RE = re.compile(r"^\s*(?:-\s+)?\*\*Tertiary:\*\*", re.MULTILINE)
PRIMARY_E_RE = re.compile(r"\*\*Primary assessment\.\*\*", re.MULTILINE)
SECONDARY_E_RE = re.compile(r"\*\*Secondary co-assessment\.\*\*", re.MULTILINE)
TERTIARY_E_RE = re.compile(r"\*\*Tertiary integrity check\.\*\*", re.MULTILINE)
PRIMARY_C_RE = re.compile(r"\*\*Primary failure\.\*\*", re.MULTILINE)
SECONDARY_C_RE = re.compile(r"\*\*Secondary failure\.\*\*", re.MULTILINE)
TERTIARY_C_RE = re.compile(r"\*\*Tertiary failure\.\*\*", re.MULTILINE)
HEADING_RE = re.compile(r"^#{4,5}\s+(.+)$")


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
    return None


def find_term_body(root: Path, term: str, registry: dict) -> tuple[str, str] | None:
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
    if not MEASUREMENTS_RE.search(body):
        errors.append("missing *Measurements:* block")
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
