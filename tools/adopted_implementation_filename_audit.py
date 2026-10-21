#!/usr/bin/env python3
"""NAV-IMPL-FILENAME-01: adopted-implementation files use their five-digit IDs."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ADOPTED_IMPLEMENTATION_DIRS = (
    "corpus_joint_structure",
    "corpus_systems",
    "corpus_institutions",
    "corpus_forum",
)

NUMBERED_PREFIX_RE = re.compile(r"^(cjs|cs|ci|cf)_\d", re.I)
ADOPTED_IMPLEMENTATION_FILE_RE = re.compile(r"^(cjs|cs|ci|cf)_(\d{5})_(.+)\.md$", re.I)


@dataclass(frozen=True)
class AdoptedImplementationName:
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


def parse_adopted_implementation_filename(name: str) -> AdoptedImplementationName | None:
    match = ADOPTED_IMPLEMENTATION_FILE_RE.fullmatch(name)
    if not match:
        return None
    layer, number, rest = match.groups()
    return AdoptedImplementationName(layer.lower(), number, "", rest, name)


def iter_adopted_implementation_filenames(root: Path) -> list[str]:
    names: list[str] = []
    for rel in ADOPTED_IMPLEMENTATION_DIRS:
        folder = root / rel
        if not folder.is_dir():
            continue
        for path in sorted(folder.glob("*.md")):
            names.append(path.name)
    return names


def audit_filenames(names: list[str]) -> list[str]:
    findings: list[str] = []
    parsed: list[AdoptedImplementationName] = []
    for name in names:
        if not NUMBERED_PREFIX_RE.match(name):
            continue
        item = parse_adopted_implementation_filename(name)
        if item is None:
            findings.append(
                f"{name}: numbered adopted-implementation filename is not parseable "
                "(expected layer_NN_home.md, layer_NNx_part.md, or layer_NN_a_part.md)"
            )
            continue
        parsed.append(item)

    by_family: dict[tuple[str, str], list[AdoptedImplementationName]] = defaultdict(list)
    by_part: dict[tuple[str, str, str], list[AdoptedImplementationName]] = defaultdict(list)
    for item in parsed:
        by_family[item.family_key].append(item)
        by_part[item.part_key].append(item)

    for (layer, number), files in sorted(by_family.items()):
        if len(files) > 1:
            listed = ", ".join(item.filename for item in files)
            findings.append(f"{layer}_{number}: duplicate chapter number ({listed})")

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
    findings = audit_filenames(iter_adopted_implementation_filenames(root))
    if findings:
        print("Adopted implementation filename audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        return 1
    print("Adopted implementation filename audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
