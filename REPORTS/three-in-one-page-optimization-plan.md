# 三合一控制器产品页内容优化方案（Codex 执行版）

> 日期：2026-10-09｜事实基线：`REPORTS/product-brief-three-in-one-thermal-controller.md` v2（唯一事实源）
> 范围：仅页面文案内容优化。不含：Title/meta（已改完）、图片 alt、中文文件名、页脚空 H2、面包屑（另行处理）。
> 所有英文文案为可直接粘贴的终稿（Codex 直接用，无需再加工）。

---

## 一、逐节处置表

| # | 当前区块（H2） | 处置 | 说明 |
|---|---|---|---|
| 0 | 页首简介（H1 下约 90 词） | REWRITE | 融入官方集成定义＋新增功率/温度口径，见 §2.1 |
| 1 | Integrated Thermal Management Control | REWRITE | 按官方规格表精确定义三合一构成＋功率，见 §2.2 |
| 2 | Product Views | KEEP | 图片区不动 |
| 3 | **NEW** Three Control Loops, One Controller | ADD | 新增：三个控制环，见 §3.1（放 Product Views 之后） |
| 4 | **NEW** From Three Boxes to One: What Integration Removes | ADD | 新增：降本对比模块，见 §3.2（放控制环之后） |
| 5 | How the Three-in-One Controller Fits the Vehicle | KEEP | 整车适配说明保留 |
| 6 | Parameter Specifications | REWRITE | 全量英文规格表，见 §4（替换现有表格） |
| 7 | Natural Air Cooling Requires a Defined Vehicle Air Path | KEEP | 自然风冷说明保留（已含 ≥3.5 m/s 要求） |
| 8 | Integrated for Commercial-Vehicle BTMS Liquid-Chiller Systems | REWRITE | 扩写应用场景，见 §2.3 |
| 9 | Four Interfaces Must Be Confirmed Before Release | KEEP | 发布前确认项保留 |
| 10 | Built Around Commercial and Off-Highway EV Integration | KEEP | 商用车/非公路定位保留 |
| 11 | Information Required for Controller Selection | KEEP | 选型信息（压缩机参数对接）保留 |
| 12 | From Vehicle Requirement to Released Controller Configuration | KEEP | 项目流程保留 |
| 13 | Project-Specific Items That Still Require Confirmation | KEEP | 项目确认项保留 |
| 14 | Three-in-One Controller FAQ | ADD 3 条 | 新增 Q&A，见 §3.4（保留现有 FAQ） |
| 15 | Complete the Thermal Management Architecture | KEEP | 页中交叉 CTA 保留 |
| 16 | Define the Right Three-in-One Controller Configuration | REWRITE | 强化 OEM 定制 CTA，见 §3.5 |

**建议页面顺序**：0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15 → 16

---

## 二、REWRITE 区块终稿文案

### 2.1 页首简介（替换 H1 下现有约 90 词）

> EVLINK's Three-in-One Thermal Management Controller integrates three control units into a single housing: a DCAC electric compressor controller, a refrigeration system ECU, and a high-voltage PTC controller. Built for 600V and 800V electric commercial vehicle platforms, it centralizes control of the compressor, expansion valve, cooling fan, and PTC heating — replacing three separate controllers with one IP67-rated unit.

### 2.2 "Integrated Thermal Management Control"（替换现有正文）

**H2 保持不变。** 正文替换为：

> Conventional EV thermal architectures run three separate controllers: one for the electric compressor, one for the refrigeration system, and one for high-voltage PTC heating. Each needs its own housing, wiring, low-voltage supply, and CAN node.
>
> The EVLINK three-in-one controller combines all three into a single unit:
>
> - **DCAC compressor controller** — 5–10 kW, adjustable to the application
> - **Refrigeration system ECU** — coordinates the refrigeration circuit
> - **High-voltage PTC controller** — 8 kW heating plus 24 kW battery heating, two channels
>
> One housing. One 24V supply. One set of CAN interfaces. Fewer parts, fewer interfaces, fewer failure points.

### 2.3 "Integrated for Commercial-Vehicle BTMS Liquid-Chiller Systems"（扩写应用场景）

**H2 保持不变。** 正文替换为：

> The controller is built around commercial-vehicle BTMS liquid-chiller systems. It coordinates battery cooling and heating loops, cabin climate, and power electronics thermal management from one unit — on 600V and 800V platforms.
>
> It suits city buses, coaches, trucks, and off-highway electric machinery. The voltage platform, compressor matching, CAN protocol, and fan control curves are configured per vehicle project, so the same controller architecture adapts across commercial vehicle types.

---

## 三、ADD 新增区块终稿文案

### 3.1 新增 H2：Three Control Loops, One Controller

> Thermal management is won or lost in the control strategy. The three-in-one controller runs three coordinated control loops:
>
> **Loop 1 — Compressor speed follows water temperature.** Compressor speed tracks the system water temperature against the target temperature: as water temperature rises, speed increases; as it falls, speed decreases. Continuous speed regulation avoids the energy waste and mechanical stress of frequent start-stop cycling.
>
> **Loop 2 — Expansion valve follows superheat.** The electronic expansion valve opening follows superheat at the evaporator outlet: higher superheat opens the valve further, lower superheat closes it. Holding superheat around 5 K is common industry practice, calibrated per project. Too little superheat risks liquid refrigerant reaching the compressor; too much wastes evaporator capacity.
>
> **Loop 3 — Fan follows condenser pressure.** The condenser fan is controlled against condenser high-side pressure. As an example, the fan may start when pressure reaches about 13 bar; start/stop pressure points and the speed curve are calibrated to the vehicle project.
>
> Because the three loops interact — a change in compressor speed shifts superheat, which shifts condenser pressure — running them in one controller means shared sensor data and no CAN latency between loops. The CAN protocol, CAN IDs, baud rate, and control logic can all be customized per project.
>
> *How the three loops work together in detail: [EV Thermal Management Control Strategy: How Compressor, Expansion Valve and Fan Work Together](/blog/ev-thermal-control-strategy/).*

### 3.2 新增 H2：From Three Boxes to One: What Integration Removes

> Every standalone controller brings a housing, a PCB, connectors, a low-voltage feed, a CAN node, and a round of validation. Multiplied by three, the overhead dominates. The three-in-one controller removes it:
>
> | | Three separate controllers | Three-in-one controller |
> |---|---|---|
> | Housings | 3 sealed housings | 1 housing, rated ≥ IP67, sealed once |
> | Low-voltage supply | 3 × 24V feeds | 1 × 24V feed (16–32V DC) |
> | CAN nodes | 3 nodes to integrate and calibrate | 1 node set |
> | Wiring | HV + LV + CAN harnesses × 3 | Single harness set |
> | Cooling design | 3 thermal designs | Shared open-fin natural cooling |
> | Spares & diagnostics | 3 part numbers, 3 diagnostic interfaces | 1 of each |
>
> Fewer interfaces also means fewer failure points, and a single EMC validation instead of three — reliability gains that compound over the vehicle's service life.
>
> *The full cost logic: [How an Integrated Thermal Management Controller Cuts Electric Bus System Cost](/blog/integrated-thermal-controller-cost/).*

### 3.3 新增应用入口（并入 §2.3，已含，此处不另起 H2）

（无。应用场景已在 §2.3 覆盖：electric bus / commercial vehicle BTMS liquid-chiller systems / off-highway。）

### 3.4 FAQ 新增 3 条（追加到现有 FAQ 末尾）

**Q: Can the controller work with our own compressor?**
A: Yes. The controller can be adapted to customer-specified compressors. Provide the compressor's technical parameters and motor parameters, and we will configure the control accordingly.

**Q: Can the CAN protocol be customized?**
A: Yes. The CAN protocol, CAN IDs, baud rate, and control logic can all be customized per project.

**Q: What are the MOQ and lead time?**
A: MOQ is 10 or 50 units. Standard lead time is 15 days.

### 3.5 最终 CTA 改写（H2 "Define the Right Three-in-One Controller Configuration" 保留，替换正文）

> Every vehicle project has a different voltage platform, compressor choice, and thermal target. Share your vehicle type, platform voltage, compressor parameters, and operating climate — we will define a controller configuration with honest trade-offs, including telling you when integration is not the right answer for your project.
>
> **[Start Your Project →]**（按钮链向现有询盘表单，Codex 确认链接目标）

---

## 四、Parameter Specifications 全量英文规格表（替换现有表格）

| Specification | Value |
|---|---|
| Integration configuration | DCAC compressor controller + refrigeration system ECU + high-voltage PTC controller in one unit |
| Rated DC voltage | 600V DC / 800V DC |
| Controller input voltage range | 250–750V DC / 600–1000V DC |
| Battery nominal voltage | 600V DC / 800V DC |
| Battery operating voltage range | 400–750V DC / 600–1000V DC |
| Control box protection rating | ≥ IP67 |
| Cooling method | Natural cooling (open-fin design; air velocity ≥ 3.5 m/s at mounting point) |
| Communication protocol | CAN 2.0 (protocol, CAN ID, baud rate, and control logic customizable per project) |
| Low-voltage control power supply | 24V DC (16–32V DC) |
| Pre-charge circuit | Integrated pre-charge resistor circuit |
| Operating ambient temperature | -40℃ to +65℃ |
| Mounting orientation | Vertical mounting (layout designed for easy installation and maintenance) |
| Weight | 6 kg (±10%) |
| Dimensions | Approx. 280 × 200 × 95 mm (varies by vehicle model) |
| Compressor power | 5–10 kW, adjustable to application |
| PTC heating power | 8 kW heating + 24 kW battery heating (two channels) |
| Power devices | SiC |
| Cable connectors | Metal cable glands |

> 表下小字（Codex 加在表格下方）：*For certification requirements on your project, contact our engineering team.*

---

## 五、SEO 备注（Codex 执行时遵守）

1. **内链**（URL 为占位，发布时 Codex 按实际 slug 确认）：
   - §3.1 末尾链 T11：`/blog/ev-thermal-control-strategy/`
   - §3.2 末尾链 T10：`/blog/integrated-thermal-controller-cost/`
   - 两个链接用文章完整英文标题做锚文本（文案中已写好）。
2. **Related Products 区**：第 3 个链接指向 `/engineering/`（非产品页）——替换为真实产品页（建议 `/products/electric-compressor/` 已有则复用，或 BTMS 分类页）。（T7 已记录，此处提醒。）
3. **Title/meta 不动**：已于 2026-10-09 改好并验证。
4. **关键词**：页面主关键词 `three-in-one thermal management controller`；次关键词 `thermal management controller 600V 800V electric bus`、`integrated thermal management controller`。H1 不变。
5. **唯一 H1**：新增的两个 H2 区块不得使用 H1 标签；对比表格用 table 元素，不要用标题标签做表头。
6. 发布后 Muse 按 T7 标准验收（链接、排版、SEO 字段）。

---

## 六、红线自查（本方案已遵守）

- [x] 全部事实出自产品总档 v2，无虚构功率/尺寸/认证
- [x] 未声称任何认证（CE/EMark/UL 均未写）
- [x] 无具名客户/车队案例（仅 "commercial vehicles" 泛称）
- [x] 温度全篇 -40℃~+65℃
- [x] 13 bar 标注为示例、可按项目标定
- [x] 5 K 过热度标注为行业常见做法、按项目标定
- [x] 尺寸标注"约"＋按车型调整
- [x] 语气：厂家视角、平实专业、无 hype
