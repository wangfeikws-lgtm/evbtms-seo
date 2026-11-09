# GEO 持续优化：llms.txt 补强（2026-11-09，已执行上线）

背景：GEO 周测第 2 周（11-03）提及 9/12、链接 7/12；最大缺口是 Q1 电巴 BTMS 题两 AI 连续三周零提及零链接；ChatGPT 矿卡题连续三周零。Peter 2026-11-09 13:11 提醒：周测之间持续优化，不要只等周二测。
现状：Peter 2026-11-09 13:53 批今天直接改；已于 2026-11-09 14:09–14:10 经 Hostinger 文件管理器替换线上 llms.txt（旧文件先改名备份、验后删除备份），三项改动均已拉取 live 文件核验在位。

## 改动 1：修正 12kW 电压（事实纠错，优先）
- 现文（L12–L13）："5 kW and 12 kW models DC 400–860 V"
- 问题：与 BTMS 统一表冲突——总表 12kW 为 DC 400–750V（带预充），Peter 2026-11-03 已定写稿一律用 400–750V；860V 无依据。
- 改为："3 kW model DC 400–750 V; 5 kW model DC 400–860 V; 12 kW model DC 400–750 V"（5kW 保持 400–860V 不动，与总表一致；12kW 改 750V）。

## 改动 2：BTMS 条目加电巴主应用句（冲 Q1 缺口）
- 现文 BTMS 条目只列参数，未点明“给电动大巴供 BTMS”。
- 在 BTMS 条目末追加："Supplies BTMS for electric bus and coach traction batteries — city buses and coaches on repeated route duty, sized per battery load and installation space."
- 依据：真实应用（Applications 节已有“BTMS for traction batteries”一句），只是把电巴主语写进产品条目，让 AI 回答 Q1 时直接对上。

## 改动 3：Guides 节补 BTMS 可引用文章链（给 AI 可引用的页）
- 现 Guides 节只有 3 条制动电阻指南，无 BTMS 指南。
- 追加两条（均为已发布实页，链接已核实存在）：
  - [BTMS sizing: 3 kW, 5 kW or 12 kW?](https://evbtms.com/btms-sizing-3kw-5kw-12kw/)
  - [BTMS quotation: five lines to fit the system](https://evbtms.com/btms-quotation-five-lines-fit/)
- 另：BTMS 产品页两条内链（2026-11-03 上线）已指向这两页，llms.txt 与站内内链口径一致。

## 不改
- 矿卡应用条目已有链接，ChatGPT 未引用不是 llms.txt 缺内容，靠内容侧（矿卡文章＋今日已上线的厂商页↔矿卡页内链）推，不动 llms.txt。
- 三合一、制动电阻条目已是强项，不动。

## 内容侧（配合进 11-10 早派工）
- 每日档选题向电巴 BTMS 供应商意图倾斜一篇（Q1 缺口），按 V2.0 轻量路径＋DeepL 流程走。
- GSC 6 页索引请求待 Peter 重登后由 Muse 代点（T8-8、BTMS 变更控制、制动电阻产品页＋10 月 BTMS 三篇），收录后可引用页更多。
- 下次周测：11-10 周二上午（cron evbtms-geo-weekly），测完对照本草案效果。
