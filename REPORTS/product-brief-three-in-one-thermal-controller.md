# 三合一控制器（热管理型）产品总档 v2（完整版）

> 信息来源：Peter 转工厂 Q&A（2026-10-09）＋ 官方中英规格表（2026-10-09）＋ 网站交叉验证 ｜ 整理：Muse
> 本文档为 Codex/Muse/业务共用的唯一产品事实源；更新时同步修改，不另起版本分叉。

## 一、产品定义

**三合一控制器 = 压缩机控制器（DCAC）＋ 制冷系统控制器（ECU）＋ 高压 PTC 控制器**，三合一，
对压缩机、风机、膨胀阀等热管理部件做集中控制。

- 一句话定位：新能源商用车热管理域控制器，用一个控制器代替原来三个独立控制器。
- 适用：600V / 800V 新能源商用车平台（电动大巴、商用车 BTMS 液冷机组等）。

**英文名**：
- 产品主名：`Three-in-One Controller`
- SEO/完整名：`Three-in-One Thermal Management Controller` / `Three-in-One EV Thermal Management Controller`
- 推荐标题：`Three-in-One Thermal Management Controller for Electric Bus`

## 二、官方规格表（2026-10-09 工厂规格表原文）

| 技术性能 Technical Performance | 参数性能 Parameter Specifications |
|---|---|
| 集成方式 Integration Configuration | 集成：压缩机控制器 DCAC、制冷系统控制器 ECU、PTC 高压控制器 / Integrated: DCAC Compressor Controller, Refrigeration System ECU, and High-Voltage PTC Controller |
| 直流额定电压等级 Rated DC Voltage | 600V DC 或 800VDC / 600V DC / 800VDC |
| 控制器输入电压范围 Controller Input Voltage Range | 250V–750V DC 和 600V–1000V DC |
| 电池实际额定电压 Battery Nominal Voltage | 600VDC 或 800VDC |
| 电池供电范围电压 Battery Operating Voltage Range | 400V–750V DC 和 600V–1000V DC |
| 控制器防护等级 Control Box Protection Rating (IP Rating) | ≥IP67 |
| 冷却方式 Cooling Method | 自然冷却 / Natural Cooling（开放鳍片设计，安装点风速 ≥3.5 m/s） |
| 控制器通讯方式 Controller Communication Protocol | CAN 2.0（协议/CAN ID/波特率/控制逻辑可按项目定制） |
| 系统低压控制电源 Low-Voltage Control Power Supply | 24VDC（16–32VDC） |
| 预充电路 Storage Temperature | 模块中内置预充电阻电路 / Integrated Pre-charge Resistor Circuit |
| 工作环境温度范围 Operating Ambient Temperature | **-40~+65℃**（官方定稿；替代口头 +60℃） |
| 安装方式 Mounting Orientation | 竖式安装（要求整机布局便于拆装维护）/ Vertical Mounting |
| 重量 Weight | 6Kg（±10%） |

**补充（Peter 2026-10-09 口头确认）**：
- 压缩机功率：5–10 kW 可调（根据不同场景调整电功率）
- PTC 加热功率：8 kW ＋ 24 kW 电池加热（两路）
- 功率器件：SiC；电缆接头：金属接头

## 三、控制逻辑（工厂 Q&A，已验证）

| 对象 | 控制依据 | 基本逻辑 |
|------|----------|----------|
| 压缩机转速 | 系统水温 / 系统目标温度 | 水温↑ → 转速↑；水温↓ → 转速↓ |
| 膨胀阀开度 | 过热度（Superheat） | 过热度↑ → 开度↑；过热度↓ → 开度↓ |
| 风机 | 冷凝器高压压力（压力＋温度传感器） | 示例约 13 bar 启动冷凝风机；启停压力/转速曲线可按客户系统标定 |

压缩机适配：可适配客户自有压缩机（需客户提供压缩机技术参数＋电机参数）。

## 四、核心优势（vs 传统多控制器独立工作）

1. **结构性降本**：减少零部件数量、线束、控制接口
2. **可靠性提升**：系统故障率降低
3. **EMC 优化**：一体化设计，电磁兼容性更好
4. **集成度高**：单控制器集中控制

## 五、定制能力（OEM/ODM 话术）

- 压缩机适配：可按客户压缩机定制
- 电压平台/输入范围：可定制
- CAN 协议、CAN ID、波特率、控制逻辑：可定制
- 风机启停压力、转速曲线：可按项目标定

## 六、客户常见问答

| 客户可能问 | 标准回答 |
|------------|----------|
| 能适配我们自己的压缩机吗？ | 可以，需要贵司提供压缩机技术参数及电机参数 |
| 压缩机转速怎么控制？ | 根据系统水温及目标温度调节：水温升高→转速提高，水温降低→转速降低 |
| 膨胀阀怎么控制？ | 根据过热度控制：过热度高→开度增大，过热度低→开度减小 |
| 风机怎么控制？ | 根据冷凝器高压压力控制，如约 13 bar 启动；启停压力/转速曲线可按项目标定 |
| 防护等级？ | ≥IP67 |
| 通讯？ | CAN 2.0，协议/ID/波特率/逻辑可定制 |

## 七、尚缺的信息（需工厂补充，Peter 承诺 2026-10-10 给）

- [x] 压缩机功率：5–10 kW 可调（2026-10-09 Peter 确认，指压缩机）
- [x] PTC 功率：8 kW ＋ 24 kW 电池加热，两路（2026-10-09 Peter 确认）
- [x] 工作温度：-40~+65℃（2026-10-09 官方规格表定稿）
- [ ] 机械尺寸
- [ ] 认证（CE/EMark/UL/IATF？）
- [ ] 量产/装车案例
- [ ] MOQ、交期
- [ ] 样件/报价政策

## 八、相关文档索引（Codex 必读）

- 网站产品页：https://evbtms.com/products/three-in-one-controller/（H1: Three-in-One EV Thermal Management Controller）
- 业务版资料：~/workspace/your_files/三合一控制器产品资料-业务版.md（中文话术＋参数表＋问答，给业务直接用）
- 产品策略复盘：REPORTS/three-in-one-thermal-strategy-review.md（含页面优化建议：Title 改名、降本对比模块、+65℃统一等）
- T10/T11 英文博客：REPORTS/T10-integrated-controller-cost-draft.md、REPORTS/T11-thermal-control-strategy-draft.md（均基于本档事实撰写）
- SERP 结论：英文尚无成熟品类词；产品页守品牌词＋博客承接工程流量（见 REPORTS/serp-th*.md）
