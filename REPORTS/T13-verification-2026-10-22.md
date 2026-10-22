# T13《8 个老页面升级闪电战》前台核验报告（2026-10-22）

核验人：Muse。方法：2026-10-22 当天 curl 抓取 evbtms.com 5 个目标页面的真实 HTML，与 `REPORTS/page-upgrade-copy-pack-2026-10-20.md` 逐项对照（Title / Meta / H1 / 新增段落首句 / FAQ 问题原文 / 指定锚文本）。第 8 项（10-28 数据复盘）不在本次范围。

## 逐页结论

| 页 | 结论 | 说明 |
|---|---|---|
| #1 BTMS 分类页 | **部分执行** | Title/Meta/H1/首屏句已是已批版，但那是 10-19 已上线的值，非 T13 本次动作；本次新增内容基本没落地（见下） |
| #2+#7 /applications/ | **未执行** | Title/Meta/H1 全为改前旧值，矿卡扩写、FAQ、板块重组、卡片替换均无 |
| #3 HVCH 产品页 | **未执行** | Title/Meta 旧值，选型段落与 3 条 FAQ 均无 |
| #4 三合一产品页 | **未执行** | Title/Meta 旧值，对比段落、3 条 FAQ、FAQ Schema 均无 |
| #5 HVCH 厂家页 | **未执行** | Title/Meta 旧值，工厂段落与 3 条 FAQ 均无 |
| #6 BTMS 测试板块（与 #1 同页） | **未执行** | 测试板块标题、正文、3 条测试 FAQ 均无 |

**总计：7 页中 0 页完整执行，1 页部分执行（且完成部分是 T13 之前已上线的），6 页未执行。** 与"Codex 10-21 18:00 死线已过、仓库无执行报告"互相印证：T13 实际上没有被执行。

## 逐项证据

### #1 BTMS 分类页 https://evbtms.com/products/battery-thermal-management-system/
- ✅ Title（页面实际）：`Battery Thermal Management System (3–12kW) | EVLINK Manufacturer`（与已批版一致，10-19 已上线）
- ✅ Meta（页面实际）：`EVLINK manufactures 3kW, 5kW and 12kW battery thermal management systems with liquid cooling, PTC heating and CAN 2.0 control for electric buses and trucks.`（一致）
- ✅ H1（页面实际）：`Battery Thermal Management Systems for Electric Buses & Trucks`（一致）
- ❌ 新增选型段落：H2 `Which Size Do You Actually Need?` 不存在；首句 `Most buyers who call us start with the wrong question` 全页无。页面 H2 仍为原有序列（BTMS Product Range → How It Works → How to Select…）。
- ⚠️ FAQ 3 条：三个主题在页面上，但**问答文字不是文案包原文**——Q1 问法与包一致（`What high-voltage platforms do EVLINK BTMS units support?`），但答案是页面自有版本（"The 3kW model supports DC 400–750V. The 5kW and 12kW models support DC 400–860V…"），与包定稿（"Our BTMS range runs on DC 400–860V platforms…"）不同；Q2 页面问法是 `What protection rating do the BTMS models use?`（包定稿：`What protection rating do the BTMS units carry?`）；Q3 页面问法是 `What PTC heating capacity is available?`（包定稿：`How much PTC heating capacity is available?`）。即 FAQ 未按包替换。
- ⚠️ 内链：指向三合一产品页、HVCH 产品页的链接存在（各 2 处 href），但文案包指定的锚文本原文（`three-in-one thermal management controller`）在页面可见文本中未出现。

### #6 BTMS 测试板块（同页）
- ❌ 板块 H2 `How Every EVLINK BTMS Is Tested Before It Ships` 不存在；正文首句 `Buyers ask about cooling capacity first and testing second` 无；3 条测试 FAQ（`What tests does an EVLINK BTMS pass before delivery?` 等）全部无。

### #2+#7 /applications/ https://evbtms.com/applications/
- ❌ Title（页面实际）：`EV Thermal Management Applications | EVLINK`（包定稿：`Electric Mining Truck Thermal Applications | EVLINK`，未改）
- ❌ Meta（页面实际）：`Explore EVLINK EV thermal management applications for electric buses, trucks, construction machinery, mining vehicles and data center liquid cooling`（旧值，未改）
- ❌ H1（页面实际）：`Thermal Management Solutions for Electric Vehicles & Data Centers`（包定稿：`Thermal Management Applications for Electric Buses, Trucks & Mining Vehicles`，未改）
- ❌ 板块顺序：实际为 Electric Bus → Electric Truck → Electric Mining Truck → Construction Machinery → **Data Center Liquid Cooling → Agricultural Machinery**（包要求 Data Center 移到最后、Agricultural 在其之前，未调整）
- ❌ 矿卡扩写：H3 `The Descent Is the Hard Part` 不存在；正文首句 `A mine is two climates in one shift` 无
- ❌ 矿卡 FAQ 3 条：全部无（`How does an electric mining truck handle braking energy on long descents?` 等）
- ❌ **Electric Compressor 卡片替换（已批变更 MINING-EC-COMP-REMOVE）：未执行。** 产品区实际仍是 `04 | Electric Compressor`（描述 "Active refrigerant compression for vehicle or equipment cooling circuits"）；`Braking Resistor` 字样只出现在全站顶部导航菜单中，不是产品卡，包定稿的卡片描述（`Liquid-cooled braking resistors that absorb the energy regenerative braking cannot take…`）页面无。

### #3 HVCH 产品页 https://evbtms.com/products/high-voltage-coolant-heater/
- ❌ Title（页面实际）：`High Voltage Coolant Heater for Electric Vehicles | EVLINK`（包定稿：`High Voltage Coolant Heater Manufacturer | EVLINK`，未改）
- ❌ Meta（页面实际）：`EVLINK high voltage coolant heaters support battery, cabin and powertrain thermal management with flexible power and voltage options.`（旧值，未改）
- ✅ H1：`High Voltage Coolant Heater for Electric Vehicles`（包要求不动，一致）
- ❌ 新增段落：H2 `How to Size a Coolant Heater Without Guessing` 不存在；首句 `Heater sizing is where projects quietly go wrong` 无
- ❌ 新增 FAQ 3 条：全部无（`What heater power range does EVLINK manufacture?` 等）

### #4 三合一产品页 https://evbtms.com/products/three-in-one-controller/
- ❌ Title（页面实际）：`Three-in-One Thermal Management Controller for Electric Bus | EVLINK`（包定稿：`Three-in-One Thermal Management Controller | EVLINK`，未改）
- ❌ Meta（页面实际）：`Explore EVLINK three-in-one controller solutions integrating thermal management control functions for electric and commercial vehicle applications.`（旧值，未改）
- ✅ H1：`Three-in-One EV Thermal Management Controller`（包要求不动，一致）
- ❌ 新增对比段落：H2 `Three Separate Controllers vs. One Integrated Unit` 不存在；首句 `The traditional layout puts three boxes on the vehicle` 无
- ❌ 新增 FAQ 3 条：全部无（`What does the three-in-one controller integrate?` 等）；页面源码中无 FAQPage schema 输出

### #5 HVCH 厂家页 https://evbtms.com/high-voltage-coolant-heater-manufacturers/
- ❌ Title（页面实际）：`8 High-Voltage Coolant Heater Manufacturers | EVLINK`（包定稿：`High-Voltage Coolant Heater Manufacturers | EVLINK Factory`，未改）
- ❌ Meta（页面实际）：`Compare eight high-voltage coolant heater manufacturers for EV thermal management, including supplier capabilities and key selection factors.`（旧值，未改）
- ✅ H1：`8 High-Voltage PTC Coolant Heater Manufacturers and HVCH Suppliers Worth Shortlisting in 2026`（包要求不动，一致）
- ❌ 新增工厂段落：H2 `Inside the EVLINK Heater Line` 不存在；首句 `A comparison list tells you who sells heaters` 无
- ❌ 新增 FAQ 3 条：全部无（`Is EVLINK a manufacturer or a trading company?` 等）

## 未执行项清单（给 Codex 的返工单，即文案包全部待办）

1. #1 BTMS 页：补选型段落（H2 `Which Size Do You Actually Need?`＋定稿正文）；FAQ 3 条按包原文替换（问法＋答案）；内链锚文本按包落实。
2. #6 BTMS 页（同页）：补测试板块（H2 `How Every EVLINK BTMS Is Tested Before It Ships`＋定稿正文）＋3 条测试 FAQ。
3. #2/#7 Applications 页：Title/Meta/H1 改包定稿唯一版；板块顺序调整（Data Center 移最后）；矿卡扩写段（H3 `The Descent Is the Hard Part`）；3 条矿卡 FAQ；**04 号产品卡由 Electric Compressor 换成 Braking Resistor（包定稿标题＋描述＋链接）**；5 条内链。
4. #3 HVCH 产品页：Title/Meta 改包定稿；补选型段落；补 3 条 FAQ；内链。
5. #4 三合一页：Title/Meta 改包定稿；补 vs 分立方案段落；补 3 条 FAQ 并核验 FAQPage schema 输出；内链。
6. #5 HVCH 厂家页：Title/Meta 改包定稿；补工厂段落；补 3 条 FAQ；内链。
7. 每页改前留改前字段值＋截图存档（文案包红线）；10-28 数据复盘与回滚线（任一页 CTR 掉 0.5% 以上回滚该页）不变。
