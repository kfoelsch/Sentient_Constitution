##### 5.3.4 地図と記録の完全性

依存関係図と資源フロー記録に依拠する前に、認証はそれらが **Article V-A** (*依存関係マッピングと資源フローの透明性*) を満たすことを確認しなければならない。これらは次の条件を満たす必要がある。

- **完全であること：** 重要な上流・下流の依存関係、資源フロー、および重要性がある場合には隠れた関係や偏った関係を網羅する。
- **最新であること：** 変化の速さとシステムの重要性に応じて十分な頻度で更新され、[§2 システムクラス評価](#2-system-class-evaluation) におけるシステムクラスも考慮されている。前回の認証時ではなく、現在稼働しているシステムを示す。
- **監査可能であること：** **Article XVI-A** (*監査可能性と観察可能な証拠*) に基づく監査に開かれている。

これらの条件のいずれかを満たさない地図または記録は、システムが十分な還元を行っているとの認定を裏付けられない。その不足を記録し、以下の *欠陥と不整合* に従って扱わなければならない。

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 システムクラスに応じた段階化と審査強化

システムのクラスは、審査の深さと十分性の判断の厳しさを決める。共有資源からの抽出を過小に数えることは決して許されない。また、主体、記録、期間に分割された抽出も、[第一章 §15.1.1 分割禁止原則](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle) に従って一体として評価する。実質性の発動条件が満たされる場合は、常に次のとおりとする。

- 感知者の生存に必要な共有基盤（共有流域や地域電力網の基幹部分など）に依存するシステムは、最も強い依存関係図と還元フローの証明を記録に残さなければならない。これらは、[第一章 §9 共有システムの能力](core_01.000_values_principles.md#9-shared-system-capacity) が持続的な能力を保護する共有システムであり、ここで最も強い証明が求められるのは **Article III-A** (*生存*) のためである。
- 共有認証、医療IT、または類似の基盤に依存するシステムは、何を利用し、その支援が十分かを、運用の重要度に応じた深さで文書化しなければならない。「相互運用性」という曖昧な標語は証拠にならない。[第一章 §18.5 モジュール型アーキテクチャと依存規律](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline) が求めるとおり、依存関係を地図と記録に明示する。
- システムは、現実的に乗り換えられない機関にとって、決済、身元確認、または人員配置の隘路へと密かに変化しながら、システム横断審査を回避してはならない。
  - **乗り換えられない主体：** [§5.3.3 評価要件](#533-evaluation-requirement) にある代替可能性の要因によって判断する。
  - **重要な理由：** これは[第一章 §11.4 資源と依存関係の集中](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) が述べる集中の類型である。同条は、現実的な代替先がない単一の提供者に依存する感知者やシステムの数、または共有基盤のインターフェースとアクセス地点を誰が管理するかなど、その水準を採用者が設定するよう求める。認証は、採用者が定めた水準を超えるまで審査強化を待たない（以下参照）。
  - **認証が行うこと：** 審査を強化し、[§2.2 すべての評価におけるシステムクラスの段階化](#22-how-system-class-scales-every-evaluation) に従ってシステムクラスを再検討する。システムが生存に不可欠な調整へのアクセスを管理する場合は、**Class A** まで引き上げる。

審査強化は、[第一章 §11.4 資源と依存関係の集中](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) に基づき設定される集中のしきい値を待たない。採用者が定め、システムが超えたしきい値は、追加の証拠となる。しきい値が未設定または高すぎても審査強化を遅らせない。また、しきい値を超えたことだけで不正行為の認定とはならない。

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 欠陥と不整合

[§5](#5-rights-floor-and-domain-evaluations) (*権利の床と領域別評価*) の欠陥は、**Article V-A** (*依存関係マッピングと資源フローの透明性*) が開示を求める依存関係情報または資源フロー情報を含め、この評価にも適用される。さらに、次の各項目は認証上の欠陥となる。

- 次のいずれかを、[比例的なシステム横断支援](core_05.040_band_continuity.md#proportionate-cross-system-support) を満たすのに十分なものとして扱うこと：
  - 象徴的、不透明、地図にない、または一度限りの移転；
  - システムが **Article III-A** (*生存*) の生存の床を満たしているという事実；または
  - システムが[第一章 §11 市場構造](core_01.000_values_principles.md#11-market-structure) の市場集中制限内にとどまっているという事実。
- 実質性の発動条件が適用されるのに、共有基盤から繰り返し資源を取り出し、それに比例した還元を行わないこと。
- 主として支配的捕捉または集中を固定化する支援。
- **Article V-A** (*依存関係マッピングと資源フローの透明性*) が求める透明性を損なう条件付きの支援。

支援の不足が記録されている場合、[第一章 §6 信頼と信頼性](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) に従って扱う。

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 差別禁止の評価

<details>
<summary><strong><span style="color: #2563eb;">追跡情報</span></strong></summary>

- 上流：
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*記録の内容*)；
  - [§2](#2-system-class-evaluation) (*システムクラス評価*)；参加測定ファミリー (*実質的公正および保護特性の代理指標化と差別的影響を憲法上の測定として扱うこと*)；**Article VI-C** (*差別禁止*)；
  - [実質的公正](core_05.055_band_participation.md#substantive-fairness)、
  - [保護特性](core_05.055_band_participation.md#protected-characteristics)、
  - [保護特性の代理指標化と差別的影響](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact)、
  - [言語、文化、遺産](core_05.040_band_continuity.md#language-culture-and-heritage)、
  - [必要性](core_05.035_band_accountability.md#necessity)、および
  - [比例性](core_05.035_band_accountability.md#proportionality)（第五章）。
- 上流：原則：第一章
  - [§3.1 公正](core_01.000_values_principles.md#31-fairness)（特に[§3.1.2 利益と負担](core_01.000_values_principles.md#312-benefits-and-burdens)）および
  - [§11.4 資源と依存関係の集中](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*門番化；§5.4.2 の審査強化*)。
- 下流：
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*システムクラス別の差別禁止適用例*)；
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*記録の完全性*)；
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*検証済み入力のゲート*)；
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*差別パターンによる不整合と代理指標による回避*)。
- 併読：認証がフォーラム、行政、または執行へのアクセスをゲートする場合の **Article VI-C** (*差別禁止*) の裁定・運用上の義務；[*差別禁止、保護特性、尊厳、親密シグナルのゲーティング、および **Article VII-E** (*成人の合意に基づく商業的性サービスと性的搾取*) の地位*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination)。
- 小節：
  - [§5.4.1](#541-evaluation-requirement) (*評価要件*)；
  - [§5.4.2](#542-system-class-scaling-and-escalation) (*システムクラスに応じた段階化と審査強化*)；
  - [§5.4.3](#543-defects-and-misalignment) (*欠陥と不整合*)；
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*システムクラス別の差別禁止適用例*)。

</details>

<br>

*平たい言葉で言えば：システムの中には、誰が参加できるかを決めるものがある。より高い料金を誰に課すかを決めるものもある。順位を下げたり、より重い負担を負わせたりするものもある。こうした決定が重要な影響をもつ場合、認証は一つの問いを立てる。害は主として保護特性をもつ感知者に生じているか、それともその特性の代わりとなる形質に生じているか。運営者が規則は中立だと言うだけでは、この問いへの答えにならない。適用例：[CS-9.320 §9 システムクラス別の差別禁止適用例](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class)。*

この節は、実質的な影響をもつシステムが、資格規則、モデル特徴、順位付けの論理、プラットフォーム方針、または同等の意思決定経路を通じて、感知者を実質的に分類、順位付け、価格設定、アクセス制限、排除し、または負担と利益を配分する場合に適用される。

実質性の発動条件が適用される場合、システム整合性認証は **Article VI-C** (*差別禁止*)、[実質的公正](core_05.055_band_participation.md#substantive-fairness)、および[保護特性の代理指標化と差別的影響](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) に基づいて**差別禁止**を評価しなければならない。

<a id="541-evaluation-requirement"></a>
##### 5.4.1 評価要件

*平たい言葉で言えば：この章は包摂の割当てを定めない。公正の公式も選ばない。それらは他の文書が扱うことがある。今後コーパスに加わる文書や、採用者が作成する文書も同様である。認証が確認するのは、誰が利益を得て誰が負担を負うのか、また保護特性の代替指標が使われているかを、実際に誰かが検討したかだけである。この評価は発動条件が適用されるすべての場面に適用される。*

認証プロセスは、システムが実質的に依拠する意思決定経路が、次のいずれかに基づいて感知者に実質的な負担、排除、または害をもたらすかを判定しなければならない。

- [保護特性](core_05.055_band_participation.md#protected-characteristics)；
- その代理指標；または
- [言語、文化、遺産](core_05.040_band_continuity.md#language-culture-and-heritage) の専門性を含め、機能上その代用となる恣意的な集団分け。

評価は、[実質的利害](core_00.000_preamble.md#material-stake) に応じた規模で、次を行わなければならない。

- [実質的公正](core_05.055_band_participation.md#substantive-fairness) に基づき、負担と利益のパターンを検証する。
- [保護特性の代理指標化と差別的影響](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) に基づき、代理指標または差別的影響のリスクを検証する。

異なる取扱いが許されるのは、文書化された[必要性](core_05.035_band_accountability.md#necessity)、[比例性](core_05.035_band_accountability.md#proportionality)、および実質的公正によって正当化される場合に限る。評価は名目上の中立性、表明された意図、またはラベルだけでなく、機能上の効果を反映しなければならない。

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 システムクラスに応じた段階化と審査強化

システムクラスは評価の深さを定める。順位付けや負担の転嫁を重要でないものとして扱うことは許されない。実質性の発動条件が満たされる場合、次を適用する。

- **停止、通知、または同等の規則によって生存必需品を断つ可能性のあるシステム：**
  - 記録には、一般的なベストプラクティスの記述ではなく、負担・利益と代理指標について最も強い分析を含める。
  - 隠れた費用転嫁は[第一章 §3.1.2 利益と負担](core_01.000_values_principles.md#312-benefits-and-burdens) を満たさない。
- **照合または経路選択の論理が救急医療、給付、または資格へのアクセスに影響するシステム：**
  - 記録には、運用上の重要度に応じた差別的影響と実質的公正の認定を文書化する。
  - その理由は、[第一章 §3.1 公正](core_01.000_values_principles.md#31-fairness) における公正が、感知者を説明のない規則で扱わず、他者が避ける費用を負わせたままにしないことを意味するからである。
- **シフト、業者、または予約の論理によって参加者を実質的に順位付けまたは排除するシステム：**
  - 実質的な分析の代わりに、名目だけの公正に関する段落を置いてはならない。
  - 調整が生存に不可欠となる場合、認証は[§2.2 すべての評価におけるシステムクラスの段階化](#22-how-system-class-scales-every-evaluation) に従い、審査と再分類を強化しなければならない。これには、人員配置または緊急時の経路選択をゲートする場合の **Class A** への再分類を含む。
  - この種の門番化は、[第一章 §11.4 資源と依存関係の集中](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) における集中の指標である。多くの感知者やシステムが、現実的な代替先のない単一の提供者に依存するためであり、これがここで認証が審査を強化する理由である。

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 欠陥と不整合

この評価には、二組の欠陥が適用される。

- **節全体に適用される欠陥：**
  - [§5](#5-rights-floor-and-domain-evaluations) (*権利の床と領域別評価*) の欠陥はこの評価にも適用される。
  - **Article VI-C** (*差別禁止*) が審査を求める実質的な分類、順位付け、または負担配分の論理にも適用される。
- **差別禁止に関する欠陥：** 次の各項目も認証上の欠陥として扱わなければならない。
  - 負担と利益の評価可能な分析を行わず、表面上の中立性、総計上の利便性指標、または運営者の自己申告だけで十分とすること。
  - **Article VI-C** (*差別禁止*) の**必要性**および**比例性**の検査を満たさずに、均質化、相互運用性、または効率性の枠組みを用いて言語、文化、遺産の保護を損なうこと。

代理指標による差別または実質的不公正が記録されている場合、[第一章 §6 信頼と信頼性](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) に基づいて扱う。

<a id="55-accessibility-evaluation"></a>
