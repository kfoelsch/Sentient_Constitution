#!/usr/bin/env python3
"""Keep only the newest audit evidence runs (AUDIT-EVIDENCE-RETENTION-01).

Audits write their reports, matrices and logs under ``evidence/<date>/``. This
script keeps the newest ``keep`` runs of each audit family (default 2) and
deletes the files of every older run, so the third-to-last run is removed as
soon as a new one exists.

Only files named in ``tools/architecture/audit_evidence_retention.json`` are
ever touched. Hand-written records that share the dated folders (evaluations,
resolutions, decision notes) are not audit output and are never deleted.

A "run" of a family is a dated folder (``evidence/YYYY-MM-DD/``) that holds at
least one file of the family. Several runs on one day share the folder, so they
count once.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CONFIG = Path("tools/architecture/audit_evidence_retention.json")
_DATE_DIR = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_DATE_TOKEN = "{date}"
_DATE_RE = r"\d{4}-\d{2}-\d{2}"


def load_config(root: Path) -> dict:
    data = json.loads((root / CONFIG).read_text(encoding="utf-8"))
    if not isinstance(data.get("keep"), int) or data["keep"] < 1:
        raise ValueError("audit_evidence_retention.json: 'keep' must be an integer >= 1")
    if not isinstance(data.get("families"), dict) or not data["families"]:
        raise ValueError("audit_evidence_retention.json: 'families' must be a non-empty object")
    return data


def _compile(template: str) -> re.Pattern[str]:
    parts = [re.escape(piece) for piece in template.split(_DATE_TOKEN)]
    return re.compile("^" + _DATE_RE.join(parts) + "$")


def dated_folders(root: Path) -> list[Path]:
    base = root / "evidence"
    if not base.is_dir():
        return []
    return sorted(p for p in base.iterdir() if p.is_dir() and _DATE_DIR.match(p.name))


def plan(root: Path, keep: int | None = None) -> dict[str, list[Path]]:
    """Return {family: files to delete}, newest ``keep`` runs per family kept."""
    config = load_config(root)
    keep = keep or config["keep"]
    folders = dated_folders(root)
    doomed: dict[str, list[Path]] = {}
    for family, templates in sorted(config["families"].items()):
        patterns = [_compile(t) for t in templates]
        runs: list[tuple[Path, list[Path]]] = []
        for folder in folders:
            matched = [
                f for f in sorted(folder.iterdir())
                if f.is_file() and any(p.match(f.name) for p in patterns)
            ]
            if matched:
                runs.append((folder, matched))
        for _folder, files in runs[: max(len(runs) - keep, 0)]:
            doomed.setdefault(family, []).extend(files)
    return doomed


def prune(root: Path, keep: int | None = None, dry_run: bool = False) -> list[Path]:
    doomed = plan(root, keep)
    removed: list[Path] = []
    for files in doomed.values():
        for path in files:
            if not dry_run:
                path.unlink()
            removed.append(path)
    if not dry_run:
        for folder in dated_folders(root):
            if not any(folder.iterdir()):
                folder.rmdir()
    return removed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--keep", type=int, default=None, help="runs to keep per family (default: from config)")
    parser.add_argument("--dry-run", action="store_true", help="list what would be deleted; delete nothing")
    parser.add_argument("--quiet", action="store_true", help="print nothing unless files were removed")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    removed = prune(root, args.keep, args.dry_run)
    verb = "would delete" if args.dry_run else "deleted"
    if removed or not args.quiet:
        families = len(plan(root, args.keep)) if args.dry_run else None
        suffix = f" across {families} audit families" if families is not None else ""
        print(f"audit evidence retention: {verb} {len(removed)} files{suffix}")
        if args.dry_run:
            for path in removed:
                print(f"  {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
