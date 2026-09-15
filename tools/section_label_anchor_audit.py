#!/usr/bin/env python3
"""Map prose section labels to resolved anchors and flag numbering divergences.

When a Markdown link's text contains a section label (``§5.4``,
``Chapter Nine §5.4 Duty to resist``), or is only a dotted number
(``4.1``), the resolved heading's current number must be that label or a
dotted parent/child of it. The fragment must exist. When the numbers are
related, the heading must carry a current-numbering id whose prefix
matches that heading's current number (dots stripped, e.g. ``54-...``,
or dots as hyphens, e.g. ``4-3-...``).

Numbered ATX headings in ``core_*.md`` files must not duplicate a sibling
number and must use consecutive last components under the same parent
prefix (so ``#### 3.16`` twice under ``### 3.`` fails; a file may start
at §6 or §11). Cite-match skips ``implementation/`` and ``evaluation/``
sources (historical cut lists and kits keep fossil § labels by design).

This corpus is pre-release: one current fragment id per heading. Do not
keep fossil or legacy redirect ids. Citations must use the current id
(``make fossil-anchor-audit``).

Rule IDs: SECTION-LABEL-ANCHOR-01, SECTION-CITE-MATCH-01,
NAV-HEADING-SEQUENCE-01
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope
from local_markdown_fragment_audit import anchors_in, github_slug, links_in, resolve_link

ROOT = Path(__file__).resolve().parents[1]
RULE = "SECTION-LABEL-ANCHOR-01"
RULE_CITE = "SECTION-CITE-MATCH-01"
RULE_SEQ = "NAV-HEADING-SEQUENCE-01"

ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
ATX_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?(?:\s+|$)")
BOLD_NUM_RE = re.compile(r"^\*\*(\d+(?:\.\d+)*)\.?\s+")
ID_NUM_RE = re.compile(r"^(\d+(?:-\d+)*)-")
SECTION_IN_TEXT_RE = re.compile(
    r"(?:Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|"
    r"Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|\d+)\s+)?"
    r"§+\s*(\d+(?:\.\d+)*)",
    re.I,
)
DOTTED_ONLY_RE = re.compile(r"^(\d+(?:\.\d+)*)$")
SKIP_CONSUMERS = (
    "<details",
    "<summary",
    "<!--",
    "<div",
    "<span",
    "<br",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def compact(num: str) -> str:
    return num.replace(".", "").replace("-", "")


def hyphenated(dotted: str) -> str:
    return dotted.replace(".", "-")


def id_matches_current(anchor_id: str, current_dotted: str) -> bool:
    match = ID_NUM_RE.match(anchor_id)
    if not match:
        return False
    prefix = match.group(1)
    return prefix == compact(current_dotted) or prefix == hyphenated(
        current_dotted
    )


def dotted_related(prose: str, current: str) -> bool:
    return (
        prose == current
        or current.startswith(prose + ".")
        or prose.startswith(current + ".")
    )


def parent_prefix(dotted: str) -> str:
    if "." not in dotted:
        return ""
    return dotted.rsplit(".", 1)[0]


def last_component(dotted: str) -> int:
    return int(dotted.rsplit(".", 1)[-1])


def source_paths(root: Path) -> list[Path]:
    names = list(binding_corpus_scope(root, include_support_docs=True))
    for pattern in ("implementation/**/*.md", "evaluation/**/*.md"):
        names.extend(
            path.relative_to(root).as_posix()
            for path in sorted(root.glob(pattern))
            if path.is_file()
        )
    out: list[Path] = []
    seen: set[str] = set()
    for name in names:
        if name.startswith(("archive/", "ai_corpus/", "evidence/")):
            continue
        if name in seen:
            continue
        seen.add(name)
        path = root / name
        if path.is_file():
            out.append(path)
    return out


def _plain_title(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"^\*\*|\*\*$", "", text).strip()


def parse_heading_index(text: str) -> tuple[dict[str, dict], list[tuple[int, str, int]]]:
    """Map fragment ids (explicit + GitHub slugs) to heading info.

    Also return numbered ATX headings as ``(level, dotted, lineno)``.
    """
    lines = text.splitlines()
    numbered_stack: list[tuple[int, str]] = []
    pending: list[str] = []
    index: dict[str, dict] = {}
    numbered_headings: list[tuple[int, str, int]] = []
    used_slugs: set[str] = set()
    next_suffix: dict[str, int] = {}

    def slug_for(title_plain: str) -> str:
        base = github_slug(title_plain)
        slug = base
        suffix = next_suffix.get(base, 1)
        while slug in used_slugs:
            slug = f"{base}-{suffix}"
            suffix += 1
        used_slugs.add(slug)
        next_suffix[base] = suffix
        return slug

    def register(info: dict, extra_ids: list[str]) -> None:
        ids = list(dict.fromkeys([*info["ids"], *extra_ids]))
        stored = {**info, "ids": ids}
        for anchor_id in ids:
            index[anchor_id] = stored

    def consume(title_plain: str, atx_level: int | None, lineno: int) -> None:
        nonlocal pending
        if not pending and atx_level is None:
            return
        slug = slug_for(title_plain) if atx_level is not None else None
        extra = [slug] if slug else []
        if atx_level is not None:
            while numbered_stack and numbered_stack[-1][0] >= atx_level:
                numbered_stack.pop()
            numbered = NUM_RE.match(title_plain)
            current = (
                numbered.group(1)
                if numbered
                else (numbered_stack[-1][1] if numbered_stack else None)
            )
            if numbered:
                numbered_stack.append((atx_level, numbered.group(1)))
                numbered_headings.append((atx_level, numbered.group(1), lineno))
        else:
            bold = BOLD_NUM_RE.match("**" + title_plain)
            if title_plain and not title_plain.startswith("**"):
                bold = BOLD_NUM_RE.match(f"**{title_plain}")
            current = (
                bold.group(1)
                if bold
                else (numbered_stack[-1][1] if numbered_stack else None)
            )
        info = {
            "ids": list(pending),
            "lineno": lineno,
            "title": title_plain[:90],
            "current": current,
        }
        register(info, extra)
        pending = []

    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        anchor = ANCHOR_RE.match(stripped)
        if anchor:
            pending.append(anchor.group(1))
            continue
        atx = ATX_RE.match(stripped)
        if atx and not pending:
            consume(_plain_title(atx.group(2)), len(atx.group(1)), lineno)
            continue
        if not pending:
            continue
        if not stripped or stripped.lower().startswith(SKIP_CONSUMERS):
            continue
        if atx:
            consume(_plain_title(atx.group(2)), len(atx.group(1)), lineno)
            continue
        bold = BOLD_NUM_RE.match(stripped)
        if bold or stripped.startswith("**"):
            consume(_plain_title(stripped), None, lineno)
            continue
        consume(_plain_title(stripped), None, lineno)
    return index, numbered_headings


def parse_clusters(text: str) -> dict[str, dict]:
    """Map each explicit id / GitHub slug to its heading cluster."""
    index, _ = parse_heading_index(text)
    return index


def heading_sequence_errors(
    rel: str, entries: list[tuple[int, str, int]]
) -> list[str]:
    groups: dict[tuple[str, int], list[tuple[str, int]]] = defaultdict(list)
    for level, dotted, lineno in entries:
        groups[(parent_prefix(dotted), level)].append((dotted, lineno))
    errors: list[str] = []
    for (parent, level), items in sorted(groups.items()):
        seen: dict[str, int] = {}
        for dotted, lineno in items:
            if dotted in seen:
                errors.append(
                    f"{rel}:{lineno}: duplicate heading §{dotted} "
                    f"(also {rel}:{seen[dotted]}) ({RULE_SEQ})"
                )
            else:
                seen[dotted] = lineno
        uniq = sorted({last_component(dotted) for dotted, _ in items})
        if uniq and uniq != list(range(uniq[0], uniq[0] + len(uniq))):
            display = ", ".join(dotted for dotted, _ in items)
            parent_label = f"§{parent}" if parent else "root"
            errors.append(
                f"{rel}:{items[0][1]}: non-consecutive sibling headings "
                f"under {parent_label} at heading level {level}: {display} "
                f"({RULE_SEQ})"
            )
    return errors


def cluster_cache_for(
    path: Path, cache: dict[Path, tuple[dict[str, dict], list[tuple[int, str, int]]]]
) -> tuple[dict[str, dict], list[tuple[int, str, int]]]:
    if path not in cache:
        cache[path] = parse_heading_index(path.read_text(encoding="utf-8"))
    return cache[path]


def prose_from_label(label: str) -> str | None:
    match = SECTION_IN_TEXT_RE.search(label)
    if match:
        return match.group(1)
    dotted = DOTTED_ONLY_RE.match(label.strip())
    if dotted:
        return dotted.group(1)
    return None


def link_labels(text: str, line_no: int, fragment: str) -> list[str]:
    lines = text.splitlines()
    line = lines[line_no - 1] if 1 <= line_no <= len(lines) else ""
    labels = [
        match.group(1)
        for match in re.finditer(r"\[([^\]]+)\]\([^)]+\)", line)
        if fragment in match.group(0)
    ]
    if labels:
        return labels
    window = "\n".join(
        lines[max(0, line_no - 3) : min(len(lines), line_no + 2)]
    )
    return [
        match.group(1)
        for match in re.finditer(r"\[([^\]]+)\]\([^)]+\)", window)
        if fragment in match.group(0)
    ]


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    cache: dict[Path, tuple[dict[str, dict], list[tuple[int, str, int]]]] = {}
    anchor_cache: dict[Path, set[str]] = {}
    root_resolved = root.resolve()
    sequenced: set[Path] = set()
    for source in source_paths(root):
        text = source.read_text(encoding="utf-8")
        rel = source.relative_to(root).as_posix()
        if source.name.startswith("core_") and source.suffix == ".md":
            if source not in sequenced:
                _, numbered = cluster_cache_for(source, cache)
                errors.extend(heading_sequence_errors(rel, numbered))
                sequenced.add(source)
        for link in links_in(source, text):
            resolved = resolve_link(root_resolved, link)
            if resolved is None:
                continue
            target_path, fragment = resolved
            if fragment is None:
                continue
            try:
                target_rel = target_path.relative_to(root_resolved).as_posix()
            except ValueError:
                continue
            if not target_path.is_file():
                continue
            labels = link_labels(text, link.line, fragment)
            if not labels:
                continue
            prose = prose_from_label(labels[0])
            if not prose:
                continue
            # Support/history files keep fossil § labels by design.
            if rel.startswith(("implementation/", "evaluation/")):
                continue
            if target_path not in anchor_cache:
                anchor_cache[target_path] = anchors_in(
                    target_path.read_text(encoding="utf-8")
                )
            if fragment not in anchor_cache[target_path]:
                errors.append(
                    f"{rel}:{link.line}: prose §{prose} resolves to "
                    f"{target_rel}#{fragment} but that fragment is absent "
                    f"({RULE_CITE})"
                )
                continue
            # Named fragments (the-model, interim-protection) are not
            # section-number ids; do not compare them to § labels.
            if not ID_NUM_RE.match(fragment):
                continue
            info_map, _ = cluster_cache_for(target_path, cache)
            info = info_map.get(fragment)
            if not info or not info.get("current"):
                continue
            current = info["current"]
            if not dotted_related(prose, current):
                errors.append(
                    f"{rel}:{link.line}: prose §{prose} resolves to "
                    f"{target_rel}#{fragment} (heading §{current} "
                    f"{info['title']!r}) ({RULE_CITE})"
                )
                continue
            aliases = info.get("ids") or [fragment]
            if id_matches_current(fragment, current):
                continue
            if any(id_matches_current(anchor_id, current) for anchor_id in aliases):
                continue
            errors.append(
                f"{rel}:{link.line}: prose §{prose} resolves to {target_rel}#"
                f"{fragment} (heading §{current} {info['title']!r}) with no "
                f"current-numbering alias (expected prefix {compact(current)}- "
                f"or {hyphenated(current)}-) ({RULE})"
            )
    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = audit(root)
    if errors:
        print(f"FAIL: {len(errors)} section-label/anchor divergence(s)")
        for err in errors:
            print(err)
        return 1
    print(
        "PASS: section labels match target headings, fragments exist, "
        "and core_* numbered sibling headings are consecutive."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
