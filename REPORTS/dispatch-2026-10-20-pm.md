# 午派工 2026-10-20（下午场）

> 派工依据：TASKS.md 权威版本（HEAD 372c81e7，blob 231de6af，GitHub API 取数，非 raw CDN）；今日提交 e2693bb8 / b0b63810 / 9527532d / 9c9d416a / ab8bacc6 / 372c81e7；前台实证＋今日内存日志。只基于实际状态，未编造任务。

## 一、上午派工完成情况（截至 12:22）

### ✅ 已交付
- T8-5《How Duty Cycle Determines Braking Resistor Size》（占空比决定制动电阻选型）——Muse 写＋发＋回填（WP ID 10117，09:21 发布，https://evbtms.com/duty-cycle-braking-resistor-sizing/）；Peter 已确认 GSC 手动提交完成。
- T12-W1（老站英文第一周）《How to Choose a High-Voltage PTC Coolant Heater: 7 Inputs OEMs Must Define》等 5 篇——Codex 已交 5 个发布包＋交接文档（commit 9c9d416a）；Peter 改派 Muse 在 ECER 手动上传发布（不要代码发）；5 篇已在 staging 落地（mao.ecer.com/test/evptc.com/news/…），正式 URL 待 www.evptc.com 自动同步后核验。
- BTMS 今日 09:00 档《btms-refrigerant-circuit-vs-coolant-loop》（ID 10113）——已发布，前台实证。
- REPORTS/mining-truck-research-2026-10-20.md（矿卡热管理调研简报）——入仓（commit 372c81e7）。
- T7 三项余项入派工（commit ab8bacc6）；GSC 索引请求记录（commit 9527532d，Codex）。

### ⏳ 进行中
- T12-W1（老站英文第一周）5 篇 ECER 发布——staging 已发，等待 www.evptc.com 同步；同步完成后 Muse 公开验收＋回填管线总表。
- HVCH 今日 14:00 档——未到档，Codex 下午执行。

### ❌ 未交付 → 超期点名（昨日 18:00 截止，今日仍零交付）
- FOOTER-EVPTC-LINK（页脚加老站品牌链 "Our legacy site: evptc.com"）——Peter 10-19 已批准（commit 24b956df），前台无执行证据。超期第 2 天，点名 Codex。
- LINKEDIN-POST（LinkedIn 代发布 #5/#6/#7）——Peter 10-19 14:54 改派 Codex（commit 5fdbcf27），无交付证据，CAPTCHA 风险仍在。点名 Codex。
- BTMS-CAT-OPT（BTMS 分类页优化）——前台实证已执行（新 Title/Meta/FAQ 生效），但 Codex 未提交交付报告＋改前基线快照。点名 Codex 补交。
- DAILY_PLAN-T10/T11 回滚（T10《集成控制器降本》/T11《热管理控制策略》DAILY_PLAN 误写回"立即发布"）——今晨 e2693bb8 把已纠偏结论写回 DAILY_PLAN.md L59-67"紧急加派/P0｜T10/T11 立即发布（Codex 现在发布）"，与"10-10 已发布、禁止重复发布"结论矛盾，重复发布风险。最高优先级，点名 Codex 立即修正。

## 二、Codex 下午任务（具体到编号＋交付物＋时间点）

1. DAILY_PLAN-T10/T11 回滚修复（最高优先级，立即执行）：修正 DAILY_PLAN.md L59-67 为"✅ T10《集成控制器降本》/T11《热管理控制策略》已于 2026-10-10 发布并验收（REPORTS/T10-T11-published-2026-10-10.md），禁止重复发布"；删除"紧急加派/P0 立即发布"整节。交付物：修正 commit。
2. HVCH-14:00（今日 14:00 档）——按九阶段验收规则发布＋回填管线总表 REPORTS/article-pipeline-and-inventory.md。交付物：正式 URL＋验收报告。
3. FOOTER-EVPTC-LINK（页脚加老站品牌链）——按 commit 24b956df 方案（页脚一行 "Our legacy site: evptc.com"，Muse 已批准互链口径：只做页脚一行，不做文章内互链/关键词锚文本）。今日 18:00 前前台落地＋交付报告入仓。
4. BTMS-CAT-OPT（BTMS 分类页优化）交付报告＋改前基线快照补交——前台已生效（Title `Battery Thermal Management System (3–12kW) | EVLINK Manufacturer`、H1、FAQ 三条），补交改前基线＋交付报告入仓。今日 18:00 前。
5. T7-STRUCT（T7 三项余项：H3 唯一化／面包屑 BreadcrumbList Schema／Q-3·A3 合并）——Peter 今晨已批准（commit ab8bacc6）。今日交付；其中 A3 301→Q-3 属高风险变更，先出修改方案经 Muse 验收后再执行。交付物：执行报告或方案报告入仓。
6. LINKEDIN-POST（LinkedIn 代发布 #5/#6/#7＋#11 LinkedIn 版《IP67+CAN 出海硬指标》）——CAPTCHA 登录风险在 Codex 栏；禁止反复硬试（锁号风险）。今日给出可行路径或明确阻塞报告。
7. BTMS-10-21-09:00（明日 09:00 档预备）——选题＋大纲，今日 18:00 前入仓备发。

## 三、Muse 下午任务

1. T12-W1（老站英文第一周）5 篇验收＋回填——待 staging→www.evptc.com 同步完成后，逐篇公开验收（HTTP 200、canonical、H1、SEO、图片内链、询盘入口），正式 URL 回填管线总表。
2. T8-4《Matching Braking Resistor Resistance to Your DC Bus Voltage (450–850 V)》（匹配制动电阻阻值与直流母线电压）管线回填——10-19 11:11 已发布，管线表仍写"待 Peter 批"。
3. IG-WEBSITE（Instagram 主页 website 字段改为 evbtms.com）——Peter 10-20 已批（"这个你来操作吧"），经 IG web 直接操作；bio 文本已有双链 evbtms.com | evptc.com。
4. T-MINING-COPY（矿卡三模块文案起草）——基于 REPORTS/mining-truck-research-2026-10-20.md，按 Peter"这个我没有，你去调研分析然后给我添加上去"出初稿呈批；不写技术小尾巴未决项（MOQ/交期、流量 172 vs 160、CD60/CD80 笔误）。
5. 老词推排名（每日必做第 7 项）——基于 10-19 GSC 导出，本周选 2–3 个排名 11–30 的页面做 Title/Meta/内容/内链优化（候选：mining truck thermal management 12.7、btms test 9.4、三合一产品页 10.7、high voltage coolant heater 29.3/CTR 44.4%）。
6. KEYWORD-200（200 买家词库）推进——Peter 任务，10-26 交首份词库＋排名变化报告。
7. T12-W1 GSC 提交链接准备——正式 URL 落定后给 Peter 手动提交。

## 四、需要 Peter 的事项（一句话一条）

1. LinkedIn 代发布 #5/#6/#7/#11 卡在登录图形验证：请你再接管浏览器做一次验证，或你在手机手动发（文案现成）。
2. IG 首发顺序：#6 已发，接下来 #10/#11 备稿中，先发哪篇你定一下。
3. T12-W1 五篇正式 URL 待 www.evptc.com 同步：同步完成后我给你链接，请在 GSC 手动提交。
4. 矿卡三模块文案初稿今晚给你审核。

## 五、今日不再列入（Peter 已明确关闭/不管，不再打扰）

- evptc 301 重定向工单（Peter："这个你就不要管了"）；evptc 敏感词 4 个（40644717/40644809/40660606/40668588，Peter："这个留着"）；土耳其邀请函（业务已去土耳其，关闭）；XTransfer 欧元户（财务处理）；LinkedIn 开发信（Peter 10-20 暂停）；T8 技术小尾巴（周一 t8-specs-weekly-reminder 单独问）。
