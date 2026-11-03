<!-- AI-assisted translation draft; unreviewed. Source lines 443–513; source SHA-256 c35fb170bf1d5c5feb22099772a0262ae5e7cf22c15f407d9a9103cfa0e5213f. -->

### 7. 认证结果

<details>
<summary><strong><span style="color: #2563eb;">追溯</span></strong></summary>

- 上游：
  - [§6](#6-forum-process)（*论坛程序与可信质疑*）；
  - [A部分§2 系统类别评估](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation)（9.000 §2）至
  - [§5 权利底线与领域评估](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations)（*评估发现的错误分类、不对齐和缺陷*）；
  - [两项宪法目标](core_00.000_preamble.md#two-constitutional-aims)；
  - [第三章§1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints)（3.000 §1）；
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior)（*定义完整性与规避*）；
  - [第三章§2.1 常见规避模式](core_03.000_definition_integrity.md#21-common-evasion-patterns)（3.000 §2.1）（*对范围和边界的规避*）；
  - [系统章程](core_05.040_band_continuity.md#system-charter)（*系统章程与行为不符以及逾期审查*）。
- 下游：
  - [C部分§8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)（*在记录中陈述结果*）；
  - [C部分§9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification)（*结果公布时开放质疑路径*）；
  - [C部分§9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening)（*重新认证与重新开启*）；
  - [C部分§10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing)（*事实支持不利认定时的已核实输入门槛*）；
  - [第十三章](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction)（13.000）（*论坛监督*）；
  - [第十章](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement)（10.000）。
- 一并阅读：关于定期重新评估数据类型，参见**[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)**（*重新分类与生命周期治理*）；关于系统类别重新评估触发条件和SAC核验，参见**[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**（*重新分类要求*）。
- 子节：
  - [§7.1](#71-go-live-gate)（*上线门槛*，包括
    - [§7.1.1 已在运行的系统](#711-systems-already-operating)和
    - [§7.1.2 试点](#712-pilots)）；
  - [§7.2](#72-certification-defects-and-correction)（*认证缺陷与纠正*）；
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct)（*补救准备度：纠正意愿与能力*，包括
    - [§7.3.1 意愿](#731-willingness)、
    - [§7.3.2 能力](#732-capacity)、
    - [§7.3.3 证明步骤](#733-proof-step)、
    - [§7.3.4 认定](#734-findings)和
    - [§7.3.5 对每个运营方采用相同条件](#735-same-terms-for-every-operator)）；
  - [§7.4](#74-denial-and-revocation)（*拒绝与撤销*，包括
    - [§7.4.1 什么是拒绝与撤销](#741-what-denial-and-revocation-are)、
    - [§7.4.2 何时必须拒绝或撤销](#742-when-denial-or-revocation-is-required)、
    - [§7.4.3 保护优先](#743-protection-first)、
    - [§7.4.4 程序](#744-process)、
    - [§7.4.5 效果](#745-effect)和
    - [§7.4.6 并非永久禁止](#746-not-a-permanent-bar)）。

</details>

<br>

*简单来说：每次认证审查都以明确结果结束，并由证据和过程中提出的关切提供支持。在系统获得认证、受影响sentient有切实可行的机会质疑已公布结果、且上线前必须采取的保护措施均经核查之前，系统不得上线。*

本节属于**阶段IV：决定**，接续[§6 论坛程序](#6-forum-process)（**阶段III：审查**）。本节规定论坛作出的结果。[§7.1 上线门槛](#71-go-live-gate)说明上线门槛，[§7.2 认证缺陷与纠正](#72-certification-defects-and-correction)说明发现缺陷后应采取的措施。

认证决定及作出决定时提出的关切，必须依照[C部分§8.1 最低记录内容](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents)记入记录。结果有以下之一：

- 临时认证；
- 完整认证；
- 有条件认证；
- 延期认证；
- 不予认证；
- 撤回；
- 到期；或
- 解除条件。

既没有临时认证也没有完整认证的系统即为**未获认证**。以下情况均属此列：

- 认证被延期；
- 被拒绝；
- 被撤回；或
- 已到期。

临时认证和完整认证是认证的两种**状态**。[C部分§9.2 临时与完整认证](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification)说明系统如何取得、维持和失去每种状态。有条件认证所附的条件可以适用于任一状态。

<a id="71-go-live-gate"></a>
