# T8 文章 #2 SERP 调研＋大纲（2026-10-15 晚备稿）

> 状态：Peter 2026-10-16 11:25（主聊）已批"t8文章你写 发布"→ 正文已写完（T8-article-02-resistance-calculation.md）＋ 2 张解释图已生成（T8-article-02-assets/，品牌色 PNG，数值已验算）→ 待发布＋验收＋管线总表回填。
> 铁律：SERP 先行（Peter 2026-10-08）——本文件即 #2 的 SERP 记录。

## 1. SERP 调研（2026-10-15 18:15 实查）

查询：`braking resistor resistance calculation U2/P formula sizing`、`dynamic braking resistor calculation formula DC bus voltage chopper`

**前排结果（全部工业 VFD 内容，无一家 EV 厂家）：**
1. Scribd《Sizing Dynamic Braking Resistors》PDF —— 标准公式 R = Vb²/P（Vb = 制动管导通时的母线电压）；算例：480VAC 驱动 → 780VDC 导通电压，P=5595W（5HP×746×150%）→ R = 780²/5595 = 108.7Ω，取标准值 100Ω，再核对 ≥ 该机型 Rmin（58Ω）。
2. Schneider Electric FAQ（FA376712）—— 前排唯一的厂家内容，给出选型三准则：R ≥ Rmin（保护制动管不被电流烧毁）;R ≤ Rmax（否则吸不动峰值功率——无损坏风险，只是制动功率打折）;功率满足负载周期。公式 Rmax = Udc²/(1.2×驱动额定功率)，算例 ATV930D22N4：785²/(1.2×22000) = 23Ω，Rmin = 15Ω。
3. Scribd《BrakeResCalc》（Stevens Drives 技术 note tnBrakeCalc）—— R = (Turn-on level)²/PKW，PKW = kW×制动转矩倍数×0.8 效率；强调算出的 R 不得低于最小阻值，否则损坏制动回路。
4. vectree.io 技术文章 —— 斩波器是 IGBT 开关＋PWM，duty cycle 决定电阻承受的平均功率。
5. mikeholt 论坛帖、weijiguanli.com 旧 PDF —— 问答/培训资料，非厂家。

**结论（与 #1 一致，EV 空白确认）：** U²/P 的计算内容前排被 VFD 世界垄断，EV 场景的电阻计算内容缺位。信息增益点：
- 现有内容讲的"U"是 VFD 固定导通电压表（390/780/930/1120VDC）；EV 的"U"是牵引电池包电压窗口，导通阈值设在满电浮充电压之上、按项目定——这一点没有任何现有内容讲。
- 用 HVH-R1402 真实参数（2.24Ω、450–850V、140kW/20min）做 EV 算例，是竞品内容没有的东西。

## 2. 大纲：Braking Resistor Resistance Calculation: The U²/P Method Explained

- **目标关键词**：`braking resistor resistance calculation` / `how to calculate braking resistor ohms`
- **Slug 建议**：`/braking-resistor-resistance-calculation/`
- **SEO title**：Braking Resistor Resistance Calculation: The U²/P Method | EVLINK
- **Meta description**：R = U²/P looks simple until you ask which U and which P. An EV-side walkthrough: what the turn-on voltage really is, the Rmin/Rmax window your chopper lives in, and a worked example on a 450–850 V bus.
- **H1**：Braking Resistor Resistance Calculation: The U²/P Method Explained
- **篇幅**：约 1000–1300 词
- **结构**：按 Peter 社媒内容标准（买家问题 → 明确观点 → 三个技术要点 → 解释图 → 项目输入清单 → 联系入口）＋ FAQ ＋ CTA

### 0. 开头（买家问题，100–150 词）
采购/电气工程师手里有母线电压和制动功率，要一个欧姆数去发 RFQ；网上搜到的公式全是 VFD 世界的（780V 导通、5HP 电机），跟他的 750V 电池包、100kW 制动功率对不上号。引出：公式没错，但 U 和 P 在 EV 世界里指的东西不一样。

### 1. 一句明确观点（50 词内）
R = U²/P gives you the ceiling, not the answer. 公式算出的是阻值上限（Rmax）；真正的答案是一个窗口：下限看斩波器开关能承受的电流，上限看你要的制动功率。

### 2. 三个技术要点

**要点一：U 到底是哪个电压——导通电压，不是标称电压（Verified：VFD 导通表来自公开资料；Unverified：我司斩波器具体导通阈值——正文不写具体数）**
- 公式里的 U 是斩波器导通瞬间母线上的电压，不是电池包标称电压。
- VFD 世界有固定对照表（240VAC→390VDC 导通、480VAC→780VDC……）；EV 没有固定表：导通阈值设在满电浮充电压之上，按项目定。
- 关键判断：U 取小了→算出的 R 偏小→电流超斩波器承受；U 取大了→R 偏大→制动功率不够。

**要点二：Rmin / Rmax 窗口——Schneider 的框架，EV 化（框架为公开行业实践；算例数字 Verified）**
- Rmax = U²/P_峰值：阻值超过它，制动管全导通也吸不动你要的峰值功率（不会烧件，只是制动打折）——对应 Schneider FAQ 的第二准则。
- Rmin 来自斩波器电流：I = U/R，阻值太小电流冲过开关器件承受——对应第一准则（不宣称我司 IGBT 具体限值，只讲原理）。
- EV 算例（只用冻结口径：HVH-R1402，2.24Ω ±10% 25℃冷态，450–850V DC，140kW 连续 20min）：
  - 850V 端：850²/140000 = 5.16Ω 恰好对应 140kW 瞬时；实际 2.24Ω → 850²/2.24 ≈ 323kW 瞬时能力 vs 140kW 连续额定——说明瞬时电气能力与连续热能力之间留了余量。
  - 450V 端：450²/2.24 ≈ 90kW 瞬时——说明阻值必须按整个电压窗口两端都验算，不能只按标称电压算一个数。
  - 回扣 #1 的 18 吨大巴算例（30km/h、7% 坡 ≈ 103kW）：850V 下 R = 850²/103000 ≈ 7.0Ω 恰好覆盖该工况。
- 电压是平方项：U 差 10%，同阻值下功率差 21%——这是"U 取哪个值"如此要紧的原因。

**要点三：P 该用哪个功率——峰值进公式，占空比管发热（桥接到 #3 连续 vs 峰值、#5 占空比）**
- 进 R = U²/P 的 P 是峰值瞬时功率，不是平均功率；平均功率/占空比决定的是电阻的热额定值（wattage rating），那是另一半选型。
- 三个常见错误：① 用标称包电压代替导通电压；② 用平均功率代替峰值功率；③ 忘了 ±10% 冷态公差，窗口算得太紧。

### 3. 解释图（配图位）
- 图 1：P–R 曲线（固定 U 下功率随阻值下降），标出 Rmin / Rmax 窗口。
- 图 2：电压标尺——标称包电压 → 满电浮充 → 斩波器导通阈值（示意，不标我司具体阈值）。

### 4. 项目输入清单（CTA 前置）
把这几项发给我们，工程师回来给你核对 R 窗口：
- 直流母线电压范围（最低/标称/满电）
- 制动功率：峰值 kW ＋ 持续 kW 和时长
- 斩波器：车上已有还是需要我们配
- 冷却回路情况

### 5. FAQ（4–5 问）
- Why is U squared — does a small voltage difference matter?（10% 电压差 → 21% 功率差）
- Can one resistor cover my whole 450–850 V range?（可以，但两端都要验算；其他电压可按项目重绕）
- What if my calculated R is below the chopper's minimum?（串联/重新核 P/换斩波器方案）
- Is R = U²/P the whole sizing story?（不是——热/占空比是另一半；链 #1 选型指南）

### 6. CTA（简短）
Send us your bus voltage window and braking power — peak and continuous. We'll check the resistance window and come back with a configuration.

### 内链规划
- → `https://evbtms.com/products/braking-resistor/`（产品页，主内链 ≥2 处）
- → `https://evbtms.com/how-to-size-braking-resistor-electric-bus-truck/`（#1 选型指南：开头回扣＋FAQ）
- → 联系页（CTA）
- 预告内链位：#3《Continuous vs. Peak Power》、#5《How Duty Cycle Determines Braking Resistor Size》发布后回链。

### 事实三级标注（写作时执行）
- Verified：HVH-R1402 参数（2.24Ω ±10%/25℃冷态、450–850V DC、140kW 连续 20min、IP6K9K、-40~+85℃）；#1 的 103kW 算例；Schneider FAQ 的 Rmin/Rmax 框架（公开资料）；VFD 导通电压表（公开资料）。
- Unverified（不进正文）：我司斩波器具体导通阈值、IGBT 电流限值——正文只讲原理不给数。
- 禁区重申：不写 150/250kW 目标值；不写 MOQ/交期（等技术给准数前写 project-based）；不宣称认证；不用方形端子盒旧图。
