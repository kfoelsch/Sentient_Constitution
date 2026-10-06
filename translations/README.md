# Read the Sentient Constitution in your language

These are **early draft translations**. They are shared so more readers can reach the Constitution, but they are not official versions:

- They do not cover every chapter yet. Each language page lists what is available.
- Where a translation and the English text differ, **the English text is the one that counts**.
- Reading a translation, like reading the English text, does not bind anyone to the Constitution.

| Language | In English | Start here |
|---|---|---|
| Español | Spanish | [Open](es/README.md) |
| हिन्दी | Hindi | [Open](hi/README.md) |
| العربية | Arabic (Modern Standard) | [Open](ar/README.md) |
| Bahasa Indonesia | Indonesian | [Open](id/README.md) |
| 中文（简体） | Chinese (Simplified) | [Open](zh/README.md) |
| Português (Brasil) | Portuguese (Brazilian) | [Open](pt/README.md) |
| বাংলা | Bengali | [Open](bn/README.md) |
| Français | French | [Open](fr/README.md) |
| اردو | Urdu | [Open](ur/README.md) |
| Русский | Russian | [Open](ru/README.md) |
| 日本語 | Japanese | [Open](ja/README.md) |
| Türkçe | Turkish | [Open](tr/README.md) |
| मराठी | Marathi | [Open](mr/README.md) |
| Tiếng Việt | Vietnamese | [Open](vi/README.md) |
| فارسی | Persian | [Open](fa/README.md) |
| తెలుగు | Telugu | [Open](te/README.md) |
| 한국어 | Korean | [Open](ko/README.md) |
| தமிழ் | Tamil | [Open](ta/README.md) |
| ไทย | Thai | [Open](th/README.md) |

How languages are chosen and translated: [Reader-language editions](../doc_architecture.md#reader-language-editions).

## Translation audits and review status

From the repository root, run `make translation-audit` to check source drift,
structural markers, local links and fragments, glossary surface forms, and the
Chapter Five definition directory. Focused commands are listed in
[`tools/README.md`](../tools/README.md#translation-maintenance).

The inventory in [`review_status.json`](review_status.json) records source and
translation hashes for future drift checks. Initial hash snapshots do **not**
mean the translation is current or reviewed. A translation is marked reviewed
only after an independent fluent reader checks it against English, consistent
with the [translation lane](../CONTRIBUTING.md#lane-f). Exact glossary-form
matches and structure counts are prompts for review; they do not certify
translation meaning.

Run `make translation-manifest-sync` after adding a translation file and its
locale README row. It registers new pairs as unreviewed and leaves existing
review records intact. After an independent fluent review, use the
`record-review` command documented in [`tools/README.md`](../tools/README.md#translation-maintenance)
to store the reviewer, date, and current content hashes.

**Help translate.** If you read one of these languages fluently, you can report errors, suggest glossary terms, or volunteer to look after a language. See the [translation lane](../CONTRIBUTING.md#lane-f). Full translation and resync work is paused until the English edit pass is finished, so some translations may be behind the English for now.

Back to the [main page](../README.md).
