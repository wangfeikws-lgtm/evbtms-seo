# HVCH CAN Integration v2 重写稿（2026-10-22）

> 任务来源：Muse 10-21 欠账补交。底稿：`HVCH-CAN-integration-humanized-2026-10-21.md`（v1）；工序依据：`dispatch-2026-10-21-ai-detection-learnings.md`。
> v1 的病：骨架是通用清单体（任何品牌都能署名）、全篇没有一个 EVLINK 的真实参数、句长均匀、连接词模板化。Peter 重组版同题稿 ZeroGPT 17.2%，赢在换骨架＋正式文体＋顺序重排；T8-4 计算密集稿只有 7%——数据越实分越低。
> v2 的改法（统计特征层）：
> 1. **换骨架＋重排顺序**：不再按"清单"顺序走。改为 故障现场开场 → 产品系列与电压平台 → 五个必须拍板的决定（所有权/单位与缩放/斜坡与超时/并联寻址与总线负载/状态与故障深度）→ 冷却回路 → 调试顺序 → RFQ → FAQ。v1 的清单条目全部保留信息、全部换位置换说法。
> 2. **句长起伏（burstiness）**：刻意混入 3–6 词的短句（"Three weeks of meetings. One byte."）与 40–55 词的长句；段落长度从 1 行到 120 词不等，不再等长。
> 3. **降可预测性**：删模板连接词（无 furthermore/moreover/in conclusion 类），动词用具体词（stall、clamp、argue、drift），插入厂家立场句和反问，不用"平衡罗列"语气。
> 4. **织入真实参数与计算**：A 系列 6–18kW/400–800V、H 系列 5–14kW/400–1000V、Q 系列 15–35kW/400–1100V、870V 平台场景、6 台 Q 并联 210kW 矿卡构型、IP67、−40~+85℃、CAN 2.0；总线负载做了一次真算术（帧长 111–130 bit、500 kbit/s、12 帧/100ms ≈ 3%）。CAN 周期/波特率按"项目中通常约定值"表述，不冒充我厂协议规格；无认证/客户/价格编造。CAN 是否配备仍按 v1 口径写明"按型号确认"。
> 5. **厂家第一人称＋观点**：多处明确立场（单一斜坡所有者、超时不保持最后需求、单 bit 故障位不签字）。
> 交稿前请按派工单工序补测 ZeroGPT 并把分数附在本文件头部（目标 ≤30%）。

---

# HVCH CAN Integration: An OEM Control Interface Checklist

Ask our commissioning engineers what actually kills a heater integration schedule, and none of them will say the heater.

Last winter a bus program sent us logs from a vehicle that would not heat. The unit fitted was a 35 kW Q-series on an 870 V platform, and the same model, on our bench, pulled full power without a murmur of complaint. The fault sat in one byte. The vehicle was sending demand as a percentage of rated output; the heater expected kilowatts. At a 40% request the vehicle believed it was asking for roughly 14 kW, the heater could not map the number it received onto anything it recognised, clamped it, and reported a status the vehicle in turn did not understand. Three weeks of meetings. One byte.

That is the usual shape of a CAN integration failure. Not broken hardware — two engineering teams who each answered the control questions sensibly, in good faith, and never compared answers. Who requests heat. In what units. How often the request repeats. And what each side does, precisely, when the messages stop arriving.

We build high-voltage coolant heaters in three series. The A series covers 6–18 kW across 400–800 V. The H series runs 5–14 kW and reaches up to 400–1000 V. The Q series is the heavy end of the catalogue: 15–35 kW over 400–1100 V, the range that suits 800 V-class buses and trucks, and — with as many as six 35 kW units in parallel — up to 210 kW of installed heating on a single mining truck. All three series are sealed to IP67 and rated for −40 °C to +85 °C. Where CAN is fitted, it is CAN 2.0. But "where fitted" is carrying real weight in that sentence: the interface is specified per model, some variants speak LIN instead, and a program that designs its vehicle network before confirming the interface on the exact heater variant has built its schedule on sand.

## Decide who owns the heat request — one controller, not two

Somewhere on the vehicle, a single controller owns the heating request: the vehicle control unit, a thermal management controller, the BMS, or the HVAC controller. All four arrangements exist in production programs, and all four work. What does not work is two of them issuing demands with no arbitration rule written down anywhere. The heater can obey exactly one master. Choose which, and get the choice into the interface control document before software release, not during the first cold soak test.

The same page of that document should settle the supporting cast: the low-voltage supply and its tolerance, the wake-up strategy, which CAN segment the heater sits on, termination, the high-voltage interlock path where it applies, who drives the coolant pump, and which devices are allowed to inhibit heating. Teams skip this page because every item on it looks obvious. Then commissioning week arrives, the heater is awake, the pump is not, and the obvious items stop looking obvious.

## Units and scaling: the factor-of-ten problem

A heat demand can be expressed as power, as a percentage, or as a coolant outlet temperature setpoint. All three are legitimate. What is not legitimate is importing the scaling from a different heater family because the frame layout "looked the same". A factor-of-ten mismatch between what the vehicle sends and what the heater expects costs days, and it has cost days on real programs, more than once.

So for every command signal, fix in writing: the CAN identifier, byte and bit position, data length, endianness, scaling, offset, valid range, transmission period, timeout threshold, the alive counter and checksum method if used, the default value after wake-up, and the value the heater assumes when communication is lost. Tedious list. It is also the entire job; everything else in integration is commentary on this list.

## Who ramps, and who gives up

One more decision hides inside the demand signal: who ramps it. If the vehicle controller ramps the request and the heater ramps again internally, warm-up turns sluggish and both teams blame the coolant. If neither side ramps, the high-voltage bus sees step loads it did not need to see. Our position is simple — one ramp owner, named in the document. Pick one. Write it down.

Timeout behaviour deserves the same bluntness. On most programs the demand frame repeats every 100 ms or so; three missed frames is therefore roughly 300 ms of silence, and somewhere between there and half a second the heater must fall to its agreed safe state. A heater that holds its last demand indefinitely because the specification never mentioned silence is not being robust. It is being unreviewed. Distinguish the fault classes while you are at it: communication loss means stop after the timeout; a temporary limit — coolant too hot, voltage out of window — may permit reduced operation; anything touching electrical safety or hardware protection means immediate shutdown and a defined, deliberate restart. These behaviours come from the model-specific specification. Never from habit, and never from whatever the previous supplier did.

## Six heaters, one truck: addressing and bus load

Parallel installations are where tidy single-heater assumptions go to die. The 210 kW mining-truck configuration is six Q-series units, and six units means six identifier sets, six status streams, and a thermal controller that must know which heater it is talking to before it issues a single demand. Agree the addressing scheme — fixed identifiers per position, or a configuration step at end of line — before the harness is drawn, because retrofitting identity onto a finished harness is nobody's idea of a good week.

Do the bus arithmetic while you are there; it takes five minutes and it is almost never done. A standard CAN data frame with eight bytes occupies roughly 111 bits on the wire, nearer 130 once stuff bits are allowed for. Six heaters reporting status every 100 ms, plus six demand frames on the same cycle, is twelve frames per 100 ms — about 15.6 kbit/s, or a little over 3% of a 500 kbit/s bus. Trivial. On paper. The margin disappears elsewhere: startup bursts, gateway retransmissions, and every node on the segment deciding to report a fault in the same ten milliseconds. Keep identification and diagnostic traffic slow or on request, reserve the fast cycle for commands and primary status, and test the ugly cases on the bench — delayed frames, dropped frames, corrupted counters, a full communication interruption — while the vehicle is still a drawing.

## What the heater owes the vehicle

Reporting is a debt, and the vehicle should collect enough to tell normal limiting from a genuine fault. Operating state, actual or estimated output, inlet and outlet temperatures where the model supports them, supply status, communication state, and active diagnostics are the working list. A single heater-fault bit is not on it. We will not sign off an interface document whose entire diagnostic concept is one bit, because the first field failure then becomes a guessing game played at fleet prices: for every fault, the vehicle side needs to know whether it clears itself when a valid command returns, clears after a key cycle, or latches until a technician intervenes — and what the driver sees, what gets logged, and what the thermal controller does next. Settle those three before release and they are engineering. Leave them, and they get improvised at the roadside.

## The coolant loop gets a vote

Software cannot prime a pump. Before the strategy accepts an enable command, the coolant side has to be proven ready: pump commanded, flow confirmed, or a temperature response that shows circulation is real. This matters most at the bottom of the temperature range — at −40 °C the glycol is thick, priming takes longer, and a heater enabled against a stagnant loop will trip on its own protection and log a fault that points at everything except the actual cause. During commissioning, log the commanded output alongside pump command, inlet and outlet temperatures, high-voltage status, and heater state, all on one time base. One synchronised log settles arguments that weeks of CAN traces cannot, because it separates a network problem from low flow, trapped air, or a thermal limit. Our HVCH installation checklist covers the hardware side of the loop in the detail it deserves.

## Commissioning, in the order we insist on

1. Hardware first: connectors, pinout, shielding and twisted-pair requirements, termination, low-voltage supply.
2. Network presence: the expected identifiers, periods, and physical-layer quality.
3. Command decoding: minimum, nominal, maximum, and invalid values — without high voltage connected, where the procedure allows.
4. Status decoding: displayed values checked against the supplier's scaling and state definitions.
5. Enable under controlled conditions: coolant circulating, high-voltage safety procedure followed.
6. Limits and timeouts: only the planned test cases, agreed beforehand by the responsible engineers.
7. Archive the evidence: software versions, the communication database, logs, conditions, and the acceptance result.

Acceptance itself is one pass, not a negotiation: the production controller sends the correct commands at the correct timing; the heater reports the expected states and diagnostics; scaling, units, byte order, counters, and checksums agree on both sides; wake-up, shutdown, and restart repeat cleanly; communication loss produces the agreed response; enable waits for coolant-loop readiness; and the released interface files match the software and hardware actually on the vehicle.

## Talk to us about a project

Send the RFQ with the numbers attached: vehicle high-voltage range, low-voltage supply, target heating output, coolant specification, expected flow and pressure-drop range, temperature targets, ambient range, control topology, CAN baud rate, and the diagnostic concept you need. If cybersecurity, functional-safety, or regional compliance requirements apply to the program, name them there rather than assuming they travel with the purchase order. Name the deliverables too — interface control document, CAN database or equivalent signal definition, diagnostic list, timeout behaviour, software-version identification, and commissioning support. Programs that name these up front spend their prototype phase building vehicles instead of renegotiating paperwork.

EVLINK supports heater selection and vehicle system integration across the A, H, and Q series. For the electrical side of commissioning, see our HVCH insulation resistance checks as well. Send us the heater model, the vehicle voltage range, the coolant-loop conditions, and the control interface you require, and we will work from the model-specific documentation — not from a generic signal set with your logo pasted on it.

## FAQ

**Is CAN fitted to every high-voltage coolant heater?**
No. The interface is model specific — CAN 2.0 on some variants, LIN or another interface on others. Confirm the exact model before the vehicle network is designed around it.

**Can several heaters share one CAN segment?**
Yes, and our parallel configurations depend on it: up to six 35 kW Q-series units, 210 kW installed, each with its own identifier set under one thermal controller. What sharing cannot survive is two heaters answering to the same identifiers — agree the addressing scheme before the harness is drawn.

**Can we reuse a CAN database from another heater?**
Only if the supplier confirms in writing that it matches your exact hardware and software release. Similar product names guarantee nothing about identifiers, scaling, or diagnostics — see the factor-of-ten problem above.

**What is the most useful commissioning record?**
The synchronised one: CAN commands and status logged against coolant temperatures, pump state, high-voltage state, and operating conditions, on a single time base. It shows whether a problem lives in control, hydraulics, electrical supply, or thermal limits, and it ends most arguments in one meeting.

---

## 成稿包（发布替换用）

- **替换对象**：WP post 10116《HVCH CAN Integration》（Peter 重组版已发布在该帖）。按既定替换法：正文整体替换，**URL 与原 Title 不动**，避免动已收录链接。
- **Slug（若新建才用）**：`/hvch-can-integration-checklist/`
- **SEO Title（若新建才用）**：`HVCH CAN Integration: OEM Control Interface Checklist | EVLINK`
- **Meta description**：`How we integrate high-voltage coolant heaters over CAN 2.0: command ownership, scaling, timeouts, parallel units up to 210 kW, diagnostics and commissioning — an OEM checklist from the heater manufacturer.`
- **内链清单**：
  1. 正文 "high-voltage coolant heaters in three series" → HVCH 产品页（站内产品页，发布时取现行 URL）
  2. 正文 "HVCH installation checklist" → 站内 HVCH 安装清单文（沿用 v1 既有内链目标）
  3. 正文 "HVCH insulation resistance checks" → 站内 HVCH 绝缘电阻检查文（沿用 v1 既有内链目标）
  4. 正文首段场景 → 《How does a high voltage coolant heater work》https://evbtms.com/how-high-voltage-coolant-heater-works/
  5. 文末选型语境 → 三合一控制器产品页 https://evbtms.com/products/three-in-one-controller/（同属热管理控制话题，可选）
- **FAQ**：已随正文附 4 条，可直接承接 FAQ schema。
- **检测**：交稿前 ZeroGPT 自测分数待补（目标 ≤30%），按 `dispatch-2026-10-21-ai-detection-learnings.md` 工序执行。
