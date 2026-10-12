# EWD108 GPS route investigation — 2026-10-12

## Cause observed in Home Assistant

At 08:46:55.947 Warsaw time the position-valid register changed to 0.
Latitude became 0.000000 at 08:46:56.098. At 08:47:00.985 the
position-valid register returned to 1, but latitude did not recover until
08:47:01.141. The tracker published latitude 0 with the previous longitude
at 08:47:01.105. An equivalent sequence occurred one minute earlier.

The separate reads in `modbus/rs485_3.yaml` expose a mixed sample while
recovering from an invalid fix. This demonstrates a reading/coherence
problem; it does not establish why the receiver loses its fix. Logs also
contain Modbus timeouts for slave 16 on rs485_3.

## Active mitigation

The existing UI template helper `device_tracker.jaskier_gps` was updated
through its options flow. Its latitude/longitude templates now use
`float(none)` and its availability template is:

```jinja
{% set lat = states('sensor.ewd108_signed_latitude') | float(none) %}
{% set lon = states('sensor.ewd108_signed_longitude') | float(none) %}
{{ is_state('sensor.ewd108_fix_status', 'Valid') and
   lat is not none and lon is not none and
   -90 <= lat <= 90 and -180 <= lon <= 180 and
   lat != 0 and lon != 0 }}
```

Exact zero on either axis is rejected as the observed receiver sentinel.
This intentionally also excludes an exact reading on the equator or prime
meridian; it is an interim guard rather than a general global GPS validator.

The location-sync automation now requires both axes to be nonzero and the
tracker to be available, and consumes the tracker's coordinates. It was
updated live and mirrored in `automations.yaml`.

Eleven template cases covered valid northern/southern coordinates, each
zero axis, both zero, bounds violations, unavailable/unknown, NaN and
infinity. Valid samples passed and invalid samples were rejected. The
first 16 post-change tracker history samples had no zero coordinates.
Previously recorded bad points remain in recorder history and will age
out of the dashboard's 24-hour route window.

## Device documentation and better acquisition

- Manufacturer product page: https://www.cdebyte.com/products/EWD108-GN05(485)/2
- Manufacturer Modbus application guide: https://www.ebyte.com/news/4455.html
- Local manual: `C:/Code/HA_EWD108/docs/EWD108-GN0x_Series_UserManual_CN_V1.0.pdf`
- Local transcription: `C:/Code/HA_EWD108/docs/EWD108-GN0x_Series_UserManual_CN_V1.0.md`

The manual's register map matches the current addresses and default
big-endian float32 layout. Changing byte/word order is not supported by
the evidence: normal readings are correct.

Documented coherent-read alternatives:

1. Function 03, start address 200 (0x00C8), count 17 (0x0011): fix status,
   UTC date/time, longitude direction/value, latitude direction/value,
   speed and course in one response. A native HA custom Modbus sensor can
   decode the 34 bytes with `structure: ">8HfHfff"`, `count: 17` and
   `precision: 6`; downstream consumers should parse this same source
   rather than combine independently updated sensors. A single response
   reduces cross-request mixing; firmware snapshot atomicity is not
   explicitly guaranteed by the manual.
2. Function 03, start address 5, count 35: complete 70-byte RMC ASCII
   payload, including fix status, both coordinates, date/time and XOR
   checksum. Validate checksum, valid-fix status, coordinate bounds and
   timestamp freshness before publishing a position.

The existing `custom_components/ewd108` integration implements option 2
and validates its RMC checksum. No EWD108 config entry is currently loaded
in HA. Before activating it, verify live RMC support and avoid simultaneous
independent connections to the same RS485 gateway. Reuse a serialized hub
connection or migrate the existing polling source. Do not simply add a
second competing poller.

The Modbus acquisition source was not changed during this investigation.
The connector currently does not grant file access to `modbus/`.

## Rollback

Restore the tracker helper's latitude/longitude templates to their original
`states(...)` expressions, and availability to valid fix plus `has_value`
on both signed sensors. Restore the location-sync automation from its
pre-change configuration (the original is also available in Git).
