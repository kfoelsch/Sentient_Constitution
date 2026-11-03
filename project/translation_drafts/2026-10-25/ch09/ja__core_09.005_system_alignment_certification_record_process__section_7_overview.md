### 7. 認証の結果

<details>
<summary><strong><span style="color: #2563eb;">参照経路</span></strong></summary>

- 上流：
  - [§6](#6-forum-process)（*フォーラム手続および信頼できる異議申立て*）；
  - [パートA §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation)（9.000 §2）から
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations)（*評価で見つかった誤分類、不整合、および欠陥*）まで；
  - [二つの憲法上の目的](core_00.000_preamble.md#two-constitutional-aims)；
  - [第三章 §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints)（3.000 §1）および
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior)（*定義の完全性と回避*）；
  - [第三章 §2.1 一般的な回避パターン](core_03.000_definition_integrity.md#21-common-evasion-patterns)（3.000 §2.1）（*範囲と境界の回避*）；
  - [システム憲章](core_05.040_band_continuity.md#system-charter)（*システム憲章と実際の挙動との不一致および期限を過ぎた審査*）。
- 下流：
  - [パートC §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)（*結果を記録に記載する*）；
  - [パートC §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification)（*結果とともに異議申立て経路を開く*）；
  - [パートC §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening)（*再認証および再開*）；
  - [パートC §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing)（*事実が不利益な所見を裏付ける場合の検証済み入力ゲート*）；
  - [第十三章](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction)（13.000）（*フォーラムの監督*）；
  - [第十章](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement)（10.000）。
- 次と併せて読む：定期的なデータ種別の再評価については**[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)**（*再分類およびライフサイクル管理*）、システムクラスの再評価トリガーとSAC検証については**[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**（*再分類の要件*）。
- 小節：
  - [§7.1](#71-go-live-gate)（*稼働開始ゲート*、以下を含む
  - [§7.1.1 すでに稼働しているシステム](#711-systems-already-operating)および
  - [§7.1.2 パイロット](#712-pilots)）；
  - [§7.2](#72-certification-defects-and-correction)（*認証の欠陥と是正*）；
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct)（*是正の準備態勢：是正する意思と能力*、以下を含む
  - [§7.3.1 意思](#731-willingness)、
  - [§7.3.2 能力](#732-capacity)、
  - [§7.3.3 立証段階](#733-proof-step)、
  - [§7.3.4 所見](#734-findings)、および
  - [§7.3.5 すべての運営者に同じ条件](#735-same-terms-for-every-operator)）；
  - [§7.4](#74-denial-and-revocation)（*拒否および取消し*、以下を含む
  - [§7.4.1 拒否および取消しとは](#741-what-denial-and-revocation-are)、
  - [§7.4.2 拒否または取消しが必要な場合](#742-when-denial-or-revocation-is-required)、
  - [§7.4.3 保護を優先](#743-protection-first)、
  - [§7.4.4 手続](#744-process)、
  - [§7.4.5 効果](#745-effect)、および
  - [§7.4.6 恒久的な禁止ではない](#746-not-a-permanent-bar)）。

</details>

<br>

*平易に言えば、認証審査はすべて、明示された結果で終わる。その結果は、証拠と過程で提起された懸念に裏付けられる。システムは、認証を受け、公開された結果によって影響を受けるsentientsに実際に異議を申し立てる機会が与えられ、稼働開始前に必要な保護措置が確認されるまで、稼働を開始しない。*

この節は、[§6 フォーラム手続](#6-forum-process)（**第III段階、審査**）に続く**第IV段階、決定**である。フォーラムが下す結果を扱う。[§7.1 稼働開始ゲート](#71-go-live-gate)は稼働開始ゲートを定め、[§7.2 認証の欠陥と是正](#72-certification-defects-and-correction)は欠陥が見つかった場合の対応を定める。

認証決定は、そこに至る過程で提起された懸念とともに、[パートC §8.1 記録の最低限の内容](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)に基づいて結果を記録に明記しなければならない。結果は次のいずれかである。

- 暫定認証；
- 完全認証；
- 条件付き認証；
- 延期された認証；
- 非認証；
- 撤回；
- 失効；または
- 条件の解除。

暫定認証も完全認証も受けていないシステムは**未認証**である。認証が次のいずれかである場合が該当する。

- 延期；
- 拒否；
- 撤回；または
- 失効。

暫定認証と完全認証は、認証の二つの**ステータス**である。[パートC §9.2 暫定認証と完全認証](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification)は、システムがそれぞれのステータスを取得し、維持し、失う方法を説明する。条件付き認証の条件は、どちらのステータスにも付されることがある。

<a id="71-go-live-gate"></a>

