#### 3.3 時間的一貫性の制約

予見可能な中期または長期の違反に対処していない場合、認証は次のいずれも十分な根拠として扱ってはならない。

- 短期指標；
- 局所的な遵守；または
- 短い時間軸での効率性。

次のいずれかを将来的に損なうことが合理的に予見されるなら、短期的な成果を追求してはならない。損害がゆっくり積み上がる、遅れて現れる、または複数のシステムにまたがる場合も同じである。

- **安全**；
- **真実**；または
- **ウェルビーイング**。

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 データの種類と取扱いの評価

<details>
<summary><strong><span style="color: #2563eb;">追跡関係</span></strong></summary>

- 上流：
  - [§3](#3-whole-system-certification-evaluation)（*システム全体評価の要素*）；
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class)（*システムクラス別システム全体適用例*）；
  - [C部 §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)（9.010 §8）（*記録の内容*）；
  - [§2](#2-system-class-evaluation)（*システムクラス評価*）；監督測定群（*憲法上の測定としての真実と認識論的完全性*）；
  - [第十五条：情報圏の完全性](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity);
  - [第十六条：監査、透明性、独立検証](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [第七条：自己所有権](core_06.005_rights_part_b.md#article-vii-self-ownership)。
- 下流：
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class)（*システムクラス別データ取扱い適用例*）；
  - [§5.1](#51-ecological-footprint-evaluation)および
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class)（*システムクラス別生態学的負荷適用例*）；
  - [C部 §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record)（9.010 §8.2）（*記録の完全性*）；
  - [C部 §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate)（9.010 §11.3）（*検証済み入力ゲート*）；
  - [B部 §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)（9.005 §7）（*再分類と取扱いの不整合*）。
- 併読：
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*情報の種類と取扱い*）および[CS-6.310 — データ分類](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**。以下を含む。
  - [CS-6.305 §5.2 再分類とライフサイクルのガバナンス](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)（*再分類とライフサイクルのガバナンス*）および
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)（*システムデータ種類記録のガバナンス*）；
  - [システムデータ種類記録](core_05.040_band_continuity.md#system-data-types-record);
  - [公的監督基準開示](core_05.050_band_oversight.md#public-oversight-baseline-disclosure);
  - **CJS-5.130 §18**（*データ保持とライフサイクルの完全性に関する条件*）、
  - **CJS-5.130 §21**（*敵対的堅牢性と悪用耐性に関する条件*）、および
  - 実質的に適用される場合は**CJS-5.130 §17**（*相互運用性、移植可能性、退出の完全性に関する条件*）；
  - プライバシー領域が関係する場合は[§4.1 プライバシー（情報）共同適用](#41-privacy-informational-joint-invocation)。
- 小節：
  - [§3.4.1](#341-type-o-baseline-disclosure)（*タイプOの基準開示*）；
  - [§3.4.2](#342-privacy-discipline)（*プライバシーの規律*）；
  - [§3.4.3](#343-protective-storage-and-key-custody)（*保護的保管と鍵の管理*）；
  - [§3.4.4](#344-scheduled-data-type-re-evaluation)（*予定されたデータ種類の再評価*）；
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance)（*システムクラスに応じたインフラ保証*）；
  - [§3.4.6](#346-infrastructure-robustness-for-data)（*データを扱うインフラの堅牢性*）；
  - [§3.4.7](#347-defects-and-misalignment)（*欠陥と不整合*）；
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class)（*システムクラス別データ取扱い適用例*）。

</details>

<br>

*平たい言葉で言えば：認証では、システムがどの種類のデータに触れ、適切に取り扱うかも確認する。現在の審査周期に照らして種類の分類が妥当か、基盤インフラがそのシステムクラスで当該データを扱うのに十分強固かも含む。種類の規則とシステムデータ種類記録はシステム群に置かれており、認証では規則が実際に適用され、記録が誠実であることを確認する。*

システム整合性認証では、実質的影響を持つ各システム認証記録の一部として**データの種類と取扱い**を評価しなければならない。本節は認証が検証すべき事項を定める。データ種類の分類体系と取扱いの仕組みは、以下と併せて**[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*情報の種類と取扱い*）および[CS-6.310 — データ分類](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**に定める。

- 情報の種類に関する正規定義；
- 取扱い規則と分離要件；
- ライフサイクルの詳細；および
- 永続的な[システムデータ種類記録](core_05.040_band_continuity.md#system-data-types-record)。

**評価要件。** 認証手続は、システムが以下を満たすかを判断しなければならない。

- 実質的に対象となるデータの種類を特定している；および
- 変換、集約、委任、保管、保持、領域横断の連結を含め、適用される分類のうち**最も制限的なもの**に従ってデータを取り扱っている。

評価はラベル、形式、パイプラインの段階だけではなく、機能上の効果を反映しなければならない。

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 タイプO基準開示

**[CS-6.305 §7 タイプO基準](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)**が適用される場合、認証では、公開済みの[公的監督基準開示](core_05.050_band_oversight.md#public-oversight-baseline-disclosure)（**タイプO**）が次から特定した**認証対象範囲**を網羅することも検証しなければならない。

- 適用される[システム憲章](core_05.040_band_continuity.md#system-charter)；
- 割り当てられたシステムクラス；および
- 観測された[システム境界](core_05.040_band_continuity.md#system-boundaries)。

この網羅には、[§3.1 ガバナンス、インセンティブ、争訟可能性の規律](#31-governance-incentive-and-contestability-discipline)に基づき確定したガバナンス、インセンティブ、争訟可能性に関する判断と割当役割を含む。

すべてのシステムクラスで、**クラスL**および**クラスP**も含め、[CS-6.310 第B部 §9.3 タイプO](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data)に従い、システム認証記録が認証データとして**タイプO**で公表されることも検証しなければならない。クラスA、B、C以外では、公表のために公的監督基準開示全体を求めない。

システムリスクが対象となる場合、評価されたリスクを共有することもこの基準を満たす場合がある。公衆が持つ基準上の権利は認証の範囲より広く、[システム分類記録](core_05.040_band_continuity.md#system-classification-record)または[システムデータ種類記録](core_05.040_band_continuity.md#system-data-types-record)に加えて別個の記録を求めるものではない。

正当な非開示・留保にはそれぞれ、合理的に可能な限り最も強い公開代替情報を添えなければならない（例は[§3.4.5 システムクラスに応じたインフラ保証](#345-system-class-scaled-infrastructure-assurance)参照）。用語の所管は第五章にあり、基準内容と公開の仕組みはCS-6.305（*情報の種類と取扱い*）およびCS-6.310（*データ分類*）が所管する。

<a id="342-privacy-discipline"></a>
