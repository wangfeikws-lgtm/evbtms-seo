# 矿卡专区三模块正式文案（2026-10-20，待 Peter 审）

> 用途：evbtms.com 矿卡专区的三模块正式文案，替换/补强现有泛化表述。
> 页面对位：现 /applications/ 矿卡专区（H2 "Mining Vehicle Thermal Management for the Complete Haul Cycle"）现有四条要点——Sustained high-load heat rejection / Regenerative-braking and charging loads / Dust, shock, vibration and washdown exposure / Altitude, temperature and remote serviceability；专区有 "View Complete Application Page" 入口指向矿卡完整页。本三模块依次对位：模块 1 → 环境与温度要点；模块 2 → 再生制动负荷要点；模块 3 → 专区结尾的 EVLINK 方案落点（BTMS＋制动电阻组合）。落到 /applications/ 专区或矿卡完整页均可直接套用。
> 事实来源：REPORTS/mining-truck-research-2026-10-20.md（行业事实均带公开来源）＋ HVH-R1402 / BTMS 已核实规格。红线自查见文末。

---

## Module 1 — Extreme Conditions（极端工况）

**Title: Mines Run from −50 °C Winters to +45 °C Deserts. The Battery Wants 15–35 °C.**

A mine is not one climate. Siberian pits drop below −50 °C in January. Pilbara and Atacama sites sit above +45 °C at midday. Add dust that works into every seal, constant vibration, and altitude that thins the air, and you have the working environment. It is no accident the big OEMs are now trialling battery-electric haul trucks in exactly these places.

The battery ignores all of it. It wants to sit between 15 °C and 35 °C, loaded or empty, January or July.

Closing that gap is our job. Our BTMS covers 3 to 12 kW of liquid cooling for the hot end. For the cold end, PTC heating brings the pack up to temperature before the truck works, because a cold pack that gets charged hard ages fast. The housing is sealed to IP67, so dust and washdown water stay outside.

Send us the coldest morning and the hottest afternoon at your site. We size from those two numbers, never from a brochure average.

> 落点：BTMS 3–12 kW 液冷＋PTC 加热、IP67。事实：矿山 −50 °C（西伯利亚）至 +45 °C（Pilbara/阿塔卡马）为环境描述（SUNHUNK 行业分析）；电池工作窗 15–35 °C（Dataintelo 报告）；Cat 793 / Komatsu 930 在 Pilbara 试用仅作行业趋势一句带过（Australian Trades 转 EV Report），未写成我方客户；−50 °C 未宣称产品覆盖。

---

## Module 2 — Downhill Energy（下坡能量）

**Title: The Downhill Problem: Two Megawatts Has to Go Somewhere**

Run the numbers on a truck. Five hundred tons loaded, a 10% grade, and gravity asks for more than 2 MW of braking power, held for 10 to 15 minutes without a pause. That energy goes somewhere. The only question is what absorbs it.

Regenerative braking takes the first share, and it should. But regen is a guest in the battery, not a tenant. When the pack sits near full, or runs hot, or cold, the BMS trims regen back, sometimes hard. Friction brakes alone on that descent means heat, wear, and a steep maintenance bill.

That gap is where our HVH-R1402 braking resistor works. It takes the surplus as heat: 140 kW continuous for 20 minutes, enough for the full descent with time to spare. The specs are plain: 2.24 Ω, 450 to 850 V DC, liquid-cooled through a DN32 connection, sealed IP6K9K against dust and washdown. NTC temperature sensing and a high-voltage interlock watch it while it works.

Size the resistor for the worst descent on your route, not the average one. Gravity does not average out.

> 落点：HVH-R1402 制动电阻已核实规格全套（140 kW 连续 20 分钟、2.24 Ω、450–850 V DC、IP6K9K、DN32 水冷、NTC＋高压互锁）。事实：500+ 吨、10% 坡道、>2 MW 连续耗散 10–15 分钟（Medium 行业科普）；SOC 高/温度极端时再生制动大幅受限（Solid Industry News）。未写冷却流量数字（口径未决，按简报红线避开）。

---

## Module 3 — What Happens Without Cooling（无冷却后果）

**Title: No Cooling Is Not a Neutral Choice**

Some buyers treat thermal management as an option box. On a mining truck it is not. It is the difference between a battery that lasts the contract and one that does not.

Research puts numbers on it. A mining truck battery run at 40 °C ambient, fully loaded, with no cooling reached a peak temperature of 81.31 °C, with a 5.76 °C spread across the pack. Both figures cross the safe line. At those temperatures cells age in months instead of years, the weak cells drag the rest down, and the margin before a thermal event gets thinner than anyone should accept.

Cooling is only half the answer. The downhill braking energy has to land somewhere, and a full battery cannot take it. So we pair the two: a 3 to 12 kW BTMS holding the pack inside the 15 to 35 °C window, and a braking resistor absorbing the descent energy the battery has to refuse.

Fit the cooling before the truck needs it. Retrofitting thermal management into a fleet already cooking its packs costs more and fixes less.

> 落点：BTMS＋制动电阻组合方案。事实：40 °C 满载无冷却电池最高 81.31 °C、温差 5.76 °C、双双超安全阈值（ScienceDirect 学术研究）；热失控风险与寿命衰减为基于该数据的定性表述，未编 EVLINK 自家测试数据。

---

## CTA（接模块 3 之后）

**Send Us Your Route. We Will Do the Sizing.**

Tell us the truck model and its gross weight, the steepest grade on your haul road and how long the descent runs, your DC bus voltage, and the coldest and hottest days at your site. We will come back with a BTMS and braking-resistor configuration sized for that cycle, and we will tell you plainly what we still need to know before anyone talks production.

---

## 红线自查

- [x] 行业事实只用调研简报带来源条目：温度跨度（SUNHUNK）、电池 15–35 °C 窗（Dataintelo）、下坡 >2 MW/10–15 分钟（Medium）、无冷却 81.31 °C/5.76 °C（ScienceDirect）、SOC 高时 regen 受限（Solid Industry News）
- [x] 产品规格只用已核实口径：BTMS 3–12 kW 液冷＋PTC 加热、IP67；HVH-R1402 140 kW 连续 20 分钟、2.24 Ω、450–850 V DC、IP6K9K、DN32、NTC＋高压互锁
- [x] Cat/Komatsu 仅一句行业趋势提及（"big OEMs are now trialling…"，未点名为我方客户、未写成案例）
- [x] 未提 BELAZ；未写任何客户名/矿山名/案例
- [x] 未写未确认认证（无 CE/EMark/UL）；未写 "25 项测试" 数字（本组模块未用到）
- [x] 未写冷却流量（172 vs 160 口径未决）、未写 BR-LC 150/250 kW 目标值、未写 MOQ/交期、未写价格
- [x] −50 °C 仅作矿山环境描述，产品侧未宣称覆盖 −50 °C
- [x] 文风：厂家第一人称、短长句交错、有明确观点（"Gravity does not average out." / "Retrofitting… costs more and fixes less."）；无 delve/furthermore/moreover/in conclusion 等 AI 腔
