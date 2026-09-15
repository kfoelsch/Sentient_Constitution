#!/usr/bin/env python3
"""Retired compatibility wrapper for the Chapter Five single-definition audit.

The old script removed alphabetical locator shells from Chapter Five section 2.
That cleanup is no longer a one-off rewrite path: the repository now enforces
the invariant directly with ``ch5_single_definition_audit.py``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_single_definition_audit import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
