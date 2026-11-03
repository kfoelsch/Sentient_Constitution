<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (zh)

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

本节规定认证必须核验的事项：

- **评估要求：**
  - 按照 CS-9.305（*系统分类机制*）和 CS-9.310（*系统影响分类*），所指定的系统类别是否反映了已观察到且可合理预见的**影响**、**依赖**和**风险**，包括：
    - 汇总效应；
    - 交互效应；
    - 对抗性效应；
    - 阈值效应；
  - 分类依据是系统的实际行为和影响，而非：
    - 声明的意图；
    - 名义范围；
    - 仅凭[系统章程](core_05.040_band_continuity.md#system-charter)文本；或
    - 仅凭自我描述；
  - 每当重大变更要求重新核查时，均已依据 **[CS-9.305 §3.5 重新分类要求](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** 重新核验系统类别；并且
  - [系统分类记录](core_05.040_band_continuity.md#system-classification-record)载明当前条件下适用的**最高系统类别**。
- **保证与回归测试：**
  - 按系统类别调整的保证、基础设施稳健性和回归测试覆盖范围，符合依照下列规定指定的系统类别：
    - CS-9.305（*系统分类机制*）和 CS-9.310（*系统影响分类*）；以及
    - CS-6.345（*系统生命周期*）；在具有实质适用性的情况下，还应结合以下共同运行术语阅读：
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c)（*连续性：平稳降级和故障模式完整性术语*）；
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c)（*连续性：可逆性和遏制术语*）；
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c)（*连续性：对抗稳健性和防滥用术语*）；
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms)（*整合：受限保密和受保护调查术语*），当系统类别或功能使其具有实质适用性时；以及
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms)（*整合：干预和覆盖完整性术语*），当系统类别或功能使其具有实质适用性时；并且
  - 按照 CS-6.345（*系统生命周期*）的要求，每次重新认证均已进行回归测试，并依据[§8.1 记录的最低内容](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents)将结果记入记录。
