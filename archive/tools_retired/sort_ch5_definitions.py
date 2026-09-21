#!/usr/bin/env python3
"""Retired Chapter Five relocation helper.

This script previously moved definition blocks according to location-routing
rules. Chapter Five now uses a single-definition model instead: edit the one
real definition home directly, keep directory rows unique, and validate with
``make ch5-single-definition-audit``.
"""

from __future__ import annotations

import sys


def main() -> int:
    print(
        "sort_ch5_definitions.py is retired. "
        "Use manual edits plus `make ch5-single-definition-audit`."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
