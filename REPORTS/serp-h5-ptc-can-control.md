# SERP 验证简报：#5 — PTC coolant heater with CAN control

> 验证日期：2026-10-09｜验证人：Muse｜关键词地图：KEYWORDS.md v2 品类三-A #5
> 决策：**GO**—— 产品落地页（CAN 集成角度），中优先级

## 一、搜索意图判定

产品采购意图，带明确技术限定。搜"带 CAN 控制的 PTC 冷却液加热器"的是做整车集成/热管理选型的工程师——他们要的不是"有没有加热器"，而是"能不能进我的 CAN 网络"。意图非常精准，转化率高。

## 二、SERP 快照（2026-10-09，en）

| # | 域名 | 页面类型 | 质量评估 |
|---|------|----------|----------|
| 1 | made-in-china.com（NF） | 6kW listing（CAN） | 弱 |
| 2 | cautop.com（NF） | PTC 空气加热器（CAN） | 弱，产品不对版 |
| 3–4, 6 | hvh-heater.com（Nanfeng） | 3kW / 10–18kW / 24kW 产品页，均有 CAN 参数 | **中等偏强，主要对手** |
| 5 | cautop.com（NF） | HVH-Q20（CAN control） | 弱 |
| 7 | made-in-china.com（NF） | listing（CAN） | 弱 |

## 三、竞争分析

- **主要对手是南丰**：3 个产品页都有真实 CAN 参数（CAN2.0B、PWM 联动、故障自诊断上传），内容扎实，是唯一认真在做 CAN 角度的厂商。
- **无 EVLINK 身影**：SERP 里完全没有我方内容，这是空白。
- **可赢性中高**：南丰的页面是"通用产品页顺带写 CAN"，没有一个页面是专门讲"CAN 集成"的。我方可以做一页"CAN 控制"专题落地页：CAN 报文控制逻辑、与整车控制器对接、故障诊断信息上传、PWM 兜底、LIN 可选——工程师想看的都在一页里，精准吃掉这个意图。

## 四、页面策略

- **页面类型**：产品落地页，一页一主词；也可作为各产品页的"CAN 集成"标准模块复用。
- **URL 建议**：`/products/ptc-coolant-heater-with-can-control/`
- **标题/H1**：`PTC Coolant Heater with CAN Control`
- **内容角度**：
  1. CAN 集成：报文控制、功率档位、温度闭环
  2. 故障自诊断信息上传整车控制器
  3. PWM / 使能信号兜底方案，LIN2.1 可选
  4. 真实规格表（QA/QC 系列 CAN 参数，Peter 确认）
  5. 询盘 CTA（OEM 集成支持）
- **规格依赖**：CAN/LIN 参数来自公开资料；建页前 Peter 确认无变化。
