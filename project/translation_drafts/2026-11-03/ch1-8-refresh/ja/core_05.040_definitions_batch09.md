# Chapter Five definition batch 09 — Certification Revocation (ja)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Certification Revocation; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 認証取消し

<details>
<summary><strong>出典</strong></summary>

- 正規の所管: 第九章B部§7.4拒否と取消し。本項はシステム適合認証のトピック群に属さず、その隣に置かれる。併読: 認証拒否、暫定認証、完全認証、再認証、是正準備状況、システム認証記録。

</details>

*平易に言えば、認証を保有するシステムから認証を取り消すこと。運用者が問題を是正する意思と能力の双方を示さない、不誠実である、または認証条件に違反した場合に行う。脅しではなく実際の結果であり、認証状態を変更する。取消し自体がシステムを停止させるわけではない。*

- **What it is**
  - **In scope / out of scope / dependencies:** 対象: 再認証または再開審査で、是正準備状況の確認が不整合・認証欠陥を直す意思と能力の双方を示さない場合、認証条件を繰り返し見逃すか重大違反した場合、または準備・是正・条件解除の証拠が虚偽、捏造、隠蔽と判明した場合に、既存認証を取り消す結果。対象外: 認証を持たないシステムへの認証拒否、認証を取り上げず期限付きで判断を延期する措置、引用認証から機関へ及ぶ連鎖（第十章§9.5）、および地位・違反の認定（第十一章のみが決定）。システム適合認証と再認証に依存する。条件と手順は第九章B§7.4、効果は§7.5。本項は第五章の意味のみ。
<a id="certification-revocation-a"></a>
- **How to measure and assess**
  - 測定: 継続性測定群。取消しが、通知と回答機会の後に記録された認定に基づき、運用者の規模・年齢・資産・競合利益に基づかないか。暫定保護と依拠制限が発効前に示され、依存する人々に伝わったか。停止が代替手段前に生存必需品を断つシステムは、状態を直ちに変更しつつ、別途認められた暫定依拠の範囲だけ運転を続けたか。
<a id="certification-revocation-c"></a>
- **What must hold**
  - **Primary failure:** 主な不履行: 認定・証拠の通知や回答機会なしに取消すこと、記録上取消しが必要なのに条件付き認証を続けること、代替手段前に生存必需品を断つ命令として扱うこと、依存者に知らせないこと。
