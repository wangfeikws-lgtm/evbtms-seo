# evbtms 午派工（下午场）— 2026-10-21

> 依据：仓库权威 TASKS.md（GitHub API `get_file_contents` @ main，与待推送区本地版本逐字节一致，SHA 2bdd10bde30ce19224e03d0b5be25484c8b892b7）＋ 今日 commits（per_page=20）＋ DAILY_PLAN 2026-10-21（commit 7e750fe8，08:17 入仓，即上午派工口径）。
> 口径变更（commit 0209123c，10:15）：Peter 2026-10-21 决定——**发布权收回，Muse/Codex 只写不发**，所有文章交 Peter 审核后亲自发布。原 DAILY_PLAN 中的"写＋发"一律改为"只写稿、入仓、呈 Peter"。

## 一、上午完成情况（对 DAILY_PLAN 2026-10-21）

| 任务 | 中文说明 | 负责人 | 状态（12:22 核验） |
|---|---|---|---|
| T13《evbtms.com 8 个老页面升级闪电战 7 页执行》 | BTMS 分类页 / 矿卡专区 / HVCH 产品页 / 三合一产品页 / HVCH 厂家页 / BTMS 测试内容 / Applications 页，Codex 按 Muse 文案包施工 | Codex | 🟡 DOING — 仓库无今日提交、无 SYNC_LOG 更新，18:00 死线未到，需下午点名要中期进度 |
| T8-6《制动电阻英文文章第 6 篇》 | 制动电阻 30 篇第 6 篇（原理支柱） | Muse | ✅ 已交付 — `REPORTS/T8-article-06-sizing-mistakes.md`＋`T8-06-serp-brief-2026-10-21.md` 入仓（commit 92ffc3f0，11:10；前次推送遇服务重启未落地，本次补推成功）。按新规只写不发，成稿即完成；但管线总表 `REPORTS/article-pipeline-and-inventory.md` 仍写"未写完"，需回填 |
| DAILY-BTMS-1021（每日 BTMS 档） | BTMS 9:00 档 | — | ✅ 已交付 — `REPORTS/BTMS-refrigerant-circuit-rewrite-2026-10-21.md`（commit 381596fa，11:08；Peter 2026-10-21 要求的人味重写版，替换 WP10113）。只写稿，待 Peter 审后亲自发布 |
| DAILY-HVCH-1021（每日 HVCH 档） | HVCH 14:00 档 | Codex | ⏳ 待办 — 14:00 未到，按新规只交成稿 |
| T12-W2《老站英文第二周 5 篇大纲》 | evptc.com 老站 5 篇英文大纲＋SERP 依据，12:00 前呈 Peter 批 | Muse | 🔴 超期零交付 — 12:22 仓库无 T12-W2 文件、无相关提交，截止已过 22 分钟，升级点名 |
| MINING-EC-COMP-REMOVE《矿卡页撤 Electric Compressor》 | https://evbtms.com/electric-mining-truck/ 第 4 位产品位撤下 Electric Compressor（Peter 10-20 17:30 已批） | Codex | ⏳ 待办 — 今日内完成，无提交 |
| LINKEDIN-POST《LinkedIn #5/#6/#7 代发》 | 候补：LinkedIn 三篇已呈批稿代发（Peter 10-20 17:34 批改回 Codex） | Codex | ⏳ 待办 — 无证据 |
| MOBILE-QA-1021《390px 移动端验收补做》 | 候补：矿卡页＋HVCH 14:00 档（ID 10116）真 390px 视口截图 | — | ⏸ 阻塞 — 待浏览器会话恢复 |

分工口径冲突待澄清：T12 写作归属，TASKS.md（Peter 2026-10-16 决定）写"老站英文正文改由 Codex 撰写，Muse 只做验收"；DAILY_PLAN 2026-10-21 写"T12-W2 大纲负责人：Muse"。下午 T12-W2 仍按 DAILY_PLAN 派给 Muse 抢回，但需 Peter 明示后续归属。

## 二、Codex 下午任务（只写不发口径）

1. **T13《evbtms.com 8 个老页面升级闪电战 7 页执行》** — 死线今日 18:00。要求：16:00 前提交中期进度（已完成页数＋每页改前基线快照已存档确认）；18:00 交付全部 7 页执行＋入仓报告。红线：英文一字不改（以 `REPORTS/page-upgrade-copy-pack-2026-10-20.md` 为准），不得改 URL/301/canonical/插件主题。
2. **MINING-EC-COMP-REMOVE《矿卡页撤 Electric Compressor》** — 今日内完成，建议 16:00 前。交付：改前基线（截图＋字段值）＋改后公开面验证报告入仓；其余产品位与内链不受影响，不改 URL。
3. **DAILY-HVCH-1021《每日 HVCH 14:00 档成稿》** — 14:00 前交成稿入仓（REPORTS/＋SERP 简报），不做 WP 发布。防重复检查先行。
4. **LINKEDIN-POST《LinkedIn #5/#6/#7 代发》** — 候补，今日内。Codex 用自有路径发布（Muse 浏览器登录被拒已停试），发后回填 URL。

## 三、Muse 下午任务（只写不发口径）

1. **T12-W2《老站英文第二周 5 篇大纲》** — 🔴 点名：原定今日 12:00 呈批，现零交付超期。下午 16:00 前必须交付 5 篇大纲＋SERP 依据入仓、呈 Peter 批。大纲未经 Peter 批准不得写全文（红线）。
2. **T13 验收** — Codex 18:00 交付后，逐页对照文案包逐字核对（Title/Meta/H1/新增段落/FAQ/内链），改前基线已存档确认；验收报告入仓。验收中发现掉量风险直接标注回滚。
3. **T8-6 管线回填** — `REPORTS/article-pipeline-and-inventory.md` 中 T8-6~30 行回填 T8-6 已交付（成稿入仓 2026-10-21，按新规不发布）。
4. **T8-7《制动电阻英文文章第 7 篇》大纲准备** — 下午备大纲，明日 08:30 前呈 Peter 批（每日节奏不断）。

## 四、需 Peter 事项（一句话一条）

1. T12-W2 5 篇大纲原定今日 12:00 呈批、延误到 16:00，请批后安排全文写作（另请明示：T12 后续写作归 Codex 还是 Muse）。
2. BTMS 9:00 档重写稿 `REPORTS/BTMS-refrigerant-circuit-rewrite-2026-10-21.md` 已入仓，请审阅后由您亲自发布替换 WP10113。
3. T8-6《制动电阻英文文章第 6 篇》成稿＋SERP 简报已入仓，请审阅后由您亲自发布。
4. T13 7 页 Codex 18:00 交付、Muse 当晚验收，请您终审。
5. Windsor 请断开 2 个连接，或 GSC 手动导出 BTMS 分类页基线数据（T13 掉量回滚用）。
6. T7 H3 真实型号映射／面包屑方案请批准（A3→Q-3 301 待批）。
7. 矿卡三模块文案初稿已备，请审稿。
8. HVCH 14:00 档今日只交成稿不发布，请知悉。

## 五、超期点名

- **T12-W2《老站英文第二周 5 篇大纲》**：上午派工 12:00 呈批，12:22 零交付，已超期 22 分钟。下午 16:00 为硬死线，仍无交付则升级为当日阻塞事项。
