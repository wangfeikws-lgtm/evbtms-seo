# evbtms-seo — Muse × Codex 协作仓库

这是 Muse、Codex 与 Peter 之间的唯一正式协作工作台。
目标网站：https://evbtms.com/ （新站，流量优先阶段）

## 角色分工
- **Muse**：SEO 策略、搜索意图、SERP 判断、任务验收、优化方向。
- **Codex**：总调度、任务拆解、技术执行、验证、报告、GitHub 状态维护。
- **Peter**：真实业务资料、关键方案选择、正式发布与高风险修改审批。

## 状态流转
`BACKLOG` → `READY` → `DOING` → `REVIEW` → `VERIFIED` → `DONE`
- `BLOCKED`：缺资料 / 登录 / 关键决定
- `WAITING_APPROVAL`：等待 Peter 批准正式发布或高风险修改
- 验收不通过：退回 `READY` 并注明问题和证据

## 高风险变更（必须 Peter 批准）
正式发布、删除页面、修改 URL、重定向、canonical、noindex、DNS、插件及其他高风险变更。
流程：Codex 在报告中给出修改方案 → 任务标记 `WAITING_APPROVAL` → Peter 批准后执行。

## 进度同步规则
- Codex 同步执行状态、证据和报告；Muse 同步策略结论和验收结果。
- 正常执行过程（DOING / REVIEW / VERIFIED）无需通知 Peter。
- 仅在 BLOCKED、WAITING_APPROVAL、验收不通过或高风险问题时通知 Peter。

## 报告规范

每个完成的任务在 `REPORTS/` 下写一份报告，文件名 `T<n>-<slug>.md`，包含：
- 做了什么（具体改了哪些文件/设置）
- 改动前后对比（数据、截图或日志）
- 是否达到验收标准
- 遗留问题

## 内容工作流（SERP 优先铁律）

写英文文章前必须先做 SERP 调研，由 Muse 按 `TEMPLATES/serp-brief.md` 输出简报，
存 `REPORTS/serp-<关键词slug>.md`。文章任务在 TASKS.md 中引用对应的简报。
Codex 只负责发布排版，不写文案、不做 SERP。

## 安全红线

- 公开仓库，禁止上传：密码、Cookie、验证码、登录链接、客户资料、私密 GSC 导出。
- Muse 不直接修改 WordPress 生产网站；Codex 不擅自写英文文案。
- 任务涉及正式网站修改时，必须先走 `WAITING_APPROVAL`。
