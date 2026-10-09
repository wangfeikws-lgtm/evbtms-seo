# EVPTC 191页未收录处理框架与公开核查记录

记录日期：2026-10-09（北京时间）。范围：老站 https://www.evptc.com/。

本记录汇总10月8日至9日上午已有工作；保存文件不代表完成191条逐URL检测。未修改生产站、删除、合并或重定向页面，未提交新的索引请求。

## 1. 历史数据

来源：用户提供的GSC网页索引截图，报告更新日期2026-09-21。已收录148，未收录191；不是10月9日当前状态。

|GSC原因|历史数量|处理方向|
|---|---:|---|
|已抓取—尚未编入索引|158|检查当前索引状态、业务价值、内容、重复、canonical与内链；不只重复提交|
|软404|10|检查有效内容、状态码与渲染；区分误判与内容缺失|
|未找到404|4|区分误删与真实下架，检查历史流量、链接及确实对应替代页|
|备用网页，有适当规范标记|12|规范目标正确时保留合理排除|
|Google选择的规范页与用户指定不同|1|对比内容及canonical、内链、sitemap的一致性|
|robots.txt屏蔽|3|区分有意排除与误屏蔽重要页|
|自动重定向|3|检查最终目标；合理跳转原页不强求收录|
|合计|191|待最新详情导出确认逐URL范围|

低价值重复是后续诊断标签，不额外增加数量，不根据相似标题直接认定重复或关键词蚕食。

## 2. 已验证事实与证据边界

已验证的是工具返回的公开文本、链接及其缓存标记，不是实时后台、Googlebot抓取或当前索引状态。

|对象|本轮可复核事实|限制|
|---|---|---|
|产品总目录|10月9日工具返回标为3天前抓取的文本，其中AS01名称为AS01 High Voltage Coolant Heater with 12V/24V Low-Voltage Supply，存在产品链接|非实时前台完整视觉检查；不能据此证明详情已被Google重新抓取|
|AS01详情|10月8日工具返回标为3周前的旧标题12V High Voltage Coolant Heater For Ev With Current Fuse|不同工具快照不证明生产页面不一致；不能回滚已修改内容|
|HVCH核心分类|10月9日工具可读取标为4周前的分类文本；已有公开导航/面包屑发现入口证据|当前HTTP头、canonical、noindex和GSC状态未知|
|robots、sitemap、原理文章|网页工具读取返回not accessible via this tool|不等于404、robots屏蔽或网站故障|

证据URL：

- 产品目录：https://www.evptc.com/products.html
- 核心分类：https://www.evptc.com/supplier-4098406-high-voltage-coolant-heater
- AS01：https://www.evptc.com/sale-36421023-12v-high-voltage-coolant-heater-for-ev-with-current-fuse.html
- 原理文章：https://www.evptc.com/news/how-does-a-high-voltage-coolant-heater-work-262644.html
- robots：https://www.evptc.com/robots.txt
- sitemap：https://www.evptc.com/sitemap.xml

## 3. 已修改重要页面队列

|页面|历史修改/请求证据|当前待核实|动作|
|---|---|---|---|
|HVCH原理文章|9月29日用户保存正文、SEO字段及标题层级；截图显示请求索引成功|修改后last crawl、索引版本、Googlecanonical|核查后续抓取，不盲目重复请求|
|AS01|9月30日用户确认优化完成；截图显示已请求索引|最终正文范围、修改后last crawl及规范页|保护既有修改，先核查|
|QA 40644851|已有参数冲突诊断，最终保存状态未确认|当前完整内容、实质修改日期、参数、GSC状态|不能列为已完成更新或确定待抓取|

QA URL：https://www.evptc.com/sale-40644851-24v-dc-automotive-ptc-water-heater-hvch-15-25kw.html

上述队列不意味着属于191个未收录URL。仅当实质修改日期晚于GSC索引版last crawl，才标为修改后待抓取候选；日期未知标待核实。实时测试不证明索引版已更新。

## 4. K系列重复候选

目录标题均涉及K Series、2–12kW、200–400V，用途接近。已提取3个实际链接；详情读取返回Cache miss，未核实正文/配置，未认定重复、未收录或404。

|编号|URL|
|---|---|
|36444685|https://www.evptc.com/sale-36444685-k-series-high-voltage-ptc-coolant-heater-200-400v-2-12kw-for-ev-battery-and-cabin-thermal-management.html|
|40735327|https://www.evptc.com/sale-40735327-k-series-high-voltage-ptc-water-heater-2-12kw-200-400v-for-electric-vehicle-thermal-management.html|
|40686519|https://www.evptc.com/sale-40686519-k-series-2-12kw-high-voltage-ptc-water-heater-200-400v-for-ev-thermal-management-systems.html|

下一步逐页对比型号配置、参数、正文、canonical、索引状态、历史查询/点击和链接，再决定保留、差异化或合并候选。

## 5. 未知项与阻塞

BLOCKED（仅逐URL分类与重新抓取资格判定）：缺少最新7个原因详情URL导出、重要URL索引版last crawl/Googlecanonical、后台实际修改URL及日期。没有这些无法准确完成191条、确认覆盖率或筛选更新后未抓取页。详情报告可能仅展示示例，须记录导出覆盖数量。

技术未知：未取得原始HTML与响应头，HTTP状态、canonical、noindex、robots规则、sitemap包含及lastmod均未确认。公开搜索/工具缓存不能替代GSC。

环境记录：此前本地读取、写入与浏览器控制曾因setup refresh错误失败；这是执行环境阻碍，不是网站故障。10月9日本轮本地命令已恢复，保存后需读回确认。

## 6. 逐URL字段与优先级

字段：URL、页面类型、型号、业务价值、GSC原因/报告日期、当前索引状态、HTTP、robots/noindex、用户canonical、Googlecanonical、sitemap、实质修改日期/来源、last crawl、历史点击/查询、发现入口、问题证据、处理动作、请求日期、复查结果。

- P0：重要页已证实的索引障碍。
- P1：重要页已实质修改且last crawl早于修改。
- P2：已抓取未收录页的内容、重复与内链问题。
- P3：规范页、跳转等合理排除，保留并记录。

## 7. 下一步与资料缺失影响

1. 获取最新GSC原因详情导出，优先158项；随后其他6类，并记录报告日期与覆盖数量。
2. 读取重要页面GSC索引版last crawl和canonical，补充后台修改记录。
3. 继续不依赖GSC的页面内容/发现入口与相似配置对比，但不把候选当作确定错误。
4. 完成资格核查后才提出逐页处理，不批量提交，不因旧缓存重复改已验证工作。

截至本记录：生产修改无；新增索引请求无，提交日期不适用。目标10月10日前核查重要页，是否可完成取决于必要资料和访问状态，不预先标为完成。
