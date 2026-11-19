# PTC-1118 v3 重写版（平直口语写法，Peter 自写段 32.5% 证据）

- 编号：PTC-1118 v3（PTC 每日一篇，2026-11-18 周三档；v1＝大白话版、v2 概念已并入本稿写法）
- 主词：ptc heater automotive（美国 50/月、KD 8%、商业型）；slug ptc-heater-automotive（2026-11-17 wp-json 核验 []，未占用）；分类 Guide；SEO Title／Meta 同 v1（49 字符／125 字符）
- 重写依据（Peter 2026-11-17 10:08 截图）：他自己写的一段（2024 韩国汽车零部件展）ZeroGPT 32.5%，与我的 100% 差 67 分。截图显示：被标黄的是开头两句打磨过的营销句（stunning appearance／showcasing its latest innovative achievements in the field of…）；后面平直短句（We are capable of doing this well. We continuously refine and test the product.）不标黄。他的正式英式书面版（PTC-1116）97.6% vs 平直口语段 32.5%——分高低的不是文体，是书面语打磨出来的那股劲。
- v3 写法改动（单变量：只换写法，事实、结构、内链全部不变）：
  1. 全称形式，不用缩写（That is／Do not／It is／Here is；Peter 自写段全篇无缩写）
  2. 去掉所有打磨过的金句与收尾句（v1 的 “That's the point”“I've said this before. I'll say it again.”“A paperweight. An expensive one.” 全部删除）
  3. 去掉反差对仗与收尾反转（“That's on the sizing, not the heater”→“That is a sizing problem, not a heater problem.”；“A real number. Not a catalog link.” 删除）
  4. 句子改回完整平直陈述，不用碎片收尾（“No free heat.”→“There is no free heat.”）
  5. 保留：第一人称 I、短句、7 项询价输入唯一清单、7 条内链（与 v1 同 URL）
- 事实账本同 v1（见 REPORTS/PTC-1118-ptc-heater-automotive-draft.md 事实账本）；未新增任何事实或数字
- 特色图：不重复用已发过的——不用媒体 10406／3186／9918；发布时从媒体库另选一张未用过的 HVCH 实物图；库里没有就先不设特色图（DAILY-1102 先例），事后补记

## 正文（纯正文版从此开始）

# Automotive PTC Heater: Where Does It Go in an EV?

Where does the PTC heater go in an EV? It goes in two places. The cabin and the battery.

There is no engine in an EV. There is no waste heat. So the heater has to make all the heat itself. That is the job of the PTC heater. Here is [how it works](https://evbtms.com/how-high-voltage-coolant-heater-works/).

## The cabin

This is the one everyone knows. On a cold morning you get in the car and you want warm air. The PTC heater makes the warm air. The same warm air clears the windshield. One heater does both jobs in the cab.

There are two kinds. Air and water. The air kind heats the air in the duct. The water kind heats the coolant, and the coolant heats the air. Ours is the water kind. It is a coolant heater. That is what this guide is about. If you need an air heater, that is a different unit.

[Size it for the coldest day](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/). Do not size it for the average day. The average day does not need a heater. The coldest day does.

One unit of electricity makes at most one unit of heat. That is the limit. There is no free heat. So add up what the cab needs at minus 20 and size the heater for that. If you size it small, the cab stays cold in January. That is a sizing problem, not a heater problem.

Our [A series](https://evbtms.com/products/high-voltage-coolant-heater/) does 6 to 18 kW on 400 to 800 V. The Q series does 15 to 35 kW up to 1100 V. Pick the one with headroom. Do not buy a heater rated exactly at your platform voltage. Buy the one with room to spare. If you buy the wrong one, you will find out in January. You will not find out in the showroom. A heater that runs at its limit all winter will not last long.

Control. Our A and Q run on CAN plus an enable signal. The vehicle controller coordinates them. The E series is different. It uses a thermostat. It has no CAN. The heater manages itself. If your vehicle does not talk CAN, the E series is the one. Check what your vehicle can talk to before you order. A heater with the wrong interface will not work in your vehicle.

## The battery

The battery needs heat too. A cold battery does not charge well. It does not give you its full range either. So you preheat the battery. That is the second job.

Preheat the battery before you charge it. A cold battery charges slow. Warm it up first and the charge goes faster.

It can be the same heater on a different loop. Or it can be a second unit. It depends on the vehicle. Either way, the battery needs its own numbers. Flow rate. Inlet temperature. Target outlet temperature. Give us [those three numbers](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). If a supplier quotes you a heater without asking for them, that tells you something about how they work.

Test it first. Fit it, run it, and check the real outlet temperature. A sample costs little. A wrong batch costs a season. A heater that fails in your loop is a problem for both of us.

## What it doesn't do

A PTC heater makes heat. It does not move heat. Moving heat is the heat pump's job. They are different jobs.

A heat pump moves heat from outside to inside. In mild weather, one unit of electricity becomes several units of heat. That is a good deal. Below about minus 10, it stops being a good deal. Then the PTC heater takes over. Cold places need both.

If someone tells you one replaces the other, they are selling you something. Do not buy that. Do not take my word for it either. Compare us. We published a [shortlist of 8 high voltage coolant heater manufacturers](https://evbtms.com/high-voltage-coolant-heater-manufacturers/).

A PTC heater will never be efficient. One to one. That is the physics. Do not buy it for efficiency. Buy it because it works at minus 20 when nothing else does.

The PTC heater uses battery power. One to one. Every kilowatt of heat is a kilowatt off your range. That is the trade. A warm cab means a shorter range. You cannot have both. Pick the power that keeps the cab warm without killing the range.

## What to send us

Do not start with "how much." Start with your numbers. I need seven things. That is all.

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

- 事实核对：与 v1 同一套事实（A/Q/E/H 系参数、CoP 1:1、自限温、驾驶室＋电池两处应用、空气／水暖两类、热泵约 -10°C 口径），未新增事实或数字；无 B 系残留；未编认证、MOQ/交期数字、客户案例。
- 语音核对（v3 自查）：全称形式（That is／Do not／It is／Here is／cannot／will not），缩写 0 处；打磨金句／收尾句 0 处；编号标题 0 处（唯一清单是文末 7 项询价输入）；禁用词 delve／furthermore／moreover／in conclusion／it's important to note／whether you're 零命中；em-dash 0 处。
- 内链：7 条 distinct URL 全部在正文以 markdown 链接标出锚点（选型报价页出现 3 次，URL 同一）。
- 检测：2026-11-17 10:10–10:11 ZeroGPT 测一次两半，上半 100%（2,560 字符／510 词）、下半 100%（2,770 字符／527 词），仍未过。结论：平直写法未改变分数，写法单变量假设被证伪（v1 大白话、v2 人声、v3 平直口语全败）；唯一证实过线的仍是 DeepL 中转（T8-11 1.9%/3.5%）。
- 结论：PASS WITH WARNINGS（警告：热泵约 -10°C 以下效益下降一处以社媒 #40 稿口径为准，未独立核验；其余事实均有来源）。
