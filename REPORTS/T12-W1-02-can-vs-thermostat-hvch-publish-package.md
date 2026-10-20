# T12-W1-02 Publishing Package

## SEO fields

- **SEO title:** CAN vs Thermostat-Controlled HVCH | EVLINK
- **Meta description:** Compare CAN-controlled and thermostat-controlled high-voltage coolant heaters by integration, diagnostics, control ownership and vehicle duty.
- **Primary keyword:** CAN vs thermostat heater control
- **H1:** CAN-Controlled vs Thermostat-Controlled HVCH: Which Architecture Fits Your Vehicle?
- **Recommended slug:** `can-vs-thermostat-controlled-hvch`

## HTML body

```html
<p>Choosing between a CAN-controlled and thermostat-controlled high-voltage coolant heater is an architecture decision, not a contest between “advanced” and “basic” technology. The right answer depends on who owns the temperature target, what the vehicle must monitor, and how faults are handled.</p>

<h2>What CAN control changes</h2>
<p>In a CAN-controlled system, the vehicle controller can coordinate the heater with the battery-management system, pumps and other thermal components. Depending on the agreed interface, the vehicle may request a power level or coolant-temperature target and receive operating status and fault information.</p>
<p>This approach fits projects that need variable heat demand, vehicle-level diagnostics, event logging or coordination between battery and cabin loops. The integration work is greater: the teams must agree on message ownership, enable logic, communication-loss behaviour, signal ranges and validation cases. A CAN connector alone does not prove that two devices are software-compatible.</p>

<h2>What thermostat control simplifies</h2>
<p>A thermostat-controlled heater uses a local temperature-control method rather than relying on the vehicle network for continuous commands. It can suit an auxiliary or standalone coolant loop with a fixed target and no requirement for fleet-level diagnostic data.</p>
<p>Simpler communication does not mean that protection can be ignored. Sensor failure, overtemperature response, pump or flow interlocks and the default safe state still need to be reviewed at system level.</p>

<h2>A practical decision matrix</h2>
<table>
<thead><tr><th>Project requirement</th><th>Likely fit</th></tr></thead>
<tbody>
<tr><td>Variable heating demand coordinated by VCU or BMS</td><td>CAN control</td></tr>
<tr><td>Remote status, fault records or service diagnostics</td><td>CAN control</td></tr>
<tr><td>Several thermal components sharing one control strategy</td><td>CAN control</td></tr>
<tr><td>Independent loop with a fixed local temperature target</td><td>Thermostat control</td></tr>
<tr><td>No vehicle-network dependency required</td><td>Thermostat control</td></tr>
</tbody>
</table>

<h2>How EVLINK product families map to the choice</h2>
<p>EVLINK A, B, K, Q, H, Z and W Series coolant heaters use CAN communication plus an enable signal. Their available power and voltage windows differ, so the control choice is only one part of selection.</p>
<p>The E Series uses thermostat control without an external control interface. Its official range is 20–24 kW at 400–800 V; the unit weighs 8.5 kg and measures 370 × 192 × 98 mm. The N Series is a separate 2 kW, 200–1000 V product using a temperature sensor or switch. It should not be treated as an E-Series substitute.</p>

<h2>Questions to close before design freeze</h2>
<ul>
<li>Who owns the coolant target: VCU, BMS, thermal ECU or local controller?</li>
<li>Will the heater receive a power request, a temperature request or only enable?</li>
<li>Which voltage, current, temperature, status and fault signals are required?</li>
<li>What happens after communication loss or a temperature-sensor fault?</li>
<li>Who controls the circulation pump and verifies coolant flow?</li>
<li>Which diagnostic and validation documents must be delivered?</li>
</ul>

<h2>When an off-the-shelf interface is not enough</h2>
<p>Projects that require a custom DBC, redundant control path, special fault timing or functional-safety work products need an engineering review before the heater is released. These requirements should be visible in the RFQ, not discovered during vehicle commissioning.</p>

<p><strong>Need to select the control architecture?</strong> Send EVLINK your control-ownership diagram and required I/O list. We will confirm whether a CAN-controlled series or a standalone thermostat architecture is the cleaner fit.</p>
```

## Internal links

- `EVLINK high-voltage coolant heater range` → https://www.evptc.com/products.html
- Publishing-workflow note only: link `how to choose a high-voltage PTC coolant heater` to W1 article 01 after its final URL exists; do not insert a placeholder URL into production HTML.
- No E-Series product-page link is included because an exact verified URL is not available.

## Image recommendations

- Simple two-column control diagram: VCU/BMS–CAN–heater versus thermostat–heater.
- Approved EVLINK E-Series and one CAN-controlled product image only.
- Alt: `CAN-controlled and thermostat-controlled EV coolant heater architectures`.

## Fact-red-line self-check

- Does not claim CAN 2.0, a baud rate, DBC content, diagnostic services, thermostat limits or functional-safety level.
- Uses official family control methods and E/N dimensions only.
- Does not describe thermostat control as inherently less safe.

## Remaining mandatory confirmation

- None for this version. No thermostat setpoint range, protocol detail or unverified E-Series URL is published.

