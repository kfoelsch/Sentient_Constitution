<!-- Locale: Japanese (ja) | Source commit: 630b161c | Baseline commit: 5148086b9fb43a343616db52cf3ef2018e2c46cb | AI-drafted, unreviewed | Partial changed-passage refresh -->

> **下流：** [第九章 — システム整合認証](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification)；[第十一章 — スタンディング記録](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened)。

> - **憲法上の所管：** 立証責任の配分、適合証拠、定義のトレーサビリティ、可観測性、セキュリティ制約付き検証。本章とあわせて読むスタンディング記録と検証済み入力の規律は**第十一章**が所管する。

> - **所管移転禁止規則：** 本章が扱うのは立証責任、トレース、可観測性、セキュリティ上の制限、証拠のみである。第五章の定義、**第十二章**の貢献またはスタンディング測定、第十四章の反憲法的違反基準を再述しない。検証済み不適合のスタンディングへの経路づけは、[第三章 §3 — 不適合所見プロフィール](core_03.000_definition_integrity.md#3-non-compliance-finding-profiles)および[第十一章 — スタンディング記録](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened)が定める。**第6節**は、第二章から第四章と[第九章 — システム整合認証](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification)の違いを述べる。

| **1 — 誰が立証するか** | 適合を主張する者が立証責任を負う | [§1 排他的執行と立証責任の配分](#1-exclusive-enforcement-and-burden-allocation) |
| **2 — 地図を示す** | 定義から観察可能な行動までの構造化されたトレース | [§2 定義トレーサビリティ要件](#2-definition-traceability-requirement) |
| **3 — 確認可能にする** | 理論上だけでなく実際に地図を検証できるだけの情報をシステムが開示する | [§3 トレーサビリティの可観測性要件](#3-observability-of-traceability-requirement) |
| **4 — セキュリティ上の制限** | 実際のセキュリティ制限は認められるが、口実による遮断は認められない | [§4 セキュリティ制約付き可観測性・検証規則](#4-security-constrained-observability-and-verification-rule) |
| **5 — 何が認められるか** | 証拠は実在し、完全で、独立しており、継続的でなければならない | [§5 適合証拠基準](#5-compliance-evidence-standard) |

**平易な言葉でのアクセス。** [第一章 §5.2 — 平易な言葉へのアクセス（参加および責務ある管理の義務）](core_01.000_values_principles.md#52-plain-language-accessibility-participation-and-stewardship-duty)は、センティエントが権利を行使し、決定に異議を申し立て、適合を検証するために使う統治、裁定、運用資料に適用される。平易な言葉による説明は、第二章から第四章の要件を**変更も軽減もしない**。平易な版が本章の定義または検証規則と異なる場合、それらの規則が優先する。専門用語、複雑さの積み重ね、不透明性を使って[争訟可能性](core_05.035_band_accountability.md#contestability)または[第XVI条：監査、透明性、独立検証](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification)へのアクセスを妨げることは、本章および**第一章 §5.2 平易な言葉へのアクセス（参加および責務ある管理の義務）**に違反する。

- **測定方法（M）** — 各層でどの測定法を適用するか

*平たい言葉で言えば：第2節はトレースマップを要求する。この節は、権限を持つ者または影響を受ける者が、理論上だけでなく実際に地図を確認できるだけの情報をシステムが開示するよう求める。不透明なアーキテクチャ、外部依存、ブラックボックス部品は免責されない。*

- 上流：原則：[第四章 §3 — トレーサビリティの可観測性要件](#3-observability-of-traceability-requirement)；[第一章 §6.2 — 認識的開示の制約](core_01.005_interaction_interpretation.md#132-epistemic-disclosure-constraints)（1.005）。
- 下流：[第四章 §5 — 適合証拠基準](#5-compliance-evidence-standard)；[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*情報の種類と取扱い*）および[CS-6.310 — データ分類](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)、さらに[CS-6.340](corpus_systems/cs_06.340_system_requirements.md#cs-6340-system-requirements)（*システム要件*）— 利用者向け機能面、認証情報、情報種別の取扱い。

暗号技術と情報種別の取扱いは、憲法ならびに**[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*情報の種類と取扱い*）および[CS-6.310 — データ分類](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**に整合しなければならない。実質的に関係する場合、本章に基づく完全な適合検証を可能にし続けなければならない。暗号技術と情報種別の取扱いは、[真実（憲法上の制約）](core_05.050_band_oversight.md#truth-constitutional-constraint)、[安全性（憲法上の制約）](core_05.040_band_continuity.md#safety-constitutional-constraint)、または**第2節**、**第3節**、**第5節**の義務に取って代わってはならない。

- 下流：[第十一章 — スタンディング記録](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened)（11.000）。

  - [第一章 §13 — 憲法上の衝突を解決する手続](core_01.005_interaction_interpretation.md#13-constitutional-collision-resolution-process)（1.005 §13）；

- 同一の評価で憲法上の価値または制約が衝突する場合は、[第一章 §13 — 憲法上の衝突を解決する手続](core_01.005_interaction_interpretation.md#13-constitutional-collision-resolution-process)との整合性を保つ

- 下流：[第九章 — システム整合認証](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification)（9.000）；[第十一章 — スタンディング記録](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened)（11.000）。
- あわせて読む：[第九章 §7 — 認証結果](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)（9.005 §7）— 第二章から第四章に基づく検証済み不適合は、過去の認証の有無にかかわらず、認証を再開させるか無効にしうる。

**[第九章 — システム整合認証](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification)**は、実質的に関係する場合、フォーラム監督下の**認証手続**を定める。これには、システム全体の評価領域、システムおよび機関の認証記録義務、認証結果、認証期間、争訟可能性の連鎖、第十一章への検証済み入力ブリッジが含まれる。同章は第二章から第四章を**適用**するが、再述はしない。

- **システムまたは機関の認証記録**を、第二章から第四章に基づく継続的適合の代替とすること
