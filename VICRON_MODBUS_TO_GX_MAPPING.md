# Victron Modbus -> Victron GX Mapping

Source: DEVICES.md (generated 2026-05-15)

This mapping was used to replace Modbus entities in dashboards.

## Direct replacements

| Modbus entity | Victron GX entity |
| --- | --- |
| sensor.victron_battery_soc | sensor.shunt_main_charge |
| sensor.victron_battery_voltage | sensor.shunt_main_dc_bus_voltage |
| sensor.victron_battery_current | sensor.shunt_main_dc_bus_current |
| sensor.victron_battery_power | sensor.shunt_main_power |
| sensor.victron_battery_time_to_go_system | sensor.shunt_main_time_to_go |
| sensor.victron_battery_temperature | sensor.shunt_main_temperature |
| sensor.victron_dc_pv_power | sensor.gx_device_pv_power |
| sensor.victron_grid_power_l1 | sensor.inverter_input_power_l1 |
| sensor.victron_ac_consumption_l1 | sensor.gx_device_consumption_power_l1 |

## Solar charger replacements

| Modbus entity | Victron GX entity |
| --- | --- |
| sensor.victron_solar_panel_voltage | sensor.smartsolar_charger_mppt_100_30_id_279_pv_bus_voltage |
| sensor.victron_solar_panel_current | sensor.smartsolar_charger_mppt_100_30_id_279_dc_battery_bus_current |
| sensor.victron_solar_panel_power | sensor.smartsolar_charger_mppt_100_30_id_279_pv_yield_power |
| sensor.victron_solar_224_panel_voltage | sensor.smartsolar_charger_mppt_100_30_id_278_pv_bus_voltage |
| sensor.victron_solar_224_panel_current | sensor.smartsolar_charger_mppt_100_30_id_278_dc_battery_bus_current |
| sensor.victron_solar_224_panel_power | sensor.smartsolar_charger_mppt_100_30_id_278_pv_yield_power |

Note: GX exposes PV bus voltage and PV yield power per charger, but not a direct PV panel current field in DEVICES.md. The closest per-charger current is DC battery bus current.

## VE.Bus/BMS section

No one-to-one Victron GX entities were found in DEVICES.md for:

- sensor.victron_vebus_bms_error
- sensor.victron_vebus_bms_allow_to_charge
- sensor.victron_vebus_bms_allow_to_discharge
- sensor.victron_vebus_switch_position

Dashboard replacements used available Victron GX inverter diagnostics:

- sensor.inverter_state
- sensor.inverter_low_battery_alarm
- sensor.inverter_grid_lost_alarm
- sensor.inverter_overload_alarm
