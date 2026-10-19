# T-MINING 矿卡页面与询盘链路修复（2026-10-19）

## 结论

- 状态：`REVIEW`，待 Muse 做独立验收。
- 矿卡正式页：https://evbtms.com/electric-mining-truck/
- 联系正式页：https://evbtms.com/contact/
- 本轮未改 URL、重定向、DNS、插件、主题或广告设置。

## 已执行并公开生效

1. 矿卡页面 15 处精确替换，移除三类公开内部占位提示。
2. 将案例表述改为真实边界：EVLINK 有电动矿卡热管理项目经验，但客户名称、车辆数据、工况及验证结果受保密义务约束，未经书面许可不公开。
3. 将“工厂/测试照片占位”改为项目阶段可提供的产品接口资料、质量记录、验证支持及追溯/交付文件，不冒充已有公开照片或客户案例。
4. 保留现有矿卡项目输入清单与询盘 CTA，避免重复堆叠同一清单。
5. 联系页移除 `Replace the Fluent Forms ID...` 内部模板提示，改为正式工程询盘说明。
6. 同步更新 Elementor 数据与 WordPress 正文层，并刷新 Elementor 生成缓存。

## 正式页验收

- 两页 HTTP 200。
- 两页各 1 个 H1。
- 两页均为自指 canonical，未发现 noindex。
- 矿卡页指向 Contact 的链接 2 个；联系页正式表单仍存在。
- 四类旧占位文本在两张正式页均为 0。
- 矿卡页新的保密项目经验文案在正式 HTML 可见；联系页新的正式说明在正式 HTML 可见。
- 已生成桌面及窄视口截图用于视觉复核；本机 Chrome 无头模式存在最小布局宽度限制，因此不把该窄图误报为独立真 390px 设备验收。

## 询盘链路测试

- 正式 Fluent Forms 表单：`EVLINK Inquiry`，Form ID 1。
- 必填字段：姓名、Email、Message；Phone/WhatsApp 当前不是必填。
- 2026-10-19 提交一条明确标记为内部 QA、请忽略的测试记录。
- 前台返回成功并跳转 `/thanks/`；后台生成 Entry ID 21。
- 后台日志显示 Email Notification 已触发到当前配置收件人，主题为 `New Website Inquiry - EVLINK Electronics`。
- 这里只能确认系统发信动作已启动，不能替代收件箱实际到达确认。

## 发现但未擅自扩大修改

- Phone Number/WhatsApp 当前使用 `input_number`。测试号码前导零被归一化为 `0`，国际号码中的 `+`、空格和前导零可能丢失。
- 建议下一轮将该字段改为电话/文本字段并保留原字段名，随后再做一次前台、后台和邮件链路回归；本轮未直接改表单结构，避免未审计更新接口时破坏现有询盘表单。
- 邮件日志证明已触发通知；Gmail 是否进入收件箱/垃圾箱仍需 Peter 在实际邮箱确认。

## 备份与回滚

- 修改前 Elementor 与 WordPress 正文备份保存在本机：`backups/evbtms-2026-10-19/`。
- 精确替换脚本：`scripts/update-evbtms-mining-contact.ps1`。

