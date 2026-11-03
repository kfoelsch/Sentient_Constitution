#### 5.6 信頼性とシステム依存の完全性に関する評価

<details>
<summary><strong><span style="color: #2563eb;">追跡情報</span></strong></summary>

- 上流：
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*記録の内容*)；
  - [§2](#2-system-class-evaluation) (*システムクラス評価*)；監督測定ファミリー (*真実と認識上の完全性；憲法上の測定としての信頼性、信頼の劣化、および誤解を招く依存*)；**Article XIII** (*信頼でき信頼性のあるシステムへの権利*)；
  - [信頼性](core_05.040_band_continuity.md#trustworthiness)、
  - [信頼](core_05.040_band_continuity.md#trust)、
  - [信頼の劣化と誤解を招く依存](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance)、
  - [争訟可能性](core_05.035_band_accountability.md#contestability)、
  - [救済と是正](core_05.035_band_accountability.md#redress-and-remediation)、
  - [インセンティブの整合](core_05.045_band_integrative.md#incentive-alignment)、
  - [可逆性](core_05.040_band_continuity.md#reversibility)、
  - [実質性](core_05.050_band_oversight.md#materiality)、
  - [依存関係](core_05.040_band_continuity.md#dependency)、および
  - [リスク](core_05.040_band_continuity.md#risk)（第五章）。
- 上流：原則：第一章
  - [§3.1.5 現在の能力と先回りした支援](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*現在の感知者に機能する異議申立てと審査経路；依存に誤解を招くかは実際に依存する感知者に照らして判断；応答しない人にも届く生存上重要な警報*)、
  - [§4 安全](core_01.000_values_principles.md#4-safety-harm-constraint)、
  - [§6 信頼](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)、
  - [§10 レジリエンスと自己修復型設計](core_01.000_values_principles.md#10-resilience-and-self-healing-design)、および
  - [§11.4 資源と依存関係の集中](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*回避できない依存；§5.6.2 の審査強化*)。
- 下流：
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*システムクラス別の信頼性適用例*)；
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*記録の完全性*)；
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*検証済み入力のゲート*)；
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*誤った信頼による不整合、逆効果のインセンティブによる不整合、および復旧の完全性に関する不整合*)。
- 併読：**Article XIII-A** (*信頼性・信頼性基準*)、**Article XIII-B** (*救済と是正を受ける権利*)、および **Article XVI** (*監査、透明性、独立検証*) — 異議申立てと監査の権利は引き続き各条が所管する；高い自律性をもつシステムが統治または検証経路を実質的に仲介する場合の **Article XIII-E** (*高自律システムとツール仲介プロセスの完全性*)；システムへの継続的依存が生存に不可欠なアクセスに影響する場合の **Article III-A** (*生存*)；身体、健康、または安全に影響する製品・サービスをシステムが提供、掲載、推奨、または助言する場合の **Article III-F** (*安全な製品と健康情報*)；依存するすべての感知者が健康・安全情報を利用できなければならない場合の **Article VI-D** (*アクセシビリティ*)；[第一章 §6 信頼](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) (1.000 §6) および[第一章 §5 真実](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint) (1.000 §5)。
- 運用用語：[CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information) (*参加：開示の十分性と観察可能性に関する用語*) — 製品・サービスの健康・安全情報ならびに評価、順位付け、有料宣伝について；[CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices) (*説明責任：構造審査、是正の緊急度、開示に関する用語*) — 害の報告と是正通知について。
- 小節：
  - [§5.6.1](#561-evaluation-requirement) (*評価要件*)；
  - [§5.6.2](#562-system-class-scaling-and-escalation) (*システムクラスに応じた段階化と審査強化*)；
  - [§5.6.3](#563-defects-and-misalignment) (*欠陥と不整合*)；
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*システムクラス別の信頼性適用例*)。

</details>

<br>

*平たい言葉で言えば：システムが、その発言や行動を感知者が信頼できるか — そして信頼が裏切られたときに異議を唱えられるか — に実質的な影響を及ぼす場合、認証は、依存が実際に正当で、誠実に開示され、修復可能かを確認しなければならない。信頼性指標とテストスイートの設計は他の文書に置かれる。認証は、発動条件が適用される場面で、信頼性、誤った信頼のリスク、および異議申立て経路が実際に評価されたかを確認する。適用例：[CS-9.320 §11 システムクラス別の信頼性適用例](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)。*

この節は、主要なシステムが、感知者が何を頼りにするか — システムが何を行い、限界がどこにあり、何が問題になり得て、どう異議を唱え、問題をどう修正するか — を形作る場合に適用される。これは次を通じて起こり得る。

- 信頼性に関する主張；
- 開示する情報と開示しない情報；
- 実際の運用方法；
- 組み込まれたインセンティブ；
- 失敗からの復旧方法；または
- 感知者がシステムに依存するようになるその他の類似の経路。

実質性の発動条件が適用される場合、システム整合性認証は次に基づいて**信頼性とシステム依存の完全性**を評価しなければならない。

- **Article XIII** (*信頼でき信頼性のあるシステムへの権利*)；
- [信頼性](core_05.040_band_continuity.md#trustworthiness)；および
- [信頼の劣化と誤解を招く依存](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance)。

<a id="561-evaluation-requirement"></a>
##### 5.6.1 評価要件

認証プロセスは、**Article XIII-A** (*信頼性・信頼性基準*) に基づき、感知者がシステムを[信頼](core_05.040_band_continuity.md#trust)する合理的な理由をもち、正確に依存できるかを確認しなければならない。

評価ではさらに、次を検証しなければならない。

- 感知者が、書面上だけでなく、実際にシステムへ異議を申し立て、決定の再審査を受け、問題を修正できること。長い手続に答えたり通過したりするのが容易でない人を含め、現在の感知者にとって機能する必要がある（[第一章 §3.1.5 現在の能力と先回りした支援](core_01.000_values_principles.md#315-present-capability-and-proactive-help)；**Article XIII-A** (*信頼性・信頼性基準*) および **Article XIII-B** (*救済と是正を受ける権利*)）；
- 感知者が、システムに値する以上に信頼したり依存したりするよう誤導される可能性があること。これは、獲得していない信頼を生じさせることや、限界を開示しないことによる場合を含む。平均的な感知者ではなく、実際にシステムを使う感知者に照らして判断する（**Article XIII-C** (*誤った信頼と誤解を招く依存の禁止*)）；
- 健康または安全に影響する製品・サービスについてシステムが提供する情報が正確で、行動に移せるだけ十分に完全であり、それを必要とする感知者が見つけて理解しやすいこと。これには、安全上の警告、健康に関する主張、栄養成分、原材料、アレルゲン情報を含む。また、不明または未検証であることを明確に伝え、「安全」と読める空白を残さないことも含む（**Article III-F** (*安全な製品と健康情報*)、ならびにシステム層の接続規定としての **Article XIII-A** (*信頼性・信頼性基準*) と **Article XIII-C** (*誤った信頼と誤解を招く依存の禁止*)）；
- 健康・安全情報が、感覚、認知、言語のニーズが異なる感知者にも利用でき、判断を行う時点で届くこと。小さな文字に埋もれたり、単一形式だけで提供されたりしてはならない（**Article III-F** (*安全な製品と健康情報*)；**Article VI-D** (*アクセシビリティ*)；[第一章 §3.1.5 現在の能力と先回りした支援](core_01.000_values_principles.md#315-present-capability-and-proactive-help)）；
- その情報が誤りだと判明した場合や製品が危険だと判明した場合、依存したすべての人に、害の緊急度に応じた通知期間（NU-1 から NU-3）内に通知し、本人の所在で連絡がつくこと。また危険な製品または誤情報が、その緊急度に応じた封じ込め期間と訂正期間（CU-1 から CU-4）内に、掲載されているすべての場所で封じ込められ、訂正されること（[第一章 §3.1.5 現在の能力と先回りした支援](core_01.000_values_principles.md#315-present-capability-and-proactive-help)；**Article XIII-B** (*救済と是正を受ける権利*)）；
- システムに組み込まれた報酬が、欺瞞や手抜きを促しているか（**Article XIII-D** (*インセンティブ整合の制約*)）；および
- 重要性がある場合に、失敗を隠したり、誰かの権利をひそかに奪ったりせず、システムが誠実に失敗から復旧できること（**Article XIII-F** (*レジリエンスと自己修復の基準*)）。

検証の規模は、[実質性](core_05.050_band_oversight.md#materiality)、[依存関係](core_05.040_band_continuity.md#dependency)、および[リスク](core_05.040_band_continuity.md#risk) に応じて調整する。

評価は、期間、規模、依存関係を通じた機能上の効果を反映しなければならず、次に基づいてはならない。

- 評判、規模、または宣伝；
- 名目上の保証ラベル；
- 信頼性バッジや提供者の評価点が実際には人員配置や購入を左右しているのに、信頼性について名目だけの段落を置くこと；
- 表明された意図；または
- 過去の実績だけ。

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 システムクラスに応じた段階化と審査強化

審査の深さはシステムクラスによって決まる。実質性の発動条件が満たされる場合、次のとおりとする。

- システムの測定値、警報、または復旧に関する主張によって、世帯や運営者が生存必需品（感知者が生きるために必要なもの）について誤導され得る場合、記録はシステムが信頼できるという主張だけでなく、強い証拠を示さなければならない。依存は、システムの実際の動作によって獲得されなければならないからである（[第一章 §6 信頼](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)）。証拠は次を示さなければならない。
  - 感知者がシステムを信頼できること；
  - 感知者が誤った安心感を抱かないこと；
  - [第一章 §3.1.5 現在の能力と先回りした支援](core_01.000_values_principles.md#315-present-capability-and-proactive-help) が求めるとおり、生存上重要な警報や助言が、受領確認をしない感知者にも届き、応答がない場合は追跡が行われること；および
  - [第一章 §10 レジリエンスと自己修復型設計](core_01.000_values_principles.md#10-resilience-and-self-healing-design) が求めるとおり、システムが失敗から誠実に復旧すること。
- 稼働時間、照合、または緊急時の上書き（「ブレークグラス」アクセス）に関するシステムの主張が、感知者が臨床ケアや緊急サービスを受けられるかを左右する場合（[第一章 §4 安全](core_01.000_values_principles.md#4-safety-harm-constraint) が扱うリスク）、記録はシステムの重要度に見合う詳細さで、次を示さなければならない。
  - 感知者がその主張にどう異議を申し立てられるか；および
  - 感知者がそれに依存するよう誤導される可能性があるか。
- 調整が生存に不可欠となる場合、認証は審査を強化し、[§2.2 すべての評価におけるシステムクラスの段階化](#22-how-system-class-scales-every-evaluation) に従ってシステムクラスを再検討しなければならない。誤解を招く依存が、感知者の生存に必要な調整を断つ可能性がある場合、**Class A** に向けてクラスを引き上げることがある。感知者が現実的に避けられない依存は、[第一章 §11.4 資源と依存関係の集中](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) が指摘する依存関係である。

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 欠陥と不整合

[§5](#5-rights-floor-and-domain-evaluations) (*権利の床と領域別評価*) の欠陥は、**Article XIII** (*信頼でき信頼性のあるシステムへの権利*) が審査を求める実質的な制限、リスク、または失敗履歴を含め、この評価にも適用される。さらに、次の各項目は認証上の欠陥として扱わなければならない。

- 評価可能な[信頼性](core_05.040_band_continuity.md#trustworthiness)の分析を行わず、評判、推奨、規模、または運営者の自己申告だけで十分とすること；
- **Article III-F** (*安全な製品と健康情報*) に基づき、不明または未検証であると明確に伝える代わりに、警告がないことや空欄を製品・サービスが安全である証拠として扱うこと；および
- **Article XIII** (*信頼でき信頼性のあるシステムへの権利*) の信頼性に関する規律および **Article XIII-A** (*信頼性・信頼性基準*) の異議申立てに関する規律を満たさず、効率性、革新性、またはセキュリティの枠組みを用いて開示、争訟可能性、または救済を損なうこと。

誤った信頼、逆効果のインセンティブ、利用できない異議申立て経路、および失敗を隠す復旧慣行が記録されている場合、[第一章 §6 信頼と信頼性](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) に基づいて扱う。

<br>

*フォーラムの手続と結果へ進む：* [第九章、Part B — フォーラムの手続と結果](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes) ([§6 フォーラム手続](core_09.005_system_alignment_certification_record_process.md#6-forum-process) および[§7 認証の結果](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes))。*続いて、記録、再認証、当事者適格への接続へ進む：* [第九章、Part C — 記録、再認証、当事者適格](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing) ([§8 システム認証記録](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) から[§11 当事者適格との関係](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing) まで)。

*各評価領域の適用例：* [CS-9.320 システム整合性認証の適用例](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations)。
