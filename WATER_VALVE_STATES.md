# Water Valve States

This document describes the target end-state for each water mode and the valve naming used in Home Assistant.

## Valve Mapping

- `switch.water_valve_tank` - formerly `water_valve_1`
- `switch.water_valve_loop` - formerly `water_valve_2`
- `switch.water_valve_pump_overwrite` - formerly `water_valve_3`
- `switch.water_valve_grid` - formerly `water_valve_4`

## Mode State Table

| Water Mode | Tank Valve (`water_valve_tank`) | Loop Valve (`water_valve_loop`) | Pump Overwrite Valve (`water_valve_pump_overwrite`) | Grid Valve (`water_valve_grid`) | Pump (`water_pump_relay`) |
| --- | --- | --- | --- | --- | --- |
| Normal | OFF | OFF | OFF | OFF | Restore previous state |
| Pump Filling | OFF | ON | ON | ON | Restore previous state |
| Grid Filling | OFF | ON | OFF | ON | OFF |
| Grid | ON | ON | OFF | ON | OFF |

## State Machine Behavior

- Desired mode is selected via `input_select.water_mode_target`.
- Current applied mode is tracked in `input_select.water_mode_current`.
- Transitions are performed by `script.water_set_mode`.
- Pump is forced OFF before any valve transition starts.
- Valves are changed one-by-one in sequence (never in parallel).
- A 5-second delay is added after each valve action.
- If a valve is already in the required state, no action is taken for that valve.
- OFF phase order is always: `Grid -> Loop -> Pump Overwrite -> Tank`.
- ON phase order is always: `Pump Overwrite -> Loop -> Grid -> Tank`.
- For `Grid` and `Grid Filling`, pump remains OFF after transition.
- For other modes, pump returns to its pre-transition state.

## Mode Detection

- The water mode is defined by the valve layout only (valve columns of the table above). The pump state is not part of the mode: the pump is switched off whenever water is not used or nobody is home, and that is a normal state.
- `automation.water_reconcile_mode_on_start` (HA start) and the exit path of `automation.water_maintenance_gate` set `input_select.water_mode_current` and `input_select.water_mode_target` from the valves. For `Grid` and `Grid Filling` they also switch the pump OFF.
- `Fault` is set, and the pump stopped, only when the valves match no known mode. A recognized layout dismisses an earlier `water_mode_fault` notification.

## Pump Safety

- `automation.water_pump_off_when_unoccupied` switches the pump off when `binary_sensor.jaskier_occupied` turns off. This occupancy sensor is shared with floor heating (45-minute presence memory; an unavailable presence sensor counts as occupied). Skipped during Water Maintenance; the water mode is not changed.
- `automation.water_leak_protection` stops the pump and sends a warning to `notify.mobile_app_mateuszphone` plus a persistent notification when `binary_sensor.sonoff_snzb_05p` (Moisture under Pump) detects water, or when the pump is switched on while the sensor is still wet. It also runs during Water Maintenance and does not change any valve.
- No pump run-time check yet: `switch.water_pump_relay` only enables the pump, and the pump's own pressure switch decides when it runs. Add the check once a pump current and/or pressure sensor is installed.

## Transition Sequences

The sequence below lists only valves that actually change for each transition.

| From | To | Valve Change Sequence |
| --- | --- | --- |
| Normal | Pump Filling | Pump Overwrite -> Loop -> Grid |
| Normal | Grid Filling | Loop -> Grid |
| Normal | Grid | Loop -> Grid -> Tank |
| Pump Filling | Normal | Grid -> Loop -> Pump Overwrite |
| Pump Filling | Grid Filling | Pump Overwrite |
| Pump Filling | Grid | Pump Overwrite -> Tank |
| Grid Filling | Normal | Grid -> Loop |
| Grid Filling | Pump Filling | Pump Overwrite |
| Grid Filling | Grid | Tank |
| Grid | Normal | Grid -> Loop -> Tank |
| Grid | Pump Filling | Tank -> Pump Overwrite |
| Grid | Grid Filling | Tank |

## Compatibility Scripts

The following scripts are wrappers that set the target mode:

- `script.water_mode_normal`
- `script.water_mode_pump_filling`
- `script.water_mode_grid_filling`
- `script.water_mode_grid`
