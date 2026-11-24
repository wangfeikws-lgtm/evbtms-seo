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
