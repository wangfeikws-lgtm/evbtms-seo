# PTC-1117《PTC Heater Manufacturer: How to Pick One for Your EV Project》初稿

- 编号：PTC-1117（PTC 每日一篇，2026-11-17 周二档）
- 主词：ptc heater manufacturer（美国 40/月、KD 11%、商业型；关键词分类总表-2026-11-13.md 采购/商业词首位，2026-11-13 已核查，30 天内不重查）
- 同簇词：custom high voltage ptc heater（20/月）、high voltage ptc heater manufacturer（10/月）、high voltage ptc heater supplier（10/月）；问题词 what is a ptc heater（260/月）已由 PTC-1116 承接，本篇只作一句话回答＋内链，不重复建页
- 意图：商业型——买家在找 PTC 加热器厂家，要比选、要报价，不是科普
- 选题简报链：目标客户（电车／电巴／重卡热管理采购与工程师，找厂家比选）→ 关键词数据（上）→ 意图（商业比选＋询价）→ SERP 验证（见下）→ 查重（管线表无 PTC-1117、无 ptc heater manufacturer 旧题；与 Codex DAILY-1117 BTMS 电巴线不撞题；站内已有制造商清单页 https://evbtms.com/high-voltage-coolant-heater-manufacturers/ 是“8 家短名单”，本篇是“怎么选厂家”指南，角度不同，互链不相食）→ 事实账本（见文末）→ 大纲（见下）→ 产品页与询价入口（HVCH 产品页＋选型报价页＋制造商清单页）
- SERP 验证（2026-11-17，铁律先行）：前排全是厂家／供应商页——KLC（台湾，IATF 16949，1982 年起做 PTC，12V–800V，OEM/ODM）、Nanfeng（河北南峰，10/15/20kW，350/600V，30 年以上车用加热器）、BLG（家用陶瓷取暖器，无关）、Amana（PTAC 空调，无关）；缺口＝没有一篇站在买家角度讲“怎么挑厂家”的指南，各家只贴自家规格，不教匹配方法；2026 年一份水暖 PTC 加热器市场报告把 Suzhou EVLINK Electronic Technology Co., Ltd. 列入重点厂商。本篇即补此缺口。
- 写作路线：大白话路线 A（Peter 2026-11-16 11:12 定）：短句、口语化、像人写的一样；测一次 ZeroGPT 两半；过线直接发，不过线当天早上直接特批直发，不再多问一轮
- 分类：Guide；slug 拟 ptc-heater-manufacturer（2026-11-17 curl 核验 404，未占用）
- SEO Title：PTC Heater Manufacturer: How to Pick the Right One for Your EV（65 字符）
- Meta 描述：Looking for a PTC heater manufacturer? Check voltage, power, control, and test data first. A short guide from EVLINK, with a 7-point RFQ checklist.（154 字符）
- 特色图：不重复用已发过的——不用媒体 10406（PTC-1111）、不用媒体 3186（PTC-1116，03-hvch-product.png）；从媒体库另选一张未用过的 HVCH 实物图；库里没有就先不设特色图（DAILY-1102 先例），事后补记
- 内链（7 处，2026-11-17 curl 逐个核验均为 200）：HVCH 产品页、选型报价页、制造商清单页、PTC-1116、PTC-1110、PTC-1111、HVCH 原理文

## 大纲

1. 短答案：好厂家三件事（电压功率对得上、控制接口对得上、拿得出测试数据）
2. 先定你自己的数字，别先翻厂家目录（平台电压、功率按最冷天算、冷却液回路、控制方式）
3. 列入短名单前先查五项（电压功率范围、控制接口、测试数据、样品、MOQ／交期／售后书面确认）
4. 前排大厂各有什么可取之处（KLC、Nanfeng，注明来源；以及它们都没讲的：怎么匹配）
5. 我们在 EVLINK 是怎么做（A/Q/E/H 四系实参＋要买家给的七项输入）
6. 五个红灯信号
7. FAQ（5 问，问题词取自实测词表）
8. 询价输入清单 CTA

## 正文（纯正文版从此开始）

# PTC Heater Manufacturer: How to Pick One for Your EV Project

You need a PTC heater for an EV. You search "ptc heater manufacturer." You get a wall of supplier pages. Most of them look the same.

Here is how to tell them apart. And what to send them so you get a real quote, not a catalog link.

## The short answer

A good PTC heater manufacturer can do three things.

Match your voltage and power. Match your control interface. Prove it with test data before you pay.

If a supplier cannot do all three, keep looking.

## Start with your numbers, not their catalog

A heater that fits someone else's bus may not fit yours. Write down your own numbers first.

**Your platform voltage.** A 400 V class truck and an 800 V class bus do not use the same heater. Our A series covers 400 to 800 V at 6 to 18 kW. Our Q series covers 400 to 1100 V at 15 to 35 kW. Pick the series that covers your platform with room to spare. A heater running at the edge of its range all winter will not last.

**Your power need.** Size for the coldest day, not the average day. PTC heat has a hard limit. One unit of electricity makes at most one unit of heat. The ratio never goes past 1 to 1. There is no free heat. So if your cab and your battery both need heat at minus 20, add the two loads up. Then pick the power.

**Your coolant loop.** A PTC coolant heater lives inside your loop. It needs your flow rate, your inlet temperature, and your target outlet temperature. Give the manufacturer these three numbers. If they quote you a heater without asking for them, that is a bad sign.

**Your control interface.** This one gets skipped a lot. Our A and Q series run on CAN plus an enable signal. The vehicle controller coordinates them. Our E series runs on a thermostat. It has no CAN. Check what your vehicle can actually talk to before you order. A heater with the wrong interface is a paperweight.

## Five checks before you shortlist anyone

**1. Does their range cover your platform?** One heater for every voltage is not a range. It is a guess. Look for a real series table. Power steps. Voltage steps. Control options. If the table is thin, the engineering behind it is thin too.

**2. Can they match your control?** CAN or thermostat. Ask which one. Ask how it wakes up. Ask what happens when the vehicle controller sends nothing. A good manufacturer answers these in one mail. A bad one sends you the catalog again.

**3. Will they share test data?** Brochure numbers are cheap. Ask what they test and how. Ask for the test report on the unit you will actually buy. If they will not share it, you are buying blind.

**4. Can you buy a sample first?** Fit it. Run it. Check the real outlet temperature against your loop. A sample costs little. A wrong batch costs a season.

**5. Are MOQ, lead time, and support in writing?** Ask for all three before you commit. A price with no MOQ and no lead time is not a quote. It is a chat message.

## What the big names do well

The top results for this search are all manufacturers. They are worth a look. Each one does something right.

KLC in Taiwan has built PTC heaters since 1982. They hold IATF 16949 certification. Their range runs from 12 V to 800 V. They do OEM and ODM work. What they do well: a wide range and documented quality certs. That is the bar for a serious supplier.

Nanfeng in Hebei builds 10, 15, and 20 kW coolant heaters at 350 and 600 V. They have made vehicle heaters for more than 30 years. What they do well: clear power steps for bus and truck platforms.

What none of these pages do is teach you how to match a heater to your loop. They show specs. They do not show the matching. That is the gap this guide fills.

One more data point. A 2026 market report on water PTC heaters lists Suzhou EVLINK Electronic Technology Co., Ltd. among the profiled producers. We are on that list. We are also the ones writing this guide. Read it as a manufacturer telling you how we want to be judged.

## How we do it at EVLINK

We build high voltage coolant heaters in three series, plus a fourth that we build per project.

A series: 6 to 18 kW, 400 to 800 V, CAN plus enable. Q series: 15 to 35 kW, 400 to 1100 V, CAN plus enable. E series: 20 to 24 kW, 400 to 800 V, thermostat control, no CAN. H series: it exists, and we spec it per project. Tell us the vehicle and we will tell you if H fits.

We also published a shortlist of 8 high voltage coolant heater manufacturers. If you want to compare us against the field, start there. We would rather you compare than guess.

When you write to us, send seven things. Your platform voltage. Your power need. Your coolant flow rate. Your inlet and target outlet temperatures. Your control type. Your vehicle type. Your annual volume. That is enough for a real quote. Our selection and quote page walks through the same seven inputs step by step.

## Five red flags

**They will not share test data.** Walk away.

**One power rating for every vehicle.** A bus and a truck do not need the same heater.

**No sample step.** They want a batch order before you have held the unit.

**A quote with no MOQ or lead time in writing.** You will find out both too late.

**Certifications they cannot show.** Ask for the certificate number. A real cert has one.

## FAQ

**What is a PTC heater?**

A PTC heater is a self regulating electric heater. Its resistance rises as it warms up, so current falls away once it reaches temperature. It cannot run away and overheat on its own. That is why EVs use it for cabin heat and battery preheating. There is no engine waste heat in an EV, so the heater has to make all the heat itself. We explain the full picture in our guide to what a PTC heater is.

**What voltage PTC heater do I need?**

Match your platform. A 400 V class vehicle takes a heater rated for 400 to 800 V. An 800 V class vehicle needs a heater rated past 800 V. Our Q series goes to 1100 V. Do not buy a heater rated exactly at your platform voltage. Leave headroom.

**CAN or thermostat control?**

It depends on your vehicle. If your vehicle controller manages heat, take CAN. Our A and Q series run on CAN plus an enable signal. If you want the heater to manage itself, take a thermostat. Our E series does that. It has no CAN.

**Can I order a custom high voltage PTC heater?**

Yes. Custom power and voltage are normal in this business. Our H series is built per project. Send your voltage, power, flow, temperatures, and control type. We will tell you what fits and what it takes.

**How do I get a quote from EVLINK?**

Use our selection and quote page. It asks for the seven inputs above. Or write to us with the same list. Either way, you will get a real number, not a catalog link.

## Send us these seven inputs

Platform voltage. Power need. Coolant flow rate. Inlet temperature. Target outlet temperature. Control type. Vehicle type and annual volume.

Send them through our selection and quote page. We will come back with a series, a price, and a sample plan.

## 事实账本（只用已核实数）

- 主词 ptc heater manufacturer：美国 40/月、KD 11%、商业型（关键词分类总表-2026-11-13.md，2026-11-13 核查）
- 同簇：custom high voltage ptc heater 20/月；high voltage ptc heater manufacturer 10/月；high voltage ptc heater supplier 10/月（同表）
- KLC：台湾，1982 年起做 PTC，IATF 16949，电压 12V–800V，OEM/ODM（ptc-heater.com.tw，SERP 2026-11-17）
- Nanfeng：10/15/20kW，350/600V，车用加热器 30 年以上（hvh-heater.com，SERP 2026-11-17）
- 2026 年水暖 PTC 加热器市场报告把 Suzhou EVLINK Electronic Technology Co., Ltd. 列入重点厂商（marketresearch.com，SERP 2026-11-17）
- EVLINK A 系 6–18kW／400–800V／CAN+enable、Q 系 15–35kW／400–1100V／CAN+enable、E 系 20–24kW／400–800V／恒温器无 CAN、H 系存在参数按项目给（Peter 2026-11-12／11-13 定）
- PTC 自限温原理＋CoP 上限 1:1（TI 设计指南，PTC-1116 已用）；电车无发动机余热（TI）
- 未写：EVLINK HVCH 认证宣称（无核实来源，不写）；HVCH 的 MOQ／交期数字（无核实来源，只写“问厂家要书面确认”）；具名客户案例（无）；NTC／HVIL（那是 T8 制动电阻的事实，不移用到 HVCH）
- 内链 7 处 2026-11-17 curl 逐个核验 200：/products/high-voltage-coolant-heater/、/high-voltage-coolant-heater-selection-quote/、/high-voltage-coolant-heater-manufacturers/、/what-is-a-ptc-heater/、/high-voltage-ptc-heater-selection-guide/、/high-voltage-coolant-heater-sizing-evs/、/how-high-voltage-coolant-heater-works/
- slug ptc-heater-manufacturer 2026-11-17 curl 核验 404，未占用

## 发布包

- SEO Title：PTC Heater Manufacturer: How to Pick the Right One for Your EV（65 字符）
- Meta 描述：Looking for a PTC heater manufacturer? Check voltage, power, control, and test data first. A short guide from EVLINK, with a 7-point RFQ checklist.（154 字符）
- Slug：ptc-heater-manufacturer（发布前复核是否被占用）
- 分类：Guide
- 特色图：媒体库另选未用过的 HVCH 实物图（不用 10406、不用 3186）；无图则不设，事后补记
- 检测：路线 A——2026-11-17 09:09–09:10 测一次 ZeroGPT 两半：上半 100%、下半 100%，均未过 ≤30% 线；大白话新写法亦未过。文章已按 Peter 2026-11-16 11:12 特批直发，不再多问一轮。
- 发布后：前台核验（200＋标题/H1 一致＋slug＋分类＋特色图＋内链逐个点开）；回填管线表；GSC 请求索引（GSC 登录 11-14／15／16 三天卡密码页，需 Peter 本人重登，暂无法做，记为缺口）

## 修订记录

- 2026-11-17 初稿：大白话路线 A；正文禁用词（delve／furthermore／moreover／in conclusion／it's important to note／whether you're）零命中；正文不用 em-dash（中文简报头除外）；无 B 系残留；未编数字、未编认证、未编客户案例

## Stage 7 自审（事后补记，2026-11-17）

- 本稿发布前未做 Stage 7（写作 worker 按路线 A 直发）；以下为发布后补审。
- 事实核对：A/Q/E/H 系参数与 REPORTS/hvch-series-parameters-recon-2026-11-09.md 一致；无 B 系残留；未编 EVLINK 认证、MOQ/交期数字、客户案例；CoP 1:1 与自限温原理有来源（TI 设计指南，PTC-1116 已用）。
- 警告：KLC（1982 年起、IATF 16949、12V–800V）、Nanfeng（10/15/20kW、350/600V、30 年以上）、2026 年市场报告列入 Suzhou EVLINK 三处事实来自本稿 SERP 简报引用的来源，未独立二次核验。
- 结论：PASS WITH WARNINGS（上述三处以引用来源为准）。
