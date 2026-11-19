# PTC-1117《PTC Heater Manufacturer: How to Pick One for Your EV Project》重写 v2

- 编号：PTC-1117（PTC 每日一篇，2026-11-17 周二档；v1 已于 2026-11-17 09:06 上线 post 10576，本文件为重写版，待替换上线）
- 主词：ptc heater manufacturer（美国 40/月、KD 11%、商业型；关键词分类总表-2026-11-13.md，2026-11-13 核查）
- 同簇词：custom high voltage ptc heater（20/月）、high voltage ptc heater manufacturer（10/月）、high voltage ptc heater supplier（10/月）；问题词 what is a ptc heater（260/月）已由 PTC-1116 承接，本篇只作一句话回答＋内链，不重复建页
- 意图：商业型——买家在找 PTC 加热器厂家，要比选、要报价，不是科普
- 改写原因（Peter 2026-11-17 09:24）：v1 大白话版仍显 AI，ZeroGPT 两半 100% / 100%。问题在骨架和腔调，不在句子长短——① 全文数着来（三件事／五项检查／五个红灯／七项输入）；② “X is not Y. It is Z.” 对仗句式重复；③ 每句 6–12 词、整篇一个节奏；④ 全是安全正确的废话，无带刺观点、无车间真细节；⑤ FAQ 定义段是教科书口吻。
- 改写规则（本次执行）：① 不数着来——全篇唯一清单是文末 7 项询价输入（真清单）；“五项检查”“五个红灯”改写成流动段落，标题去编号；② 全文禁用 “X is not Y. It is Z.” 对仗句式，禁用三连排比祈使；③ 句子长短拉开（25 词以上长句＋3–5 词碎句混用）；④ 每节一句带刺的观点；⑤ 对一个人说话（you / we），口语化；⑥ FAQ 用“人解释”的口吻，不用教科书定义。
- 不变项（与 v1／线上版完全一致）：slug ptc-heater-manufacturer；H1 标题 "PTC Heater Manufacturer: How to Pick One for Your EV Project"；SEO Title "PTC Heater Manufacturer: How to Pick the Right One for Your EV"（65 字符）；Meta 描述 154 字符（见下）；分类 Guide；特色图媒体 9918（evlink-hvch-laboratory-product-photo.jpg）；主词；7 条内链（锚点见正文 markdown 链接，URL 与 v1 一致）。
- SEO Title：PTC Heater Manufacturer: How to Pick the Right One for Your EV（65 字符）
- Meta 描述：Looking for a PTC heater manufacturer? Check voltage, power, control, and test data first. A short guide from EVLINK, with a 7-point RFQ checklist.（154 字符）
- 内链（7 条，与 v1 同 URL，正文中以 markdown 链接标出锚点）：HVCH 产品页 /products/high-voltage-coolant-heater/、选型报价页 /high-voltage-coolant-heater-selection-quote/（出现 2 次）、制造商清单页 /high-voltage-coolant-heater-manufacturers/、PTC-1116 /what-is-a-ptc-heater/、PTC-1110 /high-voltage-ptc-heater-selection-guide/、PTC-1111 /high-voltage-coolant-heater-sizing-evs/、HVCH 原理文 /how-high-voltage-coolant-heater-works/

## 正文（纯正文版从此开始）

# PTC Heater Manufacturer: How to Pick One for Your EV Project

You need a PTC heater for an EV, so you search "ptc heater manufacturer" and get a wall of supplier pages, and honestly, most of them look the same — same specs, same promises, same photos.

So how do you tell them apart? A good manufacturer matches your voltage and power and your control interface, and can prove it with test data before you pay. That's it. If any of that's missing, keep looking.

## Figure out your own numbers first

Most people call us and ask for a price first. We can't give one. Not yet. A 400-volt truck and an 800-volt bus are not the same job, and the price depends on which one you're building. So before you open a single catalog, write down your own numbers.

Voltage comes first. Our A series runs 6 to 18 kW on 400 to 800 V, Q runs 15 to 35 kW up to 1100 V. If your platform is 800 V, don't buy a heater rated exactly at 800 V. Buy the one with headroom. A heater running at its limit all winter will not last, and you'll be the one finding out in January.

Then power. Size it for the coldest day, not the average one. PTC heat has a hard limit: one unit of electricity makes at most one unit of heat. If your cab and your battery both need heat at minus 20, add the two loads up and size for that.

Your coolant loop matters just as much, and a [PTC coolant heater](https://evbtms.com/how-high-voltage-coolant-heater-works/) lives inside it, so it needs your [flow rate, inlet temperature and target outlet temperature](https://evbtms.com/high-voltage-coolant-heater-sizing-evs/). Give a manufacturer those numbers. If they quote you a heater without asking for them, that tells you something about how they work.

And control. This one gets skipped more than any other. Our A and Q series run on CAN plus an enable signal, the vehicle controller coordinates them. Our E series runs on a thermostat, no CAN. So check what your vehicle can actually talk to before you order. A heater with the wrong interface is a paperweight. An expensive one.

## What to look for before you shortlist anyone

Now check whether their range actually covers your platform. Look for a real series table with power steps, voltage steps and control options. If the table is thin, the engineering behind it is usually thin too.

Control is next, and it's the question that separates the real suppliers from the ones who just forward you a catalog. CAN or thermostat, and what happens when the vehicle controller sends nothing? A manufacturer who knows their product answers that in one mail. If you get the catalog back a second time, you have your answer.

Then test data. Brochure numbers are cheap. Ask what they test and how, then ask for the report on the unit you will actually buy. If they won't share it, you're buying blind.

Samples. This is the one I'd never skip. Fit it, run it, check the real outlet temperature. A sample costs little. A wrong batch costs a season.

And get the commercial stuff in writing: MOQ, lead time, support. A price on its own doesn't tell you when anything arrives.

## What the big names do well

The top results for this search are all manufacturers, and each of them does something right.

KLC in Taiwan has been building PTC heaters since 1982, they hold IATF 16949, and their range runs from 12 V to 800 V. What I respect is the range and the paperwork: documented certs, not just a claim on a web page. That's the bar for a serious supplier.

Nanfeng in Hebei builds 10, 15 and 20 kW coolant heaters at 350 and 600 V, and they've been making vehicle heaters for more than 30 years. What they do well is simpler: clear power steps.

What none of these pages do is teach you how to match a heater to your loop. They show specs, not the matching.

One more thing: a 2026 market report on water PTC heaters lists Suzhou EVLINK Electronic Technology Co., Ltd. among the profiled producers. We're on that list. We're also the ones writing this guide. If that makes you skeptical, good. Go compare us against the field. We published a [shortlist of 8 high voltage coolant heater manufacturers](https://evbtms.com/high-voltage-coolant-heater-manufacturers/).

## How we do it at EVLINK

We build [high voltage coolant heaters](https://evbtms.com/products/high-voltage-coolant-heater/) in three series, plus a fourth per project. I'll be honest about what each one is for.

A series is 6 to 18 kW on 400 to 800 V, CAN plus enable. Q goes bigger, 15 to 35 kW up to 1100 V, CAN plus enable. E is different: 20 to 24 kW, 400 to 800 V, thermostat control, no CAN at all. And H series exists. We spec it per project, so tell us the vehicle and we'll tell you if H fits.

The E series is simpler, no CAN, the heater manages itself, but you give up the vehicle controller doing the thinking. So if your controller already manages heat, don't buy the E. You'll regret it the first time you want the controller to do the thinking.

When you write to us, don't start with "how much." Start with your numbers. That's enough for a real quote.

## When to walk away

Some suppliers you should just walk away from.

If they won't share test data, walk away. That's the big one. A manufacturer who won't show you how their heater performs is asking you to trust them on faith.

If they have one power rating for every vehicle, that's a supplier selling you what's on the shelf.

Then the sample. If they want a batch order before you've held the unit, that's a supplier in a hurry. A real manufacturer wants you to test it first, because a heater that fails in your loop is a problem for both of us.

If the quote has no MOQ and no lead time in writing, you're going to find out both too late. Same with certifications: ask for the certificate number. A real cert has one.

## FAQ

**What is a PTC heater?**

It's a heater that backs off by itself. The hotter it gets, the more its resistance climbs, so it draws less current as it warms up. It can't run away and cook itself. That's why EVs use it for cabin heat and battery preheating: there's no engine waste heat in an EV, so the heater has to make all the heat itself. The longer version is in our [guide to what a PTC heater is](https://evbtms.com/what-is-a-ptc-heater/).

**What voltage PTC heater do I need?**

Match your platform, and leave yourself room. A 400 V vehicle takes a heater rated for 400 to 800 V. An 800 V vehicle needs one rated past 800 V, and our Q goes to 1100 V. Don't buy a heater rated exactly at your platform voltage. That's running it at its limit from day one. Our [selection guide](https://evbtms.com/high-voltage-ptc-heater-selection-guide/) walks through voltage, power and control.

**CAN or thermostat control?**

It depends on your vehicle, and honestly, on who you want doing the thinking. If your vehicle controller manages heat, take CAN. Our A and Q series run on CAN plus an enable signal. If you'd rather the heater managed itself, take a thermostat. Our E series does that, no CAN. Decide before you order, because that's not something a software update fixes.

**Can I order a custom high voltage PTC heater?**

Yes. Custom power and voltage are normal in this business, and our H series is built per project. Send us your voltage, power, flow, temperatures and control type, and we'll tell you what fits. If it doesn't fit anything we build, we'll say so. We'd rather lose an order than sell you a heater that doesn't work in your loop.

**How do I get a quote from EVLINK?**

Use our [selection and quote page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). It asks for those seven inputs, nothing more. Or write to us with the same list, and you'll get a real number.

## Send us these seven inputs

- Platform voltage
- Power need
- Coolant flow rate
- Inlet temperature
- Target outlet temperature
- Control type
- Vehicle type and annual volume

Send them through our [selection and quote page](https://evbtms.com/high-voltage-coolant-heater-selection-quote/). We'll come back with a series, a price, and a sample plan.

## 事实账本（与 v1 相同，只用已核实数）

- 主词 ptc heater manufacturer：美国 40/月、KD 11%、商业型（关键词分类总表-2026-11-13.md，2026-11-13 核查）
- 同簇：custom high voltage ptc heater 20/月；high voltage ptc heater manufacturer 10/月；high voltage ptc heater supplier 10/月（同表）
- KLC：台湾，1982 年起做 PTC，IATF 16949，电压 12V–800V，OEM/ODM（ptc-heater.com.tw，SERP 2026-11-17；本稿未独立二次核验，以 v1 引用来源为准）
- Nanfeng：10/15/20kW，350/600V，车用加热器 30 年以上（hvh-heater.com，SERP 2026-11-17；本稿未独立二次核验，以 v1 引用来源为准）
- 2026 年水暖 PTC 加热器市场报告把 Suzhou EVLINK Electronic Technology Co., Ltd. 列入重点厂商（marketresearch.com，SERP 2026-11-17；本稿未独立二次核验，以 v1 引用来源为准）
- EVLINK A 系 6–18kW／400–800V／CAN+enable、Q 系 15–35kW／400–1100V／CAN+enable、E 系 20–24kW／400–800V／恒温器无 CAN、H 系存在参数按项目给（Peter 2026-11-12／11-13 定）
- PTC 自限温原理＋CoP 上限 1:1（TI 设计指南，PTC-1116 已用）；电车无发动机余热（TI）
- 未写：EVLINK HVCH 认证宣称（无核实来源，不写）；HVCH 的 MOQ／交期数字（无核实来源，只写“问厂家要书面确认”）；具名客户案例（无）；NTC／HVIL（那是 T8 制动电阻的事实，不移用到 HVCH）；无 B 系加热器（B 是接插件变体，非加热器系列）
- 内链 7 条与 v1 同 URL（2026-11-17 v1 已 curl 逐个核验 200）；本稿锚点见正文 markdown 链接
- slug ptc-heater-manufacturer（已上线 post 10576，v2 为替换版，不改 slug）

## Stage 7 自审（2026-11-17，重写版，发布前）

- 事实核对：A/Q/E/H 系参数与 REPORTS/hvch-series-parameters-recon-2026-11-09.md 一致；无 B 系残留；未编 EVLINK 认证、MOQ/交期数字、客户案例；CoP 1:1 与自限温原理有来源（TI 设计指南，PTC-1116 已用）；“E 系更简单”仅指无 CAN、恒温器自管，未写价格比较（无价格来源）。
- 观点类表述核查：以下均为观点／建议，非事实宣称——“别买正好卡 800V 的”“拿不到测试数据就走人”“不会发样品的厂家在赶时间”“宁可丢单也不卖不匹配的加热器”；未以观点冒充实测数据。
- 语音核查（正文实测，2026-11-17，脚本核验）：正文 1,406 词（body 块全量计数，含标题/FAQ/清单；按节求和 1,370 词），117 句，平均 12.0 词/句；句长分布 1–3 词 10 句、4–5 词 11 句、6–8 词 24 句、9–12 词 24 句、13–18 词 30 句、19–24 词 13 句、25 词以上 5 句（最长 29 词正文句）；禁用词 delve／furthermore／moreover／in conclusion／it's important to note／whether you're 零命中；“X is not Y. It is Z.” 对仗句式零命中（"is not" 零命中，". It is" 句首零命中）；三连排比祈使零命中（Ask 开头句仅 1 句）；编号标题零个（仅文末 7 项询价输入一个真清单，项目符号 7 行、编号列表 0 行）；em-dash 正文 1 处（开篇一句，与 Peter 认可的样例一致）；数词核查：three 1 次（three series，产品事实）、five 0 次、seven 2 次（均指文末唯一清单）。
- 内链：7 条 distinct URL 全部在正文以 markdown 链接标出锚点（选型报价页出现 2 次，URL 同一；正文链接共 8 处）。
- 结论：PASS WITH WARNINGS（警告同 v1：KLC／Nanfeng／市场报告三处事实以 v1 引用来源为准，未独立二次核验）。

## 检测记录（v2，2026-11-17）

- 2026-11-17 09:42–09:43 测一次 ZeroGPT 两半（原文原样）：上半 100%（2,938 字符）、下半 100%（4,519 字符），均未过 ≤30% 线。
- 结论：人声重写版亦未过。与 v1 大白话版（100%/100%）、Peter 手改版（97.6%/94.5%）一致——ZeroGPT 对这类技术说明文一律判高分，写法改不动分数。文章已按路线 A 上线，不再改写、不再重测。
