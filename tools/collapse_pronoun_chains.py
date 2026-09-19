#!/usr/bin/env python3
"""Rebuild lists that were flattened into pronoun-led sentence chains.

Several CS protocol files contain runs like::

    This map must **identify key upstream and downstream systems**. It must
    **reflect resource flows**. It must **be updated at intervals**.

That is one requirement with three parts, written as three sentences that each
restate the subject and the modal. This restores the list::

    This map must:
    - identify key upstream and downstream systems;
    - reflect resource flows;
    - be updated at intervals.

The modal stays in the stem, so the obligation is unchanged and still reads as
one duty covering every item. Emphasis wrapping a whole item is dropped, since
it marked the fragment rather than any defined term.

A chain is only collapsed when every follower opens with a pronoun and repeats
the stem's modal verb, which is what makes it a restatement rather than a new
requirement.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRONOUNS = ("It", "They", "That", "Those", "These", "This")
VERBS = (
    "must not", "must", "should", "may", "includes", "include",
    "requires", "require", "triggers", "trigger", "considers", "consider",
    "applies", "apply",
)

SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
FOLLOWER_RE = re.compile(
    r"^(?:" + "|".join(PRONOUNS) + r")\s+(?P<verb>" + "|".join(VERBS) + r")\b\s*(?P<body>.*)$"
)


BOLD_SPAN_RE = re.compile(r"\*\*(.+?)\*\*")
NEGATION_RE = re.compile(r"^\**(?:not|never)\b", re.I)


def strip_wrapping_bold(text: str) -> str:
    """Drop emphasis from the list items that carries no meaning.

    Bolding a run of ordinary lowercase words -- ``**funding imbalances across
    interconnected systems**`` -- marks the fragment the sentence split created,
    not a term. A span holding a capitalised name, an italic descriptor, or a
    link is pointing at something, so it survives.
    """

    def unwrap(match: re.Match[str]) -> str:
        inner = match.group(1)
        if re.search(r"[A-Z0-9*\[\]()]", inner):
            return match.group(0)
        return inner

    stripped = text.strip()
    # Some source items bold the whole fragment and then bold a term inside it,
    # which markdown cannot nest. Drop the outer pair; the inner span was the
    # one meant to show.
    if stripped.startswith("**") and stripped.endswith("**") and "**" in stripped[2:-2]:
        stripped = stripped[2:-2].strip()

    result = BOLD_SPAN_RE.sub(unwrap, stripped).strip()
    return result if result.count("**") % 2 == 0 else stripped


def collapse_line(line: str) -> tuple[list[str], bool]:
    sentences = [s for s in SENTENCE_RE.split(line.strip()) if s.strip()]
    if len(sentences) < 3:
        return [line], False

    followers = [FOLLOWER_RE.match(s.strip()) for s in sentences[1:]]
    if not all(followers):
        return [line], False

    verbs = {m.group("verb") for m in followers}
    if len(verbs) != 1:
        return [line], False
    verb = verbs.pop()

    # A follower that negates -- "They must **not** be altered retroactively" --
    # states a prohibition, so folding it under a bare "must:" stem would put a
    # duty and its opposite in one list. Those chains are left for a human.
    if any(NEGATION_RE.match(m.group("body")) for m in followers):
        return [line], False

    head = sentences[0].rstrip()
    # The stem's modal is sometimes inside a bold run-in, as in
    # "**Changes to funding structures must** be proposed transparently."
    marker = re.search(rf"\b{re.escape(verb)}\b\**\s+", head)
    if not marker:
        return [line], False

    prefix = head[: marker.start()].rstrip()
    stem = f"{prefix} {verb}" + "**" * marker.group().count("**")
    first = head[marker.end() :].rstrip(".").strip()
    if not first:
        return [line], False

    # The split can land inside an open bold run-in, as in
    # "**Systems must monitor and disclose** ...". Close the span at the stem
    # and reopen it on the first item so both sides stay balanced. The colon
    # the caller appends then sits outside the emphasis, as list stems require.
    if stem.count("**") % 2:
        stem += "**"
        first = "**" + first

    items = [strip_wrapping_bold(first)]
    for match in followers:
        body = match.group("body").rstrip(".").strip()
        if not body:
            return [line], False
        items.append(strip_wrapping_bold(body))

    out = [f"{stem}:"]
    for item in items[:-1]:
        out.append(f"- {item};")
    out.append(f"- {items[-1]}.")
    return out, True


def collapse(text: str) -> tuple[str, int]:
    out: list[str] = []
    count = 0
    fenced = False
    depth = 0
    for line in text.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        stripped = line.strip()
        if "<details>" in stripped:
            depth += 1
        elif "</details>" in stripped:
            depth = max(0, depth - 1)

        skip = fenced or depth or not stripped
        # A paragraph may legitimately open with a bold run-in, so only real
        # list bullets ("- " / "* ") are excluded here.
        is_bullet = bool(re.match(r"^[-*+]\s", stripped))
        if skip or is_bullet or stripped.startswith(("#", "|", ">", "<")):
            out.append(line)
            continue

        replacement, changed = collapse_line(line)
        if changed:
            count += 1
        out.extend(replacement)
    result = "\n".join(out)
    if text.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    return result, count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--layer", default="corpus_systems")
    parser.add_argument("--file")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    base = root / args.layer
    if not base.is_dir():
        print(f"No such layer: {args.layer}", file=sys.stderr)
        return 2

    paths = [base / args.file] if args.file else sorted(base.glob("*.md"))
    total = changed = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        new_text, count = collapse(text)
        if not count:
            continue
        changed += 1
        total += count
        rel = path.relative_to(root).as_posix()
        print(f"{'wrote' if args.write else 'would collapse'} {rel}: {count} chains")
        if args.write:
            path.write_text(new_text, encoding="utf-8")
    print(f"\n{total} chains across {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
