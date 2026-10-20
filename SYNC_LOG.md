# SYNC_LOG.md — Muse × Codex 双向同步日志

> 只追加重要变化。详细证据放在REPORTS/，任务状态放在TASKS.md。

### 2026-10-08 18:00 +08 — Codex

- 完成：建立共享背景、操作系统、项目总览和四个月背景简报。
- 新证据：已核对Muse当日任务表、周计划、状态和入场复核，未覆盖Muse产物。
- 状态变化：T9资料已提交，等待Muse验收。
- 交接给：Muse阅读onboarding与背景简报，复核C1-C4。
- 需要Peter：暂无；真实规格、发布与广告上线仍按现有门禁。

### 2026-10-09 11:00 +08 — Codex

- 完成：汇总并落盘今天上午7个日常项目成果，统一存入 `REPORTS/2026-10-09-morning/`。
- 新站：T1/T2/T7只读审计、公开页面证据、首页资源清单和抽查结果已同步；生产站未修改。
- 老站：191页索引问题分类框架、公开核查证据、重要页面队列与证据缺口已同步。
- 阿里国际站：5个重点商品标题、关键词分组、真实参数缺口与执行边界已同步；后台未修改。
- 社媒：Instagram HVCH草稿与进度、Facebook BTMS待审批稿、YouTube制作包已同步；均未发布。
- 状态变化：Windows沙箱启动故障已修复；浏览器页面读取仍存在偶发超时。LinkedIn已进入发帖流程，等待最终发布结果与链接后补记。
- 交接给：Muse可直接审阅今日目录中的策略、事实边界与缺口，避免重复调研或重写。
- 需要Peter：LinkedIn最终公开发布按界面行动时确认；YouTube需真实产品图和Logo；阿里商品上线前需补齐真实规格、证书、MOQ、交期和质保。

### 2026-10-10 +08 — Instagram closeout
- PUBLISHED / REVIEW：@evlinkautoparts HVCH三页轮播，2026-10-09 17:40:29 +08。
- https://www.instagram.com/p/DeRNYCPm5PC/
- 旧BLOCKED/未发布状态已被正式页面、正文和三页Alt核验覆盖；勿重复发布。
- 详情：REPORTS/instagram-HVCH-published-2026-10-09.md。手机实机及匿名可见性未独立验收。

## 2026-10-10 LinkedIn — REVIEW
Previous post verified; 18 impressions / 10 members reached / 1 profile viewer / 0 reactions-comments-reposts. New original three-in-one English post and image prepared, NOT published. Sources: product brief + T10/T11. Report: REPORTS/linkedin-review-and-next-post-2026-10-10.md. Pending: recent-content duplicate check and publication preview. No profile edits, messages, invitations or ads.

### 2026-10-09 +08 — Codex Facebook协助

- Facebook：BTMS普通帖子已发布且核验，正式URL见REPORTS/2026-10-09-facebook-instagram-assistance-sync.md；未创建广告，不重复发布。
- Instagram：当时Business Suite未关联@evlinkautoparts；该旧阻碍已由Instagram直接登录发布成功所取代，以上方2026-10-10 closeout为准。
- T7：总中心已验收，不再修改。T10/T11：本协助聊天尚未发布，维持READY，不能报告完成。
- 详细进度及操作边界见上述报告。

### 2026-10-10 +08 — Codex Facebook收尾
- 原BTMS帖历史正文/配图证据已复核，未重复发布；当前公开抓取失败，互动基线未知，不记录0。
- 完成三合一自然帖英文草稿与配图需求，基于本地Muse product brief v2；远端最新版本因SSH认证与公开抓取失败未确认。
- 报告：REPORTS/facebook-closeout-2026-10-10.md；草稿：REPORTS/facebook-three-in-one-draft-2026-10-10.md。
- 未投广告、未发私信、未排期。实时验收待浏览器控制恢复；main推送此前审批拒绝，未绕过。

### 2026-10-10 +08 — Instagram task-state correction
- 拉取main并读取快速交付标准；S-IG-20261009从旧BLOCKED更正为REVIEW，对应已发布正式URL及报告。无需Peter绑定Business Suite；无新增帖子。


### 2026-10-10 +08 — Codex article publication closeout
- T10 9949 / T11 9951 published, REVIEW: https://evbtms.com/integrated-thermal-management-controller-cost/ and https://evbtms.com/ev-thermal-management-control-strategy/ .
- Both public HTTP200, self-canonical, index; desktop and 390px preview evidence recorded. Distinct feature diagrams and SEO present; T11 mobile entry animation resolved by actual rendered-body inspection. No global settings modified.
- T5 matching live topic 9941: https://evbtms.com/ptc-coolant-heater-vs-air-heater/ HTTP200. Existing automatic article, not a verbatim Muse draft; REVIEW for content mapping, no duplicate publication.
## LinkedIn 正式发布收尾 — 2026-10-10执行包
PUBLISHED / REVIEW：https://www.linkedin.com/feed/update/urn:li:activity:7514545560205336577/ 。已完成近期去重、正文/原创配图/Alt预览、公开动态发布成功核验与正式URL截图。此前未发布状态由本记录覆盖。TASKS S-LI-20261010及对应报告已更新，勿重复发布。
## 2026-10-10 Codex — 每小时低 Token SOP 固化

- 自动检查已调整为周一至周六 08:30–17:30 每小时运行，采用提交哈希增量读取。
- `OPERATING_SYSTEM.md` 已加入“每小时增量同步 SOP”：只读变化、READY 连续执行、最小回写、同轮推送、无变化保持安静。
- 后续每轮不再重复通读全部历史；以公开结果、验收证据和 GitHub 提交作为交付标准。

## 2026-10-10 Codex — 建立 Muse 每日计划派工入口

- 新增 `DAILY_PLAN.md`：Muse 每日 08:15 前整理当天可执行任务，必须关联 `TASKS.md` 编号、输入、批准状态、验收标准和负责人。
- Codex 08:30 去重校验并分配到对应子项目；整点领取临时新增；子项目只执行并回交证据。
- 每日计划、执行、验收、回写形成闭环，避免子项目无任务或重复工作。

## 2026-10-10 Codex — 仓库检查频率调整

- 按 Peter 要求，从每小时改为工作时间每2小时检查：08:30、10:30、12:30、14:30、16:30；17:30单独收尾。
- 每轮仍采用提交哈希增量读取，持续领取 Muse 新计划、同步子项目进度和回写交付结果。

## 2026-10-10 Codex — 首次读取调整为08:45

- Peter确认电脑通常08:40已开机，首次读取和派工由08:30改为08:45。
- 后续增量检查为10:45、12:45、14:45、16:45；17:30保留独立收尾。


## 2026-10-12 Facebook 三合一审核包
- WAITING_APPROVAL：未找到针对该新帖的具体发布批准，未发布/排期。英文终稿、Alt及原创1200×1200品牌文字图已完成，视觉核验无文字溢出。
- 成品：REPORTS/facebook-three-in-one-review-2026-10-12/。只普通有机帖子，禁止广告/Boost/预算/私信。

### 2026-10-12 +08 — Instagram review package
- Live account20 posts, newest old HVCH; no duplicate created. BTMS source recovered and three1080x1350 text slides delivered for review. No new READY publication task in current plan; no post published.
- REPORTS/instagram-BTMS-review-package-2026-10-12.md; local assets E:\codex项目\instagram\review-package-BTMS-2026-10-12. Caption/Alt/CTA included; actual upload preview pending.

## 2026-10-12 LinkedIn — PUBLISHED / REVIEW
发布三张Peter产品图配英文样件评估五项输入清单；正式URL https://www.linkedin.com/feed/update/urn:li:activity:7515219048998264832/ 。公开范围/正文/三图/标签核验；390px正文预览通过，图片移动完整视觉验收待补。10月10日帖14回应/144展示。报告已回写，勿重复发布。

### 2026-10-12 +08 — Instagram product-photo publication
- S-IG-20261012 REVIEW：BTMS原图6087衍生封面+两页信息卡，已按Peter直接授权发布；https://www.instagram.com/p/DeYevQglE0t/，13:26:53 +08。
- 正文、CTA、六标签、三页Alt、AI标签与正式URL核验；旧审核包被本次发布版替代，不再单独发布。REPORTS/instagram-BTMS-published-2026-10-12.md。

### LinkedIn mobile closeout 2026-10-12
390x844 three images visually verified and screenshot archived locally. Report updated. Peter approved screenshot/report upload to wangfeikws-lgtm/evbtms-seo on 2026-10-12; no duplicate post.

### 2026-10-12 — Codex website report synchronization
- Peter直接批准本次仓库合并同步；保留本地Facebook记录与远端LinkedIn/Instagram/T3a记录，不强推。
- 上午9955已由Peter发布，公开HTTP/SEO/图/5内链验收报告入仓；视觉验收未完成，不重复发布。
- HVCH仍DOING研究断点，未成稿；T7仅范围复核、未新增生产修改；T3b排期/规格清单提交REVIEW，已按新T3a裁决更新，不建生产页。
- 本条仅同步实际状态，不把未完成项、配置ACTIVE或任务转达计为交付。

### 2026-10-12 — Peter要求任务标题具体化
- T3b标题已改为中文具体任务名，明确站点、页面类型、排期和规格清单；编号保留作内部索引。
- 后续仓库新任务与对Peter汇报应使用“中文具体任务名 + 编号”，说明做哪个站/页面、交付什么、是计划/草稿/已发布。不得仅写T3b、T7等代号让Peter猜内容。
- 此次仅调整可读性，保留Muse的VERIFIED验收及未建生产页边界，未改变发布权限。

### 2026-10-13 — HVCH升温响应文章9963正式发布
- Peter直接确认“预览正常，发布”；Codex通过已验证WordPress API发布，未改已验收正文，未增加参数。
- https://evbtms.com/hvch-warm-up-response-validation/ ：HTTP200、index、self-canonical、唯一H1、SEO、特色图和5内链核验。
- 视觉确认来自Peter，不记为代理独立手机/桌面检查；实际Google收录未知。
- 发布前备份及验收报告已保存；TASKS转REVIEW，Muse下一步独立验收。旧草稿状态被本次发布结果覆盖，勿重复发布。

### 2026-10-15 — T8修正版10016重发 / REVIEW
- 用户直接批准重发和生成缓存刷新，两处修正版公开生效、旧句不存在，HTTP200/index/canonical/H1/图/链接通过。
- 报告REPORTS/T8-corrected-republished-2026-10-15.md；独立桌面390px截图待补，勿重复发布。

### 2026-10-14晚 — 800V页面10033正式发布 / REVIEW
- Peter直接发布指令已核实；HTTP200/index/self-canonical/唯一H1/SEO/CTA/三内链通过。预览来自总中心，不记为本代理独立截图。
- 报告REPORTS/800V10033-published-2026-10-14.md；不重复发布，不展开其他项目。

### 2026-10-14下午 — HVCH10031用户指令后发布 / REVIEW
- https://evbtms.com/hvch-power-verification/ ：HTTP200、SEO、特色图10030、index/self-canonical/唯一H1及5内链通过。上午/下午日更均发布；不重发T8草稿。
- 已读取LinkedIn解释型内容方法，后续网站内容按买家问题和证据适配，不机械复制或新增跨平台动作。
- 证据：REPORTS/HVCH10031-published-2026-10-14.md。

### 2026-10-14下午 — BTMS10019发布对账与HVCH10031新稿
- 上午10019已发布REVIEW，下午10031完整草稿与特色图10030已保存，阶段9待可靠预览，未发布。
- 核实T8最新10016为draft，遵守撤回不重发；旧图验收不覆盖当前状态。审批服务恢复后补齐此前未同步的文章记录。
- 证据：REPORTS/BTMS10019-HVCH10031-status-2026-10-14.md。

### 2026-10-14 — T8液冷制动电阻英文页发布与主图同步 / REVIEW
- 页面10016正式发布。生成缓存刷新后正文媒体9971效果图及非实拍说明公开生效，两个其他占位保留。
- HTTP200/index/self-canonical/唯一H1/三产品内链通过。独立桌面/390px截图待补，Google收录未知。不重复建页。
- 报告：REPORTS/T8-page-published-image-fixed-2026-10-14.md。

### 2026-10-13 — T8液冷制动电阻中文宣传PPT交付 / REVIEW
- Codex按 `REPORTS/T8-promo-content-pack-2026-10-13.md` 完成11页中文宣传PPT，只做版式与视觉执行，未擅自扩写技术结论。
- Peter提供的实物图与CAD图已用于第3页结构参考：圆筒壳体、大圆端盖、冷却接口、高压连接器、吊耳和安装支架；图中醒目标注“概念效果图，非实物照片”。
- 成品：`REPORTS/EVLINK-T8-liquid-cooled-braking-resistor-promo-2026-10-13.pptx`；验收说明：`REPORTS/T8-promo-ppt-acceptance-2026-10-13.md`。
- 11页包完整性、版面越界、元素重叠检查通过；6条内容冻结红线已逐项自查。状态转 REVIEW，交 Muse 做内容终审；英文分类页仍为独立任务，不得把本次PPT交付误报为网站上线。

### 2026-10-14 — Facebook S-FB-20261012 发布状态纠正 / REVIEW
- 发现仓库仍把已发布任务写为 READY；核对本地发布报告、正式 URL、正文和截图后确认该帖已于 2026-10-12 发布，本轮未重复发布。
- 正式URL：https://www.facebook.com/evlinkthermal/posts/pfbid0NYn8MLJaBz3FCHCFFEXZc3KdH5mAN1ccVnrSSQSbX8CjA81jjPhBfRMiwQYUc9gul
- 已核对普通公开主页帖、三合一产品主图、全文和速推关闭；未创建广告、Boost、预算或私信。
- TASKS 状态由 READY 更正为 REVIEW；匿名访问、手机实机和互动指标仍未独立验收。
- 报告：REPORTS/facebook-three-in-one-published-status-correction-2026-10-14.md。

### 2026-10-14 +08 — Instagram independent QA
- 基线285339e；无新Instagram READY项，补齐S-IG-20261012三页390px响应式证据，保持VERIFIED，无线上写操作。
- REPORTS/instagram-responsive-QA-2026-10-14.md；不把等待验收当停工，下一项HVCH素材核验仍可独立推进。

### 2026-10-15 — T7 分类页结构项当前实况复核 / REVIEW
- 只读核验三个公开分类页：HTTP200；页脚空H2与全角冒号已修复，未重复修改生产站。
- HVCH 20张产品卡H3仍按8/4/8重复；三页仍无可识别面包屑/BreadcrumbList。
- 当前产品卡重复目标缩小为Q-3两个、A3两个，旧8+8结论不再直接适用。
- 下一步需要Peter确认真实型号/唯一标题方案及批准面包屑生产修改；证据见REPORTS/T7-current-structure-recheck-2026-10-15.md。

### 2026-10-19 — T-MINING 矿卡公开占位清理与询盘链路 QA / REVIEW
- 矿卡页 15 处精确修复公开生效：删除内部编辑占位；改为真实的保密项目经验、工程资料和验证支持边界，不公开客户名称/参数/结果。
- 联系页模板提示已删除；两页 HTTP200、唯一H1、自指canonical、index/follow，旧占位文本为0。
- 正式询盘表单内部 QA 提交成功，后台 Entry ID 21，邮件通知日志显示已触发；实际邮箱到达仍需 Peter 核对。
- 新发现：Phone/WhatsApp 使用数字字段，可能丢失 `+` 和前导零；未擅自改表单结构，列为下一轮修复。
- 报告：`REPORTS/T-MINING-inquiry-chain-fix-2026-10-19.md`；状态转 REVIEW，交 Muse 独立验收。

### 2026-10-19 +08 — T10/T11 与 HVCH 当日档状态纠偏

- T10/T11 已于 2026-10-10 正式发布并通过 Muse 验收；2026-10-19 的“待发布/14:00 红线”为重复派工，现已纠正，禁止重复发布。
- T10：https://evbtms.com/integrated-thermal-management-controller-cost/
- T11：https://evbtms.com/ev-thermal-management-control-strategy/
- HVCH 当日补档已发布并技术验收：https://evbtms.com/hvch-insulation-resistance-commissioning-checks/（ID 10097）。
- 证据：REPORTS/T10-T11-published-2026-10-10.md；REPORTS/DAILY-BTMS-HVCH-gap-audit-2026-10-19.md。

### 2026-10-20 +08 — GSC 手动请求编入索引

- Peter 已确认完成本轮 12 个新发布或近期更新 URL 的 GSC“请求编入索引”，包括今日 BTMS、新近 BTMS/HVCH 补档、T8 制动电阻文章、800V PTC 产品页、矿卡页、T10/T11及两篇 HVCH 技术文章。
- 口径：仅记录请求已提交，不代表 Google 已完成抓取或收录；后续按 7–14 天复查，不重复提交。

### 2026-10-20 +08 — T12-W1 老站5篇改派 Muse 发布

- Peter 决定：T12-W1 五篇英文文章不再由 Peter 手动处理，改由 Muse 负责上传、正式发布、公开验收和仓库回填。
- Codex 已完成5份最终发布包，均在 `REPORTS/T12-W1-0*-publish-package.md`；事实红线与占位内链已清理，未发布生产页。
- Muse 发布顺序按 01→05；每篇发布后回填正式 URL、发布时间、文章 ID，并验收 HTTP 200、index/follow、canonical、唯一 H1、SEO 字段、图片、内链和询盘入口。
- 状态口径：当前仅“已写完并交接”，正式 URL 验收前不得标记为已发布或完成。

### 2026-10-20 +08 — 页脚品牌链接与询盘表单修复 / REVIEW

- 全站页脚已新增老站品牌链接 `https://www.evptc.com/`，公开页可见。
- 联系表单 Phone/WhatsApp 已由数字字段改为电话文本字段；保留原字段名和通知映射。
- 正式接口 QA 成功，后台 Entry ID 22；`+86 138 0013 8000` 原样保存，邮件通知日志显示已发送到 `wangfeikws@gmail.com`。
- Instagram 主链接需 Peter 在手机 App 改为 `https://evbtms.com/`；桌面端不允许编辑主页链接。
- 报告：`REPORTS/2026-10-20-footer-form-instagram-execution.md`。390px 截图待浏览器控制恢复后补证，不把待补截图误报为已验收。

### 2026-10-20 +08 — 低 Token 执行节奏更新

- Peter 确认采用单独当天执行会话、每天最多一篇老站文章、浏览器失败后不循环重试、无变化即结束、一次核验/回写/推送的标准。
- 总协调固定触点收敛为 08:46 任务提醒、11:20 上午汇报、17:20 当日汇总；旧版每两小时和 16:45/17:30 重复检查条款废止。
- 已更新 `COLLABORATION_STANDARDS.md`、`CODEX_INSTRUCTIONS.md` 与 `OPERATING_SYSTEM.md`；任务真相源 `TASKS.md` 的既有未提交修改未触碰。
- 17:20 自动汇总已改为只读取新增提交、变更任务行和新证据；冗余小时检查自动化在应用中已不存在，无需另行运行。

