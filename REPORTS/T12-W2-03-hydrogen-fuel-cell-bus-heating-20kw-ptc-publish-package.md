# T12-W2-03 Publishing Package

## SEO fields

- **SEO title:** Hydrogen Fuel Cell Bus Heating: Evaluating a 20 kW Class PTC Heater | EVLINK
- **Meta description:** A fuel cell stack makes heat, just never when the cabin needs it most. Why hydrogen buses pair waste-heat recovery with a 20 kW class PTC coolant heater, and what to specify.
- **Primary keyword:** hydrogen bus heater
- **H1:** Hydrogen Fuel Cell Bus Heating: Evaluating a 20 kW Class PTC Heater
- **Recommended slug:** `hydrogen-fuel-cell-bus-heating-20kw-ptc`

## HTML body

```html
<p>If a hydrogen fuel cell bus needs auxiliary cabin heating, a 20 kW class PTC coolant heater may be one candidate. Its suitability depends on cold-start demand, cabin and defrost loads, usable stack heat and available electrical power. Twenty kilowatts is a sizing option, not an industry-wide answer.</p>

<p>Waste-heat recovery and an auxiliary heater can serve different parts of the duty cycle. Establish how much heat is available at the required coolant temperature and when it becomes available. This article does not describe a particular fleet or claim an EVLINK customer installation.</p>

<h2>Problem one: the heat arrives late</h2>

<p>A diesel engine is a furnace that also turns wheels; most of its fuel becomes heat, and coolant leaves it hot. A PEM fuel cell is far more efficient, which is the point of it, and its coolant typically runs far cooler than diesel coolant. Worse, at a cold start the stack is a cold mass that needs warming itself before it can work hard. For the first minutes of a winter morning, the fuel cell is a heating load, not a heat source.</p>

<p>Passengers do not board in the first minutes after the stack reaches steady state. They board at departure. The cabin, the windscreen and the driver all need heat at exactly the moment the stack has none to spare.</p>

<h2>Problem two: the heat disappears at low load</h2>

<p>At low stack load, the heat available for recovery can differ from that at cruise. Evaluate depot preparation, stops and low-speed service separately, using the stack supplier's thermal data and the vehicle operating profile. A study on another bus cannot establish the auxiliary demand for your platform.</p>

<p>Size the heating system for the cruise condition and it fails at the terminus. Size it for the terminus and you have specified a PTC heater.</p>

<h2>Why the number lands near 20 kW</h2>

<p>Build the load estimate from cabin heat loss, ventilation, door operation, defrost and the required warm-up time. Subtract only the recoverable stack heat that is available under the same operating conditions. Select the auxiliary heater against that remaining demand, including the project's agreed margin.</p>

<p>EVLINK's official summary lists both B and E Series at 20–24 kW and 400–800 V, but their interfaces differ. B Series is listed with CAN control; E Series uses thermostat control without CAN or an external command interface. Do not choose E Series for a CAN-controlled architecture without first resolving that mismatch. Q Series is listed at 15–35 kW and 400–1100 V for evaluation where appropriate.</p>

<h2>The detail that catches projects out: the water</h2>

<p>Use the stack supplier's approved coolant and conductivity requirements. Do not assume that ordinary vehicle coolant is acceptable in the stack circuit, or that every stack uses the same fluid formulation. Where fluid or temperature requirements differ, assess a separated circuit and heat exchanger. Document which controller owns each pump, valve and heat request.</p>

<p>Decide that on paper. Deciding it during winter validation costs a season.</p>

<h2>What we would specify</h2>

<p>Specify the lowest service temperature, cabin target, defrost duty, usable waste heat, coolant requirements and voltage range before selecting power. Choose the control interface deliberately: a vehicle-commanded system needs a compatible variant and documented communication interface. Validate cold start, low-load service, transitions and agreed fault responses on the actual architecture.</p>

<h2>Questions we hear on this topic</h2>

<h3>Can stack waste heat ever be enough on its own?</h3>
<p>Possibly, under some operating conditions. The engineering question is whether it meets every required mode, including cold start and low-load service. Determine auxiliary heating from that assessment rather than assuming a PTC heater can always be deleted or is always mandatory.</p>

<h3>Why not fit a fuel-fired parking heater instead?</h3>
<p>Compare permitted energy sources, vehicle objectives, installation requirements and local operating rules. This article makes no blanket regulatory claim about fuel-fired heaters. A project requiring no onboard combustion should evaluate electric heating and its energy supply accordingly.</p>

<h3>Does a 20 kW heater hurt the bus's range?</h3>
<p>It draws real energy, and on a hydrogen bus that energy ultimately comes from hydrogen or the buffer battery. The alternative is not zero consumption; it is a cold cabin, a fogged windscreen and a vehicle that cannot enter service. Energy management, preconditioning at the depot and waste-heat blending keep the cost honest.</p>

<p><strong>Specifying a fuel cell bus for cold service?</strong> Send us the bus length, the coldest operating condition, the defrost requirement and the stack coolant architecture. We will size the heater and flag the loop questions before they reach winter testing.</p>
<h2>Related selection resources</h2>
<ul>
<li><a href="https://www.evptc.com/products.html">high-voltage coolant heater product range</a></li>
<li><a href="https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html">Q Series 15–35 kW coolant heater</a></li>
<li><a href="https://www.evptc.com/news/why-electric-bus-range-falls-in-winter-and-five-levers-fleets-can-control-422923.html">why electric bus range falls in winter</a></li>
<li><a href="https://www.evptc.com/news/electric-bus-battery-preheating-at-30c-five-planning-mistakes-422919.html">electric bus battery preheating at −30°C</a></li>
</ul>
```

## Internal links

1. Anchor: `high-voltage coolant heater product range` → https://www.evptc.com/products.html
2. Anchor: `Q Series 15–35 kW coolant heater` → https://www.evptc.com/sale-40723397-high-voltage-ptc-water-heater-15-35kw-400-1100v-for-electric-vehicles-ev-battery-thermal-management-.html
3. Anchor: `why electric bus range falls in winter` → https://www.evptc.com/news/why-electric-bus-range-falls-in-winter-and-five-levers-fleets-can-control-422923.html
4. Anchor: `electric bus battery preheating at −30°C` → https://www.evptc.com/news/electric-bus-battery-preheating-at-30c-five-planning-mistakes-422919.html

## Image recommendations

- Hero: approved EVLINK E-Series or Q-Series product photograph on a clean white background.
- Diagram: two-loop schematic (stack loop with deionised coolant, heater loop, heat exchanger between them), drawn generically without vehicle-brand references.
- Alt text: `EVLINK 20 kW class PTC coolant heater for hydrogen fuel cell bus cabin heating and defrost`.

## Technical reference

- US Department of Energy, Fuel Cell Systems: https://www.energy.gov/sites/default/files/2014/03/f10/fcm05r0.pdf . Used only for general heat-recovery/coolant-circuit context, not as evidence that every bus needs 20 kW or that EVLINK supplied a particular fleet.

## Review status — 2026-10-22

- Peter approved this article direction on 2026-10-22. Editorial revision by Codex; not a publication approval.
- Removed or qualified unsupported case histories, generalised product claims and unreferenced numerical performance/cost claims. Product data must be confirmed for the selected variant.
- Four actual HTML internal links included from the repository's published inventory. Targets have not received a fresh live HTTP check this round.
- SERP research in the earlier draft lacked reproducible query/location/result evidence; no verified search-volume or ranking claim is made. This remains an acceptance item.
- Featured-image recommendations are not an image delivery. Actual approved photo and finished image remain pending.
- Final revised text has NOT been tested in ZeroGPT/GPTZero. Do not reuse any earlier version's score. Required recorded threshold: ZeroGPT <=30%; GPTZero reference only.
- Status: revised draft, pending technical review, actual images, detector results and Peter's final review. Do not publish.
