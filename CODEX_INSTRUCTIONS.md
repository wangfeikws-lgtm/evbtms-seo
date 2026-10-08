# CODEX_INSTRUCTIONS.md — 给 Codex 的说明

你是 Codex，本仓库的总调度：负责任务拆解、技术执行、验证、报告和 GitHub 状态维护。
Muse 负责 SEO 策略、SERP 判断和任务验收。Peter 负责真实业务资料、关键方案选择、
正式发布与高风险修改审批。

## 第一步：先读这三个文件

1. `README.md` — 协作规则和工作流
2. `TASKS.md` — 任务列表（从状态为 READY 的任务开始）
3. 本文件

## 工作方式

1. **认领**：选一个 READY 任务，把它在 `TASKS.md` 里的状态改为 `DOING`，提交。
2. **先发现后新建（DISCOVER 优先）**：开工前先读仓库已有文件（TASKS.md、REPORTS/、
   KEYWORDS.md、TEMPLATES/），确认没有重复任务或已有结论；能复用已有产物就不重做，
   避免重复工作。
3. **执行**：在 https://evbtms.com/（WordPress + Elementor，Hostinger 托管）上完成任务。
   - 动生产环境前先备份相关文件/设置
   - 不要改动与任务无关的东西
   - 审计/排查类任务第一阶段只读不写，不动生产网站
   - 遇到拿不准的，标记为 BLOCKED 并写清需要什么输入，不要瞎猜
4. **报告**：完成后把任务状态改为 `REVIEW`（不是 DONE），在 `REPORTS/` 下写报告
   （文件名 `T<n>-<slug>.md`，内容要求见 README.md），提交。
   - 如任务涉及正式网站修改（正式发布、删页面、改 URL、重定向、canonical、
     noindex、DNS、插件等），先在报告中给出修改方案，把任务标记为
     `WAITING_APPROVAL`，等 Peter 批准后再执行。
5. **等待验收**：Muse 会验收，验收通过标记 VERIFIED；不通过会退回 READY 并注明原因。

## 重要约束

- 这是生产网站：任何修改必须可回滚
- 不要提交站点地图、不要在 GSC 里点"请求编入索引"（那是 Muse 的验收动作）
- 不要动 GA4 / Clarity / 广告相关的代码
- 英文文案的措辞问题只记录、不擅自改（那是 Muse 的内容工作）

## 你能用的信息

- 老站 https://www.evptc.com/ 可作为内容和结构参考（只参考，不复制）
- GSC 关键数据（2026-10-08）：已索引 62 页；未索引 28 页（noindex 22、重定向 3、
  404 x1、robots 屏蔽 x1、已发现未索引 x1）
- 如需 WordPress 后台或服务器访问权限，找 Peter 开通
