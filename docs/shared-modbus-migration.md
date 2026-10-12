# EWD108 0.2: shared Modbus migration

Home Assistant 2026.10.1 was used for development and regression tests.
Version 0.2 requires HA 2026.10 or newer. The July 2026 Modbus modernization
introduced shared units, and the October release adds the connection panel:

- https://developers.home-assistant.io/docs/modbus/introduction/
- https://www.home-assistant.io/integrations/modbus/

## What changes

One function-03 request reads registers 5–39 (35 registers / 70 bytes).
All coordinates, fix status and timestamps come from its checksum-validated
RMC sentence. The default interval is 30 seconds. Failed transport reads,
incomplete responses and parse/checksum failures have two extra attempts
after 1 and 2 seconds. Cancellation stops retries immediately. A successful
invalid-fix response is not a communication failure and is not retried.

Each attempt obeys the shared connection's timeout and spacing requirements.
Three exhausted attempts report unavailable GPS until the next poll. The
reader's lock prevents concurrent retry sequences on the same device client.

The native GPS tracker publishes the accepted latitude and longitude together.
The `Position status` diagnostic shows accepted, invalid_fix, stale_fix,
future_fix, out_of_order_fix, invalid_coordinates or implausible_jump.
Communication and parse errors are reported through coordinator availability
and the HA log; the diagnostic state may retain the prior rejection text
while its entity is unavailable.

## Existing YAML connections

HA's legacy YAML hubs maintain their own connection. They do not automatically
join the new shared manager. Copying hub settings into the setup form is only
a convenience; it does not share the old hub.

The integration refuses both configured and still-running legacy hubs on the
same endpoint. Removing a hub from YAML without reloading it is insufficient.
Other modern integrations using identical connection settings share one link.

For Jaskier, `rs485_3` currently contains only the EWD108 at slave 16, on
192.168.88.20:502 using RTU over TCP. Keep a backup of that file and record the
current tracker helper, dashboard and automation configs before migration.

1. Install the updated integration files. A first installation or changed
   manifest may require an HA restart to reload imports and dependencies.
2. Remove the EWD108 YAML hub and reload Modbus. Do not remove other devices
   from a mixed-device hub: migrate every consumer on that connection first.
3. Add EWD108 GNSS in Settings > Devices & Services, with RTU over TCP,
   host 192.168.88.20, port 502, slave 16, polling 30 seconds, timeout 3 seconds
   and conservative spacing 1 second. Keep automatic HA location updates off
   while the existing location-sync automation remains enabled.
4. Confirm fresh `Timestamp`, accepted `Position status`, and sensible GPS
   coordinates. In Settings > Connectivity > Modbus, confirm a single shared
   connection and no remaining YAML entry for this endpoint.
5. Update the dashboard map and trip automations to consume the native GPS
   tracker and timestamp from the new integration. HA determines the entity
   IDs from its device registry; inspect the created entities instead of
   assuming a name. Do not reassemble a position from two raw sensors.
6. If keeping `device_tracker.jaskier_gps` as a template compatibility helper,
   make its latitude, longitude and availability reference the single native
   tracker. Update all remaining raw EWD108 sensor consumers before removing
   their obsolete entities/templates. The local investigation document lists
   the known tracker and location-sync consumers; live trip automations need
   inspection as well.

RTU over TCP uses `ModbusSerialParams(device="socket://HOST:PORT")`.
The socket adapter's 115200 baud setting matches HA's canonical socket-RTU
parameters and affects its inter-frame timing. It does not change the
gateway's actual RS485 baud rate; configure that at the gateway.

The connection manager owns lifecycle and reconnects. The EWD108 reader never
closes a shared socket directly. Setup probing temporarily borrows a unit and
does not change the policy of a unit already held by another consumer.

## Recovery

To revert, disable/remove the EWD108 config entry before restoring the YAML
hub and reloading Modbus, then restore tracker and consumer references.
Never run both polling sources against the same gateway during rollback.

## Validation limits

The regression suite uses HA 2026.10.1's actual shared-connection API and
coordinator/tracker classes, with controlled Modbus responses. It covers
checksum failures, timeouts, incomplete frames, cancellation, fix loss,
stale/future/reversed times, Africa jumps, global coordinates, sharing and
unload ownership. Deployment still requires a live read from the physical
EWD108 and verification of the migrated consumers. No live hardware
migration has been performed by the code changes alone.
