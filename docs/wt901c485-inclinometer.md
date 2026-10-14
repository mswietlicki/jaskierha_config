# WT901C485 inclinometer (front controller)

A WitMotion WT901C485 attitude sensor on the front controller's RS485 port.
Its job is to tell whether the van is level and, if not, which corner is low.
Configured in [esphome/front-controller.yaml](../esphome/front-controller.yaml)
(commit `faf6be5`, 2026-10-14).

## Status

| Item | State |
|---|---|
| Config validated (`esphome config`, ESPHome 2026.9.1) | Done |
| Flashed to the front controller | Not yet |
| Entity IDs below | Expected from the naming pattern, confirm after the first flash |
| Roll/pitch sign convention | Expected, not tested on the unit (see [Signs](#signs-and-direction)) |
| Set Level Reference button | Not tested; the command comes from WitMotion's SDK |
| Behaviour when the sensor is unplugged | Not tested |

Update this table as items get verified.

## What the sensor can do

The WT901C485 is a 9-axis IMU with on-board sensor fusion (Kalman filter):

- 3-axis accelerometer (±16 g)
- 3-axis gyroscope (±2000 °/s)
- 3-axis magnetometer
- Fused angles: roll and pitch from the accelerometer and gyro, yaw (heading)
  from the magnetometer
- Chip temperature

It talks Modbus RTU over RS485. All of these can be read; only roll, pitch,
yaw and temperature are exposed today. The angle registers have a resolution
of 180/32768 ≈ 0.0055°, far finer than levelling needs.

Label on this unit: `WT901C485`, `7-D-3 GD202605260007`.

## Hardware

Board: Waveshare ESP32-S3-POE-ETH-8DI-8RO. Its RS485 port is isolated and
switches direction in hardware, so ESPHome needs no DE/RE pin.

| Signal | Board | Sensor |
|---|---|---|
| RS485 TX | GPIO17 | – |
| RS485 RX | GPIO18 | – |
| A | RS485 A | A |
| B | RS485 B | B |
| GND | RS485 GND, if the terminal has one | GND |
| Power | – | VCC/GND from 12 V |

- **Power:** use 12 V, e.g. the supply feeding the board's 7–36 V terminal.
  Sources disagree on the sensor's minimum (5 V vs 9 V), so never 5 V or
  3.3 V. The board has no power output for sensors; on PoE the sensor needs
  its own 12 V.
- **Two pin blocks on the label:** same bus, for daisy-chaining. Either works.
- **Termination:** the board's 120 Ω jumper is off by default. Leave it off
  for a short cable.
- **No response:** swap A and B first.

## Mounting and axes

The label shows the axes: X along the arrow, Y to the left of it, Z out of
the label. Mounted **flat, label up, X arrow toward the front of the van**,
the sensor frame matches the vehicle frame:

- X = forward, Y = left, Z = up
- Roll = rotation about X (side-to-side tilt)
- Pitch = rotation about Y (front-to-back tilt)

Other mountings change the meaning:

- X arrow pointing backward: both signs flip.
- X arrow pointing sideways: roll and pitch swap.
- Mounted on a wall (vertical): set `ORIENT` (0x23) to 1, see
  [Configuration registers](#configuration-registers).

Mount it rigidly to the body (floor, bulkhead, cabinet frame), never to an
axle or suspension part. Keep it away from battery, inverter and alternator
cables; their current disturbs the magnetometer (yaw only).

## Signs and direction

Expected with the mounting above (right-hand rule, the convention WitMotion's
axis markings follow). **Verify once:** hold the sensor label up, arrow
forward; lifting the left edge should make roll positive, lifting the arrow
end should make pitch negative. Correct this table if the unit disagrees.

| Value | Positive | Negative | To level, raise |
|---|---|---|---|
| Roll | Left side high (right low) | Right side high (left low) | `+` right wheels, `−` left wheels |
| Pitch | Front low | Front high | `+` front wheels, `−` rear wheels |

Left and right are from the driver's seat. The lowest corner combines both:
roll `+1.2°` with pitch `+0.8°` means right low and front low, so
front-right is the lowest corner.

## Home Assistant entities

Expected IDs, following `switch.front_controller_starter_battery_charger`:

| Entity | Unit | Default | Notes |
|---|---|---|---|
| `sensor.front_controller_inclinometer_roll` | ° | enabled | 2 decimals |
| `sensor.front_controller_inclinometer_pitch` | ° | enabled | 2 decimals |
| `sensor.front_controller_inclinometer_yaw` | ° | **disabled** | Magnetic heading, unreliable in the van |
| `sensor.front_controller_inclinometer_temperature` | °C | enabled, diagnostic | Chip temperature, not cabin temperature |
| `button.front_controller_inclinometer_set_level_reference` | – | enabled, config | See [Calibration](#calibration) |

Update behaviour, relevant for automations:

- The ESP polls the sensor every **1 s**.
- A `delta` filter publishes only real changes: roll/pitch ≥ 0.05°, yaw
  ≥ 0.5°, temperature ≥ 0.2 °C. When the van stands still the state does not
  change, so `last_updated` is **not** a heartbeat. Use the ESPHome
  `binary_sensor` "Status" (front controller online) for availability of the
  ESP itself.
- When the ESP is offline, all entities become `unavailable`. What happens
  when only the sensor stops answering (unplugged, cable fault) is not tested;
  the values may stay at the last reading. Don't treat a value as fresh just
  because it's numeric.
- Always parse with `float(none)` and handle `none`, as below.

## Calibration

### Level reference (the one that matters)

Makes the current roll/pitch the 0° point and saves it in the sensor, so 0°
means "van level" instead of "sensor level".

1. Park and level the van using a bubble level on the floor or a worktop.
2. Press **Inclinometer Set Level Reference**.
3. Check roll and pitch read about 0.
4. Power-cycle the sensor (or the front controller) and check they still read
   about 0. If not, the reference wasn't saved; see the raw frames below.

Never press it on a slope; every later reading would be off by that slope.
To redo it, level the van again and press it again.

### Accelerometer and magnetometer (not exposed)

Not needed for levelling, and not wired to buttons. If ever needed, they are
register writes like the level reference (always unlock with `KEY` first):

- **Accelerometer:** sensor flat and still, `CALSW` = 0x01, wait a few
  seconds, `CALSW` = 0x00, `SAVE` = 0x0000. It assumes the sensor is
  horizontal, so on an unlevel van it bakes the slope into the offsets.
  Prefer the level reference.
- **Magnetometer:** `CALSW` = 0x07, rotate the sensor through all
  orientations, then unlock again and `CALSW` = 0x00. In a van it can only
  turn flat (drive slow full circles in an open car park), so it's a partial
  calibration. Must be done with the sensor already mounted.

## Using it in automations

### Degrees to height

Height difference = distance × tan(angle). For small angles,
**1° ≈ 1.75 cm per metre**. For a van with about 3.45 m wheelbase and 1.8 m
track, 1° of pitch is about 6 cm between axles and 1° of roll about 3 cm
between left and right wheels. Replace the dimensions below with the van's
real wheelbase and rear track width.

### Template examples

All templates were checked to render correctly for level, tilted and
`unavailable` inputs.

**Van level** (template binary sensor, ±0.5°):

```jinja
{% set r = states('sensor.front_controller_inclinometer_roll') | float(none) %}
{% set p = states('sensor.front_controller_inclinometer_pitch') | float(none) %}
{{ r is not none and p is not none and r | abs <= 0.5 and p | abs <= 0.5 }}
```

**Lowest corner** (template sensor, e.g. `front-right low`, `rear low`,
`level`; 0.3° dead band):

```jinja
{% set r = states('sensor.front_controller_inclinometer_roll') | float(none) %}
{% set p = states('sensor.front_controller_inclinometer_pitch') | float(none) %}
{% set tol = 0.3 %}
{% if r is none or p is none %}unknown
{% else %}
{% set fb = 'front' if p > tol else ('rear' if p < -tol else '') %}
{% set lr = 'right' if r > tol else ('left' if r < -tol else '') %}
{{ ([fb, lr] | select | join('-') ~ ' low') if fb or lr else 'level' }}
{% endif %}
```

**Lift needed at the low axle** in cm (template sensor; same pattern with
roll and the track width for the low side):

```jinja
{% set wheelbase_cm = 345 %}
{% set p = states('sensor.front_controller_inclinometer_pitch') | float(none) %}
{% if p is not none %}{{ (wheelbase_cm * ((p * pi / 180) | tan)) | abs | round(1) }}{% endif %}
```

These templates follow the expected signs in
[Signs and direction](#signs-and-direction). If the unit turns out
different, flip the comparisons.

### Automation ideas

- **Parking slope check:** a few minutes after the engine stops, push the
  lowest corner and lift needed, or warn if the van isn't level.
- **Tilt alarm while parked:** store roll/pitch when parked; alert if either
  changes by more than about 1°. Catches jacking, towing or a wheel on soft
  ground sinking overnight.
- **Side-slope warning while driving:** warn above a set roll angle on
  tracks or ramps (tall van).
- **Dashboard:** roll/pitch gauges plus the lowest-corner text on the trip
  dashboard.

Engine state: `binary_sensor.jaskier_wican_obd_pro_engine_on` (existing
automations trigger on `from: 'on'`, so treat anything other than `on` as
"engine off"). GPS speed: `sensor.ewd108_speed_over_ground_kmh`.

Example tilt alarm. It needs two helpers that don't exist yet,
`input_number.van_parked_roll` and `input_number.van_parked_pitch`
(range −180..180, step 0.01), and a second automation that writes the
current roll/pitch into them when the engine has been off for a few minutes.

```yaml
- alias: Van tilt alarm
  description: Roll or pitch moved more than 1° since parking.
  triggers:
  - trigger: template
    value_template: >
      {% set r = states('sensor.front_controller_inclinometer_roll') | float(none) %}
      {% set p = states('sensor.front_controller_inclinometer_pitch') | float(none) %}
      {% set r0 = states('input_number.van_parked_roll') | float(none) %}
      {% set p0 = states('input_number.van_parked_pitch') | float(none) %}
      {{ none not in [r, p, r0, p0] and
         ((r - r0) | abs > 1 or (p - p0) | abs > 1) }}
  conditions:
  - condition: not
    conditions:
    - condition: state
      entity_id: binary_sensor.jaskier_wican_obd_pro_engine_on
      state: 'on'
  actions:
  - action: notify.mobile_app_mateuszphone
    continue_on_error: true
    data:
      title: Van tilt changed
      message: >
        Roll {{ states('sensor.front_controller_inclinometer_roll') }}°,
        pitch {{ states('sensor.front_controller_inclinometer_pitch') }}°
        since parking.
      data:
        tag: van_tilt
        priority: high
        ttl: 0
  mode: single
```

### Heading

Yaw is disabled because the magnetometer reads the van's own steel and
cable currents as much as the Earth's field. Two options if heading is ever
needed:

1. Enable yaw after an in-place magnetometer calibration (above). Expect
   "roughly south-east", not precise aiming.
2. Better: the EWD108 GPS reports course over ground in the register block
   already documented in [ewd108-gps-reading.md](ewd108-gps-reading.md)
   (function 03, start 200, count 17). Saving the last course while driving
   above ~5 km/h gives the parked heading. Off by 180° if you reversed into
   the spot. Not implemented.

## Modbus reference

Factory settings: address **0x50**, **9600 8N1**. Reads use function 0x03
(ESPHome `register_type: holding`), writes use function 0x06.

### Data registers

All signed 16-bit (`S_WORD`). Scaling from WitMotion's SDK sample code.

| Register | Value | Scaling | Exposed |
|---|---|---|---|
| 0x34–0x36 | Acceleration X/Y/Z | raw / 32768 × 16 g | no |
| 0x37–0x39 | Angular rate X/Y/Z | raw / 32768 × 2000 °/s | no |
| 0x3A–0x3C | Magnetic field X/Y/Z | raw counts | no |
| 0x3D | Roll | raw / 32768 × 180 ° | yes |
| 0x3E | Pitch | raw / 32768 × 180 ° | yes |
| 0x3F | Yaw | raw / 32768 × 180 ° | yes (disabled) |
| 0x40 | Temperature | raw / 100 °C | yes |
| 0x51–0x54 | Quaternion q0–q3 | raw / 32768 (not verified) | no |

### Configuration registers

From WitMotion's generic register header (`REG.h`); not tested on this unit.
Write `KEY` first, then the register, then `SAVE` to keep it after power-off.

| Register | Name | Values |
|---|---|---|
| 0x69 | KEY | 0xB588 unlocks writes |
| 0x00 | SAVE | 0x0000 saves settings to flash |
| 0x01 | CALSW | 0x00 normal, 0x01 accelerometer cal, 0x04 zero heading, 0x07 magnetometer cal, 0x08 set angle reference |
| 0x04 | BAUD | 1 = 4800, 2 = 9600, 3 = 19200, 4 = 38400, 5 = 57600, 6 = 115200 |
| 0x1A | IICADDR | Device address |
| 0x1F | BANDWIDTH | 0 = 256 Hz, 1 = 184, 2 = 94, 3 = 44, 4 = 21, 5 = 10, 6 = 5 Hz |
| 0x23 | ORIENT | 0 = horizontal, 1 = vertical mounting |
| 0x24 | AXIS6 | 0 = 9-axis (with magnetometer), 1 = 6-axis (yaw from gyro only, drifts) |

Changing `BAUD` or `IICADDR` breaks communication until the ESPHome config
matches.

### Raw frames

For testing with a USB–RS485 adapter and a serial terminal. CRCs computed
and checked against WitMotion's published example.

| Purpose | Frame (hex) |
|---|---|
| Read roll, pitch, yaw, temp (0x3D, 4 regs) | `50 03 00 3D 00 04 D8 44` |
| Read 0x34–0x40 (13 regs) | `50 03 00 34 00 0D C8 40` |
| Unlock | `50 06 00 69 B5 88 22 A1` |
| Set angle reference | `50 06 00 01 00 08 D4 4D` |
| CALSW normal | `50 06 00 01 00 00 D5 8B` |
| Save | `50 06 00 00 00 00 84 4B` |

## ESPHome notes

- Requires **ESPHome 2026.9.0 or newer** (`modbus_client.write_single_register`
  and the reworked `modbus_controller`).
- The four exposed registers are contiguous, so each poll is one request.
- Modbus hub defaults: `send_wait_time` 2000 ms, `turnaround_time` 600 ms.
  That allows roughly one to one and a half requests per second, which is
  why the poll is 1 s.
- Adding acceleration or gyro: they sit below roll (0x34–0x39). Adding all
  of 0x34–0x3C keeps one contiguous read. Adding only some leaves a gap; set
  `reuse_previous_range: true` on the roll sensor to keep one request, or
  accept a second request per poll.
- `skip_updates` no longer works. For slower polling of some values, use a
  second `modbus_controller` with the same address and a longer
  `update_interval`.
- Writes go through `modbus_client.write_single_register` with
  `address: 0x50`, `start_address` and `value`, as in the level reference
  button.

## Sources

- WitMotion SDK (register map, scaling, calibration sequences):
  https://github.com/WITMOTION/WitStandardModbus_WT901C485
- Waveshare board pinout: https://www.waveshare.com/wiki/ESP32-S3-ETH-8DI-8RO
- Waveshare product page (isolated RS485, automatic direction, 120 Ω jumper):
  https://www.waveshare.com/esp32-s3-eth-8di-8ro.htm
- ESPHome Modbus: https://esphome.io/components/modbus/,
  https://esphome.io/components/modbus_controller/,
  https://esphome.io/components/modbus_client/
