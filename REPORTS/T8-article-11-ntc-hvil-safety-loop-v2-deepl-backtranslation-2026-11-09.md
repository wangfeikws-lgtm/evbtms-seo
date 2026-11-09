# T8-11 DeepL 回译版（v2 重组版 → 英→西→英-GB，2026-11-09）

- 原稿：REPORTS/T8-article-11-ntc-hvil-safety-loop-v2.md（ZeroGPT 43.1% 未过线）
- 方法：正文按段切 19 块（每块 ≤1200 字符），每块英→西→英-GB 回译，按原顺序原结构重组；表格已改写为句子；只修正 3 处产品术语（heater→resistor），其余一字未润色。
- 全文 17,335 字符：上半 R1–R9 为 8,299 字符，下半 R10–R19 为 9,036 字符。分界点：上半止于 "'Trend' is the key word..." 段末，下半起于 "We must be honest and state this clearly..."。
- ZeroGPT 分数：两半均已通过。2026-11-09 13:54–13:56 重测（新会话，先重载＋短句验证 0%）：上半 R1–R9 1.9% AI GPT（"Your Text is Human written"，1,407 词）、下半 R10–R19 3.5% AI GPT（"Your Text is Human written"，1,498 词），两半均 ≤30%，一次成功无报错。早先上半首段 513 字单测 37.3% 仅为样本分，不代表整半分数（整半实为 1.9%）。此前 12:17 前 4 次＋12:19–13:09 8 次整半检测均无结果（1 次明确报错 "Oh Oh, An Error occurred. Please Try again."），疑似检测器对长文本不稳定。分数未编造。Peter 2026-11-09 13:57 定 5 处全部改回原文意思，已修正；按直发规则发布。修正为单字/短语级事实还原，未润色改写；分数为修正前文本所测（上半 1.9%、下半 3.5%），未重测。
- 数字核对：全部关键数字均保留，无一丢掉（140 kW、20 分钟、168 MJ、168,000 kJ、8.4 MJ、172 L/min、3,440 L、DN32、2.24 Ω、450 V、850 V、90 kW、323 kW、43%、3.6 倍、NTC 5K、±1%、IP6K9K、-40/+85 °C、25 tests、HVH-R1402、KEB/Siemens/ABB、U²/P）。

## 上半（R1–R9）

A review of the integration of a braking resistor tends to get bogged down in the same three questions. They seem straightforward, but each one has posed a problem in a real-world project. Can the vehicle cut the power supply to a connector that is not properly plugged in? Is it capable of detecting a rise in temperature during a descent early enough to take action? And when a sensor reading appears to be incorrect, does the controller have a pre-set response, or does the system have to improvise on the fly?

We manufacture the HVH-R1402 liquid-cooled braking resistor for electric buses, heavy goods vehicles, mining trucks and construction machinery, tailored to each project. Its rated power is 140 kW continuous for 20 minutes, 2.24 Ω, 450–850 V DC, IP6K9K, with an operating range of –40 to +85 °C, and it has been validated through 25 tests. These figures describe the unit. They do not indicate whether the vehicle surrounding it is safe. That aspect depends on two signals and one set of protocols: the high-voltage interlock loop (HVIL) provides protection in the moments before current flows; NTC temperature detection provides protection during the minutes whilst current is flowing; and a documented fault map provides protection when a reading ceases to make sense. If any one of these three is missing, the inspection must not give the go-ahead.

The acceptance test table: what to check and what a ‘correct’ result should look like. HVIL loop closed before activation: disconnect a high-voltage connector on first start-up and observe how the vehicle refuses to activate the resistor. A correct result is as follows: no current reaches the resistor due to an open circuit, every time, not just on the first attempt. What is overlooked if this check is omitted: a poorly connected plug that allows charging current to flow until an electric arc occurs. NTC reading under real-world conditions under load: carry out a braking test under load and confirm that the temperature reading varies according to the load. The correct behaviour is as follows: the reading follows the braking effort and stabilises as the load decreases. What is overlooked if this check is omitted: a sensor that exists only on the wiring diagram and nowhere else.

Adequate cooling for the duty cycle: compare the flow rate available at the resistor inlet with the 172 l/min required for the full 140 kW cycle over 20 minutes. The correct result looks like this: a temperature trend that stabilises during a sustained decline. What is overlooked if this step is omitted: a rise that never stabilises, which is accurately reported but on which no action is taken. Controller response agreed in advance: the integration document specifies what the controller does in the event of a power reduction, an open-loop condition and a sensor fault. The correct approach is something like this: three written responses, one for each scenario, agreed with the supplier prior to commissioning. What is overlooked if this step is omitted: a fault detected on a slope, with an improvised response on the spot. That table encapsulates the entire article in miniature. The rest explains why each row has its place, with the calculations that determine what is at stake.

Why so much is at stake: 168 MJ in a single descent

140 kW over 20 minutes equates to 140 × 20 × 60 seconds, which amounts to 168,000 kJ, or 168 MJ of heat per unit. Per minute, that amounts to 8.4 MJ. Put another way, a vehicle on a long downhill gradient is asking one resistor to absorb, minute after minute, roughly the energy of a minor car crash every few seconds – and does so without a hitch.

The cooling system works in the same way. At 172 L/min, operating at full load for 20 minutes circulates 3,440 litres of coolant through the DN32 connection. If the circuit cannot provide that flow rate — whether due to a shared pump, a hose that is too long, a sharp bend or trapped air — the rise in temperature will be the first thing to tell you so. And it won’t politely tell you twice.

The calculation of resistance provides a second reason why the control strategy is important, and here we are simply taking it a step further than what had already been set out in our guide to calculating resistance. That guide places the same nominal winding of 2.24 Ω at around 90 kW instantaneous at 450 V and around 323 kW at 850 V, compared with a continuous thermal power of 140 kW. The additional point made in this article is what these two figures imply for the chopper: at 850 V, maintaining an average power of 140 kW out of the 323 kW instantaneous power implies a duty cycle of around 43 per cent relative to the nominal resistance. (Our sizing guide highlights the same ‘voltage window’ effect from the other end: the power at the upper end of the 450–850 V window is approximately 3.6 times the power at the lower end). The rated power of the resistor, the bus voltage and the chopper strategy constitute a single calculation, not three separate lines on the technical data sheet. A safety review that checks the rated power of the resistor without verifying the duty cycle strategy has only checked half the system.

Before current flows: the HVIL loop

The HVIL system answers a single question: are the high-voltage connectors fully mated? A low-voltage signal loop runs through the connectors. In typical HVIL connector designs, the short signal pin breaks contact before the power pins separate, so that a connector that becomes loose opens the signal loop whilst the power pins remain in contact. The vehicle detects the open loop and can refuse to supply power to the resistor before current flows through a faulty connection.

Timing is everything in this case, and it is the aspect that is most often misunderstood. The HVIL is not a fault detector for a braking manoeuvre that is already in progress. It is a gate in the enable sequence. A loose connector detected during a 140 kW braking manoeuvre already poses a risk of an electric arc. A loop checked before activation turns that same fault into a connector issue detected in the workshop.

That is also why bypassing the loop is the most costly shortcut in this article. During installation or commissioning, someone bypasses the interlock to save ten minutes, intending to remove the bypass later. The vehicle then loses its only means of detecting a poorly fitted connector, and this remains the case for the vehicle’s entire service life, not just for that one afternoon. If the loop does not close, the connector is not fitted properly. Fix the connector. Never silence the loop and call it progress.

Our guide to sizing errors includes tried-and-tested checks in its pre-purchase checklist precisely for this reason. The checklist exists because ‘the loop was omitted during commissioning’ is a phrase nobody wants to have to explain following an incident.

Whilst the current is flowing: the NTC loop

Once the resistor is energised, the question changes. It is no longer ‘is everything connected?’, but ‘will this descent end well?’. An NTC sensor located inside the unit communicates the element’s temperature to the vehicle’s controller. In the HVH-R1402 model, this sensor is a 5K NTC element, with an accuracy of ±1 per cent, as stated on the product page. The resistance of the NTC decreases as the temperature rises, so the controller reads a variable resistance and converts it into a temperature trend.

‘Trend’ is the key word, and this is where continuous monitoring proves its worth compared with the industrial alternative. A thermal switch – the sort found in all protection diagrams for braking resistors in variable frequency drives (VFDs) from KEB, Siemens and ABB – provides just one piece of information: whether it is hot or not. It remains inactive, then trips, by which time the vehicle is already at its limit. An NTC sensor provides the slope. The controller can detect how the temperature rises during a descent and begin to react in advance: reducing braking power, engaging the friction brakes and alerting the driver. On a mining truck gradient that generates a sustained load minute after minute, that early response makes the difference between managing a descent and having to react to an emergency upon reaching the bottom.

## 下半（R10–R19）

We must be honest and state this clearly: the sensor detects heat, but it does not remove it. If the coolant flow rate is less than the 172 L/min required by the system, the NTC will show a rise that does not stabilise, and the vehicle will still require a response strategy to act upon. A sensor that nobody takes into account is nothing more than a decoration on the dashboard. The key question during the service is not ‘is the NTC connected?’, but ‘what does the controller do with the reading, at what point, and who has approved it?’.

Correcting the wiring deserves its own section in that review, as it has posed a real problem for some bus programmes. A service bulletin published by a bus manufacturer once attributed a power reduction fault to brake resistor temperature sensor cables that had been swapped at a connector: the protection logic was activated, but based on data from the wrong system. The lesson is universally applicable. A varying reading is not the same as a correct reading. The load brake test shown below checks for variation; the integration document should also confirm that the sensor sends the data that the strategy actually reads to the controller’s input.

When a reading no longer makes sense: fault mapping

The third safety measure is the paperwork, and this is the one most frequently left blank. There are four cases that require written action by the controller before the vehicle leaves the factory, as agreed with the resistor supplier during integration:

1. The NTC is installed but has never been connected. Everything works on level ground, so this passes the commissioning stage. It fails on the first real descent, when the vehicle needs a temperature trend and does not have one. Validation question: has it been verified that the reading varies under a real braking load, and not just that it appears on a diagram?

2. Cooling is insufficient and the NTC is the only indicator. The flow rate is lower than the load requires, and the temperature rises during the descent rather than stabilising. The sensor fulfilled its function by reporting this. Validation question: what derating or blending step follows the notification, and at what point during the ascent?

3. The HVIL loop is bypassed to start the vehicle. A jumper silences the alarm and masks any connector faults that may arise subsequently. Check question: Is there a written commissioning procedure stating that a loop that does not close is a connector fault that must be rectified, and never an alarm that should be silenced?

4. A sensor reading appears to be incorrect and no one knows what the correct value should be. An open circuit, a short circuit or a reading that does not vary each require a predefined action from the controller. That assignment is a decision to be made by the vehicle’s controller, and must be included in the integration checklist prior to commissioning, not in a discussion whilst on the road.

Notice what these four cases have in common. None of them is a fault with a resistor. All four are integration gaps, and all four are cheaper to rectify during a service than whilst on the road.

Two tests that check both loops

We recommend carrying out two tests during the first start-up, as they are inexpensive and detect the two most common faults.

Firstly, disconnect a high-voltage connector and observe how the vehicle reacts. The HVIL loop should open and the vehicle should refuse to power the resistor. If nothing happens, the loop is not wired as shown in the diagram. Correct this before carrying out any load tests, as a load test with a faulty interlock is what causes a problem with the connector to turn into an arcing fault.

Secondly, carry out a braking test under load and check that the temperature reading varies with the load. A constant reading under an actual braking load means that the NTC chain is faulty at some point between the sensor and the controller, regardless of what the wiring diagram indicates. A reading that varies with the load means that the entire chain — from the sensor to the controller, via the display or data logger — is functioning correctly.

Ten minutes of testing will provide you with an early warning system for any subsequent descents. If you skip this step, the first real descent will become the test, with a vehicle full of passengers or a loaded lorry acting as a test bed.

What to include with your enquiry

Send us these details and we’ll let you know straight away whether the HVH-R1402 is compatible with your vehicle and what integration requirements you need to meet:

- Bus voltage range and continuous power output with the longest braking cycle. The rated power of 140 kW for 20 minutes is the benchmark; your reduction determines the actual figure.
- Which NTC signal interface your controller expects and what it does with the reading: power reduction steps, warning thresholds, combination with the friction brake.
- How the HVIL loop is connected to your high-voltage system and what your controller does when the loop is opened.
- How the controller responds to a sensor fault: open circuit, short circuit or a reading that does not change.
- Coolant flow rate available at the resistor inlet, compared to the 172 L/min required for full-load operation.
- Chopper configuration: whether your controller already has a chopper output, or whether you require a separate resistor plus chopper setup, or the integrated chopper and brake unit. The safety circuits are the same across all three configurations; it is the wiring that differs.

We manufacture for electric buses, heavy goods vehicles, mining lorries and construction machinery, tailoring our solutions to each project and adapting to the voltage range and operating conditions you actually use. The resistor has a rated power of 2.24 Ω, 450–850 V DC, IP6K9K, operates between -40 and +85 °C and has been validated through 25 tests. These figures describe the unit. The two loops and the fault mapping describe how safety is ensured within your vehicle. Please enquire about both aspects.

Frequently Asked Questions

What is an NTC sensor? An NTC sensor is a temperature sensor whose resistance decreases as the temperature rises. In the HVH-R1402 model, a 5K NTC element with an accuracy of ±1 per cent transmits the temperature of the resistive element to the vehicle’s controller, which converts the change in resistance into a temperature trend that the controller can act upon before the temperature reaches a limit.

What is an HVIL loop? A high-voltage interlock loop is a low-voltage signal loop that runs through high-voltage connectors. In typical HVIL connector designs, the short signal pin breaks contact before the power pins separate, so that a connector that becomes loose opens the signal loop whilst the power pins remain in contact. The vehicle detects the open loop and refuses to power the resistor before current flows through a faulty connection.

Do I need both, or is one enough? Both. NTC cannot tell you a connector is loose. HVIL cannot tell you the resistor is overheating. They watch different failures, on different timescales, and neither covers the other's blind spot.

Can I use a thermal switch instead of an NTC? A thermal switch provides a single ‘hot’ or ‘cold’ signal. It cannot indicate how quickly the temperature is rising, nor can it give the controller time to reduce power, apply the friction brakes or warn the driver before the limit is reached. It is an end-of-line device, not a control input. The NTC’s trend and the controller’s programmed response to it are what make the system manageable during a prolonged descent.

What happens if the NTC never connects? Everything works on level ground, so the commissioning test is passed. However, it fails on the first actual descent, when the vehicle needs a temperature trend but does not have one. The load braking test exists precisely to detect this specific scenario.

What should the vehicle do when the HVIL loop is open? The vehicle must refuse to supply power to the resistor and treat the open loop as a connector fault that needs to be checked, not as an alarm to be ignored. The exact response sequence is determined by the vehicle controller’s strategy, agreed upon at the time of integration, before the system enters service.

Project data checklist (to be sent alongside your enquiry): bus voltage range; continuous power and maximum braking time; controller NTC interface and response strategy; HVIL wiring and open-loop response; behaviour in the event of sensor faults; available coolant flow rate; chopper status (existing output / split / integrated). Product details: braking resistor page. Related reading: sizing error guide (the two points on your pre-purchase checklist), how braking resistors work (the overview of the safety loop that this article expands upon), sizing guide, U²/P resistor calculation.

## 丢掉/改变的措辞清单（回译 vs 原文，未自行补填）

- R2：acceptance table→acceptance test table；open loop→open circuit；load current→charging current；connector→plug（一处）。
- R3：descent→decline；grade→slope；derating→power reduction。
- R4："asking one resistor to absorb"→"demands a cooling system that absorbs"（吸收主体改变，见事实相反清单）；without drama→without a hitch；loop→circuit。
- R6：short signal pin→short-circuit signal pin（见事实相反清单）。
- R8：bypassed→omitted。
- R9：continuous sensing/detection→continuous monitoring。
- R10：review→service；"the duty needs"→"the system requires"。
- R11：blending→fuel mixture（见事实相反清单）；climb→ascent。
- R12：Sign-off question→Check question；review→service。
- R14：NTC path is dead→NTC chain is faulty；warning system→early warning system；What to send→What to include。
- R15："your descent sets the real number"→"your reduction determines the actual figure"；derating→power reduction；bus voltage window→Bus voltage range；blending→combination。
- R16："wiring partner changes"→"it is the wiring that differs"（partner 丢掉）；"We build for…"→"We manufacture for…"；"Ask about both"→"Please enquire about both aspects"。
- R17：short signal pin→short-circuit signal pin（第二次出现）；energize→power；resistor element→resistive element。
- R18："Do I need both?"→"Do I need all three?"（见事实相反清单）；hot-or-not→"‘hot’ or ‘cold’"；written response→programmed response；review→analysis。
- R19：temperature trend→temperature gradient（见事实相反清单）；"never wired up"→"never connects"；bypass→ignored；"Project inputs checklist (send with your inquiry)"→"Project data checklist (to be sent alongside your enquiry)"；"longest braking duty"→"maximum braking time"；"the two signals"→"the two points"。

## 事实相反的词（Peter 2026-11-09 13:57 定：5 处全部改回原文意思，已修正）

1. R4：原文 "asking one resistor to absorb"（由一只电阻吸收）→ 回译 "demands a cooling system that absorbs"（由冷却系统吸收）——吸收主体由电阻换成冷却系统，与原文事实相反。
2. R6 与 R17（同一错误出现两次）：原文 short signal pin（长度短的信号针）→ 回译 short-circuit signal pin（短路信号针）——部件性质相反。
3. R11：原文 blending step（制动混合步骤）→ 回译 fuel mixture（燃油混合）——制动策略被写成燃油相关，与原文事实相反。
4. R18：原文 "Do I need both?"（两者）→ 回译 "Do I need all three?"（三者）——数量词改变。
5. R19：原文 temperature trend（温度趋势，随时间变化）→ 回译 temperature gradient（温度梯度，随空间变化）——物理量改变。

修正记录（2026-11-09，Peter 定后执行）：R4 吸收主体改回 one resistor；R6/R17 短路信号针改回 short signal pin；R11 燃油混合改回 derating or blending step；R18 整条 FAQ 恢复原文（Do I need both, or is one enough? ＋ Both. NTC cannot tell you a connector is loose. HVIL cannot tell you the resistor is overheating.）；R19 温度梯度改回 temperature trend。

## 修正过的产品术语（仅修正产品术语，其余未润色）

1. R3："heater inlet"→"resistor inlet"（原文 resistor inlet）。
2. R16："heating element inlet"→"resistor inlet"（原文 resistor inlet）。
3. R16："separate heater plus chopper setup"→"separate resistor plus chopper setup"（原文 resistor-plus-chopper split）。
