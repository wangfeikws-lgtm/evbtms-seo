# 成稿包：BTMS Refrigerant Circuit vs Coolant Loop（人味重写版，2026-10-21）

- **替换对象**：https://evbtms.com/btms-refrigerant-circuit-vs-coolant-loop/（WP 10113，Codex 2026-10-20 稿，GPTZero 判 AI 100%）
- **建议**：同 URL 原地替换正文，URL/Title 不变，不产生新页面
- **SEO Title**（不变）：BTMS Refrigerant Circuit vs Coolant Loop: An OEM Integration Guide
- **Meta description**（新）：The coolant loop and the refrigerant circuit do different jobs, and mixing them up is where BTMS integration goes wrong. EVLINK engineers explain the split, the five modes to define, and the mistakes we see in OEM reviews.
- **目标词**：btms refrigerant circuit / coolant loop / battery thermal management integration
- **内链**：正文中已埋 3 条（BTMS 分类页、BTMS coolant selection 文章、三合一控制器页）

---

## 正文

Every few months a vehicle program sends us a BTMS inquiry with one number in it: "We need 10 kW of cooling." Then we ask the awkward questions. Cooling measured where — at the chiller nameplate, or at the battery inlet on a 40 °C day with the cabin air conditioning running flat out? Most of the time, nobody has written that down yet. That gap, between the refrigerant circuit and the coolant loop, is where BTMS integration actually succeeds or fails.

The two circuits do different jobs. Confusing them is not a paperwork problem. It shows up later as a battery that runs 8 °C hotter than promised during fast charging.

### Two circuits, two different fluids, one heat path

The coolant loop is the battery's plumbing. A water-glycol mix runs through the battery cold plates, picks up cell heat, and carries it to a heat exchanger. Pump, valves, expansion tank, sensors, hoses — that is the loop. Its performance is hydraulic: flow rate, pressure drop, and how evenly the flow splits across parallel cold plates. Get the plumbing wrong and one corner of the pack quietly cooks while the average temperature on the dashboard looks fine.

The refrigerant circuit is the vehicle's air-conditioning hardware doing double duty. Compressor, condenser, expansion device, and inside the chiller, evaporation. The chiller is simply the meeting point: coolant on one side of a plate stack, refrigerant on the other. Heat crosses. The fluids never touch.

Our BTMS units (3 kW, 5 kW and 12 kW) sit on the coolant side of that meeting point, with PTC heating on board for cold starts — 5 kW or 6 kW of PTC on the smaller units, 8 kW on the 12 kW unit. The compressor and condenser belong to the vehicle. That split is deliberate, and it shapes everything below.

### The nameplate lie

Here is the opinion part, and we will stand by it: a chiller's rated capacity is the most misleading number in this industry.

That rating was measured at one refrigerant inlet state, one coolant temperature, one flow, one ambient. Your bus at a depot charger in August matches none of those. Real capacity moves with coolant inlet temperature, compressor speed, condenser airflow, and whether the cabin is also demanding cold air. We have reviewed programs where the "10 kW" chiller delivered closer to 6 kW at the vehicle's actual worst case. The hardware was not faulty. The boundary conditions were fiction.

So size the refrigerant side at your worst operating point, not at the catalog point. If a supplier will not state the conditions behind a capacity number, treat the number as marketing.

### Draw the ownership line early

Separating the circuits is also about who owns what. Battery engineers set the coolant-side limits: inlet temperature, allowed cell-to-cell spread, minimum and maximum flow. HVAC engineers own the refrigerant envelope and can say how much capacity is genuinely available after the cabin takes its share. Controls engineers arbitrate between them.

Write it into one interface sheet. Who commands the pump? Who requests compressor speed? When the battery and the cabin both want maximum cooling at the same moment, who wins? When the refrigerant side cannot deliver, how much does the battery side derate before anyone complains?

Programs that skip this sheet do not avoid the questions. They answer them accidentally, in the field, in July.

### Five modes to define before you freeze components

1. **Driving cooling.** Heat generation at cruise and on grades, real condenser airflow at road speed.
2. **Fast-charge cooling.** The harshest case for most trucks: high heat, zero vehicle speed, weak airflow, and a driver who wants the cabin cold while waiting.
3. **Cold-start warm-up.** Below freezing, the question flips from removing heat to adding it. This is where PTC heating in the coolant loop earns its place — our units run on the vehicle's DC 400–860 V bus and answer over CAN 2.0, so the warm-up strategy is a software decision, not extra hardware.
4. **Cabin-versus-battery competition.** Define the priority rule now, in a document, not during a summer test failure.
5. **Degraded operation.** A pump slows down. A sensor drifts. A fan fails. Decide what the system does — limp, derate, or shut down — before the vehicle decides for you.

### Mistakes we keep seeing in integration reviews

**Sizing the pump from a single flow number.** A pump that hits target flow on a bench misses it once production hoses, fittings and cold plates add their resistance. Work from the full system curve.

**Ignoring trapped air.** One air pocket in a cold plate cuts heat transfer and makes temperature sensors lie. De-aeration is not a commissioning detail; design the high point and the bleed path in from the start.

**Assuming parallel branches share flow evenly.** They do not. Manifold geometry decides, and the branch with the least resistance takes the most coolant. Model it or measure it, but do not assume it.

**Testing cooling and skipping the transitions.** Steady-state cooling is the easy part. The failures hide in mode changes — warm-up handing over to cooling, cabin priority switching mid-charge — where temperatures overshoot and compressors cycle themselves to death.

### How we validate the coupled system

Start on the coolant side alone: flow versus pressure drop across the real loop, leak tightness, de-aeration, sensor plausibility. Map the chiller next, across the coolant and refrigerant conditions the vehicle will actually see. Then run the vehicle scenarios — charge, drive, idle, hot soak, cold soak, and the priority transitions — while logging battery inlet and outlet temperatures, cell spread, coolant flow, pump command, compressor request and ambient.

You are proving a heat path, not a component. A [battery thermal management system](https://evbtms.com/products/battery-thermal-management-system/) that passes bench tests but fails the handover between modes has not passed. (Coolant choice matters more than most teams expect, too — see our notes on [BTMS coolant selection for cold-climate buses and trucks](https://evbtms.com/btms-coolant-selection-cold-climate/).)

### Send us the operating points, not a single number

If you are speccing a BTMS now, send the time-based picture: heat load over the duty cycle, target coolant inlet temperature, allowed cell spread, ambient range, charging profile, and who owns the compressor on your vehicle. We will tell you plainly whether our 3, 5 or 12 kW unit covers it, and where the refrigerant side needs to be checked. Programs with a [three-in-one thermal management controller](https://evbtms.com/products/three-in-one-controller/) on the vehicle can fold the pump, valve and heater commands into one unit, which makes the ownership sheet considerably shorter.

One number gets you a quote. The full operating picture gets you a system that survives August.

---

## FAQ（替换原 FAQ，3 条）

**Does the battery coolant ever mix with the refrigerant?**
No. In a chiller-based layout the two fluids sit on opposite sides of a plate heat exchanger. Heat crosses the plates; the fluids stay in their own circuits. If coolant and refrigerant are mixing, something has failed.

**Why does the same chiller cool less on the vehicle than on the bench?**
Because the bench rating assumes one set of conditions and the vehicle rarely matches it. Coolant inlet temperature, flow, compressor speed, condenser airflow, ambient heat and a competing cabin load all pull real capacity down. Always compare capacity at the same boundary conditions.

**Which circuit should be sized first?**
Neither, on its own. Start from the battery: heat load and the temperatures you will allow. Build the coolant loop hydraulics around that. Then check the refrigerant circuit can actually deliver the required capacity at those same operating points.

---

## 交付备注（给 Peter）

- 与原稿差异：保留全部技术事实和章节逻辑；改成厂家第一人称 + 具体场景（8 月充电站、温差 8°C、10 kW 变 6 kW 的评审实例为行业通例表述，未点名客户）；新增 EVLINK 产品参数（3/5/12 kW、PTC 5/6/8 kW、DC400–860 V、CAN 2.0，均为已核实口径）。
- 发布方式：WP 后台打开 post 10113，正文整体替换；Title/URL 不动；FAQ 若原稿有 FAQ 区块，一并替换。
