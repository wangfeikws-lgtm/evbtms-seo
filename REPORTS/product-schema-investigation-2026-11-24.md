# Product schema 消失查因报告（2026-11-24）

## 结论一句话

11-13 逐页加的 21 页 Product schema 现在全没了，原因是**每页的 Rank Math Schema 被设成了 None（Off），覆盖了全局默认**。丢失发生在 **2026-11-23（周一）上午 09:56–09:57（北京时间）的一次批量操作**：17 页在 48 秒内被集中改过。谁动的手、具体点了什么，Rank Math 里没有任何记录，也没有设置备份可恢复。

## 查到的事实

1. **三页面板实测（浏览器 2026-11-24 13:00–13:05，只读）**：HVCH 产品页（ID 2950）、制动电阻页（ID 10016）、BTMS 产品页（ID 2946）的 Rank Math Schema 标签均只有提示文字＋“Schema Generator”按钮，无任何已配置 Schema。页面列表中三页均显示“Schema: Off”。
2. **全局设置完好**：Pages 默认 Schema Type 为 Article，Posts 为 Article/Blog Post；Schema 模块已启用；文章页仍正常输出 BlogPosting。Rank Math 本身在工作，丢的只是逐页数据。
3. **版本无异常**：Rank Math 1.0.280，1.0.282 更新待安装、尚未应用，没有最近已更新的证据。Status & Tools 无重置/导入记录，Settings Backup 显示“There is no backup.”。Code Snippets 列表为空，无主题代码片段存 Product JSON-LD。
4. **数据库错误背景**：Error Log 近 100 行反复出现 “Commands out of sync; you can't run this command”，日期包括 11 月 11、12、13 日（13 日 04:08:50 UTC）、16、17、23、24 日。仅作记录，未证明与 schema 丢失有关。
5. **修改时间铁证（wp-json，UTC；北京时间 +8）**：21 页中 17 页集中在 2026-11-23 01:56:32–01:57:20 UTC（北京时间 09:56–09:57）被改过：12kw、3kw、800v-ptc、5kw、制动电阻、electric-compressor、a1、a2、a4、a3、a6、a7、q-3、q-4、high-voltage、q-series-2、qseries。其余：three-in-one 11-23 09:08（+08）、HVCH 11-23 17:08（+08）、a5-series 11-24 10:43（+08，原因未查到，与我方当日工作无关）、BTMS 11-24 11:06（+08，系当日孤儿页入链编辑所致）、/products/ 列表页 10-15 未动（与它从无 Product schema 一致）。
6. **时间线对得上**：schema 11-13 加完并验证 live 输出；11-23 09:56 批量改动；11-24 普查 27 页 0 页有 Product。11-13 至 11-24 间唯一的大批量页面改动窗口就是 11-23 09:56。

## 未查清的

- 批量操作是谁做的、点了什么（批量“Set Schema: None”？还是别的批量保存误触？）。Rank Math 无操作日志，无法从界面确定。
- a5-series 11-24 10:43（+08）的单次改动原因。
- 更深的核查（页面修订记录里的元数据、数据库 postmeta）需要 Hostinger/数据库访问，云端这边做不了。

## 修复方案（待 Peter 定）

重加 21 页 Product schema，但**不带 offers 块**（只写产品名、描述、品牌 EVLINK）。理由：11-13 那批带了 offers（Availability In Stock）却无价格，正是 GSC 11-23 抓到的缺价报错根源；站上按项目报价、无公开价，编不出价格。重加后逐页验证 live 输出＋富媒体测试。

## 2026-11-24 13:46–14:08 代码片段方案已落地（21/21 核验通过）

Peter 点选“改用代码片段加 Product schema”后执行：

- **工具纠正**：站上**没有** Code Snippets 插件——此前查因报告写的“Code Snippets 为空”查错了对象，菜单里那个“Code Snippets”是 Blocksy/Angie 的片段工具（angie_snippet），它会误判产品名里的 System 一词为禁用函数、且部署要登录 Angie，无法运行此代码（误建的副本已移至回收站，列表恢复为空）。实际用的是本站**已安装但未启用的 WPCode Lite**（菜单也叫 Code Snippets，启用后建片段，未装任何新插件）。
- **片段**：WPCode → “EVLINK Product Schema (no offers)”（ID 10644，Active，Frontend Only，PHP，Priority 10），一个片段按页面 ID 输出 21 页 Product JSON-LD（name＋description＋brand EVLINK＋url，无 offers／价格／SKU／评分）。产品名、描述取自各页标题与 meta 描述。代码原文见 REPORTS/product-schema-snippet-2026-11-24.php（与上线代码一致）。
- **核验（我 curl 全量复核，2026-11-24 14:0x）**：21 页每页恰好 1 个 Product、无 offers、名字与页对应，全部 200；首页无 Product。浏览器另用富媒体测试抽查 3 页（HVCH／BTMS／制动电阻）＋首页，结果一致。
- **Google 的一点说明**：富媒体测试给每页标 1 个严重问题“应指定 offers、review 或 aggregateRating”——即没有价格／评价／评分，Product 拿不到富媒体展示资格。这是无价格设计的固有代价，不是缺价报错（块里完全没有 offers，也就没有 offers 缺价的问题）。结构化数据本身在位，Ahrefs 的“21 页缺 Product schema”项已闭合；富媒体卡片要等有公开价或评价才可能出。

Peter 13:21 点选“不带 offers 重加 21 页”后实测第 1 页（HVCH，ID 2950）：按要求填产品名／描述／品牌，SKU／价格／货币／评分留空、未主动设可用性；但 Rank Math Product 表单的 Availability 下拉默认即“In Stock”，选项只有 In Stock / Sold Out / Preorder，无空白项，无法清空。保存后富媒体测试验证：Product 正确生成，但同时生成 offers 对象（type Offer、availability InStock、无 price、无 priceCurrency），Google 判 1 个严重问题“应指定 price 或 priceSpecification.price”。按任务停止条件，第 1 页已撤销（面板恢复为空、修订版仍为 497），其余 20 页未动。结论：**Rank Math 的 Product 表单无法输出不带 offers 的 Product schema**，逐页重加只会复制同一问题。

后续两条路（待 Peter 定）：
1. 改用代码片段加 Product schema：用 Code Snippets 插件（当前列表为空）或同类方式直接写 JSON-LD，不走 Rank Math 表单，可做到无 offers。但这是往生产页加自定义代码，需他批准。
2. 先不动：产品页无 Product schema，GSC 的 HVCH 缺价报错是旧抓取数据、下次抓取自消；产品页排名未因此受损（制动电阻页仍是全站点击第 1 页）。
