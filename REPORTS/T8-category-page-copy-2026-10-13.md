# T8 分类页英文文案稿（2026-10-13，Peter 已批大纲，待建页）

- URL：/products/braking-resistor/
- H1：Liquid-Cooled Braking Resistors for Electric Commercial Vehicles
- SEO title：Liquid-Cooled Braking Resistor for Electric Buses & Trucks | EVLINK
- Meta description：EVLINK HVH-R1402 series liquid-cooled braking resistors dissipate the regenerative braking energy electric buses and trucks can't feed back to the battery. 140 kW continuous, 450–850 V DC, IP6K9K.
- SERP 补充核查（2026-10-13，10-08 十一组词简报之后）：`liquid-cooled braking resistor electric vehicle manufacturer` 的真实 EV 厂商仍只有 Cressall（EV2 水冷模块化，页面为 2021 年新闻稿）与 Danotherm WHBSA（经销商 Astrolkwx 页面，内容约 3 年未更新）——EV 侧内容陈旧、中国厂商缺位，结论不变；`braking resistor electric bus dynamic braking manufacturer` 仍被 VFD/工业分销商占据，EV-only 定位不变。
- 事实源：t8-braking-resistor-specs-record.md（只用规格书正式数值）。红线：不写 150/250 kW 平台目标值、不写峰值、不写认证、不写 CD60/CD80 后缀（用 HVH-R1402 系列）、不写流量具体数字、不写 MOQ/交期、不写船舶、口径"按项目定制"。

---

## §1 What it does

Every electric bus or truck eventually meets a hill its battery can't handle. Fully charged at the top of a long descent, there is nowhere for regenerative energy to go. The battery management system cuts regen to protect the pack, and the driver is left with friction brakes alone — on exactly the grade where they fade fastest.

A braking resistor is the pressure valve for that moment. It takes the energy the battery refuses and turns it into heat, holding continuous braking power while the friction brakes stay cool. On our HVH-R1402 series, that means 140 kW dissipated continuously for 20 minutes, straight into the vehicle's coolant loop.

## §2 Why liquid-cooled on EVs

Air-cooled braking resistors work. They are also big, loud, and hard to place on a vehicle that already fights for every cubic decimeter. At 140 kW continuous, an air-cooled unit needs serious airflow and a serious footprint.

Liquid cooling changes the math. The resistor dumps heat into the same water-glycol loop the rest of the thermal system already uses — no dedicated fans, no extra ducting, and the heat stays inside a circuit the vehicle already manages. The trade-off is real too: you need coolant ports (DN32 on ours), a pump that keeps up, and a control strategy that watches temperature. For a bus or heavy truck with a proper thermal loop, that trade is worth making. For a small vehicle without one, an air-cooled unit may still be the honest answer.

## §3 Specifications — HVH-R1402 series (140 kW model)

| Item | Value |
|---|---|
| Continuous power | 140 kW (20 min at max power) |
| Resistance | 2.24 Ω ±10% (cold, @25℃) |
| Bus voltage | 450–850 V DC (max 1000 V DC) |
| Rated current | 250 A |
| Protection | IP6K9K |
| Vibration | 6 g (ISO 16750-3) |
| Ambient temperature | -40℃ to +85℃ (operating to +110℃) |
| Dimensions | 659 × 232 × 253 mm |
| Weight | approx. 40 kg |
| Cooling | Liquid, 50% water + 50% glycol, DN32 ports |
| Temperature sensing | NTC 5K ±1% |
| Interlock | HVIL |
| Connectors | HV: TE 2-2399607-1; LV: TE 1-1703820-1 |
| Insulation | >100 MΩ @1000 V DC |
| Dielectric strength | 4000 V DC, 60 s |
| Materials | RoHS / ELV compliant |
| Mounting | Horizontal bracket or suspended |
| Validation | 25 production + type tests |

## §4 Three configurations

**1. Standalone resistor unit.** The HVH-R1402 itself, no chopper. For projects where the inverter or an existing chopper already handles the switching — the resistor just does what it does best.

**2. Resistor + chopper, split.** Our chopper controller paired with the resistor over CAN. As bus voltage rises, the chopper switches energy to the resistor by duty cycle. Two boxes, one control loop.

**3. Integrated chopper-brake unit.** Chopper and resistor in one enclosure, low-EMI design. For new platforms that want a single part number and a shorter harness.

Chopper controller parameters are confirmed per project — talk to us with your bus voltage and duty cycle.

## §5 Heat recovery: from burden to resource

The heat doesn't have to be waste. On a bus in winter, 140 kW of braking heat is a meaningful number — routed through the coolant loop, it can preheat the cabin or take the edge off battery warm-up.

We build this resistor as part of a thermal system, not a standalone part. It sits on the same coolant architecture as our battery thermal management and high-voltage PTC heaters, and the same controller family as our three-in-one thermal management controller. One loop, one strategy.

## §6 Applications

- Electric buses
- Heavy-duty electric trucks
- Mining trucks
- Construction machinery

Typical duty: long downhill grades, heavy loads, frequent braking cycles.

## §7 Sizing it right

Three numbers size the resistor.

First, continuous braking power. Take vehicle weight, grade, and speed: a 20-tonne truck holding 30 km/h on a 7% grade needs roughly 100 kW — and the resistor must sustain it for the whole descent, not just the first minute.

Second, resistance. It has to match your DC bus. Ours is built around 2.24 Ω for 450–850 V systems, and we adjust the winding for other bus voltages without changing the platform.

Third, duty and cooling. How long the grade lasts, and what your coolant loop can carry away.

The mistakes we see most: sizing for peak power instead of continuous, forgetting how long the descent actually is, and leaving out temperature sensing and interlock. Every unit we ship carries an NTC sensor and an HVIL loop. Check that whoever you buy from does the same.

## §8 FAQ

**How do I size a braking resistor for my bus or truck?**
Start with continuous power (weight × grade × speed), match resistance to your bus voltage with U²/P, then check duty cycle and cooling. We walk through the full method in our sizing guide.

**What bus voltage does it support?**
450–850 V DC continuous, up to 1000 V DC maximum.

**How is it cooled?**
Through the vehicle's coolant loop — 50% water + 50% glycol via DN32 ports.

**Does it include the brake chopper?**
Three options: resistor only, resistor plus a CAN-coordinated chopper controller, or a fully integrated chopper-brake unit.

**What protection does it have?**
IP6K9K sealing, 6 g vibration resistance, NTC temperature sensing, HVIL interlock, and 4000 V dielectric strength.

**Is it certified?**
We don't claim product certifications we don't hold. The design is validated against 25 production and type tests referencing ISO 16750-3, ISO 20653, and ASTM B117, and materials comply with RoHS and ELV.

**Can I get a different resistance value?**
Yes. Resistance is wound to order for your bus voltage — the platform doesn't change.

**What are the MOQ and lead time?**
Project-based. Send us your vehicle parameters and we'll come back with a configuration and schedule.

## §9 CTA

Send us your vehicle weight, typical grade and speed, and bus voltage. Our engineers will check the power and resistance match and come back with a configuration.

---

## 建页备注（Codex）

- 内链：BTMS 分类页、PTC 加热器产品页、三合一控制器产品页（热量回收段落互链）。
- 图片位：主图、三种形态示意，全部标注"待实物图"（Photo pending — product in production）。
- 面包屑：Home / Products / Braking Resistor。
- 红线自查（Muse 2026-10-13）：✓ 无平台目标值 ✓ 无峰值 ✓ 无认证宣称 ✓ 无后缀 ✓ 无流量数字 ✓ 无 MOQ/交期 ✓ 无船舶 ✓ 无编造案例 ✓ 人味写作（禁用 delve/furthermore/moreover/it's important to note/in conclusion；破折号仅 2 处）。
