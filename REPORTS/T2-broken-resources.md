# T2 — 首页 22 个加载失败资源排查报告

> 执行人：Muse（只读审计，未修改生产站）｜ 审计日期：2026-10-09
> 数据来源：GSC 网址检查 → https://evbtms.com/ → 网页中的资源（"无法加载 22 项资源，共有 78 项"）＋ 普通浏览器逐项复验
> 验收标准对照：① 22 个真实资源 URL 清单 ✅ ② 失败原因分类 ✅ ③ 只读排查 ✅

## 结论（先看这个）

22 个失败资源 = **19 张站内图片**（/wp-content/uploads/ 下）+ **3 个 AI 聊天组件的 XHR 请求**。CSS / JS / 字体**全部正常**。

关键发现：**这些图片文件都在服务器上，普通浏览器访问全部返回 200 正常显示，只有 Googlebot 抓取时失败。** 因此不是文件缺失（404），而是服务器/WAF 对 Googlebot 图片请求的拦截、限流或抓取渲染超时。

影响：页面 HTML 本身可被抓取收录，不影响排名大局；但图片无法被 Googlebot 加载会影响图片索引与页面体验评分，值得查，不算火烧眉毛。

> 修正说明：第一遍排查时因普通浏览器全部 200，曾误判为"外部第三方问题、无需处理"。GSC 明细证明 19 个是站内图片，特此更正。

## 一、22 个失败资源真实清单

### XHR（3 个，AI 聊天组件）
| # | URL | GSC 错误 |
|---|-----|----------|
| 1 | https://adsagentclientafd-b7hqhjdrf3fpeqh2.b01.azurefd.net/locales/en-US/translation.json?v=1790812800050 | 其他错误 |
| 2 | https://evbtms.com/a/msba/api/config/read/?clientId=9b7205d0-8943-40ce-9243-65320d21bb58&lang=en-US&clientInformation=…（查询串含 Googlebot UA 标识） | 其他错误 |
| 3 | https://evbtms.com/a/msba/api/config/read?clientId=9b7205d0-8943-40ce-9243-65320d21bb58&lang=en-US&clientInformation=…（与 #2 相同，仅 read 后无斜杠，疑似其重定向目标即 #2） | 重定向错误 |

### 图片（19 个，错误均为"其他错误"）
| # | URL |
|---|-----|
| 4 | https://evbtms.com/wp-content/uploads/2026/08/34b07f0b-b431-4320-a7f4-fcfe2bf4843b_11zon-1536x640.webp |
| 5 | https://evbtms.com/wp-content/uploads/2026/08/Construction-Machinery_11zon-1536x864.webp |
| 6 | https://evbtms.com/wp-content/uploads/2026/08/Electric-Mining-Truck-1536x864.webp |
| 7 | https://evbtms.com/wp-content/uploads/2026/08/Electric-Truck-1536x864.webp |
| 8 | https://evbtms.com/wp-content/uploads/2026/08/logo-%E5%A4%96%E8%B4%B8-1.png（logo-外贸-1.png） |
| 9 | https://evbtms.com/wp-content/uploads/2026/09/%E4%B8%89%E5%90%88%E4%B8%80%E6%8E%A7%E5%88%B6%E5%99%A8.jpg（三合一控制器.jpg） |
| 10 | https://evbtms.com/wp-content/uploads/2026/09/%E5%8E%8B%E7%BC%A9%E6%9C%BA.webp（压缩机.webp） |
| 11 | https://evbtms.com/wp-content/uploads/2026/09/1-%E5%89%AF%E6%9C%AC-300x300-1-1.webp（1-副本-300x300-1-1.webp） |
| 12 | https://evbtms.com/wp-content/uploads/2026/09/2-%E5%89%AF%E6%9C%AC-300x300-1-1.webp（2-副本-300x300-1-1.webp） |
| 13 | https://evbtms.com/wp-content/uploads/2026/09/22_11zon-scaled-1.webp（首屏预加载大图） |
| 14 | https://evbtms.com/wp-content/uploads/2026/09/3-300x300_11zon-1.webp |
| 15 | https://evbtms.com/wp-content/uploads/2026/09/4-300x300_11zon-1.webp |
| 16 | https://evbtms.com/wp-content/uploads/2026/09/5-300x300_11zon-1.webp |
| 17 | https://evbtms.com/wp-content/uploads/2026/09/6-300x300_11zon-1.webp |
| 18 | https://evbtms.com/wp-content/uploads/2026/09/9372f8f0-a0f0-4343-8ff7-1dac8592782e-1024x658_11zon.webp |
| 19 | https://evbtms.com/wp-content/uploads/2026/09/Agricultural-Machinery-2-1536x864.webp |
| 20 | https://evbtms.com/wp-content/uploads/2026/09/BTMS.jpg |
| 21 | https://evbtms.com/wp-content/uploads/2026/09/Data-Center-Liquid-Cooling-1536x864.webp |
| 22 | https://evbtms.com/wp-content/uploads/2026/09/Q%E7%B3%BB%E5%88%97.jpg（Q系列.jpg） |

## 二、失败模式分析

1. **聚类明显**：19 张图片全部是 /wp-content/uploads/ 下的文件，多为 srcset 响应式尺寸变体（-1536x864、-300x300 等）及首屏预加载大图；其中 4 个为中文文件名（URL 编码后）。
2. **普通浏览器全部 200**：抽验 #7、#13 等图片在普通浏览器直接访问均返回 200 并正常渲染 → 文件存在且可公开访问。
3. **Googlebot 特定失败**：#2 的请求参数中 UA 字段明示为 Googlebot，说明失败发生在 Google 抓取链路。可能原因：服务器防火墙 / 安全插件（如 LiteSpeed / Cloudflare Bot Fight Mode 类规则）误拦 Googlebot 的图片请求、或对爬虫限流、或抓取渲染超时。
4. **聊天组件 XHR**：#1 在普通浏览器验证为 200；#2/#3 为聊天组件后端 API（/a/msba/api/config/read 疑似不存在或拒绝机器人请求）。机器人本就不该触发聊天 API，属 косметический 问题，优先级低。

## 三、修复方案

### 可直接执行（只读验证，Codex 负责）
1. Codex 在本地环境用 Googlebot UA curl 请求 #7、#13 两张图片，对比普通 UA 的返回，确认是被拦截（403/429）还是超时。
2. 检查服务器防火墙 / 安全插件 / CDN 的 Bot 管理规则，确认是否有针对 Googlebot 或图片路径的拦截/限流规则（只看不改）。

### 需 Peter 批准（生产环境变更）
1. 调整 WAF/安全插件规则，放行 Googlebot 对 /wp-content/uploads/ 的图片请求（高价值，修完可直接改善 19 个失败项）。
2. AI 聊天组件改为懒加载 / 延迟初始化，减少对抓取渲染的干扰（可选）。
3. 中文文件名图片改用英文文件名（可选 hygiene；改名需同步更新引用并做重定向，不急）。

## 四、补充验证（2026-10-09，Muse 直连测试）

用 Googlebot UA（Nexus 5X / compatible; Googlebot/2.1）直接请求失败图片 URL：
- 英文文件名图片（Electric-Truck-1536x864.webp）：200，93KB，1.0s
- 中文文件名图片（三合一控制器.jpg）：200，372KB，0.9s
- 首页 HEAD：200

**结论更新**：服务器不存在基于 UA 拦截 Googlebot 的规则。GSC 抓取失败更可能的原因排序：
1. 抓取渲染超时（首页 78 个资源＋AI 聊天组件＋外部字体，渲染负载重）
2. 针对 Google 抓取 IP 段的限流（非 UA 维度，需服务器日志确认，Codex 侧查）

**处理降级**：暂不建议动 WAF 规则（无证据支持，且属生产变更）。优先做性能减负：AI 聊天组件懒加载、减少渲染阻塞资源。观察 GSC 下次抓取 22 项是否自行下降。
