# 2026-10-20 页脚、询盘表单与 Instagram 链接执行报告

## 已完成并公开生效

- 全站页脚仅新增老站品牌链接：`Our legacy site: evptc.com`，目标为 `https://www.evptc.com/`。
- Fluent Forms 表单 ID 1 的 `Phone Number/WhatsApp` 已从数字字段改为电话文本字段（`input_text` / `type=tel`）。
- 保留原字段名 `numeric_field`，避免破坏既有邮件通知映射和历史数据。
- 新增输入提示：支持国家区号、空格、`+`、括号和连字符。

## 询盘链路验收

- 使用正式前端提交接口完成一次明确标注的内部 QA 测试。
- 提交成功并返回感谢页：`https://evbtms.com/thanks/`。
- 后台生成 Entry ID `22`。
- 测试号码 `+86 138 0013 8000` 在后台原样保存，未再丢失 `+`、空格或前导数字。
- 通知日志：`EmailNotification (Email sending initiated)`，发送目标为 `wangfeikws@gmail.com`，主题为 `New Website Inquiry - EVLINK Electronics`。
- 桌面公开页已确认表单字段与页脚链接可见；390px 实机复核因本轮浏览器控制连接超时，留到下一次可用会话补一张证据截图，不影响本次字段和后台链路结果。

## 备份

- `backups/evbtms-2026-10-20-footer-form/block-9-before.txt`
- `backups/evbtms-2026-10-20-footer-form/fluent-form-1-before.json`
- `backups/evbtms-2026-10-20-footer-form/fluent-form-1-after-fields.json`

## 唯一剩余用户操作

- Instagram `@evlinkautoparts` 当前主链接仍是老站。
- Instagram 桌面编辑页明确限制链接只能在移动端修改，因此未用修改 Bio 文本的方式绕过。
- Peter 需在 Instagram 手机 App 将主页链接改为 `https://evbtms.com/`；完成后 Codex 再做公开页核验。

## 状态

- 页脚：`REVIEW`（已公开生效，待 Muse 独立验收）。
- 表单字段及后端链路：`REVIEW`（已完成并有 Entry 22 与通知日志证据）。
- Instagram 主链接：`WAITING_USER_ACTION`（平台移动端限制）。
