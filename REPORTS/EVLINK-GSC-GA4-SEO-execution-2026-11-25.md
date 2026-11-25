# EVLINK 新站 SEO 执行清单 · 2026-11-25

## 数据基线

GSC Web 正式数据和 GA4 落地页按相同日期比较。7 天为 11 月 16–22 日，28 天为 10 月 26 日–11 月 22 日。GSC 分页汇总和 GA4 落地会话是不同口径。GA4 未返回的落地页用空值记录。小样本只作为排查线索。

| 页面 | 28 天 GSC 点击 / 展示 / 平均排名 | 同期 GA4 落地会话 / 参与会话 |
| --- | --- | --- |
| HVCH 供应商对比 | 0 / 115 / 17.3 | 未返回 |
| 高压 PTC 选型指南 | 1 / 91 / 8.0 | 2 / 1 |
| HVCH 产品总页 | 1 / 60 / 25.4 | 2 / 1 |
| BTMS 产品总页 | 0 / 59 / 63.2 | 1 / 0 |
| BTMS 5kW 子页 | 2 / 23 / 8.7 | 未返回 |
| 电动客车应用 | 1 / 51 / 40.6 | 未返回 |
| 矿卡应用 | 0 / 25 / 24.2 | 1 / 1 |
| 三合一控制器产品页 | 0 / 13 / 20.8 | 3 / 0 |
| 制动电阻原理 | 2 / 235 / 38.4 | 1 / 0 |

## 执行顺序与承接边界

1. **HVCH 供应商对比。** 现有正文实际比较八家供应商，旧摘要把页面写成 EVLINK 工厂产品页。更新 Rank Math SEO 标题、描述，让搜索摘要和正文一致。展示最多的查询是 `automotive high voltage coolant heaters market`（30 次），包含市场研究意图。观察供应商及采购相关查询的点击，另看排名是否变化。单靠总 CTR 无法判断标题更新效果。
2. **HVCH 主产品页与选型文。** 产品总页承接产品采购、规格、应用和询盘。选型文承接 `high voltage ptc heater` 的选型信息需求，保留已确认版本。对比文承接 `high voltage coolant heater manufacturers` 比较意图。产品页和对比页的定位分开，避免另建同意图厂家页。
3. **三合一控制器补信息。** 先核验现页是否已给出清晰的接口资料入口，再加入下面的项目询问模块。三次 GA4 落地会话未记录参与，样本量不足以判断原因。上线时验收按钮目的地、正文、手机布局。已更新现有项目输入段和按钮。
4. **BTMS 总页与 5kW 子页。** 继续监测总页泛系统词与 5kW 规格词。总页平均排名 63.2，子页为 8.7，优先核对实际词和承接差异。先从相关文章补已核实的相关链接，按原派工保留总页及现有 5kW 页面布局。客车关键词内链调整沿用 Muse 当天任务，避免重复操作。
5. **矿卡及新页面。** 现有矿卡应用页已覆盖工况、产品组合、验证清单。旧址是否恢复或 301 需先确认，不另建同意图矿卡页。新页面候选为单独的三合一接口资料页，面向需要 CAN 与电气接口文档的项目工程师。开工条件为确认美国搜索意图确有独立需求、现有控制器页没有同主题承接、工程能提供可公开资料。缺少证据时先完善现有页。
6. **制动电阻原理文章。** 展示 235、平均排名 38.4。下一轮先按查询拆出原理词、故障词和选型词，确认产品链接和承接关系。当前样本不足以把点击偏低归因于标题。

## 三合一产品页英文补充文案（待上线）

### What to Share for a Controller Interface Review

Send your vehicle’s high- and low-voltage ranges, the loads you need the controller to coordinate, and your CAN network requirements. Include connector drawings, mounting space and the expected startup and fault responses if they are available. EVLINK can review the proposed configuration with your engineering team. Model-specific ratings and supported interfaces should be confirmed against the selected controller’s documentation.

Suggested CTA: **Request a Controller Interface Review** → existing contact page, after checking the destination.

## 复查

保存变更前数据和前台 HTML 字段。首轮用改动后完整 7 天与改动前可比 7 天核对，28 天检查趋势。按页看 GSC 展示、点击、平均排名及查询构成，结合 GA4 落地会话与参与会话。实际询盘以业务记录为准。

## 本次上线记录

已按 URL 单页刷新 LiteSpeed 缓存。普通公开原链接返回 HTTP 200，新 SEO 标题和描述均已输出，H1 和 canonical 核对一致。

三合一控制器页已上线接口评审说明和新按钮文案，原页面只保留一个 H1，按钮仍跳到本页询盘区。普通公开 URL 核验通过。见 [变更与基线](./EVLINK-controller-interface-review-2026-11-25.json)。
