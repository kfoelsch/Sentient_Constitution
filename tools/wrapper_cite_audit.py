#!/usr/bin/env python3
"""Flag citations of an implementation-layer wrapper file such as ``corpus_systems.md``.

Rule ID: REF-WRAPPER-01 (a companion to REF-FAMILY in doc_architecture.md).

``corpus_systems.md`` is a compatibility entrypoint and reader landing page. It
holds no rules. Text that relies on the systems layer must cite the subfile
that owns the rule (``CS-6.305``, ``CS-9.305``, ``CS-6.335`` ...) and link that
subfile, not the wrapper. This audit finds every place the wrapper is cited as
a source: a Markdown link whose target is the wrapper, or the file name written
in prose or in backticks.

Default wrappers: all four (``corpus_systems.md``, ``corpus_institutions.md``,
``corpus_joint_structure.md``, ``corpus_forum.md``). ``--wrapper NAME``
(repeatable) narrows the check to the named wrapper(s); ``--all-wrappers`` is
kept as an explicit spelling of the default.

Out of scope (navigation, not citation):

* the wrapper files themselves, the registry and reading-rules annexes, and
  ``cjs_reader_guide.md``;
* headings, tables, HTML-only lines, blockquotes (the file-top placement
  note), fenced code, ``**Previous file:**`` / ``**Next file:**`` lines, and
  lines that point at a "landing page"; and list items that label a whole
  layer (``- [**CS**](../corpus_systems.md) — ...``);
* in ``core_00.000_preamble.md`` and ``core_19.000_incorporation.md`` (which
  incorporate the layers), a list entry that opens with the wrapper link.

Exit status is 2 when anything is found. ``--summary`` prints counts only.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "REF-WRAPPER-01"

ALL_WRAPPERS = (
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_joint_structure.md",
    "corpus_forum.md",
)
DEFAULT_WRAPPERS = ALL_WRAPPERS

# Files that incorporate the layers: a list entry opening with the wrapper link
# is an inventory entry, not a citation.
INVENTORY_FILES = frozenset(
    {"core_00.000_preamble.md", "core_19.000_incorporation.md"}
)
# Navigation documents that exist to point at the layers.
NAVIGATION_FILE_RE = re.compile(
    r"(?:_registry_and_reading_rules\.md|cjs_reader_guide\.md|"
    r"cjs_00\.110_scope_purpose_boundary_interface\.md)$"
)

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]*)\)")
FENCE_RE = re.compile(r"^\s*```")
NAV_LINE_RE = re.compile(
    r"\*\*(?:Previous|Next) file:\*\*|landing page|Reader landing", re.I
)
LIST_ENTRY_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
# A list item that labels a whole layer, e.g. "- [**CS**](../corpus_systems.md) — ...",
# names the layer; it does not cite the wrapper for a rule.
LAYER_LABEL_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\[\*\*(?:CS|CI|CF|CJS)\*\*\]\(")
CITE_TOKEN_RE = re.compile(r"\b(?:CS|CI|CF|CJS)-\d+(?:\.\d+)*")


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    wrapper: str
    kind: str  # "link" or "text"
    hint: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--wrapper",
        action="append",
        dest="wrappers",
        help="Wrapper file name to check (repeatable). Default: all four layer wrappers.",
    )
    parser.add_argument(
        "--all-wrappers",
        action="store_true",
        help="Check all four layer wrappers (the default).",
    )
    parser.add_argument(
        "--paths",
        nargs="*",
        help="Specific repository-relative Markdown paths to scan.",
    )
    parser.add_argument(
        "--summary", action="store_true", help="Print per-file counts only."
    )
    return parser.parse_args()


def is_wrapper_target(target: str, wrapper: str) -> bool:
    path = target.split("#", 1)[0]
    while path.startswith("./") or path.startswith("../"):
        path = path[path.index("/") + 1 :]
    return path == wrapper


def text_re(wrapper: str) -> re.Pattern[str]:
    return re.compile(r"(?<![\w-])(?:\.\./)*" + re.escape(wrapper) + r"(?!\w)")


def is_exempt_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped[0] in "#|<>":
        return True
    if LAYER_LABEL_RE.match(line):
        return True
    return bool(NAV_LINE_RE.search(line))


def hint_for(line: str, family_map: dict | None, resolve) -> str:
    tokens = CITE_TOKEN_RE.findall(line)
    for token in dict.fromkeys(tokens):
        if family_map is not None:
            try:
                target = resolve(family_map, token)
            except Exception:  # noqa: BLE001 - hint only
                target = None
            if target:
                return f"link {token} at {target}"
    return "cite the subfile that owns the rule, by id and title"


def scan_line(
    rel_path: str,
    line_number: int,
    line: str,
    wrappers: tuple[str, ...] = DEFAULT_WRAPPERS,
    family_map: dict | None = None,
    resolve=None,
) -> list[Finding]:
    if is_exempt_line(line):
        return []
    findings: list[Finding] = []
    hint = hint_for(line, family_map, resolve) if resolve else (
        "cite the subfile that owns the rule, by id and title"
    )
    for wrapper in wrappers:
        found: list[Finding] = []
        remaining = line
        first_link_at_entry_start = False
        for match in LINK_RE.finditer(line):
            if is_wrapper_target(match.group(2), wrapper):
                found.append(Finding(rel_path, line_number, wrapper, "link", hint))
                entry = LIST_ENTRY_RE.match(line)
                before = line[: match.start()]
                if entry and re.fullmatch(
                    r"\s*(?:[-*+]|\d+\.)\s+\**", before
                ):
                    first_link_at_entry_start = True
        remaining = LINK_RE.sub(
            lambda m: "" if is_wrapper_target(m.group(2), wrapper) else m.group(0),
            line,
        )
        for _ in text_re(wrapper).finditer(remaining):
            found.append(Finding(rel_path, line_number, wrapper, "text", hint))
        if not found:
            continue
        if rel_path in INVENTORY_FILES and first_link_at_entry_start:
            continue
        findings.extend(found)
    return findings


def masked_fences(text: str) -> list[str]:
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
        elif in_fence:
            out.append("")
        else:
            out.append(line)
    return out


def scan_text(rel_path: str, text: str, wrappers=DEFAULT_WRAPPERS, **kw) -> list[Finding]:
    findings: list[Finding] = []
    for idx, line in enumerate(masked_fences(text), start=1):
        findings.extend(scan_line(rel_path, idx, line, wrappers, **kw))
    return findings


def scope_files(root: Path, wrappers: tuple[str, ...]) -> list[str]:
    skip = set(ALL_WRAPPERS)
    return [
        rel
        for rel in binding_corpus_scope(root)
        if rel not in skip and not NAVIGATION_FILE_RE.search(rel)
    ]


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    wrappers = ALL_WRAPPERS if args.all_wrappers else tuple(
        args.wrappers or DEFAULT_WRAPPERS
    )
    unknown = [w for w in wrappers if w not in ALL_WRAPPERS]
    if unknown:
        print(f"{RULE}: unknown wrapper(s): {', '.join(unknown)}", file=sys.stderr)
        return 1
    try:
        from family_map_lib import load_family_map, resolve_section_file

        family_map = load_family_map(root)
        resolve = resolve_section_file
    except Exception:  # noqa: BLE001 - hints are optional
        family_map, resolve = None, None
    rels = args.paths if args.paths else scope_files(root, wrappers)
    findings: list[Finding] = []
    for rel in rels:
        if Path(rel).name in ALL_WRAPPERS or NAVIGATION_FILE_RE.search(rel):
            continue
        path = root / rel
        if not path.is_file():
            continue
        findings.extend(
            scan_text(
                rel,
                path.read_text(encoding="utf-8"),
                wrappers,
                family_map=family_map,
                resolve=resolve,
            )
        )
    if not findings:
        print(f"{RULE}: no citations of {', '.join(wrappers)}.")
        return 0
    per_file = Counter(f.file for f in findings)
    if not args.summary:
        for f in findings:
            print(
                f"{f.file}:{f.line}: {RULE}: {f.wrapper} cited ({f.kind}); {f.hint}"
            )
    print(
        f"{RULE}: {len(findings)} citation(s) of {', '.join(wrappers)} in "
        f"{len(per_file)} file(s). Cite the subfile, not the wrapper "
        "(REF-FAMILY in doc_architecture.md)."
    )
    for rel, count in per_file.most_common():
        print(f"  {count:4d}  {rel}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
