# DAILY-HVCH-1022 — Low-Voltage Supply and Wake-Up Review Draft
Owner: Codex. Delivered 2026-10-22 as an overdue manuscript, not a published article.
Current disposition (2026-10-22 evening): REWORK, DO NOT PUBLISH. Muse fixed-full-text test: ZeroGPT 62.6% FAIL; GPTZero AI 100% / Mixed 0% / Human 0% (reference only). Actual featured image delivered; this text remains a failed version, not final accepted delivery.

## SEO fields
- H1 / SEO title: HVCH Not Starting? Check Low-Voltage Supply and Wake-Up
- Primary keyword: high voltage coolant heater not starting
- Supporting terms: HVCH low voltage supply; coolant heater wake-up; heater enable conditions
- Proposed slug (not live): hvch-low-voltage-supply-wake-up-checks
- Meta: A high-voltage coolant heater may need a separate control supply and defined wake-up conditions. Build a model-specific evidence record before diagnosing a no-start.
- Audience: commercial-EV integration/service engineers, international English; demand and country volume unknown.
- Scope: low-voltage/control evidence, not a live high-voltage testing procedure, generic CAN tutorial or insulation-test guide.

## HTML body
```html
<p>If a high-voltage coolant heater does not start, high-voltage availability is only one part of the investigation. The selected unit may also depend on a separate control supply, a wake-up input, valid messages and other enable conditions. Begin with the exact heater documentation rather than assuming every HVCH starts in the same way.</p>

<h2>Identify the variant before reading the fault</h2>
<p>Record the part number, hardware revision, software version and interface-document revision. Confirm which supply powers the electronics and how the unit is expected to leave its sleep state. A CAN-controlled heater and a thermostat-controlled heater do not offer the same commands or diagnostic information.</p>
<p>Some manufacturers publish separate high-voltage and low-voltage ratings. That establishes why both interfaces need review; it does not make another supplier's supply range valid for an EVLINK unit. Use the approved drawing and limits for your selected variant.</p>

<h2>Distinguish three questions</h2>
<p>First, was the specified control supply available at the relevant time? Second, did the heater reach the documented awake or ready state? Third, were the conditions for heating satisfied? A “no heat” report does not say which of these failed.</p>
<p>A vehicle-controller log showing an enable request is useful, but it is not proof that the heater received or accepted it. Compare the request with the unit's documented feedback where that interface provides feedback. If it does not, agree an alternative observation with the supplier instead of inventing a ready-state signal.</p>

<h2>Capture the supply during the event</h2>
<p>A supply reading taken after the event may not explain an intermittent start problem. Ask the responsible electrical engineer to define the approved measurement point and capture method for the control supply and return during wake-up. Include relevant events from other vehicle loads if they occur at the same time.</p>
<p>This is not permission for unqualified live testing. High-voltage isolation, access and measurement must follow the vehicle manufacturer's procedures and local requirements. Do not bridge an interlock, force a power stage on or use an assumed pinout to see whether the heater runs.</p>

<h2>Check the wake-up definition, not a familiar pattern</h2>
<p>Use the interface specification to establish whether wake-up depends on an input, a network event, an ignition state or another defined condition. Record the required sequence and timing from that document. Do not import a delay, baud rate or message identifier from a similar-looking heater.</p>
<p>If the selected model uses communication commands, check the relevant protocol fields and version. If it uses thermostat or switched control, follow that architecture instead. A missing CAN response is not a useful fault finding on a unit that has no CAN interface.</p>

<h2>Review inhibits before replacing the heater</h2>
<p>A unit may be awake without being permitted to heat. Its documentation determines which conditions can inhibit operation and how they are reported. Supply limits, temperature limits, interlocks and other protections should be reviewed only where they actually apply to the variant.</p>
<p>Preserve the reported fault state before clearing anything. Repeated resets can remove useful event information and are not a substitute for diagnosing the cause. The responsible engineer should decide the next test from the available evidence and approved service instructions.</p>

<h2>Prepare one time-aligned evidence package</h2>
<ul>
<li>Exact heater identity and the document versions used for interpretation.</li>
<li>Requested operation and the vehicle state immediately before the failed start.</li>
<li>Approved control-supply observation, with measurement location and instrument stated.</li>
<li>Wake-up or enable input as defined for that model, not an assumed generic signal.</li>
<li>Available heater states, diagnostics and relevant vehicle-controller events.</li>
<li>Changes between successful and unsuccessful attempts, including software or harness work.</li>
</ul>
<p>Keep successful and failed attempts under comparable conditions where possible. If an event was not captured, mark it missing. A hypothesis such as a supply interruption remains provisional until the recorded evidence supports it.</p>

<h2>What counts as a resolved issue?</h2>
<p>Agree acceptance criteria before the corrective test. Confirm the documented wake-up and shutdown behaviour and the required heating response under the approved conditions. Save the final configuration with the logs so the result can be repeated. One successful restart after an unexplained fault is not the same as a verified repair.</p>
<p>For broader command mapping, use the separate <a href="https://evbtms.com/hvch-can-integration-oem-checklist/">HVCH CAN integration checklist</a>; for product selection, review the <a href="https://evbtms.com/products/high-voltage-coolant-heater/">high-voltage coolant heater range</a>. Neither replaces the interface documentation for the actual part.</p>

<h2>Ask for a model-specific review</h2>
<p><a href="https://evbtms.com/contact/">Send EVLINK the heater identity, interface revision and available event record</a>. State which observations are confirmed and which are still assumptions. That gives the supplier a defined question to review without disguising a wiring, control or operating-condition issue as a proven product failure.</p>
```

## Sources and claim boundaries
- Manufacturer example of separate HV/LV ratings, not EVLINK specifications: https://www.webasto.com/en-us/heating/high-voltage-heaters/800v-hvh.html
- EVLINK interface distinction: repository REPORTS/evptc-official-spec-summary.md (B/Q CAN; E thermostat/no CAN; model-level confirmation still required).
- Existing CAN article is a supporting page, not copied text.
- No model-specific voltage range, pinout, CAN identifier, timeout, safety compliance or successful customer repair claimed. Checklist is an editorial evidence method.

## Editorial and image packet
- Featured image brief: authorised real EVLINK heater photograph beside a clean schematic separating power supply from control supply/interface. The schematic must not imply a real pinout.
- Text: “HVCH Start-Up Review / Supply • Wake-Up • Enable”.
- Alt: EVLINK high-voltage coolant heater with a generic power and control interface schematic.
- Actual image delivered: REPORTS/assets/daily-2026-10-22/hvch-start-up-review-feature.webp (1199×675; 61,158 bytes), an AI-assisted application illustration based on an existing product visual.
- Duplicate check: existing CAN, power-verification, insulation and warm-up themes reviewed in repository. No complete live title inventory obtained; WP REST refused connection. If an existing no-start article owns this task, use as an update, not a second URL.
- Research: general web search, not verified country/device-specific top-five Google SERP; demand unknown. Stage 3 remains pending. Editorial candidate, not nine-gate-approved publication.
- Muse fixed-full-text result: ZeroGPT 62.6% FAIL; GPTZero AI 100% / Mixed 0% / Human 0% (reference only), per REPORTS/detection-two-daily-1022-muse-results.md. This failed version is not publication-ready.
- Peter reviews and publishes; no production edit performed.
