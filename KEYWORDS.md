# KEYWORDS.md — 四品类关键词地图 v2（2026-10-08）

> 图例：✅ SERP 已验证可打 / 🔬 验证中 / ⏳ 待验证（假设，**不得直接建生产页**）
> v1（12 词，加热器/BTMS 方向）完整保留在下文；v2 新增制动电阻、三合一控制器两品类。

## 品类一：制动电阻 Braking Resistor（P0，新品类，页面待建）

✅ SERP 已验证（2026-10-08，简报 `REPORTS/serp-braking-resistor-ev.md`，Muse 已复核）。
核心结论：EV 定向词竞争弱（仅 Cressall、REO 两家真对手，内容老化 3–4 年）；"brake chopper resistor EV" 内容真空；
"electric bus" 修饰词被 Google 判为工业意图（勿硬打）；工业词（VFD/电梯/起重机）为价格绞肉机，战略放弃。

候选方向（✅ 已验证，见 SERP 简报 §10）：
| # | 候选关键词 | 页面类型建议 |
|---|-----------|-------------|
| R1 | braking resistor EV | 产品分类页（主）✅ |
| R2 | brake chopper resistor EV | 博客 B1（内容真空）✅ |
| R3 | EV braking resistor sizing / how to size | 博客 B2（选型缺口）✅ |
| R4 | electric vehicle braking resistor manufacturer | 采购页（marketplace 主导，谨慎）⏳ |
| R5 | braking resistor VFD / elevator / crane | ❌ 战略放弃（价格绞肉机，见 SERP 简报 §10） |

## 品类二：三合一控制器 Three-in-One Controller（P1）

✅ **产品类型已澄清（2026-10-09）**：工厂 Q&A ＋ 网站现页面（`/products/three-in-one-controller/`，H1 "Three-in-One EV Thermal Management Controller"）一致确认为**热管理三合一控制器**（压缩机控制器＋制冷系统 ECU＋高压 PTC 控制器）。
⚠️ 早前"OBC + DC/DC + PDU 电源电子"的理解系误会，作废；T1–T4 的 SERP 验证同步作废，需按热管理方向重做。
英文主名：`Three-in-One Controller` / `3-in-1 Thermal Management Controller`。
产品档案：`REPORTS/product-brief-three-in-one-thermal-controller.md`。

⏳ 待 SERP 验证（热管理方向）：
| # | 候选关键词 | 页面类型建议 | 状态 |
|---|-----------|-------------|------|
| TH1 | three in one thermal management controller | 现有分类页优化 | ⏳ |
| TH2 | integrated thermal management controller electric bus | 落地页 | ⏳ |
| TH3 | EV thermal management controller | 落地页 | ⏳ |
| TH4 | electric compressor controller | 落地页 | ⏳ |

## 品类三：高压冷却液加热器 High Voltage Coolant Heater（P2）

### A. 产品长尾词 → 落地页
| # | 关键词 | 状态 |
|---|--------|------|
| 1 | 800V high voltage PTC coolant heater for electric bus | ✅（SERP GO，简报 `serp-h1-800v-ptc-coolant-heater-ebus.md`） |
| 2 | high voltage heater for hydrogen fuel cell bus | ✅（SERP GO·小众，简报 `serp-h2-hydrogen-fuel-cell-bus-heater.md`） |
| 3 | DC870V PTC coolant heater for mining truck | ✅（SERP GO·高优，简报 `serp-h3-dc870v-mining-truck.md`） |
| 4 | high voltage battery heater for electric truck | ✅（SERP GO·高优，简报 `serp-h4-battery-heater-electric-truck.md`） |
| 5 | PTC coolant heater with CAN control | ✅（SERP GO·中优，简报 `serp-h5-ptc-can-control.md`） |

### B. 场景/问题词 → 博客
| # | 关键词 | 状态 |
|---|--------|------|
| 6 | electric bus battery heating in winter | ⏳ |
| 7 | PTC coolant heater vs air heater EV | ✅（SERP GO，初稿待 Peter 确认发布） |
| 8 | how battery thermal management works in electric bus | ⏳ |
| 9 | fuel cell bus thermal management challenges | ⏳ |

### C. 采购意向词 → 落地页
| # | 关键词 | 状态 |
|---|--------|------|
| 10 | BTMS supplier for commercial electric vehicles | ⏳ |
| 11 | high voltage heater manufacturer e-bus OEM | ⏳ |
| 12 | custom PTC heater battery thermal management | ⏳ |

## 品类四：BTMS / Battery Thermal Management System（P3）

已有 #8、#10 覆盖；可增补（⏳ 待验证）：
- battery thermal management system for electric truck
- BTMS manufacturer China OEM

## 验证路线图

- ✅ 已完成：#7、#1、#2、#3、#4、#5、制动电阻 R 组（简报均已推送）
- ⚠️ 三合一 T 组作废重做：产品澄清为热管理三合一（非 OBC+DC/DC+PDU），T1–T4 验证作废，改按 TH1–TH4（热管理方向）重做
- ⏳ 待排期：#6、#8、#9、#10、#11、#12 ＋ BTMS 增补 2 词 ＋ TH1–TH4，Muse 按优先级逐批验证

## 执行规则（对应 TASKS.md）

1. ⏳ 词不得建生产页；先 SERP 验证（Muse）→ 再建页（Codex）
2. 一页一主词；标题/H1 直接用目标关键词
3. 英文正文一律 Muse 撰写/改写，Codex 不写英文、不复制老站原文
4. 新建页面 = 正式发布，走 `WAITING_APPROVAL`
