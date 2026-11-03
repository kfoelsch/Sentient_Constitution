#### 5.6 可信度与系统依赖完整性评估

<details>
<summary><strong><span style="color: #2563eb;">脉络</span></strong></summary>

- 上游：
  - [Part C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8)（*记录内容*）；
  - [§2](#2-system-class-evaluation)（*系统类别评估*）；监督测量族（*真实与认识完整性；可信度、信任削弱及误导性依赖作为宪法衡量*）；**Article XIII**（*可靠且值得信赖的系统权利*）；
  - [Trustworthiness](core_05.040_band_continuity.md#trustworthiness)、
  - [Trust](core_05.040_band_continuity.md#trust)、
  - [Trust Degradation and Misleading Reliance](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance)、
  - [Contestability](core_05.035_band_accountability.md#contestability)、
  - [Redress and Remediation](core_05.035_band_accountability.md#redress-and-remediation)、
  - [Incentive Alignment](core_05.045_band_integrative.md#incentive-alignment)、
  - [Reversibility](core_05.040_band_continuity.md#reversibility)、
  - [Materiality](core_05.050_band_oversight.md#materiality)、
  - [Dependency](core_05.040_band_continuity.md#dependency)，以及
  - [Risk](core_05.040_band_continuity.md#risk)（第五章）。
- 上游：原则：第一章
  - [§3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)（*适合感知者当前状况、实际可用的质疑和复查渠道；以实际依赖系统的感知者为准判断误导性依赖；将生存关键警报送达未回应者*）、
  - [§4 Safety](core_01.000_values_principles.md#4-safety-harm-constraint)、
  - [§6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)、
  - [§10 Resilience and Self-Healing Design](core_01.000_values_principles.md#10-resilience-and-self-healing-design)，以及
  - [§11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)（*无法避免的依赖；§5.6.2中的升级评估*）。
- 下游：
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)（*按系统类别说明可信度评估的应用示例*）；
  - [Part C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2)（*记录完整性*）；
  - [Part C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3)（*已核验输入门槛*）；
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7)（*虚假信任导致的不一致、反常激励导致的不一致及恢复完整性不一致*）。
- 配合阅读：**Article XIII-A**（*可靠性与可信度基线*）、**Article XIII-B**（*获得救济与补救的权利*）和**Article XVI**（*审计、透明度与独立核验*）——质疑权和审计权仍由这些条文管辖；当高自主性系统实质性介入治理或核验路径时，适用**Article XIII-E**（*高自主性系统与工具中介流程完整性*）；继续依赖系统会影响生存必需品获取时，适用**Article III-A**（*生存*）；系统提供、列出、推荐或建议可能影响身体、健康或安全的产品或服务时，适用**Article III-F**（*安全产品与健康信息*）；每位依赖健康与安全信息的感知者都必须能够使用这些信息时，适用**Article VI-D**（*无障碍*）；以及[Chapter One §6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) (1.000 §6)和[Chapter One §5 Truth](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint) (1.000 §5)。
- 运营术语：[CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information)（*参与：披露充分性与可观察性条款*）适用于产品和服务的健康与安全信息，以及评级、排名和付费推广；[CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices)（*问责：结构审查、纠正时效与披露条款*）适用于伤害报告和纠正通知。
- 子节：
  - [§5.6.1](#561-evaluation-requirement)（*评估要求*）；
  - [§5.6.2](#562-system-class-scaling-and-escalation)（*系统类别分级与升级*）；
  - [§5.6.3](#563-defects-and-misalignment)（*缺陷与不一致*）；
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)（*按系统类别说明可信度评估的应用示例*）。

</details>

<br>

*用直白的话说：系统对感知者是否信任其言行——以及信任失效时能否提出异议——具有实质影响时，认证必须检查这种依赖是否确有依据、是否如实披露、是否能够补救。可靠性指标和测试套件设计由其他文件规定；认证要核验在触发条件适用时，可信度、虚假信任风险和质疑渠道是否确实经过评估。示例：[CS-9.320 §11 Illustrative trustworthiness application by system class](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class)。*

如果重大系统影响感知者对它的依赖事项，本节便适用：系统的功能、限制、可能发生的故障、如何提出质疑，以及如何修复问题。这可能通过以下方面发生：

- 对系统可靠性的主张；
- 系统披露或不披露的内容；
- 系统的实际运行方式；
- 系统内置的激励；
- 系统从故障中恢复的方式；或
- 感知者依赖系统的任何类似方式。

在实质性触发条件适用时，系统对齐认证必须依据以下内容评估**可信度与系统依赖完整性**：

- **Article XIII**（*可靠且值得信赖的系统权利*）；
- [Trustworthiness](core_05.040_band_continuity.md#trustworthiness)；以及
- [Trust Degradation and Misleading Reliance](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance)。

<a id="561-evaluation-requirement"></a>
##### 5.6.1 评估要求

认证流程必须依据**Article XIII-A**（*可靠性与可信度基线*），检查感知者是否有充分理由[信任](core_05.040_band_continuity.md#trust)该系统，以及能否准确地依赖它。

评估还必须检验：

- 感知者能否真正质疑系统、要求复核决定并解决问题，而非仅在纸面上具备这些权利。该流程必须适合感知者当前的状况，包括不易回应或难以完成漫长流程的感知者（[Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)；**Article XIII-A**（*可靠性与可信度基线*）和**Article XIII-B**（*获得救济与补救的权利*））；
- 感知者是否可能被误导，以超过系统应得程度的信任或依赖它，无论是因为系统尚未赢得信任，还是因为它未披露自身限制。判断时以真正使用该系统的感知者为准，而非以一般感知者为准（**Article XIII-C**（*禁止虚假信任与误导性依赖*））；
- 系统提供的、涉及可能影响健康或安全的产品与服务的信息是否准确、足够完整、可据以行动，并且需要该信息的感知者能够轻易找到和理解。范围包括安全警告、健康主张、营养成分、配料和过敏原信息。还包括明确说明哪些事项未知或未经测试，而非留下看似表示「安全」的空白（**Article III-F**（*安全产品与健康信息*）；系统层面的引入条款为**Article XIII-A**（*可靠性与可信度基线*）和**Article XIII-C**（*禁止虚假信任与误导性依赖*））；
- 不同感官、认知和语言需求的感知者能否使用安全与健康信息，并能否在作出决定时及时收到信息，而不是让信息埋在小字中或只提供一种格式（**Article III-F**（*安全产品与健康信息*）；**Article VI-D**（*无障碍*）；[Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)）；
- 信息后来证实错误或产品后来证实不安全时，所有曾依赖该信息的对象是否都能在与伤害紧迫程度相对应的通知期限内（NU-1至NU-3）收到通知，并在其所在之处联系到；以及不安全产品或错误信息是否在对应紧迫程度的遏制和纠正期限内（CU-1至CU-4）于所有出现之处得到遏制和纠正（[Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)；**Article XIII-B**（*获得救济与补救的权利*））；
- 系统内置的奖励是否鼓励欺骗或走捷径（**Article XIII-D**（*激励协调约束*））；以及
- 在相关情况下，系统能否诚实地从故障中恢复，不隐瞒故障，也不暗中剥夺任何人的权利（**Article XIII-F**（*韧性与自我修复基线*））。

检验深度按[Materiality](core_05.050_band_oversight.md#materiality)、[Dependency](core_05.040_band_continuity.md#dependency)和[Risk](core_05.040_band_continuity.md#risk)调整。

评估必须反映跨时间、规模和依赖关系的实际功能影响，而不能依据：

- 声誉、规模或营销宣传；
- 名义上的保障标签；
- 以敷衍段落谈可信度，但实际决定人员配置或采购的是可靠性徽章或供应商评分；
- 宣称的意图；或
- 仅凭过往表现。

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 系统类别分级与升级

审查深度取决于系统类别。每当实质性触发条件满足时：

- 若系统的读数、警报或恢复主张可能使家庭或运营者对生存必需品（感知者赖以生活的事项）产生误解，记录必须提供有力证据，而不能只声称系统可靠，因为依赖必须由系统的实际行为赢得（[Chapter One §6 Trust](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)）。证据必须证明：
  - 感知者能够信任系统；
  - 感知者不会受到虚假的安心保证；
  - 生存关键警报和建议会送达未确认收到的感知者；无人回应时还会跟进，符合[Chapter One §3.1.5 Present Capability and Proactive Help](core_01.000_values_principles.md#315-present-capability-and-proactive-help)的要求；以及
  - 系统会依照[Chapter One §10 Resilience and Self-Healing Design](core_01.000_values_principles.md#10-resilience-and-self-healing-design)的要求，诚实地从故障中恢复。
- 若系统有关运行时间、匹配或紧急覆盖（「破窗」访问）的主张，会影响感知者能否获得临床护理或紧急服务（这是[Chapter One §4 Safety](core_01.000_values_principles.md#4-safety-harm-constraint)涵盖的风险），记录必须按系统关键程度详细说明：
  - 感知者如何质疑这些主张；以及
  - 感知者是否可能因此被误导而依赖系统。
- 当协调对生存至关重要时，认证必须依照[§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation)升级审查并重新考虑系统类别。如果误导性依赖可能切断感知者赖以生存的协调渠道，系统类别可因此提高至**Class A**。感知者实际上无法摆脱的依赖，正是[Chapter One §11.4 Resource and Dependency Concentration](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable)所指的依赖集中。

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 缺陷与不一致

[§5](#5-rights-floor-and-domain-evaluations)（*权利底线与领域评估*）中的缺陷适用于本评估，包括在**Article XIII**（*可靠且值得信赖的系统权利*）要求审查时，对实质限制、风险或故障历史的审查。此外，下列每一项都必须视为认证缺陷：

- 没有可评估的[Trustworthiness](core_05.040_band_continuity.md#trustworthiness)分析，却把声誉、背书、规模或运营方自报视为充分依据；
- 依据**Article III-F**（*安全产品与健康信息*），没有警告或字段留空时，应明确说明情况未知或未经测试，而不能将其视为产品或服务安全的证明；以及
- 未满足**Article XIII**（*可靠且值得信赖的系统权利*）关于可靠性和**Article XIII-A**（*可靠性与可信度基线*）关于质疑机制的约束，却以效率、创新或安全为说辞，削弱披露、可质疑性或救济权。

记录在案的虚假信任、反常激励、不可及的质疑路径，以及隐瞒故障的恢复做法，均依照[Chapter One §6 Trust and Trustworthiness](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)计入。

<br>

*继续阅读评议所流程与结果：*[Chapter Nine, Part B — Forum Process and Outcomes](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes)（[§6 Forum Process](core_09.005_system_alignment_certification_record_process.md#6-forum-process)和[§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)）。*然后阅读记录、再认证与轨迹衔接：*[Chapter Nine, Part C — Record, Recertification, and Standing](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing)（[§8 System Certification Record](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record)至[§11 Relationship to Standing](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing)）。

*各评估领域的示例：*[CS-9.320 System alignment certification illustrations](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations)。
