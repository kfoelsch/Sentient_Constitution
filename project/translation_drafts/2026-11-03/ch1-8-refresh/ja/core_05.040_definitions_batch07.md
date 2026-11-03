# Chapter Five definition batch 07 — Certification Denial (ja)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Certification Denial; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 認証拒否

<details>
<summary><strong>トレース</strong></summary>
- 正準の所管：[第9章 パートB §7.4 拒否と取消し](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation)。
- クラスター構成要素：なし。本項目は[システム整合性認証](core_05.040_band_continuity.md#system-alignment-certification)の話題群に隣接しますが、その一部にはなりません。
- [認証取消し](core_05.040_band_continuity.md#certification-revocation)、[暫定認証](core_05.040_band_continuity.md#provisional-certification)、[完全認証](core_05.040_band_continuity.md#full-certification)、[再認証](core_05.040_band_continuity.md#recertification)、[是正準備状況](core_05.035_band_accountability.md#remediation-readiness)、[システム認証記録](core_05.040_band_continuity.md#system-certification-record)と併せて読む。
</details>

*平たく言えば、**認証拒否**とは、まだ認証を得ていないシステムの運営者が問題を是正する意思と能力の両方を示していないため、認証を拒むことです。脅しではなく実際の結果です。システムの認証状態を変えますが、それだけでシステムを停止するものではありません。*

- **内容**
  - **対象範囲：** 初回認証、新規審査、その他の認証一巡において、認証状態のないシステムに対し、是正準備状況の確認で運営者が整合不全または認証欠陥を是正する意思と能力の両方を示せなかったため、認証しない結果となること。
  - **対象外：**
    - 既に取得した認証を取り消す[認証取消し](core_05.040_band_continuity.md#certification-revocation)。
    - 決定を限定期間延期する認証延期。これは何も拒否しません。
    - 運用停止命令。これは[第9章 パートC §9.3.5](core_09.010_system_alignment_certification_record_recertification.md#935-class-a-reliance)の生存必須保護に基づき別途決定します。
    - 地位への影響または違反認定。地位を決めるのは[第11章](core_11.000_standing_assessment.md#chapter-eleven-compliance-violation-and-standing-model)だけです。
    これらは各自の項目に属します。
  - **依存先：** [システム整合性認証](core_05.040_band_continuity.md#system-alignment-certification)。
  - 条件と手続は[第9章 パートB §7.4](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation)、影響は[§7.5 拒否の影響](core_09.005_system_alignment_certification_record_process.md#75-effects-of-denial-and-revocation)にあります。本項目は第5章の意味だけを示します。
<a id="certification-denial-a"></a>
- **測定と評価**
  - **主要測定：** [継続性の測定群](core_05.010_apex_continuity_aim.md#measuring-continuity-preamble-measurement-family) — *感知者とシステムは、生態的に、確実に、そして障害を越えて持続できますか。*

    **主要評価：**
    1. 拒否が、運営者の規模、年齢、資産、競合利益ではなく、是正する意思と能力が示されなかったという記録上の認定に基づくこと。
    2. 拒否の発効前に暫定保護と依拠制限が明示され、システムに依存する感知者へ伝えられること。
    3. 拒否決定前に、運営者が認定の通知を受け、回答または証拠段階を示す機会を持つこと。
<a id="certification-denial-c"></a>
- **満たすべき要件**
  - **主要な不履行：**
    - 是正準備状況の認定を記録せずに、または是正と関係のない理由で認証を拒否すること。
    - 是正準備状況が拒否を要するのに条件付き認証を与えること。
    - 代替手段が整う前に生存必須サービスを断つ命令として拒否を扱うこと。
    - 認証拒否をしながら、システムの依存者へ知らせないこと。
