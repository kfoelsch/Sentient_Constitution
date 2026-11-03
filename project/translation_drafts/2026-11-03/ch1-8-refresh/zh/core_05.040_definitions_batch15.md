# Chapter Five definition batch 15 — Go-Live (zh)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Go-Live; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 上线运行（Go-Live）

<details>
<summary><strong>溯源</strong></summary>

- 规范归属：第九章B部分§7.1上线门槛。本条位于系统一致性认证主题组旁边但不属于该组。下游：第九章A部分§2.3试点认证。与试点、临时/完整认证、系统认证记录、重大影响、依赖、系统边界及可逆性合读。

</details>

*通俗地说，系统停止仅处于构建或测试状态，开始实际影响感知者或被感知者依赖的时刻。判断看实际运行，而不是发布名称。*

- **What it is**
  - **In scope / out of scope / dependencies:** 范围：系统首次对感知者产生重大影响或被其重大依赖的时点，无论试点还是全面部署。试点、试点后的全面部署，以及超出认证范围/人群/期限的重大扩展，各自构成独立上线。beta、试用、预览、抢先体验、软启动/实验发布等标签、公告日期或内部里程碑均不决定。范围外：无真实影响/依赖的开发、测试、验证、预发布环境或模拟；没有重大影响或依赖的系统；采用文件生效时已在运行的系统（由第二十八-A条的过渡期处理，不视为再次上线）；非重大扩展的常规变化。依赖重大影响和依赖定义。上线门槛、通知期和条件核验见第九章B部分§7.1。本条仅定义第五章含义。
<a id="go-live-a"></a>
- **How to measure and assess**
  - 按实际重大影响/依赖开始日确定日期，不用标签、公告或内部里程碑；确认系统记录允许的最早日期前没有产生实际影响；将试点、全面部署、重大扩展分别视为上线。
<a id="go-live-c"></a>
- **What must hold**
  - **Primary failure:** 主要失败：未过门槛即上线；改称beta/试验以掩盖实际运行；分阶段发布使整体逃过门槛；把重大扩展当作先前上线的延续或事后设定日期。
