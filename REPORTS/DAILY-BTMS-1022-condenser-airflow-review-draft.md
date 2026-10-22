# DAILY-BTMS-1022 — Condenser Airflow Review Draft
Owner: Codex. Delivered 2026-10-22 as an overdue manuscript, not a published article.
Status: complete text/SEO/HTML draft; not final accepted delivery. AI test, actual featured image, full-site duplicate check and reproducible country-specific SERP remain pending.

## SEO fields
- H1 / SEO title: BTMS Condenser Airflow: An Installation Review Checklist
- Primary keyword: BTMS condenser airflow
- Supporting terms: battery thermal management cooling; condenser air recirculation; electric truck BTMS installation
- Proposed slug (not a live URL): btms-condenser-airflow-installation-checklist
- Meta: Check the condenser air path before judging BTMS cooling capacity. Review inlet conditions, recirculation, fan operation and evidence for vehicle integration.
- Audience: commercial-EV integration engineers; English-language international B2B. Country demand/volume: unknown, not measured.
- Scope: a practical inspection record, not EVLINK performance results or a replacement for the unit installation manual.

## HTML body
```html
<p>If a battery thermal management system cools acceptably on a bench but struggles after installation, check the condenser air path before ordering a larger unit. A fan can be running while the condenser is drawing restricted or already-heated air. This review is for an air-cooled condenser in a refrigerant-based BTMS; it does not apply unchanged to a liquid-cooled condenser.</p>

<h2>Define the air the unit actually receives</h2>
<p>Record both surrounding ambient temperature and air temperature at the condenser inlet. They are not automatically the same measurement. An inlet beside another heat source, inside a restricted enclosure or close to its own discharge needs attention before catalogue capacity can be compared with vehicle performance.</p>
<p>Ask for the installation drawing, intended airflow direction, service clearances and operating conditions used for the supplier's capacity data. Do not borrow a clearance or airspeed value from a different model. A controller's local cooling-air requirement is also not automatically the condenser's required airflow.</p>

<h2>Inspect the complete path, not just the fan</h2>
<p>Trace where air enters the vehicle enclosure, how it crosses the condenser and where it leaves. Include grilles, guards, ducts and body panels. Photograph the installed arrangement with the panels in their normal operating positions. An open workshop panel can conceal a restriction that returns when the vehicle is reassembled.</p>
<p>Look for a route that lets discharge air return to the inlet. Check nearby surfaces and the effect of other cooling fans. Danfoss identifies restricted flow, incorrect direction and air recirculation among the possible contributors to high condensing pressure. Those are general refrigeration checks, not a diagnosis of any particular EVLINK installation.</p>

<h2>Separate a command from a physical response</h2>
<p>A fan command in a log proves that a command was issued. It does not prove the required airflow reached the coil. Compare the requested state with the available feedback, observed direction and the actual air path. Follow the equipment manual when interpreting speed or fault signals.</p>
<p>Any work near rotating fans, electrical equipment or the refrigerant circuit belongs to trained personnel under the vehicle's approved safety procedures. Do not bypass pressure protection, remove guards during operation or open the refrigerant circuit simply to complete an airflow checklist.</p>

<h2>Build a useful evidence record</h2>
<p>Before changing the installation, agree which measurements will answer the question. A useful record keeps the following information together:</p>
<ul>
<li>BTMS model, configuration, software version and installation drawing revision.</li>
<li>Vehicle state: stationary or moving, operating load and other thermal systems running.</li>
<li>Ambient and condenser-inlet temperatures, with measurement positions identified.</li>
<li>Fan request, available feedback and observed airflow direction.</li>
<li>Coolant inlet/outlet temperatures and flow, where approved measurements are available.</li>
<li>Relevant controller limits, alarms and the time each event occurred.</li>
<li>Photos showing grilles, ducting, service panels and nearby heat sources.</li>
</ul>
<p>Synchronise the records so a change in a command can be compared with the measured response. Missing channels should be marked unavailable. A single photograph or temperature difference cannot establish airflow volume or cooling capacity by itself.</p>

<h2>Compare changes under controlled conditions</h2>
<p>Change one installation variable at a time where practical, and document what changed. Keep the starting state and load comparable. If the weather or battery load changes between runs, record that difference rather than attributing the entire result to the duct modification.</p>
<p>Agree the acceptance criteria with the responsible engineer before testing. This article gives no universal passing temperature, pressure, airspeed or percentage improvement. Supplier requirements and vehicle limits determine the decision.</p>

<h2>Know when the airflow check is not enough</h2>
<p>An airflow concern is one possible explanation, not the final answer. If the documented air path meets its requirements and the issue remains, the investigation may need to examine sensors, refrigerant-side operation, controls or the load assumption. Use the equipment's diagnostic procedure rather than repeatedly increasing fan demand.</p>
<p>Our <a href="https://evbtms.com/products/battery-thermal-management-system/">battery thermal management system range</a> is a starting point for a model-specific discussion. For the distinction between the liquid and refrigeration sides, see <a href="https://evbtms.com/btms-refrigerant-circuit-vs-coolant-loop/">BTMS refrigerant circuit versus coolant loop</a>.</p>

<h2>Send the installation evidence with the enquiry</h2>
<p>When you <a href="https://evbtms.com/contact/">contact EVLINK about a BTMS installation</a>, include the unit model, vehicle duty, drawing, inlet conditions and available logs. If those data are not yet available, say so. The next step is to agree the review scope, not to invent missing measurements or promise a capacity increase.</p>
```

## Sources and claim boundaries
- General refrigeration fault possibilities only: https://reftools.danfoss.com/tools/cooling/troubleshooter/system-areas/high-pressure/system/condensing-pressure-too-high/air-cooled-condensers/
- Scope distinction/current product context: https://evbtms.com/products/battery-thermal-management-system/12kw/
- Public-source check: 2026-10-22. No EVLINK test data, customer experience, capacity improvement or universal design threshold claimed. Evidence-record structure is an editorial review method, not an industry certification.

## Editorial and image packet
- Featured image brief: existing authorised real BTMS product photograph, with a separate simple inlet/discharge arrow diagram; do not alter the real product's construction.
- Suggested image text: “BTMS Condenser Airflow / Review the Installed Air Path”.
- Alt: EVLINK BTMS unit with a schematic showing condenser inlet and discharge air paths.
- Actual image file: not yet delivered. No external competitor image reused.
- Internal links are embedded; target live status/preview not verified this round.
- Duplicate review: repository pipeline/title review and indexed query checked; public WP REST connection refused. This is NOT full-site duplicate clearance. If an existing condenser-airflow draft owns this intent, merge this manuscript into it rather than create another URL.
- Research: general web query, not a verified US/UK top-five Google SERP. No search volume reported. Stage 3 still pending; this is an editorial candidate, not a nine-gate-approved publication.
- ZeroGPT: NOT TESTED; GPTZero: NOT TESTED. Final text must meet Peter's recorded ZeroGPT <=30% gate, with report/screenshot. Do not reuse another draft's score.
- Publication: Peter final review and release only. No WordPress change performed.
