# PTC-1118 v4 重写版（Peter 人工化改写标准，2026-11-17 10:38）

- 编号：PTC-1118 v4（PTC 每日一篇，2026-11-18 周三档；v1 大白话、v2 人声、v3 平直口语均 ZeroGPT 100%/100%）
- 主词：ptc heater automotive（美国 50/月、KD 8%、商业型）；slug ptc-heater-automotive（2026-11-17 wp-json 核验 []，未占用）；分类 Guide；SEO Title／Meta 同 v1（49 字符／125 字符）
- 改写依据：Peter 2026-11-17 10:38 发来的《AI文章人工化改写标准》（语言／内容／SEO／最终目标四节）。核心主题不变（车用 PTC 加热器装在哪：驾驶室＋电池）。
- v4 改动（按标准逐条）：
  1. 语言：短句为主、平直用词；去掉 v1/v3 的金句与收尾句（“That's the point”“I've said this before”“A real number. Not a catalog link.” 全部删除）；段落结构拉开（有 1–2 句短段、有场景段、有 4 句说明段，不再每段同一骨架）。
  2. 内容：新增真实应用场景与客户问题——按平均冬天选型到一月不够用的错误、订了 CAN 加热器但车无 CAN 总线的错误、寒冷城市公交车队夜间充电＋早上预热、温和气候与寒冷气候对热泵／PTC 的不同取舍。以上均为通用场景与常见问题，未编具名客户、未编测试数据、未编资质。
  3. 技术解释通俗化：空气／水暖两类、热泵搬热 vs PTC 造热、1:1 上限，均用日常语言讲清。
  4. 事实不变：A 系 6–18kW／400–800V、Q 系 15–35kW／400–1100V、E 系恒温器无 CAN、CoP 1:1、热泵约 -10°C 以下效益下降、-20 选型口径，均与 v1 事实账本一致；未编新数字。
  5. SEO：主词 ptc heater automotive 在标题／首段；high voltage coolant heater、high voltage ptc heater 自然融入正文与内链锚点；H1＋H2 结构保留，FAQ 沿用站内已发布格式（粗体问题）。
- 内链：7 条 distinct URL 与 v1/v3 同一套（选型报价页出现 3 次）；正文以 markdown 链接标出锚点
- 特色图：不重复用已发过的——不用媒体 10406／3186／9918；发布时从媒体库另选一张未用过的 HVCH 实物图；库里没有就先不设特色图（DAILY-1102 先例），事后补记
- 事实账本同 v1（见 REPORTS/PTC-1118-ptc-heater-automotive-draft.md 事实账本）

## 正文（纯正文版从此开始）

# Automotive PTC Heater: Where Does It Go in an EV?

An EV has no engine. That means no waste heat. So the heat has to come from somewhere. In most EVs, it comes from the PTC heater. It goes in two places. The cabin and the battery. Here is [how it works](https://evbtms.com/how-high-voltage-coolant-heater-works/).

## The cabin first

Cold morning. You get in the car. You want warm air, fast. That is the PTC heater's first job.

The same warm air clears the windshield. One heater, two jobs. If the windshield fogs up on a damp morning, the same unit that warms your hands clears the glass.

There are two kinds of PTC heater. Air and water. The air kind sits in the duct and heats the air directly. The water kind heats the coolant, and the coolant heats the air through the heater core. Ours is the water kind. It is a coolant heater. If you need an air heater, that is a different unit. Ask for it by name. Do not assume they are the same.

How big should it be? [Size it for the coldest day](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/). Not the average day. The average day does not need a heater. Here is the mistake I see most often. A buyer sizes the heater for a normal winter day. Then January comes. The cab stays cold. The driver complains. The buyer blames the heater. It was not the heater. It was the sizing.

One unit of electricity makes at most one unit of heat. There is no free heat. So add up what the cab needs at minus 20 and size for that number.

Our [A series](https://evbtms.com/products/high-voltage-coolant-heater/) does 6 to 18 kW on 400 to 800 V. The Q series does 15 to 35 kW up to 1100 V. Pick the one with headroom. A heater that runs at its limit all winter will not last long. Buy the wrong one and you find out in January, not in the showroom.

Then there is the control. Our A and Q run on CAN plus an enable signal. The vehicle controller coordinates them. The E series is different. It uses a thermostat and has no CAN. The heater manages itself. So check what your vehicle can talk to before you order. I have seen the other mistake too. A buyer orders a CAN heater for a vehicle with no CAN bus. The heater arrives. It cannot be controlled. It sits in the warehouse. Check the interface first. It takes five minutes and saves a season.

## The battery

The battery needs heat too. A cold battery does not charge well. It does not give you its full range. So you preheat it. That is the second job of the PTC heater.

Think of a bus fleet in a cold city. The buses charge overnight. In the morning, the batteries are cold. If you start charging a cold battery, it charges slow. Warm it up first and the charge goes faster. The same applies to the range. A cold battery gives you less range. Preheating is not a luxury. It is part of running the vehicle.

It can be the same heater on a different loop. Or it can be a second unit. It depends on the vehicle. Either way, the battery needs its own numbers. Flow rate. Inlet temperature. Target outlet temperature. Give us [those three numbers](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). If a supplier quotes you a heater without asking for them, that tells you something about how they work.

Test it first. Fit it, run it, and check the real outlet temperature. A sample costs little. A wrong batch costs a season. A heater that fails in your loop is a problem for both of us.

## What it cannot do

A PTC heater makes heat. It does not move heat. That is the heat pump's job. They are different jobs, and they do not replace each other.

A heat pump moves heat from outside to inside. In mild weather, one unit of electricity becomes several units of heat. That is a good deal. Below about minus 10, it stops being a good deal. Then the PTC heater takes over. So a vehicle in a mild climate can lean on the heat pump. A vehicle in a cold climate needs both. Anyone who tells you one replaces the other is selling you something. Do not buy that. Compare us. We published a [shortlist of 8 high voltage coolant heater manufacturers](https://evbtms.com/high-voltage-coolant-heater-manufacturers/).

A PTC heater will never be efficient. One unit of electricity makes one unit of heat. That is the physics. Do not buy it for efficiency. Buy it because it works at minus 20 when nothing else does.

And it uses battery power. Every kilowatt of heat is a kilowatt off your range. A warm cab means a shorter range. You cannot have both. Pick the power that keeps the cab warm without killing the range.

## What to send us

Do not start with "how much." Start with your numbers. I need seven things.

- Platform voltage
- Power need
- Coolant flow rate
- Inlet temperature
- Target outlet temperature
- Control type
- Vehicle type and annual volume

Send those through our [selection and quote page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). We will come back with a series, a price, and a sample plan.

## FAQ

**What is an automotive PTC heater?**

It is the heater that warms the cab and preheats the battery in an EV. There is no engine and no waste heat, so something has to make the heat. That is the PTC heater. It backs off by itself as it warms up. It cannot run away and cook itself. The longer version is in our [guide to what a PTC heater is](https://evbtms.com/what-is-a-ptc-heater/).

**Cabin or battery: which first?**

Both need heat. The cab needs it for the driver. The battery needs it to charge and to give range. If you can only do one, do the cab first. Then do the battery. Do not skip the battery. A cold battery costs you range every single day.

**Can a PTC heater replace a heat pump?**

No. They are different jobs. The heat pump moves heat. The PTC heater makes heat. In mild weather, the heat pump wins. At minus 20, the PTC heater wins. Cold places need both.

**What voltage do I need?**

Match your platform. A 400 V vehicle needs a 400 to 800 V heater. An 800 V vehicle needs past 800 V. Our Q goes to 1100 V. Leave headroom. Do not buy exactly at your voltage. Our [selection guide](https://evbtms.com/high-voltage-ptc-heater-selection-guide/) walks through voltage, power and control.

**How do I get a quote?**

Send the seven numbers above. Use our [selection and quote page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). Or write to us. Either way, you get a real number.

## Stage 7 自审（2026-11-17，发布前）

- 事实核对：与 v1 同一套事实（A/Q/E/H 系参数、CoP 1:1、自限温、驾驶室＋电池两处应用、空气／水暖两类、热泵约 -10°C 口径），未新增事实或数字；无 B 系残留；未编认证、MOQ/交期数字、客户案例、测试数据。新增的四处场景（选型错误、接口错误、公交车队、气候取舍）均为通用场景与常见问题，未具名、未编数。
- 标准核对：短句为主；禁用词 delve／furthermore／moreover／in conclusion／it's important to note／whether you're 零命中；em-dash 0 处；段落结构拉开（短段 1–2 句、场景段、说明段交错）；无空洞总结段；关键词自然融入（ptc heater automotive 标题／首段，high voltage coolant heater 内链锚点）。
- 内链：7 条 distinct URL 全部在正文以 markdown 链接标出锚点（选型报价页出现 3 次，URL 同一）。
- 检测：2026-11-17 10:39–10:40 ZeroGPT 测一次两半，上半 100%（2,963 字符／581 词）、下半 100%（2,814 字符／536 词），仍未过。结论：按人工化标准重写（场景＋结构拉开）未改变分数；v1/v3/v4 全败，写法改不动分数。
- 结论：PASS WITH WARNINGS（警告：热泵约 -10°C 以下效益下降一处以社媒 #40 稿口径为准，未独立核验；其余事实均有来源）。
