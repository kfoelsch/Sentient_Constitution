#!/usr/bin/env python3
"""Historical helper: Article V subsection relabel (former I-B..I-G → I-A..I-E).

Applied to the corpus on 2026-04-10. Do **not** re-run the naive composite-then-replace
sequence: expanding "**Articles V-E and I-F**" to "**Articles V-C and I-D**" and then
running a second pass that rewrites **Articles V-C** will corrupt the string.

Safe pattern for future migrations: encode `Article V-[BCEFG]` as opaque tokens first,
apply token-level composites, then map tokens to final letters.

This file is kept as a record only.
"""

raise SystemExit(
    "Disabled: one-shot migration complete. See git history if you need the old script body."
)
