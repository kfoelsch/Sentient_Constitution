#!/usr/bin/env python3
"""Heading-anchor fragments for generated links (HTML-ANCHOR-LINK-01).

The corpus keys sections by a stable custom ``<a id>``. The editor preview only
follows heading anchors, so generated pages link with the heading slug whenever
the ``<a id>`` sits directly above a heading whose slug is unique in its file.
Anything else keeps the stable id. See ``local_markdown_fragment_audit.py``.
"""

from __future__ import annotations

from pathlib import Path

from local_markdown_fragment_audit import anchor_info

REPO_ROOT = Path(__file__).resolve().parent.parent
_cache: dict[Path, dict[str, str]] = {}


def link_fragment(rel_file: str, anchor: str, root: Path | None = None) -> str:
    """Return the fragment to link for ``anchor`` in repository file ``rel_file``."""
    if not anchor:
        return anchor
    path = (root or REPO_ROOT) / rel_file
    if path not in _cache:
        _cache[path] = (
            anchor_info(path.read_text(encoding="utf-8"))[2] if path.is_file() else {}
        )
    return _cache[path].get(anchor, anchor)


_rev_cache: dict[Path, dict[str, list[str]]] = {}


def ids_for_fragment(path: Path, fragment: str) -> list[str]:
    """Custom ``<a id>`` anchors that sit above the heading whose slug is ``fragment``.

    Audits keyed to stable ids use this to accept a heading-slug link as the same
    target as the id it replaced.
    """
    if not fragment or not path.is_file():
        return []
    if path not in _rev_cache:
        reverse: dict[str, list[str]] = {}
        for ident, slug in anchor_info(path.read_text(encoding="utf-8"))[2].items():
            reverse.setdefault(slug, []).append(ident)
        _rev_cache[path] = reverse
    return _rev_cache[path].get(fragment, [])


def normalize_href(root: Path, source_rel: str, href: str) -> str:
    """Return ``href`` with its fragment mapped to the heading slug when it is an id."""
    target, hash_sep, fragment = href.partition("#")
    if not hash_sep or not fragment:
        return href
    rel = source_rel if not target else (Path(source_rel).parent / target).as_posix()
    return f"{target}#{link_fragment(rel, fragment, root)}"
