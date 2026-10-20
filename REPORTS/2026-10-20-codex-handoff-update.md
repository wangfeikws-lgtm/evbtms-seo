# 2026-10-20 Codex 交接更新（基于 Muse commit c8843083）

## 已关闭 / 已同步

- T12-W1 老站 5 篇已由 Muse 发布到正式站；Muse 报告 5 个 URL 均 HTTP 200，正式 URL/ECER ID 已写入 `REPORTS/article-pipeline-and-inventory.md`（commit `c8843083`）。不再列为待办、不重复发布。
- T10/T11 的库存状态已由 Muse 修正为已发布；T8 剩余清单已改为 #6–30 共 25 篇。
- 新站 BTMS 09:00（WP 10113）、HVCH 14:00（WP 10116）、T8-5、页脚老站链接、询盘电话字段 QA 已有完成记录；HVCH 与表单/页脚 390px 视觉证据仍待补。
- Peter 已确认 12 个 URL 已向 GSC 提交索引请求；不代表已收录。

## 仍未闭环

- **BTMS 分类页效果复盘**：正式改前 GSC 基线仍缺。Windsor 搜索数据 connector 因免费方案仅支持 1 个账号、当前连接 3 个账号而暂停；需 Peter 在 Windsor 断开 2 个不用的连接，或提供 GSC 导出。恢复数据后补基线/报告，不凭旧的无日期数字下结论。
- **T7 页面结构**：20 张产品卡真实型号映射未提供，不能编造 H3。BreadcrumbList 尚需可控后台会话及桌面/390px验收。**A3→Q-3 301 先由 Muse 审方案，审完等 Peter 决定；批准前不实施。**
- **LinkedIn**：既有会话读取超时，发布状态未核实；不重复硬试。若恢复后出现 CAPTCHA，需 Peter 完成验证。
- **Instagram Bio**：旧计划记载主链接仍为 evptc.com；Peter 已选新站 evbtms.com。需手机 App 改链后再公开验收。
- **390px 验收**：HVCH 文章、表单/页脚截图待浏览器会话可用后补做；桌面和后台测试记录不等于手机端验收。

## 同步通道修复

- 已确认专用私钥文件存在（未读取或暴露私钥内容）；系统 OpenSSH 显式指定该 key 后，GitHub SSH 443 认证成功。
- 本仓库 Git 已配置显式使用系统 OpenSSH/key；本次以 `c8843083` 为基线建立隔离工作目录，未改动主工作目录中 Muse 尚未提交的 `TASKS.md`。
- GitHub 集成写入 403 不再作为阻塞，后续使用已验证 SSH 443。报告不包含账号凭据或私钥。
