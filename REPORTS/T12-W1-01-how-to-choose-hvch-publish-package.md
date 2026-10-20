# T12-W1-01 Publishing Package

## SEO fields

- **SEO title:** How to Choose a High-Voltage PTC Coolant Heater | EVLINK
- **Meta description:** Define heat load, voltage, control, coolant, duty cycle, packaging and safety requirements before choosing an HVCH for an electric bus or truck.
- **Primary keyword:** how to choose high voltage coolant heater
- **H1:** How to Choose a High-Voltage PTC Coolant Heater: 7 Inputs OEMs Must Define
- **Recommended slug:** `how-to-choose-high-voltage-ptc-coolant-heater`

## HTML body

```html
<p>A high-voltage coolant heater should not be selected from a power number alone. A unit labelled 18 kW or 35 kW may still be the wrong choice if its voltage window, control interface, coolant conditions or mounting envelope do not match the vehicle.</p>

<p>For an electric bus or truck project, we recommend defining seven engineering inputs before comparing heater models. This turns the discussion from “Which heater is biggest?” into “Which configuration fits the thermal system and can be validated?”</p>

<h2>1. Required heat load and warm-up target</h2>

<p>Start with the job the heater must perform. Is it heating the traction battery, the passenger cabin, or both? What are the starting coolant temperature, target temperature and allowed warm-up time? A city bus with frequent door opening does not have the same load profile as a truck battery loop.</p>

<p>Do not treat rated heater power as the heat load calculation. Vehicle mass, cabin leakage, battery thermal mass, coolant volume, piping losses and ambient conditions all affect the result. If these inputs are not available, the responsible answer is to request them rather than promise a warm-up time.</p>

<h2>2. High-voltage and low-voltage architecture</h2>

<p>Provide the minimum, nominal and maximum high-voltage bus values, not only the nominal voltage. Also define the low-voltage supply used for control electronics. A heater must remain inside its approved electrical window throughout normal operation, charging and transient conditions.</p>

<p>As an initial EVLINK shortlist, the A Series covers 6–18 kW at 400–800 V, while the Q Series covers 15–35 kW at 400–1100 V. These ranges help narrow the discussion; they do not replace a project review.</p>

<h2>3. Control and diagnostic requirements</h2>

<p>Most vehicle projects need more than an on/off command. Define who owns the coolant-temperature target, whether the vehicle requests power or temperature, which operating values must be returned, and how faults are handled.</p>

<p>EVLINK A and Q Series heaters use CAN communication plus an enable signal. The exact message set, timing and diagnostic requirements must be agreed for the vehicle. If the project needs a standalone temperature-control architecture instead, that should be stated at the beginning because it changes the suitable product family.</p>

<h2>4. Coolant-loop conditions</h2>

<p>A useful request for quotation includes coolant type and concentration, inlet-temperature range, target outlet temperature, flow range, allowable pressure drop and system pressure. These values determine whether heat can be transferred safely and consistently.</p>

<p>They also prevent a common integration error: specifying enough electrical power but not enough coolant flow to remove the heat from the unit. Flow detection, pump control and low-flow fault handling should be part of the system review.</p>

<h2>5. Duty cycle and environment</h2>

<p>Describe continuous versus intermittent operation, cold-soak duration, expected ambient-temperature range and daily operating hours. A heater selected for a short preheating event may not be suitable for continuous cabin heating without confirming the complete duty cycle.</p>

<p>EVLINK’s official range for these coolant-heater families includes an operating temperature of −40 to +85°C and IP67 protection. These are product boundaries, not a promise that every vehicle will achieve its target warm-up time at −40°C.</p>

<h2>6. Packaging and connectors</h2>

<p>Send a 3D envelope or at least the available length, width and height, mounting orientation, hose direction and service-clearance requirement. The A Series is 350 × 184 × 120 mm and weighs 5.1 kg. The Q Series is 346 × 268 × 123 mm and weighs 12 kg.</p>

<p>Connector selection matters as much as physical size. For the A Series, available project variants include Amphenol, AVIC and flying-lead configurations. Connector naming and pin definitions should be confirmed on the project drawing before release.</p>

<h2>7. Protection, EMC and documentation</h2>

<p>Define the vehicle’s protection, EMC and documentation requirements before design freeze. EVLINK’s official specification includes insulation resistance of at least 100 MΩ for the high-voltage section at DC 1000 V, IP67 protection, EMC compliance with ISO 11452 Class 3 requirements, and protection against overvoltage, undervoltage, overcurrent, short circuit and overheating.</p>

<p>Certification and test documents should be matched to the exact project configuration. A family-level statement or laboratory activity is not a substitute for the certificate, report or validation evidence required by an OEM.</p>

<h2>A practical HVCH RFQ checklist</h2>

<ul>
  <li>Vehicle type and heating application</li>
  <li>Calculated heat load and required warm-up time</li>
  <li>HV minimum, nominal and maximum voltage</li>
  <li>Low-voltage supply</li>
  <li>Coolant type, inlet temperature, flow and pressure limits</li>
  <li>Ambient range and duty cycle</li>
  <li>CAN, enable, feedback and diagnostic requirements</li>
  <li>Installation envelope, mounting orientation and connectors</li>
  <li>Validation standards and required documents</li>
</ul>

<p><strong>Need an engineering shortlist?</strong> Send these seven application inputs to EVLINK. We will identify the suitable series and the missing validation questions instead of guessing from kW alone.</p>
```

## Internal links

1. Anchor: `high-voltage coolant heater product range` → https://www.evptc.com/products.html
2. Anchor: `Q Series 15–35 kW coolant heater` → https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
3. Publishing-workflow note only: add a reciprocal contextual link from the existing HVCH working-principle article after its exact URL is verified; do not insert a placeholder URL into production HTML.

## Image recommendations

- Hero: approved EVLINK A-Series or Q-Series product photograph on a clean white background; do not use an unverified third-party render.
- Diagram: seven-input selection flow, created from the article checklist without performance claims.
- Alt text: `EVLINK high-voltage PTC coolant heater for electric bus and truck integration`.

## Fact-red-line self-check

- Uses only official A/Q power, voltage, size, weight, control, IP, operating-temperature, insulation, EMC and protection data.
- Does not publish efficiency, coolant flow, pressure drop, warm-up time, service life, MOQ, lead time or customer claims.
- Does not resolve the QA01 naming conflict; the article uses A Series and Q Series only.
- Certification documents are described as configuration-specific and subject to verification.

## Remaining mandatory confirmation

- None for this version. Certification names and the conflicting Geely/QA01 product-page link are intentionally excluded from the publishable HTML.
