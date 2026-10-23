# 两站核心内容分工与去重处置（2026-10-22 本轮）

## 范围和证据

- 新站公开WP REST：37篇已发布文章、54个页面；单页上限100而实际少于100，涵盖本轮接口返回的全部publish记录，不含草稿/回收站/自定义文章类型。
- 老站公开sitemap与news发现54条URL，含3个列表页及同一内容的2个别名地址；实际文章记录51条、按canonical折算50篇。不是ECER私有后台导出，不声称覆盖未公开/孤立稿件。
- 原始证据：public-audit/inventory.json、page-snapshots.json、article-titles.md。标题相似只用于候选发现，不作为合并/删除依据。
- 不执行任何删除、改URL、301或跨域canonical。

## 立即裁决

1. DAILY-BTMS-1022气流新稿与新站10074《BTMS Condenser Airflow: An OEM Installation Review》同一意图，撤销新页面建议。已有URL /btms-condenser-airflow-installation/保留。缺EVLINK实测资料时只允许谨慎的增补建议，不编造。
2. DAILY-HVCH-1022低压唤醒稿与10116 CAN集成、10031功率验证相邻，但“为何不启动”是更窄排障任务；可修订候选，不把接口总清单重写一遍。优先评估作为现有CAN文的支持模块，未验证搜索需求前不承诺新建。
3. T12-W2最终稿使用Muse的v2/v3，不再用Codex旧v1覆盖检测分数或正文。

## 意图簇分工（保留现有URL，以下不是新建清单）

| 意图 | 新站主承接 | 老站承接 | 裁决 |
|---|---|---|---|
| HVCH是什么/原理 | /how-high-voltage-coolant-heater-works/（333） | 老站How Does a High Voltage Coolant Heater Work | 都保留；新站讲系统热路与集成，老站讲产品原理。需要逐段文本相似审查，不能仅凭标题合并 |
| HVCH产品/规格 | /products/high-voltage-coolant-heater/ | 对应系列与功率电压产品页 | 两站均已有商业页，不整篇互抄；分别体现系统集成与型号选型 |
| 400V/800V选择 | /400v-800v-high-voltage-coolant-heater/（9935） | 型号电压产品页 | 新站承担边界/接口解释，老站承担实际型号，不新建近义文章 |
| HVCH选型/RFQ | /high-voltage-coolant-heater-rfq-checklist/（9917） | W1-1七项输入 | 新站集成资料交接，老站采购选型；交叉支撑，不复制清单全文 |
| CAN集成 | /hvch-can-integration-oem-checklist/（10116） | W1-2 CAN与温控架构 | 新站信号/验收，老站控制架构选择；B/E真实差异要保留 |
| 流量/压降 | /hvch-coolant-flow-pressure-drop-oem-guide/（9856） | 产品曲线和接口资料 | 优先升级9856；新文章不能只是改问法 |
| 功率/热量验证 | /hvch-power-verification/（10031） | 型号额定参数 | 10031解释请求/输入/热侧差异；型号表不代替测试 |
| 冬季预热 | /cold-weather-battery-preconditioning-electric-buses-trucks/（9845） | W1-3−30°C规划误区 | 保留不同任务；避免共用具体段落和虚构温升/时间 |
| 热泵与PTC | /heat-pump-hvch-backup-heating-duty/（10088） | W1-4各系统适用条件 | 新站重点备用负荷和控制，老站选型；不再写第三篇泛对比 |
| 风暖与水暖 | /ptc-coolant-heater-vs-air-heater/（9941） | W2-04总成本 | 保留“架构选择”与“成本范围比较”的差异；不得笼统宣称总更便宜 |
| BTMS选型 | /how-to-select-btms-electric-truck-bus/（9840） | 老站BTMS产品/基础介绍 | 新站主工程支持；老站产品介绍不再重复长篇选型 |
| BTMS验证 | /btms-validation-electric-truck-bus/（9841） | 产品支持资料 | 与9840标题相似但任务不同，不能因0.90标题相似度合并 |
| BTMS流量/泵扬程 | /btms-coolant-flow-rate-commercial-ev/（9920）、/btms-pump-head-pressure-drop-commercial-ev/（10095） | 产品接口资料 | 9920热负荷估算，10095水力工作点；互链而非合并 |
| BTMS测温/温差 | /btms-temperature-sensor-placement/（9938）、/btms-temperature-spread-diagnosis/（10019） | 无新增建议 | 测点设计与故障诊断不同，保留 |
| BTMS气流/冷量 | /btms-condenser-airflow-installation/（10074）、/btms-cooling-capacity-rating-conditions/（10085） | 产品额定数据 | 不新建重复气流页；资料不足就暂缓实测结论 |
| 控制器成本/策略 | /integrated-thermal-management-controller-cost/（9949）、/ev-thermal-management-control-strategy/（9951） | 对应产品页 | 成本范围与控制职责不同，保留；可补指向BTMS商业页的语境内链 |
| 制动电阻 | T8已有7篇及产品页 | 不派新文章 | Muse负责，不为日档重复写 |
| 换电重卡 | 新站应用方案；老站现有换电新闻 | T12-W2-05工程稿 | 新闻与长期工程说明区别；不得声称同一运营商是EVLINK客户 |

## 后续验收

- 标题清单和上述分工已交付，实际“谷歌关键词互抢”必须用同一GSC查询/页面数据验证；当前没有数据，不能宣称已证明蚕食。
- 优先从现有商业页和已排名文章做最小有效修改，不追求新URL数量。
