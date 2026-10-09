# SERP 简报：三合一控制器 T1–T4

> 铁律执行：英文落地页动笔前先完成本简报。由 Muse 负责。
> 调研日期：2026-10-09 ｜ 搜索环境：google.com / 英文 / 无痕 ｜ 对应 KEYWORDS.md 品类二 T1–T4

## 0. 核心发现（先看这个）

**"three-in-one" 在英文 EV 语境里有两个完全不同的意思，SERP 无法自动区分：**
- (a) **电驱三合一**：电机 + 电机控制器 + 减速器（如 accio.com 的 FAQ 所说 "combines the electric motor, motor controller, and reducer"）
- (b) **电源三合一**：OBC + DC/DC + PDU（如 DPC 3-in-1 Power Control Unit）

**这是本品类的最大风险点**：如果产品是 (b) 却按 (a) 的词去打（或反之），流量全是错的。

**2026-10-09 更新（已确认）**：Peter 提供了产品实物图（EVLINK 鳍片散热壳体 + 高低压接插件），并经法莱奥对标确认为 **(b) OBC + DC/DC + PDU 电源三合一**。
法莱奥官方叫法：
- "3-in-1 bi-directional Combo power electronics"（Mahindra 订单官方口径）
- "On Board Power Supply 3-in-1 combo unit"（Pune 工厂口径）
- 官网产品页标题："High Voltage On-Board Charger & DCDC converter Combo"
- 行业报告通用名："OBC+DC/DC+PDU Three-in-One On-board Charger"
- 对 EVLINK 的英文命名建议：**3-in-1 Onboard Power Supply (OBC + DC/DC + PDU)** ——不要用 "Three-in-One Controller" 做主名，英文里 controller 易被误解为电机控制器。

T1/T3/T4 维持放弃/换词；T2 转为 GO（等真实规格）。

---

## T1 — three in one controller electric vehicle（产品分类页主词）

### 1. 能不能排
- Top 10 类型：AI 采电源内容站（accio.com #1）、专利站（patsnap ×2）、Amazon e-bike 配件（×2，无关）、B2B 目录（mfrbee）、LinkedIn 行业文章（X-TEAM，讲的是无人机/机器人三合一，无关）
- 低权重网站进前 10：有（mfrbee 目录页）
- 结论：**不可直接打**。意图混乱（a/b 两种三合一 + e-bike 噪音），即使排上去，来的流量一半是错的。

### 2. 搜索意图与页面类型
- 意图：混合（信息 + 商业调查），Google 自己都没统一
- 倾向页面类型：无明显倾向，产品页/专利/文章混杂

### 3. SERP 特征
- AI Overview：本轮未观察到稳定触发
- 应对：不打此词，无需应对

### 9. Go / No-Go
- **决策：不写，换词**
- 换成：产品若是 (b) 电源三合一 → 用 T2 精确词；若是 (a) 电驱三合一 → 需另起一组词（如 "3 in 1 e-axle" / "integrated electric drive unit"）重新调研

---

## T2 — 3 in 1 EV controller OBC DC DC（落地页）⭐ 本组唯一可打

### 1. 能不能排
- Top 结果：
  1. m.weycablesupply.com — 厂商独立站产品页（DPC 3-in-1 Power Control Unit，含完整规格表：DCDC 200~450VDC / OBC 90~265VAC / IP67 / 液冷）
  2–6. made-in-china.com Landworld 供应商页面（3.3kW/6.6kW/11kW OBC+DC/DC 组合）
  7. worldbid.com B2B listing（Rawsuns PDU+OBC+DCDC）
- 低权重网站进前 10：有（weycablesupply、worldbid 均为中小厂商站/目录）
- 结论：**可打**。Google 接受厂商独立站产品页排第一（weycablesupply 就是例证）；made-in-china 主导说明采购意向强，独立站产品页 + 规格表有差异化空间。

### 2. 搜索意图与页面类型
- 意图：**商业调查 / 交易**（找供应商、比规格）
- Google 倾向：产品页（供应商产品页、规格参数页）

### 3. SERP 特征
- AI Overview：本轮未观察到
- 精选摘要/视频：无明显特征
- 应对：页面必须有结构化规格表（对手 Landworld 全是参数表，这是入场券）

### 4. 竞争对手内容（Top 5）
| 排名 | URL | 页面类型 | 结构摘要 | 备注 |
|------|-----|----------|----------|------|
| 1 | m.weycablesupply.com/products/three-in-one-onboard-power-supply-dc-dc-obc-pdu-for/ | 厂商产品页 | Features + 完整参数表（DCDC/OBC/PDU 三表）+ 详细照片 | 最直接的对标对象 |
| 2–6 | landworld.en.made-in-china.com 系列 | 平台供应商页 | Features + 参数表 + 询盘按钮 | 平台站，内容同质化 |
| 7 | worldbid.com …/pdu-obc-dcdc…i327389.html | B2B listing | 基础参数 + 联系方式 | 薄 |

### 5. 内容缺口
- 对手没回答的问题：三合一 vs 分体方案的选型逻辑（什么时候该集成、什么时候分开更合适）；不同电压平台（400V/800V）的匹配；真实装车案例
- 薄弱点：made-in-china 页面全是参数堆砌、无应用场景；weycablesupply 有参数但无选型指南、无案例

### 6. PAA 问题清单
- 本轮 SERP 未抓到稳定 PAA；建议页面 FAQ 覆盖：What is 3 in 1 OBC? / OBC vs DC/DC vs PDU 区别 / 如何选三合一电源功率 / IP67 是否必要

### 7. 我方独特资产映射
- ⚠️ 待 Peter 提供：真实规格（OBC 功率、DC/DC 功率、电压范围、冷却方式、IP 等级、认证）；是否有装车案例
- 差异化点（规划）：选型指南（集成 vs 分体）、800V 平台视角、与 PTC/制动电阻的系统搭配（站内独有）

### 8. 内链规划
- 落地页 URL（建议）：`/products/three-in-one-controller/`
- 支撑文章：后续可配一篇 "OBC vs DC/DC vs PDU: What Does 3-in-1 Integration Mean for EVs" 反链回落地页

### 9. Go / No-Go
- **决策：GO（2026-10-09 产品类型已确认，等真实规格）**
- 条件：Peter 提供真实规格（OBC 功率、DC/DC 功率、电压范围、冷却方式、IP 等级、认证）
- 拟定 H1：3-in-1 Onboard Power Supply (OBC + DC/DC + PDU) for Electric Vehicles | EVLINK
- 大纲（H2）：What Is a 3-in-1 Controller / Key Specifications / 3-in-1 vs Discrete: How to Choose / Applications (bus/truck/special vehicles) / FAQ / CTA

---

## T3 — integrated power control unit electric bus（落地页）

### 1. 能不能排
- Top 结果：electrive.com 新闻（MG 电动大巴）、sustainable-bus.com 新闻（Kiepe）、galaxus/digitec 瑞士零售（DALI 调光器，完全无关）、bestcontactor（变电站控制器，无关）、专利、worldbid Rawsuns PDU
- 结论：**放弃**。意图完全分散，新闻 + 无关零售 + 电力设备，没有可承接的商业意图。

### 9. Go / No-Go
- **决策：不写**。如需覆盖电动大巴场景，改用 "PDU for electric bus" 或 "high voltage PDU electric bus" 重新调研。

---

## T4 — three in one controller manufacturer supplier（采购意向页）

### 1. 能不能排
- Top 结果：Amazon e-bike 控制器（×2，无关）、techsparx 充电桩新闻（无关）、LinkedIn 无人机文章（无关）、accio 内容农场、vectorque（V&T 三合一电机控制器供应商页，唯一相关）
- 结论：**放弃此词**。采购意向明确但 SERP 被电商和内容农场占据，独立厂商页挤不进去。

### 9. Go / No-Go
- **决策：不写独立采购页**。采购意向由 T2 落地页承接（页面内加 "Manufacturer & Supplier" 板块 + 询盘 CTA 即可）。

---

## 总结与待决策

| 词 | 决策 | 说明 |
|----|------|------|
| T1 | ❌ 换词 | 意图混乱，(a)/(b) 两种三合一打架 |
| T2 | ⚠️ 有条件 GO | 唯一可打；等产品类型确认 + 真实规格 |
| T3 | ❌ 放弃 | 意图分散，无商业承接 |
| T4 | ❌ 放弃（并入 T2） | 被电商/内容农场占据 |

**需 Peter 决定的事（阻断后续）：**
1. ~~三合一产品到底是哪种集成~~ ✅ 已确认：(b) OBC+DC/DC+PDU（2026-10-09，产品图 + 法莱奥对标）
2. 真实规格清单（功率、电压、冷却、防护、认证、MOQ/交期）——无规格不得写正文、不得建生产页
