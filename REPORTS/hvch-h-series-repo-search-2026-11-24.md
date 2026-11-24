# H 系高压加热器资料仓库检索报告（2026-11-24）

- 任务来源：Codex 周二八项第 8 项未交，改派检索。只做检索报告，不发布、不推仓。
- 结论一句话：**找到了。H 系参数在 Peter 2026-10-10 提供的官方双语规格书里全有。** 仓库 Single Source of Truth（`REPORTS/evptc-official-spec-summary.md`）早已据此汇总过 H 行。2026-11-09 摸底报告"老站无 H 产品页"的结论仍成立——它查的是老站网站，不是规格书；两者不冲突，参数缺口现由规格书补上。

## 一、找到的参数（原样抄录）

来源：`~/workspace/user/files/-.xlsx`（Peter 2026-10-10 提供的官方双语规格书），工作表「H系列」（A1:F18，全表 18 行已逐行核对）。

| 项目 | 数值（中文 / 英文原样） |
|---|---|
| 额定电压 Rated Voltage | 可定制 / Customizable |
| 工作电压范围 Operating Voltage Range | 400V-1000V |
| 功率 Power Output | 5-14KW |
| 绝缘电阻 Insulation Resistance | ≥100MΩ（DC1000V）（高压部分）/ ≥100 MΩ (DC1000 V, high-voltage section) |
| 工作温度 Operating Temperature | -40ºC~+85ºC |
| 防护等级 Protection Rating | IP67 |
| EMC | 满足ISO 11452 Class 3 要求 / Complies with ISO 11452 Class 3 requirements |
| 高压安全防护 High-Voltage Safety Protection | 具备过压、欠压、过流、短路、过热保护等 / Equipped with overvoltage, undervoltage, overcurrent, short circuit, and overheat protection |
| 通讯方式 Communication Method | CAN通讯，使能通讯 / CAN communication, enable signal communication |
| 系统舒适性、安全性控制 System Comfort & Safety Control | 支持PID调节、故障自诊断、自动限功率等 / Supports PID control, fault self-diagnosis, automatic power limiting |
| 质保期 Warranty | 2年 / 2 years |
| 已有认证 Certifications Obtained | CE，E-Mark |
| 重量 Weight | 5KG |
| 产品尺寸 Product Size | 33.5X17X10.6cm |

## 二、接插件 / 变体（原样抄录）

来源：同一规格书工作表「公司产品介绍」（水加热器变体表），表头：系列 | 状态 | 状态 | 高压插件 | 低压插件。

- H 系列：高压插件 **HA中航**；变体 **HA高压兴华款**；低压插件 **HV低压甩线款**。
- 料号（按表列原样抄录）：HA高压兴华款行——高压插件 NGY14N1-02-3-1 G018，低压插件 RT0W0106PN03；HV低压甩线款行——高压插件 NGY14N1-02-3-1 G018，低压插件 AMP282090-1。
- 与已知事实一致：HA 高压＋HV 低压主插（Peter 2026-11-13 截图确认）。

## 三、温控口径（按表直述，不推断）

- H 表**无"温控方式 / 恒温器"独立行**（与 E 系"温控器 Thermostat"不同）。控制相关行只有两条：通讯方式 CAN+enable；系统控制"支持PID调节、故障自诊断、自动限功率"。
- 因此：H 系无恒温器口径；温控写法应为整车控制器协调（CAN）＋PID 调节，与 Peter 2026-11-13 给 A、Q 两系定的"Vehicle controller coordination (CAN)"同一路数。是否沿用该写法由 Peter 定，本报告不代定。
- 无温度设定值、无出水温度目标值、无 PID 参数。

## 四、交叉核对（独立来源一致）

- `REPORTS/evptc-official-spec-summary.md`（仓库 Single Source of Truth，来源即同一 xlsx）：H 行——`5–14 kW | 400–1000 V | 5 kg | 335×170×106 mm | CAN＋使能 | 备注"C6 归并主 40754365"`；通用段（除 E/N 外适用：绝缘电阻、工作温度、IP67、EMC、PID 等）与 H 表一致；变体节："H系列：HA中航"。
- `REPORTS/buyer-keyword-lexicon-v01-2026-10-19.md` L88 与 `buyer-keyword-lexicon-v10-2026-10-22.md` L132："H 系列 5–14kW/400–1000V（/5kg）；-40~+85℃、IP67、CAN"。
- `REPORTS/T7-category-cards-model-audit-2026-10-22.md` L53："H 系列：5–14kW / 400–1000V"。
- `REPORTS/linkedin/li-aqh-series-selector-2026-10-20.txt`："H covers 5–14 kW…400–1000V…-40 to +85°C, IP67, CAN plus enable, self-diagnose"。
- `REPORTS/HVCH-CAN-integration-v2-2026-10-22.md` 与 `v3`：同样三数（H 5–14 kW / 400–1000 V）。
- 规格书内 A/Q/E 表与 2026-11-09 摸底报告逐项一致（A 6–18kW/400–800V/CAN、Q 15–35kW/400–1100V/CAN、E 20–24kW/400–800V/温控器/无 CAN），证明 H 表与三系同出一套规格书，可信度相同。
- 2026-11-09 摸底报告（`REPORTS/hvch-series-parameters-recon-2026-11-09.md`）"H 系列未找到产品页"结论仍成立——它查的是老站网站（站内搜索 95 结果、产品总页均无 H 系列），不是规格书。

## 五、未找到（缺什么）

1. **型号名：全仓库无 H 系加热器型号名。** 规格书 H 表无型号行；变体表只有接插件变体（HA/HV），不是加热器型号；站内 `/h-series-high-voltage-coolant-heater/` 与 `/h2-series-high-voltage-coolant-heater/` 只是页面 slug，不是厂家型号名，不可当型号写。
2. **温控设定值：** 无恒温器设定温度、无出水温度目标值、无 PID 参数。
3. **适用车型 / 用途：** H 表无此行（A/Q/E 表同样无此行；A/Q/E 的适用车型来自老站产品页，H 无老站产品页，故无来源）。
4. **MOQ / 交期 / 价格：** 规格书无，仓库无。
5. **H 系老站产品页：** 无（2026-11-09 已查，不重复查）。

## 六、存疑点（不采用，只记录）

1. H 表内嵌残格 `| Power | 15–35 kW |`：与 Q 系功率相同，属模板粘贴残留（同 E 系 FAQ"15–35kW"残留一例，摸底报告已按此先例处理）；正式功率行 5-14KW 为准，不采用。
2. T7 卡表把 `/h-series-high-voltage-coolant-heater/` 与 `/h2-series-high-voltage-coolant-heater/` 两页标为"400v 24kw"：24kW 超出 H 系 5–14kW 范围，卡片标签未经核实，不可当 H 参数用；两卡归属待 Peter 确认（T7 表原意即如此）。
3. 认证口径差异：H 表写"CE，E-Mark"；`evptc-official-spec-summary.md` 总表头写"认证 CE / E-Mark / UL 全系列通用（Peter 2026-10-10 确认）"。Q 表同样只写 CE、E-Mark。以分系表（CE、E-Mark）为准还是以总表头为准，须 Peter 定；本报告不代定。
4. "C6 归并主 40754365"（spec-summary H 行备注）：疑似老站 listing 归并编号，非加热器型号；原意不明，照录不解释。
5. 接口按型号确认：HVCH-CAN-integration v2/v3 稿称"接口按型号确认，部分变体用 LIN"；H 表写 CAN+enable。两者不冲突（表为系列默认值，变体以型号为准），写文案时按型号确认，不一概而论。

## 七、翻过的文件清单

- `~/workspace/user/files/` 全部 8 个文件：`-.xlsx`（即官方双语规格书，22 个工作表；H 系列表全读，A/Q/E/B/K/W/Z 表关键行核对，S/N/BTMS/三合一/暖风机表已扫过与 H 无关）、`20260921…V1.0.pptx`（16 页，0 处 H/HVCH 相关）、`20260917…HVH-R1402-00001CD60_v1.docx`（液冷制动电阻规格书，0 处 H/HVCH 相关）、`B2B__SEO_______V2.0.md`（流程文件，无产品参数）、3 个 skill zip（无关）。
- `~/workspace/evbtms-seo-pending-push/REPORTS/` 全部 214 个文件：全文 grep `H 系|H系列|H-series|H series` 得 22 个命中文件，逐一核对。全文读：`hvch-series-parameters-recon-2026-11-09.md`、`evptc-official-spec-summary.md`、`buyer-keyword-lexicon-v01-2026-10-19.md`、`buyer-keyword-lexicon-v10-2026-10-22.md`、`T7-category-cards-model-audit-2026-10-22.md`、`product-page-assault-plan-2026-11-10.md`、`HVCH-CAN-integration-v2-2026-10-22.md`、`HVCH-CAN-integration-v3-2026-10-22.md`、`linkedin/li-aqh-series-selector-2026-10-20.txt`、`DAILY_PLAN-2026-11-10-draft.md`。其余命中文件（PTC-1111/1116/1117/1118/1119 稿、HVCH-1022v2/1023 稿、`dispatch-2026-10-22-linkedin-publish-backlog.md`）经 grep 核对，均只写"H 系存在，参数按项目给（Peter 2026-11-12／11-13 定）"，无新增参数。
- 未检索：老站网站（2026-11-09 已查过，不重复）；evbtms.com 前台（产品页口径见 PTC-1119 事实核对，已是"H 系存在、参数按项目提供"，与本次结论一致）。
