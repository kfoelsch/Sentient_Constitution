# Chapter Five definition batch 06 — Certification Condition (zh)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Certification Condition; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 认证条件

<details>
<summary><strong>追溯</strong></summary>
- 规范归属：[第九章B部分§7.1 上线门槛](core_09.005_system_alignment_certification_record_process.md#71-go-live-gate)；并参阅[§7.4 拒绝与撤销](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation)。
- 集群组成部分：无。
- 并读：[临时认证](core_05.040_band_continuity.md#provisional-certification)、[完整认证](core_05.040_band_continuity.md#full-certification)、[系统认证记录](core_05.040_band_continuity.md#system-certification-record)。
</details>

*简言之，**认证条件**是写入认证结果、要求运营方满足或持续满足的要求。有些须在上线前满足，有些须在系统获准运行期间一直满足，还有一些是在限定范围内获授权后允许开展的纠正工作。*

- **含义**
  - **范围内：**认证结果中要求运营方在上线前、获准运行期间或获授权的限定范围内开展纠正工作时满足的要求。
  - **范围外：**
    - [依赖限制](core_05.040_band_continuity.md#reliance-limits)，规定他人可依赖的程度，不是运营方要满足的要求；
    - [暂停令](core_05.035_band_accountability.md#stay)，推迟或阻止某项行动或结果；或
    - 对结果没有影响的建议。
    这些事项各有归属条目。
  - **依赖项：**[临时认证](core_05.040_band_continuity.md#provisional-certification)、[完整认证](core_05.040_band_continuity.md#full-certification)、[系统认证记录](core_05.040_band_continuity.md#system-certification-record)。
  - 三类条件、每项条件须列明的内容以及上线前核验见[第九章B部分§7.1 上线门槛](core_09.005_system_alignment_certification_record_process.md#71-go-live-gate)。两次未满足或实质性违反条件的后果见[§7.4 拒绝与撤销](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation)。本条目仅说明第五章中的含义。
<a id="certification-condition-a"></a>
- **测量与评估**
  - **主要测量：**[连续性测量组](core_05.010_apex_continuity_aim.md#measuring-continuity-preamble-measurement-family)——*感知者和系统能否在生态上、可靠地并跨越故障持续存在？*

    **主要评估：**
    1. 认证结果是否为每项条件列出责任人、证据和独立核验；
    2. 是否存在上线前条件尚未核验却已运行的范围。
<a id="certification-condition-c"></a>
- **必须满足**
  - **主要失败：**
    - 条件缺少负责人、证据或后果；或
    - 上线前条件未核验就允许运行。
