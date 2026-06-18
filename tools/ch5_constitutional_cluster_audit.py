#!/usr/bin/env python3
"""Audit Chapter Five constitutional band placement and compass completeness."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from ch5_paths import CH5_BANDS, CH5_INDEX

COMPASS_ANCHOR = "chapter-five-compass-and-definition-map"
TRACE_BLOCK_RE = re.compile(
    r"<details>\s*\n<summary><strong><span style=\"color: #2563eb;\">Trace</span></strong></summary>\s*\n(.*?)\n</details>",
    re.DOTALL,
)
CLUSTER_HEADING_RE = re.compile(r"^#### (3\.\d+) .+$", re.MULTILINE)

EXPECTED_CLUSTER_IDS = [
    "3.2", "3.3", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10",
    "3.11", "3.12", "3.13", "3.14", "3.15", "3.16",
]

BAND_CLUSTER_RANGES = {
    "core_05o_oversight_definitions.md": {"3.2", "3.3"},
    "core_05p_participation_definitions.md": {"3.5", "3.6", "3.7"},
    "core_05a_accountability_definitions.md": {"3.8", "3.9", "3.10", "3.11"},
    "core_05c_continuity_definitions.md": {"3.12", "3.13", "3.14", "3.15"},
    "core_05i_integrative_definitions.md": {"3.16"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    failures: list[str] = []

    index_path = root / CH5_INDEX
    if not index_path.is_file():
        failures.append(f"Missing Chapter Five index: {CH5_INDEX}")
    else:
        index_text = index_path.read_text(encoding="utf-8")
        if COMPASS_ANCHOR not in index_text:
            failures.append(f"{CH5_INDEX}: missing compass anchor #{COMPASS_ANCHOR}")
        if "Constitutional bands" not in index_text:
            failures.append(f"{CH5_INDEX}: missing constitutional bands table")

    found_clusters: set[str] = set()
    for band_file in CH5_BANDS:
        path = root / band_file
        if not path.is_file():
            failures.append(f"Missing band file: {band_file}")
            continue
        text = path.read_text(encoding="utf-8")
        ids = set(CLUSTER_HEADING_RE.findall(text))
        expected = BAND_CLUSTER_RANGES[band_file]
        if ids != expected:
            failures.append(
                f"{band_file}: cluster ID mismatch expected {sorted(expected)} got {sorted(ids)}"
            )
        found_clusters |= ids
        for cid in ids:
            block_m = re.search(rf"^#### {re.escape(cid)} .+$", text, re.MULTILINE)
            if not block_m:
                continue
            start = block_m.start()
            chunk = text[start : start + 4000]
            trace_m = TRACE_BLOCK_RE.search(chunk)
            if not trace_m:
                failures.append(f"{band_file}: §{cid} missing Trace block")
                continue
            trace_body = trace_m.group(1)
            if "Constitutional frame:" not in trace_body:
                failures.append(f"{band_file}: §{cid} Trace missing Constitutional frame")

    missing = set(EXPECTED_CLUSTER_IDS) - found_clusters
    extra = found_clusters - set(EXPECTED_CLUSTER_IDS)
    if missing:
        failures.append(f"Missing §3 clusters: {sorted(missing)}")
    if extra:
        failures.append(f"Unexpected §3 clusters: {sorted(extra)}")

    if failures:
        print("FAIL: Chapter Five constitutional cluster audit:")
        for f in failures:
            print(f"  - {f}")
        return 1

    print("PASS: Chapter Five constitutional band files and compass checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
