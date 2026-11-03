#### 3.3 时间一致性约束

若可预见的中期或长期违规仍未得到处理，认证不得把下列任何一项视为充分依据：

- 近期指标；
- 局部合规；或
- 短期效率。

如果可以合理预见，追求短期成果会在未来损害下列任一事项，即不可接受；即使损害缓慢累积、迟迟才显现，或扩散到不同系统，也一样：

- **安全**；
- **真实**；或
- **福祉**。

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 数据类型与处理评估

<details>
<summary><strong><span style="color: #2563eb;">脉络</span></strong></summary>

- 上游：
  - [§3](#3-whole-system-certification-evaluation)（*全系统评估因素*）；
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class)（*按系统类别说明全系统评估的应用示例*）；
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8)（*记录内容*）；
  - [§2](#2-system-class-evaluation)（*系统类别评估*）；监督测量族（*真实与认识完整性作为宪法衡量*）；
  - [Article XV: Info-Sphere Integrity](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity)；
  - [Article XVI: Audit, Transparency, and Independent Verification](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification)；
  - [Article VII: Self-Ownership](core_06.005_rights_part_b.md#article-vii-self-ownership)。
- 下游：
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class)（*按系统类别说明数据处理的应用示例*）；
  - [§5.1](#51-ecological-footprint-evaluation)以及
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class)（*按系统类别说明生态足迹评估的应用示例*）；
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2)（*记录完整性*）；
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3)（*已核验输入门槛*）；
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7)（*重新分类与处理不一致*）。
- 配合阅读：
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*信息类型与处理*）及[CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**（包括**
  - [CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)**（*重新分类与生命周期治理*），以及**
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)**（*System Data Types Record治理*））；
  - [System Data Types Record](core_05.040_band_continuity.md#system-data-types-record)；
  - [Public Oversight Baseline Disclosure](core_05.050_band_oversight.md#public-oversight-baseline-disclosure)；
  - **CJS-5.130 §18**（*数据保留与生命周期完整性条款*）、
  - **CJS-5.130 §21**（*对抗韧性与滥用防护条款*），以及
  - **CJS-5.130 §17**（*互操作性、可移植性与退出完整性条款*），在具有实质适用性时；
  - 涉及隐私领域时，[§4.1 Privacy (Informational) Joint Invocation](#41-privacy-informational-joint-invocation)。
- 子节：
  - [§3.4.1](#341-type-o-baseline-disclosure)（*Type O基线披露*）；
  - [§3.4.2](#342-privacy-discipline)（*隐私纪律*）；
  - [§3.4.3](#343-protective-storage-and-key-custody)（*保护性存储与密钥保管*）；
  - [§3.4.4](#344-scheduled-data-type-re-evaluation)（*定期重新评估数据类型*）；
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance)（*按系统类别调整的基础设施保证*）；
  - [§3.4.6](#346-infrastructure-robustness-for-data)（*数据基础设施稳健性*）；
  - [§3.4.7](#347-defects-and-misalignment)（*缺陷与不一致*）；
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class)（*按系统类别说明数据处理的应用示例*）。

</details>

<br>

*用直白的话说：认证还必须检查系统接触哪些类型的数据，以及处理方式是否恰当——包括在当前审查周期中数据分类是否仍然正确，以及底层基础设施对于该数据类型和系统类别是否足够稳健。数据类型规则和System Data Types Record位于系统资料库中；认证要核验规则是否确已适用，以及记录是否真实。*

系统对齐认证必须将**数据类型与处理**纳入每份具有实质影响的System Certification Record。本节说明认证必须核验什么。数据类型分类法和处理机制位于**[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling)（*信息类型与处理*）及[CS-6.310 — Data classifications](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**，并包括：

- 信息类型的规范定义；
- 处理规则和隔离要求；
- 生命周期细节；以及
- 持久保存的[System Data Types Record](core_05.040_band_continuity.md#system-data-types-record)。

**评估要求。** 认证流程必须判定系统是否：

- 识别了范围内具有实质意义的数据类型；以及
- 按**所有适用分类中限制最严格的一项**处理这些数据，包括转换、聚合、委托、存储、保留和跨领域关联的全过程。

评估必须反映实际功能影响，而不能只依据标签、格式或流程阶段。

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 Type O基线披露

在适用**[CS-6.305 §7 Type O baseline](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)**时，认证还必须核验已发布的[Public Oversight Baseline Disclosure](core_05.050_band_oversight.md#public-oversight-baseline-disclosure)（**Type O**）涵盖了**认证范围**，且该范围依据下列内容映射确定：

- 管辖该系统的[System Charter](core_05.040_band_continuity.md#system-charter)；
- 已分配的系统类别；以及
- 观察到的[System Boundaries](core_05.040_band_continuity.md#system-boundaries)。

此项覆盖还必须包括依照[§3.1 Governance, Incentive, and Contestability Discipline](#31-governance-incentive-and-contestability-discipline)确立的治理、激励和可质疑性认定及已分配角色。

对每一种系统类别，包括Class L和Class P，认证还必须核验System Certification Record已依据[CS-6.310 Part B §9.3 Type O](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data)作为**Type O**认证数据发布。在Class A、B、C以外发布该记录，并不要求发布完整的Public Oversight Baseline Disclosure。

如果涉及系统性风险，共享已评估的风险信息也可计入这项基线。公众享有的基线权利范围宽于认证本身；它不要求在[System Classification Record](core_05.040_band_continuity.md#system-classification-record)或[System Data Types Record](core_05.040_band_continuity.md#system-data-types-record)旁另建一份记录。

每项有正当理由的暂缓披露，都必须配有在合理可行范围内最充分的公开替代信息（[§3.4.5 System-Class-Scaled Infrastructure Assurance](#345-system-class-scaled-infrastructure-assurance)提供示例）。第五章规定该术语；CS-6.305（*信息类型与处理*）和CS-6.310（*数据分类*）规定基线内容及发布机制。

<a id="342-privacy-discipline"></a>
