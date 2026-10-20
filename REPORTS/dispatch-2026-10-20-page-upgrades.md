# 派工单 2026-10-20：T13 8 个老页面升级闪电战（BTMS/矿卡/HVCH/三合一/厂家页/测试/Applications）

下达：2026-10-20（Muse 代 Peter 下达；Peter 2026-10-20 14:37 主聊批准"明天（10-21）一天，8 个页面全改完"；此前 14:31 批准 8 页一个月计划，14:36 要求压缩到本月、14:37 再压缩到 10-21 一天干完）
优先级：P0。死线：Codex 2026-10-21 18:00（北京时间）前完成 7 页执行；Muse 验收；10-28 Muse 出 7 天数据报告。

## 执行链条

1. **Muse 今晚（10-20）**产出逐页文案包 `REPORTS/page-upgrade-copy-pack-2026-10-20.md`：每页的完整 Title / Meta description / H1 / 新增段落 / FAQ（3 条）/ 内链清单，一字稿。
2. **Codex 10-21** 按文案包逐页执行，改前先留存每页改前字段值+截图（基线）。
3. **Muse 验收**后转 VERIFIED；**10-28** Muse 出数据报告（排名/CTR 变化、回滚清单）。

## 8 页清单

| # | 页面 | URL | 基线（GSC） | 目标 | 改动规格 |
|---|------|-----|------------|------|----------|
| 1 | BTMS 分类页 | /products/battery-thermal-management-system/ | CTR 1.35%（30 天计划基线；10-15 快照该页 0/184/0%/66.9，口径不同，执行前以文案包复核） | CTR →2.5% | Title 加 (3-12kW)、Meta 重写、H1 改、首屏加厂家句、FAQ 加 3 条（已批，Codex 在做，收尾验收） |
| 2 | 矿卡（mining truck thermal management） | /applications/ 矿卡专区（无独立矿卡页，见 10-13 矿卡派工单） | 查询排名 12.7（10-15 快照：1/16/6.3%/14.6） | 进前 10 | 矿卡专区补 300 词（矿山工况+产品对位）、Title 加 Electric Mining Truck、加 FAQ |
| 3 | HVCH 产品页 | /products/high-voltage-coolant-heater/ | 排名 29.3、CTR 44%（10-15 快照：9/68/13.2%/38.5） | 排名进前 20 | Title 加 Manufacturer、补选型段落、3 篇老文章加内链 |
| 4 | 三合一产品页 | /products/three-in-one-controller/ | 排名 10.7 | 进前 10 | 加 FAQ Schema、补"vs 分立方案"对比段 |
| 5 | HVCH 厂家页 | /high-voltage-coolant-heater-manufacturers/ | 67 曝光（10-15 快照：1/56/1.8%/38.2） | CTR 翻倍 | Title/Meta 重写，加工厂实力段落 |
| 6 | BTMS 测试内容 | 待定（查询词 btms test 排名 9.4） | 排名 9.4 | 进前 10 | 新建测试流程页**或**在现有页补强（Muse 在文案包中定方案） |
| 7 | Applications 页 | /applications/ | 109 曝光、排名 43（10-15 快照：1/108/0.9%/40.0） | 排名进前 30 | 按应用场景重组内容，加内链 |
| 8 | 数据复盘 | — | — | — | Muse 10-28：8 页排名/CTR 变化、掉量回滚、月报 |

基线说明：GSC 会话 10-16 起连续失效（10-20 快照"未取到"），最后有效快照为 2026-10-15（覆盖至 10-12），见 `~/workspace/goals/evbtms-com-seo-traffic-growth/hidden_files/gsc-snapshots/2026-10-15.md`。上表括号内为该快照可核验值；主聊引用的更新数字（12.7/29.3/10.7/9.4/43/CTR 44%）口径不同——Codex 改前必须从 live 页抓取当前 Title/Meta/H1 作为改前基线存档，以文案包中的基线表为准绳。

## 红线（违反即返工）

- **Codex 不写英文文案**（沿用 T8 派工单红线）：一切英文以 Muse 文案包为准，一字不改。
- 不得改 URL / 301 / canonical / 插件主题；结构性动作一律需 Peter 批准。
- **`/applications/` 的 title 只动一次**：#2（矿卡区 Title 需求）与 #7（整页重组）合并执行；另有 10-13 遗留的"/applications/ title/description 已备好、待投递"方案（见 `REPORTS/dispatch-2026-10-13-mining-truck-internal-links.md` §46 引用）——Codex 执行前必须先找到并核对那份方案，同一字段不得两次改动；冲突时退回 Muse 裁定，不擅自取舍。
- 改前每页必须留存改前字段值+截图；7 天后（10-28）任一页 CTR 掉 0.5% 以上即回滚该页。
- 验收不通过：退回 READY，任务下写清问题和证据。

## 交付

- 2026-10-21 18:00 前：7 页全部改完 + 验收报告（URL、改前改后 Title/Meta/H1 对照、FAQ/内链 HTTP 200、移动端首屏）。
- 状态流：READY → DOING → REVIEW；Muse 独立抓 live 页验收后转 VERIFIED。
- 2026-10-28：Muse 数据报告（8 页排名/CTR 变化、回滚清单）。

## 状态

- [x] Peter 批准 8 页计划 + 10-21 一天干完（2026-10-20 14:37 主聊）
- [x] 派工单入仓（Muse 2026-10-20 15:15，TASKS.md T13 已建）
- [ ] Muse 逐页文案包 `REPORTS/page-upgrade-copy-pack-2026-10-20.md`（今晚）
- [ ] Codex 领取（转 DOING）
- [ ] 10-21 交付 REVIEW
- [ ] Muse 验收 → VERIFIED
- [ ] 10-28 数据报告
