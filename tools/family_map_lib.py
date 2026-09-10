"""Load companion family_map.json and resolve family IDs to subfiles."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterator

FAMILY_MAP_REL = Path("tools/architecture/family_map.json")
SECTION_ID_RE = re.compile(r"^(CJS|CS|CI|CF)-(\d+)(?:\.(\d+))?(?:\.(\d+))?", re.I)

CS_PART_DEFAULTS = {
    "CS-2": "corpus_systems/cs_02_a_information_types_and_handling.md",
    "CS-3": "corpus_systems/cs_03_a_system_classification_machinery.md",
}


def load_family_map(root: Path) -> dict[str, Any]:
    return json.loads((root / FAMILY_MAP_REL).read_text(encoding="utf-8"))


def iter_entries(data: dict[str, Any]) -> Iterator[dict[str, Any]]:
    for layer in data.get("layers", {}).values():
        for group in layer.get("groups", []):
            yield from group.get("entries", [])


def family_files(data: dict[str, Any]) -> dict[str, str]:
    """Map canonical family IDs (CI-12, CS-4, CJS-2, CF-3) to repo-relative files."""
    mapping: dict[str, str] = dict(CS_PART_DEFAULTS)
    for entry in iter_entries(data):
        if entry.get("status") == "reserved":
            continue
        file_rel = entry.get("file")
        raw_id = str(entry.get("id", ""))
        if not file_rel or not raw_id:
            continue
        mapping[raw_id] = file_rel
        token = re.match(r"^(CJS|CS|CI|CF)-\d+", raw_id)
        if token and token.group(0) not in mapping:
            mapping[token.group(0)] = file_rel
    mapping.setdefault(
        "CJS-3",
        "corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md",
    )
    mapping.setdefault(
        "CJS-0",
        "corpus_joint_structure/cjs_00_registry_and_reading_rules.md",
    )
    mapping.setdefault(
        "CJS-0.1",
        "corpus_joint_structure/cjs_00_registry_and_reading_rules.md",
    )
    return mapping


def cjs3_home(data: dict[str, Any], cluster_id: str) -> str | None:
    homes = data.get("cjs3_cluster_homes", {})
    match = re.match(r"^(?:CJS-)?3\.(\d+)$", cluster_id, re.I)
    if not match:
        return None
    return homes.get(f"3.{int(match.group(1))}")


def cjs12_home(data: dict[str, Any], section_id: str) -> str | None:
    homes = data.get("cjs12_section_homes", {})
    match = re.match(r"^(?:CJS-)?([12]\.\d+(?:\.\d+)?)$", section_id, re.I)
    if not match:
        return None
    return homes.get(match.group(1))


def cs_section_home(data: dict[str, Any], section_id: str) -> str | None:
    homes = data.get("cs_section_homes", {})
    match = re.match(r"^(?:CS-)?(\d+)\.(\d+)$", section_id, re.I)
    if not match:
        return None
    return homes.get(f"{int(match.group(1))}.{int(match.group(2))}")


def resolve_section_file(data: dict[str, Any], section_id: str) -> str | None:
    """Resolve CI-9.3 / CJS-3.8 / CS-5.8 / CF-12 to a subfile."""
    text = section_id.strip().strip("*")
    files = family_files(data)
    # Exact map ids such as CS-5A / CS-2B are not CS-5 / CS-2.
    if text in files and not SECTION_ID_RE.fullmatch(text):
        return files[text]
    match = SECTION_ID_RE.match(text)
    if not match:
        return files.get(text)
    prefix, major, minor, _third = match.groups()
    prefix = prefix.upper()
    family = f"{prefix}-{int(major)}"
    if prefix == "CJS" and minor is not None and int(major) == 3:
        home = cjs3_home(data, f"CJS-3.{int(minor)}")
        if home:
            return home
    if prefix == "CJS" and minor is not None and int(major) in (1, 2):
        dotted = f"{int(major)}.{int(minor)}"
        if _third is not None:
            dotted_third = f"{dotted}.{int(_third)}"
            home = cjs12_home(data, dotted_third)
            if home:
                return home
        home = cjs12_home(data, dotted)
        if home:
            return home
    if prefix == "CS" and minor is not None:
        home = cs_section_home(data, f"CS-{int(major)}.{int(minor)}")
        if home:
            return home
    return files.get(family) or files.get(text)
