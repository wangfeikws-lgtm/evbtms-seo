# 矿卡热管理调研简报（2026-10-20）

> 用途：为 EVLINK 矿卡页（https://evbtms.com/electric-mining-truck/）三模块文案提供公开可查的行业数据。
> 原则：只用公开可验证的行业数据＋EVLINK 已确认规格；**不编造 EVLINK 测试结果、客户名、案例**。

---

## 一、行业关键事实（带来源）

### 1. 矿山环境温度极端跨度大
- 采矿环境温度跨度：西伯利亚矿区低至 **-50°C**，智利阿塔卡马沙漠、澳大利亚 Pilbara 地区高于 **45°C**（来源：SUNHUNK 行业分析 https://www.sunhunk.com/about/groupnews-detail-590.htm ）
- 内蒙古华能伊敏露天矿：年温差超过 **60°C**，冬季低于 **-30°C**，其纯电动矿卡车队（100 台无人驾驶）可在 **-40°C** 下运行（来源：MachMall https://www.machmall.com/content-info/extreme-cold-challenge-unmanned-pure-electric-mining-trucks-pioneering-a-zero-carbon-future/1364 ）
- 电池需维持 **15–35°C** 工作温度，而矿山环境从高海拔 **-10°C** 到热带矿区 **45°C**（来源：Dataintelo 氢电矿卡市场报告 https://dataintelo.com/report/hydrogen-electric-mining-truck-market ）

### 2. 厂商公开的热管理设计温度
- LGMG（临工重机）电动矿卡：专用热管理系统设计温度 **-30°C 至 50°C**，3C 快充架构（来源：PR Newswire / BusinessWire 2026-10 发布 https://hkbusinesswire.com/lgmg-showcases-ultra-fast-charging-and-integrated-energy-solutions-for-mining-electrification/ ）
- 其快充数据：20%→90% 电量 23 分钟（测试条件），峰值充电功率约 3.6 MW（厂商自报）

### 3. 占空比与运行强度
- 露天矿卡年运行 **>5,000 小时**（来源：Dataintelo 报告，同上）
- 下坡连续制动是矿卡独有工况：超大型矿卡（总重 500+ 吨）在 10% 坡道下行时需**连续耗散 2 MW 以上功率、持续 10–15 分钟不停**（来源：Medium 行业科普 https://medium.com/@brakinggod/the-brakes-that-stop-500-tons-downhill-4c41eb56941c ）
- Caterpillar 793 电动原型车实测：满载 4.3 英里路线，10% 坡道上行 0.62 英里、下行 0.62 英里，下行段再生制动回收能量（来源：Equipment World https://www.equipmentworld.com/construction-equipment/heavy-equipment/off-road-trucks/article/15303756/caterpillars-first-batterypowered-mining-truck ）
- 学术仿真：满矿循环中制动能量回收率可达 **39.41%**（来源：MDPI 研究 https://www.mdpi.com/2032-6653/17/6/317 ）；电池 SOC 超过 92% 或环境温度超过 42°C 时，再生制动效果大幅下降，独立制动/耗散能力不可替代（来源：Solid Industry News https://www.solidindunews.com/news/Mining-Dump-Trucks/Articulated-Dump-Trucks/Can-articulated-dump-trucks-safely-operate-on-15-underground-gradients-under-ISO-21807-compliant-conditions.html ）

### 4. 电池热失控风险（无冷却工况）
- 学术研究（ScienceDirect）：40°C 环境、满载、无冷却时，矿卡电池最高温度达 **81.31°C**、温差 5.76°C，**双双超过安全阈值**；液冷＋相变材料耦合系统可把最高温度降低 43% 以上、温差控制在 5°C 内（来源：https://www.sciencedirect.com/science/article/abs/pii/S1290072925008622 ）
- 矿山昼夜温差 15°C 加剧电池热管理难度（同上）

### 5. 井下矿：通风与热
- 井下矿通风占总能耗高达 **40–50%**；柴油车改电动车可使通风需求下降 **40–50%**（来源：Stantec https://www.stantec.com/en/ideas/topic/covid-19/charged-up-key-considerations-around-electric-vehicle-use-on-mine-sites ；Canadian Mining Journal https://www.canadianminingjournal.com/featured-article/applying-the-3rs-to-mine-ventilation/ ）
- 但电池散热不会凭空消失：热量被排入矿井环境，车辆热设计必须与矿井通风/制冷系统一并评估（来源：YT Steels https://www.ytsteels.com/news/Green_Mining/Electric_Mining_Fleet/How_EV_battery_tech_thermal_management_affects_haul_truck_uptime.html ）
- 充电站本身也是热源：240 kW 充电套件局部通风需求 34 kcfm（来源：MDPI Mining 2026, 6, 90 https://mdpi-res.com/d_attachment/mining/mining-06-00090/article_deploy/mining-06-00090.pdf?version=1791015035 ）

### 6. 行业公开项目（可引用、不可冒充自家案例）
- **Caterpillar × Rio Tinto × BHP**：Pilbara 地区联合测试电池电动矿卡，Cat 793 于 2024 年下半年开始试用，Komatsu 930 于 2026 年试用（来源：Australian Trades 转 EV Report https://www.australiantrades.com/rio-tinto-and-bhp-collaborate-on-battery-electric-truck-trials-caterpillar-komatsu ）
- **LGMG 鄂尔多斯演示（2026-10）**：电动矿卡＋光伏＋储能＋兆瓦级充电在真实矿区联调（来源同第 2 条）
- **伊敏矿 100 台无人电动矿卡**：6 分钟自动换电，年替代柴油 15,000+ 吨、减排 CO₂ 48,000 吨（来源：MachMall，同第 1 条）

---

## 二、EVLINK 可安全宣称的（基于已确认规格）

以下规格均为 2026-10-13 已核实的 HVH-R1402 口径，可直接写：

| 规格 | 数值 | 与矿卡场景的对接点 |
|---|---|---|
| 连续功率 | 140 kW 连续 20 分钟 | 矿卡下坡连续制动 10–15 分钟的工况时长（行业事实见 1.3） |
| 工作温度 | -40 ~ +85°C | 覆盖公开报道的矿山极端温度（-50°C 极端值除外，不宣称） |
| 防护等级 | IP6K9K | 矿山粉尘＋高压水冲洗环境（可对标"粉尘/泥浆"场景描述） |
| 电压平台 | 450–850 V DC | 矿卡高压平台区间内 |
| 冷却方式 | 液冷 DN32 接口 | 行业主流：矿卡电池普遍用液冷（学术与厂商资料一致） |
| 安全 | NTC 温度传感＋高压互锁 | — |
| 测试 | 25 项测试已验证 | 只能说"完成 25 项测试"，**不说**通过了什么认证 |

**可写的表述示例（均为规格＋行业事实的组合，无编造）：**
- "Mining descents demand continuous braking for 10–15 minutes. The HVH-R1402 is rated 140 kW continuous for 20 minutes."
- "Mining sites span -40°C winters to +45°C desert heat. The unit operates from -40 to +85°C."
- "IP6K9K sealing for dust- and wash-down-heavy mine environments."

---

## 三、需 Peter 确认后才能写的（红线）

1. **任何具体客户/矿山名称**——无 EVLINK 矿卡交付证据，不得写"已用于 XX 矿"
2. **EVLINK 自家测试数据**（如实测温升、实测占空比曲线）——25 项测试的具体报告未公开前，只能说"25 tests verified"，不能编数字
3. **冷却流量**——172 vs 160 L/min 口径未决（T8 技术小尾巴），矿卡页**暂不写流量数字**
4. **BR-LC 150/250 kW 目标值**——设计目标非实测规格，不得引用
5. **MOQ / 交期**——未确认，页面不写
6. **-50°C 宣称**——产品口径是 -40°C 起，行业极端值 -50°C 只能作环境描述，不能说产品覆盖
7. **认证**——无已确认认证，不得写 CE/EMark/UL 等

---

## 四、建议文案角度（不需要编造数据）

### 模块 1：Validation for Harsh Mining Conditions
角度：**用行业工况定义"苛刻"，用产品规格回应**
- 矿山温度跨度（-40°C 冬季矿区至 +45°C 沙漠矿区，引用行业公开数据）
- 连续下坡制动 10–15 分钟 ≈ 100% 占空比——对应 140 kW/20 分钟连续额定
- 粉尘＋高压冲洗——对应 IP6K9K
- 写法：先讲工况（行业事实），再讲规格如何对位；不出现"我们测试了/客户验证了"

### 模块 2：Show the Proof Behind the Engineering
角度：**展示可验证物，不展示编造结果**
- 可展示：25 项测试的事实陈述（只列测试类别，如温度循环/振动/IP 防护——**类别清单需 Peter 从测试报告中确认**后再列）
- 可展示：产品实物图＋CAD 几何（已定视觉标准：圆柱形产品图；禁用老方形端子盒渲染图）
- 可展示：行业参照（Cat/Komatsu 公开试用、伊敏矿车队）说明"这条赛道已被验证"——明确标注为行业动态，非 EVLINK 案例

### 模块 3：Electric Mining Vehicle Thermal Project
角度：**项目制叙事：输入→评估→交付，不编案例**
- 结构：项目输入清单（坡度/海拔差、环境温度带、车辆总重、电压平台、制动策略）→ 工程评估流程 → 配置选项（纯电阻/电阻+斩波分体/斩波制动集成，三种已确认构型）
- CTA：Submit your route profile → duty-cycle sizing assessment
- 全程用"we evaluate / we size"，不用"we delivered to"

---

## 五、数据缺口（本简报未覆盖、后续如需再补）
- Komatsu 930 电动版公开热管理细节较少（厂商未披露），后续可跟踪其 2026 年 Pilbara 试用报道
- BELAZ 电动矿卡无公开热管理数据，本次未找到可靠来源，**不建议在文案中提及 BELAZ**
- 矿卡制动电阻专项的行业公开装机数据（非再生制动）公开资料稀少，建议文案走"连续制动能量耗散需求"角度而非引用装机量
