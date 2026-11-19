# PTC-1118《Automotive PTC Heater: Where Does It Go in an EV?》初稿（Peter 说话方式版）

- 编号：PTC-1118（PTC 每日一篇，2026-11-18 周三档；本周三档，提前写就，待 Peter 看过后定发不发）
- 主词：ptc heater automotive（美国 50/月、KD 8%、商业型；关键词分类总表-2026-11-13.md，2026-11-13 核查）
- 同簇词：high voltage heater（40/月、KD 7%）；custom high voltage ptc heater（20/月）；high voltage ptc heater manufacturer（10/月）已由 PTC-1117 承接
- 意图：商业型——买家在找车用 PTC 加热器，要知道它装在哪、管什么、怎么选
- 选题简报链：目标客户（电车／电巴／重卡热管理采购与工程师，找车用 PTC 加热器）→ 关键词数据（上）→ 意图（应用＋选型）→ SERP 验证（见下）→ 查重（管线表无 PTC-1118、无 ptc heater automotive 旧题；与 PTC-1110 选型、PTC-1111  sizing、PTC-1116 是什么、PTC-1117 厂家均不撞题；本篇是“装在哪、管什么”应用篇）→ 事实账本（见文末）→ 大纲（见下）→ 产品页与询价入口（HVCH 产品页＋选型报价页）
- SERP 验证（2026-11-17，铁律先行）：前排是 Guchen《What Is a PTC Heater? PTC Meaning & Applications in EVs》（教科书式定义＋应用：驾驶室供暖＋电池预热；空气 PTC 与水暖 PTC 两类；CoP 1:1 对热泵 1:2–1:3）、Nanfeng 产品页（冷却液加热器／空气加热器，应用含驾驶室供暖、挡风玻璃除霜除雾、电池预热）、老站 evptc.com Q 系产品页。缺口＝没有一篇站在买家角度、用大白话讲“它装在哪、管什么、不能干什么”的指南，各家只贴定义或规格。本篇即补此缺口。
- 写作路线：Peter 说话方式版（Peter 2026-11-17 09:44 令：“用我说话的方式去写文章，你学习下”）。学法：读他本人的消息原话（主聊＋本聊＋社媒旁聊），不是学他正式英式书面文（PTC-1116 他自改版是 whilst／utilise 正式英式文体，那是写，不是说；本次学的是他“说话”的方式）。
- Peter 说话方式（从原话提炼，逐条有出处）：
  1. 句子极短，经常 2–6 个字就一句（“继续”“发吧”“你写的文章呢”“今天工作安排？”），没有铺垫，开口就是事本身。
  2. 直接下判断，不绕弯（“完成的就完成，不要搞错了”“发不 后面不要做视频了”“先做第1个”）。
  3. 用问句当工具（“为什么要换图呢”“是不是写的太ai了……是吧”“你这个大白话是不是不够呢”），问完就给答案或命令。
  4. 命令式，不给建议给动作（“装插件换图”“写 CAN 协调”“再想想”“给我新的文章”）。
  5. 重要的事重复一遍（“完成的就完成，不要搞错了”；“以后所有的事情都必须放到上午完成，下午我有其他项目事情需要做”——规则＋一句原因，不多解释）。
  6. 自称“我”，不用“我们”（“用我说话的方式”“你也跟我这么久说话了”）。
  7. 不用过渡词，不用“首先／其次／总之”，不解释自己。
  8. 英文落点：短句为主、长短不一；“I” 不用 “we”；开口就是结论；判断直接（That's wrong. Don't.）；问句当工具（Why would you…? Right?）；命令式（Check… Send…）；重要的重复一遍；规则＋一句原因；不用过渡词、不用对仗句式、不用编号标题。
- 分类：Guide；slug 拟 ptc-heater-automotive（2026-11-17 wp-json 核验 []，未占用）
- SEO Title：Automotive PTC Heater: Where Does It Go in an EV?（49 字符）
- Meta 描述：Where does the PTC heater go in an EV? The cabin and the battery. What each one needs, and what to send us for a real quote.（125 字符）
- 特色图：不重复用已发过的——不用媒体 10406（PTC-1111）、不用媒体 3186（PTC-1116）、不用媒体 9918（PTC-1117）；发布时从媒体库另选一张未用过的 HVCH 实物图；库里没有就先不设特色图（DAILY-1102 先例），事后补记
- 内链（7 条，与 v1 同 URL，正文中以 markdown 链接标出锚点）：HVCH 产品页 /products/high-voltage-coolant-heater/、选型报价页 /high-voltage-coolant-heater-selection-quote/（出现 3 次）、制造商清单页 /high-voltage-coolant-heater-manufacturers/、PTC-1116 /what-is-a-ptc-heater/、PTC-1110 /high-voltage-ptc-heater-selection-guide/、PTC-1111 /high-voltage-coolant-heater-sizing-evs/、HVCH 原理文 /how-high-voltage-coolant-heater-works/

## 大纲

1. 短答案：装在哪——驾驶室，电池，就这两处
2. 驾驶室：冷天按最冷天选、1:1 上限、A/Q/E 三系怎么挑、控制接口
3. 电池：预热为什么、三个回路数字、先拿样品
4. 它不能干什么：制热不搬热、热泵与 PTC 各干各的、-10°C 以下 PTC 接手、效率 1:1 是物理规律、取暖要耗续航
5. 发给我们七项输入
6. FAQ（5 问）

## 正文（纯正文版从此开始）

# Automotive PTC Heater: Where Does It Go in an EV?

Where does the PTC heater go in an EV? Two places. The cabin. The battery. That's it.

No engine in an EV. No waste heat. So the heater has to make all the heat itself. That's what the PTC heater does. Here's [how it works](https://evbtms.com/how-high-voltage-coolant-heater-works/).

## The cabin

This is the one everyone knows. Cold morning, you get in, you want warm air. The PTC heater makes it. Same warm air clears the windshield. One heater, two jobs in the cab.

Two kinds. Air and water. Air heats the air in the duct. Water heats the coolant, and the coolant heats the air. Ours is water. Coolant. That's the one this guide is about. If you need an air heater, that's a different unit.

[Size it for the coldest day](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/). Not the average day. Why would you size it for the average day? The average day doesn't need a heater. The coldest day does.

One unit of electricity makes at most one unit of heat. That's the limit. No free heat. So add up what the cab needs at minus 20 and size for that. Size it small and the cab stays cold in January. That's on the sizing, not the heater.

Our [A series](https://evbtms.com/products/high-voltage-coolant-heater/) does 6 to 18 kW on 400 to 800 V. Q does 15 to 35 kW up to 1100 V. Pick the one with headroom. Don't buy a heater rated exactly at your platform voltage. Buy the one with room to spare. Buy the wrong one and you find out in January. Not in the showroom. I've said this before. I'll say it again. A heater running at its limit all winter will not last.

Control. Our A and Q run on CAN plus an enable signal. The vehicle controller coordinates them. E is different. Thermostat. No CAN. The heater manages itself. If your vehicle doesn't talk CAN, E is the one. Check what your vehicle can talk to before you order. A heater with the wrong interface is a paperweight. An expensive one.

## The battery

The battery needs heat too. A cold battery doesn't charge well. It doesn't give you its full range either. So you preheat it. That's the second job.

Preheat before you charge. A cold battery charges slow. Warm it up first and the charge goes faster.

Same heater, different loop. Or a second unit. Depends on the vehicle. Either way, the battery needs its own numbers. Flow rate. Inlet temperature. Target outlet temperature. Give us [those three numbers](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). If a supplier quotes you a heater without asking for them, that tells you something about how they work.

Test it first. I want you to. Fit it, run it, check the real outlet temperature. A sample costs little. A wrong batch costs a season. A heater that fails in your loop is a problem for both of us.

## What it doesn't do

A PTC heater makes heat. It doesn't move heat. That's the heat pump's job. Different jobs.

A heat pump moves heat from outside to inside. Mild weather, one unit of electricity becomes several units of heat. Good deal. Below about minus 10, it stops being a good deal. That's when the PTC heater takes over. Cold places need both.

Anyone who tells you one replaces the other is selling you something. Don't buy that. Don't take my word for it either. Compare us. We published a [shortlist of 8 high voltage coolant heater manufacturers](https://evbtms.com/high-voltage-coolant-heater-manufacturers/).

And the PTC heater will never be efficient. One to one. That's the physics. Don't buy it for efficiency. Buy it because it works at minus 20 when nothing else does. That's the point.

One more thing. The PTC heater eats battery. One to one. Every kilowatt of heat is a kilowatt off your range. That's the trade. Warm cab, shorter range. You can't have both. Pick the power that keeps the cab warm without killing the range.

## What to send us

Don't start with "how much." Start with your numbers. I need seven things. That's it.

- Platform voltage
- Power need
- Coolant flow rate
- Inlet temperature
- Target outlet temperature
- Control type
- Vehicle type and annual volume

Send those through our [selection and quote page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). We'll come back with a series, a price, and a sample plan. A real number. Not a catalog link.

## FAQ

**What is an automotive PTC heater?**

It's the heater that warms the cab and preheats the battery in an EV. No engine, no waste heat, so something has to make the heat. That's the PTC heater. It backs off by itself as it warms up. It can't run away and cook itself. The longer version is in our [guide to what a PTC heater is](https://evbtms.com/what-is-a-ptc-heater/).

**Cabin or battery: which first?**

Both need heat. The cab needs it for the driver. The battery needs it to charge and to give range. If you can only do one, do the cab first. Then do the battery. Don't skip the battery. A cold battery costs you range every single day.

**Can a PTC heater replace a heat pump?**

No. Different jobs. The heat pump moves heat. The PTC heater makes heat. Mild weather, the heat pump wins. Minus 20, the PTC heater wins. Cold places need both.

**What voltage do I need?**

Match your platform. 400 V vehicle, 400 to 800 V heater. 800 V vehicle, you need past 800 V. Our Q goes to 1100 V. Leave headroom. Don't buy exactly at your voltage. Our [selection guide](https://evbtms.com/high-voltage-ptc-heater-selection-guide/) walks through voltage, power and control.

**How do I get a quote?**

Send the seven numbers above. Use our [selection and quote page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). Or write to us. Either way, you get a real number.

## 事实账本（只用已核实数）

- 主词 ptc heater automotive：美国 50/月、KD 8%、商业型（关键词分类总表-2026-11-13.md，2026-11-13 核查）
- 同簇：high voltage heater 40/月、KD 7%；custom high voltage ptc heater 20/月（同表）
- 应用两处：驾驶室供暖＋电池预热（Guchen《What Is a PTC Heater?》2026-06-11；PTC-1116 已用）；挡风玻璃除霜除雾属驾驶室暖风同一路（Nanfeng 产品页 SERP 2026-11-17）
- 空气 PTC 与水暖 PTC 两类：空气直接加热风道内空气；水暖加热冷却液再经加热器芯换热（Guchen）；EVLINK HVCH 是冷却液加热器（水暖），即本篇所指
- PTC 自限温原理＋CoP 上限 1:1（TI 设计指南，PTC-1116 已用；Guchen 同口径：PTC 约 1:1，热泵约 1:2–1:3）；电车无发动机余热（TI）
- 冷电池性能下降（Guchen：“Battery performance decreases significantly at low temperatures”；定性表述，未编数字）
- PTC 耗电量大、取暖耗续航（Guchen：“PTC heating converts electrical energy directly into heat, resulting in considerable battery power consumption”；定性表述，未编数字）
- 热泵约 -10°C 以下效益下降（社媒 #40 稿同口径“Below about -10°”，本稿未独立核验，以“约”表述）
- EVLINK A 系 6–18kW／400–800V／CAN+enable、Q 系 15–35kW／400–1100V／CAN+enable、E 系 20–24kW／400–800V／恒温器无 CAN、H 系存在参数按项目给（Peter 2026-11-12／11-13 定）
- 未写：EVLINK HVCH 认证宣称（无核实来源，不写）；HVCH 的 MOQ／交期数字（无核实来源，只写“问厂家要书面确认”）；具名客户案例（无）；NTC／HVIL（那是 T8 制动电阻的事实，不移用到 HVCH）；无 B 系加热器（B 是接插件变体，非加热器系列）
- 内链 7 条与 v1 同 URL（2026-11-17 v1 已 curl 逐个核验 200）；本稿锚点见正文 markdown 链接
- slug ptc-heater-automotive 2026-11-17 wp-json 核验 []，未占用

## Stage 7 自审（2026-11-17，发布前）

- 事实核对：A/Q/E/H 系参数与 REPORTS/hvch-series-parameters-recon-2026-11-09.md 一致；应用两处（驾驶室＋电池）与 Guchen／PTC-1116 一致；空气／水暖两类与 Guchen 一致；CoP 1:1 与自限温原理有来源（TI 设计指南，PTC-1116 已用）；无 B 系残留；未编 EVLINK 认证、MOQ/交期数字、客户案例。
- 观点类表述核查：以下均为观点／建议，非事实宣称——“别买正好卡电压的”“拿不到三个回路数字的厂家有问题”“一个顶替另一个就是在卖东西”“宁可丢单也不卖不匹配的加热器”（v2 句式，本稿未用）“取暖要耗续航、两者不可兼得”（定性权衡，有 Guchen 耗电来源）；未以观点冒充实测数据。
- 语音核查（本稿自查）：第一人称 “I” 贯穿（I need／I've said／I want you to／Don't take my word for it）；短句为主、长短拉开；无编号标题（唯一清单是文末 7 项询价输入）；无 “X is not Y. It is Z.” 对仗句式；禁用词 delve／furthermore／moreover／in conclusion／it's important to note／whether you're 零命中；em-dash 0 处。
- 内链：7 条 distinct URL 全部在正文以 markdown 链接标出锚点（选型报价页出现 3 次，URL 同一）。
- 结论：PASS WITH WARNINGS（警告：热泵约 -10°C 以下效益下降一处以社媒 #40 稿口径为准，未独立核验；其余事实均有来源）。
