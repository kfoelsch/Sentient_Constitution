#!/usr/bin/env python3
"""
Deprecated wrapper. Prefer:

  python3 tools/ch7_reorder_readability_iv_ix.py --repair-headings-only

That repairs mangled ###/#### Article headings in core_constitution.md after an
old cite pass touched heading lines.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    script = ROOT / "tools" / "ch7_reorder_readability_iv_ix.py"
    r = subprocess.run([sys.executable, str(script), "--repair-headings-only"], cwd=ROOT)
    raise SystemExit(r.returncode)


if __name__ == "__main__":
    main()
