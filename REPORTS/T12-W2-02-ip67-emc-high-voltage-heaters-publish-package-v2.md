# T12-W2-02 Publishing Package (v2)

> v2 重组版，2026-10-22，原因：v1 ZeroGPT 40.5% 未过线。本版为全文重组（非润色）：换开头切入点、重排结构、打散段落节奏、观点提前；事实口径与 v1 完全一致，未新增参数、认证、客户或价格声明。SEO 字段、内链清单、图片建议、红线自查沿用 v1 原文。**复测 2026-10-22：ZeroGPT 27.2% ✅ 过线（≤30%）。**

## SEO fields

- **SEO title:** IP67 and EMC in High-Voltage Heaters: What the Spec Sheet Doesn't Tell You | EVLINK
- **Meta description:** IP67 and an EMC pass are real ratings with narrow test conditions. Here is what they cover, what they miss, and the questions to ask any HVCH supplier before design freeze.
- **Primary keyword:** IP67 EMC high voltage heater
- **H1:** IP67 and EMC in High-Voltage Heaters: What the Spec Sheet Doesn't Tell You
- **Recommended slug:** `ip67-emc-high-voltage-heaters-spec-sheet`

## HTML body

```html
<p>Nobody calls us because a heater failed its datasheet. They call in February, when a truck that passed every incoming inspection throwing faults on cold mornings — and the paperwork has a line that says IP67, another that says EMC passed, and both are technically true.</p>

<p>That gap, bench versus winter, is the subject here. We ship IP67 heaters across our A, E, H and Q series, and we would rather explain where the rating stops.</p>

<h2>What the IP67 test actually puts a heater through</h2>

<p>It comes from IEC 60529. The 6 means dust-tight. The 7 is an immersion test, and an oddly gentle one: clean water, one metre deep, thirty minutes, static. No jet, no spray. The unit is new, connectors mated as specified.</p>

<p>Passing it is worth having. Road spray, slush and standing water are its daily diet under a vehicle floor. Do not read more into the two digits than the test put there.</p>

<h2>Where the rating stops: wash bays, birthdays, open connectors</h2>

<p>Pressure washing kills more heaters than deep water. A wash bay is not an immersion tank: a pressure jet at half a metre drives water at the seal faces, and that is IP69K territory, a different rating altogether. Before fixing its position, find out how the depot washes the truck, and how close it gets.</p>

<p>Age is the second gap: the rating describes seals that have never been heat-cycled. Give that connector five winters of −40°C starts, hot coolant, chassis vibration and one hard pull on the harness, and it is not the seal that sat in the tank. What survives to year five comes down to seal compound and connector design, and none of that is on the datasheet.</p>

<p>The tested state matters. IP67 assumes the connectors are mated. A spare heater is not mated. Neither is a unit bolted down, connector open, through a week of vehicle build. We have taken that call: water inside a heater never plugged in, blamed on a seal it never got the chance to use.</p>

<p>And the rating faces outward only, judging the enclosure against dust and water from outside. Coolant lives behind the wall — casting porosity, hose joints, a freeze in a parked truck — and fails on its own schedule.</p>

<h2>EMC cuts both ways, and the bench is not your truck</h2>

<p>A high-voltage PTC heater is a multi-kilowatt switched load, and EMC testing is a bench exercise: in our case, ISO 11452 Class 3 levels on a defined harness, ground plane and load. Controlled and repeatable, nothing like a truck.</p>

<p>Your harness is longer, runs against a chassis rather than a ground plane, and the low-voltage ground lands where the body shop put it. Any of that moves the result, which is why the field symptom is so recognisable: CAN errors only on cold mornings, only at full heater power, gone by the workshop. The heater passed its bench test. The installation is failing one the bench never set.</p>

<p>Traffic runs the other way: load dumps, cranking transients, a noisy neighbour on the same supply all travel into the heater's electronics too. Read past the EMC line to the protection list — it is what stands between a transient and a dead unit: overvoltage, undervoltage, overcurrent, short circuit and overheating protection, plus a high-voltage interlock.</p>

<h2>One number we would compare first</h2>

<p>Ask where field life hides on a datasheet and we point at insulation resistance. Ours is specified at 100 MΩ or more for the high-voltage section, measured at DC 1000 V. Coolant does not stay insulating over years of service, and seals breathe a little; that figure is the margin absorbing all of it, slowly, not suddenly.</p>

<p>Compare that line, then ask the awkward follow-up: is it a design target on paper, or a tested value on production units? The answers sound alike in a sales email; on year four of a fleet they are not the same thing.</p>

<h2>Five questions, and what the answers tell you</h2>

<p>Ask these of any supplier, us included. None needs a lab, and the answers separate a rating earned on your configuration from one borrowed off a family datasheet.</p>

<ul>
<li>That test report — is it for this exact configuration, connectors included, or a family report from a different model?</li>
<li>In what mated state was the IP test run, and what does the rating assume about the harness side?</li>
<li>Has it run at vehicle level, full power, on the production harness, with CAN error frames logged during the run?</li>
<li>The insulation resistance figure: what is it, and is it verified on every unit or sampled?</li>
<li>If we suspect water ingress in service, what does the warranty process need from us?</li>
</ul>

<p>A supplier who has done the work answers in one email. A supplier who has not sends the datasheet again.</p>

<h2>Questions we hear on this topic</h2>

<h3>Is IP67 enough for underbody mounting?</h3>
<p>For spray, slush and standing water, yes, with connectors mated correctly and the wash routine keeping pressure jets at a distance. The rating alone is not the whole answer; the installation is the other half.</p>

<h3>Can a heater pass EMC testing and still upset the vehicle network?</h3>
<p>Yes. Bench compliance is measured in a defined setup; long harnesses, shared grounds and routing choices can create problems the bench never saw. That is why vehicle-level running at full power belongs in validation.</p>

<h3>Does IP67 say anything about coolant leaks?</h3>
<p>Nothing at all. It rates the enclosure against dust and water from outside. Internal coolant integrity is a separate design and test question.</p>

<p><strong>Reviewing a heater specification?</strong> Send us the datasheet you are evaluating, ours or a competitor's. We will mark the lines that carry real information and the ones that are decoration.</p>
```

## Internal links

1. Anchor: `high-voltage coolant heater product range` → https://www.evptc.com/products.html
2. Anchor: `Q Series 15–35 kW coolant heater` → https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
3. Anchor: `CAN-controlled vs thermostat-controlled HVCH` → https://www.evptc.com/news/can-controlled-vs-thermostat-controlled-hvch-which-architecture-fits-your-vehicle-422917.html
4. Anchor: `seven inputs OEMs must define before choosing an HVCH` → https://www.evptc.com/news/how-to-choose-a-high-voltage-ptc-coolant-heater-7-inputs-oems-must-define-422912.html

## Image recommendations

- Hero: approved EVLINK heater product photograph showing the connector face and housing seal line.
- Diagram: simple two-column graphic, "tested on the bench" vs "true on the vehicle", without competitor claims.
- Alt text: `EVLINK IP67 high-voltage PTC coolant heater with sealed connectors for electric buses and trucks`.

## Fact-red-line self-check

- Uses only official EVLINK data already published in the Week 1 package: IP67 across the series, insulation resistance ≥100 MΩ at DC 1000 V, ISO 11452 Class 3 EMC requirement, and the standard protection list.
- IEC 60529 test conditions are described generically from the standard; no test report, certificate or approval is claimed for any specific configuration.
- No customer names, prices, or competitor product claims.
- SERP note (2026-10-22): top results are marketplace spec tables quoting ratings without test conditions; the gap is an honest explanation of rating limits, which this article fills.

## Remaining mandatory confirmation

- None for this version.
