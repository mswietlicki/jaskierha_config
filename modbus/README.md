# Modbus Hubs and Devices

This folder contains per-hub Home Assistant Modbus configuration loaded by:

- `modbus: !include_dir_merge_list modbus`

## Hub: relay_board

- Host: `192.168.88.19:502`
- Type: `rtuovertcp`
- Description: 8-channel relay board used for generic relay outputs.

Devices on this hub:

- Slave `1`: Relay board with coils `0-7` (`Relay 0` to `Relay 7`).

## Hub: victron_cerbo

- Host: `192.168.88.22:502`
- Type: `tcp`
- Description: Victron Cerbo GX Modbus TCP endpoint.

Devices on this hub:

- Slave `100`: Victron system registers:
  - 843: Battery SOC
  - 840: Battery voltage
  - 841: Battery current
  - 842: Battery power
  - 850: DC PV power
  - 851: DC PV current
  - 846: Battery time-to-go (system)
  - 817: AC consumption L1
  - 820: Grid power L1
- Slave `239`: Victron battery service registers:
  - 262: Battery temperature
  - 318: Minimum cell temperature
  - 319: Maximum cell temperature
- Slave `226` (assumed): Victron solar charger service registers:
  - 776: PV voltage
  - 777: PV current
  - 792: PV power
- Slave `227`: Victron VE.Bus inverter/charger registers:
  - 31: VE.Bus state
  - 33: VE.Bus switch position (control)
  - 57: BMS allows charge
  - 58: BMS allows discharge
  - 60: BMS error
- Slave `239`: Alternator controller readings:
  - 4117: Alternator input voltage
  - 4118: Alternator input power

Note: ID `226` is a common default for Victron solar service and may vary by installation. If an entity is unavailable, check your Cerbo GX Modbus service list and update `slave` values in [modbus/victron_cerbo.yaml](modbus/victron_cerbo.yaml).

## Hub: rs485_1

- Host: `192.168.88.18:502`
- Type: `tcp`
- Description: RS485 bridge with boiler, water temp, and valve/pump relays.

Devices on this hub:

- Slave `50`: Temperature controller
  - 160: Boiler temp
  - 161: Water temp
- Slave `32`: Relay module
  - Coil 0: Water pump relay
  - Coil 1: Gray water valve
- Slave `33`: Valve relay module
  - Coil 0: Water valve tank
  - Coil 1: Water valve loop
  - Coil 2: Water valve pump overwrite
  - Coil 3: Water valve grid
