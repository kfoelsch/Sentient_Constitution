#!/usr/bin/env python3
"""One-shot: make file-top opening widgets contiguous.

Rewrites the region after the H1 and before the first body heading so that
Corpus placement / Reader guidance / Trace / D/A/C widgets sit together with
only blank lines between them. Owner/home lines, ``<br>``, ``---``, and other
prose move after the widget stack (with a single trailing ``<br>`` before that
prose when any remains).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import COMPANION_WRAPPERS, binding_corpus_scope
from widget_top_placement_audit import (
    DEC_SUMMARY,
    PLACEMENT_SUMMARY,
    READER_GUIDANCE_RE,
    TRACE_SUMMARY,
    classify_details,
    details_close_idx,
    heading_level,
    is_registry_annex,
    next_nonempty,
)

ROOT = Path(__file__).resolve().parents[1]
WRAPPER_NAMES = set(COMPANION_WRAPPERS)
STACK_KINDS = {"placement", "reader", "trace", "dac"}
PLAIN_TERMS_RE = re.compile(r"^\*In plain terms[:,]")
NON_OPERATIVE_SUBTITLE_RE = re.compile(r"^\*Non-operative subtitle:")
ANCHOR_RE = re.compile(r'^<a id="[^"]+"></a>\s*$')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--apply", action="store_true")
    return parser.parse_args()


def rewrite_file_top(lines: list[str], rel: str) -> list[str] | None:
    if Path(rel).name in WRAPPER_NAMES:
        return None

    first_heading = None
    for idx, line in enumerate(lines):
        if heading_level(line) == 1:
            first_heading = idx
            break
    if first_heading is None:
        return None

    body_start = len(lines)
    for idx in range(first_heading + 1, len(lines)):
        if heading_level(lines[idx]) is not None:
            body_start = idx
            break

    prefix = lines[: first_heading + 1]
    region = lines[first_heading + 1 : body_start]
    suffix = lines[body_start:]

    pre: list[str] = []
    widgets: list[list[str]] = []
    post: list[str] = []
    registry = is_registry_annex(rel)

    idx = 0
    seen_widget = False
    while idx < len(region):
        stripped = region[idx].strip()
        if stripped == "<details>":
            kind = classify_details(region, idx, len(region))
            close = details_close_idx(region, idx, len(region))
            if close is None:
                return None
            block = region[idx : close + 1]
            if kind in STACK_KINDS:
                widgets.append(block)
                seen_widget = True
            elif not seen_widget:
                pre.extend(block)
            else:
                post.extend(block)
            idx = close + 1
            continue

        if not seen_widget:
            if (
                not stripped
                or ANCHOR_RE.match(stripped)
                or NON_OPERATIVE_SUBTITLE_RE.match(stripped)
                or (registry and PLAIN_TERMS_RE.match(stripped))
            ):
                pre.append(region[idx])
                idx += 1
                continue
            # Unexpected pre-widget prose (for example a stray <br>) — park in post
            # only after widgets exist; otherwise keep in pre for registries/titles.
            if stripped == "<br>" or stripped == "---":
                idx += 1
                continue
            pre.append(region[idx])
            idx += 1
            continue

        # After widgets have started: drop only between-widget <br>; keep prose
        # and blank lines that belong to the post-stack body. Horizontal rules
        # move with the post body.
        if stripped == "<br>":
            idx += 1
            continue

        post.append(region[idx])
        idx += 1

    if not widgets:
        return None

    # Drop leading/trailing blanks in post; keep interior shape.
    while post and not post[0].strip():
        post.pop(0)
    while post and not post[-1].strip():
        post.pop()

    new_region: list[str] = []
    # Preserve a single blank after H1 when pre is empty.
    if pre:
        # Trim trailing blanks in pre.
        while pre and not pre[-1].strip():
            pre.pop()
        new_region.extend(pre)
        if new_region and new_region[-1].strip():
            new_region.append("")
    else:
        new_region.append("")

    for i, block in enumerate(widgets):
        if i:
            new_region.append("")
        new_region.extend(block)

    new_region.append("")
    new_region.append("<br>")
    if post:
        new_region.append("")
        new_region.extend(post)
        new_region.append("")

    rewritten = prefix + new_region + suffix
    if rewritten == lines:
        return None
    return rewritten


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    changed: list[str] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if not path.is_file() or path.suffix != ".md":
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        rewritten = rewrite_file_top(lines, rel)
        if rewritten is None:
            continue
        changed.append(rel)
        if args.apply:
            path.write_text("\n".join(rewritten) + "\n", encoding="utf-8")

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {len(changed)} file(s).")
    for rel in changed:
        print(f"  - {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
