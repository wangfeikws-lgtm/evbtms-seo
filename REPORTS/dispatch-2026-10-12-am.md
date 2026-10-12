# 早派工 2026-10-12（上午场）

## 状态盘点（截至 2026-10-12 09:22 +08）

- TASKS.md 权威版本：HEAD `3b30aaaa`（2026-10-12 09:22 +08），经 GitHub API 三步验证取回（commits/main → contents/TASKS.md?ref=sha → git/blobs → base64 解码），blob `ba4072cb32b49b65ff2cf0f15324ac2379021c3c`。
- 近 24h 提交（per_page=20 核对）：
  - 2026-10-11：**全天零提交**。
  - 2026-10-12 09:21 `f67fbd69`（EVLINK Codex）"Deliver BTMS cold-start Instagram review asset package"：新增 REPORTS/instagram-BTMS-review-package-2026-10-12.md（仅内容评审包，**未发布**、未上传）。
  - 2026-10-12 09:22 `3b30aaaa`（Codex）"Record published LinkedIn sample evaluation post"：新增 REPORTS/linkedin-published-2026-10-12.md，TASKS.md 新增 S-LI-20261012 → REVIEW。
- TASKS.md 当前状态分布：T0/T1/T2/T5/T7/T9/T10/T11 均为 VERIFIED；**无 READY 任务**；T3/T4/T6/T8 均为 BACKLOG；新增 REVIEW 一项：S-LI-20261012。

## 🔴 点名升级（核心逾期项连续三天零交付）

按派工规则标注：Codex 在核心任务上已连续多日零交付，继续点名——

- 10-09：缺席 9:00 BTMS / 14:00 HVCH 两档自动发布。
- 10-10：缺席 14:00 档；T7 🟡 结构项整改零交付；17:30 下达的 T10/T11 正文恢复指令零执行。
- 10-11：全天零提交，上述逾期项无一补交。
- 10-12 今早 09:21/09:22 的两笔提交均为社媒件（Instagram 评审包＋LinkedIn 已发帖记录），**不是**逾期核心项的补救：T10/T11 正文恢复、T7 结构项、每日 WP 自动发布三项至今仍无任何交付证据。社媒交付认可，但不能抵核心逾期。

## Codex 今日任务（编号＋交付物＋时间点）

1. **T10/T11 线上正文恢复原批准版（最高优先，已逾期约 40 小时）**：用仓库原稿（REPORTS/T10-integrated-controller-cost-draft.md、REPORTS/T11-thermal-control-strategy-draft.md）替换 WP 文章 9949（T10）、9951（T11）正文；URL Slug、SEO title/meta 保持不变，只替换正文；**今日下班前完成**并转 REVIEW，提交 REPORTS 验收报告。
2. **T7 🟡 结构项整改（已逾期，原期限 10-10 下班前）**：按 REPORTS/T7-fix-checklist.md 🟡 部分——加热器页 20 张产品卡 H3 去重＋8 个空 H3 补标题、页脚空 H2 模板修复、面包屑、中文文件名、重复链接确认；**今日下班前交付**并转 REVIEW。
3. **每日自动发布补交与执行**：今日 9:00 BTMS 档截至 09:22 仓库无 WP 发布交付证据，立即说明情况并补交；14:00 HVCH 档今日必须按规则执行，冲突排队、不许暂停；发布后更新 TASKS.md＋REPORTS。
4. **Instagram BTMS 评审包后续**：该包状态为 READY FOR CONTENT REVIEW、未发布；资产目前只在 Codex 本地、未入仓，仓库侧无法做视觉 QA——请把三张图（1080×1350）与 content.md 入仓供 Muse 评审；**未经 Peter 明确批准不得上传/发布**。
5. **S-LI-20261012 证据补强**：其报告自认图片移动端完整视觉验收未做、截图因权限未归档；补齐移动端图片视觉证据后回写报告（帖已发布，勿重复发布）。
6. **T3b 待命**：Muse 完成 T3a SERP 验证后，按"验证路线图"逐词认领建页；未经 SERP 验证的词不得建生产页面。

## Muse 今日任务

1. 验收 S-LI-20261012（REVIEW）：09:25 巡检已独立抓取正式页核验通过（英文正文、五项样件输入、4 标签与报告一致，无编造参数/认证声明），结论 VERIFIED；回写推送待主会话执行（proposed 文件已备于 hidden_files/watch-2026-10-12-0925/，推送前须再核 HEAD 未动）。
2. 内容评审 Instagram BTMS 评审包：核对 Caption/6 标签/三张卡 Alt 与来源口径（源自站内 post 9931 的存储/循环启动/冷浸/预调温条件），Codex 入仓图片后补视觉 QA；未过评审＋Peter 未批准前不发布。
3. 验收 Codex 今日交付：T10/T11 正文恢复（公开页核验 HTTP200、self-canonical、index、正文与原稿一致）、T7 结构项（逐项证据核验）、9:00 补交与 14:00 发布档。
4. T3a：继续剩余长尾词 SERP 验证，验证通过词交接 T3b。
5. T6A Google Ads：关键词/结构草稿已于 2026-10-11 在本地备好（REPORTS/T6A-ads-keyword-structure.md，待推送入仓）；广告文案待 Peter 四品类规格资料到位后补，上线口径按"广告客户验证通过后"（见需 Peter 第 2 条）。

## 需 Peter 的事项（一句话一条）

1. T8 制动电阻：仍缺市场范围确认（仅 EV/商用车 vs 兼做工业变频器/电梯/起重机）＋真实规格参数，T8 和 T6B 都被这条卡住。
2. Google Ads：账户仍因广告客户验证未完成而暂停，10-13 上线需改到"验证通过后"，请你完成验证；T6A $32/天（三合一 $12＋加热器 $12＋BTMS $8）草稿已就绪待你批准。
3. T6 落地页与广告文案前置：四品类规格资料仍待你提供（与第 1 条合并提供更省事）。
4. Instagram BTMS 评审包：内容评审通过后，发布仍需你明确批准才可上传。
