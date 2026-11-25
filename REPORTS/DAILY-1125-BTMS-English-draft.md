# Electric Bus BTMS: Why One Battery Pack Runs Hotter on the Same Coolant Loop

**Draft for review · DAILY-1125 · Written by Codex**

- Proposed SEO title: Electric Bus BTMS: Coolant Flow Across Battery Packs
- Proposed meta description: One battery pack runs hotter even when total coolant flow is on target. See what an electric bus team should measure before changing the BTMS.
- Proposed slug: electric-bus-btms-battery-pack-flow-balance
- Search topic: electric bus battery thermal management. The specific diagnostic question is a candidate angle. US search volume for the long-tail wording has not been confirmed.
- Publication status: English working draft. DeepL return translation and ZeroGPT scores pending. Featured image pending.

---

The pump is running. The chiller outlet is at the target temperature. But one battery pack in the bus keeps running hotter than the others. Before asking for a bigger chiller, check how much coolant is actually reaching that pack. A flow meter on the main line tells you what went through the whole loop. It cannot tell you what each battery branch received.

## Put the readings from each pack on the same timeline

Pick a condition where the temperature difference shows up. That might be a climb near the end of a shift, or charging after the bus returns to the depot. Use the same test window for all packs. Ask the battery team to confirm which reading you are comparing, such as maximum cell temperature or a reading from a particular module.

On the same timeline, log coolant inlet and outlet temperatures for the affected pack and a comparison pack. Add branch flow, where you can measure it, and the pump command and valve position. Include the battery load and which cooling mode the vehicle requested. A set of numbers taken at different points in the run can send the investigation in the wrong direction.

## Follow the branch that comes up short

Parallel pipes can carry different flows. Hose length, fittings, valves and the resistance inside each pack all count. Anadolu Isuzu engineers reported this issue in an [18-metre electric bus study](https://doi.org/10.4271/2025-01-5017). They investigated how differences in pressure drop affected the distribution of coolant among the battery packs.

If one branch is below its project flow target, compare its installed routing with the drawing. Check the valve state and ask whether the cooling loop was filled and bled using the approved procedure. Then compare measured pressure drop with the pack supplier’s data at the measured flow and fluid condition. Agree on the measurement points first. A pressure reading across the pack alone misses the losses in its hoses and fittings.

If both branches receive their expected flow but one pack still runs hotter, ask the battery team to look at pack load, sensor placement and heat transfer inside the pack. A larger chiller changes how much heat the system can reject. The temperature readings and flow measurements should tell you whether you need that capacity or whether the problem lies elsewhere.

## Repeat the check in the operating condition that matters

After making a change, run the condition that first exposed the issue. Use the same acceptance limits from the battery team. Record what changed and review whether the other branches still meet their own flow requirements. When the system switches between driving and charging, confirm that the new settings work in the modes that your vehicle actually uses.

For an [electric bus thermal management review](https://evbtms.com/electric-bus/), send the coolant loop drawing, pack flow targets and a short log from the problem run. Include the ambient temperature and coolant specification. These are the inputs the vehicle and [BTMS](https://evbtms.com/products/battery-thermal-management-system/) teams need to agree on what to measure next.

## Can I use coolant temperature rise to diagnose low flow?

Use it as a clue. A larger temperature rise can occur when a branch carries less coolant or when the pack is putting more heat into the same flow. Compare it with branch flow and pack load before deciding which one you are seeing.

## Does every battery branch need the same flow?

Use the requirement for each pack. Identical packs with the same duty may share a target. Different packs or operating conditions can call for different targets. The battery supplier’s limits govern the decision.

---

## Editorial checks

- The existing coolant-flow guide covers estimating and verifying loop flow. This draft focuses on a hot-pack diagnostic sequence and uses no model-specific limits or numerical temperature thresholds.
- Existing coverage checked: [air removal](https://evbtms.com/btms-coolant-loop-air-removal/), [rating conditions](https://evbtms.com/btms-cooling-capacity-rating-conditions/), [battery heat-load sizing](https://evbtms.com/battery-heat-load-btms-sizing-commercial-ev/).
- Featured image brief: EVLINK’s real BTMS unit beside a bus in a service bay with battery-cooling commissioning equipment. Show the real enclosure unchanged. Create a new scene and export WebP.
- External reference: Birgül and Meydan, Anadolu Isuzu, SAE Technical Paper 2025-01-5017.
