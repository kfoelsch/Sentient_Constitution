#!/usr/bin/env python3
"""Report Chapter Five definition-directory drift in reader-language indexes.

The localized Chapter Five Part A files are indexes. This audit compares the
current English A–Z definition directory with the source snapshot at the most
recent commit that updated each locale's translated index. It reports both
whole-directory coverage drift and entries added or removed since that
baseline. It does not judge translation quality or scan the full Chapter Five
band files.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_INDEX = "core_05__definitions_home.md"
LOCALES = "es hi ar id zh pt bn fr ur ru ja tr mr vi fa te ko ta th".split()
DEFINITION_START = '<a id="definitions-a-z"></a>'
CLUSTER_START = '<a id="clusters-a-z"></a>'
ENTRY_RE = re.compile(r"^\s*-\s+\[([^\]]+)\]\(([^)]+)\)\s*$", re.MULTILINE)


@dataclass(frozen=True)
class Entry:
    label: str
    target_file: str
    anchor: str

    @property
    def key(self) -> tuple[str, str]:
        return (self.target_file, normalize_anchor(self.anchor))


def normalize_anchor(anchor: str) -> str:
    """Normalize the common localized ``-constitutional`` suffix."""
    return anchor.removesuffix("-constitutional")


def git_text(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def parse_entries(text: str, source: str) -> list[Entry]:
    try:
        begin = text.index(DEFINITION_START) + len(DEFINITION_START)
        end = text.index(CLUSTER_START, begin)
    except ValueError as exc:
        raise ValueError(f"{source}: missing stable A–Z directory anchors") from exc

    entries: list[Entry] = []
    for label, target in ENTRY_RE.findall(text[begin:end]):
        if "#" not in target:
            continue
        target_file, anchor = target.rsplit("#", 1)
        entries.append(Entry(label.strip(), Path(target_file).name, anchor))
    return entries


def latest_index_commit(locale: str) -> str:
    path = f"translations/{locale}/{SOURCE_INDEX}"
    commit = git_text("log", "-1", "--format=%H", "--", path).strip()
    if not commit:
        raise ValueError(f"No Git history found for {path}")
    return commit


def read_index_at(commit: str) -> str:
    return git_text("show", f"{commit}:{SOURCE_INDEX}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--baseline",
        help="Git commit to compare against (default: latest common translation-index commit)",
    )
    args = parser.parse_args()

    try:
        baselines = {locale: latest_index_commit(locale) for locale in LOCALES}
        unique = set(baselines.values())
        if args.baseline:
            baseline = args.baseline
        elif len(unique) == 1:
            baseline = unique.pop()
        else:
            details = ", ".join(f"{k}={v[:10]}" for k, v in baselines.items())
            raise ValueError(
                "Locale index histories do not share a baseline; pass --baseline explicitly. "
                + details
            )

        current_source = (ROOT / SOURCE_INDEX).read_text(encoding="utf-8")
        baseline_source = read_index_at(baseline)
        current_entries = parse_entries(current_source, SOURCE_INDEX)
        baseline_entries = parse_entries(baseline_source, f"{baseline}:{SOURCE_INDEX}")
        current_by_label = {entry.label: entry for entry in current_entries}
        baseline_by_label = {entry.label: entry for entry in baseline_entries}
        added = [entry for entry in current_entries if entry.label not in baseline_by_label]
        removed = [entry for entry in baseline_entries if entry.label not in current_by_label]

        print(f"Chapter Five definitions: {len(baseline_entries)} at {baseline[:10]} → {len(current_entries)} now")
        print(f"Added since translation baseline: {len(added)}")
        for entry in added:
            print(f"  + {entry.label} [{entry.target_file}#{entry.anchor}]")
        print(f"Removed or renamed since translation baseline: {len(removed)}")
        for entry in removed:
            print(f"  - {entry.label} [{entry.target_file}#{entry.anchor}]")

        any_gaps = False
        for locale in LOCALES:
            path = ROOT / "translations" / locale / SOURCE_INDEX
            translated_entries = parse_entries(path.read_text(encoding="utf-8"), str(path))
            translated_keys = {entry.key for entry in translated_entries}
            current_keys = {entry.key for entry in current_entries}
            missing = [entry for entry in current_entries if entry.key not in translated_keys]
            stale = [entry for entry in translated_entries if entry.key not in current_keys]
            if missing or stale:
                any_gaps = True
            added_missing = [entry for entry in added if entry.key not in translated_keys]
            removed_stale = [entry for entry in removed if entry.key in translated_keys]
            print(
                f"{locale}: full coverage {len(missing)} missing / {len(stale)} stale; "
                f"since baseline {len(added_missing)} missing additions / {len(removed_stale)} stale removals"
            )
            for entry in missing:
                tag = "NEW-MISSING" if entry in added else "MISSING"
                print(f"  {tag:11} {entry.label} [{entry.target_file}#{entry.anchor}]")
            for entry in stale:
                print(f"  STALE    {entry.label} [{entry.target_file}#{entry.anchor}]")

        return 1 if any_gaps else 0
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"Chapter Five translation audit failed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
