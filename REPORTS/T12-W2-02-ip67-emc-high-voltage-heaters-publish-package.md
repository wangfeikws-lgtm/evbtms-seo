# T12-W2-02 Publishing Package

## SEO fields

- **SEO title:** IP67 and EMC in High-Voltage Heaters: What the Spec Sheet Doesn't Tell You | EVLINK
- **Meta description:** IP67 and an EMC pass are real ratings with narrow test conditions. Here is what they cover, what they miss, and the questions to ask any HVCH supplier before design freeze.
- **Primary keyword:** IP67 EMC high voltage heater
- **H1:** IP67 and EMC in High-Voltage Heaters: What the Spec Sheet Doesn't Tell You
- **Recommended slug:** `ip67-emc-high-voltage-heaters-spec-sheet`

## HTML body

```html
<p>Two lines on every high-voltage heater datasheet are meant to close the conversation: IP67, and EMC passed. Both ratings are real. Both are also narrower than most buyers assume, and the gap between the test bench and a truck in February is where winter failures are born.</p>

<p>We build heaters that carry these ratings, across our A, E, H and Q series. That is exactly why we would rather explain their limits than hide behind them.</p>

<h2>What IP67 actually certifies</h2>

<p>IP67 comes from IEC 60529. The 6 means dust-tight. The 7 means the unit survived immersion in clean water, one metre deep, for thirty minutes, in a laboratory, as a new unit, with its connectors mated the way the test setup specifies. That is a genuinely useful test. A heater that passes it will shrug off road spray, slush and the general filth of life under a vehicle floor.</p>

<p>Now read what the test does not say.</p>

<h2>Four things IP67 does not cover</h2>

<p><strong>Pressure washing.</strong> Immersion is static and gentle. A steam lance or a high-pressure jet at close range is a different attack entirely; that territory belongs to IP69K ratings, and an IP67 line on a datasheet says nothing about it. Depots wash trucks hard. Ask where the heater may sit relative to the wash routine.</p>

<p><strong>Age.</strong> The rating describes a new unit with new seals. Five winters of thermal cycling between −40°C starts and hot coolant, plus vibration, plus one careless harness pull during a pump replacement, is a different unit. Seal material and connector design decide how much of the rating survives year five.</p>

<p><strong>The unmated state.</strong> A spare heater on a warehouse shelf, or a connector left open during a vehicle build, is not in its tested condition. We have seen water ingress blamed on a heater that was open to the weather for a week before it was ever bolted down.</p>

<p><strong>The inside.</strong> IP ratings describe the enclosure against the outside world. They say nothing about the coolant circuit inside it: casting porosity, hose joints and freeze damage live on the other side of the wall and fail on their own schedule.</p>

<h2>EMC: the heater is a suspect, not just a victim</h2>

<p>A high-voltage PTC heater is a multi-kilowatt switched electrical load. Treating EMC as a box it passed once misses the point twice over. The heater must not disturb the vehicle, and the vehicle must not disturb the heater.</p>

<p>Component testing follows defined methods, in our case the specification calls for ISO 11452 Class 3 levels, with a defined harness, a defined ground plane and a defined load. Your vehicle has none of those. Harness length, routing against the chassis, and where the low-voltage ground lands all move the result. The classic field symptom is CAN errors that appear only on cold mornings at full heater power, then vanish in the workshop. The heater passed its bench test. The installation failed its own.</p>

<p>The reverse direction matters too. Load dumps, cranking transients and a noisy neighbour on the same supply can push disturbances into the heater's electronics. This is why the protection list deserves as much reading as the EMC line: overvoltage, undervoltage, overcurrent, short circuit and overheating protection, plus a high-voltage interlock, are what stand between a transient and a dead heater.</p>

<h2>The quiet line that predicts field life</h2>

<p>If one number on our datasheet predicts how a heater ages, it is insulation resistance: at least 100 MΩ for the high-voltage section, measured at DC 1000 V. Coolant is conductive enough over time, seals breathe, and the insulation figure is the margin that absorbs all of it. When you compare suppliers, compare that line, and ask whether it is a design target or a tested value on production units.</p>

<h2>Questions to ask any supplier, including us</h2>

<ul>
<li>Is there a test report for this exact configuration, connectors included, or a family report from a different model?</li>
<li>In what mated state was the IP test run, and what does the rating assume about the harness side?</li>
<li>Has the heater run at vehicle level, full power, with the production harness, and were CAN error frames logged during the test?</li>
<li>What is the insulation resistance specification, and is it verified on every unit or sampled?</li>
<li>What does the warranty process need from us when an ingress failure is suspected?</li>
</ul>

<p>None of these questions is hostile. A supplier who has done the work answers them in one email. A supplier who has not will send you the datasheet again.</p>

<h2>Questions we hear on this topic</h2>

<h3>Is IP67 enough for underbody mounting?</h3>
<p>For spray, slush and standing water, yes, provided the connectors are mated correctly and the wash routine keeps pressure jets at a sensible distance. The rating alone is not the whole answer; the installation is the other half.</p>

<h3>Can a heater pass EMC testing and still upset the vehicle network?</h3>
<p>Yes. Bench compliance is measured in a defined setup. Long harnesses, shared grounds and routing choices on the vehicle can create problems the bench never saw, which is why vehicle-level running at full power belongs in validation.</p>

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
