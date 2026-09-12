#!/usr/bin/env python3
"""Flag parallel-norm risk in a draft answer.

Process support. Does not decide constitutional meaning. Checks:

- house-term misuse (court / tribunal / standing calculus / Router read / …)
- markdown citations whose fragments fail ``corpus_lookup.py validity``
- claim-like sentences with no owner stack (no ``core_*`` / companion link)
- skipped mandatory read-with when ``--query`` is supplied

Usage::

    python3 tools/parallel_norm_check.py --root . --file draft.md
    python3 tools/parallel_norm_check.py --root . --text "..."
    python3 tools/parallel_norm_check.py --root . --file draft.md --query "CJS-R09"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

import corpus_lookup  # noqa: E402

MD_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")
CLAIM_HINT = re.compile(
    r"\b(must|shall|required|forbidden|non-compliant|duty|obligation)\b",
    re.IGNORECASE,
)
OWNER_FILE = re.compile(
    r"(?:core_|corpus_(?:joint_structure|systems|institutions|forum))"
)

HOUSE_TERMS: tuple[tuple[str, str, str], ...] = (
    (r"\bcourts?\b", "court", "forums / forum family / adjudicative body"),
    (r"\btribunals?\b", "tribunal", "forum / forums / panel / bench"),
    (r"\bstanding[- ]calculus\b", "standing calculus", "standing measurement"),
    (r"\bRouter read\b", "Router read", "Topic routing (primary owner) / (mandatory read-with)"),
    (
        r"\bfiled claim is not standing\b",
        "filed claim is not standing",
        "filed case is not standing by itself",
    ),
    (r"\bChapter Zero\b|\bChapter 00\b", "Chapter Zero", "Preamble"),
    (
        r"\bstakeholder governance\b|\bconstitutional governance layer\b|\bstakeholder[- ]layer\b",
        "governance layer label",
        "Constitutional Contract Layer / Stakeholder System Participation",
    ),
)


def flags_for_house_terms(text: str) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for pattern, avoid, prefer in HOUSE_TERMS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            hits.append(
                {
                    "kind": "house_term",
                    "avoid": avoid,
                    "prefer": prefer,
                    "excerpt": match.group(0),
                }
            )
    return hits


def citation_targets(text: str) -> list[tuple[str, str | None]]:
    out: list[tuple[str, str | None]] = []
    for match in MD_LINK.finditer(text):
        target = match.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        path, _, frag = target.partition("#")
        path = path.split("?")[0]
        if not path.endswith(".md"):
            continue
        # Strip leading ../
        while path.startswith("../"):
            path = path[3:]
        path = path.lstrip("./")
        out.append((path, f"#{frag}" if frag else None))
    return out


def flags_for_validity(indexes: corpus_lookup.Indexes, text: str) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for file_rel, anchor in citation_targets(text):
        if not anchor:
            continue
        path = indexes.root / file_rel
        if not path.is_file():
            hits.append(
                {
                    "kind": "missing_file",
                    "file": file_rel,
                    "anchor": anchor,
                }
            )
            continue
        ident = anchor.lstrip("#")
        source = path.read_text(encoding="utf-8")
        if f'id="{ident}"' not in source:
            from generate_plain_terms_edition import HEADING_RE, auto_slug, clean_title

            slugs = set()
            for line in source.splitlines():
                match = HEADING_RE.match(line)
                if match:
                    slugs.add(auto_slug(clean_title(match.group(2))))
            if ident not in slugs:
                hits.append(
                    {
                        "kind": "missing_anchor",
                        "file": file_rel,
                        "anchor": anchor,
                    }
                )
                continue
        result = corpus_lookup.cmd_validity(indexes, file_rel, anchor)
        if result["status"] == "fossil":
            hits.append(
                {
                    "kind": "validity",
                    "file": file_rel,
                    "anchor": anchor,
                    "status": result["status"],
                }
            )
    return hits


def flags_for_owner(text: str) -> list[dict[str, str]]:
    if not CLAIM_HINT.search(text):
        return []
    if OWNER_FILE.search(text) or MD_LINK.search(text):
        return []
    return [
        {
            "kind": "no_owner",
            "detail": "claim-like language with no core_* or companion citation",
        }
    ]


def flags_for_read_with(
    indexes: corpus_lookup.Indexes, text: str, query: str | None
) -> list[dict[str, str]]:
    if not query:
        return []
    try:
        routed = corpus_lookup.cmd_route(indexes, query)
    except corpus_lookup.LookupError_:
        return []
    missing: list[dict[str, str]] = []
    haystack = text.casefold()
    for owner in routed.get("read_with") or []:
        href = str(owner.get("href") or "")
        file_rel = href.split("#", 1)[0]
        ident = str(owner.get("id") or "")
        if file_rel and file_rel.casefold() in haystack:
            continue
        if ident and ident.casefold() in haystack:
            continue
        missing.append(
            {
                "kind": "skipped_read_with",
                "id": ident,
                "href": href,
            }
        )
    return missing


def check_text(
    indexes: corpus_lookup.Indexes, text: str, query: str | None
) -> dict[str, Any]:
    flags: list[dict[str, str]] = []
    flags.extend(flags_for_house_terms(text))
    flags.extend(flags_for_validity(indexes, text))
    flags.extend(flags_for_owner(text))
    flags.extend(flags_for_read_with(indexes, text, query))
    return {
        "status": "process_support_not_binding",
        "cannot_narrow_core": True,
        "edition": indexes.edition,
        "ok": not flags,
        "flag_count": len(flags),
        "flags": flags,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--file", dest="source_file")
    src.add_argument("--text")
    p.add_argument("--query", help="Optional fact pattern or topic; checks skipped read-with.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    try:
        indexes = corpus_lookup.load_indexes(root)
    except (corpus_lookup.EditionMismatch, FileNotFoundError) as exc:
        sys.stderr.write(f"{exc}\n")
        return 2
    if args.source_file:
        text = Path(args.source_file).read_text(encoding="utf-8")
    else:
        text = args.text
    payload = check_text(indexes, text, args.query)
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
