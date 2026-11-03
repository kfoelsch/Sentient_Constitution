# Chapter Five definition batch 15 — Go-Live (ja)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Go-Live; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 稼働開始（Go-Live）

<details>
<summary><strong>出典</strong></summary>

- 正規の所管: 第九章B部§7.1稼働開始ゲート。本項はシステム適合認証のトピック群に属さず隣接する。下流: 第九章A部§2.3パイロット認証。パイロット、暫定/完全認証、システム認証記録、重大な影響、依存関係、システム境界、可逆性と併読。

</details>

*平易に言えば、システムが構築・試験段階を離れ、sentientに実際の影響を及ぼす、またはsentientが依存し始める時点である。名称でなく実際の運用で判断する。*

- **What it is**
  - **In scope / out of scope / dependencies:** 対象: システムがsentientに重大な影響を与える、または重大な依存対象となる最初の運用時点。パイロット、パイロット後の本格配備、認証範囲を超える重大な拡張は各々独立した稼働開始。ベータ、試行、プレビュー、早期アクセス、ソフトローンチ、実験、発表日、社内節目という表示では決まらない。対象外: 開発・検証・ステージング・シミュレーションで実影響/依存がない運用; 重大な影響も依存もないシステム; 採択文書発効時に既に稼働するシステム（第XXVIII-A条の移行期間で扱い、二度目の稼働開始としない）; 重大拡張でない通常変更。重大な影響と依存関係に依存。ゲート、通知期間、条件確認は第九章B§7.1。本項は第五章の意味のみ。
<a id="go-live-a"></a>
- **How to measure and assess**
  - 継続性測定群で評価: 実際の重大影響/依存開始から日付を特定し、名称・発表・社内節目に頼らない。システム記録の最早許可日より前に実影響運用がないこと。パイロット、本格配備、重大拡張をそれぞれ別の稼働開始として扱うこと。
<a id="go-live-c"></a>
- **What must hold**
  - **Primary failure:** 主な不履行: ゲート前の稼働、ベータ等への改称で稼働を隠す、段階分割で全体としてゲートを逃れる、重大拡張を以前の継続と扱う、開始日を事後設定する。
