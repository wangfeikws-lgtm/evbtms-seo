# T7 整改执行清单（精确到字段）

> 来源：REPORTS/T7-category-onpage-audit.md｜Peter 2026-10-09 批准执行
> 图例：🟢 Peter/现在可点（字段级）｜🟡 Codex 工单（结构级）

## 🟢 现在就能点的（WP 后台，几分钟一个）

### 1. 三合一页 meta description 加句号
- 位置：WP 后台 → 页面 → 找到 "Three-in-One Controller" → Rank Math SEO metabox → Description
- 现状：`...for electric and commercial vehicle applications`（末尾无句号）
- 改为：末尾加 `.`

### 2. 加热器页 Title 命名统一（二选一，需 Peter 定）
- 位置：同上 → Rank Math → Title
- 现状：`High Voltage Coolant Heater Manufacturer | EVLINK`
- 选项 A：`High Voltage Coolant Heater for Electric Vehicles | EVLINK`（与其他页模式一致）
- 选项 B：全站统一加 Manufacturer（不推荐）
- ⚠️ 请 Peter 先选 A/B

### 3. 三合一页 Title 改名（与复盘文档一致）
- 位置：同上 → Rank Math → Title
- 现状：`Three-in-One Controller for EV Systems | EVLINK`
- 改为：`Three-in-One Thermal Management Controller for Electric Bus | EVLINK`

### 4. 三合一页 4 张产品图 alt 去重
- 位置：媒体库 → 找到 4 张 "Product Views" 产品图 → alt 文本
- 现状：4 张全是 `Three-in-one Controller`
- 改为（按图内容）：`Three-in-one controller front view` / `side view` / `connector close-up` / `cooling fins detail`（看图写意，核心是 4 张不重复、带描述）

### 5. 加热器页 Energy Storage 卡片 alt 错位
- 位置：该页面 Elementor 编辑 → 应用区块 → Energy Storage 卡片图片
- 现状：alt = `Data Center Liquid Cooling`
- 改为：`Energy Storage`

### 6. 加热器页全角冒号 → 已转 Codex（见 🟡-12）
- 2026-10-09 Muse 浏览器实测：全角冒号共 2 处（第 1 个 "800v 35kw" 卡、第 4 个 "400v 24kw" 卡的图像框小部件"描述"文本框）；程序化 fill 无法持久化（Elementor React 受控组件限制），需人工手动修改

## 🟡 Codex 工单（结构级，他做完 Muse 验收）

### 7. 加热器页 20 张产品卡 H3 去重＋8 个空 H3 补标题（P0）
- 现状："800v 35kw"×8、"600v 30kw"×4、"400v 24kw"×8，另 8 个空 H3
- 要求：每卡唯一 H3（含型号区分，如 Q-3 / A3 系列＋功率电压）

### 8. 页脚空 H2 模板修复（全站）
- 现状：三页页脚 "Call Us" 为空 H2（文本在 H2 之后）
- 要求：修模板一处，全站生效

### 9. 面包屑导航（三页）
- 要求：Home > Products > 分类名

### 10. 中文图片文件名改英文
- 如：三合一控制器1.webp → three-in-one-controller-1.webp
- 要求：重传＋更新引用＋旧文件重定向或删除（需 Peter 批准删除）

### 11. 重复链接确认
- 现状：加热器页前 8 张卡全链 Q-3 页面，13–20 张全链 a3-series
- 需 Peter 确认：是否刻意（如是，H3 标题需体现差异；如否，修正链接）

### 12. 全角冒号手动修复（Muse 浏览器无法完成，转 Codex）
- 位置：加热器页 Elementor 编辑 → 2 处"图像框"小部件的"描述"文本框（第 1 个 "800v 35kw" 卡下方、第 4 个 "400v 24kw" 卡下方）
- 操作：人工用真实键盘/鼠标将 `Rated Voltage：Customizable` 的全角冒号改为半角 `Rated Voltage: Customizable`，点"更新"，清 LiteSpeed 缓存后前端验证
- 原因：程序化 fill 后点更新会导致编辑器 UI 崩溃、修改不持久化（2026-10-09 实测）
