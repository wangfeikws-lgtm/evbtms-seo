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
| T5 | PTC Coolant Heater vs Air Heater（PTC 水暖 vs 风暖对比） | ✅ 已更新 2026-10-19（内容升级到旧文章 https://evbtms.com/ptc-coolant-heater-vs-air-heater/，Peter 已批准） | REPORTS/T5-ptc-coolant-vs-air-draft.md | https://evbtms.com/ptc-coolant-heater-vs-air-heater/ |
| T10 | 集成控制器如何给电动大巴热系统降本 | ✅ 已发布 2026-10-10（post 9949）https://evbtms.com/integrated-thermal-management-controller-cost/ | REPORTS/T10-integrated-controller-cost-draft.md | ✅ 完成 |
| T11 | 电动车热管理控制策略：压缩机/膨胀阀/风机 | ✅ 已发布 2026-10-10（post 9951）https://evbtms.com/ev-thermal-management-control-strategy/ | REPORTS/T11-thermal-control-strategy-draft.md | ✅ 完成 |
| T8-1 | How to Size a Braking Resistor for an Electric Bus or Truck（选型指南） | ✅ 已发布 2026-10-15（Muse 发布） | REPORTS/T8-article-01-sizing-guide.md | https://evbtms.com/how-to-size-braking-resistor-electric-bus-truck/ |
| T8-2 | Braking Resistor Resistance Calculation: The U²/P Method Explained（电阻计算法） | ✅ 已发布 2026-10-16（Muse 发布） | REPORTS/T8-article-02-resistance-calculation.md | https://evbtms.com/braking-resistor-resistance-calculation/ |
| T8-3 | Continuous vs. Peak Power: What Really Sizes a Braking Resistor（连续 vs 峰值功率） | ✅ 已发布 2026-10-19（Muse 写＋发；大纲经 Peter 授权 Muse 专业审核通过） | REPORTS/T8-article-03-continuous-vs-peak-power.md | https://evbtms.com/continuous-vs-peak-power-braking-resistor/ |
| T8-4 | Matching Braking Resistor Resistance to Your DC Bus Voltage (450–850 V)（阻值-电压匹配篇） | ✅ 已发布 2026-10-19（Muse 写＋发；Peter 2026-10-19 批准） | REPORTS/T8-article-04-resistance-voltage-matching.md | https://evbtms.com/matching-braking-resistor-resistance-dc-bus-voltage/ |
| T8-5 | How Duty Cycle Determines Braking Resistor Size（占空比决定选型） | ✅ 已发布 2026-10-20（Muse 写＋发；Peter 2026-10-20 批准大纲） | REPORTS/T8-article-05-duty-cycle-sizing.md | https://evbtms.com/duty-cycle-braking-resistor-sizing/ |
| T8-6 | Sizing Mistakes That Kill Braking Resistors（选型错误清单） | ✅ 已发布 2026-10-22（Peter 定稿，Muse 代发 post 10189；前台核验通过） | REPORTS/T8-article-06-peter-version-2026-10-22.md | https://evbtms.com/braking-resistor-sizing-mistakes/ |
| T8-7 | How Braking Resistors Work in Electric Vehicles（制动电阻工作原理） | ✅ 已发布 2026-10-22（Peter 发布版，Muse 代发 post 10168；ZeroGPT 16.6%；GSC 索引已请求 2026-10-22） | REPORTS/T8-article-07-how-braking-resistors-work.md | https://evbtms.com/how-braking-resistors-work-electric-vehicles/ |
| T8-8 | What Is a Brake Chopper? Resistor + Chopper Architectures Explained（制动斩波器与三架构） | ⏸ 搁置：五版 ZeroGPT 均未过线（v1 38%｜v2 32.9%｜v3 39.5%｜v4 43.2%｜v5 34.2%，2026-10-23 v5 复测）；日后换故障诊断切入点重写 | REPORTS/T8-article-08-brake-chopper-v5.md | ❌ 未发布 |
| T8-9 | Where Does Regenerative Braking Energy Go When the Battery Is Full?（电池满了再生制动能量去哪；发布标题用 Peter 问句版） | ✅ 已发布（2026-10-23）：发布版为 Peter 改定稿，ZeroGPT 17.5% ✅ 过线，Muse 按其逐篇授权代发 | REPORTS/T8-article-09-regen-energy-battery-full.md | https://evbtms.com/regen-braking-energy-battery-full/（post 10251，2026-10-23）|
| T8-10~30 | 制动电阻 30 篇规划其余 21 篇（见 REPORTS/T8-30-articles-plan-2026-10-15.md） | 写作中（周一到周五每天 1 篇） | — | ❌ 未写完 |
| DAILY-1029 | EV Coolant Is Not Engine Antifreeze: What to Specify for Battery Thermal Loops（每日档合并：DAILY-1028 补交＋DAILY-1029 今日档） | ✅ 已发布 2026-10-29（Peter 修订版，Muse 按其逐篇授权代发 post 10353；ZeroGPT 22.8%） | REPORTS/DAILY-1029-merged-ev-coolant-peter-version-2026-10-29.md | https://evbtms.com/ev-coolant-battery-thermal-loops/ |
| HVCH-1023 | Full Power on a Mild Day: Why Your HVCH Needs Modulated Output（HVCH 1023档） | ✅ 已发布 2026-10-29（Peter 修订版，Muse 按其逐篇授权代发 post 10356；Peter 审过版不检测） | REPORTS/HVCH-1023-modulated-output-peter-version-2026-10-29.md | https://evbtms.com/hvch-modulated-output-mild-days/ |
| HVCH-1022v2 | HVCH Not Starting? Check Low-Voltage Supply and Wake-Up（1022 HVCH v2返工稿） | ✅ 已发布 2026-10-29（Peter 修订版，Muse 按其逐篇授权代发 post 10357；Peter 审过版不检测） | REPORTS/HVCH-1022v2-not-starting-peter-version-2026-10-29.md | https://evbtms.com/hvch-not-starting-low-voltage-wake-up/ |
| BTMS-1022v2 | Reading a BTMS Quotation: Five Lines That Decide Whether the Unit Fits Your Vehicle（1022 BTMS v2返工稿） | ✅ 已发布 2026-10-29（Peter 修订版，Muse 按其逐篇授权代发 post 10362；Peter 审过版不检测） | REPORTS/BTMS-1022v2-quotation-audit-peter-version-2026-10-29.md | https://evbtms.com/btms-quotation-five-lines-fit/ |
| BTMS-1023 | Will Your Bus Leave the Depot Warm? Specifying BTMS Preconditioning Before Winter（BTMS 1023档，德语版） | ✅ 已发布 2026-10-29（Peter 德语修订版，Muse 按其逐篇授权代发 post 10367；Peter 审过版不检测） | REPORTS/BTMS-1023-preconditioning-peter-german-version-2026-10-29.md | https://evbtms.com/electric-bus-btms-preconditioning-depot/ |

## 三、每日自动发布规则（Codex 自动化，2026-10-09 修正版）

- 每天北京时间 9:00 BTMS、14:00 HVCH 各一篇
- 选题重复就换题；**九阶段验收通过后直接发布，不再重复请 Peter 确认**
- 事实、图片授权、技术问题必须核查
- 并行冲突 → 排队等待，等待期间做不冲突的准备工作；**不许把"等待"当"任务结束"**
- "配置完成" ≠ "任务完成"；以实际发布为准

| T12-W1-1 | How to Choose a High-Voltage PTC Coolant Heater: 7 Inputs OEMs Must Define（老站选型篇） | ✅ 已发布 2026-10-20 正式站（ECER 422912） | — | https://www.evptc.com/news/how-to-choose-a-high-voltage-ptc-coolant-heater-7-inputs-oems-must-define-422912.html |
| T12-W1-2 | CAN-Controlled vs Thermostat-Controlled HVCH: Which Architecture Fits Your Vehicle?（老站架构对比篇） | ✅ 已发布 2026-10-20 正式站（ECER 422917） | — | https://www.evptc.com/news/can-controlled-vs-thermostat-controlled-hvch-which-architecture-fits-your-vehicle-422917.html |
| T12-W1-3 | Electric Bus Battery Preheating at −30°C: Five Planning Mistakes（老站预热篇） | ✅ 已发布 2026-10-20 正式站（ECER 422919） | — | https://www.evptc.com/news/electric-bus-battery-preheating-at-30c-five-planning-mistakes-422919.html |
| T12-W1-4 | PTC Coolant Heater vs Heat Pump for Commercial EVs: Where Each System Wins（老站对比篇） | ✅ 已发布 2026-10-20 正式站（ECER 422921） | — | https://www.evptc.com/news/ptc-coolant-heater-vs-heat-pump-for-commercial-evs-where-each-system-wins-422921.html |
| T12-W1-5 | Why Electric Bus Range Falls in Winter—and Five Levers Fleets Can Control（老站冬季续航篇） | ✅ 已发布 2026-10-20 正式站（ECER 422923） | — | https://www.evptc.com/news/why-electric-bus-range-falls-in-winter-and-five-levers-fleets-can-control-422923.html |
| T12-W2-01 | 15 kW vs 35 kW: Sizing Your HVCH for Heavy-Duty Trucks（15/35kW 选型） | 最终版已过检（ZeroGPT 22.6%），待 Peter 审发 | REPORTS/T12-W2-01-15kw-vs-35kw-hvch-sizing-heavy-duty-trucks-publish-package-v2.md | 未发布（老站 evptc.com） |
| T12-W2-02 | IP67 and EMC in High-Voltage Heaters: What the Spec Sheet Doesn't Tell You（IP67 与 EMC 盲区） | 最终版已过检（27.2%），待 Peter 审发 | REPORTS/T12-W2-02-ip67-emc-high-voltage-heaters-publish-package-v2.md | 未发布 |
| T12-W2-03 | Hydrogen Fuel Cell Bus Heating: Why 20 kW PTC Became the Standard Answer（氢燃料客车加热） | 最终版已过检（v3，24.1%），待 Peter 审发 | REPORTS/T12-W2-03-hydrogen-fuel-cell-bus-heating-20kw-ptc-publish-package-v3.md | 未发布 |
| T12-W2-04 | Air Heater vs Coolant Heater for EV Cabins: A Total Cost Comparison（风暖 vs 液暖总成本） | 最终版已过检（13.7%），待 Peter 审发 | REPORTS/T12-W2-04-air-heater-vs-coolant-heater-total-cost-publish-package-v2.md | 未发布 |
| T12-W2-05 | Battery-Swapping Heavy Trucks Need Thermal Management Too（换电重卡热管理） | 最终版已过检（3.5%），待 Peter 审发 | REPORTS/T12-W2-05-battery-swapping-heavy-trucks-thermal-management-publish-package-v2.md | 未发布 |

## 四、信息同步机制

1. 文章状态唯一以本文件"库存清单"为准，Muse 维护
2. Codex 发布后 1 小时内回填：发布时间、URL、截图/证据
3. 库存不足（可发布文章 < 3 篇）时，Codex 在 TASKS.md 标注，Muse 优先补写
