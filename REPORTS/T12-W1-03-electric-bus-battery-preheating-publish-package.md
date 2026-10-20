# T12-W1-03 Publishing Package

## SEO fields

- **SEO title:** Electric Bus Battery Preheating at −30°C | EVLINK
- **Meta description:** Avoid five common mistakes when planning electric-bus battery preheating, from unplugged warm-up to incorrect heat-load and depot assumptions.
- **Primary keyword:** electric bus battery preheating
- **H1:** Electric Bus Battery Preheating at −30°C: Five Planning Mistakes
- **Recommended slug:** `electric-bus-battery-preheating-minus-30c`

## HTML body

```html
<p>At −30°C, battery preheating is not simply a request for a larger heater. A fleet must coordinate cold-soak time, battery and cabin loads, charger availability, coolant-loop conditions and the departure schedule. Missing one of these inputs can consume route energy before the bus leaves the depot.</p>

<h2>Mistake 1: starting preheating after the bus is unplugged</h2>
<p>Where the vehicle and charging system support it, preconditioning while connected allows the depot supply to cover part of the warm-up energy. The U.S. Joint Office of Energy and Transportation recommends plugged-in preconditioning to preserve battery energy for service. The exact function and interface vary by vehicle manufacturer, so this capability must be checked during procurement.</p>

<h2>Mistake 2: treating battery and cabin heating as one load</h2>
<p>The battery has its own temperature target and thermal mass. The cabin adds air leakage, glass area, defrost demand and repeated door opening. A single headline power value hides these separate loads. Define which loop is served, whether loads occur together, and which demand has priority.</p>

<h2>Mistake 3: sizing from ambient temperature alone</h2>
<p>Ambient temperature matters, but it does not determine warm-up time by itself. Engineers also need battery mass and initial temperature, the target temperature, available time, coolant volume, flow, heat losses and available high-voltage power.</p>
<p>Without these inputs, a supplier should not promise that a heater will raise a battery to a target temperature in a fixed number of minutes.</p>

<h2>Mistake 4: ignoring depot and charger limits</h2>
<p>Outdoor parking creates a different cold-soak condition from indoor storage. Charger capacity, simultaneous vehicle demand and departure waves can also limit preconditioning. A thermal plan that works for one bus may overload the depot when fifty buses request heat at the same time.</p>

<h2>Mistake 5: omitting control and fallback behaviour</h2>
<p>The design should define who requests heat, who confirms coolant flow, and what happens after communication loss, pump failure, sensor failure or overtemperature. Fleet operations also need a fallback for extreme events: extra charging time, route reserve, spare vehicles or a reduced service plan.</p>

<h2>Where a high-voltage coolant heater fits</h2>
<p>A high-voltage PTC coolant heater supplies controlled heat to the liquid loop used for battery or cabin thermal management. EVLINK’s Q Series provides a 15–35 kW selection window at 400–1100 V, with CAN communication plus enable control, IP67 protection and an official operating-temperature range of −40 to +85°C.</p>
<p>Those specifications make the Q Series a candidate for heavy-duty projects. They are not proof of a particular −30°C warm-up time. That result must be validated in the complete vehicle loop.</p>

<h2>Cold-weather validation checklist</h2>
<ul>
<li>Cold-soak temperature and duration</li>
<li>Battery initial and target temperature</li>
<li>Cabin and defrost demand</li>
<li>Plug-in power available before departure</li>
<li>Coolant, flow, pressure drop and pump strategy</li>
<li>Warm-up time and total energy consumed</li>
<li>Fault handling and repeat operation across several shifts</li>
</ul>

<p><strong>Planning a cold-climate bus?</strong> Send the cold-soak condition, pack and cabin heat-load targets, departure window, charger availability and coolant-loop data to EVLINK for an engineering preheating review.</p>
```

## Sources and internal links

- External evidence: https://driveelectric.gov/files/transit-cold-weather-help-sheet.pdf
- Research context: https://www.sciencedirect.com/science/article/pii/S1361920925002196
- `Q Series high-voltage coolant heater` → https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
- Publishing-workflow note only: link `how to choose an HVCH` to W1 article 01 after its final URL exists; do not insert a placeholder URL into production HTML.

## Image recommendations

- Depot preconditioning flow diagram showing grid/charger, battery loop and cabin loop.
- Approved Q-Series product image; no third-party fleet or customer logo.
- Alt: `electric bus battery preheating coolant loop in cold weather`.

## Fact-red-line self-check

- −30°C is a planning scenario, not an EVLINK performance claim.
- No warm-up time, range improvement or customer deployment is claimed.
- Q-Series data matches the official specification source.
- External findings are attributed and not presented as EVLINK test results.

## Remaining mandatory confirmation

- None for this version. −30°C is explicitly framed as a planning scenario, and no EVLINK cold-soak result is claimed.

