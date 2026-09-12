#!/usr/bin/env python3
"""Prove that a plain-language rewrite did not change any obligation.

Extracts every normative clause from a file -- statements carrying ``must``,
``must not``, ``may``, ``may not``, ``required``, ``prohibited``, ``shall``, or
``should`` -- and records its modality together with the content words around
it. Comparing the inventory before and after a rewrite makes an added, dropped,
or weakened obligation visible even when the wording changed completely.

Modality is the part that must never move: turning ``must not`` into ``may``,
or dropping a ``must`` sentence entirely, fails the diff. Rewording within one
modality is expected and passes as long as the subject matter still lines up.

Usage::

    # snapshot before editing
    python3 tools/obligation_inventory_diff.py --root . --snapshot before.json \\
        --paths corpus_forum/cf_10_technical_specialist_forums_specialist_chambers.md

    # after editing, compare
    python3 tools/obligation_inventory_diff.py --root . --compare before.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Ordered longest-first so "must not" wins over "must".
MODALITIES = (
    ("must not", "PROHIBITION"),
    ("shall not", "PROHIBITION"),
    ("may not", "PROHIBITION"),
    ("must never", "PROHIBITION"),
    ("is prohibited", "PROHIBITION"),
    ("are prohibited", "PROHIBITION"),
    ("prohibited", "PROHIBITION"),
    ("non-compliant", "PROHIBITION"),
    ("must", "DUTY"),
    ("shall", "DUTY"),
    ("is required", "DUTY"),
    ("are required", "DUTY"),
    ("required", "DUTY"),
    ("should", "EXPECTATION"),
    ("may", "PERMISSION"),
)

# Colons and semicolons punctuate within a sentence: "these must be documented:
# timing, format, ..." is one obligation, and splitting there would strand the
# enumeration outside the duty that governs it.
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
WORD_RE = re.compile(r"[a-z][a-z-]{2,}")

# Structural noise that carries no obligation of its own.
STOPWORDS = {
    "the", "and", "that", "this", "those", "these", "with", "for", "from", "not",
    "any", "all", "must", "shall", "may", "should", "required", "prohibited",
    "where", "when", "which", "each", "such", "under", "into", "than", "then",
    "are", "was", "were", "been", "being", "have", "has", "had", "its", "their",
    "other", "within", "without", "must-not", "also", "including", "include",
    "includes", "included", "over", "per", "via", "but", "who", "whom", "does",
}


def content_terms(text: str) -> set[str]:
    return {
        word
        for word in WORD_RE.findall(text.lower())
        if word not in STOPWORDS
    }


def strip_noise(text: str) -> str:
    """Remove markdown that changes freely without changing obligations."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`[^`]*`", " ", text)
    text = text.replace("**", "").replace("*", "")
    return re.sub(r"\s+", " ", text).strip()


def modal_hits(sentence: str) -> list[tuple[int, int, str]]:
    """Every modal phrase in a sentence, as (start, end, kind), non-overlapping.

    One sentence often carries more than one obligation -- "architecture should
    be modular, and changes must not break other systems" is an expectation and
    a prohibition. Recording only the first would make an honest split into two
    sentences look like an invented obligation.
    """
    lowered = sentence.lower()
    hits: list[tuple[int, int, str]] = []
    taken: list[tuple[int, int]] = []
    for phrase, kind in MODALITIES:
        for match in re.finditer(rf"\b{re.escape(phrase)}\b", lowered):
            span = match.span()
            if any(span[0] < end and start < span[1] for start, end in taken):
                continue
            taken.append(span)
            hits.append((span[0], span[1], kind))
    return sorted(hits)


LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\S")


def operative_lines(path: Path) -> list[str]:
    """Body lines only: widget interiors and glosses state no new obligation.

    A line ending in a colon is joined to the list it introduces. "Each
    institution must name the office responsible for:" governs every bullet
    beneath it, so the bullets belong to that duty; read apart from the stem
    they look like free-floating text, and moving an item between the stem and
    a bullet would register as an obligation appearing from nowhere.
    """
    raw = path.read_text(encoding="utf-8").splitlines()

    body: list[str] = []
    depth = 0
    for line in raw:
        stripped = line.strip()
        if "<details>" in stripped:
            depth += 1
            continue
        if "</details>" in stripped:
            depth = max(0, depth - 1)
            continue
        if depth:
            continue
        if stripped.startswith(("#", "<", "---", "*In plain terms", "|", "> ")):
            body.append("")
            continue
        body.append(line.rstrip())

    out: list[str] = []
    index = 0
    while index < len(body):
        line = body[index]
        stripped = line.strip()
        index += 1
        if not stripped:
            continue
        if not stripped.endswith(":"):
            out.append(stripped)
            continue

        merged = [stripped.rstrip(":")]
        stem_indent = len(line) - len(line.lstrip())
        stem_is_item = bool(LIST_ITEM_RE.match(line))
        cursor = index
        while cursor < len(body) and not body[cursor].strip():
            cursor += 1
        while cursor < len(body) and LIST_ITEM_RE.match(body[cursor]):
            item_indent = len(body[cursor]) - len(body[cursor].lstrip())
            # A bullet ending in a colon governs only the items nested under it;
            # its siblings belong to whatever stem introduced the outer list.
            if stem_is_item and item_indent <= stem_indent:
                break
            item = body[cursor].strip().lstrip("-*+ ").strip()
            # Item-terminating punctuation is list formatting, not a sentence end.
            merged.append(item.rstrip(";").rstrip())
            cursor += 1
            while cursor < len(body) and not body[cursor].strip():
                peek = cursor
                while peek < len(body) and not body[peek].strip():
                    peek += 1
                if peek < len(body) and LIST_ITEM_RE.match(body[peek]):
                    cursor = peek
                break
        if len(merged) > 1:
            out.append(merged[0] + ": " + ", ".join(merged[1:]))
            index = cursor
        else:
            out.append(stripped)
    return out


CONNECTOR_RE = re.compile(r",\s+(?:and|or|but)\s+|;\s+|,\s+(?=\w)|\s+(?:and|or|but)\s+")


def clause_boundary(sentence: str, after: int, before: int) -> int:
    """Where one modal clause ends and the next begins.

    Cut at the last conjunction between the two modal phrases, so each clause
    keeps its own subject and object. Without this, "architecture should be
    modular and changes must not break other systems" hands the modularity
    wording to the prohibition, and a faithful split then looks like drift.
    """
    span = sentence[after:before]
    cuts = list(CONNECTOR_RE.finditer(span))
    if cuts:
        return after + cuts[-1].start()
    return after + len(span) // 2


def inventory(path: Path) -> list[dict]:
    """One record per modal clause, not per sentence."""
    found: list[dict] = []
    for line in operative_lines(path):
        clean = strip_noise(line)
        for sentence in SENTENCE_SPLIT_RE.split(clean):
            sentence = sentence.strip(" -–—•")
            if len(sentence) < 12:
                continue
            hits = modal_hits(sentence)
            if not hits:
                continue
            bounds = [0]
            for index in range(len(hits) - 1):
                bounds.append(clause_boundary(sentence, hits[index][1], hits[index + 1][0]))
            bounds.append(len(sentence))
            for index in range(len(hits)):
                kind = hits[index][2]
                clause = sentence[bounds[index] : bounds[index + 1]].strip(" ,;:-–—")
                found.append(
                    {
                        "modality": kind,
                        "terms": sorted(content_terms(clause)),
                        "text": clause[:220],
                    }
                )
    return found


def build(root: Path, paths: list[str]) -> dict:
    return {
        "generated": dt.date.today().isoformat(),
        "files": {rel: inventory(root / rel) for rel in paths},
    }


def modality_vocabulary(items: list[dict]) -> dict[str, set[str]]:
    """All content terms available at each modality strength."""
    vocab: dict[str, set[str]] = {}
    for item in items:
        vocab.setdefault(item["modality"], set()).update(item["terms"])
    return vocab


def coverage(item: dict, vocab: dict[str, set[str]]) -> float:
    """Fraction of a clause's content terms still spoken at the same strength.

    Coverage rather than pairwise similarity, because splitting one duty into
    two shorter duties should pass: the terms are all still there, just spread
    across more clauses. Dropping the duty, or restating it as a permission,
    moves those terms out of the modality and the score collapses.
    """
    terms = set(item["terms"])
    if not terms:
        return 1.0
    return len(terms & vocab.get(item["modality"], set())) / len(terms)


def compare(before: dict, after: dict, threshold: float) -> tuple[list[str], list[str]]:
    """Return (failures, notes).

    Splitting one long duty into two shorter duties is the point of a
    plain-language rewrite, so counts are reported as notes rather than
    failures. What must hold is coverage in both directions: every obligation
    that existed still exists at the same strength (nothing dropped or
    weakened), and every obligation now present traces back to one that did
    (nothing invented).
    """
    failures: list[str] = []
    notes: list[str] = []

    for rel, old_items in before["files"].items():
        new_items = after["files"].get(rel)
        if new_items is None:
            failures.append(f"{rel}: file missing from the after-snapshot")
            continue

        old_counts = Counter(item["modality"] for item in old_items)
        new_counts = Counter(item["modality"] for item in new_items)
        for modality in sorted(set(old_counts) | set(new_counts)):
            if old_counts[modality] != new_counts[modality]:
                notes.append(
                    f"{rel}: {modality} clause count {old_counts[modality]} -> "
                    f"{new_counts[modality]} (split or merged; coverage still checked)"
                )

        new_vocab = modality_vocabulary(new_items)
        old_vocab = modality_vocabulary(old_items)

        for item in old_items:
            score = coverage(item, new_vocab)
            if score < threshold:
                missing = sorted(set(item["terms"]) - new_vocab.get(item["modality"], set()))
                failures.append(
                    f"{rel}: DROPPED or WEAKENED {item['modality']} "
                    f"({score:.0%} of terms survive; missing {missing[:8]}): "
                    f"{item['text'][:130]!r}"
                )

        for item in new_items:
            score = coverage(item, old_vocab)
            if score < threshold:
                added = sorted(set(item["terms"]) - old_vocab.get(item["modality"], set()))
                failures.append(
                    f"{rel}: ADDED {item['modality']} not in the source "
                    f"({score:.0%} of terms traceable; new {added[:8]}): "
                    f"{item['text'][:130]!r}"
                )

    return failures, notes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--paths", nargs="*", help="Repository-relative markdown paths.")
    parser.add_argument("--snapshot", help="Write an inventory to this JSON path.")
    parser.add_argument("--compare", help="Compare current state against this snapshot.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.75,
        help="Minimum fraction of a clause's terms that must survive at the same modality.",
    )
    parser.add_argument("--write-evidence", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    if args.compare:
        before = json.loads(Path(args.compare).read_text(encoding="utf-8"))
        after = build(root, list(before["files"]))
        findings, notes = compare(before, after, args.threshold)

        if args.write_evidence:
            out_dir = root / "evidence" / dt.date.today().isoformat()
            out_dir.mkdir(parents=True, exist_ok=True)
            # Name the artifact after its snapshot so successive tranches do
            # not overwrite one another's evidence.
            stem = Path(args.compare).stem.replace("obligation_snapshot", "").strip("_")
            suffix = f"_{stem}" if stem else ""
            target = out_dir / f"obligation_inventory_diff{suffix}.json"
            target.write_text(
                json.dumps(
                    {
                        "before": before,
                        "after": after,
                        "findings": findings,
                        "notes": notes,
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
            print(f"Evidence: {target.relative_to(root)}")

        total_before = sum(len(v) for v in before["files"].values())
        total_after = sum(len(v) for v in after["files"].values())
        print(f"Obligations before: {total_before}, after: {total_after}")
        for note in notes:
            print(f"  note: {note}")
        if findings:
            print("Obligation inventory diff FAILED:", file=sys.stderr)
            for item in findings:
                print(f"  - {item}", file=sys.stderr)
            print(f"Total: {len(findings)}", file=sys.stderr)
            return 1
        print("Obligation inventory diff OK: every obligation matched 1:1.")
        return 0

    if not args.paths:
        print("Provide --paths when taking a snapshot.", file=sys.stderr)
        return 2
    data = build(root, args.paths)
    total = sum(len(v) for v in data["files"].values())
    target = Path(args.snapshot or "obligation_inventory.json")
    target.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Captured {total} obligations across {len(data['files'])} files -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
