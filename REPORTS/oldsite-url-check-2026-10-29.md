# 老站 evptc.com URL 核验报告（2026-10-29）

- 核验方法铁律：只看页面真实标题与正文内容，不看 HTTP 状态码（ECER 缺失页也回 200，状态码不作数）。以下每条均以前台文本抓取实测为准。
- 核验范围：15 条 URL。来源：管线表 W1 正式 URL 5 条＋W2 文章 URL 5 条（仓库发布包中无 W2 文章 URL，本次经前台新闻页导航实测取得）＋产品总览页 1 条＋Q 系列产品页 1 条＋前 T12 对照文章 1 条＋新闻页 1 条＋W1-3 变体 slug 1 条（计入第 15 条）。
- **异常数：0 条。** 15 条全部在位、标题与内容一致。另有 4 项须注记的发现（非异常，见文末）。

## 逐条核验表

| # | URL | 真实标题 | 内容证据 | 结论 |
|---|---|---|---|---|
| 1 | https://www.evptc.com/news/how-to-choose-a-high-voltage-ptc-coolant-heater-7-inputs-oems-must-define-422912.html | How to Choose a High-Voltage PTC Coolant Heater | 七项输入正文完整；Published 2026-10-20 09:52:44 | 正常（W1-1） |
| 2 | https://www.evptc.com/news/can-controlled-vs-thermostat-controlled-hvch-which-architecture-fits-your-vehicle-422917.html | CAN vs Thermostat-Controlled HVCH | 决策矩阵与 E 系列（20–24 kW／400–800 V／8.5 kg／370×192×98 mm）、N 系列（2 kW／200–1000 V）内容完整；Published 2026-10-20 09:57:20 | 正常（W1-2） |
| 3 | https://www.evptc.com/news/electric-bus-battery-preheating-at-30c-five-planning-mistakes-422919.html | Electric Bus Battery Preheating at −30°C | 五项失误＋冷天验证清单完整；Published 2026-10-20 10:00:48 | 正常（W1-3，管线表正式 slug，at-30c 拼写） |
| 4 | https://www.evptc.com/news/ptc-coolant-heater-vs-heat-pump-for-commercial-evs-where-each-system-wins-422921.html | PTC Coolant Heater vs Heat Pump for Commercial EVs | 三种商用车决策＋架构评审输入完整；Published 2026-10-20 10:02:21 | 正常（W1-4） |
| 5 | https://www.evptc.com/news/why-electric-bus-range-falls-in-winter-and-five-levers-fleets-can-control-422923.html | Why Electric Bus Range Falls in Winter | 五项杠杆＋RFQ 数据完整；Published 2026-10-20 10:03:47 | 正常（W1-5） |
| 6 | https://www.evptc.com/news/15-kw-vs-35-kw-sizing-your-hvch-for-heavy-duty-trucks-425081.html | 15 kW vs 35 kW: Sizing Your HVCH for Heavy-Duty Trucks | 功率选型全文（电池质量×温升×出发时间窗＋电流校核）完整；Published 2026-10-23 09:24:33 | 正常（W2-01） |
| 7 | https://www.evptc.com/news/ip67-and-emc-in-high-voltage-heaters-what-to-check-before-installation-425083.html | IP67 and EMC in High-Voltage Heaters: What to Check Before Installation | 防护与电磁兼容全文完整；Published 2026-10-23 09:32:19 | 正常（W2-02） |
| 8 | https://www.evptc.com/news/hydrogen-fuel-cell-bus-heating-20-kw-class-coolant-heater-selection-425088.html | Hydrogen Fuel Cell Bus Heating: 20 kW-Class Coolant Heater Selection | 燃料电池客车 20 kW 配置全文完整；Published 2026-10-23 09:36:22 | 正常（W2-03，前台实标题与发布包标题措辞不同，见注记 2） |
| 9 | https://www.evptc.com/news/air-heater-vs-coolant-heater-for-ev-cabins-a-total-cost-comparison-425090.html | Air Heater vs Coolant Heater for EV Cabins: A Total Cost Comparison | 风暖与水暖总成本全文完整；Published 2026-10-23 09:40:09 | 正常（W2-04） |
| 10 | https://www.evptc.com/news/battery-swapping-heavy-trucks-need-thermal-management-too-427130.html | Battery-Swapping Heavy Trucks Need Thermal Management Too | 换电重卡热管理全文完整；Published 2026-10-26 17:31:07 | 正常（W2-05） |
| 11 | https://www.evptc.com/products.html | Products | 11 个加热器分类＋供应商子页链接＋联系方式（Contact Us, Mr. Xu, 13004587611@evptc.com, +86 13004587611，WhatsApp 链接）完整 | 正常（联系方式为站点自身公开内容，见注记 4） |
| 12 | https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html | High Voltage PTC Water Heater 15-35kW 400-1100V for Electric Vehicles, EV Battery Thermal Management Systems and Heating IP67 | Q-Series、MOQ 1 SET、$1500 per set、T/T、100 sets per 2 weeks、产地 CHINA、额定电压 Customizable、400V–1100V、15–35kW、-40ºC~85ºC、IP67、Battery / Cabin Heating / RBS、InStock 完整 | 正常（页面自带 E-Mark/CE 标注为 ECER 商品页原有内容，T12-1 不引用，见注记 4） |
| 13 | https://www.evptc.com/news/how-does-a-high-voltage-coolant-heater-work-262644.html | How Does a High Voltage Coolant Heater Work? | 通用原理长文完整；Published 2025-11-23、Updated 2026-10-15 | 正常（前 T12 对照文章） |
| 14 | https://www.evptc.com/news.html | News | 首屏列出 12 条：W2 五篇标题（dated 10-23/10-26）＋W1-5（10-20）＋非 T12 文章 6 条（行业例文 10-27、PTC"心脏"深度分析 10-23、电动卡车增长 10-21、CATL 换电战略 07-03、JiuXing DC870V BTMS 合作 2022、冬奥氢燃料客车 2023），标题与摘要真实 | 正常（新闻索引页） |
| 15 | https://www.evptc.com/news/electric-bus-battery-preheating-at-30-c-five-planning-mistakes-422919.html | Electric Bus Battery Preheating at −30°C | 返回与第 3 条同一篇 -30°C 文章全文（同标题、同发布日期）；变体 slug 可解析为同一文章 | 正常（双 slug 并存，见注记 3，不算异常） |

## 注记（非异常，须主 agent 知晓）

1. **W2 管线表状态已过期，建议主 agent 更新管线表。** 仓库管线总表仍记 W2 五篇"待 Peter 审发／未发布"，但前台实测五篇全部在位，发布时间分别为 2026-10-23（4 篇）与 2026-10-26（1 篇）。本次核验以公开面实证为准，不改仓库文件（本任务只写稿、不推仓库）；管线表回填由主 agent 统一处理。另，2026-10-23 午派工所称"Peter 亲发 3 篇（待点名）"与实测 5 篇在位数量不一致，以本次实测为准。
2. **W2-03 前台实标题与发布包标题措辞不同。** 发布包标题为 "Why 20 kW PTC Became the Standard Answer"，前台实标题为 "Hydrogen Fuel Cell Bus Heating: 20 kW-Class Coolant Heater Selection"。内容为同一篇（燃料电池客车 20 kW 配置论证），不算异常；管线表回填时以前台实标题为准。
3. **W1-3 双 slug 并存。** 管线表正式 slug（at-30c）与 W2 发布包内链变体 slug（at-30-c）均解析为同一篇 -30°C 文章。双 slug 并存不算异常，但建议主 agent 后续统一内链使用正式 slug，避免分散。
4. **站点自身公开内容说明。** products.html 的联系方式（Mr. Xu、邮箱、电话、WhatsApp）与 Q 系列产品页的 E-Mark/CE 标注均为 ECER 站点原有公开内容，核验如实记录；T12-1 全文未引用该认证标注，不混用口径。

## 未覆盖项

- W3/W4 计划选题（各 5 篇）未发布，无 URL 可核验，不在本次清单内。
- 本次核验未使用 HTTP 状态码作任何一条的判断依据；全部结论来自页面真实标题与正文内容。
