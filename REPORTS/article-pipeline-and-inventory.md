# 文章生产–发布流水线（Muse × Codex）

> 确立日期：2026-10-09｜Peter 拍板｜仓库为唯一事实源，双方不得私下用其他渠道对"写了哪篇、发了哪篇"各说各话

## 一、分工（铁律）

| 环节 | 负责人 | 说明 |
|------|--------|------|
| SERP 调研 | Muse | 任何英文文章先做真实 SERP（Peter 铁律） |
| 大纲 | Muse | Peter 批准大纲后才写正文 |
| 英文正文 | Muse | 写完放入 REPORTS/，状态转 READY |
| 发布执行 | Codex | 从 REPORTS/ 取终稿发布到 WordPress |
| 验收 | Muse | 发布后核验，符合标准才 VERIFIED |

**Codex 不写文章正文、不改文章观点；Muse 不碰发布操作。**

## 二、文章库存清单（Codex 发布照此单）

| # | 文章 | 状态 | 位置 | 可否发布 |
|---|------|------|------|----------|
| T5 | PTC Coolant Heater vs Air Heater（~1500词） | ✅ 措辞已定（Peter 授权 Muse 按数据核验，2026-10-09 修订 2 处） | REPORTS/T5-ptc-coolant-vs-air-draft.md | ✅ 可发布 |
| T10 | 集成控制器如何给电动大巴热系统降本 | ✅ 正文 Peter 已批准（2026-10-09） | REPORTS/T10-integrated-controller-cost-draft.md | ✅ 可发布 |
| T11 | 电动车热管理控制策略：压缩机/膨胀阀/风机 | ✅ 正文 Peter 已批准（2026-10-09） | REPORTS/T11-thermal-control-strategy-draft.md | ✅ 可发布 |
| T8-1 | Brake Chopper Resistor in EVs: How It Works | 规划（缺真实规格，禁写） | — | ❌ |
| T8-2 | How to Size a Braking Resistor for Buses/Trucks | 规划（同上） | — | ❌ |

## 三、每日自动发布规则（Codex 自动化，2026-10-09 修正版）

- 每天北京时间 9:00 BTMS、14:00 HVCH 各一篇
- 选题重复就换题；**九阶段验收通过后直接发布，不再重复请 Peter 确认**
- 事实、图片授权、技术问题必须核查
- 并行冲突 → 排队等待，等待期间做不冲突的准备工作；**不许把"等待"当"任务结束"**
- "配置完成" ≠ "任务完成"；以实际发布为准

## 四、信息同步机制

1. 文章状态唯一以本文件"库存清单"为准，Muse 维护
2. Codex 发布后 1 小时内回填：发布时间、URL、截图/证据
3. 库存不足（可发布文章 < 3 篇）时，Codex 在 TASKS.md 标注，Muse 优先补写
