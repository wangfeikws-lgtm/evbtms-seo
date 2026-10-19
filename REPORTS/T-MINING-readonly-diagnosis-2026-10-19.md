# T-MINING 矿卡页面三块内容只读诊断

- 页面：https://evbtms.com/electric-mining-truck/
- 核对日期：2026-10-19
- 本轮未修改生产站。

## 当前仍公开的三块占位内容

1. Validation for Harsh Mining Conditions：仍显示要求未来替换为已验证测试证据的内部编辑提示。
2. Show the Proof Behind the Engineering：仍显示四张泛占位卡及“Replace these editable placeholders”提示。
3. Electric Mining Vehicle Thermal Project：仍显示要求替换为真实案例的占位提示。

## 执行阻塞

- 仓库与本机均找不到任务引用的 `hidden_files/mining-truck-baseline-2026-10-15.md`。
- 当前没有三块已批准目标文案、真实工厂照片、可追溯测试证据或获授权客户案例。
- 在这些输入缺失时不能自行编造，也不能安全覆盖生产内容。

## 最小安全修复方案

1. 先导出当前 Elementor 页面 JSON 或创建 WordPress revision，并保存公开 HTML、桌面与 390px 截图作为新现场基线。
2. 只编辑上述三个 section，不整页导入，不改模板、主题、插件、URL、canonical 或 noindex。
3. 每块分别保存并立即核验前台；失败时先检查 revision、缓存和编辑器状态，不升级插件。
4. 验收必须确认占位词消失、目标内容与批准稿一致、图片和 alt 合规、CTA 正常、HTTP 200、唯一 H1、self-canonical、index/follow、title/meta/URL 不变。
5. 生效后观察 7–14 天，异常时用 revision 只回滚这三块。

## 状态

`BLOCKED`：需要 Peter 提供/确认三块目标文案与真实素材，或批准先删除明显内部占位内容并保留中性框架。
