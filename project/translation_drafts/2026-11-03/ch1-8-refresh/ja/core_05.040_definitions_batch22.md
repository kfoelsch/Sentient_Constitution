# Chapter Five definition batch 22 — Pilot (ja)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Pilot; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### パイロット

<details>
<summary><strong>出典</strong></summary>

- 正規の所管: 第九章A部§2.3パイロット認証、第九章B部§7.1稼働開始ゲート。下流: CS-6.345システムライフサイクル。稼働開始、暫定認証、システム認証/分類記録、依存関係、システム的ロックイン、可逆性と併読。

</details>

*平易に言えば、意図的に限定した実運用の開始である。sentientに実影響がある、または依存が始まるため隔離試験ではない。範囲・対象集団・期間を事前に定める。実運用なので開始前に独自の認証が必要で、認証限度を密かに越えてはならない。*

- **What it is**
  - **In scope / out of scope / dependencies:** 対象: 完全配備前に、独自のシステム認証記録で事前明記した範囲・対象・期間に限る稼働開始で、実際に影響/依存が生じるもの。認証は記録上の限度のみを対象とする。超過運用は重大拡張として別の稼働開始となり、事前に独自認証が必要。ベータ、試行、プレビュー等の名称で判断しない。隔離環境のテストや採択移行の段階導入は、定義を満たさない限り対象外。稼働開始とシステム記録に依存。評価の深さ、パイロットを行わない理由は第九章A§2.3。本項は第五章の意味のみ。
<a id="pilot-a"></a>
- **How to measure and assess**
  - 継続性測定群で評価: 開始前に独自認証と範囲・対象・期間が記録されるか; 限度内に留まり、超過運用は事前に別認証を得るか; 別名の実運用をパイロットまたは完全配備として認証するか。
<a id="pilot-c"></a>
- **What must hold**
  - **Primary failure:** 主な不履行: 独自認証不要の試験扱い; 範囲/対象/終了がなく実質的に全面配備のパイロット; 新認証なしの限度超過; 後の拒否・条件付与・取消しをsentientにとって高くつかせる依存やロックインを作ること。
