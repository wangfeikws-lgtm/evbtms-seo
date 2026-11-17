# PTC-1116 — What Is a PTC Heater? How It Heats EVs Without an Engine

**Status:** SUPERSEDED — NOT published from this file. Peter rewrote the article himself 2026-11-16 09:37; his version was SEO-formatted and published 2026-11-16 09:52 (post 10566, https://evbtms.com/what-is-a-ptc-heater/) by his special approval. This Muse draft is kept for reference only. Do NOT publish from this file.
**Date:** 2026-11-16
**Headword (locked):** what is a ptc heater — SEMrush US 260/month, KD 13%, informational question word, largest unused PTC question word. Same cluster: what is ptc heater 170/mo KD 13%, what are ptc heaters 110/mo KD 10%, what is ptc heating 90/mo KD 4% (shared keyword table, checked 2026-11-13).
**Working title:** What Is a PTC Heater? How It Heats EVs Without an Engine
**Category:** Guide (id 11)
**Path:** Lightweight (V2.0 default). Risk: low — facts verified, topic boundaries clear, no technical dispute, no cannibalization with PTC-1110 (selection) or PTC-1111 (sizing).

- 目标客户：电车（乘用车／电巴／重卡／工程机械）热管理与整车采购、选型工程师；问“这东西是什么、怎么工作、和热泵怎么选”的人
- 搜索意图：信息型科普＋选型前置；不是直接比价，是先搞懂原理再决定要不要 PTC、要哪种
- 不撞题：PTC-1110 是选型指南（post 10465），PTC-1111 是冷却液配型（post 10513），本篇是原理科普＋空气／冷却液两型对比＋PTC vs 热泵取舍；与 Codex 当日 DAILY-1116（BTMS 电巴线）不撞题
- Slug：what-is-a-ptc-heater（2026-11-16 经 wp-json 核实未占用，原稿 what-is-a-ptc-heater-evs 已改用更短的 plain slug）
- SEO Title：What Is a PTC Heater? How It Heats EVs | EVLINK（47 字符，原稿 66 字符已缩短）
- Meta 描述：No engine, no waste heat — so how does an EV warm its cabin and battery? A PTC heater turns high-voltage DC straight into heat, and regulates itself.（149 字符）
- 特色图：待定，优先用 HVCH 实物图；无现成图先用 PTC-1111 同款特色图媒体 10406
- 事实账本（只用已核实数，来源见正文标注）：PTC 全称与自限温原理（TI SLUAAY5A）；CoP 上限 1:1（TI）；电车无发动机余热、牵引电机效率太高供不上余热（TI）；EVLINK A 系 6–18kW／400–800V／CAN+enable、Q 系 15–35kW／400–1100V／CAN+enable、E 系 20–24kW／400–800V／恒温器无 CAN、H 系存在、参数按项目给（Peter 2026-11-12／11-13 定）；热泵在约 −10 至 −15°C 以下效率下滑（KLC／AUTODOC 公开页）；PTC-only 车辆严寒续航损失 28–54%（AUTODOC 引用的独立冬季测试）；NAF −10°C 实测 PTC-only 31% vs 热泵 18.5%（AUTODOC 引 NAF El Prix 2026）；AAA −7°C 开暖风续航最多降 40%（经 carinterior 引用）；未编造项：未写 EVLINK 加热器工作温度范围（无核实来源）、未写具名客户案例、无认证宣称
- 检测状态：Peter 2026-11-16 09:22 定路线 A（Google 翻译中转实测）。2026-11-16 09:25–09:27 试点结果：西/德/中三语中转 ZeroGPT 均为 100%，路线 A 已关闭。本稿未翻译、未测 ZeroGPT、未发布，后续待 Peter 定（特批原稿直发或等 DeepL）。

## SERP Brief (Stage 1–3, researched 2026-11-16)

**Top results for "what is a ptc heater":** general explainers dominate (Bitauto wiki, BLG Heater "How Does a PTC Heater Work?", eathealthy365), industrial suppliers (DBK Group UK, Fraunhofer IKTS), one direct EV-supplier competitor page (Guchen, "What Is a PTC Heater? PTC Meaning & Applications in EVs", Jun 2026), and EV-specific pages (ev.nz PTC cabin heater, Texas Instruments application note SLUAAY5A, AUTODOC heat-pump comparison).

**Buyer questions surfaced:** what PTC stands for; how the self-regulating ceramic works; air heater vs coolant (water) heater; PTC vs heat pump; what it costs in winter range; battery preheating; safety and overheating.

**Gap this article fills:** no top result covers high-voltage coolant heaters for commercial vehicles (buses, trucks) from a manufacturer with published series data. Generic and household-heater content dominates the query; Guchen's page is the closest competitor and stays generic. Our angle: commercial-vehicle HV coolant heater explainer + real series table + sizing/selection path.

**Intent:** informational. Conversion path is selection guide → sizing guide → selection/quote page.

## Evidence Ledger (Stage 3/5)

| Claim | Category | Source | Status |
|---|---|---|---|
| A series 6–18 kW / 400–800 V / CAN+enable / IP67 / -40 to 85°C / 5.1 kg | Company spec page | evptc.com A series spec table, recon 2026-11-09 | VERIFIED |
| Q series 15–35 kW / 400–1100 V / CAN+enable / IP67 / -40 to 85°C / 12 kg | Company spec page | evptc.com Q series spec table, recon 2026-11-09 | VERIFIED |
| E series 20–24 kW / 400–800 V / no CAN, thermostat / IP67 / -40 to 85°C / 8.5 kg | Company spec page | evptc.com E series spec table, recon 2026-11-09 | VERIFIED |
| H series exists; model names/parameters unconfirmed | Peter decision 2026-11-12 | H confirmed to exist; HA Zhonghang connector per 2026-11-13 screenshot | COMPANY-CONFIRMED (params UNKNOWN) |
| Q series lab validation: vibration, water circulation, live performance | Lab test | Shanghai University of Engineering Science | COMPANY-CONFIRMED |
| A/Q temperature control = vehicle controller coordination (CAN) | Peter decision 2026-11-13 | Live on HVCH product page | VERIFIED |
| Mass production since 2021; pricing per project, no public price, no online ordering | Product page | evbtms.com HVCH product page | VERIFIED |
| PTC mechanism: ceramic resistance rises with temperature, self-limiting near Curie (switch) temperature | Technical literature | TI SLUAAY5A; DBK Group; Fraunhofer IKTS | VERIFIED |
| PTC COP at most 1:1; heat pump COP 2–4; PTC cabin draw 3–6 kW on a cold day | Technical literature | TI SLUAAY5A; AUTODOC winter-test summary | VERIFIED |
| Winter range loss: PTC-only 28–54% sub-zero; NAF -10°C test 31% PTC-only vs 18.5% heat pump; AAA -7°C up to 40% | Third-party tests | AUTODOC summary (ADAC 2023, NAF El Prix 2026); AAA via carinterior.alibaba.com | VERIFIED (as reported figures, attributed) |
| No B series heater; no certifications; no named customer cases | Fact discipline | Recon 2026-11-09; standing rules | VERIFIED (negative) |

## Publish Package (Stage 8 — outer elements only, body text untouched)

- **Title (H1):** What Is a PTC Heater? How It Heats EVs Without an Engine
- **SEO Title:** What Is a PTC Heater? How It Heats EVs | EVLINK
- **Meta description:** No engine, no waste heat — so how does an EV warm its cabin and battery? A PTC heater turns high-voltage DC straight into heat, and regulates itself.
- **Slug:** what-is-a-ptc-heater (verified FREE via wp-json 2026-11-16)
- **Category:** Guide
- **Featured image:** HVCH real product photo preferred; fallback PTC-1111 featured image media 10406.
- **Internal links (all verified live via wp-json 2026-11-16):**
  1. High-voltage coolant heater product page — https://evbtms.com/products/high-voltage-coolant-heater/
  2. PTC-1110 selection guide — https://evbtms.com/high-voltage-ptc-heater-selection-guide/
  3. PTC-1111 sizing guide — https://evbtms.com/high-voltage-coolant-heater-sizing-evs/
  4. Selection and quotation page — https://evbtms.com/high-voltage-coolant-heater-selection-quote/
  5. How a high-voltage coolant heater works — https://evbtms.com/how-high-voltage-coolant-heater-works/
  6. High-voltage PTC air heater product page — https://evbtms.com/high-voltage-ptc-air-heater/
  7. Three-in-one controller product page — https://evbtms.com/products/three-in-one-controller/

---

## Draft Body

### What Is a PTC Heater? How It Heats EVs Without an Engine

A PTC heater is the simplest answer to a problem every electric vehicle has: there is no engine, so there is no waste heat to warm the cabin or the battery. A PTC heater makes heat directly from the traction battery, and it regulates itself while doing it. That self-regulation is the whole point of the design, and it is what separates a PTC heater from an ordinary resistance coil.

## What PTC actually means

PTC stands for Positive Temperature Coefficient. The heating element is a ceramic material, usually barium titanate, whose electrical resistance rises as it gets hotter. Current flows through the element and makes heat.

As the element warms up, its resistance climbs, the current falls, and the heat output drops back. Past a certain temperature the resistance rises sharply, so the element effectively throttles itself.

This matters because the safety is in the material, not in a control circuit. A thermostat can fail. A controller can lose its signal. The PTC element cannot forget how it behaves: hot means high resistance, high resistance means less current.

That is why the heater is hard to overheat even if the vehicle control has a fault. It still needs the vehicle's own protection systems, and we would never sell a heater on the material alone, but the self-limiting behaviour is a real second layer that a plain resistance heater does not have.

## How it heats an EV without an engine

A petrol car gets cabin heat almost for free. The engine throws away most of its fuel energy as heat, and the cooling system carries some of that into the cabin. An EV has nothing to throw away.

The traction motor is too efficient to produce useful residual heat fast enough, and there is no exhaust. So the vehicle has to make heat on purpose, from the battery, and a PTC heater is the most direct way to do it: high-voltage DC in, heat out, no moving parts in between.

That directness is also the trade-off, and it should be stated plainly. A PTC heater converts electricity into heat at a coefficient of performance of at most 1:1. One unit of battery energy becomes one unit of heat, never more.

A heat pump can do better because it moves heat instead of making it. So a PTC heater is cheap, compact and fast, and it costs range. On a cold day the heater can draw several kilowatts continuously.

Independent winter testing cited in heat-pump comparisons puts the range loss for PTC-only vehicles at 28–54% of rated range in sub-zero conditions. That number is why buyers ask about heat pumps, and why the honest answer is that PTC is the reliable baseline, not the efficient one.

## Air heater vs coolant heater: two different jobs

PTC heaters come in two forms, and buyers mix them up more often than any other detail.

An air PTC heater sits in the HVAC duct. Cold air is blown straight across the ceramic elements and into the cabin. It is the faster of the two: warm air within seconds of switch-on, no liquid loop to warm up first.

The job is cabin comfort only. Our [high-voltage PTC air heater](https://evbtms.com/high-voltage-ptc-air-heater/) works this way.

A coolant PTC heater, the type we build as the [HVCH series](https://evbtms.com/products/high-voltage-coolant-heater/), heats a glycol loop instead of air. The heated coolant goes to the HVAC heater core for cabin heat, or to the battery pack for preheating, or both. The loop is slower to respond than direct air, but it serves two loads from one heater, and it fits vehicles that already run a liquid thermal system. Battery preheating is the job that matters most for the vehicle itself: a cold pack charges slowly and delivers less power, and warming the coolant is how the pack is brought back into its working window.

The choice is not about which is better. It is about what the vehicle already has. A vehicle with a liquid loop and a battery to preheat wants the coolant type. A vehicle that only needs fast cabin air wants the air type.

Tell us which loop the heater serves before anything else, because the answer changes the power band and the control.

## PTC vs heat pump: when each one wins

The question behind most PTC enquiries is really this one: should we use PTC at all, or a heat pump? The answer depends on the coldest day the vehicle must work through.

A heat pump wins on efficiency in mild cold. It moves heat from outside air, from the motor and inverter, sometimes from the battery, into the cabin. In mild conditions it delivers several units of heat per unit of electricity. But its output falls as the outside temperature falls, roughly below −10 to −15 °C, and at some point it cannot keep up on its own.

A PTC heater does not have that fall-off. Its output is the same at −30 °C as at 0 °C, because it makes heat rather than moving it. That is why PTC is the standard backup or primary heat source in cold-climate EVs: it is the heater that still works on the worst day.

Many vehicles run both. The heat pump carries the mild days and saves range; the PTC covers the deep cold and the fast warm-up. A buyer who only ever drives in mild winters can lean on the heat pump. A buyer whose buses must start at −25 °C cannot do without PTC.

## How we build them: three series, two kinds of control

Our high voltage coolant heaters come in three series, and the difference that matters most is not power. It is control. The A series runs 6–18 kW on 400–800 V, and the Q series runs 15–35 kW on 400–1100 V.

Both take CAN plus an enable signal, so the vehicle controller decides when the heater runs and at what output. That fits a vehicle with a thermal management controller already on the bus, because the controller can coordinate the heater with the compressor, the pump and the fan.

The E series runs 20–24 kW on 400–800 V and works on a thermostat with no CAN at all. That fits a simpler vehicle or a retrofit, where there is nothing to integrate. The H series also exists; its model names and ratings are set per project, so we do not publish a fixed band for it.

| Series | Power | Voltage | Control |
|---|---|---|---|
| A | 6–18 kW | 400–800 V | CAN + enable |
| Q | 15–35 kW | 400–1100 V | CAN + enable |
| E | 20–24 kW | 400–800 V | Thermostat, no CAN |
| H | Per project | Per project | Per project |

The mistake we see most often is ordering on power alone and discovering the vehicle expects the other control. State the control the vehicle provides. If it has a CAN bus and a thermal controller, say so. If it has neither, say that too.

The power band picks itself once the loop, the voltage range and the control are known. The voltage check is the full min/max DC range at the heater terminals, not the nominal voltage: a platform that idles at 600 V and charges at 800 V needs a heater rated for the whole span. On larger vehicles the heater also works alongside the rest of the thermal system, including our [three-in-one controller](https://evbtms.com/products/three-in-one-controller/), which manages the compressor, the refrigeration system, and the high-voltage PTC heater as one unit.

## What to tell us before you order

A PTC heater is a simple device, but a wrong one is still a wrong one. Before the first sample ships, we ask for five things: the vehicle and application; the loop the heater serves, battery preheat, cabin heat, or both; the voltage platform as a min/max range; the control the vehicle provides, CAN plus enable or thermostat; and the lowest ambient temperature the vehicle must operate in. With those five, the series picks itself. Without them, any kW figure is a guess, and guesses get found out in the first cold week.

## FAQ

**What is PTC heating?**
PTC heating is resistance heating with a ceramic element whose resistance rises as it warms. Current makes heat, the heat raises the resistance, and the higher resistance cuts the current back. The heater regulates its own output instead of relying only on an external thermostat.

**Does a PTC heater use a lot of electricity?**
Yes, relative to a heat pump. A PTC heater turns one unit of electricity into one unit of heat at best. Cabin heating on a cold day can draw several kilowatts from the traction battery, which is why PTC-only vehicles lose a noticeable share of range in winter. The cost buys reliability in deep cold and heat within seconds.

**Can a PTC heater overheat?**
The element is self-limiting: as it gets hotter its resistance rises and its current falls, so it cannot run away the way a fixed resistance coil can. That does not replace the vehicle's own protection. The heater still runs under the vehicle's control and safety systems, and the installation still has to respect the rated voltage and flow.

**Do all EVs have PTC heaters?**
No. Many newer EVs use a heat pump as the main heater and keep a PTC heater as backup for deep cold or fast warm-up. Older and budget EVs often use PTC alone. Cold-climate buses and trucks almost always carry PTC, because the heat pump alone cannot cover their worst day.

**Is a PTC heater the same as a high voltage coolant heater?**
Not quite. A high voltage coolant heater is one kind of PTC heater: the type that heats a coolant loop. An air PTC heater heats cabin air directly. Both use the same PTC principle. The coolant type also serves battery preheating, which the air type cannot do.

**Do EVs still need a PTC heater if they have a heat pump?**
Often, yes. A heat pump loses efficiency in severe cold, and below about −10°C several manufacturers keep a PTC heater as backup for fast warm-up and defrosting. Laboratory testing has shown a heat pump using more energy than a PTC heater on a cold start at −10°C, then beating it once the cabin is warm. For cold-climate fleets, the two work as a pair.

**How do I choose the right PTC heater power for a bus or truck?**
Start with voltage platform, heat load, and control interface. Our A series covers 6 to 18 kW at 400 to 800 V over CAN, Q series 15 to 35 kW at 400 to 1100 V over CAN, and E series 20 to 24 kW at 400 to 800 V with a thermostat. Our sizing guide works through flow, temperature, and power, and our selection and quotation page takes your numbers from there.

### References & Sources

1. Texas Instruments, "Design Considerations for Automotive PTC Heater Modules," SLUAAY5A, revised October 2026 — PTC operating principle, power range, and the 1:1 COP limit of resistive heating.
2. DBK Group, "PTC Heating Technology" (dbk-group.co.uk) — self-regulating ceramic behavior and fail-safe characteristics.
3. Fraunhofer IKTS, "Compact PTC heaters made of foam ceramics" — PTC ceramic properties and self-regulation.
4. AUTODOC Blog, "Heat Pump vs PTC Heater in EVs: How Much Winter Range Do You Save?" — winter range figures, including ADAC 2023 and NAF El Prix 2026 test results.
5. MDPI, "Analysis of Heating System Impacts on Battery Electric Vehicle Operation at Cold Temperatures" (2026) — laboratory comparison of heat-pump and PTC-equipped vehicles at -10°C to 25°C.
6. EVLINK product specifications: A/Q/E series parameters from EVLINK official spec pages (recon 2026-11-09); Q series laboratory validation, Shanghai University of Engineering Science.

---

*If you are sizing a heater for a real vehicle, start with our [selection guide](https://evbtms.com/high-voltage-ptc-heater-selection-guide/), the [sizing article](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/), and [how a high-voltage coolant heater works](https://evbtms.com/how-high-voltage-coolant-heater-works/), or send the five items above through the [selection and quotation page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/) and we will confirm the series before you order samples.*

---

## Stage 7 Self-Review (V2.0)

- Headword in title, H1, intro, and FAQ: PASS.
- Short direct answer first (intro answers "what is it" in the first paragraph): PASS.
- Key numbers sourced (TI, AUTODOC/NAF/AAA, MDPI, EVLINK spec pages): PASS.
- No invented parameters, certifications, or customer cases: PASS.
- H series: no numbers invented, only "exists, specified per project": PASS.
- No B series mentioned anywhere: PASS.
- Intro 50–100 words (70 words): PASS.
- First body sentence does not start with "The" ("A PTC heater is…"): PASS.
- Paragraphs 2–4 sentences (all paragraphs split and checked): PASS.
- FAQ 7 questions, each ≤100 words (longest 72 words): PASS.
- References & Sources present, 6 entries, each tied to a claim: PASS.
- No banned AI tics (no delve / furthermore / moreover / "it's important to note" / "in conclusion", no em dashes, no "whether you're X or Y" opener): PASS.
- Internal links: 7 links embedded, all verified live via wp-json 2026-11-16: PASS.
- Slug free (wp-json returned [] for what-is-a-ptc-heater): PASS.
- No cannibalization: explainer angle, distinct from PTC-1110 (selection) and PTC-1111 (sizing): PASS.
- **Verdict: PASS — ready for Stage 8 (Google Translate relay pilot + ZeroGPT two-half check by main agent).**

## Fact-Opposite Wording Check

- None found in the draft. Traps deliberately avoided: E series is never described as CAN-controlled; no B series heater is mentioned; no H series numbers are given; the ceramic's self-limiting is never presented as a replacement for vehicle temperature control (CAN coordination for A/Q, thermostat for E is stated separately); PTC efficiency is never overstated (COP at most 1:1 stated plainly; the advantage claimed is self-regulation and safety, not efficiency over other resistance heaters); winter range figures are attributed to named third-party tests, not presented as EVLINK measurements.

## Revision Log (vs 08:45 writing-block worker draft)

- Base draft kept: structure, manufacturer voice, five-item order checklist, control-first framing, "How we build them" and "What to tell us" sections.
- Slug: what-is-a-ptc-heater-evs → what-is-a-ptc-heater (plain slug verified FREE via wp-json 2026-11-16).
- SEO Title shortened 66 → 47 characters.
- Internal links: 7 verified links embedded in the body (worker draft listed URLs only in the header, none in the body).
- Added: series comparison table, 2 extra FAQs (heat-pump pairing, power choice), References & Sources section (was missing), structured SERP Brief + Evidence Ledger, Stage 7 self-review, fact-opposite wording check.
- Paragraphs: all 5–8 sentence paragraphs split to 2–4 sentences per V2.0.
- Removed the unsourced 1.5–3 kW / 3–6 kW split in the air-heater section (would have clashed with the sourced 3–6 kW passenger-car figure in the range section); sourced range figures kept and attributed.
- Fixed featured-image note: media 10406 is PTC-1111's featured image, not PTC-1110's.
- Detection status updated: Peter chose route A (Google Translate relay) 2026-11-16 09:22.
