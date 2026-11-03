##### 3.4.2 隐私纪律

认证必须依照以下隐私纪律审查数据处理：

- *Types H、I、N、S和Y。* 对于**Type H**、**Type I**、**Type N**、**Type S**和**Type Y**数据，认证必须核验处理方式符合各类型在**CS-6.305（*信息类型与处理*）和CS-6.310**（*数据分类*）中指定的[隐私归属](corpus_systems/cs_06.310_data_classifications.md#privacy-link)，包括[必要性](core_05.035_band_accountability.md#necessity)、[比例性](core_05.035_band_accountability.md#proportionality)、最小化处理，以及同意或其他充分授权。
- *共同触发。* 若涉及多个隐私领域，[§4.1 Privacy (Informational) Joint Invocation](#41-privacy-informational-joint-invocation)也适用。
- *标签并不足够。* 类型标签正确，本身并不能证明符合隐私要求。
- *Types W、U和T。* 对于**Type W**、**Type U**和**Type T**作品，认证必须核验创作者的控制权受到尊重，包括：
  - 依据[CS-6.310 Part B §9.9](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published)（*Type W：已发布作品*）撤回公开发布；
  - 依据[CS-6.310 Part B §9.13](corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants)（*商业授权*）遵守每项已记录授权的限制；以及
  - 创作者的[保留权利](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)。
- *不得推定同意。* 授权仅涵盖其明确列出的用途，并限于所述范围、期限、地域和媒介。未列出的事项仍由创作者保留。认证不得把默认设置、捆绑条款、沉默或范围更广的授权，视为同意该授权未列明的用途。例如，允许发布或销售作品的一般许可，并不等于同意将其用作训练数据；这需要创作者本人作出明确同意（见[保留权利](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)）。

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 保护性存储与密钥保管

对于默认限制访问和不可访问类别中的数据，认证必须核验系统符合[CS-6.305 Part A §5.0 Access-posture bands](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands)规定的保护性存储与密钥保管最低要求。记录必须显示：

- 受限数据及其密钥实际存放的位置，包括备份、缓存、日志和交换空间；
- 明文仅限于确实需要它的进程；以及
- 审计、导出和合法覆盖路径仍然有效。

没有这些证据，仅声称已加密并不能满足此要求。

<a id="344-scheduled-data-type-re-evaluation"></a>
<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 定期重新评估数据类型

每次认证或再认证具有实质影响的系统时，审查都必须核验其重要数据集是否：

- 依据**[CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)**（*重新分类与生命周期治理*）及**CJS-5.130 §18**（*数据保留与生命周期完整性条款*），为确认分类是否恰当而**重新评估**；并且
- 在该次审查要求时已**重新分类**。

依据CS-6.305（*信息类型与处理*）和CS-6.310（*数据分类*）进行的事件触发式重新定类，不能取代这项定期认证核验。

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 按系统类别调整的基础设施保障

依据[§2.2 How system class scales every evaluation](#22-how-system-class-scales-every-evaluation)、CS-9.305（*系统分类机制*）和CS-9.310（*系统影响分类*），类别较高的系统必须提供相应更有力的证据，证明处理、存储、运算、传输、备份、恢复和监测基础设施能在压力下保持：

- 分类完整性；
- 归属可追溯性；以及
- 可质疑性。

若适用CS-6.305（*信息类型与处理*）和CS-6.310（*数据分类*）规定的公共利益可见性默认要求，认证必须核验限制措施：

- 范围严格限定；
- 有记录且可审计；并且
- 附有合理可行范围内最充分的公开替代信息（例如摘要、汇总数据、去标识化版本、延迟发布或限定资格的审计访问），以说明为何扣留信息，而非简单地将其隐藏。

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 数据基础设施稳健性

认证必须评估数据处理基础设施是否适合相关数据类型及系统类别。基础设施包括：

- 持久化层和数据流程管道；
- 访问控制；
- 加密或隔离边界；
- 备份与恢复路径；以及
- 运营方或供应商的委托链条。

生命周期完整性、对抗韧性、可移植性或可恢复性方面的重大缺口，必须记入记录，并反映在认证结果、认证条件或依赖限制中。

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 缺陷与不一致

下列每一项都必须视为认证缺陷：

- 数据分类错误；
- 规避性重组；
- 不安全的跨领域关联；
- 处理时虽使用正确类型标签，却仍破坏该类型要求的隐私保护；
- 未记录谁曾访问、处理或更改数据，以致无法调查重大伤害；
- **定期数据类型重新评估逾期或被跳过**；
- 受限数据以明文存储，或超出获准处理边界；或者密钥可被不需要它的进程访问；以及
- 基础设施脆弱，足以预见会破坏CS-6.305（*信息类型与处理*）和CS-6.310（*数据分类*）规定的保护。

这些缺陷的后果见[§7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)。

<a id="4-evaluations-where-implicated"></a>
