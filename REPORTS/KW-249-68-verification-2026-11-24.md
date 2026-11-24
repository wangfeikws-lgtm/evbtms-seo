# KW-249《249 词 C 档 68 词》承接页核验（2026-11-24，Muse 补位，Codex 未交改派）

- 来源：协作仓库 REPORTS/newsite-249-ranking-actions-2026-10-28.csv（Codex 2026-10-28 提交，commit 3879e453），全文 249 行逐行核对：A 保住前 15 有 8 词、B 优先推进前 15 有 33 词、C 长期建设 68 词、先核实业务与意图 93 词、不作为目标 47 词，8＋33＋68＋93＋47＝249，对得上。本项只做 C 档 68 词，其余四档未动。B 档 33 词已于 2026-11-02 核验完毕（REPORTS/KW-249-priority-33-verification-2026-11-02.md）。
- 核验方法：2026-11-24 用 curl 公开读取 9 个承接页的真实标题与正文内容逐词核对，不猜 URL、不改任何 URL／结构；对照 GSC 快照 2026-11-24.md（数据至 11-21）的 7 天／28 天查询与页面数据；对 8 个承接页存疑的词做美国 SERP 抽查（dc charger thermal management system、engine coolant heater manufacturer、rail transit thermal management、electric bus roof cooling、how are electric buses heated、air-cooled heat exchangers for mining truck、battery thermal management heater manufacturer、thermal design alignment）。
- CSV 自标注：68 词中仅 4 词“已按完全匹配查询实测”（#1–#4），其余 64 词标注“实际 URL 未逐词核验、仅为建议归属”；本轮 68 词承接页全部逐个核验完毕。
- 结论：**匹配 39／弱匹配 16／需换页 2／不匹配 11**，合计 68。10-28 快照值：68 词合计 332 曝光、1 点击（仅 high voltage heater 有 1 点击）；全部排名 50–100 位，属长期建设档，无前 20 词。
- 排名、点击、曝光数字沿用 10-28 快照值（见表），仅下节所列 6 词有 11-24 快照新数据；其余 62 词未出现在本次快照的 Top 查询列表中（快照只列前 10），当前位置未重测。搜索量／KD 不在 CSV 源数据中，未编造（KW-249 是 GSC 排名词，与 SEMrush 挖词量不合并计数，与 33 词核验口径一致）。

## GSC 11-24 快照对照（数据至 11-21）

- high voltage heater（#23）：28 天 1／7／21.0 名，10-28 为 1／3／52.3——排名 52.3→21.0，大幅上升；68 词中唯一有点击的词，仍是 C 档头号词。
- braking resistor（#20）：28 天 0／29／63.4，10-28 为 0／4／75.2——曝光 4→29、排名 75.2→63.4，上升；制动电阻产品页仍是全站点击第 1 页（28 天 3／88／21.0）。
- thermal management system（#18）：7 天 0／16／25.6，10-28 为 0／5／63.2——排名 63.2→25.6，大幅上升。
- compressors for electric vehicles（#9）：7 天 0／12／51.8，10-28 为 0／10／69.5——排名 69.5→51.8，上升。
- battery thermal management system（#1）：BTMS 主型号页 28 天 0／69／62.9，10-28 为 0／43／62.7——排名持平约 63 位，未进前 40。
- dc charger thermal management system（#2）：28 天 0／0／无数据，本窗口零展示（10-28 为 0／32／84.3）——只观察不做。

## 核验清单（68 词，按 10-28 曝光降序）

| # | 优先词 | 10-28 快照（点击／曝光／排名） | 已核验承接页 | 核验结论 |
|---|---|---|---|---|
| 1 | battery thermal management system | 0／43／62.7 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页（3／5／12 kW、选型、CAN、PTC 制热）；11-24 快照主型号页仍约 63 位 |
| 2 | dc charger thermal management system | 0／32／84.3 | https://evbtms.com/system-design-integration/ | 不匹配：SERP 均为直流快充桩散热（Cooltron 充电桩冷却、EVSE 液冷），充电桩冷却不在 EVLINK 业务内（只观察不做）；承接页零充电桩内容；11-24 快照本窗口零展示。建议移出目标 |
| 3 | thermal design validation | 0／24／67.3 | https://evbtms.com/prototype-validation/ | 匹配（主题匹配）：原型验证与热管理测试页；“thermal design validation”短语未逐字出现 |
| 4 | electric vehicle thermal management system | 0／21／59.2 | https://evbtms.com/system-design-integration/ | 匹配：EV 热系统设计与集成总页 |
| 5 | charging solutions for electrical refrigerated trucks | 0／15／79.1 | https://evbtms.com/system-design-integration/ | 不匹配：冷藏车（冷链）充电方案，非 EVLINK 业务；承接页无冷藏车内容。建议移出目标 |
| 6 | thermal load management system | 0／12／69.8 | https://evbtms.com/system-design-integration/ | 匹配：页面含 thermal load 表述，属系统设计范畴 |
| 7 | high voltage thermal management heater | 0／11／67.5 | https://evbtms.com/products/high-voltage-coolant-heater/ | 匹配：高压加热器产品页 |
| 8 | electric bus btms | 0／11／80.6 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页含电巴应用；注：电巴页也可承接，维持原分配 |
| 9 | compressors for electric vehicles | 0／10／69.5 | https://evbtms.com/products/electric-compressor/ | 匹配：电动压缩机页；11-24 快照 7 天 51.8 名（上升）。附注：Electric Compressor 单品已从 Products 下拉移除、不推广，页面保留作承接，不另建内容 |
| 10 | ev thermal management system | 0／9／63.6 | https://evbtms.com/system-design-integration/ | 匹配：EV 热管理系统设计与集成页 |
| 11 | custom high voltage heater assembly | 0／8／58.0 | https://evbtms.com/products/high-voltage-coolant-heater/ | 匹配（概念匹配）：页内 Custom HV Range 与项目定制配置；“assembly”一词未出现 |
| 12 | ev thermal management systems china | 0／7／66.7 | https://evbtms.com/system-design-integration/ | 匹配：中国厂商＋OEM 身份在页 |
| 13 | ev charging cabinet thermal management system | 0／7／88.3 | https://evbtms.com/system-design-integration/ | 不匹配：充电柜散热属充电桩侧；承接页零充电桩内容；与 #2 同族。建议移出目标 |
| 14 | electric bus roof cooling | 0／6／72.7 | https://evbtms.com/electric-bus/ | 不匹配：SERP 均为车顶空调机组（TCHAIN、Thermo King、Webasto、Konvekta 车顶空调）；EVLINK 不做车顶空调；承接页零 roof／HVAC／空调内容。建议移出目标（无合适承接页） |
| 15 | battery thermal management systems | 0／5／52.4 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页（复数形同义） |
| 16 | thermal management architecture | 0／5／52.4 | https://evbtms.com/system-design-integration/ | 匹配：页面含 thermal architecture 表述 |
| 17 | ev battery thermal management system | 0／5／62.2 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页 |
| 18 | thermal management system | 0／5／63.2 | https://evbtms.com/system-design-integration/ | 匹配：热管理系统总页；11-24 快照 7 天 25.6 名（大幅上升） |
| 19 | generator thermal load management system | 0／4／63.2 | https://evbtms.com/system-design-integration/ | 不匹配：发电机热管理，非 EVLINK 业务；承接页零 generator 内容。建议移出目标 |
| 20 | braking resistor | 0／4／75.2 | https://evbtms.com/products/braking-resistor/ | 匹配：制动电阻产品页；11-24 快照 28 天 63.4 名（上升），产品页全站点击第 1 |
| 21 | powertrain thermal management | 0／4／78.0 | https://evbtms.com/system-design-integration/ | 弱匹配：页面无 powertrain（含 power train／drivetrain 变体均无）；动力总成热管理是独立子系统，页面未作主题覆盖，最佳可用页 |
| 22 | thermal management system manufacturer china | 0／4／86.8 | https://evbtms.com/system-design-integration/ | 匹配：制造商身份＋中国＋OEM 在页 |
| 23 | high voltage heater | 1／3／52.3 | https://evbtms.com/products/high-voltage-coolant-heater/ | 匹配：高压加热器产品页；68 词唯一有点击的词，11-24 快照 28 天 21.0 名（大幅上升） |
| 24 | battery thermal management system for electric vehicles | 0／3／59.0 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页 |
| 25 | rail transit electronic cooling systems manufacturer | 0／3／66.3 | https://evbtms.com/system-design-integration/ | 不匹配：SERP 为轨道交通 HVAC 与电池轨道车；EVLINK 无轨道产品；承接页零 rail transit 内容。建议移出目标 |
| 26 | battery thermal solutions | 0／3／66.7 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页 |
| 27 | electrification validation | 0／3／70.7 | https://evbtms.com/prototype-validation/ | 弱匹配：验证与测试主题在，但 electrification 一词不在页 |
| 28 | contact ev cooling solutions | 0／3／84.0 | https://evbtms.com/system-design-integration/ | 弱匹配：联系类查询，页面有联系入口但非联系页；备选 /contact/；仅 3 次曝光，低优先级 |
| 29 | ev thermal management manufacturer | 0／3／89.0 | https://evbtms.com/system-design-integration/ | 匹配：制造商身份在页 |
| 30 | electric bus hvac systems | 0／3／92.0 | https://evbtms.com/electric-bus/ | 弱匹配：页面有制冷制热内容，但零 HVAC／空调内容；HVAC 系统（车顶空调机组）属 EVLINK 不做的产品族 |
| 31 | high voltage ptc heater supplier | 0／2／50.5 | https://evbtms.com/products/high-voltage-coolant-heater/ | 匹配：页内 PTC＋供应商身份，标题即制造商 |
| 32 | battery thermal management system of electric vehicles | 0／2／53.0 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页 |
| 33 | how are electric buses heated | 0／2／56.0 | https://evbtms.com/system-design-integration/ | 换页：SERP 为电巴加热方式科普（PTC、热泵、燃油加热器），应由电巴应用页回答，系统设计页是服务页而非问答页。换至 https://evbtms.com/electric-bus/（页内有 heater／heating 内容） |
| 34 | high voltage ptc heater manufacturer | 0／2／58.5 | https://evbtms.com/products/high-voltage-coolant-heater/ | 匹配：页内 PTC＋制造商身份 |
| 35 | thermal design alignment | 0／2／58.5 | https://evbtms.com/system-design-integration/ | 不匹配：SERP 为热成像相机对准、旋转机械热膨胀对准、热焊盘对准，与 EV 热管理无关，词意不明，属噪声词。建议移出目标 |
| 36 | battery pack thermal management system | 0／2／61.5 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页含 battery pack 内容 |
| 37 | how to size a braking transistor | 0／2／64.0 | https://evbtms.com/products/braking-resistor/ | 弱匹配：页面零 transistor 一词；词本身疑似 braking resistor 的误写／口语变体；页面有 sizing 与 chopper 内容，为最佳可用页 |
| 38 | ev battery heater manufacturer in china | 0／2／66.0 | https://evbtms.com/products/high-voltage-coolant-heater/ | 匹配：EV 电池加热器制造商即 HVCH 页 |
| 39 | engine coolant heater manufacturer | 0／2／74.0 | https://evbtms.com/products/high-voltage-coolant-heater/ | 不匹配：SERP 主导为 Webasto／Arctic Fox 柴油／燃油发动机预热器；engine coolant heater 指内燃机预热，非 EV 高压加热；承接页零 engine coolant 内容。建议移出目标 |
| 40 | ev thermal management | 0／2／74.0 | https://evbtms.com/system-design-integration/ | 匹配：EV 热管理设计与集成页 |
| 41 | powertrain thermal systems | 0／2／75.5 | https://evbtms.com/system-design-integration/ | 弱匹配：同 #21，页面无 powertrain 内容 |
| 42 | ev thermal solution provider | 0／2／76.0 | https://evbtms.com/system-design-integration/ | 匹配：EV 热解决方案供应商身份在页 |
| 43 | two-way thermal management system | 0／2／81.0 | https://evbtms.com/system-design-integration/ | 弱匹配：页面无 two-way／bidirectional 一词；制冷＋制热双向概念页面两者都有，最佳可用页 |
| 44 | battery thermal management solution | 0／2／83.0 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页 |
| 45 | battery thermal management solutions supplier | 0／2／83.0 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页含 supplier 身份 |
| 46 | battery pack thermal management systems | 0／2／84.0 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页 |
| 47 | thermal management electrification | 0／2／85.0 | https://evbtms.com/system-design-integration/ | 弱匹配：词意宽泛，页面无 electrification 表述 |
| 48 | ev thermal management solution provider | 0／2／87.0 | https://evbtms.com/system-design-integration/ | 匹配：EV 热管理解决方案供应商身份在页 |
| 49 | scalable cooling system integration | 0／2／52.0 | https://evbtms.com/system-design-integration/ | 弱匹配：集成主题在，但 scalable 一词不在页 |
| 50 | traction resistor | 0／1／53.0 | https://evbtms.com/products/braking-resistor/ | 弱匹配：页面零 traction 一词；牵引电阻属轨道／工业语境，页面是 EV 制动电阻，最佳可用页 |
| 51 | cooling bus | 0／1／55.0 | https://evbtms.com/electric-bus/ | 弱匹配：词意不明（公交制冷／笔误），页面为最佳承接 |
| 52 | battery thermal management heater manufacturer | 0／1／57.0 | https://evbtms.com/products/battery-thermal-management-system/ | 换页：SERP 该词首位即 EVLINK 自家 HVCH 产品页（电池预热、座舱加热、15–35 kW）；查询意图是加热器产品而非 BTMS 系统。换至 https://evbtms.com/products/high-voltage-coolant-heater/ |
| 53 | thermal management system for electric vehicles | 0／1／61.0 | https://evbtms.com/system-design-integration/ | 匹配：EV 热管理系统设计与集成页 |
| 54 | e compressor for electric vehicle | 0／1／62.0 | https://evbtms.com/products/electric-compressor/ | 匹配：电动压缩机页；附注同 #9（单品不推广，页面保留作承接） |
| 55 | e-mobility thermal conditioning systems | 0／1／62.0 | https://evbtms.com/system-design-integration/ | 弱匹配：e-mobility 一词不在页，EV 热调节主题相近 |
| 56 | ev heater factory quote | 0／1／66.0 | https://evbtms.com/products/high-voltage-coolant-heater/ | 匹配：工厂身份＝制造商标题，quote 入口在页 |
| 57 | rail transit thermal management | 0／1／69.0 | https://evbtms.com/system-design-integration/ | 不匹配：同 #25，SERP 为轨道交通 HVAC 与电池轨道车；承接页零 rail transit 内容。建议移出目标 |
| 58 | powertrain thermal | 0／1／76.0 | https://evbtms.com/system-design-integration/ | 弱匹配：同 #21／#41，页面无 powertrain 内容 |
| 59 | vehicle thermal management system | 0／1／79.0 | https://evbtms.com/system-design-integration/ | 匹配：车辆热管理系统设计与集成页 |
| 60 | btms system | 0／1／81.0 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 产品页 |
| 61 | cooling load management systems | 0／1／82.0 | https://evbtms.com/system-design-integration/ | 弱匹配：页面无 cooling load 表述（有 thermal load）；制冷负荷管理非页面主题 |
| 62 | industrial liquid cooling systems for ev applications | 0／1／84.0 | https://evbtms.com/system-design-integration/ | 弱匹配：页面无 industrial liquid cooling 表述；工业角度非页面主题 |
| 63 | air-cooled heat exchangers for mining truck | 0／1／85.0 | https://evbtms.com/electric-mining-truck/ | 不匹配：SERP 为铝制板翅风冷换热器（发动机／液压／变速箱油路）；EVLINK 矿卡页是液冷电池 BTMS，零 air-cooled／heat exchanger 内容。建议移出目标（风冷换热器非 EVLINK 产品） |
| 64 | charging pile thermal solution provider | 0／1／85.0 | https://evbtms.com/system-design-integration/ | 不匹配：充电桩热方案属充电桩侧；承接页零充电桩内容；与 #2／#13 同族。建议移出目标 |
| 65 | thermal management system solution | 0／1／86.0 | https://evbtms.com/system-design-integration/ | 匹配：热管理系统解决方案页 |
| 66 | thermal management modules solutions | 0／1／88.0 | https://evbtms.com/system-design-integration/ | 弱匹配：页面无 modules 表述；模块化热系统非页面主题 |
| 67 | battery thermal management equipment manufacturer | 0／1／96.0 | https://evbtms.com/products/battery-thermal-management-system/ | 匹配：BTMS 设备制造商身份在页 |
| 68 | battery air cooling system | 0／1／100.0 | https://evbtms.com/battery-liquid-cooling-vs-air-cooling/ | 匹配：液冷 vs 风冷对比文章，air cooling 内容在 |

## 不匹配清单（11 词，建议移出 C 档目标）

| # | 词 | 原因 |
|---|---|---|
| 2 | dc charger thermal management system | 充电桩散热，业务外；本窗口零展示 |
| 5 | charging solutions for electrical refrigerated trucks | 冷藏车冷链，业务外 |
| 13 | ev charging cabinet thermal management system | 充电柜散热，业务外 |
| 14 | electric bus roof cooling | 车顶空调机组，EVLINK 不做该产品，无承接页 |
| 19 | generator thermal load management system | 发电机热管理，业务外 |
| 25 | rail transit electronic cooling systems manufacturer | 轨道交通，业务外 |
| 35 | thermal design alignment | 词意不明，SERP 与 EV 热管理无关，噪声词 |
| 39 | engine coolant heater manufacturer | 燃油／柴油发动机预热器，内燃机方向 |
| 57 | rail transit thermal management | 轨道交通，业务外 |
| 63 | air-cooled heat exchangers for mining truck | 风冷换热器产品，非 EVLINK 产品 |
| 64 | charging pile thermal solution provider | 充电桩热方案，业务外 |

## 换页建议（2 词）

| # | 词 | 原承接页 | 换至 | 依据 |
|---|---|---|---|---|
| 33 | how are electric buses heated | /system-design-integration/ | https://evbtms.com/electric-bus/ | 问答意图由电巴应用页回答；系统设计页是服务页 |
| 52 | battery thermal management heater manufacturer | /products/battery-thermal-management-system/ | https://evbtms.com/products/high-voltage-coolant-heater/ | SERP 该词首位即 EVLINK 自家 HVCH 页；意图是加热器产品 |

## 弱匹配清单（16 词，暂不换页，维持原承接页）

#21／#41／#58 powertrain thermal management／powertrain thermal systems／powertrain thermal（页面无 powertrain 内容，动力总成热管理未作主题覆盖）；#27 electrification validation；#28 contact ev cooling solutions（备选 /contact/）；#30 electric bus hvac systems（页面无 HVAC 内容）；#37 how to size a braking transistor（疑似误写，页面有 sizing 与 chopper）；#43 two-way thermal management system；#47 thermal management electrification；#49 scalable cooling system integration；#50 traction resistor（轨道／工业语境）；#51 cooling bus（词意不明）；#55 e-mobility thermal conditioning systems；#61 cooling load management systems；#62 industrial liquid cooling systems for ev applications；#66 thermal management modules solutions。

## 未核到／未重测说明

- 62 词未出现在 GSC 11-24 快照的 Top 查询列表中（快照只列前 10），当前位置未重测，沿用 10-28 快照值；本轮未逐词查美国 SERP，仅 8 个存疑词做了抽查（见方法节）。
- SEMrush 搜索量／KD 不在 CSV 源数据中，本报告未编造；33 词核验同样沿用快照值。
- 未改任何 URL／结构，未发布，未推仓。

## 附注

- 承接页集中度：/system-design-integration/ 承接 34 词、BTMS 产品页 14 词、HVCH 产品页 8 词、制动电阻页 3 词、电巴页 3 词、原型验证页 2 词、电动压缩机页 2 词、矿卡页 1 词、液冷 vs 风冷文章 1 词，合计 68 词（#33／#52 换页后：系统设计页 33 词、BTMS 页 13 词、HVCH 页 9 词、电巴页 4 词）。
- 上升信号：#18 thermal management system、#23 high voltage heater、#9 compressors for electric vehicles、#20 braking resistor 四词 11-24 快照排名较 10-28 明显上升（63→26、52→21、70→52、75→63），其中 #23 是 68 词中唯一有点击的词，优先跟进价值最高。
- Electric Compressor 单品已从 Products 下拉移除、不推广（#9／#54 承接页保留，不另建内容）。
