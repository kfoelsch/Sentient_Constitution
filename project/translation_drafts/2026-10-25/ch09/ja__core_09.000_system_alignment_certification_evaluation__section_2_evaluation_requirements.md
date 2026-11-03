<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (ja)

## English source (lines 311–335)

This section states what certification must verify:

- **Evaluation requirement:**
  - whether the assigned system class reflects observed and reasonably foreseeable **impact**, **dependency**, and **risk** under CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*), including:
    - aggregate effects;
    - interaction effects;
    - adversarial effects;
    - threshold effects;
  - that classification is determined by actual system behavior and impacts, not from:
    - declared intent;
    - nominal scope;
    - [System Charter](core_05.040_band_continuity.md#system-charter) text alone; or
    - self-description alone;
  - that the system's class was re-checked under the **[CS-9.305 §3.5 reclassification requirement](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** whenever a significant change called for it; and
  - that the [System Classification Record](core_05.040_band_continuity.md#system-classification-record) shows the **highest system class that applies** under current conditions.
- **Assurance and regression testing:**
  - that system-class-scaled assurance, infrastructure robustness, and regression coverage match the assigned system class under:
    - CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*); and
    - CS-6.345 (*System lifecycle*), read with these shared operational terms where materially applicable:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Continuity: graceful degradation and failure-mode integrity terms*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Continuity: reversibility and containment terms*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Continuity: adversarial robustness and abuse-resistance terms*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Integrative: constrained-secrecy and protected-investigation terms*), where the system's class or function makes it materially applicable; and
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Integrative: intervention and override integrity terms*), where the system's class or function makes it materially applicable; and
  - that regression testing was run for each recertification, as CS-6.345 (*System lifecycle*) requires, with its results on the record under [§8.1 Minimum record contents](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).

## Translation draft

この節では、認証が何を検証しなければならないかを定める。

- **評価要件：**
  - 割り当てられたシステムクラスが、CS-9.305（*システム分類の仕組み*）およびCS-9.310（*システム影響分類*）に基づく観察済みかつ合理的に予見可能な**影響**、**依存性**、**リスク**を反映しているか。これには次を含む。
    - 集積効果
    - 相互作用効果
    - 敵対的効果
    - 閾値効果
  - 分類は実際のシステム動作と影響によって決まり、次のものによって決まるのではないこと。
    - 表明された意図
    - 名目上の範囲
    - [システム憲章](core_05.040_band_continuity.md#system-charter)の文面だけ
    - 自己説明だけ
  - 重大な変更により必要となる場合には、**[CS-9.305 §3.5の再分類要件](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**に従ってシステムクラスが再確認されたこと。さらに、
  - [システム分類記録](core_05.040_band_continuity.md#system-classification-record)が、現状で適用される**最も高いシステムクラス**を示していること。
- **保証および回帰テスト：**
  - システムクラスに応じた保証、インフラの堅牢性、および回帰テスト範囲が、次に基づく割当クラスと一致していること。
    - CS-9.305（*システム分類の仕組み*）およびCS-9.310（*システム影響分類*）；ならびに
    - CS-6.345（*システムライフサイクル*）。実質的に該当する場合、次の共通運用用語も併せて読む。
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c)（*継続性：段階的縮退および故障モード完全性の用語*）
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c)（*継続性：可逆性および封じ込めの用語*）
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c)（*継続性：敵対的状況への堅牢性および悪用耐性の用語*）
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms)（*統合：制約付き秘匿および保護された調査の用語*）。システムクラスまたは機能により実質的に該当する場合。ならびに
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms)（*統合：介入およびオーバーライド完全性の用語*）。システムクラスまたは機能により実質的に該当する場合。ならびに
  - CS-6.345（*システムライフサイクル*）の要件どおり各再認証で回帰テストが実施され、その結果が[§8.1 記録の最低限の内容](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents)に基づき記録されたこと。
