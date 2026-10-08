# MUSE_REVIEW.md — Muse 入场复核

> 编写：Muse · 日期：2026-10-08（加入协作第一天）
> 依据：已通读 README.md、CODEX_INSTRUCTIONS.md、TASKS.md、REPORTS/、TEMPLATES/serp-brief.md。
> 注意：`MUSE_ONBOARDING.md` 在仓库中不存在（本地/远端均无），见第 2 节。

---

## 1. 已理解的业务与项目情况

- **公司与网站**：苏州易为联科电子科技有限公司，品牌 EVLINK；新站 https://evbtms.com/（流量优先阶段，WordPress + Elementor，Hostinger 托管）；老站 https://www.evptc.com/ 仅作内容/结构参考。
- **四品类优先级**：制动电阻（#1，未上站）> 三合一控制器 > 高压冷却液加热器 > BTMS。
- **双轨作战**：A 轨 Google Ads（即时询盘，新账户 evbtms/371-253-3088 已验证通过，老账户 evlink 已撤销）；B 轨 SEO（收录与流量）。
- **角色分工**：Muse=SEO 策略、搜索意图、SERP、验收；Codex=总调度、技术执行、验证、报告、跨项目协调、GitHub 状态维护；Peter=真实资料、关键决策、发布与高风险审批。
- **铁律**：英文动笔前必须 SERP（TEMPLATES/serp-brief.md）；公开仓库禁密码/Cookie/客户资料；Muse 不改生产站；Codex 不写英文文案；正式修改走 WAITING_APPROVAL。
- **已验证结论（我认可，不推翻）**：#7 关键词 SERP GO（T5 初稿待 Peter 确认）；GSC 基线（索引 62/noindex 22）；T0 VERIFIED；T6A/T6B 分阶段。

## 2. 仍缺少的信息

1. **`MUSE_ONBOARDING.md` 不存在**——用户要求阅读，但仓库无此文件。待确认：是由 Codex 补建，还是 T9（Codex 4 个月背景同步）的输出即覆盖此需求。
2. **Codex 4 个月背景**：T9 已建（READY），待 Codex 输出 `REPORTS/codex-4month-briefing.md`。
3. **四品类真实规格**：Peter 待提供（T6 文案、T8 页面深度都卡这个）。
4. **GSC 访问方案**：Peter 未在两个方案中二选一（浏览器接管登录 / 保持截图）。
5. **Codex 的 WordPress 后台权限状态**：未知（CODEX_INSTRUCTIONS 要求找 Peter 开通；Muse 已于今日经接管登录打通只读）。

## 3. 需要补充证据的结论（Muse 今日结论中证据不足项）

| # | 结论 | 证据缺口 | 补强方式 |
|---|------|---------|---------|
| E1 | 制动电阻 SERP 结论（EV 词可打、工业词放弃） | 基于 browser.search 快照，非无痕实时浏览器；AI Overview 未能确认 | Codex/后续用无痕复核核心词；发布后监控 AI Overview |
| E2 | "braking resistor electric bus 被 Google 判工业意图" | 快照结论，排名会浮动 | 同上 |
| E3 | R2/R3（brake chopper/sizing）内容真空 | 快照未见厂商页 ≠ 长期真空 | 建页前复查一次 |

## 4. CONFLICT 标记（待 Codex 先核对历史记录，不直接覆盖）

| 编号 | 事项 | 潜在冲突 | Muse 依据 | 状态 |
|------|------|---------|----------|------|
| C1 | WORKFLOW.md 按天给 Codex 排任务（10.9 认领 T1/T2/T7 等） | Codex 是"总调度"，排期权在他 | 用户要求 Muse 计划工作流；但具体到天的 Codex 排期应视为**建议** | 待 Codex 核对，可调整 |
| C2 | T3 拆分为 T3a（Muse 验证）/T3b（Codex 建页） | 原 T3 为整体任务，拆分是 Muse 单方面做的 | 拆分意图与原阻塞说明一致（验证后转 READY），未改变验收方向 | 待 Codex 确认 |
| C3 | 新增 T7（分类页 on-page 审计） | 是否与 Codex 已有计划/历史工作重复 | 按现有任务表无重复；但 Codex 4 个月历史我不知，需按"DISCOVER 优先"核对 | 待 Codex 核对 |
| C4 | Muse 经接管登录取得 WP 后台只读权限 | README 称"Muse 不直接修改生产网站"；只读是否在 Muse 职责内 | 用户明确要求 Muse 直连后台拿一手信息；全程只读、零修改 | 已执行，请 Codex 知悉 |

说明：以上均未覆盖原方案原文，仅标记待核对。关键冲突才提交用户决定——目前 C1–C4 均未达到提交用户的级别。

## 5. 建议调整的策略及原因

1. **T6A 转化跟踪的执行人需明确**：CODEX_INSTRUCTIONS 禁止 Codex 动 GA4/广告代码；但 T6A 上线前必须装好询盘表单转化跟踪。建议：由 Muse 出技术方案 → Peter 批准 → 执行人待定（Codex 在批准下执行，或 Peter 找建站方）。原因：职责真空会导致上线延期。
2. **T9 与 MUSE_ONBOARDING.md 合并**：若补建 onboarding 文档，建议直接以 T9 输出为准，避免两份背景文档分叉。原因：单一事实来源。
3. 其余策略（双轨、T6A/T6B、EV-only 倾向）维持今日结论，待证据补强（E1–E3）后复核。

## 6. 建议优先级（Muse 视角，供 Codex 核对）

- P0：T1、T2（技术基建，READY 待认领）、T6A（下周上线，待规格+Peter 批准）
- P1：T7（READY 待认领）、T9（背景同步）、T3a（Muse 本周做三合一 SERP）
- P2：T4（等改写稿）、T5（等 Peter 发布批准）
- 待定：T8（等 Peter：EV-only 决策+规格+大纲批准）、T3b（等 T3a 验证）

## 7. 需要用户确认的事项

1. `MUSE_ONBOARDING.md` 是否需要补建，或 T9 输出即视为覆盖？
2. GSC 访问二选一：浏览器接管登录（Peter 亲自输密码）/ 保持截图现状。
3. 制动电阻 EV-only 确认 + 产品页/文章大纲批准（今日已提交，待答复）。
4. 四品类规格资料（今日已提交，待答复）。
5. T5 博客是否批准发布（今日已提交，待答复）。
6. T6A 下周二（10.13）上线批准（10.13 前）。

## 8. 可直接交给 Codex 执行的任务（READY 状态）

- T1（noindex 排查）、T2（失败资源排查）、T7（分类页 on-page 审计）：均 READY，待认领
- T9（4 个月背景同步）：READY，输出 `REPORTS/codex-4month-briefing.md`
- 另请 Codex 核对本文件的 C1–C4，有异议直接在仓库回复或改状态
