# HVCH 系列参数摸底（老站只读，2026-11-09）

执行：browser-task 08d1abf4，2026-11-09 15:46–15:49。只读调研，未登录后台、未编辑任何内容、未触碰 evbtms.com 或 WordPress。核查日期：2026-11-09。

## A 系列（已找到）
来源：https://www.evptc.com/sale-36421007-a-series-6-18kw-400-800v-high-voltage-ptc-coolant-heater-for-ev-battery-and-vehicle-thermal-manageme.html
- 功率：6–18kW（规格表 Power Output 栏；同一页正文另写“delivering 10–18 kW”，两处不一致，制表以规格表为准并标注）
- 电压平台：400–800V（Rated Voltage 栏注明 Customizable；低压供电 12V/24V）
- 控制接口：CAN + enable signal（规格表 Communication Method 栏）
- 温控方式：页面未明确说明（未写恒温器、PID 或出水温度设定值；仅写 CAN 让整车控制器协调加热）
- 适用车型/用途：trucks、buses、construction machinery；用途 Battery Heating、Cabin Heating、RBS
- 其他：IP67，工作温度 -40°C 至 85°C，重量 5.1KG

## Q 系列（已找到）
来源：https://www.evptc.com/sale-40660606-q-series-high-voltage-ptc-coolant-heater-400-1100v-15-35kw-for-ev-battery-and-thermal-management.html
- 功率：15–35kW（另有 25kW / 30kW / 35kW 档位表述）
- 电压平台：400–1100V（600V / 800V / 1100V 档位；Rated Voltage 栏注明 Customizable；低压供电 12V/24V）
- 控制接口：CAN + enable signal（规格表 Communication Method 栏）
- 温控方式：页面未明确说明（仅写 CAN 让整车控制器协调、用于电池温度控制，未写恒温器、PID 或温度设定值）
- 适用车型/用途：electric buses、trucks、construction vehicles；用途 Battery Heating、Cabin Heating、RBS
- 其他：IP67，工作温度 -40°C 至 85°C，重量 12KG

## E 系列（已找到，交叉核对一致：恒温器、无 CAN）
来源：https://www.evptc.com/sale-40751921-e-series-high-voltage-ptc-coolant-heater-20-24kw-400-800v-for-electric-buses-trucks-and-battery-ther.html
- 功率：20–24kW（20kW / 22kW / 24kW 档位）
- 电压平台：400–800V（Rated Voltage 栏注明 Customizable；低压供电 12V/24V）
- 控制接口：无 CAN（规格表 Communication Method 栏写 NO）
- 温控方式：Thermostat（页面将其列在 High-Voltage Protection 栏；未说明恒温器设定温度或控温逻辑）
- 适用车型/用途：electric buses、trucks、small commercial vehicles、construction vehicles；安装空间有限的小型商用车；用途 Battery Heating、Cabin Heating、RBS
- 其他：IP67，工作温度 -40°C 至 85°C，重量 8.5KG
- 注意：该页 FAQ / Applications 段落中出现“15–35kW”表述，与本页 20–24kW 规格不一致，疑似套用模板文字，制表以规格表 20–24kW 为准，不采用该段数字。

## H 系列（未找到产品页）
- 老站站内搜索“H Series”及“H Series High Voltage PTC Coolant Heater”（共 95 个结果）逐页核查全部 6 页结果标题，未出现任何以 H Series 命名的产品页；产品总页（https://www.evptc.com/products.html）上出现的系列标题只有 A、E、K、Q、W、Z，也无 H 系列。
- 结论：H 系列的功率、电压、控制接口、温控方式、适用车型均无法从老站页面提取，不做推测。明日执行前须向产品方确认 H 系列是否属新站新增系列或另有型号名称，否则新站系列表只上 A、Q、E 三系。

## B 系列（未找到产品页，交叉核对）
- 站内搜索“B Series”（共 103 个结果）第 1 页及第 7 页（最后一页）均未出现以 B Series 命名的产品页，产品总页上亦无 B 系列标题。已确认的 CAN + enable 组合实际出现在 A 系列与 Q 系列页面上。
- 结论：仅说明老站无 B 系列产品页，不否定 B 系列存在（PTC-1110 稿中“B 系列＝CAN＋enable”来自产品事实库，非老站页面；E 系列恒温器、无 CAN 已与老站页交叉核对一致）。

## 明日执行前待确认（进 11-10 08:00 计划）
1. H 系列参数无来源：确认 H 系列是否存在／型号名／参数，或系列表只上 A、Q、E 三系。
2. Q 系列电压 400–1100V 与新站 HVCH 产品页口径“平台最高 DC 870V”冲突：制表用哪边，须定。
3. A 系列功率正文 10–18kW 与规格表 6–18kW 不一致：制表以规格表 6–18kW 为准。
4. A、Q 两系温控方式老站页未写：系列表温控一栏写“整车控制器协调（CAN）”或留空待确认，不编恒温器/PID。
