"""Shrink-only baselines for audits that now run on the whole corpus (AUDIT-SCOPE-01).

An audit that used to check only added lines (``--changed-only``) now scans every corpus file.
Findings that already existed are recorded once in ``tools/architecture/baselines/<name>.json``
so the gate stays usable while the backlog is repaired. The baseline can only shrink:

* a finding that is not in the baseline fails (a new problem anywhere in the corpus);
* a baseline entry with no matching finding fails (the problem was fixed, so delete the entry).

Keys hold the file and the finding text, never the line number, so edits above a finding do not
disturb it. ``--write-baseline`` rewrites the file from the current findings.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

BASELINE_DIR = Path("tools/architecture/baselines")


def make_key(file: str, text: str, seen: Counter) -> str:
    norm = re.sub(r"\s+", " ", text).strip()
    digest = hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]
    base = f"{file}::{digest}"
    seen[base] += 1
    return base if seen[base] == 1 else f"{base}#{seen[base]}"


def load(root: Path, name: str) -> dict[str, str]:
    path = root / BASELINE_DIR / f"{name}.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {e["key"]: e.get("snippet", "") for e in data.get("entries", [])}


def write(root: Path, name: str, rule: str, entries: list[tuple[str, str]]) -> None:
    path = root / BASELINE_DIR / f"{name}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "rule": rule,
        "note": "Shrink-only backlog (AUDIT-SCOPE-01). Fix a finding, then delete its entry. Do not add entries by hand.",
        "entries": [{"key": k, "snippet": s[:160]} for k, s in sorted(entries)],
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def split(root: Path, name: str, keyed: list[tuple[str, str, object]]):
    """keyed: (key, snippet, finding). Returns (new_findings, stale_entries)."""
    baseline = load(root, name)
    current = {k for k, _s, _f in keyed}
    new = [f for k, _s, f in keyed if k not in baseline]
    stale = sorted(k for k in baseline if k not in current)
    return new, stale
