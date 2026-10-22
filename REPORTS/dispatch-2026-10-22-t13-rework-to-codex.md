# T13 返工执行转派 Codex（Peter 2026-10-22 17:10 指令）

Peter 原话：其余 5 项让 Codex 干，"他很闲"。本单覆盖 `REPORTS/codex-to-muse-browser-handoff-2026-10-22.md` 中 T13 执行归属：**T13 页面执行改回 Codex**；Muse 已完成的矿卡页撤卡（/electric-mining-truck/，2026-10-22 17:07 前台核验通过）不重做。390px 验收仍归 Muse（Codex 改完后 Muse 做）。

## 执行清单（文案一律以 `REPORTS/page-upgrade-copy-pack-2026-10-20.md` 定稿原文，一字不改）

依据核验报告 `REPORTS/T13-verification-2026-10-22.md`：

1. **#1 BTMS 页**（/products/battery-thermal-management-system/）：Title/Meta/H1 不动；补选型段落（H2 `Which Size Do You Actually Need?`＋定稿正文，插在 Product Range 之后、How It Works 之前）；FAQ 3 条按包原文替换（问法＋答案）；内链锚文本按包 4 条落实（其中 2 条是 T10/T11 文章 → 本页，在文章侧加链）。
2. **#2+#7 Applications 页**（/applications/）：Title 改 `Electric Mining Truck Thermal Applications | EVLINK`、Meta/H1 改包定稿；板块顺序调整（Data Center 移到最后）；矿卡板块追加扩写（H3 `The Descent Is the Hard Part`＋定稿正文）；追加 3 条矿卡 FAQ；**产品区 04 号卡 Electric Compressor 换成 Braking Resistor 卡**（包定稿标题＋描述＋链接到 /how-to-size-braking-resistor-electric-bus-truck/）；内链 5 条按包。
3. **#3 HVCH 产品页**（/products/high-voltage-coolant-heater/）：Title 改 `High Voltage Coolant Heater Manufacturer | EVLINK`、Meta 改包定稿；H1 不动；补选型段落（H2 `How to Size a Coolant Heater Without Guessing`）；追加 3 条 FAQ；内链 4 条按包。
4. **#4 三合一页**（/products/three-in-one-controller/）：Title 改 `Three-in-One Thermal Management Controller | EVLINK`、Meta 改包定稿；H1 不动；补对比段落（H2 `Three Separate Controllers vs. One Integrated Unit`）；追加 3 条 FAQ 并核验 FAQPage Schema 输出；内链 3 条按包。
5. **#5 HVCH 厂家页**（/high-voltage-coolant-heater-manufacturers/）：Title 改 `High-Voltage Coolant Heater Manufacturers | EVLINK Factory`、Meta 改包定稿；H1 不动；补工厂段落（H2 `Inside the EVLINK Heater Line`）；追加 3 条 FAQ；内链 3 条按包。

## 暂缓项（不要执行）

- **#6 BTMS 测试板块**（同 BTMS 页）：文案包正文把制动电阻的"25 项测试""9,360 循环"写成了 BTMS 机组数据，Muse 已向 Peter 列异常待确认。Peter 确认前**整节不要上线**（含其 3 条 FAQ）。

## 死线与回填

- **死线 2026-10-23 12:00**，不延期。每页改前记录旧值（Title/Meta/相关段落）入报告；改完逐页在 TASKS.md 本项下留言＋出执行报告入仓，Muse 逐页前台复验（只看真实内容）＋390px 验收。
- **通道预警**：你今日 IAB/Chrome 后台各一次连接超时。若执行通道仍不通，**立刻入仓回报阻塞**，Muse 接管，不许再出现 10-21 那种"死线过了才发现没执行"。
- 红线：不改 URL/301/canonical/插件主题；英文不改字；任一页改坏先回滚再回报。
