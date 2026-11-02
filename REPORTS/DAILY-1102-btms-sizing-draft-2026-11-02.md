# DAILY-1102《BTMS 选型：3kW／5kW／12kW 怎么选》全文稿（Muse 补欠账，2026-11-02）

- 选题：BTMS 选型（3 kW / 5 kW / 12 kW 制冷量怎么选），BTMS 线。
- 防重复：已读管线表全文对照——新站 BTMS 已发（10113 制冷剂回路 vs 冷却液回路、BTMS-1022v2 报价单、BTMS-1023 德语冬季预处理、Codex 10347 冷板接口）均非选型角度；HVCH 档无关；老站 T12 W2-01 是 HVCH 选型，非 BTMS 选型；无撞题。周五 DAILY-1030 未交付记为缺口，本篇只写 DAILY-1102 一篇，不合并。
- SERP 简报：搜“how to size/select BTMS”者要的是选法（热负荷算法→容量→环境→电气→安装空间），排名靠前页结构一致：分步选型指南＋分档对照表。本篇只借结构，未引用竞品数字作 EVLINK 事实；竞品车型长度-容量映射表一律未采用（别人家标定）；分档只按制冷量与尺寸重量相对大小说。
- ZeroGPT：25.3% ✅ 过线（2026-11-02 实测，全文一次提交）。
- SEMrush 门禁：三个选型词在美国库均无数据——btms sizing、how to size btms、battery thermal management system sizing（第三个词换节点复核过，同样无量）。门禁未过，但 Peter 2026-11-02 批进待审清单，作 BTMS 产品页支撑内容。
- 数值来源：全部出自中文总表 REPORTS/evptc-official-spec-summary.md；12kW 电压值按“先不动”口径未印 750V 或 800V 任一数字，表格内只写待书面确认＋一段说明；噪音＜75dB 已在总表核到；未写认证、客户案例、实测数据。
- 内链：4 条全部实测 HTTP 200（BTMS 分类页、报价单文、冬季预处理文、冷却液文）；正文 HTML 内只链分类页 1 条，另 3 条为可挂建议；5kW 相关表述只链 BTMS 分类页，未引用 404 的 5kW 系列页。
- slug 建议：btms-sizing-3kw-5kw-12kw（wp-json 查过，无占用）。
- 分类：Guide。
- 配图：特色图建议媒体库 10084（BTMS 三风扇分档示意，alt 自注示意性质），发布时以媒体库实物图优先替换。

## 全文

**What Size BTMS Does Your Electric Bus Need? 3 kW, 5 kW, or 12 kW**

Requests like this land on our desk every week. One line: "12-metre electric bus, need a BTMS, please quote." We reply with questions, and sometimes the buyer thinks we are stalling. We are not. Bus length alone does not size a battery thermal management system, and anyone who quotes a unit from that one line is guessing.

Three inputs decide the size. Everything else is detail.

**The three inputs that actually size a BTMS**

First, heat load. A pack that fast-charges twice a day in high ambient heat makes a different amount of heat than the same pack on a mild city route. The kilowatt-hours of the pack do not tell you that. Charge rate, discharge rate, and ambient temperature do. If you only know the pack size, you do not yet know the cooling load.

Second, winter. If the bus parks outside overnight in winter, the pack needs heating, not just cooling. That single answer splits our 5 kW class in two. One model cools only, with heating as an option. The other cools and heats, with a 6 kW PTC heater fitted as standard. Buy the wrong one and the first cold week will tell you.

Third, fit. Voltage window, mounting space, weight, and the coolant loop. A unit that cools well on paper but does not fit the vehicle is not a solution. We have seen projects stall at this point, with a unit delivered and nowhere sensible to put it.

**Three capacity classes**

Our BTMS range comes in three cooling classes. The table below lists only figures from our official specification sheet.

| Model | Cooling | Heating | Weight | Dimensions (mm) | DC voltage window |
|---|---|---|---|---|---|
| LDC300HA-3KW | 3 kW | Optional (external) | 24 kg | 556 × 465 × 291 | DC 400–750V, with precharge |
| LDC502HA-5KW (single-cool) | 5 kW | Optional | 32 kg | 775 × 594 × 286 | DC 400–860V, with precharge |
| LDC560HA-5KW (cool + heat) | 5 kW | 6 kW PTC, standard | 32 kg | 775 × 594 × 286 | DC 400–860V, with precharge |
| LDC280HA-12KW (cool + heat) | 12 kW | 8 kW PTC, standard | 86 kg | 1179 × 778 × 345 | Confirm in writing (see note) |

All four models share the same platform basics: DC 24V low voltage, CAN 2.0 at 250 kbps, R134a refrigerant, 50% glycol coolant, 3.5 Bar system pressure, COP above 2.0, IP67, operating temperature from -35 to 60 °C, 3-year warranty, and 10-year design life. Noise stays below 75 dB.

A note on the 12 kW unit's voltage window: confirm it in writing against the current model interface specification before ordering. Catalogue figures differ across sources, and we do not publish a single figure here until it is confirmed. Do not size the 12 kW unit from a voltage figure you found in an old document.

**Four sizing mistakes we see**

The first is sizing by bus length or pack size alone. Both are inputs, neither is a heat load. A short bus on a fast-charge cycle can need more cooling than a long bus on a gentle route.

The second is buying cooling-only and discovering winter later. The 5 kW single-cool model takes heating as an option, which is fine if you order it that way. It is not fine if you discover the need in January.

The third is confirming only one end of the voltage window. A unit that matches the top of your bus voltage range but not the bottom, or the other way around, is a mismatch. Get both limits in writing.

The fourth is forgetting the physical job. The 12 kW unit weighs 86 kg and measures 1179 mm long. Plan the lifting and the mounting before it arrives, not after. The 3 kW unit at 24 kg is a different job entirely. Check the bay against the dimensions in the table above.

**Confirm these in writing before you order**

- Battery voltage window, upper and lower limits, for the exact model
- Continuous heat load and peak heat load, not just pack size
- Ambient temperature extremes the bus will actually run in
- Heating requirement: cooling-only, or cooling plus heating
- Installation space, mounting position, and weight budget
- Coolant interface and flow available at the connection point
- Control interface: CAN 2.0, and what the vehicle controller expects

**What to send us**

Send those seven inputs and we will match a unit from the three classes above, or tell you if none of them fits. A quote built on written inputs is a quote you can install. For the full range, see our battery thermal management system page.

## 发布包

- SEO 标题：What Size BTMS Does Your Electric Bus Need? 3 kW, 5 kW, or 12 kW | EVLINK
- Meta 描述：Bus length alone does not size a BTMS. Compare our 3 kW, 5 kW and 12 kW battery cooling units, and the inputs you need to confirm in writing before ordering.
- slug 建议：btms-sizing-3kw-5kw-12kw
- 分类：Guide
- 内链（全部实测 HTTP 200）：
  1. battery thermal management system（结尾 CTA，已在正文 HTML 内）→ https://evbtms.com/products/battery-thermal-management-system/
  2. reading a BTMS quotation（可挂建议）→ https://evbtms.com/btms-quotation-five-lines-fit/
  3. preconditioning（可挂建议）→ https://evbtms.com/electric-bus-btms-preconditioning-depot/
  4. battery coolant（可挂建议）→ https://evbtms.com/ev-coolant-battery-thermal-loops/
