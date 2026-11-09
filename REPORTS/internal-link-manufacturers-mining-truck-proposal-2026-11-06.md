# 厂商页 ↔ 矿卡页内链补强方案（报批用，2026-11-06 下午准备）

> 来源：2026-11-06 GSC 日检建议兑现（厂商页与 mining truck 词均已精确复核带内站稳，按计划进派工单：SERP 先行、方案先报批再动手）。
> 状态：**已批（Peter 2026-11-09 09:57）并已执行（2026-11-09 10:13–10:57，WP Elementor 内改完发布）**。链 A：厂商页（博客文章 ID 3727）EVLINK 条目锚文本 mining and engineering equipment → 矿卡页，前台独立核验到锚文本；链 B：矿卡页（页面 ID 2919）02 卡新增引导句，锚文本 compare high-voltage coolant heater manufacturers for mining duty → 厂商页，浏览器任务实际点击核验通过（落到厂商页，标题一致；矿卡页 Elementor 卡片正文不在前台文本抓取内，故以后台点击核验为准）。编辑中一次 TinyMCE 误写已用 Elementor 历史恢复，未影响发布内容。效果等下个 GSC 窗口判。
> 执行口径：只加 2 条内链（双向各 1 条），不动标题、Meta、slug、正文其他内容，不提交 sitemap、不点索引。

## 1. GSC 依据（2026-11-06 日检，数据截至 11-03，精确筛选值）

- 厂商页 `/high-voltage-coolant-heater-manufacturers/`：28 天 1 点击 / 111 曝光 / 17.4 名；7 天 14.6 名，带内站稳。
- 查询词 `mining truck thermal management`：28 天 0 点击 / 23 曝光 / 11.7 名，带内站稳；承接页以 `/electric-mining-truck/` 为主，该页对该词 8.0 名（已进首页）。
- 查询词 `automotive high voltage coolant heaters market`：7 天 7.0 名，承接页厂商页 3.0 名，守住即可。
- 矿卡页 `/electric-mining-truck/` 整页 28 天 21.1 名（带外边缘），7 天未进前 10——补强的目标是把整页从 21.1 推回 8–20 位带内，不是只保住单个词的 8.0 名。

## 2. SERP 意图（2026-11-06 实查）

- `mining truck thermal management`：前排是整车/系统级页面——Dongfeng 非洲矿用电动卡车（高温、粉尘、高海拔）、TZ5Y 卡塔尔石灰石矿卡（50℃ 环境液冷）、矿用电动自卸系统设计指南、L&M MESABI 矿用热管理系统。意图是系统级工程（持续大负荷、再生制动、粉尘、振动、高海拔、快充），不是单一零件。EVLINK 矿卡页现有结构（整车热循环、粉尘/振动/海拔、制动电阻）与该意图对得上，缺的是从高权重厂商页导过来的站内 topical 关联。
- `high voltage coolant heater manufacturers`：前排是市场报告（WiseGuy：2024 年 9.359 亿美元 → 2035 年 25 亿美元）、竞品厂家页（Nanfeng 等）、EVLINK 的 ECER 公司页。意图是供应商比选。厂商页现有结构（8 家按产品层分档＋RFQ 核对清单）与该意图对得上，缺的是把“EVLINK 最适合”落到一个真实应用场景（矿卡）上。

## 3. 方案：只加 2 条链

### 链 A：厂商页 → 矿卡页（已核验可落位，原文逐字抄自前台）

- 位置：厂商页 EVLINK 条目第 1 节，原文（前台 2026-11-06 实测）：
  > "The strongest fit is a project with a defined HV bus and coolant circuit, especially battery preheating, commercial-vehicle winter operation, cabin heating through a heat exchanger, or mining and engineering equipment."
- 改法：仅把锚文本 `mining and engineering equipment` 链到 `https://evbtms.com/electric-mining-truck/`，句子一字不动。
- 理由：该句已写明矿卡是 EVLINK 最适合的场景，链过去是顺着原文走，不加新说法、不编新数字。

### 链 B：矿卡页 → 厂商页（方向已定，精确锚点待 WP 编辑器内确认）

- 位置：矿卡页“EVLINK Products for Mining Truck Thermal Management”第 02 卡“High Voltage Coolant Heater”（前台文案：“Controlled coolant heating for battery preconditioning in cold mines.”）。
- 改法：在该卡补一句引导语，锚文本 `compare high-voltage coolant heater manufacturers for mining duty` 链到 `https://evbtms.com/high-voltage-coolant-heater-manufacturers/`；或在同卡产品名上加链。二选一，执行时在 WP 编辑器里看该卡现有链接情况再定（若产品名已链向 HVCH 产品页，则另起一句引导语，不抢占现有链）。
- 理由：矿卡买家下一步就是比选加热器供应商，厂商页正是比选页；回链形成双向 topical 闭环。
- 注意：矿卡页前台文本抓取有多节只有标题无正文（Elementor 区块），精确落位须进 WP 编辑器确认，不得凭猜测写锚点位置。

## 4. 不做的事

- 不改两页标题、Meta、slug、正文其他内容；不新增段落、不加新数字（矿卡 40 吨/325kW 等口径只在已核实处用，本方案不引用）。
- 不碰三合一页（其滑出查因是另一项，见周一派工单 P1-4）。
- 改完只做前台点击核验（两链 200＋落地页标题一致），效果等下个 GSC 窗口判，不当天报效果。

## 5. 执行（批后）

- 责任：周一 11-09 10:15–11:15 独立站优化段执行（Muse 段内，低风险字段级内链修改，按单页工作流直接改）。
- 验收：改后当天前台点两链核验，写一行回填（改了哪两处锚文本＋核验结果），不单独出长报告。
