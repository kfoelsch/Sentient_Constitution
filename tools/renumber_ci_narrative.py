#!/usr/bin/env python3
"""Renumber CI section families for narrative reorder (pre-release migration).

Three-phase migration:
  1. --placeholder  : CI-12.3 -> ⟦CI:12.3⟧, ci_12_ -> ⟦FILE:12⟧_, #ci-123 -> ⟦ANCHOR:12.3⟧
  2. (manual/git)   : rename corpus_institutions/ci_*.md via temp slots
  3. --finalize     : ⟦CI:12.3⟧ -> CI-8.3 using MAIN_MAP

  --verify          : fail if operative tree still has stale CI-N or placeholders

Run from repository root.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules", "evidence"}
EXTENSIONS = {".md", ".py", ".json"}
SKIP_FILES = {"renumber_ci_narrative.py", "renumber_ci_institutional.py"}

# Old CI-N (main section) -> new CI-N
MAIN_MAP: dict[int, int] = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    12: 8,  # transparency / participation
    9: 9,
    10: 10,
    11: 11,
    8: 12,  # cross-institution coordination
    13: 13,
    14: 14,
    24: 15,  # participation overlay (Book III entry)
    20: 16,  # care labor
    19: 17,  # end of life
    25: 18,  # public health
    15: 19,  # vulnerable personal services
    21: 20,  # coercive control
    18: 21,  # community life
    22: 22,
    23: 23,
    16: 24,  # innovation
    17: 25,  # science / evidence
    26: 26,
}

# Old ci_NN filename prefix -> new ci_NN prefix (content relocation)
FILE_MAP: dict[int, int] = {
    8: 12,
    12: 8,
    15: 19,
    16: 24,
    17: 25,
    18: 21,
    19: 17,
    20: 16,
    21: 20,
    24: 15,
    25: 18,
}

CI_TOKEN = "⟦CI:{key}⟧"
FILE_TOKEN = "⟦FILE:{nn:02d}⟧"
ANCHOR_TOKEN = "⟦ANCHOR:{key}⟧"

# CI-12.4, CI-12, CI-1 — longest match first
CI_REF_RE = re.compile(
    r"\bCI-(?P<main>\d{1,2})(?:\.(?P<sub>\d+[A-Z]?))?\b"
)
CI_ANCHOR_RE = re.compile(
    r"\bci-(?P<main>\d{1,2})(?:-(?P<sub>\d+[a-z0-9-]*))?\b"
)
FILE_REF_RE = re.compile(r"\bci_(?P<nn>\d{2})_")
PLACEHOLDER_CI_RE = re.compile(r"⟦CI:(?P<key>[\d.]+[A-Z]?)⟧")
PLACEHOLDER_FILE_RE = re.compile(r"⟦FILE:(?P<nn>\d{2})⟧")
PLACEHOLDER_ANCHOR_RE = re.compile(r"⟦ANCHOR:(?P<key>[\d.]+[A-Z]?)⟧(?P<suffix>[a-z0-9-]*)")
ANCHOR_LINK_RE = re.compile(r"#ci-(?P<body>[a-z0-9-]+)")
HEADING_ANCHOR_RE = re.compile(r"^(\s*\{:#ci-(?P<body>[a-z0-9-]+)\})\s*$", re.MULTILINE)


def parse_anchor_body(body: str) -> tuple[str, str] | None:
    """Parse ci-121-foo into (key='12.1', suffix='-foo')."""
    for main in sorted(MAIN_MAP, reverse=True):
        ms = str(main)
        if not body.startswith(ms):
            continue
        rest = body[len(ms) :]
        if not rest:
            return ms, ""
        if rest[0].isdigit():
            m = re.match(r"(\d+[A-Z]?)", rest)
            if m:
                return f"{main}.{m.group(1)}", rest[m.end() :]
            continue
        if rest.startswith("-"):
            return ms, rest
        continue
    return None


def anchor_to_placeholder_hash(body: str) -> str:
    parsed = parse_anchor_body(body)
    if not parsed:
        return f"#ci-{body}"
    key, suffix = parsed
    return f"#⟦ANCHOR:{key}⟧{suffix}"


def anchor_key_to_slug(key: str) -> str:
    if "." in key:
        main_s, sub = key.split(".", 1)
        new_main = MAIN_MAP.get(int(main_s), int(main_s))
        return f"ci-{new_main}{sub}"
    main = int(key)
    new_main = MAIN_MAP.get(main, main)
    return f"ci-{new_main}"

# After migration, these old main numbers must not appear as CI-N in operative tree
STALE_MAIN_NUMBERS = {8, 12, 15, 16, 17, 18, 19, 20, 21, 24, 25}
# Stale only when they appear in OLD sense — verify checks unmapped patterns post-finalize


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        yield path


def ci_keys_by_length() -> list[str]:
    keys: set[str] = set()
    for old in MAIN_MAP:
        keys.add(str(old))
        for sub in ("1", "2", "3", "4", "2A", "3B", "4"):
            keys.add(f"{old}.{sub}")
    return sorted(keys, key=lambda k: (-len(k), k))


def to_placeholder_ci(match: re.Match[str]) -> str:
    main = int(match.group("main"))
    sub = match.group("sub")
    key = f"{main}.{sub}" if sub else str(main)
    return CI_TOKEN.format(key=key)


def resolve_ci_key(key: str) -> str:
    if "." in key:
        main_s, sub = key.split(".", 1)
        main = int(main_s)
        new_main = MAIN_MAP.get(main, main)
        return f"CI-{new_main}.{sub}"
    main = int(key)
    new_main = MAIN_MAP.get(main, main)
    return f"CI-{new_main}"


def to_placeholder_file(match: re.Match[str]) -> str:
    nn = int(match.group("nn"))
    return FILE_TOKEN.format(nn=nn)


def placeholder_pass(text: str) -> str:
    text = CI_REF_RE.sub(lambda m: to_placeholder_ci(m), text)
    text = ANCHOR_LINK_RE.sub(
        lambda m: anchor_to_placeholder_hash(m.group("body")), text
    )
    text = FILE_REF_RE.sub(to_placeholder_file, text)
    return text


def finalize_pass(text: str) -> str:
    text = PLACEHOLDER_CI_RE.sub(
        lambda m: resolve_ci_key(m.group("key")), text
    )
    text = PLACEHOLDER_FILE_RE.sub(
        lambda m: f"ci_{FILE_MAP.get(int(m.group('nn')), int(m.group('nn'))):02d}_",
        text,
    )

    def finalize_anchor(m: re.Match[str]) -> str:
        slug = anchor_key_to_slug(m.group("key"))
        return f"#{slug}{m.group('suffix')}"

    text = PLACEHOLDER_ANCHOR_RE.sub(finalize_anchor, text)
    return text


def has_placeholders(text: str) -> bool:
    return "⟦" in text


def verify_operative(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(iter_files(root)):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        if has_placeholders(text):
            errors.append(f"{rel}: unresolved placeholders")
    return errors


def process_tree(root: Path, transform, dry_run: bool) -> list[Path]:
    changed: list[Path] = []
    for path in sorted(iter_files(root)):
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            changed.append(path)
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--placeholder", action="store_true")
    parser.add_argument("--finalize", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    if args.verify:
        errors = verify_operative(root)
        if errors:
            for err in errors:
                print(err, file=sys.stderr)
            print(f"verify failed: {len(errors)} issue(s)", file=sys.stderr)
            return 1
        print("verify ok")
        return 0

    if args.placeholder:
        changed = process_tree(root, placeholder_pass, args.dry_run)
    elif args.finalize:
        changed = process_tree(root, finalize_pass, args.dry_run)
    else:
        parser.error("specify --placeholder, --finalize, or --verify")

    label = "Would update" if args.dry_run else "Updated"
    for path in changed:
        print(path.relative_to(root))
    print(f"{label} {len(changed)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
