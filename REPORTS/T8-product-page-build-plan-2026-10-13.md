# T8 制动电阻产品页建页施工单（2026-10-13）

> Peter 2026-10-13 批准建页。文案已定稿（`REPORTS/T8-category-page-copy-2026-10-13.md`，Muse 撰写并过红线），事实源为冻结内容包（`REPORTS/T8-promo-content-pack-2026-10-13.md`）。
> **Codex 只做技术搭建，不写、不改英文文案**（§6 的 manufacturer 段落由 Muse 在此单内写好，Codex 原样粘贴）。

## 1. 页面基本信息

- URL（新建）：`https://evbtms.com/products/braking-resistor/`
- H1：Liquid-Cooled Braking Resistors for Electric Commercial Vehicles
- SEO title：Liquid-Cooled Braking Resistor for Electric Buses & Trucks | EVLINK
- Meta description：EVLINK HVH-R1402 series liquid-cooled braking resistors dissipate the regenerative braking energy electric buses and trucks can't feed back to the battery. 140 kW continuous, 450–850 V DC, IP6K9K.
- 面包屑：Home / Products / Braking Resistor
- 页面结构：文案稿 §1–§9 共 9 节 ＋ 本单 §6 新增 1 个 manufacturer H2（共 10 节）

## 2. 关键词布局总表

| 关键词 | 类型 | 布局位置 |
|---|---|---|
| braking resistor for electric vehicles | 核心词 | URL slug（含 braking-resistor）；§1 首段前 100 词内精确出现 1 次；meta 语义覆盖 |
| liquid-cooled braking resistor | 支撑词/差异点 | SEO title、H1、§2 H2（Why liquid-cooled on EVs） |
| braking resistor manufacturer | B2B 语义（T3a-R4 裁决：不单独建页，语义做到本页） | §6 新增 H2 "Braking Resistor Manufacturer in China — OEM & Custom Supply" |
| HVH-R1402 | 产品型号词 | §3 规格表、图片 alt |
| braking resistor for electric bus / electric truck / mining truck | 长尾 | §6 Applications 列表（4 项各成行）＋ 后续内链锚文本 |
| dynamic braking resistor | 场景词 | FAQ（§8 Q4 相关表述）＋ 博客 B1 内链（发布后补） |
| how to size a braking resistor for EV | 选题词 | FAQ（§8 Q1）＋ 博客 B2 内链（发布后补；未发布前不加死链） |

布局纪律：核心词全页精确出现 2–3 次（§1、§6 新增段各 1 次），其余用变体（braking resistors / brake energy dissipation）；**禁止堆砌**。

## 3. Google 合规清单（Codex 逐项落实，打勾交付）

- [ ] 全页唯一 H1；H2/H3 层级唯一且有序
- [ ] Title ≤ 60 字符、meta 120–155 字符、站内唯一
- [ ] self-canonical；robots index, follow；加入 XML sitemap
- [ ] 移动端布局正常；图片 alt 唯一（含关键词变体，见 §7）；图片懒加载
- [ ] BreadcrumbList schema；面包屑可点击
- [ ] Product schema（name / description / brand=EVLINK；**不编造 price/availability，不加 offers**）＋ FAQPage schema（§8 八问原句）
- [ ] 内链：本页出链到 BTMS 分类页、PTC 加热器产品页、三合一控制器产品页（§5 热回收段落处）；产品导航有入口（首页 ≤3 次点击可达）
- [ ] 首段自然出现核心词，不生硬

## 4. GEO SEO 要点（AI 搜索可摘取性）

- §1 开头 40–90 词直接回答 "what is a braking resistor for EVs"（文案稿已有，保留不动）
- §3 规格表用原生 HTML `<table>`（AI 摘取偏好），不要做成图片
- §8 FAQ 采用问答原句，一问一段，配 FAQPage schema
- 关键数字独立成句：140 kW continuous / 450–850 V DC / IP6K9K / 2.24 Ω（已在文案中）
- E-E-A-T：25 项试验依据、真实规格书来源、公司名＋网址、概念图"非实物照片"标注
- 人味写作已由 Muse 把关（Peter 写作标准）；**Codex 不得润色、改写、扩写任何英文句子**

## 5. 技术实施清单（Codex）

1. 用现有产品页模板新建 `/products/braking-resistor/`（参考三合一产品页结构）
2. 按文案稿 §1–§9 搭建 ＋ 本单 §6 的 manufacturer H2（Codex 原样粘贴 §6 文案）
3. 图片位 3 处：主图、三形态示意、应用场景；全部标注 "Photo pending — product in production"；alt 见 §7
4. 注入 JSON-LD：Product ＋ FAQPage ＋ BreadcrumbList（三段可合并一处）
5. CTA 按钮链到询盘表单/联系页（§9 文案已定）
6. 加入产品导航与 sitemap；检查桌面＋手机渲染
7. 完成后转 REVIEW，附交付物：公开 URL、桌面/手机截图、schema 校验结果（rich results test 或等效）、合规清单打勾版

## 6. Manufacturer H2 文案（Muse 撰写，Codex 原样粘贴，不得改动）

**H2：** Braking Resistor Manufacturer in China — OEM & Custom Supply

**正文：**
EVLINK designs and builds braking resistors in-house for electric commercial vehicles. Resistance is wound to order — tell us your bus voltage and duty cycle, and we match the winding to your platform instead of asking you to fit a catalog part. Every unit ships with temperature sensing and an interlock loop, because a resistor without them is a liability, not a product. Project-based supply, from prototype validation to volume.

## 7. 图片 alt 清单

- 主图：`HVH-R1402 liquid-cooled braking resistor for electric buses and trucks — photo pending`
- 三形态示意：`Three braking resistor configurations: standalone unit, resistor with chopper controller, integrated chopper-brake unit`
- 应用场景：`Electric bus and mining truck applications for liquid-cooled braking resistors`

## 8. 验收标准（Muse 验收，Peter 再审）

1. HTTP 200、self-canonical、robots index
2. 单 H1；title/meta 与 §1 一致；面包屑在位
3. 10 节齐全，文案与定稿逐字一致（Codex 未改写；§6 为本单版本）
4. Product/FAQPage/BreadcrumbList schema 校验通过
5. 图片占位标注在位，alt 与 §7 一致
6. 3 条出链可达且锚文本自然；导航 ≤3 点击可达
7. 桌面＋手机渲染正常；无红线违规（认证/峰值/MOQ/船舶/后缀/流量数字）

> 建页完成后先由 Muse 验收（REVIEW→VERIFIED），再交 Peter 审核正式发布。发布前不得投 T6B 广告。
