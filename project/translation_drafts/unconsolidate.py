#!/usr/bin/env python3
"""Restore the one-passage chunk files from the consolidated files in this folder.

Usage: python3 -I unconsolidate.py <consolidated.md> [outdir]
Each chunk is stored as:  <!-- CHUNK-BEGIN name bytes=N -->\n<N raw bytes>\n<!-- CHUNK-END -->\n
Default outdir is the consolidated file's folder. The git history before the
consolidation commit also still holds every original chunk file.
"""
import os, sys
B = b"<!-- CHUNK-BEGIN "
src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(src))
blob = open(src, "rb").read(); pos = 0; n = 0
while pos < len(blob):
    assert blob.startswith(B, pos), "unexpected content at byte %d" % pos
    e = blob.index(b" -->\n", pos)
    name, nb = blob[pos + len(B):e].decode().rsplit(" bytes=", 1); nb = int(nb)
    s = e + 5
    open(os.path.join(out, name), "wb").write(blob[s:s + nb])
    pos = s + nb + len(b"\n<!-- CHUNK-END -->\n"); n += 1
print("restored", n, "chunk files to", out)
