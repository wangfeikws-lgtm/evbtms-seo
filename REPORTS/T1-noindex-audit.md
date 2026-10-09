# T1 — 22 个 noindex 页面排查报告

> 执行人：Muse（只读审计，未修改生产站）｜ 审计日期：2026-10-09
> 数据来源：GSC 网页索引编制报告（"被'noindex'标记排除了"=22，首次检测 2026/9/15）＋ WordPress 后台 Rank Math Titles & Meta 全程核查
> 验收标准对照：① 22 个真实 URL 清单 ✅ ② 每页判定及理由 ✅ ③ 只读审计 ✅

## 结论（先看这个）

**22 个 noindex 里：15 个是故意配置（正常），7 个曾是意外但已修复。目前生产站无需任何修改。**

建议的唯一动作：在 GSC 中对"被'noindex'标记排除了"点击「验证修正情况」，让 Google 重新抓取确认。这是一个只读请求动作，不改网站——但按只读约定，请 Peter 点一下（GSC → 网页索引编制 → 该原因 → 验证修正情况）。

---

## 一、故意 noindex（15 个，无需处理）

| # | URL | 类型 | 依据 |
|---|-----|------|------|
| 1 | https://evbtms.com/search/QUERY_STRING/ | 搜索页 | Rank Math 全局「Noindex Search Results」已开启 |
| 2 | https://evbtms.com/author/wangfeikws/ | 作者存档 | Rank Math「Authors Archives Robots Meta = No Index」 |
| 3 | https://evbtms.com/category/guide/ | 分类存档 | Rank Math「分类目录存档 = No Index」 |
| 4 | https://evbtms.com/?s={search_term_string} | 搜索参数 URL | 搜索参数，故意 |
| 5 | https://evbtms.com/news/page/2/ | 博客分页 | 存档分页，故意 |
| 6–15 | 10 个 Lorem Ipsum 占位文章（/malesuada-fames-acturpis-egestas/ 等） | 占位瘦内容 | 模板占位内容，noindex 合理 |

> 备注：第 6–15 项为建站模板遗留的 Lorem Ipsum 占位文章。noindex 处理正确；更彻底的做法是直接删除（删页面属生产修改，需 Peter 批准，本轮未执行）。

## 二、曾意外 noindex、现已修复（7 个）

均为 2026 年 8 月网站改版／产品页 URL 迁移（旧 URL → /products/ 新 URL＋重定向）期间意外产生，现已恢复正常：

| # | 旧 URL（GSC 抓取时 noindex） | 当前状态 |
|---|------------------------------|----------|
| 16 | https://evbtms.com/services/ | HTML robots 已为 index（已手动修复） |
| 17 | https://evbtms.com/12kw/ | 重定向 → /products/battery-thermal-management-system/12kw/（index） |
| 18 | https://evbtms.com/battery-thermal-management-system/ | 重定向 → /products/battery-thermal-management-system/ |
| 19 | https://evbtms.com/battery-thermal-management-system/3kw/ | 重定向 → /products/battery-thermal-management-system/3kw/ |
| 20 | https://evbtms.com/electric-bus-2/ | 重定向 → /electric-bus/ |
| 21 | https://evbtms.com/three-in-one-controller/ | 重定向 → /products/three-in-one-controller/ |
| 22 | https://evbtms.com/high-voltage-coolant-heater/ | 重定向 → /products/high-voltage-coolant-heater/ |

GSC 显示的仍是 8 月旧抓取状态，属报告滞后，点「验证修正情况」后会消退。

## 三、Rank Math 全局 noindex 规则核查（全部为故意配置）

- Global Meta：仅 Index，无全局 noindex；「Noindex Empty Category and Tag Archives」已勾选
- 文章／页面：默认（未设 noindex）；媒体附件：重定向到父内容
- 分类目录存档：No Index ✅｜标签存档：No Index ✅｜作者存档：No Index ✅
- Misc：日期存档已禁用；Noindex Search Results ✅；子页面／分页／密码保护页未设 noindex
- 单独页面级：全站仅 1 页单独 noindex——「Thanks」表单感谢页（合理）

## 四、附带发现（未处理，供后续）

1. Rank Math 提示有 1 篇已发布文章在回收站，并建议将 /blog/ 重定向（/blog/ → /news/ 的 301 早在 2026-09-21 已建好，属过期提醒，可忽略）。
2. /services/ 已修复为 index，但 GSC 仍显示 2026-08-04 旧状态——点验证后会更新。

## 五、修复方案（分两类）

- **可直接执行**：无（生产站当前配置正确，无需改动）。
- **需 Peter 批准**：
  1. GSC 点击「验证修正情况」（1 分钟，零风险）
  2. 删除 10 篇 Lorem Ipsum 占位文章（而非长期 noindex 挂着）——可选，不急
