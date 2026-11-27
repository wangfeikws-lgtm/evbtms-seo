# Google 产品摘要报错修复 · 2026-11-27

WPCode 片段 10644 原先在 21 个询价型产品网址注入 Product JSON-LD，缺 offers、review 和 aggregateRating。已停用该片段并刷新页面缓存。片段代码仍保存在 WordPress，原始清单见 product-schema-snippet-2026-11-24.php。

逐一访问原片段的 21 个正式网址。21/21 均 HTTP 200，保留 canonical 标签，网页源代码均已无 Product JSON-LD。此检查覆盖原片段的范围。没有读取 GSC 受影响网址完整清单。

Google 产品摘要报告的验证由 Peter 提交，Google 重抓和验证结果待定。请在 GSC 产品摘要中打开本错误后点击验证修复。
