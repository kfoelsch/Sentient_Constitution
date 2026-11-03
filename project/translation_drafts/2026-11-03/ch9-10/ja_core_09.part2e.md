### 4. 関係する場合の評価

<details>
<summary><strong><span style="color: #2563eb;">追跡関係</span></strong></summary>

- 上流：[§3](#3-whole-system-certification-evaluation)（*常時適用の小段階を含むシステム全体評価*）；[§2](#2-system-class-evaluation)（*システムクラス評価*）；[第一章 §12 システム評価要件](core_01.000_values_principles.md#12-systemic-evaluation-requirement)（1.000 §12）。
- 下流：
  - [§4.1](#41-privacy-informational-joint-invocation)（*プライバシー領域*）；
  - [§4.2](#42-voluntary-discontinuation-major-self-modification-and-exit-rights)（*退出権*）；
  - [§4.3](#43-assembly-collective-organization-and-institutional-formation)（*集会と異議*）；
  - [C部 §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)（9.010 §8）（*記録の内容*）。
- 併読：[§5 権利の床および領域別評価](#5-rights-floor-and-domain-evaluations)（*発動条件を満たす場合に適用される小段階*）。

</details>

<br>

*平たい言葉で言えば：三つの審査は、システムが実際に関係する場合に限り適用される。個人情報が適切に隔離されているか、感知者が閉じ込められずに退出できるか、集団が組織化し異議を申し立て続けられるかを確認する。システムがそのいずれかに関わるなら、認証では審査しなければならない。*

本節は、第II段階（評価）の小段階**IIb**である。各小節の発動条件が満たされる場合に限り適用されるシステム全体評価をまとめる。

<a id="41-privacy-informational-joint-invocation"></a>
#### 4.1 プライバシー（情報）の共同適用

<details>
<summary><strong><span style="color: #2563eb;">追跡関係</span></strong></summary>

- 併読：意味を所管する第五章の[**Def.C3**（*プライバシー（情報）* — 同階層クラスターの見出し）](core_05.040_band_continuity.md#defc3-privacy-informational--peer-level-cluster-head)およびクラスター見出しの根拠である[プライバシー（情報）](core_05.040_band_continuity.md#privacy-informational)。

</details>

<br>

*平たい言葉で言えば：第六章はプライバシー保護を一つの整理された領域ではなく、複数の条文に分散している。認証審査がそのうち複数に関係する場合、審査者は実際に適用されるすべての保護を確認しなければならない。最も簡単な項目だけを満たして終わりにはできない。*

認証案件が第六章の複数のプライバシー領域に実質的に関係する場合、認証では該当する各領域を扱わなければならない。一つの領域だけで案件を終結させるのは不十分である。

**適用される原則。** 以下は各領域を併せて読む際の規律である。

- *共同評価。* 一つの領域を経由させ、別の領域を回避できる形で案件をルーティングしてはならない（[§15.1.1 反セグメンテーション原則](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle)）。
- *横断的な読み替えによる緩和の禁止。* クラスターの各構成要素は、それぞれの範囲内では当該要素に明記された基準に従う。他の構成要素のより緩い基準を持ち込んで緩和してはならない（[§15.1.1 反セグメンテーション原則](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle)）。
- *種類ごとの最低要件を維持。* 本要素は、対象データに適用される**[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*情報の種類と取扱い*）および[CS-6.310](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**（*データ分類*）のいずれの種類の取扱いも狭めない。各種類のアクセス態勢と取扱義務は、[CS-6.310 第B部 §9](corpus_systems/cs_06.310_data_classifications.md#cs-6310-9-data-classifications)（*データ分類*）に従い、当該種類が定める[プライバシー上の根拠](corpus_systems/cs_06.310_data_classifications.md#privacy-link)と併せて全面的に適用する。
- *最も保護的な種類が適用される。* 同じデータに複数の種類が当てはまる場合は、[CS-6.305 第A部 §2](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-2-determination-of-classification)（*分類の決定*）に基づき、適用される中で最も保護的な取扱いが適用される。一種類の取扱いを満たしても、別の種類の義務は免除されない。

**クラスターの各領域。** プライバシー保護は次の条文に分散しており、それぞれが対象とするデータ種類を伴う。

- **第七条-A**（*身体の自己所有権*）—健康、生体情報、基盤に関連づけられた記録に関する[**タイプI**](corpus_systems/cs_06.310_data_classifications.md#95-type-i-identity-and-attribution-data)；
- **第七条-B**（*心の自己所有権*）—再構成または推論を含む内部状態に関する[**タイプN**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data)；
- **第九条**（*肖像、経験データ、公開権*）：
  - [第九条-A](core_06.005_rights_part_b.md#article-ix-a-self-ownership-of-likeness-and-reputation)（*肖像および評判の自己所有権*）に基づく肖像と音声の**タイプI**；
  - [**タイプH**](corpus_systems/cs_06.310_data_classifications.md#94-type-h-historical-relational-transactional-and-participation-data) — [第九条-B](core_06.005_rights_part_b.md#article-ix-b-experiential-and-derived-data-rights)（*経験データと派生データの権利*）に基づく経験データおよび相互作用から得られるデータ；および
  - [**タイプY**](corpus_systems/cs_06.310_data_classifications.md#98-type-y-yours) — [第九条-D](core_06.005_rights_part_b.md#article-ix-d-creative-work-training-data-use-and-anti-displacement)（*創作物、学習データ利用、置換防止*）に基づく作成者の作品。その保護は[**タイプW**](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published)、[**タイプU**](corpus_systems/cs_06.310_data_classifications.md#911-type-u-use-licensed)、[**タイプT**](corpus_systems/cs_06.310_data_classifications.md#912-type-t-transferred)にも引き継がれ、作成者の[留保権](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)と併せて適用される；
- **第十条-A**（*主体性と操作からの自由*）—再構成または推論を含む内部状態に関する[**タイプN**](corpus_systems/cs_06.310_data_classifications.md#96-type-n-neurocognitive-and-internal-data)；および
- **第十四条-A**（*セキュリティ、諜報、秘密権力の制限*）—制限付きのセキュリティ・調査資料に関する[**タイプS**](corpus_systems/cs_06.310_data_classifications.md#97-type-s-safety-security-and-restricted-investigation-data)。制限が終了しても、その**H**、**I**、**N**要素は各種類の保護を維持する。

**認証で示すべき事項：**

- *参加の実効性。* [プライバシー（情報）](core_05.040_band_continuity.md#privacy-informational)は実質的な[参加](core_05.025_apex_participation_leg.md#participation-constitutional)を可能にする。認証では、発言、熟議、結社、異議申立てを支えるプライバシー保護が、分割、横断的読み替え、または情報露出の圧力によって損なわれていないことを確認しなければならない。
- *公開され監査可能な種類。* 下限は両方向に適用される。
  - **タイプE**、**タイプG**、**タイプO**の資料に含まれる個人、関係性、内部状態の内容は、その**H**、**I**、**N**の取扱いを維持する；
  - プライバシー領域があるからといって、その領域だけで、**タイプO**または**タイプE**のデータを各規則が認める狭い留保を超えて非公開にできるわけではない；および
  - プライバシー保護と公衆が知る権利のある情報の公開が真に衝突する場合、どちらも自動的に優先されない。**[CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)**（*クラスA／B／CシステムのタイプO基準*）に従い、対立を公開の記録上で決定する。
- *データ種類の証拠。* 認証では、[システムデータ種類記録](core_05.040_band_continuity.md#system-data-types-record)を[§3.4 データの種類と取扱いの評価](#34-data-types-and-handling-evaluation)に基づき検証し、対象となる各プライバシー領域の証拠として使用しなければならない。証拠には対象の種類とその目的、受領者、根拠、派生データを含む。その記録に示されていない取扱いを根拠に、プライバシー領域を終結させてはならない。

<a id="42-voluntary-discontinuation-major-self-modification-and-exit-rights"></a>
#### 4.2 自発的な停止、大幅な自己改変、退出権

認証案件に[第一章 §7.4 自発的な停止、大幅な自己改変、退出権](core_01.000_values_principles.md#74-voluntary-discontinuation-and-exit-rights)が適用される場合、認証の主張が成立する前に、認証では自発性、同意、反強制、依存圧力、情報、可逆性を検証しなければならない。形式的な同意だけでは不十分である。

<a id="43-assembly-collective-organization-and-institutional-formation"></a>
#### 4.3 集会、集団的組織化、機関の形成

認証案件に[第一章 §7.2 集会、集団的組織化、機関の形成](core_01.000_values_principles.md#72-assembly-collective-organization-and-institutional-formation)が適用される場合、認証では[反セグメンテーション原則](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle)に基づき問題を一体として検証しなければならない。集会または集団的組織化の保護を損なう形で、一つの枠組みだけを通して案件をルーティングするなら、評価は不完全である。

<a id="431-dissent-and-peaceful-protest"></a>
