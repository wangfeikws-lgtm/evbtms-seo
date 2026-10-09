# SERP 简报：制动电阻分类页（R1 执行版）

> 本简报是 `serp-braking-resistor-ev.md`（2026-10-08，11 组词调研）的执行补充：
> 前者回答"哪些词可打"，本篇回答"分类页怎么做"。
> 调研日期：2026-10-09 ｜ 对应 KEYWORDS.md R1 ｜ TASKS.md T8

## 0. 结论先行

- **GO，建分类页**。主词 `braking resistor EV` 可打（见前简报 §10：真实厂商竞争仅 Cressall 与 REO）。
- 建议 URL：`/products/braking-resistor/`（与前简报一致）
- 定位：**EV-only**，不碰工业 VFD/电梯/起重机（前简报已定战略）

## 1. 对标：头部厂商分类页在讲什么

**Cressall（cressall.com，EV2 系列）**——最直接的对标：
- 卖点结构：应用场景先行（BEV / FCEV / 矿用电动车辆）→ 系统原理图（Brake Chopper + Resistor Bank 在整车电气架构中的位置）→ 模块化（最多 5 模块组合，125kW，可并联/串联扩展）→ 水冷（体积仅为风冷 10%、重量 15%）
- 内容形式：产品手册 PDF + 应用文章（如 electric-mines 矿用场景文）+ 系统框图
- 差异化：水冷、模块化、"多余热量可复用（预热电池/座舱）"

**REO**——前简报已覆盖，传统制动电阻厂商，EV 页面相对薄。

### 内容缺口（我方可打）
1. Cressall 强在欧美重载/矿用场景，**对"电动大巴/电动卡车/工程机械"的中文供应链视角只字未提**
2. 无人讲**选型方法**（阻值/功率怎么算）——分类页挂 FAQ + 博客 B2（sizing）承接
3. 无人讲 **brake chopper 与电阻的搭配关系**——博客 B1（brake chopper resistor EV 内容真空）承接
4. 系统集成视角：制动电阻 + PTC + BTMS 的热管理整体方案（站内独有，无人有）

## 2. 分类页结构建议（H2 级）

1. What Is a Braking Resistor in an EV?（50–80 词定义段，抢 AI Overview 引用位）
2. How It Works: Brake Chopper + Resistor Bank（系统框图，文字版）
3. Key Specifications（规格表——⚠️ 等 Peter 真实规格，**不得编造**）
4. Applications: Electric Bus / Truck / Mining & Construction Machinery（场景化，每个 60–100 词）
5. Water-Cooled vs Air-Cooled（Cressall 已教育市场，直接对标）
6. FAQ（4–6 个，来自 PAA + 前简报）
7. CTA：厂家选型咨询（询盘导向）

## 3. 内链规划
- 分类页 → 博客 B1（Brake Chopper 原理）、B2（Sizing 选型）
- 博客 B1/B2 → 反链回分类页
- 首页/Products 总页 → 分类页

## 4. Go / No-Go
- **决策：GO（有条件）**
- 条件：① Peter 确认 EV-only 定位；② 真实规格到位（阻值、持续/峰值功率、电压、冷却、防护、温度、振动冲击、认证、MOQ/交期）；③ 三合一是否含 brake chopper（影响"系统搭配"写法）
- 规格未到之前：**页面框架可搭，参数区留空占位，不得填编造数字**

## 5. 待 Peter 决定的事
1. EV-only 定位是否接受
2. 真实规格清单（同上）
3. 有无可公开的 OEM/装车案例（有则分类页可信度翻倍）
