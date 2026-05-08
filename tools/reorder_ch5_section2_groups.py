#!/usr/bin/env python3
"""Retired Chapter Five section-2 regrouping tool.

Chapter Five Part B is now maintained directly in topic groups while the
non-operative directory in Part A supplies the A-Z view. Automated regrouping
from anchor lists is intentionally retired so it cannot recreate locator rows
or old section-routing assumptions.
"""

from __future__ import annotations


def main() -> int:
    print(
        "retired: maintain Chapter Five Part B topic groups directly; "
        "run `make ch5-single-definition-audit` to verify the current rule."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
