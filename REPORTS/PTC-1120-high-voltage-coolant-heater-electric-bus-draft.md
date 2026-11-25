# PTC-1120 v1 初稿（2026-11-25 周三档，PTC 每日一篇）

- 编号：PTC-1120（PTC 每日一篇，2026-11-25 周三档）
- 主词：high voltage coolant heater for electric bus（美国 20/月、KD 不可用；共享词表 2026-11-09 魔法工具全量值，30 天内；2026-11-25 关键词概览复核：美国量显示“不可用”（非 0）、KD 3%（非常容易）、意图商务——量值视图差异已记入共享词表，11-09 值仍为留词依据，KD 与意图更优，按原计划开篇）
- 集群复核：high voltage coolant heater for electric buses 11-25 复核美国量“不可用”、KD 8%、意图信息＋交易；electric vehicle cabin ptc heater 与 11-09 一致（美国 20/月、KD 不可用、CPC $0）
- 集群说明：主词 20/月单开偏薄，按 11-06 HVCH 结论走“一篇吃一串”——电巴角＋复数长尾＋座舱长尾同一篇：high voltage coolant heater for electric buses 20/月＋electric vehicle cabin ptc heater 20/月，集群合计 60/月
- slug：high-voltage-coolant-heater-electric-bus（待发布前 wp-json 核验未占用＋前台 404）
- 分类：Guide；SEO Title 53 字符（High Voltage Coolant Heater for Electric Bus | EVLINK）／Meta 152 字符（Specify the right high voltage coolant heater for your electric bus: power, voltage, CAN control, cabin and battery heat. Send your numbers for a quote.）
- ZeroGPT 切分：正文 9,316 字符／1,615 词；上半＝标题～“Cabin heat is not an afterthought”节末（4,567 字符），下半＝“Send us your numbers”节～FAQ 末（4,749 字符）
- 选题简报链：目标客户＝电巴整车厂／车队采购＋热管理工程师（已有平台、需电巴专用加热方案）；关键词数据＝见上；意图＝商业＋信息（电巴加热器选型／询价前置）；SERP 验证＝2026-11-25 搜索 high voltage coolant heater for electric bus：首页为 Webasto 800V HVH 产品页、Webasto 巴士方案页、Ecer 产品页、本站 HVCH 产品页，无电巴 HVCH 选型／配型指南文章，无 evbtms.com 文章页，缺口明确（竞品均为产品页或方案总览，不回答“电巴该定多大功率、什么电压、怎么控”）；查重＝管线表核对：PTC-1110 选型指南（通用选型）、PTC-1111 配型（通用流量／温度／功率）、PTC-1116 是什么、PTC-1117 挑厂家、PTC-1118 装在哪（EV 通用，座舱＋电池各一笔，未写电巴专篇）、PTC-1119 定制，均未写电巴专篇；T12-W1-3 电巴电池预热在老站 evptc.com、新站无此文；BTMS-1023 场站预调节为 BTMS 系统角、DAILY-1102 为 BTMS 选型、DAILY-1124 为 BTMS 供应商，均属 BTMS 线、非加热器选型，不撞题；Codex DAILY-1125 为 BTMS 线（选型／容量／制冷量或电池预调节角），本篇为 HVCH 加热器线，产品线不同，不撞题；事实素材＝HVCH 产品页实时核验（系列参数表＋电巴询价提示：注明电池预热、座舱加热或两者兼顾＋场站供电）；大纲＝一台加热器两份活→功率按车定→电压按平台定→控制按整车定→座舱与电池怎么分→要发哪些数字→提防点→FAQ；承接页＝HVCH 产品页＋选型报价页
- 检测路线：路线 A（Peter 2026-11-16 11:12 定，今日派工单重申）：大白话写，测一次 ZeroGPT 两半；过线直接发，不过线当天早上特批直发，不再多问一轮。DeepL 免费额度仍在 17 天冻结期，中转堵死。

## 正文（纯正文版从此开始）

# High Voltage Coolant Heater for Electric Bus: What to Specify Before You Order

An electric bus needs heat in two places. The battery needs it before the bus leaves the depot. The cabin needs it all day. One coolant heater can do both jobs. But only if you specify it for the bus, not for a car.

Most bus buyers come to us with a car heater in mind. The numbers look close. The voltage looks right. Then the bus runs a winter route and the heater falls short. A bus is not a big car. It carries fifty people. It runs sixteen hours. It parks outside overnight. Size the heater for the bus you run, not the car you know.

## Two jobs, one loop

The first job is the battery. A cold battery charges slow and gives back less. Preheating at the depot fixes that before the bus rolls out. The bus leaves warm. That is the whole point of depot preconditioning. Our [BTMS preconditioning guide](https://evbtms.com/electric-bus-btms-preconditioning-depot/) walks through the depot side. The heater is the part that makes the heat.

The second job is the cabin. Fifty people, glass everywhere, doors opening every few minutes. The cabin loses heat fast. A heat pump helps on mild days. Below about -10°C it struggles, and the PTC heater carries the load. That is why buses run a PTC heater even when the brochure talks about heat pumps. The brochure describes October. The heater has to survive January.

One heater can feed both loops. Or you split them. That choice belongs in the specification, not after delivery. Tell us up front: battery preheating, cabin heating, or both. And tell us what depot power you have. Our product page asks bus buyers for exactly those two answers before we quote. Send them with the enquiry and the sizing starts right.

## Power: size it for the coldest morning

Our [A series](https://evbtms.com/products/high-voltage-coolant-heater/) covers 6 to 18 kW. The Q series covers 15 to 35 kW. The E series covers 20 to 24 kW. A city bus on a short loop can live on the small end. A long-route bus in a cold climate cannot. Do not size for the average day. Size for the coldest morning the bus actually sees.

Big vehicles stack heaters. Six 35 kW units on one truck give 210 kW of heating where a single heater cannot reach. Buses stack the same way when one unit is not enough. That is a standard answer to a big number. You do not need a custom heater for a big number. You need more units.

What you do need to get right is the split. Battery preheat wants a fast warm-up before departure. Cabin heat wants steady output all day. If one heater does both, the control has to manage the handover. Our A and Q series run on CAN plus an enable signal, and the vehicle controller coordinates them. Say which job matters more on your route, and we size around it.

## Voltage: match the full window

An 800 V bus is not 800 V all day. Give us the full window: minimum, nominal, maximum. Our A series runs 400 to 800 V. Our Q series runs up to 1100 V. If your window runs past 800 V, say so up front. Do not find out at integration.

The E series runs 400 to 800 V with a thermostat and no CAN. That suits a bus whose thermal control is simple and does not need to talk to the vehicle controller. Most modern bus platforms do talk. Check what your vehicle can speak before you order. A CAN heater on a bus with no CAN bus cannot be controlled. It arrives, it sits in the warehouse. Check the interface first. It takes five minutes and saves a season.

## Cabin heat is not an afterthought

Cabin heating on an electric bus is a [PTC heater](https://evbtms.com/what-is-a-ptc-heater/) job as much as a battery job. The coolant loop carries heat to the cabin heater core the same way it carries heat to the battery. One loop, two loads. The question is how much of the output each load gets on a cold morning, when both want heat at once.

Plan the split before you order. A bus that preheats the battery at the depot has less to do on the road. A bus that parks outside with no depot power needs the heater to do everything while driving. Those are two different heaters. Tell us where the bus sleeps and the answer changes.

The PTC element itself backs off as it warms up. It cannot run away and cook itself. That is the same in a small unit and a big one. What changes with a bus is the duty: long hours, cold starts, doors opening all day. The heater has to hold output hour after hour. Ask for the rated conditions behind any kilowatt number: voltage, coolant, flow rate, inlet temperature. A kilowatt without conditions is not a real number.

## Send us your numbers

Do not start with "how much." A price without numbers is a guess. We do not guess. Send us the numbers below, and we come back with a series, a price, and a sample plan.

- Bus type and route: city loop, long route, or school run. And where the bus sleeps at night.
- Battery preheating, cabin heating, or both. And which one matters more on a cold morning.
- Depot power available for preconditioning.
- Platform voltage: minimum, nominal, maximum. Not just nominal.
- Power need at your coldest operating temperature. Not at room temperature.
- Coolant: what mixture, and what flow rate.
- Inlet temperature and target outlet temperature.
- Control: CAN plus enable, or thermostat.
- Annual volume.
- Installation envelope: the space the heater has to fit in, and where the ports have to point.

[Size it for the coldest day](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/), not the average day. The average day does not need a heater. A buyer sizes the heater for a normal winter day. Then January comes. The cab stays cold. The driver complains. The buyer blames the heater. It was not the heater. It was the sizing.

## What to watch for

Watch for a supplier who quotes you a heater without asking for your numbers. That tells you how they work.

Watch for power quoted without conditions. A kilowatt number means nothing without the voltage, the coolant, the flow rate and the inlet temperature behind it. Ask for the rated conditions. If the supplier cannot give them, the number is not real.

And watch the voltage. Some suppliers quote nominal voltage only. Your platform has a window, not a single number. Match the full window. A heater bought exactly at nominal voltage has no headroom. Leave headroom. Our Q goes to 1100 V. If your window runs past 800 V, say so up front.

We also build the H series. Specifications are provided per project. If your bus sits outside the A, Q and E boxes, ask us about H. It exists for exactly that case. Compare us. We published a [shortlist of manufacturers](https://evbtms.com/high-voltage-coolant-heater-manufacturers/) so you can see how the field looks before you choose.

Our [selection guide](https://evbtms.com/high-voltage-ptc-heater-selection-guide/) walks through voltage, power and control. Use it before you send the numbers. It will tell you which ones you are missing. And if you are still deciding where the heater goes, our [automotive PTC guide](https://evbtms.com/ptc-heater-automotive/) covers cabin and battery placement.

A bus heater is not a car heater with a bigger label. It is a different job. Specify it for the bus. Send us the numbers through our [selection and quote page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). We will build the heater around them. Start with the numbers. Everything else follows.

## FAQ

**How much power does an electric bus heater need?**

It depends on the bus and the route, not on a catalog row. Our A series covers 6 to 18 kW, Q covers 15 to 35 kW, E covers 20 to 24 kW, and big platforms stack units. Send us the bus type, the route, the coldest operating temperature and whether the heater does battery, cabin, or both, and we size it. Our [sizing guide](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/) explains the inputs.

**Can one heater do battery preheating and cabin heating?**

Yes. One coolant loop can feed both. The control has to manage the split on a cold morning, when both want heat at once. Tell us which job matters more on your route. If your bus preheats at the depot, the road load is smaller. Read our [guide to what a PTC heater is](https://evbtms.com/what-is-a-ptc-heater/) first if the basics are new.

**What voltage does an electric bus heater run on?**

Match your platform window, not a single number. Our A series runs 400 to 800 V, Q runs up to 1100 V, E runs 400 to 800 V. Send the minimum, nominal and maximum voltage. If your window runs past 800 V, say so up front.

**CAN or thermostat control for a bus?**

Most modern bus platforms use CAN. Our A and Q series run on CAN plus an enable signal, coordinated by the vehicle controller. The E series uses a thermostat and has no CAN, for simpler thermal control. Check what your vehicle speaks before you order. Our [manufacturer guide](https://evbtms.com/ptc-heater-manufacturer/) covers how to judge a supplier on more than price.

**Does the bus need depot power for preconditioning?**

It helps a lot. Preheating at the depot means the bus leaves warm and the heater does less on the road. Tell us what depot power you have when you enquire. Our [BTMS preconditioning guide](https://evbtms.com/electric-bus-btms-preconditioning-depot/) covers the depot side of the same morning.

## 来源

- EVLINK 高压冷却液加热器产品页（系列参数表 A/Q/E/H、电巴询价提示：注明电池预热、座舱加热或两者兼顾＋场站供电、2021 年起量产、6 台 35kW 并联 210kW）：https://evbtms.com/products/high-voltage-coolant-heater/
- PTC-1110《High Voltage PTC Heater Selection Guide for EVs》（选型指南）：https://evbtms.com/high-voltage-ptc-heater-selection-guide/
- PTC-1111《High Voltage Coolant Heater Sizing for EVs》（配型：流量／温度／功率）：https://evbtms.com/high-voltage-coolant-heater-sizing-evs/
- PTC-1116《What Is a PTC Heater?》（PTC 自限温、CoP 1:1）：https://evbtms.com/what-is-a-ptc-heater/
- PTC-1118《Automotive PTC Heater》（热泵约 -10°C 以下效益下降、座舱＋电池布置）：https://evbtms.com/ptc-heater-automotive/
- BTMS-1023《Will Your Bus Leave the Depot Warm?》（场站预调节）：https://evbtms.com/electric-bus-btms-preconditioning-depot/
- Webasto 800V HVH 巴士方案页（电巴 HVH 5–12kW、250–880V，竞品口径参考）：https://www.webasto.com/en-in/choose-vehicle-solution/bus/heating-solutions.html

## Stage 7 自审（2026-11-25，发布前核验，待发布后补复核）

- 事实核对：与 HVCH 产品页核验逐项一致——A 系 6–18kW／400–800V／CAN+enable／整车控制器协调（CAN）／IP67／-40~85°C／5.1kg；Q 系 15–35kW／400–1100V／CAN+enable／IP67／-40~85°C／12kg；E 系 20–24kW／400–800V／恒温器无 CAN／IP67／-40~85°C／8.5kg；H 系存在、参数按项目提供；2021 年起量产；6 台 35kW 并联 210kW；MOQ／交期／样品流程随询价确认（未编固定数）；热泵约 -10°C 以下效益下降沿用 PTC-1118 v4 已审口径；电巴询价提示（电池预热／座舱加热／两者＋场站供电）引自产品页原文；竞品 Webasto 电巴 HVH 5–12kW 未写入正文，仅列来源作 SERP 背景；无 B 系残留；未编认证、客户案例、测试数据、具体车型适配。
- 标准核对：短句为主；禁用词 delve／furthermore／moreover／in conclusion／it's important to note／whether you're 零命中；em-dash 正文 0 处；段落结构拉开（短段 1–2 句、场景段、说明段交错）；无计数式修辞（项目输入清单为功能性清单，无计数导语）；关键词自然融入（主词标题／首段，集群词 for electric buses／cabin ptc heater 正文融入）。
- 内链：9 条 distinct URL（12 处锚点）全部在正文以 markdown 链接标出锚点；发布后 HTML 复核：前台 9 个不重复 URL 均已渲染（锚点 0–8），10 条清单完整。
- 检测：2026-11-25 08:59–09:03 ZeroGPT 测一次两半，上半 100%（文件 4,565 字符，ZeroGPT 页面显示 4,398 字符／840 词）、下半 100%（文件 4,749 字符，页面显示 4,231 字符／764 词），未过线；按路线 A（Peter 2026-11-16 定、今日派工单重申）当天早上特批直发，未改写、未重测。字符数差异系粘贴时 markdown 链接只取锚文本、URL 未计入，与 PTC-1119 同口径。
- 结论：PASS WITH WARNINGS（警告：ZeroGPT 两半 100% 未过线，按路线 A 特批直发；与 PTC-1116/1117/1118/1119 同一检测关未过模式，DeepL 中转仍在 17 天冻结期）。
- 发布：2026-11-25 09:20（UTC 01:20），post 10645，https://evbtms.com/high-voltage-coolant-heater-electric-bus/ ；slug 发布前核验未占用（wp-json []、前台 404）；分类 Guide（cat 11）；SEO 标题 53 字符、Meta 152 字符，前台 HTML 独立复核一致（browser.open 抓取：标题即 SEO 标题，Description 字段与 Meta 逐字一致，Published 2026-11-25T01:20:36+00:00）；特色图媒体 9422（银色 EVLINK HVCH 实物图，2026-09-16 上传，1536×1024，未当过特色图；禁用的 10406／3186／9918／10297／9475 均未用；10601 因 alt 注明 illustration 已排除）；前台 200、标题与 H1 一致；7 个 H2（含 FAQ）、5 条 FAQ、10 条清单均已渲染。
