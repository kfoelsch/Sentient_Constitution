#!/usr/bin/env python3
"""Compatibility wrapper for the Chapter Five single-definition audit.

The former checker searched for placeholder-only and locator-style entries.
The current rule is centralized in ``ch5_single_definition_audit.py``: one
visible definition entry per label, one directory row per label, no
placeholder-only definition bodies, and no repeated cluster-owner roster member.
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
