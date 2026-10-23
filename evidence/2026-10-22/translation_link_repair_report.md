# Translation link repair report (2026-10-22)

Written by `tools/translation_link_repair.py --write` over all 19 locales. Only link targets were changed, plus `<a id>` anchor lines added above aligned translated headings so that English fragment ids resolve. No translated text was changed.

- **DROPPED** (4517): the English heading the link pointed to no longer exists (or was renumbered with no matching title), so the link now goes to the file without a fragment. A reader of the section can retarget these.
- **ENGLISH** (5188): the target is translated, but no heading in the translation could be aligned to the English anchor, so the link goes to the English file.
- **UNMAPPED** (0): no current English file found.

## Lines by locale

The per-line detail is split by locale to keep each file under the size limit.

| Locale | DROPPED | ENGLISH | Detail |
|---|---|---|---|
| ar | 240 | 149 | [`ar.md`](translation_link_repair/ar.md) |
| bn | 242 | 366 | [`bn.md`](translation_link_repair/bn.md) |
| es | 326 | 364 | [`es.md`](translation_link_repair/es.md) |
| fa | 214 | 447 | [`fa.md`](translation_link_repair/fa.md) |
| fr | 212 | 227 | [`fr.md`](translation_link_repair/fr.md) |
| hi | 207 | 266 | [`hi.md`](translation_link_repair/hi.md) |
| id | 204 | 168 | [`id.md`](translation_link_repair/id.md) |
| ja | 242 | 182 | [`ja.md`](translation_link_repair/ja.md) |
| ko | 242 | 261 | [`ko.md`](translation_link_repair/ko.md) |
| mr | 117 | 95 | [`mr.md`](translation_link_repair/mr.md) |
| pt | 245 | 1043 | [`pt.md`](translation_link_repair/pt.md) |
| ru | 276 | 221 | [`ru.md`](translation_link_repair/ru.md) |
| ta | 265 | 220 | [`ta.md`](translation_link_repair/ta.md) |
| te | 227 | 204 | [`te.md`](translation_link_repair/te.md) |
| th | 248 | 215 | [`th.md`](translation_link_repair/th.md) |
| tr | 265 | 224 | [`tr.md`](translation_link_repair/tr.md) |
| ur | 265 | 213 | [`ur.md`](translation_link_repair/ur.md) |
| vi | 257 | 266 | [`vi.md`](translation_link_repair/vi.md) |
| zh | 223 | 57 | [`zh.md`](translation_link_repair/zh.md) |
