#!/usr/bin/env python3
"""Audit link destinations for off-corpus and machine-local targets.

Rule: LINK-OFF-CORPUS-15 in tools/architecture/rule_registry.json.

Two scopes, two standards:

* **Binding corpus** (``core_*`` files and adopted implementation text) — every
  link target stays inside the repository. Only relative paths and in-file
  ``#fragment`` targets are allowed. An absolute URL, a root-absolute path, or
  any other URI scheme fails: the instrument must read the same from a clone, a
  print pack, or the Pages render, and a reader must never be sent off the
  corpus to learn what a provision says.
* **Maintained support documents** (README, START_HERE, ``docs/``,
  ``implementation/``, and the rest) — external ``http(s)`` and ``mailto``
  targets are legitimate citations and pass. Machine-local targets never do:
  ``file://`` URLs, VS Code webview URLs (``vscode-resource``, ``vscode-cdn``,
  ``vscode-webview``), home-directory or drive-letter paths, ``~/`` paths, and
  ``localhost`` URLs resolve for one machine only. They almost always arrive by
  copying a rendered preview URL out of an editor.

Dated records (``evidence/``, ``evaluation/``, ``MEMLOG.md``, ``TODO.md``),
generated trees, ``archive/``, and ``translations/`` stay out of the blocking
scope: they record what was true when written. ``--report`` inventories those
and every allowed external citation without failing.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope

ROOT = _TOOLS.parent
RULE = "LINK-OFF-CORPUS-15"

# Trees and working logs that keep historical or generated hrefs by design.
EXCLUDED_PREFIXES = (
    ".git/",
    ".github/",
    "_pages_site/",
    "archive/",
    "translations/",
    "evidence/",
    "evaluation/",
    "node_modules/",
    "ai_corpus/",
    "doc_architecture/generated/",
    "nimbalyst-local/",
)
EXCLUDED_FILES = ("MEMLOG.md", "TODO.md")

INLINE_LINK_RE = re.compile(
    r"!?\[[^\]\n]*\]\(\s*(?P<target><[^>\n]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
REFERENCE_LINK_RE = re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(?P<target><[^>\n]+>|\S+)")
HTML_TARGET_RE = re.compile(r"<[^>\n]*?\b(?:href|src)\s*=\s*\"(?P<target>[^\"]+)\"")
CODE_SPAN_RE = re.compile(r"`+[^`\n]*`+")
FENCE_RE = re.compile(r"^\s*(```|~~~)")

SCHEME_RE = re.compile(r"^(?P<scheme>[A-Za-z][A-Za-z0-9+.\-]*):")
WINDOWS_PATH_RE = re.compile(r"^[A-Za-z]:[\\/]")
HOME_PATH_RE = re.compile(r"^(?:~|/Users/|/home/|/Volumes/|/private/|/var/folders/|/tmp/)")
LOCAL_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "[::1]", "::1")
LOCAL_HOST_MARKERS = ("vscode-resource", "vscode-cdn", "vscode-webview", "file+")
# Editor workspace markers only matter on an absolute target: the repository has
# its own .cursor/ directory, and a relative link into it is an ordinary in-repo link.
EDITOR_PATH_MARKERS = ("/.cursor/", "/.vscode/", "/Library/Application Support/")


@dataclass(frozen=True)
class Link:
    rel: str
    line: int
    target: str


def is_excluded(rel: str) -> bool:
    return rel.startswith(EXCLUDED_PREFIXES) or rel in EXCLUDED_FILES


def strip_code(text: str) -> list[str]:
    """Blank out fenced blocks and mask inline code spans, keeping line numbers."""
    out: list[str] = []
    in_fence = False
    fence_token = ""
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            token = match.group(1)
            if not in_fence:
                in_fence, fence_token = True, token
                out.append("")
                continue
            if token == fence_token:
                in_fence = False
                out.append("")
                continue
        out.append("" if in_fence else CODE_SPAN_RE.sub(" ", line))
    return out


def extract_links(rel: str, text: str) -> list[Link]:
    links: list[Link] = []
    for number, line in enumerate(strip_code(text), 1):
        for pattern in (INLINE_LINK_RE, REFERENCE_LINK_RE, HTML_TARGET_RE):
            for match in pattern.finditer(line):
                target = match.group("target").strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1].strip()
                if target:
                    links.append(Link(rel, number, target))
    return links


def machine_local_reason(target: str) -> str | None:
    """Why this target resolves on one machine only, or None."""
    lowered = target.lower()
    scheme = SCHEME_RE.match(target)
    if scheme and scheme.group("scheme").lower() == "file":
        return "file:// URL"
    if any(marker in lowered for marker in LOCAL_HOST_MARKERS):
        return "editor preview URL (VS Code webview resource)"
    if scheme and scheme.group("scheme").lower() in {"http", "https"}:
        host = urlsplit(target).hostname or ""
        if host.lower() in LOCAL_HOSTS:
            return "localhost URL"
    if WINDOWS_PATH_RE.match(target):
        return "drive-letter path"
    if HOME_PATH_RE.match(target):
        return "machine-local filesystem path"
    absolute = bool(scheme) or target.startswith(("/", "~")) or WINDOWS_PATH_RE.match(target)
    if absolute and any(marker in target for marker in EDITOR_PATH_MARKERS):
        return "editor-local workspace path"
    return None


def off_corpus_reason(target: str) -> str | None:
    """Why this target leaves the corpus, or None. Binding-scope standard."""
    if target.startswith("#"):
        return None
    scheme = SCHEME_RE.match(target)
    if scheme:
        return f"{scheme.group('scheme').lower()}: URL"
    if target.startswith("//"):
        return "protocol-relative URL"
    if target.startswith("/"):
        return "root-absolute path"
    return None


def audit_link(link: Link, binding: bool) -> str | None:
    local = machine_local_reason(link.target)
    if local is not None:
        return (
            f"{link.rel}:{link.line}: {local} — link targets must resolve for every "
            f"reader, not one machine: {link.target[:100]}"
        )
    if not binding:
        return None
    off = off_corpus_reason(link.target)
    if off is not None:
        return (
            f"{link.rel}:{link.line}: {off} in binding corpus text — cite corpus "
            f"files by relative path or #fragment: {link.target[:100]}"
        )
    return None


def maintained_markdown(root: Path) -> list[str]:
    files: list[str] = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if is_excluded(rel) or not path.is_file():
            continue
        files.append(rel)
    return files


def audit(root: Path) -> tuple[list[str], list[Link]]:
    """Return (blocking findings, allowed external citations)."""
    binding = set(binding_corpus_scope(root))
    findings: list[str] = []
    external: list[Link] = []
    for rel in maintained_markdown(root):
        path = root / rel
        text = path.read_text(encoding="utf-8", errors="replace")
        for link in extract_links(rel, text):
            finding = audit_link(link, binding=rel in binding)
            if finding is not None:
                findings.append(finding)
            elif rel not in binding and off_corpus_reason(link.target) is not None:
                external.append(link)
    return findings, external


def report(root: Path) -> None:
    findings, external = audit(root)
    print(f"{RULE} report — root {root}")
    print(f"\nBlocking findings: {len(findings)}")
    for item in findings:
        print(f"  - {item}")
    print(f"\nAllowed external citations in support documents: {len(external)}")
    by_file: dict[str, int] = {}
    for link in external:
        by_file[link.rel] = by_file.get(link.rel, 0) + 1
    for rel, count in sorted(by_file.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {count:4d}  {rel}")
    skipped: list[str] = []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if not is_excluded(rel) or rel.startswith((".git/", "_pages_site/", "node_modules/")):
            continue
        for link in extract_links(rel, path.read_text(encoding="utf-8", errors="replace")):
            if machine_local_reason(link.target):
                skipped.append(f"  - {rel}:{link.line}: {link.target[:100]}")
    print(f"\nMachine-local targets in dated or generated records (not blocking): {len(skipped)}")
    for item in skipped:
        print(item)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--report",
        action="store_true",
        help="inventory external and machine-local targets without failing",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    if args.report:
        report(root)
        return 0

    findings, external = audit(root)
    if findings:
        print("External link audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(findings)}", file=sys.stderr)
        return 1

    print(
        f"External link audit OK ({RULE}): binding corpus links stay in-repository; "
        f"{len(external)} external citation(s) in support documents; "
        f"no machine-local targets."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
