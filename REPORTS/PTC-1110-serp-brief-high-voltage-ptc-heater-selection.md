# SERP Brief：High Voltage PTC Heater Selection Guide for EVs（PTC-1110，2026-11-10，Muse 写＋发）

立项卡：目标词 high voltage ptc heater（美国 50/月、KD 4%、商业意图）；读者：电动车／电巴热管理选型工程师与采购；转化动作：读完去产品页／发询盘；页面类型：选型指南文章；风险：低（事实均已核实，无认证宣称）。

## 关键词（SEMrush 美国库，2026-11-09）
- 主词：high voltage ptc heater — 美国 50/月、KD 4%、意图商业（C）。
- 核心词（Peter 2026-11-09 定，正文重点词，后天单开一篇）：high voltage coolant heater — 美国 20/月、KD 不可用；对应产品页 https://evbtms.com/products/high-voltage-coolant-heater/（一词一页）。
- 支撑词：ptc heater automotive（50、KD 8%、信息+商业）、high voltage heater（40、KD 7%、信息+商业）、ptc heater manufacturer（40、KD 11%、信息）、custom high voltage ptc heater（20、KD 不可用）、high voltage ptc heater supplier（10）、high voltage ptc heater manufacturer（10）、high voltage ptc heater for ev platforms（10）。
- 通用大词不当主词：ptc heater（1600、KD 27%）、ptc heaters（480、KD 15%）、what is a ptc heater（260、KD 13%）偏向家用／风暖，只作流量锚或正文词。
- 无数据：electric bus coolant heater（美国库未找到任何数据）。

## SERP（Google 美国英文，2026-11-09 首页扫描）
- high voltage ptc heater：AI 概览定义高压 PTC 加热器约 250V–900V，用于 EV／混动；首页为 Infineon 汽车 PTC 加热器模块、KLC 高压 PTC 加热器（12V–999V）、DBK USA 高压空气加热器、Grayson、Fellten 3kW 座舱加热器、ROHM 参考设计——多为空气加热器／元器件单品页。缺口：没有面向电动车冷却液应用的电压／功率／流量选型指南。
- high voltage coolant heater：AI 概览定义 HVCH、工作于 400V–800V；首页为 Cascadia Motion 400V/800V 产品页、Valeo HVCH 目录、Webasto HVH 50/70（5–7kW）、BorgWarner 新闻稿、Reddit 车主讨论及购物 listing。缺口：没有独立的选型方法文章；没有 PTC 与厚膜技术对比、按电池与座舱负荷选功率的选型表。
- 写前须补：10 维 SERP 框架逐项核对（本文只做了首页扫描＋缺口判断）。

## 角度与结构（买家问题驱动）
选型指南：先给选型结论（电压平台→功率档→控制方式→冷却回路核对），再展开。结构草拟：① 选型前先定加热任务（电池预热／座舱／两者，工况与可用时间）；② 电压与功率同点匹配（400/600/800V 平台，功率档 6–18／20–25／30–35 kW，勿只看铭牌功率）；③ 控制接口（B 系列 CAN＋enable，E 系列恒温器无 CAN；谁发加热请求、故障时整车如何响应）；④ 冷却回路安装（压降数据、泵曲线、并联支路流量）；⑤ 一张共享接口记录表（加热任务／供电／冷却回路／控制／安装／验证／采购）；⑥ 样件验收与量产配置确认；⑦ 询盘清单＋FAQ。

## 事实（只用已核实项，不编数）
- HVCH B 系列＝CAN＋enable；E 系列＝恒温器、无 CAN。
- 功率档：6–18 kW、20–25 kW、30–35 kW；电压平台 400V、600V、800V 及定制；产品页口径：15–35 kW／台、平台最高 DC 870V、2021 年起量产。
- Q 系列实验室验证（上海工程技术大学）：振动、水循环、带电性能评估。
- 询盘导向：价格按项目报价，站上无标价、无在线下单。
- 禁写：认证宣称（无认证数据）、原厂背书（车型适配词只作长尾，不暗示原厂适配）。

## 内链（只链已核实实页）
- 产品页 https://evbtms.com/products/high-voltage-coolant-heater/
- 制造商页 https://evbtms.com/high-voltage-coolant-heater-manufacturers/
- PTC 选型文（11-04）https://evbtms.com/ptc-coolant-heater-btms-selection/
- BTMS 产品页 https://evbtms.com/products/battery-thermal-management-system/

## PTC 商业承接页选题（11-10 带给 Peter 定）
- (a) HVCH 选型／报价页（新页：选型表＋询盘表单，按项目报价）；(b) 制造商页已存在（market 词 7 天 7.0 名、承接页 3.0 名）——强化 CTA 并从新指南链过去；(c) 价格因素页（不标价，只讲定价因素：功率／电压／接口／数量）。建议 (a)+(b)。

## 执行与防撞
- 流程：Brief→英文正文→阶段 7 终审→DeepL 英→西→英-GB→ZeroGPT 两半 ≤30%→达标直发（11-06 规则）；发布时显式设 slug，发后实链核验。
- 撞题检查：明早派工时与 Codex 当日档（DAILY-1110）选题核对，撞题换题。
