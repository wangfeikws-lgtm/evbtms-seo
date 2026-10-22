# 真人原文对照检测样本（2026-10-22）

> 用途：拿真人撰写的英文技术原文去测 ZeroGPT，分清分数高到底是"工具问题"还是"文本问题"。
> 用法：把每段样本**单独、原样**粘进 ZeroGPT 检测，逐段记录分数，再与我方稿件分数对照。样本一经改写对照即失效，故以下英文全部为原文照录（仅统一了引号字形与断行，措辞、标点、拼写错误均未动）。
> 选取标准：工业厂商/行业刊物的工程文本；优先选 LLM 普及（2022 年底）之前已出版的文本，从时间上排除 AI 代笔可能；内容须带真实计算或实测数据。

---

## 样本 1：ABB《Technical Guide No. 8 — Electrical Braking》

- **出处**：ABB Drives 技术指南系列第 8 册《Electrical Braking》（Rev. B），"Drive applications map according to speed and torque"一节。
- **抓取 URL**：https://docslib.org/download/5378036/technical-guide-no-8-electrical-braking （该指南全文镜像；原出版方为 ABB Drives）
- **词数**：约 312 词
- **为什么判定是真人原文**：ABB 技术指南系列是其驱动部门工程师编写的经典工程手册，该册初版年代远早于商用 LLM；文中英式拼写（utilised、behaviour）、"ie,"的欧式用法、围绕公式 (2.1)(2.2) 的推导语境，都是厂商工程文档的典型人工痕迹；内容是制动应用分类的经验性归纳，不是营销文案。

> Drive applications can be divided into three main categories according to speed and torque. The most common AC drive application is a single quadrant application where speed and torque always have the same direction, ie, the power flow (which is speed multiplied by torque) is from inverter to process. These applications are typically pump and fan applications having quadratic behaviour of load torque and thus often called variable torque applications. Some single quadrant applications such as extruders or conveyors are constant torque applications, ie, the load torque does not inherently change when speed changes. The second category is two-quadrant applications where the direction of rotation remains unchanged but the direction of torque can change, ie, the power flow may be from drive to motor or vice versa. The single quadrant drive may turn out to be two quadrants for example if a fan is decelerated faster than mechanical losses could naturally achieve. In many industries also the requirement for emergency stopping of machinery may require two-quadrant operation although the process itself is single quadrant type. The third category is fully four-quadrant applications where the direction of speed and torque can freely change. These applications are typically elevators, winches and cranes, but many machinery processes such as cutting, bending, weaving, and engine test benches may require repetitive speed and torque change. One can also mention single quadrant processes where the power flow is mainly from machinery to inverter such as in a winder or an uphill to downhill conveyor. It is commonly understood that from the energy saving point of view the AC motor combined with inverter is superior to mechanical control methods such as throttling. However, less attention is paid to the fact that many processes may inherently include power flow from process to drive, but how this braking energy could be utilised in the most economical way has not been considered.

---

## 样本 2：Kvaser《CAN Messages》教程页（CAN Protocol Tour 第 1 页）

- **出处**：Kvaser（CAN 接口厂商）官网 "Introduction to CAN / The CAN Protocol Tour" 教程系列，CAN Messages, page 1 of 3。
- **抓取 URL**：https://kvaser.com/about-can/the-can-protocol/can-messages-13/
- **词数**：约 349 词（含列表条目）
- **为什么判定是真人原文**：Kvaser 的 CAN 教程是该公司工程师维护多年的教学材料（其 CAN Protocol Tutorial PDF 在业内流传已久，成文于 LLM 出现之前）；行文带明显的个人讲解口吻——比如给 Data Frame 配的拟人小结 "Hello everyone, here's some data labeled X, hope you like it!" 和两处 "Note:" 旁注，这种随手补注的习惯是检测器最难模仿的人工特征。

> The CAN bus is a broadcast type of bus. This means that all nodes can "hear" all transmissions. There is no way to send a message to just a specific node; all nodes will invariably pick up all traffic. The CAN hardware, however, provides local filtering so that each node may react only on the interesting messages.
>
> CAN uses short messages – the maximum utility load is 94 bits. There is no explicit address in the messages; instead, the messages can be said to be contents-addressed, that is, their contents implicitly determines their address.
>
> There are four different message types (or "frames") on a CAN bus: the Data Frame, the Remote Frame, the Error Frame, and the Overload Frame.
>
> The Data Frame is the most common message type. It comprises the following major parts (a few details are omitted for the sake of brevity):
>
> - the Arbitration Field, which determines the priority of the message when two or more nodes are contending for the bus. The Arbitration Field contains: For CAN 2.0A, an 11-bit Identifier and one bit, the RTR bit, which is dominant for data frames. For CAN 2.0B, a 29-bit Identifier (which also contains two recessive bits: SRR and IDE) and the RTR bit.
> - the Data Field, which contains zero to eight bytes of data.
> - the CRC Field, which contains a 15-bit checksum calculated on most parts of the message. This checksum is used for error detection.
> - an Acknowledgement Slot; any CAN controller that has been able to correctly receive the message sends an Acknowledgement bit at the end of each message. The transmitter checks for the presence of the Acknowledge bit and retransmits the message if no acknowledge was detected.
>
> Note 1: It is worth noting that the presence of an Acknowledgement Bit on the bus does not mean that any of the intended addressees has received the message. The only thing we know is that one or more nodes on the bus has received it correctly.
>
> Note 2: The Identifier in the Arbitration Field is not, despite of its name, necessarily identifying the contents of the message.

---

## 样本 3：Schneider Electric 官方 FAQ FA376712《What is the criteria for braking resistor selection?》

- **出处**：Schneider Electric 官方支持 FAQ（编号 FA376712，Altivar ATV930 制动电阻选型），页面标注 2019-06-07 发布。
- **抓取 URL**：https://www.se.com/vn/vi/faqs/FA376712/ （越南站镜像，内容与全球站同一 FAQ 编号）
- **词数**：约 313 词
- **为什么判定是真人原文**：发布于 2019 年，时间上排除 AI 代笔；作者是厂商支持工程师，文本里留着非母语人工痕迹——"must be equal or greater **then**"（then/than 误用）、"This **criteria** has nothing to do with resistance"（单复数错误）——这类错误恰恰是真人快写支持文档的指纹；且带真实机型计算（ATV930D22N4、785V、Rmax = 785²/(1.2×22000) = 23 Ω）。

> Selection of braking resistor must respect 3 criteria:
>
> 1. Resistance of braking resistor must be equal or greater then minimal allowed resistance Rmin
> 2. Resistance of braking resistor must be equal or less then maximal resistance Rmax
> 3. Power of the braking resistor must be adequate to load and load cycle
>
> 1. Each ATV requires that resistance of braking resistor must be above min value. The purpose is to prevent braking transistor from damage because when transistor is conductive, it is only the resistance of braking resistor that limits the current via braking transistor. Min values for each ATV size can be found in dedicated ATV document, i.e. installation manual.
>
> Example ATV930D22N4 says that Rmin is 15 Ohms
>
> 2. The resistor's resistance has also to be below certain value, otherwise when braking transistor is permanently conductive, the resistor will not be able to absorb peak power. There is no risk of damage if resistance of braking resistor is above the max value, but only the braking power will be reduced.
>
> Information about maximal resistance is sometimes missing in ATV document. However it can be easily calculated. Considering the level of DC bus voltage when braking transistor operates (785V for ATV...N4 drives) and by defining that peak power must be at least equal (or greater) then ATV power including overload, we can write:
>
> peak power Pmax=Udc^2 / R > ATV max power
>
> If we have drive that allows 1.2 times overload we will get:
>
> Rmax = Udc^2 / ATV max power = Udc^2/ (1.2* ATV rated power)
>
> Example: In case of ATV930D22N4 we get Rmax = 785^2 / (1.2*22000) = 23 Ohms
>
> 3. This criteria has nothing to do with resistance, but with the power. Power of braking resistor must be selected with respect to the load and load cycle. Usually it requires calculation of average braking power or you can use values defined for some typical load cycles in catalog.

---

## 样本 4：Electronics Cooling《Direct-Die Liquid Cooling: A Scalable Approach for Power Module Thermal Integration》

- **出处**：行业刊物《Electronics Cooling》技术文章（功率模块热管理/液冷），Introduction、Technical Approach 两节。
- **抓取 URL**：https://www.electronics-cooling.com/2025/11/direct-die-liquid-cooling-a-scalable-approach-for-power-module-thermal-integration/
- **词数**：约 360 词（含后段耐久试验一节）
- **为什么判定是真人原文（附保留意见）**：作者是做 DBC 液冷板的从业工程师，文中参数全部来自自家实验记录（原文后段有 35,000 小时自来水耐久试验、通道腐蚀 50–70 μm 等一次数据），这类一次实测数据不是通用文本能编出来的。**保留意见**：该文发表于 2025 年，时间上无法像样本 1–3 那样天然排除 AI 辅助；若要一组"绝对干净"的对照，只用样本 1–3，此样本作为"当代行业刊物工程文"的参照系使用。

> The push toward electrification across transportation — rail, marine, aviation, and ground vehicles — brings significant benefits such as lower emissions, quieter operation, and reduced dependency on fossil fuels. However, it also places higher demands on power electronic systems, requiring efficient thermal management to handle increasing power densities. Emerging wide-bandgap semiconductors, like Gallium Nitride (GaN) and Silicon Carbide (SiC), are highly efficient but introduce thermal challenges due to smaller die footprints and higher heat flux. To mitigate this, active cooling systems such as pumped liquid cooling are deployed. This method provides more precise temperature control compared to passive or forced-air cooling, thereby enhancing the reliability and performance of systems operating in extreme environments.
>
> Typical high-power modules like IGBT packs employ a layered structure: die mounted on a DBC substrate, which is then soldered to a copper or AlSiC baseplate. The whole assembly is bolted to a cold plate. Each interface — solder joints, thermal interface materials (TIMs), and baseplates — adds thermal resistance, that impacts heat removal.
>
> Key problems:
> - Many thermal interfaces between the die and coolant.
> - Material mismatches in coefficient of thermal expansion (CTE).
> - Dependence on surface flatness, flow channel geometry, and coolant performance.
>
> Improving thermal paths and minimizing resistances are critical for maintaining optimal junction temperatures, extending module lifespan, and supporting high-power-density applications.
>
> To address these challenges, the proposed solution involves embedding the DBC substrate into the cold plate. Copper and ceramic (Al₂O₃ or AlN) are joined using a high-temperature process, forming a robust monolithic structure. This integrated design maintains the electrical isolation provided by ceramics while embedding coolant channels directly under the heat source.
>
> This integration:
> - Eliminates the baseplate and its associated thermal resistance.
> - Removes external TIMs (TIM2) between module and cold plate.
> - Reduces total thermal resistance between the junction and the coolant.
>
> （同文后段 "Lifetime Testing with Water Coolant" 一节）To validate long-term reliability, DBC-based liquid cold plates were subjected to endurance testing using water as a coolant in a closed-loop system. A diode laser application was selected due to its high thermal load and continuous operation demands. Over 35,000 operational hours were recorded using unconditioned tap water, rather than deionized water or water with additives like antifreeze or biocides.

---

## 记录表（检测时填）

| 样本 | 来源 | 词数 | ZeroGPT AI% | 备注 |
|---|---|---|---|---|
| 1 | ABB Technical Guide No. 8 | ~312 | | |
| 2 | Kvaser CAN Messages 教程 | ~349 | | |
| 3 | Schneider Electric FAQ FA376712（2019） | ~313 | | |
| 4 | Electronics Cooling（2025，参照系） | ~360 | | |
| 对照 | HVCH CAN v2 重写稿（同批交稿） | ~1,900 | | | |
| 对照 | T8-4 计算密集稿（已知 7%） | | | |
