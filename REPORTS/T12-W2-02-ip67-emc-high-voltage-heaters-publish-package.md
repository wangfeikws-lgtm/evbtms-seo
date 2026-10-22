# T12-W2-02 Publishing Package

## SEO fields

- **SEO title:** IP67 and EMC in High-Voltage Heaters: What the Spec Sheet Doesn't Tell You | EVLINK
- **Meta description:** IP67 and an EMC pass are real ratings with narrow test conditions. Here is what they cover, what they miss, and the questions to ask any HVCH supplier before design freeze.
- **Primary keyword:** IP67 EMC high voltage heater
- **H1:** IP67 and EMC in High-Voltage Heaters: What the Spec Sheet Doesn't Tell You
- **Recommended slug:** `ip67-emc-high-voltage-heaters-spec-sheet`

## HTML body

```html
<p>If a high-voltage heater datasheet lists IP67 and an EMC result, ask which configuration and test conditions those entries cover. They are useful starting points, not a substitute for checking the installed vehicle.</p>

<p>For an EVLINK quotation, request the requirements and available reports for the exact heater variant, connector arrangement and software version. A family-level description must not be presented as a certificate for every configuration.</p>

<h2>What the IP67 designation describes</h2>

<p>IP67 is an enclosure-protection designation under IEC 60529: the first digit concerns solid-particle ingress and the second concerns water ingress under specified conditions. Obtain the applicable test report for the detailed setup, duration, immersion conditions and acceptance criteria. Do not turn a rating into an unrestricted waterproofing guarantee.</p>

<p>Now read what the test does not say.</p>

<h2>Four things IP67 does not cover</h2>

<p><strong>Pressure washing.</strong> Temporary immersion testing is not the same as high-pressure or hot-water cleaning. Check the applicable vehicle cleaning requirement and corresponding test evidence rather than inferring jet resistance from an IP67 entry.</p>

<p><strong>Age.</strong> The rating describes a new unit with new seals. Five winters of thermal cycling between −40°C starts and hot coolant, plus vibration, plus one careless harness pull during a pump replacement, is a different unit. Seal material and connector design decide how much of the rating survives year five.</p>

<p><strong>The unmated state.</strong> An open connector may be outside the tested configuration. Define protection during transport, storage, assembly and service as well as during normal vehicle operation.</p>

<p><strong>The inside.</strong> IP ratings describe the enclosure against the outside world. They say nothing about the coolant circuit inside it: casting porosity, hose joints and freeze damage live on the other side of the wall and fail on their own schedule.</p>

<h2>EMC: the heater is a suspect, not just a victim</h2>

<p>A high-voltage PTC heater is a multi-kilowatt switched electrical load. Treating EMC as a box it passed once misses the point twice over. The heater must not disturb the vehicle, and the vehicle must not disturb the heater.</p>

<p>An EMC statement needs the exact standard and part, test method, severity, frequency range, operating mode and acceptance criteria. The shorthand “ISO 11452 Class 3” in a summary is not enough to establish a complete test requirement or a vehicle approval. Installation validation should consider production harness routing, grounding and network behaviour.</p>

<p>The reverse direction matters too. Load dumps, cranking transients and a noisy neighbour on the same supply can push disturbances into the heater's electronics. This is why the protection list deserves as much reading as the EMC line: overvoltage, undervoltage, overcurrent, short circuit and overheating protection, plus a high-voltage interlock, are what stand between a transient and a dead heater.</p>

<h2>The quiet line that predicts field life</h2>

<p>Insulation resistance is a separate electrical requirement, not a lifetime forecast. EVLINK's specification summary lists at least 100 MΩ at DC 1000 V for the high-voltage section of the applicable heater families, with E and N excluded from that blanket summary. Confirm the selected model, test points, method and production inspection plan with the supplier; do not apply a test voltage without an approved procedure.</p>

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
<p>Not from the rating alone. Assess mounting location, connector condition, cleaning, vibration, temperature cycling and the relevant vehicle requirements. Accept the installation against its documented test plan, not a general promise about underbody use.</p>

<h3>Can a heater pass EMC testing and still upset the vehicle network?</h3>
<p>Yes. Bench compliance is measured in a defined setup. Long harnesses, shared grounds and routing choices on the vehicle can create problems the bench never saw, which is why vehicle-level running at full power belongs in validation.</p>

<h3>Does IP67 say anything about coolant leaks?</h3>
<p>Nothing at all. It rates the enclosure against dust and water from outside. Internal coolant integrity is a separate design and test question.</p>

<p>Reviewing a heater specification? Send the selected model, mounting environment, electrical interfaces and applicable project requirements. EVLINK can identify the corresponding product information and clarify which supporting reports are available.</p>
<h2>Related selection resources</h2>
<ul>
<li><a href="https://www.evptc.com/products.html">high-voltage coolant heater product range</a></li>
<li><a href="https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html">Q Series 15–35 kW coolant heater</a></li>
<li><a href="https://www.evptc.com/news/can-controlled-vs-thermostat-controlled-hvch-which-architecture-fits-your-vehicle-422917.html">CAN-controlled vs thermostat-controlled HVCH</a></li>
<li><a href="https://www.evptc.com/news/how-to-choose-a-high-voltage-ptc-coolant-heater-7-inputs-oems-must-define-422912.html">seven inputs OEMs must define before choosing an HVCH</a></li>
</ul>
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

## Technical reference

- IEC, IEC 60529 enclosure-protection classification: https://webstore.iec.ch/en/publication/2447 . This reference establishes the scope of the IP code, not certification of an EVLINK product or a substitute for the purchased standard and test report.

## Review status — 2026-10-22

- Peter approved this article direction on 2026-10-22. Editorial revision by Codex; not a publication approval.
- Removed or qualified unsupported case histories, generalised product claims and unreferenced numerical performance/cost claims. Product data must be confirmed for the selected variant.
- Four actual HTML internal links included from the repository's published inventory. Targets have not received a fresh live HTTP check this round.
- SERP research in the earlier draft lacked reproducible query/location/result evidence; no verified search-volume or ranking claim is made. This remains an acceptance item.
- Featured-image recommendations are not an image delivery. Actual approved photo and finished image remain pending.
- Final revised text has NOT been tested in ZeroGPT/GPTZero. Do not reuse any earlier version's score. Required recorded threshold: ZeroGPT <=30%; GPTZero reference only.
- Status: revised draft, pending technical review, actual images, detector results and Peter's final review. Do not publish.
