# evbtms-seo — Muse × Codex 协作仓库

这是 Muse（SEO 策略）和 Codex（技术执行）之间的协作接口仓库。
目标网站：https://evbtms.com/ （新站，流量优先阶段）

## 分工

| 角色 | 职责 |
|------|------|
| Muse | SEO 策略、关键词地图、英文内容、任务拆解、GSC 验收、持续监控 |
| Codex | WordPress/Elementor 技术修改、批量处理、性能与资源问题排查 |
| Peter | 决策、验收、提供账号与服务器访问 |

## 工作流

1. Muse 在 `TASKS.md` 里发布任务（含背景、验收标准）
2. Codex 认领任务（把状态改为 DOING），在网站上执行
3. Codex 完成后：更新任务状态为 DONE，并在 `REPORTS/` 下写执行报告
4. Muse 用 GSC / 页面检查验收，验收通过后任务关闭

## 任务状态

- `TODO` — 待认领
- `DOING` — 执行中
- `BLOCKED` — 被阻塞（注明原因和需要的输入）
- `DONE` — 已完成，待 Muse 验收
- `VERIFIED` — Muse 已验收（由 Muse 标记）

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

## 网站技术信息

- 新站：https://evbtms.com/ — WordPress + Elementor，Hostinger 托管，Microsoft Clarity 已装，GA4 未关联
- 老站（参考）：https://www.evptc.com/ — 有大量产品页、规格表、Product Schema
- GSC 账号下有两个资产：evbtms.com / www.evptc.com
