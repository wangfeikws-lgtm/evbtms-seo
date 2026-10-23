# DAILY-HVCH-1022 返工v2 — 不是已过检稿

负责人Codex。2026-10-22晚间。全文重组，不是同义词替换；保留原主意图“HVCH不启动/不加热的控制证据”。

## 字段
- Title/H1: HVCH Not Heating? Separate the Supply and Control Evidence
- Meta: An HVCH enable request does not prove heating has started. Separate the variant, control supply and response using model-specific evidence before replacing hardware.
- Primary keyword: high voltage coolant heater not heating
- Secondary: HVCH not starting; HVCH control supply; coolant heater enable
- URL: 未批准新建。优先作为10116的窄主题支持模块；若另建必须先完成搜索需求和站内意图确认。原候选slug不代表已存在页面。
- 分类：工程集成支持；不面向家用/柴油驻车加热器维修流量。

## 事实与来源
- B/E 20–24kW、400–800V及控制区别来自REPORTS/evptc-official-spec-summary.md的冻结型号行。
- 22kW/600V≈36.7A为明确假设演算，不是实测、不用于现场电气选型。
- 未写任意低压阈值、pinout、CAN ID、客户返修经历、加热时间或认证。
- 公开来源示例https://www.webasto.com/en-us/heating/high-voltage-heaters/800v-hvh.html仅说明行业产品会区分HV/LV接口，不套用其参数到EVLINK。
- 本轮通用搜索返回车型投诉、协议专利等不相干结果，不作为主来源；没有完成US/UK固定设备Top5，因此不谎报SERP门禁通过。需要Muse复用已有策略确认此窄意图是否独立成页。
- 参见本批spec-and-claim-ledger.md，不使用“全系列通用认证”。

## HTML（正文）
```html
<p>We would not replace a high-voltage coolant heater just because the vehicle sends an enable request and the coolant stays cold. Before calling the heater faulty, establish what that particular unit is meant to accept. A power connection, a control request and useful heat in the coolant are different observations.</p>

<p>Our B and E Series make the distinction concrete. Both appear in the EVLINK specification summary at 20–24 kW and 400–800 V. B Series is listed with CAN and an enable interface. E Series uses thermostat control, without CAN or an external control interface. Choosing a unit from the power and voltage columns alone can therefore leave the vehicle expecting a conversation the heater was never designed to have.</p>

<h2>The same kilowatts do not mean the same start command</h2>
<p>Suppose a project requires the vehicle controller to request heating and read a defined status over CAN. B Series is a candidate to investigate; the E Series entry does not meet that communication requirement. That is a selection mismatch to resolve before commissioning, not evidence that an E Series unit has a CAN fault.</p>
<p>The exact B variant still needs its approved interface document. “CAN plus enable” does not provide a pinout, message identifier, wake-up sequence or diagnostic definition. We would not fill those gaps from another heater's manual. Similar power ratings do not make the wiring or software interchangeable.</p>

<h2>What a 22 kW calculation can tell you</h2>
<p>Consider a deliberately simplified electrical example: a heater taking 22 kW from a 600 V DC source. Dividing power by voltage gives 22,000 / 600, or approximately 36.7 A. That is an arithmetic reference for those assumed conditions, not a measured current from an EVLINK heater.</p>
<p>It does not establish that the control electronics have their required supply, that a command was accepted or that the heater delivers 22 kW at every point in its voltage range. It is not a cable or fuse recommendation either. Those decisions need the selected unit's actual limits and the vehicle electrical design.</p>
<p>If the available evidence consists only of a nominal battery voltage and an enable request in the VCU log, the diagnosis is still open. A calculation cannot supply the missing observations.</p>

<h2>Start with the event that failed</h2>
<p>For an intermittent no-start, a voltage reading taken several minutes later is a weak substitute for a record of the attempted start. We would ask the responsible engineer to capture the relevant control-supply condition at the approved observation point, together with the documented wake-up or enable input and any feedback the variant actually provides.</p>
<p>Keep the timing relationship. Did the unit reach its defined ready state before a heating request arrived? Did a supply or vehicle-state change coincide with the failed attempt? These are questions for the evidence package. They are not universal timing rules; the released interface specification determines the required sequence.</p>
<p>Do not invent a ready-state signal if the model has none. For a thermostat-controlled unit, follow its own control architecture. An empty CAN trace cannot prove that a non-CAN heater is defective.</p>

<h2>Awake is not the same as allowed to heat</h2>
<p>A controller may be awake while heating remains inhibited. The particular heater and vehicle documentation determines which conditions matter and which states are observable. Use those definitions to interpret an alarm or a refusal to heat, rather than treating every inhibit as an internal hardware failure.</p>
<p>Preserve the original fault information before a reset. If a restart makes the symptom disappear, retain that result alongside the failed attempt; do not rewrite the history as “no fault found”. A controlled comparison between successful and unsuccessful attempts can be more useful than another catalogue page.</p>

<h2>Cold coolant does not identify an electrical cause</h2>
<p>Even when electrical input is established, the thermal side remains a separate question. Coolant flow, starting temperature, circuit mass, sensor positions and the observation period affect what a temperature trace means. Use the existing <a href="https://evbtms.com/hvch-power-verification/">HVCH power-verification guide</a> to distinguish a requested output, electrical input and delivered heat.</p>
<p>A no-start investigation should stay focused. First establish whether the documented start and heating conditions were met. If the unit is taking power but the coolant response is unexpected, move to the thermal investigation with those electrical observations attached. Do not keep changing communication settings to solve an unverified hydraulic problem.</p>

<h2>Keep the test within the approved procedure</h2>
<p>High-voltage access and measurements require qualified personnel and the vehicle's approved isolation and service procedures. Do not bridge an interlock, force a power stage on, apply an assumed test voltage or use an unverified connector pin assignment. The purpose of the review is to identify the next justified inspection, not to improvise a live test.</p>
<p>A useful evidence package identifies the heater part and software version, the interface revision, the requested operation, the observed supply and states, and the fault information. Include the measurement location and the differences between runs. Where a channel was not captured, write “not recorded”. That is more useful than reconstructing a plausible value afterwards.</p>

<h2>What we need for a model-specific review</h2>
<p>Send the exact heater identity, vehicle voltage range, required control method and the available start-event record when you <a href="https://evbtms.com/contact/">contact EVLINK about an HVCH integration</a>. State whether the problem is a missing start response, a reported inhibit or an unexpected thermal result. We can then identify which product documents and project inputs the discussion needs.</p>
<p>For network mapping, the separate <a href="https://evbtms.com/hvch-can-integration-oem-checklist/">HVCH CAN integration checklist</a> covers the wider interface task. The <a href="https://evbtms.com/products/high-voltage-coolant-heater/">coolant heater product range</a> supports selection. Neither should be used to turn a series-level description into a made-up protocol for an individual unit.</p>
```

## 配图
复用REPORTS/assets/daily-2026-10-22/hvch-start-up-review-feature.webp；图文主题仍匹配。不是接线图或测试照片。

## 检测
本v2未检测。旧v1的ZeroGPT62.6%/GPTZero100%均不能沿用为本v2结果。固定检测文本：REPORTS/detection-1022/DAILY-HVCH-1022-low-voltage-wake-up-v2.txt。要求完整全文、一次提交、保留实际分数和报告；不符合<=30%则继续修订，不发布。

Peter已明确明天审核后才发布；本次只交修订候选。
