# OPERATING_SYSTEM.md — Muse × Codex 协同操作系统

## 原则

- GitHub是正式事实来源，聊天只负责通知、讨论和审批。
- 多项目并行；调研、写作和资料整理可并行。
- 同一页面、文件、后台设置或任务状态同一时间只有一方修改。
- 开工前拉取并发现已有产物，提交前再次检查冲突。
- 结论保留来源、日期和证据状态；未知保持未知。

## 文件责任

| 文件/目录 | 主维护人 | 另一方动作 |
|---|---|---|
| MUSE_ONBOARDING.md | Codex | Muse在MUSE_REVIEW.md复核 |
| PROJECTS.md | Codex | Muse补充策略状态 |
| TASKS.md | Codex维护执行状态；Muse维护验收 | 修改前先拉取 |
| MUSE_STATUS.md / MUSE_REVIEW.md | Muse | Codex读取，不覆盖 |
| REPORTS/serp-*、英文内容稿 | Muse | Codex复用，不重复调研/写作 |
| REPORTS/T*-audit/fix | Codex | Muse验收，不重复技术审计 |
| SYNC_LOG.md | 双方追加 | 只追加，不重写历史 |

## 双向同步节奏

### 工作日08:30

双方拉取仓库，阅读任务、项目、对方状态和最新同步日志；检查依赖、冲突和可并行任务，认领后开工。

### 重要变化即时同步

任务认领、阶段完成、新证据、阻塞、审批需求、验收结果和正式发布结果必须提交。普通思考、无状态变化轮询和无结论尝试无需提交。

### 工作日17:30

Codex更新执行状态、报告和次日技术计划；Muse更新策略状态、验收结果和次日研究计划；双方在SYNC_LOG.md各追加一条记录。仅BLOCKED、WAITING_APPROVAL、验收失败或高风险问题通知Peter。

### 每周五

Codex提交跨项目完成/阻塞/下周执行摘要；Muse提交策略、搜索、内容与验证摘要。过时结论标注superseded日期和替代来源，不删除历史。

## 风险门禁

正式发布/删除、URL/重定向、canonical/noindex、DNS/插件、广告上线与付费、不可可靠回滚的生产变更必须先转WAITING_APPROVAL。只读审计、草稿、调研、报告和非生产测试可直接进行。
