#!/usr/bin/env python3
"""NAV-IMPL-FILENAME-01: companion files share a numeric prefix only as chapter parts.

Undifferenced ``cjs_02_foo.md`` and ``cjs_02_bar.md`` are not parts of one chapter.
Same-chapter extras need a discriminator: glued letter (``cjs_03o_``) or CS-style
part letter (``cs_02_a_``). Family ``01`` is the unique scope page for that layer.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMPANION_DIRS = (
    "corpus_joint_structure",
    "corpus_systems",
    "corpus_institutions",
    "corpus_forum",
)

NUMBERED_PREFIX_RE = re.compile(r"^(cjs|cs|ci|cf)_\d", re.I)
COMPANION_FILE_RE = re.compile(
    r"^(cjs|cs|ci|cf)_(\d{2,})(?:([a-z]+)|_([a-z]))?_(.+)\.md$",
    re.I,
)
SINGLETON_FAMILIES = {"01"}


@dataclass(frozen=True)
class CompanionName:
    layer: str
    number: str
    part: str
    rest: str
    filename: str

    @property
    def family_key(self) -> tuple[str, str]:
        return (self.layer, self.number)

    @property
    def part_key(self) -> tuple[str, str, str]:
        return (self.layer, self.number, self.part)


def parse_companion_filename(name: str) -> CompanionName | None:
    match = COMPANION_FILE_RE.fullmatch(name)
    if not match:
        return None
    layer, number, glued, us_letter, rest = match.groups()
    part = (glued or us_letter or "").lower()
    return CompanionName(layer.lower(), number, part, rest, name)


def iter_companion_filenames(root: Path) -> list[str]:
    names: list[str] = []
    for rel in COMPANION_DIRS:
        folder = root / rel
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.md")):
            names.append(path.name)
    return names


def audit_filenames(names: list[str]) -> list[str]:
    findings: list[str] = []
    parsed: list[CompanionName] = []
    for name in names:
        if not NUMBERED_PREFIX_RE.match(name):
            continue
        item = parse_companion_filename(name)
        if item is None:
            findings.append(
                f"{name}: numbered companion filename is not parseable "
                "(expected layer_NN_home.md, layer_NNx_part.md, or layer_NN_a_part.md)"
            )
            continue
        parsed.append(item)

    by_family: dict[tuple[str, str], list[CompanionName]] = defaultdict(list)
    by_part: dict[tuple[str, str, str], list[CompanionName]] = defaultdict(list)
    for item in parsed:
        by_family[item.family_key].append(item)
        by_part[item.part_key].append(item)

    for (layer, number), files in sorted(by_family.items()):
        homes = [item for item in files if not item.part]
        parts = [item for item in files if item.part]
        if number in SINGLETON_FAMILIES and len(files) > 1:
            listed = ", ".join(item.filename for item in files)
            findings.append(
                f"{layer}_{number}: family 01 is the unique scope page; "
                f"found {len(files)} files: {listed}"
            )
            continue
        if len(homes) > 1:
            listed = ", ".join(item.filename for item in homes)
            findings.append(
                f"{layer}_{number}: multiple undifferenced files share this prefix; "
                f"same-chapter extras need a part letter ({listed})"
            )
        if number in SINGLETON_FAMILIES and parts:
            listed = ", ".join(item.filename for item in parts)
            findings.append(
                f"{layer}_{number}: family 01 may not use part letters ({listed})"
            )

    for key, files in sorted(by_part.items()):
        if not key[2] or len(files) < 2:
            continue
        listed = ", ".join(item.filename for item in files)
        findings.append(
            f"{key[0]}_{key[1]}{key[2]}: duplicate part letter ({listed})"
        )
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings = audit_filenames(iter_companion_filenames(root))
    if findings:
        print("Companion filename audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        return 1
    print("Companion filename audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
