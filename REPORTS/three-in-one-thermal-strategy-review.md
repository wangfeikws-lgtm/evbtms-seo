# 三合一（热管理）完整复盘：产品定位 × 关键词 × 独立站诊断 × 行动计划

> 复盘日期：2026-10-09｜信息来源：Peter 转工厂 Q&A ＋ 网站现页面核验 ＋ TH1–TH4 英文 SERP 实测
> 产品档案：`REPORTS/product-brief-three-in-one-thermal-controller.md`

---

## 一、产品复盘：到底是什么

**一句话**：新能源商用车热管理域控制器——把**电动压缩机控制器、制冷系统 ECU、高压 PTC 控制器**三合一，对压缩机、膨胀阀、风机、PTC 做集中控制。

| 维度 | 内容 |
|------|------|
| 集成对象 | DCAC 压缩机控制器 / 制冷系统 ECU / 高压 PTC 控制器 |
| 电压平台 | 600V / 800V（输入 250–750V / 600–1000V DC，可定制） |
| 防护/通信/温度 | IP67 / CAN 2.0（可定制）/ -40~+60℃（网站写+65℃，待统一） |
| 散热 | 自然风冷，开放鳍片＋SiC 器件，安装点风速 ≥3.5 m/s |
| 重量/安装 | 6 kg，垂直安装；集成预充电阻 |
| 控制逻辑 | 压缩机按水温调速 / 膨胀阀按过热度调开度 / 风机按冷凝压力启停（~13 bar） |
| 定制能力 | 压缩机适配、电压平台、CAN 协议/ID/波特率、风机曲线均可按项目调 |

**核心卖点排序**（按买家关心度）：
1. 结构性降本：3 个控制器变 1 个，少线束、少接口
2. 可靠性：故障点减少
3. EMC：一体化设计电磁兼容更好
4. 定制灵活：Tier1 给不了的按项目定制（CAN、压缩机适配、电压平台）

**竞争格局**：Valeo / Hanon / Highly Marelli（刚发布集成压缩机＋高压加热器＋电控的热管理系统）、Grayson（电动大巴 CTMS 完整热管理系统）。EVLINK 的错位优势：**只做控制器**（不碰整套热管理系统），给已有热管理方案的客户做"控制器集成升级"，定制灵活、价格更有竞争力。

---

## 二、英文命名定稿

- **产品主名**：`Three-in-One Controller`（工厂叫法，网站在用，准确，不用改）
- **SEO 主标题**：`Three-in-One Thermal Management Controller`（把品类说清楚，避免被理解成电机三合一）
- **完整落地页标题**：`Three-in-One Thermal Management Controller for Electric Bus`

---

## 三、TH1–TH4 SERP 实测结论（2026-10-09）

| # | 关键词 | 意图判定 | 结论 |
|---|--------|----------|------|
| TH1 | three in one thermal management controller | ❌ 意图混乱 | 搜出来是 Webasto "Heated Chiller"（三合一换热板，另一个东西）、电机电控三合一专利——没人指 EVLINK 这种产品。**不打** |
| TH2 | integrated thermal management controller electric bus | ⚠️ 信息型 | 全是 Grayson CTMS 整套系统、行业新闻，没有卖控制器的产品页。**转博客，不建落地页** |
| TH3 | EV thermal management controller | ⚠️ 技术信息型 | GitHub 仿真、学术论文、行业新闻。**转博客** |
| TH4 | electric compressor controller EV | ❌ 意图跑偏 | 搜出来是工业空压机控制器（DATAKOM，230/400V 市电）和 48V 改装件——完全不是 EV 热管理。**不打** |

### 核心判断（重要）

**英文自然搜索里，没有现成的"三合一热管理控制器"品类词。** 这是一个 category-creation 的现实：
- 买家不会搜一个不存在的品类名
- 最接近的已有概念是 Grayson 的 "Complete Thermal Management System"（整套系统）和 Webasto 的 "Heated Chiller"（换热部件），都不是控制器
- 因此 SEO 策略不能是"抢品类词"，而是：**守住品牌词 ＋ 打问题词/场景词 ＋ 靠阿里、社媒、展会带品牌搜索**

### 可打的关键词体系（修正版）

| 类型 | 关键词 | 打法 |
|------|--------|------|
| 品牌防守 | three-in-one controller EVLINK | 现有分类页已覆盖，保持 |
| 场景问题词（博客） | how to reduce thermal management system cost in electric buses | 博客：算账（3 控制器变 1 个省多少） |
| 场景问题词（博客） | integrated vs discrete thermal controllers EV | 博客：集成 vs 独立方案对比 |
| 场景问题词（博客） | electric bus thermal management control strategy | 博客：压缩机/膨胀阀/风机控制逻辑（工厂刚给的干货） |
| 长尾产品词 | thermal management controller 600V 800V electric bus | 现有分类页覆盖 |
| 采购词 | 走阿里类目（thermal management controller / compressor controller） | 阿里产品页 |

---

## 四、独立站现有页面诊断：对不对？要不要改？

页面：`/products/three-in-one-controller/`

### 做对的地方 ✅
1. 产品类型正确：写的就是热管理三合一（压缩机＋ECU＋PTC），跟工厂一致
2. H1 好："Three-in-One EV Thermal Management Controller"，品类说清楚了
3. 规格真实：600/800V、IP67、CAN 2.0、6kg、自然风冷要求都写了
4. 诚实：输出功率、尺寸、CAN 报文等标注"按项目确认"，不虚构——这是对的

### 要改的地方 🔧
1. **Title 太泛**：现在是 "Three-in-One Controller for EV Systems | EVLINK" → 建议改为 **"Three-in-One Thermal Management Controller for Electric Bus | EVLINK"**（把 thermal management 和 electric bus 两个词吃进去）
2. **缺工厂刚给的控制逻辑**：压缩机按水温调速、膨胀阀按过热度、风机按 13 bar 启停——这是工程师最想看的内容，页面上没有，要加上
3. **缺降本叙事**："3 变 1 省多少"没有算账，这是打动采购的核心，要加一个对比模块（传统方案：3 控制器＋3 套线束 vs 三合一：1 控制器）
4. **缺应用场景**：电动大巴 BTMS 液冷机组是主场景，页面要明确写
5. **温度小出入**：工厂说 +60℃，页面写 +65℃，统一口径（以工程文件为准）
6. **CTA**：询盘按钮是否醒目、是否有"按项目定制"入口（T7 审计会细查）

以上 1–4 属内容优化（低风险），由 Codex 按 T7 报告执行；改 Title 走正常流程（Title 修改需 Peter 知晓，不算高风险但要留记录）。

---

## 五、行动计划

| # | 动作 | 负责人 | 状态 |
|---|------|--------|------|
| 1 | 现有分类页内容补强（控制逻辑＋降本叙事＋应用场景＋Title 优化） | Codex（T7 报告含此页） | 待 T7 报告 |
| 2 | 博客 1：《How Integrated Thermal Controllers Cut EV Bus Thermal System Cost》 | Muse（SERP→大纲→Peter 批→正文） | 待启动 |
| 3 | 博客 2：《Compressor / Expansion Valve / Fan Control Strategy in EV Thermal Management》 | Muse（工厂干货直接可用） | 待启动 |
| 4 | 阿里产品页：按"三合一热管理控制器"上架（标题＋详情逻辑） | Muse 起草 | 待 Peter 确认是否上阿里 |
| 5 | 社媒：一稿多发（工厂照片＋降本故事 → FB/IG/LinkedIn/YouTube 脚本） | Muse 起草 | 待启动 |
| 6 | 尚缺资料：压缩机驱动功率、认证、量产案例、MOQ/交期、温度口径统一 | Peter 问工厂 | 待补充 |

**一句话总结**：产品是好的（热管理三合一，差异化清晰），网站页面底子是对的（小修即可），英文 SEO 没有现成品类词可抢（打问题词＋守品牌词），真正的流量抓手是"降本故事＋控制逻辑干货"的内容。
