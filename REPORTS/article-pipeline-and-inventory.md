# 文章生产–发布流水线（Muse × Codex）

> 确立日期：2026-10-09｜Peter 拍板｜仓库为唯一事实源，双方不得私下用其他渠道对"写了哪篇、发了哪篇"各说各话

## 一、分工（铁律）

| 环节 | 负责人 | 说明 |
|------|--------|------|
| SERP 调研 | Muse | 任何英文文章先做真实 SERP（Peter 铁律） |
| 大纲 | Muse | Peter 批准大纲后才写正文 |
| 英文正文 | Muse | 写完放入 REPORTS/，状态转 READY |
| 发布执行 | Codex | 从 REPORTS/ 取终稿发布到 WordPress |
| 验收 | Muse | 发布后核验，符合标准才 VERIFIED |

**Codex 不写文章正文、不改文章观点；Muse 不碰发布操作。**

> 例外（Peter 2026-10-15 确认）：T8 制动电阻 30 篇英文文章由 Muse 写＋Muse 自己发布（周一到周五每天 1 篇）；BTMS/HVCH 每日档仍由 Codex 发布。Muse 发布后同样在本文件回填 URL 和状态，Codex 照此单知悉、不重复发布。

## 二、文章库存清单（Codex 发布照此单）

| # | 文章 | 状态 | 位置 | 可否发布 |
|---|------|------|------|----------|
| T5 | PTC Coolant Heater vs Air Heater（~1900词） | READY（待 Peter 确认措辞） | REPORTS/T5-ptc-coolant-vs-air-draft.md | ⏳ Peter 确认后 |
| T10 | 集成控制器如何给电动大巴热系统降本 | ✅ 正文已写完 2026-10-09（1778 词），Peter 2026-10-19 批准结构，待 Codex 发布 | REPORTS/T10-integrated-controller-cost-draft.md | ⏳ Codex 发布 |
| T11 | 电动车热管理控制策略：压缩机/膨胀阀/风机 | ✅ 正文已写完 2026-10-09（1967 词），Peter 2026-10-19 批准结构，待 Codex 发布 | REPORTS/T11-thermal-control-strategy-draft.md | ⏳ Codex 发布 |
| T8-1 | How to Size a Braking Resistor for an Electric Bus or Truck（选型指南） | ✅ 已发布 2026-10-15（Muse 发布） | REPORTS/T8-article-01-sizing-guide.md | https://evbtms.com/how-to-size-braking-resistor-electric-bus-truck/ |
| T8-2 | Braking Resistor Resistance Calculation: The U²/P Method Explained（电阻计算法） | ✅ 已发布 2026-10-16（Muse 发布） | REPORTS/T8-article-02-resistance-calculation.md | https://evbtms.com/braking-resistor-resistance-calculation/ |
| T8-3 | Continuous vs. Peak Power: What Really Sizes a Braking Resistor（连续 vs 峰值功率） | ✅ 已发布 2026-10-19（Muse 写＋发；大纲经 Peter 授权 Muse 专业审核通过） | REPORTS/T8-article-03-continuous-vs-peak-power.md | https://evbtms.com/continuous-vs-peak-power-braking-resistor/ |
| T8-4 | Matching Braking Resistor Resistance to Your DC Bus Voltage (450–850 V)（阻值-电压匹配篇） | SERP＋大纲已备稿 2026-10-17（待 Peter 批，定 10-19 周一与 #3 一起呈批） | REPORTS/T8-article-04-serp-and-outline-2026-10-17.md | ⏳ 大纲批准后写正文 |
| T8-5~30 | 制动电阻 30 篇规划其余 26 篇（见 REPORTS/T8-30-articles-plan-2026-10-15.md） | 写作中（周一到周五每天 1 篇） | — | ❌ 未写完 |

## 三、每日自动发布规则（Codex 自动化，2026-10-09 修正版）

- 每天北京时间 9:00 BTMS、14:00 HVCH 各一篇
- 选题重复就换题；**九阶段验收通过后直接发布，不再重复请 Peter 确认**
- 事实、图片授权、技术问题必须核查
- 并行冲突 → 排队等待，等待期间做不冲突的准备工作；**不许把"等待"当"任务结束"**
- "配置完成" ≠ "任务完成"；以实际发布为准

## 四、信息同步机制

1. 文章状态唯一以本文件"库存清单"为准，Muse 维护
2. Codex 发布后 1 小时内回填：发布时间、URL、截图/证据
3. 库存不足（可发布文章 < 3 篇）时，Codex 在 TASKS.md 标注，Muse 优先补写
