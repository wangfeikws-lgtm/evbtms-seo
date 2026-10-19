# T12-W1｜evptc.com 第一周 5 篇英文文章 SERP 简报与详细大纲

- 调研日期：2026-10-19
- 目标站：https://www.evptc.com/
- 工作边界：本文件只完成真实 SERP 意图核对与大纲；Peter 批准后才写英文全文和发布包。
- 事实口径：产品参数只用 `evptc-official-spec-summary.md`。旧站产品页出现的 250–870V、15–25kW、>95%、10 年寿命、客户/市场份额等冲突信息均不得继承。
- 共同写作要求：厂家第一人称但不杜撰车间或客户细节；每篇回答“什么时候用、怎么选、何时不适用”；不用绝对化词汇；每个关键数据写作阶段标注 Verified / Unverified / Unsupported。

## SERP 总判断

1. 选型词当前结果混合产品页、供应商指南和 HVCH 产品目录；大多只列功率和电压，缺少完整输入清单和“先算热负荷再选型号”的采购路径。EVLINK 应做工程选型清单，而不是泛科普。
2. `CAN vs thermostat` 是低覆盖、意图模糊词；SERP 几乎没有直接比较页，机会在于解释“车辆级联动/诊断”与“独立温控、无外部控制”的边界，严禁把恒温器写成 CAN 的廉价替代。
3. `electric bus battery preheating` 结果由政府和研究机构主导，核心意图是车队冷天运营、插枪预调温、冷浸、出车可靠性，而非单一产品广告。
4. `PTC heater vs heat pump` 结果以对比和决策页为主，强烈要求诚实结论：温和气候效率优先时热泵更合适，极寒、高热负荷或冗余时 PTC 或混合架构更合理。
5. `winter EV bus range loss` 结果由政府、研究和媒体数据主导。标题里的“40%”只能作为有出处的特定车队或工况范围，不可写成所有电动公交的普遍结论。

## 1｜选型篇

### Proposed title

**How to Choose a High-Voltage PTC Coolant Heater: 7 Inputs Bus and Truck OEMs Must Define**

### Primary intent / keyword

- Intent：commercial investigation + engineering selection
- Primary：how to choose high voltage coolant heater
- Secondary：PTC coolant heater for electric bus; high voltage heater selection; HVCH sizing inputs

### SERP content pattern

- 高排位结果常见：HVCH 定义、应用列表、功率/电压表、供应商 CTA。
- 信息缺口：缺少“不能只看 kW”的输入顺序、控制接口、安装边界、冷却回路和询价资料清单。

### Search promise / direct answer

选 HVCH 不能从目录里的功率数字开始；OEM 必须先冻结热负荷、HV/LV 平台、控制方式、冷却回路、安装包络、环境与防护需求、诊断/安全接口，再把这些输入映射到候选系列。

### Detailed outline

1. **Why rated power alone is not a selection method**
   - 区分系统热负荷、加热器额定功率、实际受电压、流量和入口温度约束的可用输出。
2. **Input 1: Required heat load and warm-up target**
   - 舱内、动力电池或两者；目标温升与允许升温时间；不得在无系统数据时承诺升温时间。
3. **Input 2: High-voltage and low-voltage architecture**
   - 额定、最小和最大母线电压；24V 控制电源等由项目确认。
4. **Input 3: Control and diagnostics**
   - CAN、使能信号、目标温度或功率请求、状态与故障反馈。
5. **Input 4: Coolant-loop conditions**
   - 介质、入口温度、流量、压降、系统耐压均需客户提供；官方汇总未给数值，正文不可猜。
6. **Input 5: Vehicle duty cycle and ambient conditions**
   - 连续或间歇、冷浸、公交频繁开门、卡车长时间工况。
7. **Input 6: Packaging and connectors**
   - 安装空间、重量、方向、HV/LV 接插件；A 系列变体 AZ、AN01、AN02 可作为询价确认项。
8. **Input 7: Protection, EMC and compliance requirements**
   - 仅用官方口径：IP67、ISO 11452 Class 3、过欠压、过流、短路、过热保护；认证声明以项目证书核对后为准。
9. **EVLINK shortlist example—not a final selection**
   - A：6–18kW、400–800V、5.1kg、350×184×120mm、CAN + Enable。
   - Q：15–35kW、400–1100V、12kg、346×268×123mm、CAN + Enable。
   - 强调最终选型必须由 7 项输入确认。
10. **RFQ checklist table**
    - Vehicle / application / heat load / HV min-nom-max / LV / coolant / flow / inlet temp / ambient / control / package / connector / annual volume / validation needs。

### Fact boundary

- Verified：A/Q 上述官方参数；通用 IP67、工作温度 -40~+85℃、绝缘 ≥100MΩ、ISO 11452 Class 3、保护功能、2 年质保。
- Unverified before publication：效率、流量、压降、升温时间、寿命小时、MOQ、交期、具体认证编号。
- Special conflict：QA01 在官方汇总中按 Peter 实物确认为 A 系列，但旧站多页写成 Q/15–25kW；正文只写 “A-series configuration; exact naming to be confirmed in RFQ”，除非 Peter 最终确认。

### Internal links

- Primary product target（需先核对页面参数与官方表一致）：https://www.evptc.com/sale-40669478-hvch-high-voltage-coolant-heater-for-geely-group-ev.html
- Product hub：https://www.evptc.com/products.html
- Related article：现有 HVCH 工作原理文章（发布包阶段填正式 URL）。

### CTA

“Send the seven application inputs and our engineering team will return a series shortlist and the missing validation questions—not a guess based on kW alone.”

### Peter confirmation

- QA01 最终公开归属或命名是否明确写 “A Series”。
- 是否允许文章展示 A/Q 两行参数表及 CE/E-Mark/UL 通用认证表述。

---

## 2｜控制篇

### Proposed title

**CAN-Controlled vs Thermostat-Controlled HVCH: Which Architecture Fits Your Vehicle?**

### Primary intent / keyword

- Intent：engineering comparison / integration decision
- Primary：CAN vs thermostat heater control
- Secondary：CAN controlled HVCH; thermostat controlled coolant heater; EV heater control architecture

### SERP content pattern

- 精确比较页稀缺；相关结果主要是 CAN 驱动文档、产品数据表和普通恒温器解释。
- 排名机会来自清晰决策矩阵，而不是泛讲 CAN 协议。

### Search promise / direct answer

CAN 控制适合需要 VCU/BMS 协同、可变功率请求、状态或故障回传和车辆级诊断的项目；恒温器控制适合目标温度固定、控制独立、无需车辆网络交互的简单回路。选择依据是系统架构，不是“谁更先进”。

### Detailed outline

1. **The two architectures in one diagram**
   - CAN + Enable：vehicle controller ↔ heater controller ↔ coolant loop。
   - Thermostat：local temperature device/switch → heater, no external network control。
2. **What CAN control enables**
   - 目标功率或温度请求、限功率、故障或状态回传、与 VCU/BMS 联动；具体报文或 DBC 需项目确认。
3. **What thermostat control simplifies**
   - 独立回路、固定控制逻辑、较少的网络集成；不能暗示无安全控制。
4. **Decision matrix**
   - Variable demand / remote diagnostics / fleet fault logs / multi-loop coordination → CAN。
   - Fixed local setpoint / standalone auxiliary loop / no vehicle CAN dependency → thermostat。
5. **Failure and service questions buyers should ask**
   - 通讯丢失时策略、传感器故障、默认安全状态、故障码、维修诊断入口——都列为项目问题，不编答案。
6. **EVLINK product mapping**
   - A/B/K/Q/H/Z/W：CAN + Enable。
   - E：20–24kW、400–800V、8.5kg、370×192×98mm、thermostat / no external control。
   - N：2kW、200–1000V、1.22kg、temperature sensor/switch；仅用于说明另一种简单控制边界，不与 E 混同。
7. **When neither off-the-shelf option is enough**
   - 需要自定义报文、冗余、功能安全文档或特定故障处理时先技术评审。
8. **Integration checklist**
   - CAN protocol / baud / DBC、enable logic、setpoint owner、feedback signals、fault strategy、sensor ownership、validation plan。

### Fact boundary

- Verified：各系列控制方式与 E/N 官方参数。
- Unverified：CAN 2.0 或波特率（HVCH 官方汇总未明确，不能从 BTMS 250kbps 借用）、报文周期、诊断服务、恒温上下限、功能安全等级。

### Internal links

- Product hub：https://www.evptc.com/products.html
- E-series exact page：未在 SERP 确认，发布包前从后台或站内清单定位正式 URL，不用错误页面代替。
- Cross-link：W1 第 1 篇选型指南。

### CTA

“Send your control ownership diagram and required I/O list; EVLINK will confirm whether a CAN-controlled series or a standalone thermostat architecture is the cleaner fit.”

### Peter confirmation

- E 系列“无外部控制”是否允许公开解释为本地恒温器控制。
- 能否提供 E 系列正式产品 URL 及其温控范围或设定方式。

---

## 3｜-30°C 预热篇

### Proposed title

**Electric Bus Battery Preheating at −30°C: Five Planning Mistakes That Cost Range and Dispatch Time**

### Primary intent / keyword

- Intent：fleet operations + engineering planning
- Primary：electric bus battery preheating
- Secondary：electric bus cold weather preconditioning; battery preheating −30°C; electric bus winter operation

### SERP content pattern

- 政府与研究结果强调：插枪状态预调温、冷浸、电池和舱内共同热负荷、车队调度或充电策略。
- 竞争内容常给通用“预热有益”，但少把采购输入和 HVCH 选型连接起来。

### Search promise / direct answer

−30°C 场景的问题不是“装一个更大加热器”就结束；车队必须同时规划冷浸时间、插枪预调温、动力电池与舱内热负荷、可用充电功率、冷却回路和出车窗口。

### Detailed outline

1. **What cold soak changes before the bus moves**
   - 电池可用能量或充电接受能力下降、舱体和冷却液都是冷的、加热会占用牵引电量。
2. **Mistake 1: preheating after unplugging**
   - 政府指南建议尽量在插枪时预调温，以保留路线能量。
3. **Mistake 2: treating battery and cabin loads as one number**
   - 公交频繁开门增加舱内热负荷；电池回路有独立目标，需系统热平衡。
4. **Mistake 3: sizing from ambient temperature alone**
   - 还需电池质量、初温、目标温度、允许时间、冷却回路损失；无数据不得承诺多久升温。
5. **Mistake 4: ignoring charger/depot constraints**
   - 充电功率、室内或室外停放、出车排班决定预调温策略。
6. **Mistake 5: no control and fallback plan**
   - VCU/BMS 请求、流量确认、过热保护、通讯故障策略、极寒时备用运营方案。
7. **HVCH selection window for a bus project**
   - Q 系列可作为 15–35kW、400–1100V 的候选范围；不是“−30°C 保证值”。
8. **Fleet worksheet**
   - Overnight ambient / parking / plug-in availability / departure / pack data / cabin load / HV range / loop data / route reserve / validation temperatures。
9. **What to validate before SOP**
   - 冷浸试验、目标温度达成时间、能耗、故障处理、连续多班次表现；没有 EVLINK 实测数据时全部写成验证项目。

### Evidence boundary

- 可引用外部来源：Joint Office / DriveElectric 政府指南指出插枪预调温可保留行驶能量，冷浸电池加热可能耗时较长：https://driveelectric.gov/files/transit-cold-weather-help-sheet.pdf
- 可引用研究摘要：两年 7 辆 BEB 研究发现电池加热约占寒冷天气新增能耗的一半（应准确归因，不外推）：https://www.sciencedirect.com/science/article/pii/S1361920925002196
- Verified product：Q 15–35kW / 400–1100V / 12kg / CAN + Enable / IP67 / −40~+85℃。
- 禁止：声称 EVLINK 在 −30°C 下达到某升温时间、续航提升百分比或已用于某车队，除非 Peter 提供报告。

### Internal links

- Q-series：https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
- Existing Q test article：https://www.evptc.com/news/evlink-successfully-validates-q-series-ptc-coolant-heaters-in-joint-testing-with-shanghai-university-371383.html （只能写“实验室水循环和通电性能测试记录”，不能写第三方认证或 −30°C 证明）
- Cross-link：W1 第 1 篇选型指南。

### CTA

“Send the cold-soak temperature, pack and cabin heat-load targets, departure window, charger availability and coolant-loop data for an engineering preheating review.”

### Peter confirmation

- 是否保留标题中的 −30°C 作为场景条件而非产品性能声明。
- 是否有可公开的冷浸测试报告；没有则正文只讲设计与验证方法。

---

## 4｜PTC vs 热泵篇

### Proposed title

**PTC Coolant Heater vs Heat Pump for Commercial EVs: Where Each System Wins**

### Primary intent / keyword

- Intent：comparison / architecture decision
- Primary：PTC heater vs heat pump
- Secondary：commercial EV heating system; PTC coolant heater heat pump backup; electric bus heating comparison

### SERP content pattern

- 主流页按效率、低温性能、复杂度、响应和成本比较。
- 常见问题是把结论写成“PTC 永远更好”或给无出处的温度或 COP 阈值。
- 信息增益应是按商业车辆任务周期给决策树，并明确混合架构。

### Search promise / direct answer

温和气候、长时间稳定加热且能利用环境或余热时，热泵通常更节能；高热负荷、快速升温、极寒冗余或系统简化优先时，PTC 更直接；很多商业车辆合理答案是热泵 + PTC，而不是二选一。

### Detailed outline

1. **How each system moves or creates heat**
   - PTC 把电能转为热；热泵搬运热量。只做原理级解释。
2. **Comparison table**
   - Energy efficiency：heat pump advantage under suitable conditions。
   - Cold/high-load robustness：PTC output is architecture-simple, but actual output depends on supply/loop conditions。
   - System complexity：heat pump includes compressor/refrigerant components；PTC coolant heater needs HV electrical + coolant integration。
   - Response/defrost/backup：由整车策略决定，不给未经验证秒数。
   - Service：制冷剂系统和高压冷却液加热器有不同技能或工具需求。
3. **Decision case A: urban bus in moderate winter**
   - 长时运行或效率优先 → 先评估热泵，PTC 作峰值或冗余。
4. **Decision case B: heavy truck or bus with high peak heat demand**
   - 需要 15–35kW 候选与可控输出 → Q 系列可进入评估，但必须算系统热负荷。
5. **Decision case C: extreme cold and fixed dispatch time**
   - 混合架构、插枪预调温和备用容量比单一设备宣传更重要。
6. **When PTC is not the best answer**
   - 温和气候、能源消耗最优是首要且热泵系统已有足够能力时，不应为卖产品强推纯 PTC。
7. **When heat pump is not enough alone**
   - 是否需要补热应由低温能力曲线、除霜、出车要求和系统验证决定，不写固定 −10°C 阈值。
8. **Architecture input checklist**
   - Climate histogram / duty cycle / cabin+battery load / waste heat / refrigerant loop / redundancy / HV budget / service capability。

### Evidence boundary

- 外部技术来源可引用：TI EV 热管理概述：https://www.ti.com/lit/wp/szzy015a/szzy015a.pdf
- 同车型实验比较可作为“条件依赖”的证据，不用于 EVLINK 产品性能：https://doi.org/10.3390/wevj17040168
- Verified product only：Q 系列 15–35kW、400–1100V、CAN + Enable 及通用保护口径。
- 禁止：无来源的“热泵低于某温度失效”、3–5 倍成本、PTC 固定效率、EVLINK 节省 X% 续航。

### Internal links

- Q-series：https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
- Product hub：https://www.evptc.com/products.html
- Cross-link：W1 第 3 篇预热文章 + W1 第 1 篇选型文章。

### CTA

“Share the climate, route duty cycle, battery/cabin heat loads and existing refrigerant/coolant architecture; EVLINK will help define whether PTC should be primary, auxiliary or unnecessary.”

### Peter confirmation

- 是否接受明确写“某些温和气候项目热泵更合适”。
- 是否有允许公开的 PTC + 热泵组合架构图。

---

## 5｜冬季续航篇

### Proposed title

**Why Electric Bus Range Falls in Winter—and the Five Levers Fleet Managers Can Actually Control**

> 不建议继续用绝对标题 “Why Winter Cuts E-Bus Range by 40%”。40% 是某些车队或工况观察值，不是通用规律。若 Peter 坚持，可改为：**When Winter Cuts E-Bus Range by Around 40%: A Fleet Planning Checklist**，正文首段必须解释范围差异。

### Primary intent / keyword

- Intent：fleet problem-solving
- Primary：winter electric bus range loss
- Secondary：electric bus cold weather range; e-bus winter operations; electric bus heating energy

### SERP content pattern

- 权威结果解释电池低温、舱内 HVAC、预调温、路线或充电计划。
- 用户需要的是可控措施，不是“冷天续航差”的重复说明。

### Search promise / direct answer

冬季续航下降来自多个变量：电池在低温下效率或可用能量变化、舱内与电池加热负荷、频繁开门、冷浸、路线与充电策略。车队可控制的是插枪预调温、热负荷或控制策略、路线储备、停放或充电条件和数据化验证，而不是用一个 40% 数字替代规划。

### Detailed outline

1. **Range loss is a range, not a universal 40%**
   - 不同车型、路线、温度和加热系统差异大。
2. **Where the winter energy goes**
   - 电池温控、舱内热负荷或除霜、低温电池效率、辅助系统、路线与怠速。
3. **Lever 1: precondition while connected**
   - 把预热能量尽量从电网而非路线电池中获取。
4. **Lever 2: separate battery, cabin and defrost requirements**
   - 避免一个温度目标或一个功率覆盖所有回路。
5. **Lever 3: size heat capacity from the coldest duty case**
   - 路线、频繁开门、乘员、冷浸、温升时间；不是只看平均气温。
6. **Lever 4: protect operational reserve**
   - 冬季 SOC 储备、机会充电、极端天气备用车辆或班次策略。
7. **Lever 5: measure by route and temperature**
   - 建议记录 ambient / HVAC kWh / traction kWh / idle / charging / route / passenger load；用本车队数据更新模型。
8. **Where an HVCH helps—and where it does not**
   - 作为电池或舱内冷却液回路的可控热源；不能修复小电池、低效车身保温、不足充电或错误排班。
9. **Fleet-to-supplier RFQ block**
   - 车辆电压、目标功率、冷却条件、控制、环境、防护、验证计划。

### Evidence boundary

- 美国能源部 AFDC 指出极寒中加热需求可使某些校车续航下降最高约 50%，必须表述为 “up to / specific conditions”：https://afdc.energy.gov/guides/electric-school-bus
- NREL 帮助单示例提到一项公交研究约 33% 下降，不可泛化：https://www.nrel.gov/docs/fy24osti/87940.pdf
- Cornell 对特定 7 辆公交数据报道寒冷天气能耗增加 48%（−4 至 0°C），是能耗，不等同续航下降：https://news.cornell.edu/stories/2025/05/electric-buses-dont-cold-study-finds
- 官方产品事实可用于解决方案框：Q 15–35kW、400–1100V、CAN + Enable；不得声称可恢复 40% 续航。

### Internal links

- Q-series：https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
- Product hub：https://www.evptc.com/products.html
- Cross-links：W1 第 3 篇预热 + W1 第 4 篇 PTC vs Heat Pump。

### CTA

“Send one cold-week route dataset plus your voltage, heating and coolant-loop inputs; EVLINK can help convert the fleet problem into an HVCH requirement and validation checklist.”

### Peter confirmation

- 批准删除通用“40%”绝对标题，改为范围或条件表达。
- 是否有车队匿名数据可用于信息增益；没有则只使用公开第三方证据。

---

## Peter 一次审核清单（只需回复选项）

1. 5 个方向：全部通过 / 指定编号修改。
2. QA01 公开归属：A Series / 暂不写系列名。
3. 认证表述：允许写 CE/E-Mark/UL 通用 / 仅写 “project documentation available on request”。
4. 第 4 篇立场：允许明确承认温和气候下热泵可能更合适：是 / 否。
5. 第 5 篇标题：A 删除 40%（推荐） / B 保留 “around 40%” 并限定条件。
6. −30°C：仅作设计场景 / 有可公开测试报告另行提供。

## 交付状态

- SERP：5/5 完成。
- 大纲：5/5 完成。
- 正文：等待 Peter 一次审核后启动。
- 发布：未执行。
