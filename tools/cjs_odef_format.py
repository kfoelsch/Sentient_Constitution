#!/usr/bin/env python3
"""Shared CJS-3 oDef guidepost block detection helpers."""

from __future__ import annotations

import re

# Titled entry followed by guidepost O/M/A/C headers (plain-terms optional).
GUIDEPOST_BLOCK_RE = re.compile(
    r"^(?P<title>[^\n]{2,200})\n"
    r"(?:\*In plain terms:[^\n]*\n\n)?"
    r"- \*\*What it is\*\*\n"
    r"(?P<body>"
    r"(?:.+\n)*?"
    r"- \*\*What must hold\*\*\n"
    r"(?:.+\n)*?"
    r"  - \*\*Primary failure:\*\*[^\n]*)",
    re.MULTILINE,
)

WHAT_IT_IS_RE = re.compile(r"(?m)^- \*\*What it is\*\*\s*$")
HOW_MEASURE_RE = re.compile(r"(?m)^- \*\*How to measure and assess\*\*\s*$")
WHAT_MUST_HOLD_RE = re.compile(r"(?m)^- \*\*What must hold\*\*\s*$")
# Consolidated `- **In scope:**` or dimensional `- **In scope — {dimension}:**`
# (doc_architecture.md Measurement-informed O/M/A/C).
IN_SCOPE_RE = re.compile(r"(?m)^\s*- \*\*In scope(?:\s*—[^:]+)?:\*\*")
OUT_SCOPE_RE = re.compile(r"(?m)^\s*- \*\*Out of scope:\*\*")
PRIMARY_MEASURE_RE = re.compile(r"(?m)^\s*- \*\*Primary measure:\*\*")
PRIMARY_ASSESS_RE = re.compile(r"(?m)^\s*\*\*Primary assessment:\*\*")
PRIMARY_FAILURE_RE = re.compile(r"(?m)^\s*- \*\*Primary failure:\*\*")
LEGACY_OP_RE = re.compile(r"(?m)^- OP-[OEC]:")


def titled_guidepost_entries(text: str) -> list[str]:
    """Return titled entry names that open a guidepost oDef block.

    A title is a non-markup line whose next non-empty neighbor is either
    ``*In plain terms:…*`` or ``- **What it is**``.
    """
    titles: list[str] = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith(("-", "#", "|", "<", ">", "`")):
            continue
        if stripped.startswith("*In plain terms:"):
            continue
        # Prose sentences are not titles.
        if stripped.endswith(".") and not stripped.startswith("**"):
            continue
        if len(stripped) > 140:
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines):
            continue
        nxt = lines[j].strip()
        if nxt.startswith("*In plain terms:") or nxt == "- **What it is**":
            titles.append(stripped)
    return titles


def guidepost_complete(body: str) -> tuple[bool, bool, bool]:
    """Return (has_o, has_measure_assess, has_c) for a guidepost block body."""
    has_o = bool(WHAT_IT_IS_RE.search(body) and IN_SCOPE_RE.search(body) and OUT_SCOPE_RE.search(body))
    has_m = bool(
        HOW_MEASURE_RE.search(body)
        and PRIMARY_MEASURE_RE.search(body)
        and PRIMARY_ASSESS_RE.search(body)
    )
    has_c = bool(WHAT_MUST_HOLD_RE.search(body) and PRIMARY_FAILURE_RE.search(body))
    return has_o, has_m, has_c
