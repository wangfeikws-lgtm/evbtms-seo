# DAILY-BTMS-1022 返工v2：型号配置说明，不另建重复气流页

负责人Codex。2026-10-22晚间。原冷凝器气流候选因与10074撞题且缺实测数据撤销新建建议。此稿用冻结型号资料与假设计算重组，作为现有10085评级条件文或5kW商业页的支持内容候选；不未经意图复核新建URL。

## SEO与页面归属
- Title/H1: A 5 kW BTMS Is Not a Complete Specification
- Meta: Compare the actual BTMS model, heating option and voltage window—not cooling kilowatts alone. Use EVLINK's listed configurations to define the next review.
- Primary keyword: 5kW BTMS specifications
- Supporting: BTMS cooling and heating; BTMS voltage range; battery thermal management selection
- URL: 不申请新建。优先增补既有10085 /btms-cooling-capacity-rating-conditions/或产品页，最终由Peter审核具体落点。
- 与9840通用选型的区别：本稿只讲同5kW标签的配置差异，不重写全面选型流程。
- 资料：REPORTS/evptc-official-spec-summary.md型号行；https://evbtms.com/products/battery-thermal-management-system/5kw/公开LDC560HA口径。原始xlsx/曲线本轮未重验。
- 搜索证据：2026-10-22通用查询“5kW BTMS heating 6kW”出现产品页和目录，表明当前可见结果以产品规格为主，因此优先商业页/既有文章支持，不凭搜索片段建立新独立文章。没有国家/设备固定Top5，不报门禁通过。
- 算例：820V为假设连接电压；6kW×0.5h=3kWh是热量计算，不是实测、不是直接电输入或升温时间。
- 不含机组气流实测数据、客户经历、认证、产量和效果保证。

## 正文HTML
```html
<p>We would not accept “5 kW BTMS” as a complete selection specification. It identifies a cooling-capacity class, but it does not settle the heating configuration, voltage window or duty the unit must support. Those omissions can survive a quotation comparison and appear only when the vehicle team starts connecting systems.</p>

<p>EVLINK's own model list contains two useful examples: LDC502HA-5KW and LDC560HA-5KW. Both are listed at 5 kW cooling, 400–860 V DC, 24 V DC control supply, 32 kg and 775 × 594 × 286 mm. The heating entries are not the same. LDC502HA lists heating as optional without a capacity in that row; LDC560HA lists 6 kW PTC heating. The shared “5 kW” label cannot answer whether a quotation includes the required winter function.</p>

<h2>Ask what the quoted configuration includes</h2>
<p>For a cooling-only project, an optional heating entry may be perfectly reasonable. For a vehicle that requires preconditioning, it leaves a question to resolve: which heater, control arrangement and installation items are included? We would write those items into the comparison rather than infer them from a cooling rating.</p>
<p>The published <a href="https://evbtms.com/products/battery-thermal-management-system/5kw/">5 kW BTMS product page</a> describes the LDC560HA configuration with 6 kW heating. That does not convert every 5 kW unit in the range into the same configuration. Use the model and revision on the actual quotation.</p>

<h2>More cooling capacity can still be the wrong electrical fit</h2>
<p>Our existing specification summary lists LDC300HA-3KW and LDC280HA-12KW at 400–750 V DC. The two 5 kW models above are listed at 400–860 V DC. A buyer comparing only 3, 5 and 12 kW could miss that difference.</p>
<p>Consider a hypothetical vehicle connection that can reach 820 V. On the listed ranges alone, a direct connection to a unit whose maximum is 750 V is not an acceptable selection. A 12 kW cooling label does not override its electrical limit. The 400–860 V models merit further electrical review, but that range alone does not prove the complete vehicle match.</p>
<p>If the architecture includes a separate converter or another supply arrangement, assess the voltage actually presented to the BTMS. Do not compare an upstream battery nominal voltage with the wrong interface. Record the minimum, maximum and relevant operating conditions at the unit's connection.</p>

<h2>Keep cooling, heating and electrical input separate</h2>
<p>A 5 kW cooling rating describes a heat-removal duty under its stated conditions. It is not a claim that electrical input is 5 kW. Likewise, a heating-capacity entry and a cooling-capacity entry are different duties, not values to add into a single universal system rating.</p>
<p>For an illustration, delivering a constant 6 kW of heat for half an hour transfers 3 kWh of thermal energy. That calculation says nothing by itself about how quickly a specific battery warms. Pack thermal mass, initial temperature, heat losses, coolant distribution and the actual available heater output still determine the response. It is not an EVLINK warm-up test.</p>

<h2>Use the load record to select the capacity</h2>
<p>A larger unit is worth considering when the required cooling duty exceeds the smaller unit's available output at matching conditions. It is not automatically necessary because the battery capacity is larger. Establish the heat-generation profile, coolant limits, ambient conditions and operating cycle first.</p>
<p>For charging and driving, distinguish the peak from the duration and repetition of the load. For heating, state the starting condition, target and time available. If those data are unknown, the sensible next step is a requirements review, not a confident recommendation of 12 kW.</p>
<p>The existing <a href="https://evbtms.com/battery-heat-load-btms-sizing-commercial-ev/">battery heat-load worksheet</a> and <a href="https://evbtms.com/btms-cooling-capacity-rating-conditions/">BTMS rating-condition guide</a> cover those two parts of the decision. This comparison supplies the model-level configuration distinction rather than repeating the complete sizing process.</p>

<h2>What belongs on the comparison sheet</h2>
<p>Put the model and configuration revision beside the cooling duty, heating duty and voltage limits. Then add the low-voltage supply, controls, mechanical envelope and the applicable performance conditions. Where an option has not been defined, leave a visible open item rather than quietly assuming it is included.</p>
<p>We can start a product discussion from the available information without claiming a finished vehicle design. When you <a href="https://evbtms.com/contact/">ask EVLINK for a BTMS configuration review</a>, identify the vehicle, actual supply range, cooling and heating needs, ambient conditions and any installation drawing you can share. State which inputs remain unknown. That is a more useful enquiry than a request for “the biggest 5 kW unit”.</p>
```

## 配图与检测
新封面已制作并人工目视检查：assets/btms-configuration-v2-feature.png及.webp。基于公开5kW产品参考，标题“5 kW IS NOT THE FULL SPEC”，副标题“Check Heating, Voltage and Configuration”；标注Product configuration illustration。属于AI辅助配置示意，不作原始实物摄影或测试证据。不能复用旧气流主题封面。
固定检测文本：REPORTS/detection-1022/DAILY-BTMS-1022-configuration-v2.txt。本v2未测，不沿用原69%或其他文章分数。ZeroGPT<=30%才可作为合格交稿，GPTZero仅参考；彼此不等于实际人工占比。正文任何改变后重导出、重测。
Peter明天审核后才决定发布；本轮不修改生产。
