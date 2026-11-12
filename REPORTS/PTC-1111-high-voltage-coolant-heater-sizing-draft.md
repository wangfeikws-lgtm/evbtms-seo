# PTC-1111 — High Voltage Coolant Heater Sizing for EVs (DRAFT, Muse)

- 主词：high voltage coolant heater（SEMrush 美国 20/月，KD 不可用；同簇 17 变体、总量 150，≥10 的 8 个）
- 核心词即主词；不撞题：PTC-1110 是通用选型指南（post 10465），10405 是 BTMS 场景选型（Choosing a PTC Coolant Heater for a Battery Thermal Management System），科普文讲工作原理；本篇讲冷却液回路的配型（热负荷／流量／温度／功率四项）
- Slug（待发布前复核是否被占用）：high-voltage-coolant-heater-sizing-evs
- SEO Title：High Voltage Coolant Heater Sizing for EVs | EVLINK（48 字符）
- Meta 描述：Sizing a high voltage coolant heater? Match heat load, coolant flow, inlet temperature and voltage platform before you order samples — the four numbers we check first.（158 字符）
- 分类：Guide（id 11）；特色图：复用媒体 10406（Q-series 插图，PTC-1110 同款；如媒体库有未用的 HVCH 实物图可换）
- 内链（发布前逐一核验目标页存在）：HVCH 产品页 https://evbtms.com/products/high-voltage-coolant-heater/；PTC-1110 选型指南 https://evbtms.com/high-voltage-ptc-heater-selection-guide/；BTMS 产品页 https://evbtms.com/products/battery-thermal-management-system/；三合一控制器页 https://evbtms.com/products/three-in-one-controller/

---

# High Voltage Coolant Heater Sizing for EVs: Flow, Temperature and Power

A high voltage coolant heater is sized right when three things line up: the heat load, the coolant flow, and the voltage platform. Get the heat load wrong and the loop never holds temperature. Get the flow wrong and the heater cannot move its heat into the coolant at all. Get the voltage wrong and the unit will not run on the vehicle. Everything else in this article is about how to pin those three down before you order samples.

## What the heater actually heats

A coolant heater does not heat air. It heats a liquid loop, and that loop serves one of two jobs, sometimes both. The first job is battery preheating: warming the pack so it can charge and discharge in cold weather. The second is cabin heat through a heat exchanger. The two jobs want different things from the same heater. A battery loop cares about a steady coolant temperature and a known flow. A cabin loop cares about how fast warm air reaches people, which depends on the exchanger and the airflow behind it. When a project brief says only "we need a heater," the first question back is always which loop it serves, or both. The answer changes the power band, the flow requirement, and the control logic. We have seen projects stall for weeks because the heater was picked before that question was answered.

## Start from the heat load, not the catalogue

Catalogues list power bands. Our coolant heaters come in 6 to 18 kW, 20 to 25 kW, and 30 to 35 kW bands, with single units rated 15 to 35 kW. Those bands are the answer, not the starting point. The starting point is the heat load: how much heat the loop must deliver, at what ambient temperature, and for how long. A battery preheat loop on a city bus and a cabin loop on the same bus can ask for very different numbers, even though they share one vehicle. Ambient temperature matters more than most buyers expect. A heater that holds a loop at minus 10 degrees may not hold it at minus 30. Insulation, parking time, and whether the vehicle preheats while plugged in all move the number. We do not publish a universal sizing table because there is not one. What we ask for instead is the duty: the lowest ambient the vehicle must operate in, the target coolant temperature, and how long the heater has to hold it. With those three, the power band picks itself. Without them, any kW figure is a guess, and guesses get found out in the first cold week.

## Match the voltage platform

Coolant heaters run on the traction battery, so the voltage platform is not a detail. Our heaters cover 400V, 600V and 800V platforms, and the Q series runs to 1100V. The check is not the nominal voltage. It is the range: the lowest and highest DC voltage the heater terminals will see across every heating condition. A platform that idles at 600V and charges at 800V needs a heater rated for the whole span, not the middle. Send us the range and we will confirm the series. Send only the nominal voltage and we will ask for the range anyway, because a heater picked on nominal voltage alone is how projects end up with a unit that faults on the first charge cycle. This is also where the Q series earns its place: if the platform runs above 800V, the 1100V rating is not a luxury, it is the requirement.

## Coolant flow and inlet temperature

A coolant heater can only deliver the power the loop can carry away. That is the flow rate, and it is the number most often missing from an enquiry. The loop needs a defined flow, a defined inlet temperature, and a defined glycol type and concentration. Without a flow figure, the heater cannot be validated: the same 20 kW unit behaves completely differently in a fast loop and a slow one. In a slow loop the coolant leaves the heater hotter than the system wants, and the control starts cycling. In a fast loop the heater may never reach its setpoint. Neither is a heater fault. Both are sizing faults, and both are avoidable if the flow is stated up front. The same goes for the fluid. Tell us the coolant type and concentration, the inlet temperature range, and the flow. If the flow is not fixed yet, say so, and say what pump and piping are planned. We would rather size from a range than from silence.

## Control interface: who decides when the heater runs

Two of our series cover the same heating job with different control. The B series takes CAN plus an enable signal, so the vehicle controller decides when the heater runs and at what output. The E series runs on a thermostat and needs no CAN at all. Neither is better in the abstract. A vehicle with a thermal management controller already on the bus will usually want the CAN version, because the controller can coordinate the heater with the compressor, the pump and the fan. A simpler vehicle, or a retrofit, often wants the thermostat version, because there is nothing to integrate. The mistake is ordering one and discovering the vehicle expects the other. State the control the vehicle provides. If the vehicle has a CAN bus and a thermal controller, say so. If it has neither, say that too. The interface record below is the one-page version of this whole article, and it is the page we ask every buyer to fill in.

## One shared interface record

| Item | What to write down |
|---|---|
| Vehicle and application | Bus, truck, construction vehicle; battery preheat, cabin heat, or both |
| Voltage platform | Nominal voltage and the full min/max DC range at the heater terminals |
| Power band | Heat load, lowest ambient, target coolant temperature, hold time |
| Coolant | Type and concentration, inlet temperature range, flow rate |
| Control | CAN + enable, or thermostat; who commands the heater |
| Installation | Space, mounting, coolant connections, low-voltage supply (12V/24V) |
| Validation | Sample plan and the tests the sample must pass |

Fill this in before the first sample ships and most sizing arguments disappear. Leave it blank and they all come back later, usually after the sample is already built.

## Validate the sample, then freeze the configuration

A sample proves the sizing, not the brochure. Our Q series went through lab validation at Shanghai University of Engineering Science covering vibration, water circulation and live performance evaluation, and that is the kind of evidence a sample should be checked against: does it hold temperature in the real loop, does it survive the vibration profile, does the control behave the way the vehicle expects. Run the sample in the actual loop, not on a bench with a bucket of coolant. A bench test proves the heater makes heat. A loop test proves the vehicle gets heat. Once the sample passes, freeze the configuration: same series, same power band, same control, same coolant spec. Changes after that point are a new validation, not a tweak.

## What to send with your enquiry

Send the application, the loop it serves, the voltage range, the heat load with its ambient and target temperature, the coolant type and flow, the control the vehicle provides, and the installation space. Add the annual volume and the sample plan if you have them. That is enough for a real quotation. Anything less and the first reply will be a list of questions, which is fine, but it costs a week. The manufacturers who get the fastest quotes are the ones who send the interface record filled in.

## FAQ

**What is a high voltage coolant heater?**
It is an electric heater that warms the coolant in an EV liquid loop, usually for battery preheating or cabin heat through a heat exchanger. It runs on the traction battery voltage, typically 400V, 600V or 800V, with the Q series rated to 1100V.

**How is it different from a high voltage PTC air heater?**
A coolant heater warms liquid; an air heater warms HVAC air directly. The choice depends on the loop: battery preheat and cabin heat exchangers need a coolant heater, while direct cabin air heating needs an air heater. Tell us the medium and we will point you to the right unit.

**What power do I need?**
It depends on the heat load, the lowest ambient, and the target coolant temperature. Our bands are 6 to 18 kW, 20 to 25 kW and 30 to 35 kW. Send the duty and we will confirm the band; we do not guess from the vehicle type alone.

**What coolant flow does the heater need?**
A defined flow, inlet temperature range, and glycol type and concentration. Without a flow figure the heater cannot be validated in the loop. If the flow is not fixed yet, share the planned pump and piping so we can size from a range.

**Does it need CAN?**
Not always. The B series uses CAN plus an enable signal, so the vehicle controller commands it. The E series runs on a thermostat with no CAN. Tell us what control the vehicle provides and we will match the series.

**Can one heater serve both the battery and the cabin?**
It can, if the loop is designed for it and the heat load covers both jobs. State both jobs in the enquiry with their temperatures and flows, because a heater sized for one job will not automatically cover the other.

## References & Sources

- EVLINK high voltage coolant heater product page, power bands 6–18 / 20–25 / 30–35 kW, single units 15–35 kW, voltage platforms 400/600/800V, Q series to 1100V, mass production since 2021.
- EVLINK HVCH series parameters recon (old-site product pages), A/Q/E series power, voltage, control and weight figures.
- Q series laboratory validation, Shanghai University of Engineering Science: vibration, water circulation, live performance evaluation.
- SEMrush (US database), keyword data for "high voltage coolant heater" and cluster, checked 2026-11-09.
- Google search (US, English), "high voltage coolant heater" results, checked 2026-11-09: Cascadia Motion, Valeo, Webasto HVH 50/70 (5–7 kW), BorgWarner; no standalone sizing guide found.
