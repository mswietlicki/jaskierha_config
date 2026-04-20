# Water Valve States

This document describes the target end-state for each water mode and the valve naming used in Home Assistant.

## Valve Mapping

- `switch.water_valve_tank` - formerly `water_valve_1`
- `switch.water_valve_loop` - formerly `water_valve_2`
- `switch.water_valve_pump_overwrite` - formerly `water_valve_3`
- `switch.water_valve_grid` - formerly `water_valve_4`

## Mode State Table

| Water Mode      | Tank Valve (`water_valve_tank`) | Loop Valve (`water_valve_loop`) | Pump Overwrite Valve (`water_valve_pump_overwrite`) | Grid Valve (`water_valve_grid`) | Pump (`water_pump_relay`) |
|-----------------|----------------------------------|----------------------------------|------------------------------------------------------|----------------------------------|----------------------------|
| Normal          | OFF                              | OFF                              | OFF                                                  | OFF                              | Restore previous state     |
| Pump Filling    | OFF                              | ON                               | ON                                                   | ON                               | Restore previous state     |
| Grid Filling    | OFF                              | ON                               | OFF                                                  | ON                               | OFF                        |
| Grid            | ON                               | ON                               | OFF                                                  | ON                               | OFF                        |

## State Machine Behavior

- Desired mode is selected via `input_select.water_mode_target`.
- Current applied mode is tracked in `input_select.water_mode_current`.
- Transitions are performed by `script.water_set_mode`.
- Pump is forced OFF before any valve transition starts.
- Valves are changed one-by-one in sequence (never in parallel).
- A 5-second delay is added after each valve action.
- If a valve is already in the required state, no action is taken for that valve.
- For `Grid` and `Grid Filling`, pump remains OFF after transition.
- For other modes, pump returns to its pre-transition state.

## Compatibility Scripts

The following scripts are wrappers that set the target mode:

- `script.water_mode_normal`
- `script.water_mode_pump_filling`
- `script.water_mode_grid_filling`
- `script.water_mode_grid`
