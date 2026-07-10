#!/usr/bin/env python3
"""One-off migration: rename the definition Assessment component from E -> A.

Renames the O/M/E/C model to O/M/A/C across the live corpus:
  - Chapter Five `{term}-e` component anchors  -> `{term}-a`
  - every inbound link fragment that targets a renamed `{term}-e` anchor
  - the D/A/C widget visible label `[E](...)` -> `[A](...)` on retargeted links
  - prose tokens: O/E/C, O/M/E/C -> O/M/A/C; "Evaluative" -> "Assessment"; M/E -> M/A

Anchor DEFINITIONS live only in core_05*.md. A blind `-e)` replace is unsafe
(it would hit unrelated anchors), so link retargeting is keyed to the exact set
of renamed slugs discovered from the anchor definitions.

Dry-run by default; pass --apply to write.

doc_architecture.md and README.md are intentionally excluded (hand-edited).
"""
import difflib
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INCLUDE_GLOBS = [
    "core_*.md",
    "corpus_*.md",
    "corpus_joint_structure/**/*.md",
    "corpus_systems/**/*.md",
    "corpus_forum/**/*.md",
    "corpus_institutions/**/*.md",
    "ai_corpus/**/*.md",
    "implementation/**/*.md",
    "plans/**/*.md",
]

EXCLUDE_SUBSTR = [
    "/archive/",
    "/evidence/",
    "/doc_architecture/generated/",
    "/tools/",
]
EXCLUDE_BASENAMES = {"doc_architecture.md", "README.md"}

# Ordered literal prose replacements (most specific first).
PROSE_LITERALS = [
    ("Ontological (O), Evaluative (E), and Compliance (C)",
     "Ontological (O), Assessment (A), and Compliance (C)"),
    ("Ontological (O), Evaluative (E), or Compliance (C)",
     "Ontological (O), Assessment (A), or Compliance (C)"),
    ("Measurement and Evaluative (M/E)", "Measurement and Assessment (M/A)"),
    ("Evaluative Components (E)", "Assessment Components (A)"),
    ("Evaluative components", "Assessment components"),
    ("Evaluative component", "Assessment component"),
    ("Evaluative (E)", "Assessment (A)"),
    ("Evaluative part", "Assessment part"),
    ("O/M/E/C", "O/M/A/C"),
    ("O/E/C", "O/M/A/C"),
    ("semantic, evaluative, and compliance", "semantic, assessment, and compliance"),
    ("evaluative rigor", "assessment rigor"),
    # local stable anchor introduced during Ch2 restructure
    ("22-evaluative-components", "12-assessment-components"),
]


def discover_files():
    seen = set()
    out = []
    for g in INCLUDE_GLOBS:
        for p in glob.glob(os.path.join(ROOT, g), recursive=True):
            rp = os.path.abspath(p)
            norm = rp.replace(os.sep, "/")
            if any(s in norm for s in EXCLUDE_SUBSTR):
                continue
            if os.path.basename(rp) in EXCLUDE_BASENAMES:
                continue
            if rp in seen:
                continue
            seen.add(rp)
            out.append(rp)
    return sorted(out)


def discover_anchor_slugs():
    """Return set of slugs (without trailing -e) for component anchors in core_05*."""
    slugs = set()
    pat = re.compile(r'id="([a-z0-9-]+)-e"')
    for p in glob.glob(os.path.join(ROOT, "core_05*.md")):
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        for m in pat.finditer(text):
            slugs.add(m.group(1))
    return slugs


def build_regexes(slugs):
    # old -> new fragment maps
    old_to_new = {f"{s}-e": f"{s}-a" for s in slugs}
    # link fragment retarget: #{slug-e} followed by a boundary char
    frag_alt = "|".join(re.escape(k) for k in sorted(old_to_new, key=len, reverse=True))
    frag_re = re.compile(r'#(' + frag_alt + r')(?=[)\s"\'#])')
    # widget label swap: [E](...#{slug-a})
    new_alt = "|".join(re.escape(v) for v in sorted(old_to_new.values(), key=len, reverse=True))
    label_re = re.compile(r'\[E\]\((?P<h>[^)]*#(?:' + new_alt + r'))\)')
    # anchor definition rename
    def_re = re.compile(r'id="(' + frag_alt + r')"')
    return old_to_new, frag_re, label_re, def_re


def prose_catchall(text):
    n = 0
    # capital standalone "Evaluative" not part of an anchor/url token
    text, c = re.subn(r'(?<![-#/"\w])Evaluative(?![-"\w])', "Assessment", text)
    n += c
    # lowercase standalone "evaluative"
    text, c = re.subn(r'(?<![-#/"\w])evaluative(?![-"\w])', "assessment", text)
    n += c
    return text, n


def migrate_text(path, text, old_to_new, frag_re, label_re, def_re):
    changes = 0
    is_ch5 = os.path.basename(path).startswith("core_05")

    if is_ch5:
        def _defsub(m):
            return 'id="' + old_to_new[m.group(1)] + '"'
        text, c = def_re.subn(_defsub, text)
        changes += c
        # legacy pre-guidepost letter markers (Evaluative component): - E: / - **E:** / - E —
        for pat, repl in (
            (r'^- E:', '- A:'),
            (r'^- \*\*E:\*\*', '- **A:**'),
            (r'^- E —', '- A —'),
            (r'^- \*\*E\*\* —', '- **A** —'),
        ):
            text, c = re.subn(pat, repl, text, flags=re.MULTILINE)
            changes += c

    def _fragsub(m):
        return "#" + old_to_new[m.group(1)]
    text, c = frag_re.subn(_fragsub, text)
    changes += c

    text, c = label_re.subn(r"[A](\g<h>)", text)
    changes += c

    for old, new in PROSE_LITERALS:
        cnt = text.count(old)
        if cnt:
            text = text.replace(old, new)
            changes += cnt

    text, c = prose_catchall(text)
    changes += c

    return text, changes


WIDGET_E_RE = re.compile(r'· \[E\]\((?P<h>[^)]*)-e\)')


def widget_e_cleanup(apply):
    """Convert any residual D/A/C widget Assessment column `· [E](...-e)` to
    `· [A](...-a)`, including rows whose target anchor never existed (resolved
    via base-slug fallback). Independent of the anchor set."""
    files = discover_files()
    total = 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            orig = fh.read()
        new, c = WIDGET_E_RE.subn(r'· [A](\g<h>-a)', orig)
        # Clustered-head rows point the Assessment column at the base anchor
        # (no -e suffix); swap the label only.
        new, c2 = re.subn(r'· \[E\]\(', '· [A](', new)
        c += c2
        if c:
            total += c
            print(f"  {c:5d}  {os.path.relpath(path, ROOT)}")
            if apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)
    print(f"\nWidget-E cleanup: {total} rows. Mode: {'APPLY' if apply else 'DRY-RUN'}")


def main():
    apply = "--apply" in sys.argv
    if "--widget-e-cleanup" in sys.argv:
        widget_e_cleanup(apply)
        return
    show = [a.split("=", 1)[1] for a in sys.argv if a.startswith("--show=")]
    slugs = discover_anchor_slugs()
    old_to_new, frag_re, label_re, def_re = build_regexes(slugs)
    files = discover_files()

    if show:
        for target in show:
            path = os.path.join(ROOT, target)
            with open(path, encoding="utf-8") as fh:
                orig = fh.read()
            new, _ = migrate_text(path, orig, old_to_new, frag_re, label_re, def_re)
            diff = difflib.unified_diff(
                orig.splitlines(), new.splitlines(),
                fromfile=target + " (old)", tofile=target + " (new)", lineterm="")
            print("\n".join(diff))
        return

    print(f"Discovered {len(slugs)} component anchor slugs in core_05*.")
    print(f"Scanning {len(files)} files. Mode: {'APPLY' if apply else 'DRY-RUN'}\n")

    total = 0
    touched = 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            orig = fh.read()
        new, changes = migrate_text(path, orig, old_to_new, frag_re, label_re, def_re)
        if changes and new != orig:
            touched += 1
            total += changes
            rel = os.path.relpath(path, ROOT)
            print(f"  {changes:5d}  {rel}")
            if apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new)

    print(f"\nTotal edits: {total} across {touched} files.")
    if not apply:
        print("Dry-run only. Re-run with --apply to write.")


if __name__ == "__main__":
    main()
