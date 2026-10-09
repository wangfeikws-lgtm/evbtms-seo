# T11 SERP 简报：电动车热管理控制策略（压缩机/膨胀阀/风机）

> 日期：2026-10-09｜状态：SERP 完成，待 Peter 批大纲（批后才写正文）
> 控制逻辑基线（工厂 Q&A 已验证，**写文案时只许用这些，不许编**）：
> - 压缩机：按系统水温和目标温度调速；水温升高→转速提高，水温降低→转速降低
> - 膨胀阀：按过热度控制；过热度高→开度增大，过热度低→开度减小
> - 风机：按冷凝器高压压力控制；示例约 13 bar 启动；启停压力/转速曲线可按项目标定
> - CAN 协议、CAN ID、波特率、控制逻辑可定制；可适配客户自有压缩机（需对方提供技术/电机参数）

## 一、跑过的查询

1. `EV thermal management control strategy compressor expansion valve fan`
2. `electric vehicle heat pump control strategy superheat expansion valve`
3. `battery thermal management system control logic sensors actuators`

## 二、搜索意图判定

**Informational（信息型）＋工程深度。** 搜的人是热管理工程师、系统集成商，想搞懂"压缩机/膨胀阀/风机到底按什么逻辑联动"。英文 SERP 现状两极分化：
- 学术端：MDPI/Springer 论文、Google Patents（控制算法、MPC、过热度专利）——深但难读，不面向买家
- 业余端：GitHub 上 Arduino/ESP32 的 DIY 电池热管理项目——与商用车采购意图完全错位

**结论：中间层断裂，GO。** 没有一篇"厂家工程师用大白话讲清三个控制环"的文章。我们的验证过的控制逻辑（水温→压缩机、过热度→膨胀阀、压力→风机）恰好填这个空，且与学术界的主流做法一致（见下），可信度高。

## 三、竞争页面结构观察

- **MDPI《Demand-Based Control Design for Efficient Heat Pump Operation of EVs》**：核心证据页。它的"基础控制算法"正是三个环：压缩机 PI 调速（跟踪目标送风温度）、**膨胀阀 PI 控制保持蒸发器出口过热度 5K**（防压缩机液击）、座舱风机 PI 调风量（跟踪座舱温度）。结构 = 控制目标 → 每个执行器的控制律 → 仿真验证。这是我们"三个环"划分的学术背书，写文案时可引用"过热度维持 ~5K 是行业常见做法"。
- **Google Patent CN103245154B（汽车空调电子膨胀阀过热度控制）**：关键技巧——用**压缩机转速做膨胀阀开度的前馈预调**，再叠加过热度反馈微调，减少调节幅度。这验证了"压缩机与膨胀阀必须联动、且最好在同一个控制器里做"的论点，是 T10/T11 互链的天然桥梁。
- **MDPI《Advanced Control Strategies for EV Cabin AC: A Review》**：综述了 MPC/强化学习等高级策略 vs 规则控制的节能对比。告诉我们：读者分两层——一层要"能落地的规则控制"（我们的受众），一层追学术前沿（不是我们的受众）。本文定位前者，不写 MPC 公式。
- **GitHub DIY 项目群**（thermo-guardian、btms-by-pb 等）：阈值＋迟滞的简易逻辑，Arduino 级。反面参照：商用车不能靠这种逻辑，引出"车规级集成控制器"的价值。
- **缺口**：没有厂家把真实产品的三个控制环（传感器→执行器→标定）讲透——本文的位置。

## 四、标题备选（3 选 1，需 Peter 定）

1. **EV Thermal Management Control Strategy: How Compressor, Expansion Valve and Fan Work Together**（推荐：关键词全，意图正）
2. **Inside an Integrated Thermal Controller: Three Control Loops Explained**（与产品绑定最紧，询盘导向）
3. **Compressor Speed, Superheat and Condenser Pressure: EV Thermal Control Logic That Works**（工程师口吻，技术社区传播性强）

## 五、关键词

- 主关键词：`EV thermal management control strategy`
- 次关键词：`electronic expansion valve superheat control`、`electric compressor speed control`、`condenser fan pressure control`、`integrated thermal management controller`、`battery thermal management control logic`

## 六、文章大纲（~1500–2000 词）

**Intro（~150 字）**：热管理拼的不是部件，是控制策略——再好的压缩机，控制逻辑差照样费电。本文拆开三个控制环：压缩机、膨胀阀、风机各自听谁的、为什么。

### H2：The three actuators — and what each one really controls
- 压缩机 = 制冷量（转速决定循环工质流量）
- 膨胀阀 = 制冷剂流量分配（开度决定过热度）
- 风机 = 散热能力（转速决定冷凝器换热）
- 学术背书：MDPI 需求型控制——三个执行器各有各的 PI 环（简述，不展开公式）

### H2：Loop 1 — Compressor speed follows water temperature
- 工厂逻辑：系统水温升高→转速提高；水温降低→转速降低（目标温度为基准）
- 为什么听水温的：水温是系统冷量需求的直接代理信号；连续调速 vs 启停——避免频繁启停的能耗与机械冲击
- 工程意义：制冷量与需求成比例，能耗不浪费

### H2：Loop 2 — Expansion valve follows superheat
- 工厂逻辑：过热度高→开度增大；过热度低→开度减小
- 过热度是什么（一句话科普：蒸发器出口制冷剂温度与饱和温度之差）
- 为什么重要：过热度过低→液态制冷剂进压缩机（液击，致命）；过热度过高→蒸发器利用率低（费电）
- 行业做法：维持 ~5K 过热度是常见目标（引用 MDPI 论文口径，注明"常见做法、按项目标定"）
- 进阶技巧：压缩机转速前馈＋过热度反馈（引用专利 CN103245154B 的思路，说明为什么两个环要在一个控制器里——CAN 延迟和数据共享）

### H2：Loop 3 — Fan follows condenser pressure
- 工厂逻辑：按冷凝器高压压力控制；示例约 13 bar 启动风机；启停压力/转速曲线可按项目标定
- 为什么听压力不听温度：高压压力直接反映冷凝负荷与换热需求；压力信号响应快
- 标定空间：启停压力点、转速曲线按车辆项目标定（工厂原话"可按项目标定"）

### H2：Why the three loops belong in ONE controller
- 三个环互相耦合：压缩机转速变了，过热度跟着变，冷凝压力跟着变——分立控制器之间靠 CAN 协调，有延迟、有标定割裂
- 集成控制器：共享传感器数据、统一时序、无通信延迟（呼应 T10，互链）
- 定制：CAN 协议/ID/波特率/控制逻辑可按项目定制（工厂原话）

### H2：Three control mistakes that waste energy（反面清单，工程师共鸣）
1. 膨胀阀 hunting（开度振荡）——过热度控制没调好
2. 压缩机频繁启停——缺连续调速或水温环没做好
3. 风机常转——缺压力控制，全年满转费电
- CTA：提供压缩机技术/电机参数＋系统目标，获取控制逻辑配置建议

**Sources & notes（不发布）**：MDPI Demand-Based Control（压缩机 PI/过热度 5K/风机 PI）；专利 CN103245154B（转速前馈＋过热度反馈）；MDPI 综述（规则控制 vs 高级策略的定位依据）；工厂 Q&A（三环逻辑原文、13 bar 示例、标定口径）。
**红线**：13 bar 必须标注为"示例值、按项目标定"；不写具体过热度目标值（写"~5K 为行业常见做法、按项目标定"）；不编压缩机功率、CAN 报文、认证；三个环的因果方向严格按工厂 Q&A（水温→转速、过热度→开度、压力→风机），不得反转。
