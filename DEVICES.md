# Home Assistant Devices and Entities

Generated: 2026-05-15 15:00:54 +02:00
Home Assistant URL: https://jaskierha.swietlicki.net/

- Devices: 44
- Entities: 969

## AC Inverter

- Device ID: 27e94ad58d8a5c178db995864494f704
- Manufacturer: Victron Energy
- Model: GX internal relay 1
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| switch.ac_inverter_state | State | victron_gx | no |

## Backup

- Device ID: 9c71597e9dd909777e404ee1d9f53ad6
- Manufacturer: Home Assistant
- Model: Home Assistant Backup
- Software Version: 2026.5.0
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| event.backup_automatic_backup | Automatic backup | backup | no |
| sensor.backup_backup_manager_state | Backup Manager state | backup | no |
| sensor.backup_last_attempted_automatic_backup | Last attempted automatic backup | backup | no |
| sensor.backup_last_successful_automatic_backup | Last successful automatic backup | backup | no |
| sensor.backup_next_scheduled_automatic_backup | Next scheduled automatic backup | backup | no |

## dagaphone

- Device ID: b03875db015c7d425f1f1df2bbd1262e
- Manufacturer: samsung
- Model: SM-S918B
- Software Version: 36
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.dagaphone_android_auto | Android Auto | mobile_app | yes (integration) |
| binary_sensor.dagaphone_app_inactive | App inactive | mobile_app | yes (integration) |
| binary_sensor.dagaphone_bluetooth_state | Bluetooth state | mobile_app | yes (integration) |
| binary_sensor.dagaphone_device_locked | Device locked | mobile_app | yes (integration) |
| binary_sensor.dagaphone_device_secure | Device secure | mobile_app | yes (integration) |
| binary_sensor.dagaphone_doze_mode | Doze mode | mobile_app | yes (integration) |
| binary_sensor.dagaphone_headphones | Headphones | mobile_app | yes (integration) |
| binary_sensor.dagaphone_high_accuracy_mode | High accuracy mode | mobile_app | yes (integration) |
| binary_sensor.dagaphone_hotspot_state | Hotspot state | mobile_app | yes (integration) |
| binary_sensor.dagaphone_interactive | Interactive | mobile_app | yes (integration) |
| binary_sensor.dagaphone_is_charging | Is charging | mobile_app | yes (integration) |
| binary_sensor.dagaphone_keyguard_locked | Keyguard locked | mobile_app | yes (integration) |
| binary_sensor.dagaphone_keyguard_secure | Keyguard secure | mobile_app | yes (integration) |
| binary_sensor.dagaphone_mic_muted | Mic muted | mobile_app | yes (integration) |
| binary_sensor.dagaphone_mobile_data | Mobile data | mobile_app | yes (integration) |
| binary_sensor.dagaphone_mobile_data_roaming | Mobile data roaming | mobile_app | yes (integration) |
| binary_sensor.dagaphone_music_active | Music active | mobile_app | yes (integration) |
| binary_sensor.dagaphone_nfc_state | NFC state | mobile_app | yes (integration) |
| binary_sensor.dagaphone_power_save | Power save | mobile_app | yes (integration) |
| binary_sensor.dagaphone_speakerphone | Speakerphone | mobile_app | yes (integration) |
| binary_sensor.dagaphone_wi_fi_state | Wi-Fi state | mobile_app | yes (integration) |
| binary_sensor.dagaphone_work_profile | Work profile | mobile_app | yes (integration) |
| device_tracker.dagaphone | - | mobile_app | no |
| notify.dagaphone | - | mobile_app | no |
| sensor.dagaphone_accent_color | Accent color | mobile_app | yes (integration) |
| sensor.dagaphone_active_calories_burned | Active calories burned | mobile_app | yes (integration) |
| sensor.dagaphone_active_notification_count | Active notification count | mobile_app | yes (integration) |
| sensor.dagaphone_app_importance | App importance | mobile_app | yes (integration) |
| sensor.dagaphone_app_memory | App memory | mobile_app | yes (integration) |
| sensor.dagaphone_app_rx_gb | App Rx GB | mobile_app | yes (integration) |
| sensor.dagaphone_app_standby_bucket | App standby bucket | mobile_app | yes (integration) |
| sensor.dagaphone_app_tx_gb | App Tx GB | mobile_app | yes (integration) |
| sensor.dagaphone_audio_mode | Audio mode | mobile_app | yes (integration) |
| sensor.dagaphone_basal_body_temperature | Basal body temperature | mobile_app | yes (integration) |
| sensor.dagaphone_basal_metabolic_rate | Basal metabolic rate | mobile_app | yes (integration) |
| sensor.dagaphone_battery_cycle_count | Battery cycle count | mobile_app | yes (integration) |
| sensor.dagaphone_battery_health | Battery health | mobile_app | yes (integration) |
| sensor.dagaphone_battery_level | Battery level | mobile_app | no |
| sensor.dagaphone_battery_power | Battery power | mobile_app | yes (integration) |
| sensor.dagaphone_battery_state | Battery state | mobile_app | no |
| sensor.dagaphone_battery_temperature | Battery temperature | mobile_app | yes (integration) |
| sensor.dagaphone_beacon_monitor | Beacon monitor | mobile_app | yes (integration) |
| sensor.dagaphone_ble_transmitter | BLE transmitter | mobile_app | yes (integration) |
| sensor.dagaphone_blood_glucose | Blood glucose | mobile_app | yes (integration) |
| sensor.dagaphone_bluetooth_connection | Bluetooth connection | mobile_app | yes (integration) |
| sensor.dagaphone_body_fat | Body fat | mobile_app | yes (integration) |
| sensor.dagaphone_body_temperature | Body temperature | mobile_app | yes (integration) |
| sensor.dagaphone_body_water_mass | Body water mass | mobile_app | yes (integration) |
| sensor.dagaphone_bone_mass | Bone mass | mobile_app | yes (integration) |
| sensor.dagaphone_car_battery | Car battery | mobile_app | yes (integration) |
| sensor.dagaphone_car_charging_status | Car charging status | mobile_app | yes (integration) |
| sensor.dagaphone_car_ev_connector_type | Car EV connector type | mobile_app | yes (integration) |
| sensor.dagaphone_car_fuel | Car fuel | mobile_app | yes (integration) |
| sensor.dagaphone_car_fuel_type | Car fuel type | mobile_app | yes (integration) |
| sensor.dagaphone_car_name | Car name | mobile_app | yes (integration) |
| sensor.dagaphone_car_odometer | Car odometer | mobile_app | yes (integration) |
| sensor.dagaphone_car_range_remaining | Car range remaining | mobile_app | yes (integration) |
| sensor.dagaphone_car_speed | Car speed | mobile_app | yes (integration) |
| sensor.dagaphone_charger_type | Charger type | mobile_app | no |
| sensor.dagaphone_current_time_zone | Current time zone | mobile_app | yes (integration) |
| sensor.dagaphone_current_version | Current version | mobile_app | yes (integration) |
| sensor.dagaphone_daily_distance | Daily distance | mobile_app | yes (integration) |
| sensor.dagaphone_daily_elevation_gained | Daily elevation gained | mobile_app | yes (integration) |
| sensor.dagaphone_daily_floors | Daily floors | mobile_app | yes (integration) |
| sensor.dagaphone_daily_hydration | Daily hydration | mobile_app | yes (integration) |
| sensor.dagaphone_daily_steps | Daily steps | mobile_app | yes (integration) |
| sensor.dagaphone_data_network_type_sim_1 | Data network type (SIM 1) | mobile_app | yes (integration) |
| sensor.dagaphone_data_network_type_sim_2 | Data network type (SIM 2) | mobile_app | yes (integration) |
| sensor.dagaphone_detected_activity | Detected activity | mobile_app | yes (integration) |
| sensor.dagaphone_diastolic_blood_pressure | Diastolic blood pressure | mobile_app | yes (integration) |
| sensor.dagaphone_do_not_disturb_sensor | Do Not Disturb sensor | mobile_app | yes (integration) |
| sensor.dagaphone_external_storage | External storage | mobile_app | yes (integration) |
| sensor.dagaphone_geocoded_location | Geocoded location | mobile_app | yes (integration) |
| sensor.dagaphone_heart_rate | Heart rate | mobile_app | yes (integration) |
| sensor.dagaphone_heart_rate_variability | Heart rate variability | mobile_app | yes (integration) |
| sensor.dagaphone_height | Height | mobile_app | yes (integration) |
| sensor.dagaphone_high_accuracy_update_interval | High accuracy update interval | mobile_app | yes (integration) |
| sensor.dagaphone_internal_storage | Internal storage | mobile_app | yes (integration) |
| sensor.dagaphone_ipv6_addresses | IPv6 addresses | mobile_app | yes (integration) |
| sensor.dagaphone_last_notification | Last notification | mobile_app | yes (integration) |
| sensor.dagaphone_last_reboot | Last reboot | mobile_app | yes (integration) |
| sensor.dagaphone_last_removed_notification | Last removed notification | mobile_app | yes (integration) |
| sensor.dagaphone_last_update_trigger | Last update trigger | mobile_app | yes (integration) |
| sensor.dagaphone_last_used_app | Last used app | mobile_app | yes (integration) |
| sensor.dagaphone_lean_body_mass | Lean body mass | mobile_app | yes (integration) |
| sensor.dagaphone_light_sensor | Light sensor | mobile_app | yes (integration) |
| sensor.dagaphone_media_session | Media session | mobile_app | yes (integration) |
| sensor.dagaphone_mobile_rx_gb | Mobile Rx GB | mobile_app | yes (integration) |
| sensor.dagaphone_mobile_tx_gb | Mobile Tx GB | mobile_app | yes (integration) |
| sensor.dagaphone_network_type | Network type | mobile_app | yes (integration) |
| sensor.dagaphone_next_alarm | Next alarm | mobile_app | yes (integration) |
| sensor.dagaphone_os_version | OS version | mobile_app | yes (integration) |
| sensor.dagaphone_oxygen_saturation | Oxygen saturation | mobile_app | yes (integration) |
| sensor.dagaphone_phone_state | Phone state | mobile_app | yes (integration) |
| sensor.dagaphone_pressure_sensor | Pressure sensor | mobile_app | yes (integration) |
| sensor.dagaphone_proximity_sensor | Proximity sensor | mobile_app | yes (integration) |
| sensor.dagaphone_public_ip_address | Public IP address | mobile_app | yes (integration) |
| sensor.dagaphone_remaining_charge_time | Remaining charge time | mobile_app | yes (integration) |
| sensor.dagaphone_respiratory_rate | Respiratory rate | mobile_app | yes (integration) |
| sensor.dagaphone_resting_heart_rate | Resting heart rate | mobile_app | yes (integration) |
| sensor.dagaphone_ringer_mode | Ringer mode | mobile_app | yes (integration) |
| sensor.dagaphone_screen_brightness | Screen brightness | mobile_app | yes (integration) |
| sensor.dagaphone_screen_off_timeout | Screen off timeout | mobile_app | yes (integration) |
| sensor.dagaphone_screen_orientation | Screen orientation | mobile_app | yes (integration) |
| sensor.dagaphone_screen_rotation | Screen rotation | mobile_app | yes (integration) |
| sensor.dagaphone_security_patch | Security patch | mobile_app | yes (integration) |
| sensor.dagaphone_signal_strength_sim_1 | Signal strength (SIM 1) | mobile_app | yes (integration) |
| sensor.dagaphone_signal_strength_sim_2 | Signal strength (SIM 2) | mobile_app | yes (integration) |
| sensor.dagaphone_sim_1 | SIM 1 | mobile_app | yes (integration) |
| sensor.dagaphone_sim_2 | SIM 2 | mobile_app | yes (integration) |
| sensor.dagaphone_sleep_confidence | Sleep confidence | mobile_app | yes (integration) |
| sensor.dagaphone_sleep_duration | Sleep duration | mobile_app | yes (integration) |
| sensor.dagaphone_sleep_segment | Sleep segment | mobile_app | yes (integration) |
| sensor.dagaphone_steps_sensor | Steps sensor | mobile_app | yes (integration) |
| sensor.dagaphone_systolic_blood_pressure | Systolic blood pressure | mobile_app | yes (integration) |
| sensor.dagaphone_total_calories_burned | Total calories burned | mobile_app | yes (integration) |
| sensor.dagaphone_total_rx_gb | Total Rx GB | mobile_app | yes (integration) |
| sensor.dagaphone_total_tx_gb | Total Tx GB | mobile_app | yes (integration) |
| sensor.dagaphone_vo2_max | VO2 max | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_accessibility | Volume level accessibility | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_alarm | Volume level alarm | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_call | Volume level call | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_dtmf | Volume level DTMF | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_music | Volume level music | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_notification | Volume level notification | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_ringer | Volume level ringer | mobile_app | yes (integration) |
| sensor.dagaphone_volume_level_system | Volume level system | mobile_app | yes (integration) |
| sensor.dagaphone_weight | Weight | mobile_app | yes (integration) |
| sensor.dagaphone_wi_fi_bssid | Wi-Fi BSSID | mobile_app | yes (integration) |
| sensor.dagaphone_wi_fi_connection | Wi-Fi connection | mobile_app | yes (integration) |
| sensor.dagaphone_wi_fi_frequency | Wi-Fi frequency | mobile_app | yes (integration) |
| sensor.dagaphone_wi_fi_ip_address | Wi-Fi IP address | mobile_app | yes (integration) |
| sensor.dagaphone_wi_fi_link_speed | Wi-Fi link speed | mobile_app | yes (integration) |
| sensor.dagaphone_wi_fi_signal_strength | Wi-Fi signal strength | mobile_app | yes (integration) |

## ESPHome Device Builder

- Device ID: c9e4296bd1ca0eb226b8dbb3f0f1569f
- Manufacturer: ESPHome
- Model: Home Assistant App
- Software Version: 2026.4.5
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.esphome_device_builder_running | Running | hassio | yes (integration) |
| sensor.esphome_device_builder_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.esphome_device_builder_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.esphome_device_builder_newest_version | Newest version | hassio | yes (integration) |
| sensor.esphome_device_builder_version | Version | hassio | yes (integration) |
| switch.esphome_device_builder | - | hassio | yes (integration) |
| update.esphome_device_builder_update | Update | hassio | no |

## File editor

- Device ID: 87a11da1d046b63af1dd5949ff0e6ee3
- Manufacturer: Official apps
- Model: Home Assistant App
- Software Version: 6.0.0
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.file_editor_running | Running | hassio | yes (integration) |
| sensor.file_editor_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.file_editor_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.file_editor_newest_version | Newest version | hassio | yes (integration) |
| sensor.file_editor_version | Version | hassio | yes (integration) |
| switch.file_editor | - | hassio | yes (integration) |
| update.file_editor_update | Update | hassio | no |

## FloorHeating

- Device ID: 6c955f318f6506f017acdd79acdafa7c
- Manufacturer: Shelly
- Model: Shelly 1 Gen4
- Software Version: 20260311-095901/1.7.5-g9979d16
- Hardware Version: gen4
- Area ID: jaskier

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.floorheating_cloud | Cloud | shelly | yes (integration) |
| binary_sensor.floorheating_input_0 | Input 0 | shelly | no |
| binary_sensor.floorheating_restart_required | Restart required | shelly | yes (integration) |
| button.floorheating_restart | Restart | shelly | no |
| sensor.floorheating_last_restart | Uptime | shelly | yes (integration) |
| sensor.floorheating_signal_strength | Signal strength | shelly | yes (integration) |
| sensor.floorheating_temperature | Temperature | shelly | yes (integration) |
| switch.floorheating | - | shelly | no |
| update.floorheating_beta_firmware | Beta firmware | shelly | yes (integration) |
| update.floorheating_firmware | Firmware | shelly | no |

## Forecast

- Device ID: ff210150842afff0739b76a3d84192e4
- Manufacturer: Met.no
- Model: Forecast
- Software Version: -
- Hardware Version: -
- Area ID: outside

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| weather.forecast_home | Jaskier | met | no |

## Generator (ID: 4)

- Device ID: 33d465433bd02a6da9eaf7ee5153c11b
- Manufacturer: Victron Energy
- Model: Generator
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.generator_id_4_alarm | Alarm | victron_gx | no |
| sensor.generator_id_4_raw_state | Raw state | victron_gx | no |
| sensor.generator_id_4_state | State | victron_gx | no |
| sensor.generator_id_4_type | Type | victron_gx | no |
| switch.generator_id_4_invert_digital_input | Invert digital input | victron_gx | no |

## Get HACS

- Device ID: 4185a5c2011c58a27393ac6bbc6e4c17
- Manufacturer: Home Assistant Community Store
- Model: Home Assistant App
- Software Version: 1.3.1
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.get_hacs_running | Running | hassio | yes (integration) |
| sensor.get_hacs_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.get_hacs_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.get_hacs_newest_version | Newest version | hassio | yes (integration) |
| sensor.get_hacs_version | Version | hassio | yes (integration) |
| switch.get_hacs | - | hassio | yes (integration) |
| update.get_hacs_update | Update | hassio | no |

## Git pull

- Device ID: acb210acde5f4295216a694d55d8f7a1
- Manufacturer: Official apps
- Model: Home Assistant App
- Software Version: 9.0.1
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.git_pull_running | Running | hassio | yes (integration) |
| sensor.git_pull_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.git_pull_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.git_pull_newest_version | Newest version | hassio | yes (integration) |
| sensor.git_pull_version | Version | hassio | yes (integration) |
| switch.git_pull | - | hassio | yes (integration) |
| update.git_pull_update | Update | hassio | no |

## Google Translate en com

- Device ID: cd6e1084f4838071c5710a1eb2a97343
- Manufacturer: Google
- Model: Google Translate TTS
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| tts.google_translate_en_com | - | google_translate | no |

## GX Device

- Device ID: 46b83e1cfe1d2f4b3f1b41016130104a
- Manufacturer: Victron Energy
- Model: GX Device
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.gx_device_dynamic_ess_active | Dynamic ESS active | victron_gx | no |
| binary_sensor.gx_device_dynamic_ess_available | Dynamic ESS available | victron_gx | no |
| number.gx_device_ac_export_limit | AC export limit | victron_gx | no |
| number.gx_device_ac_input_limit | AC input limit | victron_gx | no |
| number.gx_device_ac_power_setpoint | AC power setpoint | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_0_duration | ESS BatteryLife schedule charge 0 duration | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_0_soc | ESS BatteryLife schedule charge 0 SoC | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_1_duration | ESS BatteryLife schedule charge 1 duration | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_1_soc | ESS BatteryLife schedule charge 1 SoC | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_2_duration | ESS BatteryLife schedule charge 2 duration | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_2_soc | ESS BatteryLife schedule charge 2 SoC | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_3_duration | ESS BatteryLife schedule charge 3 duration | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_3_soc | ESS BatteryLife schedule charge 3 SoC | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_4_duration | ESS BatteryLife schedule charge 4 duration | victron_gx | no |
| number.gx_device_ess_batterylife_schedule_charge_4_soc | ESS BatteryLife schedule charge 4 SoC | victron_gx | no |
| number.gx_device_ess_max_charge_current | ESS max charge current | victron_gx | no |
| number.gx_device_ess_max_charge_power_limit | ESS max charge power limit | victron_gx | no |
| number.gx_device_ess_max_charge_voltage | ESS max charge voltage | victron_gx | no |
| number.gx_device_ess_max_feed_in_power | ESS max feed-in power | victron_gx | no |
| number.gx_device_ess_max_inverter_power_limit | ESS max inverter power limit | victron_gx | no |
| number.gx_device_ess_min_soc_limit | ESS min SoC limit | victron_gx | no |
| select.gx_device_dess_mode | DESS mode | victron_gx | no |
| select.gx_device_ess_batterylife_schedule_charge_0_days | ESS BatteryLife schedule charge 0 days | victron_gx | no |
| select.gx_device_ess_batterylife_schedule_charge_1_days | ESS BatteryLife schedule charge 1 days | victron_gx | no |
| select.gx_device_ess_batterylife_schedule_charge_2_days | ESS BatteryLife schedule charge 2 days | victron_gx | no |
| select.gx_device_ess_batterylife_schedule_charge_3_days | ESS BatteryLife schedule charge 3 days | victron_gx | no |
| select.gx_device_ess_batterylife_schedule_charge_4_days | ESS BatteryLife schedule charge 4 days | victron_gx | no |
| select.gx_device_ess_batterylife_state | ESS BatteryLife state | victron_gx | no |
| select.gx_device_ess_mode_hub4 | ESS mode (Hub4) | victron_gx | no |
| sensor.gx_device_ac_active_input_source | AC active input source | victron_gx | no |
| sensor.gx_device_consumption_current_l1 | Consumption current L1 | victron_gx | no |
| sensor.gx_device_consumption_on_output_phases | Consumption on output phases | victron_gx | no |
| sensor.gx_device_consumption_phases | Consumption phases | victron_gx | no |
| sensor.gx_device_consumption_power_l1 | Consumption power L1 | victron_gx | no |
| sensor.gx_device_critical_loads_on_l1 | Critical loads on L1 | victron_gx | no |
| sensor.gx_device_dc_alternator_power | DC alternator power | victron_gx | no |
| sensor.gx_device_dc_battery_charge | DC battery charge | victron_gx | no |
| sensor.gx_device_dc_battery_charge_energy | DC battery charge energy | victron_gx | no |
| sensor.gx_device_dc_battery_current | DC battery current | victron_gx | no |
| sensor.gx_device_dc_battery_discharge_energy | DC battery discharge energy | victron_gx | no |
| sensor.gx_device_dc_battery_power | DC battery power | victron_gx | no |
| sensor.gx_device_dc_battery_state | DC battery state | victron_gx | no |
| sensor.gx_device_dc_battery_voltage | DC battery voltage | victron_gx | no |
| sensor.gx_device_dc_consumption | DC consumption | victron_gx | no |
| sensor.gx_device_dynamic_ess_error | Dynamic ESS error | victron_gx | no |
| sensor.gx_device_dynamic_ess_number_of_schedules | Dynamic ESS number of schedules | victron_gx | no |
| sensor.gx_device_dynamic_ess_reactive_strategy | Dynamic ESS reactive strategy | victron_gx | no |
| sensor.gx_device_dynamic_ess_target_soc | Dynamic ESS target SoC | victron_gx | no |
| sensor.gx_device_grid_phases | Grid phases | victron_gx | no |
| sensor.gx_device_gx_system_heartbeat | GX system heartbeat | victron_gx | yes (integration) |
| sensor.gx_device_installed_version | Installed version | victron_gx | no |
| sensor.gx_device_pv_current | PV current | victron_gx | no |
| sensor.gx_device_pv_energy | PV energy | victron_gx | no |
| sensor.gx_device_pv_power | PV power | victron_gx | no |
| sensor.gx_device_relay_0_custom_name | Relay 0 custom name | victron_gx | no |
| sensor.gx_device_relay_1_custom_name | Relay 1 custom name | victron_gx | no |
| sensor.gx_device_system_state | System state | victron_gx | no |
| switch.gx_device_ess_batterylife_schedule_charge_0_enabled | ESS BatteryLife schedule charge 0 enabled | victron_gx | no |
| switch.gx_device_ess_batterylife_schedule_charge_1_enabled | ESS BatteryLife schedule charge 1 enabled | victron_gx | no |
| switch.gx_device_ess_batterylife_schedule_charge_2_enabled | ESS BatteryLife schedule charge 2 enabled | victron_gx | no |
| switch.gx_device_ess_batterylife_schedule_charge_3_enabled | ESS BatteryLife schedule charge 3 enabled | victron_gx | no |
| switch.gx_device_ess_batterylife_schedule_charge_4_enabled | ESS BatteryLife schedule charge 4 enabled | victron_gx | no |
| switch.gx_device_ess_only_critical_loads_from_battery | ESS only critical loads from battery | victron_gx | no |
| switch.gx_device_pv_dc_overvoltage_feed_in | PV DC overvoltage feed-in | victron_gx | no |
| switch.gx_device_relay_0_state | Relay 0 state | victron_gx | no |
| switch.gx_device_relay_1_state | Relay 1 state | victron_gx | no |
| time.gx_device_ess_batterylife_schedule_charge_0_start | ESS BatteryLife schedule charge 0 start | victron_gx | no |
| time.gx_device_ess_batterylife_schedule_charge_1_start | ESS BatteryLife schedule charge 1 start | victron_gx | no |
| time.gx_device_ess_batterylife_schedule_charge_2_start | ESS BatteryLife schedule charge 2 start | victron_gx | no |
| time.gx_device_ess_batterylife_schedule_charge_3_start | ESS BatteryLife schedule charge 3 start | victron_gx | no |
| time.gx_device_ess_batterylife_schedule_charge_4_start | ESS BatteryLife schedule charge 4 start | victron_gx | no |

## GX internal relay 2

- Device ID: bf4660033ddab1f05f9e7e528ef3d88f
- Manufacturer: Victron Energy
- Model: GX internal relay 2
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| switch.gx_internal_relay_2_state | State | victron_gx | no |

## HACS

- Device ID: 8345f9a3247a5635c6b08dd3f0d8d3fc
- Manufacturer: hacs.xyz
- Model: -
- Software Version: 2.0.5
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| switch.hacs_pre_release | Pre-release | hacs | yes (integration) |
| update.hacs_update | Update | hacs | no |

## Home Assistant Core

- Device ID: d26a1e8b86389878d21df87ede9b6e2b
- Manufacturer: Home Assistant
- Model: Home Assistant Core
- Software Version: 2026.5.0
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.home_assistant_core_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.home_assistant_core_memory_percent | Memory percent | hassio | yes (integration) |
| update.home_assistant_core_update | Update | hassio | no |

## Home Assistant Host

- Device ID: ccc136280dbfde487711d041d82a19f7
- Manufacturer: Home Assistant
- Model: Home Assistant Host
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.home_assistant_host_apparmor_version | AppArmor version | hassio | yes (integration) |
| sensor.home_assistant_host_disk_free | Disk free | hassio | yes (integration) |
| sensor.home_assistant_host_disk_total | Disk total | hassio | yes (integration) |
| sensor.home_assistant_host_disk_used | Disk used | hassio | yes (integration) |
| sensor.home_assistant_host_os_agent_version | OS Agent version | hassio | yes (integration) |

## Home Assistant Operating System

- Device ID: 5239c4c26726c388b882104ddc191aed
- Manufacturer: Home Assistant
- Model: Home Assistant Operating System
- Software Version: 17.3
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.home_assistant_operating_system_newest_version | Newest version | hassio | yes (integration) |
| sensor.home_assistant_operating_system_version | Version | hassio | yes (integration) |
| update.home_assistant_operating_system_update | Update | hassio | no |

## Home Assistant Supervisor

- Device ID: 6eadd3e7fa1d4992b0435695ddd417e9
- Manufacturer: Home Assistant
- Model: Home Assistant Supervisor
- Software Version: 2026.05.0
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.home_assistant_supervisor_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.home_assistant_supervisor_memory_percent | Memory percent | hassio | yes (integration) |
| update.home_assistant_supervisor_update | Update | hassio | no |

## Inverter

- Device ID: 233378516e5bcdebbe4386a2f20f606e
- Manufacturer: Victron Energy
- Model: MultiPlus-II 12/3000/120-32
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.inverter_connected | Connected | victron_gx | no |
| number.inverter_assist_current_boost_factor | Assist current boost factor | victron_gx | no |
| number.inverter_current_limit | Current limit | victron_gx | no |
| select.inverter | - | victron_gx | no |
| sensor.inverter_0_inverted_power | 0 inverted power | victron_gx | no |
| sensor.inverter_0_line_1_input_power | 0 line 1 input power | victron_gx | no |
| sensor.inverter_0_line_1_output_power | 0 line 1 output power | victron_gx | no |
| sensor.inverter_0_line_l2_input_power | 0 line L2 input power | victron_gx | no |
| sensor.inverter_0_line_l2_output_power | 0 line L2 output power | victron_gx | no |
| sensor.inverter_active_ac_input | Active AC input | victron_gx | no |
| sensor.inverter_dc_current | DC current | victron_gx | no |
| sensor.inverter_dc_power | DC power | victron_gx | no |
| sensor.inverter_dc_temperature | DC temperature | victron_gx | no |
| sensor.inverter_dc_voltage | DC voltage | victron_gx | no |
| sensor.inverter_energy_from_ac_in_1_to_ac_out | Energy from AC-in-1 to AC-out | victron_gx | no |
| sensor.inverter_energy_from_ac_in_1_to_inverter | Energy from AC-in-1 to inverter | victron_gx | no |
| sensor.inverter_energy_from_ac_in_2_to_ac_out | Energy from AC-in-2 to AC-out | victron_gx | no |
| sensor.inverter_energy_from_ac_in_2_to_inverter | Energy from AC-in-2 to inverter | victron_gx | no |
| sensor.inverter_energy_from_ac_out_to_ac_in_1 | Energy from AC-out to AC-in-1 | victron_gx | no |
| sensor.inverter_energy_from_ac_out_to_ac_in_2 | Energy from AC-out to AC-in-2 | victron_gx | no |
| sensor.inverter_energy_from_inverter_to_ac_in_1 | Energy from inverter to AC-in-1 | victron_gx | no |
| sensor.inverter_energy_from_inverter_to_ac_in_2 | Energy from inverter to AC-in-2 | victron_gx | no |
| sensor.inverter_energy_from_inverter_to_ac_out | Energy from inverter to AC-out | victron_gx | no |
| sensor.inverter_energy_from_out_to_inverter | Energy from out to inverter | victron_gx | no |
| sensor.inverter_grid_lost_alarm | Grid lost alarm | victron_gx | no |
| sensor.inverter_high_dc_current_alarm | High DC current alarm | victron_gx | no |
| sensor.inverter_high_dc_voltage_alarm | High DC voltage alarm | victron_gx | no |
| sensor.inverter_high_temperature_alarm | High temperature alarm | victron_gx | no |
| sensor.inverter_input_apparent_power_l1 | Input apparent power L1 | victron_gx | no |
| sensor.inverter_input_current_l1 | Input current L1 | victron_gx | no |
| sensor.inverter_input_frequency_l1 | Input frequency L1 | victron_gx | no |
| sensor.inverter_input_power_l1 | Input power L1 | victron_gx | no |
| sensor.inverter_input_voltage_l1 | Input voltage L1 | victron_gx | no |
| sensor.inverter_low_battery_alarm | Low battery alarm | victron_gx | no |
| sensor.inverter_output_apparent_power_l1 | Output apparent power L1 | victron_gx | no |
| sensor.inverter_output_current_l1 | Output current L1 | victron_gx | no |
| sensor.inverter_output_frequency_l1 | Output frequency L1 | victron_gx | no |
| sensor.inverter_output_power_l1 | Output power L1 | victron_gx | no |
| sensor.inverter_output_voltage_l1 | Output voltage L1 | victron_gx | no |
| sensor.inverter_overload_alarm | Overload alarm | victron_gx | no |
| sensor.inverter_phase_rotation_alarm | Phase rotation alarm | victron_gx | no |
| sensor.inverter_ripple_alarm | Ripple alarm | victron_gx | no |
| sensor.inverter_state | State | victron_gx | no |
| sensor.inverter_state_of_ignore_ac_in_1 | State of ignore AC-in-1 | victron_gx | no |
| sensor.inverter_temperature_sensor_alarm | Temperature sensor alarm | victron_gx | no |
| sensor.inverter_voltage_sensor_alarm | Voltage sensor alarm | victron_gx | no |
| switch.inverter_0_powerassist_enabled | 0 PowerAssist enabled | victron_gx | no |
| switch.inverter_control_ignore_ac_in_1 | Control ignore AC-in-1 | victron_gx | no |
| switch.inverter_grid_lost_alarm_setting | Grid lost alarm setting | victron_gx | no |

## JaskierDash

- Device ID: 37ae670e9c2adae2cc4ef15aafb31f38
- Manufacturer: LENOVO
- Model: TB520FU
- Software Version: 34
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.jaskierdash_android_auto | Android Auto | mobile_app | no |
| binary_sensor.jaskierdash_app_inactive | App inactive | mobile_app | no |
| binary_sensor.jaskierdash_bluetooth_state | Bluetooth state | mobile_app | no |
| binary_sensor.jaskierdash_device_locked | Device locked | mobile_app | no |
| binary_sensor.jaskierdash_device_secure | Device secure | mobile_app | no |
| binary_sensor.jaskierdash_doze_mode | Doze mode | mobile_app | yes (integration) |
| binary_sensor.jaskierdash_headphones | Headphones | mobile_app | no |
| binary_sensor.jaskierdash_high_accuracy_mode | High accuracy mode | mobile_app | no |
| binary_sensor.jaskierdash_hotspot_state | Hotspot state | mobile_app | yes (integration) |
| binary_sensor.jaskierdash_interactive | Interactive | mobile_app | yes (integration) |
| binary_sensor.jaskierdash_is_charging | Is charging | mobile_app | no |
| binary_sensor.jaskierdash_keyguard_locked | Keyguard locked | mobile_app | yes (integration) |
| binary_sensor.jaskierdash_keyguard_secure | Keyguard secure | mobile_app | yes (integration) |
| binary_sensor.jaskierdash_mic_muted | Mic muted | mobile_app | no |
| binary_sensor.jaskierdash_music_active | Music active | mobile_app | no |
| binary_sensor.jaskierdash_power_save | Power save | mobile_app | yes (integration) |
| binary_sensor.jaskierdash_speakerphone | Speakerphone | mobile_app | no |
| binary_sensor.jaskierdash_wi_fi_state | Wi-Fi state | mobile_app | no |
| binary_sensor.jaskierdash_work_profile | Work profile | mobile_app | yes (integration) |
| device_tracker.jaskierdash | - | mobile_app | no |
| notify.jaskierdash | - | mobile_app | no |
| sensor.jaskierdash_accent_color | Accent color | mobile_app | no |
| sensor.jaskierdash_active_calories_burned | Active calories burned | mobile_app | yes (integration) |
| sensor.jaskierdash_active_notification_count | Active notification count | mobile_app | no |
| sensor.jaskierdash_app_importance | App importance | mobile_app | yes (integration) |
| sensor.jaskierdash_app_memory | App memory | mobile_app | yes (integration) |
| sensor.jaskierdash_app_rx_gb | App Rx GB | mobile_app | yes (integration) |
| sensor.jaskierdash_app_standby_bucket | App standby bucket | mobile_app | yes (integration) |
| sensor.jaskierdash_app_tx_gb | App Tx GB | mobile_app | yes (integration) |
| sensor.jaskierdash_audio_mode | Audio mode | mobile_app | no |
| sensor.jaskierdash_basal_body_temperature | Basal body temperature | mobile_app | yes (integration) |
| sensor.jaskierdash_basal_metabolic_rate | Basal metabolic rate | mobile_app | yes (integration) |
| sensor.jaskierdash_battery_cycle_count | Battery cycle count | mobile_app | yes (integration) |
| sensor.jaskierdash_battery_health | Battery health | mobile_app | yes (integration) |
| sensor.jaskierdash_battery_level | Battery level | mobile_app | no |
| sensor.jaskierdash_battery_power | Battery power | mobile_app | yes (integration) |
| sensor.jaskierdash_battery_state | Battery state | mobile_app | no |
| sensor.jaskierdash_battery_temperature | Battery temperature | mobile_app | no |
| sensor.jaskierdash_beacon_monitor | Beacon monitor | mobile_app | no |
| sensor.jaskierdash_ble_transmitter | BLE transmitter | mobile_app | no |
| sensor.jaskierdash_blood_glucose | Blood glucose | mobile_app | yes (integration) |
| sensor.jaskierdash_bluetooth_connection | Bluetooth connection | mobile_app | no |
| sensor.jaskierdash_body_fat | Body fat | mobile_app | yes (integration) |
| sensor.jaskierdash_body_temperature | Body temperature | mobile_app | yes (integration) |
| sensor.jaskierdash_body_water_mass | Body water mass | mobile_app | yes (integration) |
| sensor.jaskierdash_bone_mass | Bone mass | mobile_app | yes (integration) |
| sensor.jaskierdash_car_battery | Car battery | mobile_app | yes (integration) |
| sensor.jaskierdash_car_charging_status | Car charging status | mobile_app | yes (integration) |
| sensor.jaskierdash_car_ev_connector_type | Car EV connector type | mobile_app | yes (integration) |
| sensor.jaskierdash_car_fuel | Car fuel | mobile_app | yes (integration) |
| sensor.jaskierdash_car_fuel_type | Car fuel type | mobile_app | yes (integration) |
| sensor.jaskierdash_car_name | Car name | mobile_app | yes (integration) |
| sensor.jaskierdash_car_odometer | Car odometer | mobile_app | yes (integration) |
| sensor.jaskierdash_car_range_remaining | Car range remaining | mobile_app | yes (integration) |
| sensor.jaskierdash_car_speed | Car speed | mobile_app | yes (integration) |
| sensor.jaskierdash_charger_type | Charger type | mobile_app | no |
| sensor.jaskierdash_current_time_zone | Current time zone | mobile_app | no |
| sensor.jaskierdash_current_version | Current version | mobile_app | no |
| sensor.jaskierdash_daily_distance | Daily distance | mobile_app | yes (integration) |
| sensor.jaskierdash_daily_elevation_gained | Daily elevation gained | mobile_app | yes (integration) |
| sensor.jaskierdash_daily_floors | Daily floors | mobile_app | yes (integration) |
| sensor.jaskierdash_daily_hydration | Daily hydration | mobile_app | yes (integration) |
| sensor.jaskierdash_daily_steps | Daily steps | mobile_app | yes (integration) |
| sensor.jaskierdash_detected_activity | Detected activity | mobile_app | no |
| sensor.jaskierdash_diastolic_blood_pressure | Diastolic blood pressure | mobile_app | yes (integration) |
| sensor.jaskierdash_do_not_disturb_sensor | Do Not Disturb sensor | mobile_app | no |
| sensor.jaskierdash_external_storage | External storage | mobile_app | yes (integration) |
| sensor.jaskierdash_geocoded_location | Geocoded location | mobile_app | no |
| sensor.jaskierdash_heart_rate | Heart rate | mobile_app | yes (integration) |
| sensor.jaskierdash_heart_rate_variability | Heart rate variability | mobile_app | yes (integration) |
| sensor.jaskierdash_height | Height | mobile_app | yes (integration) |
| sensor.jaskierdash_high_accuracy_update_interval | High accuracy update interval | mobile_app | no |
| sensor.jaskierdash_internal_storage | Internal storage | mobile_app | yes (integration) |
| sensor.jaskierdash_ipv6_addresses | IPv6 addresses | mobile_app | yes (integration) |
| sensor.jaskierdash_last_notification | Last notification | mobile_app | no |
| sensor.jaskierdash_last_reboot | Last reboot | mobile_app | no |
| sensor.jaskierdash_last_removed_notification | Last removed notification | mobile_app | no |
| sensor.jaskierdash_last_update_trigger | Last update trigger | mobile_app | yes (integration) |
| sensor.jaskierdash_last_used_app | Last used app | mobile_app | yes (integration) |
| sensor.jaskierdash_lean_body_mass | Lean body mass | mobile_app | yes (integration) |
| sensor.jaskierdash_light_sensor | Light sensor | mobile_app | no |
| sensor.jaskierdash_media_session | Media session | mobile_app | no |
| sensor.jaskierdash_network_type | Network type | mobile_app | yes (integration) |
| sensor.jaskierdash_next_alarm | Next alarm | mobile_app | no |
| sensor.jaskierdash_os_version | OS version | mobile_app | no |
| sensor.jaskierdash_oxygen_saturation | Oxygen saturation | mobile_app | yes (integration) |
| sensor.jaskierdash_proximity_sensor | Proximity sensor | mobile_app | no |
| sensor.jaskierdash_public_ip_address | Public IP address | mobile_app | no |
| sensor.jaskierdash_remaining_charge_time | Remaining charge time | mobile_app | no |
| sensor.jaskierdash_respiratory_rate | Respiratory rate | mobile_app | yes (integration) |
| sensor.jaskierdash_resting_heart_rate | Resting heart rate | mobile_app | yes (integration) |
| sensor.jaskierdash_ringer_mode | Ringer mode | mobile_app | no |
| sensor.jaskierdash_screen_brightness | Screen brightness | mobile_app | no |
| sensor.jaskierdash_screen_off_timeout | Screen off timeout | mobile_app | no |
| sensor.jaskierdash_screen_orientation | Screen orientation | mobile_app | no |
| sensor.jaskierdash_screen_rotation | Screen rotation | mobile_app | no |
| sensor.jaskierdash_security_patch | Security patch | mobile_app | no |
| sensor.jaskierdash_sleep_confidence | Sleep confidence | mobile_app | yes (integration) |
| sensor.jaskierdash_sleep_duration | Sleep duration | mobile_app | yes (integration) |
| sensor.jaskierdash_sleep_segment | Sleep segment | mobile_app | yes (integration) |
| sensor.jaskierdash_steps_sensor | Steps sensor | mobile_app | yes (integration) |
| sensor.jaskierdash_systolic_blood_pressure | Systolic blood pressure | mobile_app | yes (integration) |
| sensor.jaskierdash_total_calories_burned | Total calories burned | mobile_app | yes (integration) |
| sensor.jaskierdash_total_rx_gb | Total Rx GB | mobile_app | yes (integration) |
| sensor.jaskierdash_total_tx_gb | Total Tx GB | mobile_app | yes (integration) |
| sensor.jaskierdash_vo2_max | VO2 max | mobile_app | yes (integration) |
| sensor.jaskierdash_volume_level_accessibility | Volume level accessibility | mobile_app | no |
| sensor.jaskierdash_volume_level_alarm | Volume level alarm | mobile_app | no |
| sensor.jaskierdash_volume_level_call | Volume level call | mobile_app | no |
| sensor.jaskierdash_volume_level_dtmf | Volume level DTMF | mobile_app | no |
| sensor.jaskierdash_volume_level_music | Volume level music | mobile_app | no |
| sensor.jaskierdash_volume_level_notification | Volume level notification | mobile_app | no |
| sensor.jaskierdash_volume_level_ringer | Volume level ringer | mobile_app | no |
| sensor.jaskierdash_volume_level_system | Volume level system | mobile_app | no |
| sensor.jaskierdash_weight | Weight | mobile_app | yes (integration) |
| sensor.jaskierdash_wi_fi_bssid | Wi-Fi BSSID | mobile_app | yes (integration) |
| sensor.jaskierdash_wi_fi_connection | Wi-Fi connection | mobile_app | no |
| sensor.jaskierdash_wi_fi_frequency | Wi-Fi frequency | mobile_app | yes (integration) |
| sensor.jaskierdash_wi_fi_ip_address | Wi-Fi IP address | mobile_app | no |
| sensor.jaskierdash_wi_fi_link_speed | Wi-Fi link speed | mobile_app | yes (integration) |
| sensor.jaskierdash_wi_fi_signal_strength | Wi-Fi signal strength | mobile_app | yes (integration) |

## Let's Encrypt

- Device ID: 79958a2afd66b81430e5463ad3cf3246
- Manufacturer: Official apps
- Model: Home Assistant App
- Software Version: 6.3.2
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.let_s_encrypt_running | Running | hassio | yes (integration) |
| sensor.let_s_encrypt_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.let_s_encrypt_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.let_s_encrypt_newest_version | Newest version | hassio | yes (integration) |
| sensor.let_s_encrypt_version | Version | hassio | yes (integration) |
| switch.let_s_encrypt | - | hassio | yes (integration) |
| update.let_s_encrypt_update | Update | hassio | no |

## Mosquitto broker

- Device ID: 7f73502836f13372cc7bc8e38e2b3649
- Manufacturer: Official apps
- Model: Home Assistant App
- Software Version: 7.1.0
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.mosquitto_broker_running | Running | hassio | yes (integration) |
| sensor.mosquitto_broker_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.mosquitto_broker_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.mosquitto_broker_newest_version | Newest version | hassio | yes (integration) |
| sensor.mosquitto_broker_version | Version | hassio | yes (integration) |
| switch.mosquitto_broker | - | hassio | yes (integration) |
| update.mosquitto_broker_update | Update | hassio | no |

## MSPhone29

- Device ID: 06d178ba250d70e38a4738d2578aa6e3
- Manufacturer: Ulefone
- Model: Armor 29 Pro
- Software Version: 35
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.msphone29_android_auto | Android Auto | mobile_app | no |
| binary_sensor.msphone29_app_inactive | App inactive | mobile_app | yes (integration) |
| binary_sensor.msphone29_bluetooth_state | Bluetooth state | mobile_app | yes (integration) |
| binary_sensor.msphone29_device_locked | Device locked | mobile_app | yes (integration) |
| binary_sensor.msphone29_device_secure | Device secure | mobile_app | yes (integration) |
| binary_sensor.msphone29_doze_mode | Doze mode | mobile_app | yes (integration) |
| binary_sensor.msphone29_headphones | Headphones | mobile_app | yes (integration) |
| binary_sensor.msphone29_high_accuracy_mode | High accuracy mode | mobile_app | yes (integration) |
| binary_sensor.msphone29_hotspot_state | Hotspot state | mobile_app | yes (integration) |
| binary_sensor.msphone29_interactive | Interactive | mobile_app | yes (integration) |
| binary_sensor.msphone29_is_charging | Is charging | mobile_app | yes (integration) |
| binary_sensor.msphone29_keyguard_locked | Keyguard locked | mobile_app | yes (integration) |
| binary_sensor.msphone29_keyguard_secure | Keyguard secure | mobile_app | yes (integration) |
| binary_sensor.msphone29_mic_muted | Mic muted | mobile_app | yes (integration) |
| binary_sensor.msphone29_mobile_data | Mobile data | mobile_app | yes (integration) |
| binary_sensor.msphone29_mobile_data_roaming | Mobile data roaming | mobile_app | yes (integration) |
| binary_sensor.msphone29_music_active | Music active | mobile_app | yes (integration) |
| binary_sensor.msphone29_nfc_state | NFC state | mobile_app | yes (integration) |
| binary_sensor.msphone29_power_save | Power save | mobile_app | yes (integration) |
| binary_sensor.msphone29_speakerphone | Speakerphone | mobile_app | yes (integration) |
| binary_sensor.msphone29_wi_fi_state | Wi-Fi state | mobile_app | yes (integration) |
| binary_sensor.msphone29_work_profile | Work profile | mobile_app | yes (integration) |
| device_tracker.msphone29 | - | mobile_app | no |
| notify.msphone29 | - | mobile_app | no |
| sensor.msphone29_accent_color | Accent color | mobile_app | yes (integration) |
| sensor.msphone29_active_calories_burned | Active calories burned | mobile_app | yes (integration) |
| sensor.msphone29_active_notification_count | Active notification count | mobile_app | yes (integration) |
| sensor.msphone29_app_importance | App importance | mobile_app | yes (integration) |
| sensor.msphone29_app_memory | App memory | mobile_app | yes (integration) |
| sensor.msphone29_app_rx_gb | App Rx GB | mobile_app | yes (integration) |
| sensor.msphone29_app_standby_bucket | App standby bucket | mobile_app | yes (integration) |
| sensor.msphone29_app_tx_gb | App Tx GB | mobile_app | yes (integration) |
| sensor.msphone29_audio_mode | Audio mode | mobile_app | yes (integration) |
| sensor.msphone29_basal_body_temperature | Basal body temperature | mobile_app | yes (integration) |
| sensor.msphone29_basal_metabolic_rate | Basal metabolic rate | mobile_app | yes (integration) |
| sensor.msphone29_battery_cycle_count | Battery cycle count | mobile_app | yes (integration) |
| sensor.msphone29_battery_health | Battery health | mobile_app | yes (integration) |
| sensor.msphone29_battery_level | Battery level | mobile_app | no |
| sensor.msphone29_battery_power | Battery power | mobile_app | yes (integration) |
| sensor.msphone29_battery_state | Battery state | mobile_app | no |
| sensor.msphone29_battery_temperature | Battery temperature | mobile_app | yes (integration) |
| sensor.msphone29_beacon_monitor | Beacon monitor | mobile_app | yes (integration) |
| sensor.msphone29_ble_transmitter | BLE transmitter | mobile_app | yes (integration) |
| sensor.msphone29_blood_glucose | Blood glucose | mobile_app | yes (integration) |
| sensor.msphone29_bluetooth_connection | Bluetooth connection | mobile_app | yes (integration) |
| sensor.msphone29_body_fat | Body fat | mobile_app | yes (integration) |
| sensor.msphone29_body_temperature | Body temperature | mobile_app | yes (integration) |
| sensor.msphone29_body_water_mass | Body water mass | mobile_app | yes (integration) |
| sensor.msphone29_bone_mass | Bone mass | mobile_app | yes (integration) |
| sensor.msphone29_car_battery | Car battery | mobile_app | yes (integration) |
| sensor.msphone29_car_charging_status | Car charging status | mobile_app | yes (integration) |
| sensor.msphone29_car_ev_connector_type | Car EV connector type | mobile_app | yes (integration) |
| sensor.msphone29_car_fuel | Car fuel | mobile_app | yes (integration) |
| sensor.msphone29_car_fuel_type | Car fuel type | mobile_app | yes (integration) |
| sensor.msphone29_car_name | Car name | mobile_app | yes (integration) |
| sensor.msphone29_car_odometer | Car odometer | mobile_app | yes (integration) |
| sensor.msphone29_car_range_remaining | Car range remaining | mobile_app | yes (integration) |
| sensor.msphone29_car_speed | Car speed | mobile_app | yes (integration) |
| sensor.msphone29_charger_type | Charger type | mobile_app | no |
| sensor.msphone29_current_time_zone | Current time zone | mobile_app | yes (integration) |
| sensor.msphone29_current_version | Current version | mobile_app | yes (integration) |
| sensor.msphone29_daily_distance | Daily distance | mobile_app | yes (integration) |
| sensor.msphone29_daily_elevation_gained | Daily elevation gained | mobile_app | yes (integration) |
| sensor.msphone29_daily_floors | Daily floors | mobile_app | yes (integration) |
| sensor.msphone29_daily_hydration | Daily hydration | mobile_app | yes (integration) |
| sensor.msphone29_daily_steps | Daily steps | mobile_app | yes (integration) |
| sensor.msphone29_data_network_type_sim_1 | Data network type (SIM 1) | mobile_app | yes (integration) |
| sensor.msphone29_data_network_type_sim_2 | Data network type (SIM 2) | mobile_app | yes (integration) |
| sensor.msphone29_detected_activity | Detected activity | mobile_app | yes (integration) |
| sensor.msphone29_diastolic_blood_pressure | Diastolic blood pressure | mobile_app | yes (integration) |
| sensor.msphone29_do_not_disturb_sensor | Do Not Disturb sensor | mobile_app | yes (integration) |
| sensor.msphone29_external_storage | External storage | mobile_app | yes (integration) |
| sensor.msphone29_geocoded_location | Geocoded location | mobile_app | yes (integration) |
| sensor.msphone29_heart_rate | Heart rate | mobile_app | yes (integration) |
| sensor.msphone29_heart_rate_variability | Heart rate variability | mobile_app | yes (integration) |
| sensor.msphone29_height | Height | mobile_app | yes (integration) |
| sensor.msphone29_high_accuracy_update_interval | High accuracy update interval | mobile_app | yes (integration) |
| sensor.msphone29_internal_storage | Internal storage | mobile_app | yes (integration) |
| sensor.msphone29_ipv6_addresses | IPv6 addresses | mobile_app | yes (integration) |
| sensor.msphone29_last_notification | Last notification | mobile_app | yes (integration) |
| sensor.msphone29_last_reboot | Last reboot | mobile_app | yes (integration) |
| sensor.msphone29_last_removed_notification | Last removed notification | mobile_app | yes (integration) |
| sensor.msphone29_last_update_trigger | Last update trigger | mobile_app | yes (integration) |
| sensor.msphone29_last_used_app | Last used app | mobile_app | yes (integration) |
| sensor.msphone29_lean_body_mass | Lean body mass | mobile_app | yes (integration) |
| sensor.msphone29_light_sensor | Light sensor | mobile_app | yes (integration) |
| sensor.msphone29_media_session | Media session | mobile_app | yes (integration) |
| sensor.msphone29_mobile_rx_gb | Mobile Rx GB | mobile_app | yes (integration) |
| sensor.msphone29_mobile_tx_gb | Mobile Tx GB | mobile_app | yes (integration) |
| sensor.msphone29_network_type | Network type | mobile_app | yes (integration) |
| sensor.msphone29_next_alarm | Next alarm | mobile_app | yes (integration) |
| sensor.msphone29_os_version | OS version | mobile_app | yes (integration) |
| sensor.msphone29_oxygen_saturation | Oxygen saturation | mobile_app | yes (integration) |
| sensor.msphone29_phone_state | Phone state | mobile_app | yes (integration) |
| sensor.msphone29_pressure_sensor | Pressure sensor | mobile_app | yes (integration) |
| sensor.msphone29_proximity_sensor | Proximity sensor | mobile_app | yes (integration) |
| sensor.msphone29_public_ip_address | Public IP address | mobile_app | yes (integration) |
| sensor.msphone29_remaining_charge_time | Remaining charge time | mobile_app | yes (integration) |
| sensor.msphone29_respiratory_rate | Respiratory rate | mobile_app | yes (integration) |
| sensor.msphone29_resting_heart_rate | Resting heart rate | mobile_app | yes (integration) |
| sensor.msphone29_ringer_mode | Ringer mode | mobile_app | yes (integration) |
| sensor.msphone29_screen_brightness | Screen brightness | mobile_app | yes (integration) |
| sensor.msphone29_screen_off_timeout | Screen off timeout | mobile_app | yes (integration) |
| sensor.msphone29_screen_orientation | Screen orientation | mobile_app | yes (integration) |
| sensor.msphone29_screen_rotation | Screen rotation | mobile_app | yes (integration) |
| sensor.msphone29_security_patch | Security patch | mobile_app | yes (integration) |
| sensor.msphone29_signal_strength_sim_1 | Signal strength (SIM 1) | mobile_app | yes (integration) |
| sensor.msphone29_signal_strength_sim_2 | Signal strength (SIM 2) | mobile_app | yes (integration) |
| sensor.msphone29_sim_1 | SIM 1 | mobile_app | yes (integration) |
| sensor.msphone29_sim_2 | SIM 2 | mobile_app | yes (integration) |
| sensor.msphone29_sleep_confidence | Sleep confidence | mobile_app | no |
| sensor.msphone29_sleep_duration | Sleep duration | mobile_app | yes (integration) |
| sensor.msphone29_sleep_segment | Sleep segment | mobile_app | no |
| sensor.msphone29_steps_sensor | Steps sensor | mobile_app | yes (integration) |
| sensor.msphone29_systolic_blood_pressure | Systolic blood pressure | mobile_app | yes (integration) |
| sensor.msphone29_total_calories_burned | Total calories burned | mobile_app | yes (integration) |
| sensor.msphone29_total_rx_gb | Total Rx GB | mobile_app | yes (integration) |
| sensor.msphone29_total_tx_gb | Total Tx GB | mobile_app | yes (integration) |
| sensor.msphone29_vo2_max | VO2 max | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_accessibility | Volume level accessibility | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_alarm | Volume level alarm | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_call | Volume level call | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_dtmf | Volume level DTMF | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_music | Volume level music | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_notification | Volume level notification | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_ringer | Volume level ringer | mobile_app | yes (integration) |
| sensor.msphone29_volume_level_system | Volume level system | mobile_app | yes (integration) |
| sensor.msphone29_weight | Weight | mobile_app | yes (integration) |
| sensor.msphone29_wi_fi_bssid | Wi-Fi BSSID | mobile_app | yes (integration) |
| sensor.msphone29_wi_fi_connection | Wi-Fi connection | mobile_app | yes (integration) |
| sensor.msphone29_wi_fi_frequency | Wi-Fi frequency | mobile_app | yes (integration) |
| sensor.msphone29_wi_fi_ip_address | Wi-Fi IP address | mobile_app | yes (integration) |
| sensor.msphone29_wi_fi_link_speed | Wi-Fi link speed | mobile_app | yes (integration) |
| sensor.msphone29_wi_fi_signal_strength | Wi-Fi signal strength | mobile_app | yes (integration) |

## OpenAI AI Task

- Device ID: 2976962ea84b70ecf24e577c2b2986f1
- Manufacturer: OpenAI
- Model: gpt-4o-mini
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| ai_task.openai_ai_task | - | openai_conversation | no |

## OpenAI Conversation

- Device ID: ada53fbce796d9b437db456924cfb861
- Manufacturer: OpenAI
- Model: gpt-4o-mini
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| conversation.openai_conversation | - | openai_conversation | no |

## OpenAI STT

- Device ID: 02e25e295f456ebc26dc408a20d4e260
- Manufacturer: OpenAI
- Model: gpt-4o-mini-transcribe
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| stt.openai_stt | - | openai_conversation | no |

## OpenAI TTS

- Device ID: a08ebd3fc9fe675089ad0e3692e1897e
- Manufacturer: OpenAI
- Model: gpt-4o-mini-tts
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| tts.openai_tts | - | openai_conversation | no |

## openWakeWord

- Device ID: e903647f6fd79d84fe7eca81e49d2dc8
- Manufacturer: Official apps
- Model: Home Assistant App
- Software Version: 2.1.0
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.openwakeword_running | Running | hassio | yes (integration) |
| sensor.openwakeword_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.openwakeword_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.openwakeword_newest_version | Newest version | hassio | yes (integration) |
| sensor.openwakeword_version | Version | hassio | yes (integration) |
| switch.openwakeword | - | hassio | yes (integration) |
| update.openwakeword_update | Update | hassio | no |

## Orion XS

- Device ID: 2da563de377eb0c84a7a9871715d0672
- Manufacturer: Victron Energy
- Model: Orion XS 12/12-50A Charger
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| number.orion_xs_charge_current_limit | Charge current limit | victron_gx | no |
| sensor.orion_xs_dc_output_current | DC output current | victron_gx | no |
| sensor.orion_xs_dc_output_power | DC output power | victron_gx | no |
| sensor.orion_xs_dc_output_voltage | DC output voltage | victron_gx | no |
| sensor.orion_xs_input_current | Input current | victron_gx | no |
| sensor.orion_xs_input_power | Input power | victron_gx | no |
| sensor.orion_xs_input_voltage | Input voltage | victron_gx | no |
| sensor.orion_xs_state | State | victron_gx | no |
| switch.orion_xs | - | victron_gx | no |

## Samba share

- Device ID: 3688928f053920068843a3d235fd191b
- Manufacturer: Official apps
- Model: Home Assistant App
- Software Version: 12.6.1
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.samba_share_running | Running | hassio | yes (integration) |
| sensor.samba_share_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.samba_share_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.samba_share_newest_version | Newest version | hassio | yes (integration) |
| sensor.samba_share_version | Version | hassio | yes (integration) |
| switch.samba_share | - | hassio | yes (integration) |
| update.samba_share_update | Update | hassio | no |

## Shunt Main

- Device ID: 53ba484a4efa91985311ef5e90ab869e
- Manufacturer: Victron Energy
- Model: SmartShunt 500A/50mV
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.shunt_main_automatic_syncs | Automatic syncs | victron_gx | no |
| sensor.shunt_main_average_discharge | Average discharge | victron_gx | no |
| sensor.shunt_main_capacity | Capacity | victron_gx | no |
| sensor.shunt_main_charge | Charge | victron_gx | no |
| sensor.shunt_main_charged_energy | Charged energy | victron_gx | no |
| sensor.shunt_main_consumed_amp_hours | Consumed amp-hours | victron_gx | no |
| sensor.shunt_main_cumulative_ah_drawn | Cumulative Ah drawn | victron_gx | no |
| sensor.shunt_main_dc_bus_current | DC bus current | victron_gx | no |
| sensor.shunt_main_dc_bus_voltage | DC bus voltage | victron_gx | no |
| sensor.shunt_main_deepest_discharge | Deepest discharge | victron_gx | no |
| sensor.shunt_main_discharged_energy | Discharged energy | victron_gx | no |
| sensor.shunt_main_last_discharge | Last discharge | victron_gx | no |
| sensor.shunt_main_maximum_voltage | Maximum voltage | victron_gx | no |
| sensor.shunt_main_minimum_voltage | Minimum voltage | victron_gx | no |
| sensor.shunt_main_power | Power | victron_gx | no |
| sensor.shunt_main_temperature | Temperature | victron_gx | no |
| sensor.shunt_main_time_since_last_full_charge | Time since last full charge | victron_gx | no |
| sensor.shunt_main_time_to_go | Time to go | victron_gx | no |
| sensor.shunt_main_total_charge_cycles | Total charge cycles | victron_gx | no |

## SmartSolar Charger MPPT 100/30 (ID: 278)

- Device ID: 156fbcc2de187b76a84708a847e67f99
- Manufacturer: Victron Energy
- Model: SmartSolar Charger MPPT 100/30
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.smartsolar_charger_mppt_100_30_id_278_load_state | Load state | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_dc_battery_bus_current | DC (battery) bus current | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_dc_battery_bus_voltage | DC (battery) bus voltage | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_device_off_reason | Device-off reason | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_error_code | Error code | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_max_battery_voltage_today | Max battery voltage today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_max_power_today | Max power today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_max_power_yesterday | Max power yesterday | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_min_battery_voltage_today | Min battery voltage today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_mppt_operation_mode | MPPT operation mode | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_pv_bus_voltage | PV bus voltage | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_pv_yield_power | PV yield power | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_state | State | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_time_in_absorption_today | Time in absorption today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_time_in_bulk_today | Time in bulk today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_time_in_float_today | Time in float today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_total_yield | Total yield | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_yield_today | Yield today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_278_yield_yesterday | Yield yesterday | victron_gx | no |
| switch.smartsolar_charger_mppt_100_30_id_278 | - | victron_gx | no |

## SmartSolar Charger MPPT 100/30 (ID: 279)

- Device ID: 1972890e1eee72046e0707847ce2de82
- Manufacturer: Victron Energy
- Model: SmartSolar Charger MPPT 100/30
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.smartsolar_charger_mppt_100_30_id_279_load_state | Load state | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_dc_battery_bus_current | DC (battery) bus current | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_dc_battery_bus_voltage | DC (battery) bus voltage | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_device_off_reason | Device-off reason | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_error_code | Error code | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_max_battery_voltage_today | Max battery voltage today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_max_power_today | Max power today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_max_power_yesterday | Max power yesterday | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_min_battery_voltage_today | Min battery voltage today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_mppt_operation_mode | MPPT operation mode | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_pv_bus_voltage | PV bus voltage | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_pv_yield_power | PV yield power | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_state | State | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_time_in_absorption_today | Time in absorption today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_time_in_bulk_today | Time in bulk today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_time_in_float_today | Time in float today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_total_yield | Total yield | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_yield_today | Yield today | victron_gx | no |
| sensor.smartsolar_charger_mppt_100_30_id_279_yield_yesterday | Yield yesterday | victron_gx | no |
| switch.smartsolar_charger_mppt_100_30_id_279 | - | victron_gx | no |

## SONOFF Dongle Plus MG24

- Device ID: afdba1a300ef524afbf3574611769047
- Manufacturer: SONOFF
- Model: Dongle Plus MG24
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.sonoff_dongle_plus_mg24_address_conflict_sent | ADDRESS_CONFLICT_SENT | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_allocate_packet_buffer_failure | ALLOCATE_PACKET_BUFFER_FAILURE | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_data_rx_broadcast | APS_DATA_RX_BROADCAST | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_data_rx_unicast | APS_DATA_RX_UNICAST | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_data_tx_broadcast | APS_DATA_TX_BROADCAST | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_data_tx_unicast_failed | APS_DATA_TX_UNICAST_FAILED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_data_tx_unicast_retry | APS_DATA_TX_UNICAST_RETRY | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_data_tx_unicast_success | APS_DATA_TX_UNICAST_SUCCESS | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_decryption_failure | APS_DECRYPTION_FAILURE | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_frame_counter_failure | APS_FRAME_COUNTER_FAILURE | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_aps_link_key_not_authorized | APS_LINK_KEY_NOT_AUTHORIZED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_ash_framing_error | ASH_FRAMING_ERROR | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_ash_overflow_error | ASH_OVERFLOW_ERROR | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_ash_overrun_error | ASH_OVERRUN_ERROR | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_broadcast_table_full | BROADCAST_TABLE_FULL | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_child_removed | CHILD_REMOVED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_ezsp_free_buffers | EZSP_FREE_BUFFERS | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_join_indication | JOIN_INDICATION | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_mac_rx_broadcast | MAC_RX_BROADCAST | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_mac_rx_unicast | MAC_RX_UNICAST | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_mac_tx_broadcast | MAC_TX_BROADCAST | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_mac_tx_unicast_failed | MAC_TX_UNICAST_FAILED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_mac_tx_unicast_retry | MAC_TX_UNICAST_RETRY | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_mac_tx_unicast_success | MAC_TX_UNICAST_SUCCESS | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_neighbor_added | NEIGHBOR_ADDED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_neighbor_removed | NEIGHBOR_REMOVED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_neighbor_stale | NEIGHBOR_STALE | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_nwk_decryption_failure | NWK_DECRYPTION_FAILURE | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_nwk_frame_counter_failure | NWK_FRAME_COUNTER_FAILURE | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_packet_validate_library_dropped_count | PACKET_VALIDATE_LIBRARY_DROPPED_COUNT | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_phy_cca_fail_count | PHY_CCA_FAIL_COUNT | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_phy_to_mac_queue_limit_reached | PHY_TO_MAC_QUEUE_LIMIT_REACHED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_pta_hi_pri_denied | PTA_HI_PRI_DENIED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_pta_hi_pri_requested | PTA_HI_PRI_REQUESTED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_pta_hi_pri_tx_aborted | PTA_HI_PRI_TX_ABORTED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_pta_lo_pri_denied | PTA_LO_PRI_DENIED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_pta_lo_pri_requested | PTA_LO_PRI_REQUESTED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_pta_lo_pri_tx_aborted | PTA_LO_PRI_TX_ABORTED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_relayed_unicast | RELAYED_UNICAST | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_route_discovery_initiated | ROUTE_DISCOVERY_INITIATED | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_type_nwk_retry_overflow | TYPE_NWK_RETRY_OVERFLOW | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_unicast_rx | unicast_rx | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_unicast_tx_success | unicast_tx_success | zha | yes (integration) |
| sensor.sonoff_dongle_plus_mg24_utility | UTILITY | zha | yes (integration) |

## SONOFF SNZB-05P

- Device ID: 598840bccc46b999a729c0c9b263cbb0
- Manufacturer: SONOFF
- Model: SNZB-05P
- Software Version: 0x00001002
- Hardware Version: -
- Area ID: jaskier

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.sonoff_snzb_05p | - | zha | no |
| button.sonoff_snzb_05p_identify | Identify | zha | no |
| sensor.sonoff_snzb_05p_battery | Battery | zha | no |
| sensor.sonoff_snzb_05p_lqi | LQI | zha | yes (integration) |
| sensor.sonoff_snzb_05p_rssi | RSSI | zha | yes (integration) |
| update.sonoff_snzb_05p_firmware | Firmware | zha | no |

## Sun

- Device ID: 5e67fa8b9022981864d784a3a16bd58a
- Manufacturer: -
- Model: -
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.sun_solar_rising | Solar rising | sun | yes (integration) |
| sensor.sun_next_dawn | Next dawn | sun | no |
| sensor.sun_next_dusk | Next dusk | sun | no |
| sensor.sun_next_midnight | Next midnight | sun | no |
| sensor.sun_next_noon | Next noon | sun | no |
| sensor.sun_next_rising | Next rising | sun | no |
| sensor.sun_next_setting | Next setting | sun | no |
| sensor.sun_solar_azimuth | Solar azimuth | sun | yes (integration) |
| sensor.sun_solar_elevation | Solar elevation | sun | yes (integration) |

## Terminal & SSH

- Device ID: fbf4d45da47fea7f574e25580e9cf3a2
- Manufacturer: Official apps
- Model: Home Assistant App
- Software Version: 10.2.0
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| binary_sensor.terminal_ssh_running | Running | hassio | yes (integration) |
| sensor.terminal_ssh_cpu_percent | CPU percent | hassio | yes (integration) |
| sensor.terminal_ssh_memory_percent | Memory percent | hassio | yes (integration) |
| sensor.terminal_ssh_newest_version | Newest version | hassio | yes (integration) |
| sensor.terminal_ssh_version | Version | hassio | yes (integration) |
| switch.terminal_ssh | - | hassio | yes (integration) |
| update.terminal_ssh_update | Update | hassio | no |

## Atom Echo Voice

- Device ID: 107535a9b8376688fbb418df9ef30cbb
- Manufacturer: m5stack
- Model: atom-echo-wake-word-voice-assistant
- Software Version: 25.12.2 (ESPHome 2025.11.3)
- Hardware Version: -
- Area ID: jaskier

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| assist_satellite.m5stack_atom_echo_8887dc_assist_satellite | Assist satellite | esphome | no |
| binary_sensor.m5stack_atom_echo_8887dc_button | Button | esphome | yes (integration) |
| button.m5stack_atom_echo_8887dc_factory_reset | Factory reset | esphome | no |
| light.m5stack_atom_echo_8887dc | - | esphome | yes (integration) |
| media_player.m5stack_atom_echo_8887dc | - | esphome | no |
| select.m5stack_atom_echo_8887dc_assistant | Assistant | esphome | no |
| select.m5stack_atom_echo_8887dc_assistant_2 | Assistant 2 | esphome | no |
| select.m5stack_atom_echo_8887dc_finished_speaking_detection | Finished speaking detection | esphome | no |
| select.m5stack_atom_echo_8887dc_wake_word | Wake word | esphome | no |
| select.m5stack_atom_echo_8887dc_wake_word_2 | Wake word 2 | esphome | no |
| select.m5stack_atom_echo_8887dc_wake_word_engine_location | Wake word engine location | esphome | no |
| switch.m5stack_atom_echo_8887dc_use_listen_light | Use listen light | esphome | no |
| update.m5stack_atom_echo_8887dc_firmware | Firmware | esphome | no |

## ButtonLight

- Device ID: 3f67873a70ae0f4c20e5a1579d7b3604
- Manufacturer: eWeLink
- Model: SNZB-01P
- Software Version: 0x00002200
- Hardware Version: -
- Area ID: jaskier

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| button.ewelink_snzb_01p_identify | Identify | zha | no |
| sensor.ewelink_snzb_01p_battery | Battery | zha | no |
| sensor.ewelink_snzb_01p_lqi | LQI | zha | yes (integration) |
| sensor.ewelink_snzb_01p_rssi | RSSI | zha | yes (integration) |
| update.ewelink_snzb_01p_firmware | Firmware | zha | no |

## ButtonLightFront

- Device ID: 6929468e394bf280185ad4d26eff8c4d
- Manufacturer: eWeLink
- Model: SNZB-01P
- Software Version: 0x00002200
- Hardware Version: -
- Area ID: jaskier

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| button.ewelink_snzb_01p_identify_2 | Identify | zha | no |
| sensor.ewelink_snzb_01p_battery_2 | Battery | zha | no |
| sensor.ewelink_snzb_01p_lqi_2 | LQI | zha | yes (integration) |
| sensor.ewelink_snzb_01p_rssi_2 | RSSI | zha | yes (integration) |
| update.ewelink_snzb_01p_firmware_2 | Firmware | zha | no |

## Internal Sensor

- Device ID: dbd7253d18aeacc193f55a3068ff28fa
- Manufacturer: SONOFF
- Model: SNZB-02D
- Software Version: 0x00002300
- Hardware Version: -
- Area ID: jaskier

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| button.sensor_internal_identify | Identify | zha | no |
| number.sensor_internal_comfort_humidity_max | Comfort humidity max | zha | no |
| number.sensor_internal_comfort_humidity_min | Comfort humidity min | zha | no |
| number.sensor_internal_comfort_temperature_max | Comfort temperature max | zha | no |
| number.sensor_internal_comfort_temperature_min | Comfort temperature min | zha | no |
| number.sensor_internal_humidity_offset | Humidity offset | zha | no |
| number.sensor_internal_temperature_offset | Temperature offset | zha | no |
| select.sensor_internal_display_unit | Display unit | zha | no |
| sensor.sensor_internal_battery | Battery | zha | no |
| sensor.sensor_internal_humidity | Humidity | zha | no |
| sensor.sensor_internal_lqi | LQI | zha | yes (integration) |
| sensor.sensor_internal_rssi | RSSI | zha | yes (integration) |
| sensor.sensor_internal_temperature | Temperature | zha | no |
| update.sensor_internal_firmware | Firmware | zha | no |

## Jaskiercore

- Device ID: a0df18c56b9f2ec992d3306ab76c1f5e
- Manufacturer: Glances
- Model: -
- Software Version: -
- Hardware Version: -
- Area ID: -

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| sensor.jaskiercore_amd_gpu_gpu_amd0_fan_speed | AMD GPU (GPU amd0) fan speed | glances | yes (config_entry) |
| sensor.jaskiercore_amd_gpu_gpu_amd0_memory_usage | AMD GPU (GPU amd0) memory usage | glances | yes (config_entry) |
| sensor.jaskiercore_amd_gpu_gpu_amd0_processor_usage | AMD GPU (GPU amd0) processor usage | glances | yes (config_entry) |
| sensor.jaskiercore_amd_gpu_gpu_amd0_temperature | AMD GPU (GPU amd0) temperature | glances | yes (config_entry) |
| sensor.jaskiercore_br_294f7058e6f8_rx | br-294f7058e6f8 RX | glances | yes (config_entry) |
| sensor.jaskiercore_br_294f7058e6f8_tx | br-294f7058e6f8 TX | glances | yes (config_entry) |
| sensor.jaskiercore_br_e9c10a255669_rx | br-e9c10a255669 RX | glances | yes (config_entry) |
| sensor.jaskiercore_br_e9c10a255669_tx | br-e9c10a255669 TX | glances | yes (config_entry) |
| sensor.jaskiercore_br0_rx | br0 RX | glances | yes (config_entry) |
| sensor.jaskiercore_br0_tx | br0 TX | glances | yes (config_entry) |
| sensor.jaskiercore_composite_1_temperature | Composite 1 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_composite_4_temperature | Composite 4 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_composite_temperature | Composite temperature | glances | yes (config_entry) |
| sensor.jaskiercore_containers_active | Containers active | glances | yes (config_entry) |
| sensor.jaskiercore_containers_cpu_usage | Containers CPU usage | glances | yes (config_entry) |
| sensor.jaskiercore_containers_memory_used | Containers memory used | glances | yes (config_entry) |
| sensor.jaskiercore_cpu_load | CPU load | glances | yes (config_entry) |
| sensor.jaskiercore_cpu_usage | CPU usage | glances | yes (config_entry) |
| sensor.jaskiercore_disk_free | / disk free | glances | yes (config_entry) |
| sensor.jaskiercore_disk_usage | / disk usage | glances | yes (config_entry) |
| sensor.jaskiercore_disk_used | / disk used | glances | yes (config_entry) |
| sensor.jaskiercore_dm_0_disk_read | dm-0 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_dm_0_disk_write | dm-0 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_edge_temperature | edge temperature | glances | yes (config_entry) |
| sensor.jaskiercore_memory_free | Memory free | glances | yes (config_entry) |
| sensor.jaskiercore_memory_usage | Memory usage | glances | yes (config_entry) |
| sensor.jaskiercore_memory_use | Memory use | glances | yes (config_entry) |
| sensor.jaskiercore_mt7921_phy0_0_temperature | mt7921_phy0 0 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_nvme0n1_disk_read | nvme0n1 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme0n1_disk_write | nvme0n1 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme0n1p1_disk_read | nvme0n1p1 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme0n1p1_disk_write | nvme0n1p1 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme0n1p9_disk_read | nvme0n1p9 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme0n1p9_disk_write | nvme0n1p9 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1_disk_read | nvme1n1 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1_disk_write | nvme1n1 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1p1_disk_read | nvme1n1p1 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1p1_disk_write | nvme1n1p1 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1p2_disk_read | nvme1n1p2 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1p2_disk_write | nvme1n1p2 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1p3_disk_read | nvme1n1p3 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme1n1p3_disk_write | nvme1n1p3 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme2n1_disk_read | nvme2n1 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme2n1_disk_write | nvme2n1 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme2n1p1_disk_read | nvme2n1p1 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme2n1p1_disk_write | nvme2n1p1 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_nvme2n1p9_disk_read | nvme2n1p9 disk read | glances | yes (config_entry) |
| sensor.jaskiercore_nvme2n1p9_disk_write | nvme2n1p9 disk write | glances | yes (config_entry) |
| sensor.jaskiercore_pkg_temperature | pkg temperature | glances | yes (config_entry) |
| sensor.jaskiercore_r8169_0_300_00_0_temperature | r8169_0_300:00 0 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_running | Running | glances | yes (config_entry) |
| sensor.jaskiercore_sensor_1_2_temperature | Sensor 1 2 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_sensor_1_5_temperature | Sensor 1 5 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_sensor_1_temperature | Sensor 1 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_sensor_2_3_temperature | Sensor 2 3 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_sensor_2_6_temperature | Sensor 2 6 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_sensor_2_temperature | Sensor 2 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_sensor_3_temperature | Sensor 3 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_sleeping | Sleeping | glances | yes (config_entry) |
| sensor.jaskiercore_spd5118_0_temperature | spd5118 0 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_spd5118_1_temperature | spd5118 1 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_swap_free | Swap free | glances | yes (config_entry) |
| sensor.jaskiercore_swap_usage | Swap usage | glances | yes (config_entry) |
| sensor.jaskiercore_swap_use | Swap use | glances | yes (config_entry) |
| sensor.jaskiercore_tank_certs_disk_free | /tank/certs disk free | glances | yes (config_entry) |
| sensor.jaskiercore_tank_certs_disk_usage | /tank/certs disk usage | glances | yes (config_entry) |
| sensor.jaskiercore_tank_certs_disk_used | /tank/certs disk used | glances | yes (config_entry) |
| sensor.jaskiercore_tank_disk_free | /tank disk free | glances | yes (config_entry) |
| sensor.jaskiercore_tank_disk_usage | /tank disk usage | glances | yes (config_entry) |
| sensor.jaskiercore_tank_disk_used | /tank disk used | glances | yes (config_entry) |
| sensor.jaskiercore_tank_nas_disk_free | /tank/nas disk free | glances | yes (config_entry) |
| sensor.jaskiercore_tank_nas_disk_usage | /tank/nas disk usage | glances | yes (config_entry) |
| sensor.jaskiercore_tank_nas_disk_used | /tank/nas disk used | glances | yes (config_entry) |
| sensor.jaskiercore_tank_onedrive_disk_free | /tank/onedrive disk free | glances | yes (config_entry) |
| sensor.jaskiercore_tank_onedrive_disk_usage | /tank/onedrive disk usage | glances | yes (config_entry) |
| sensor.jaskiercore_tank_onedrive_disk_used | /tank/onedrive disk used | glances | yes (config_entry) |
| sensor.jaskiercore_tank_services_disk_free | /tank/services disk free | glances | yes (config_entry) |
| sensor.jaskiercore_tank_services_disk_usage | /tank/services disk usage | glances | yes (config_entry) |
| sensor.jaskiercore_tank_services_disk_used | /tank/services disk used | glances | yes (config_entry) |
| sensor.jaskiercore_tccd1_temperature | Tccd1 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_tccd2_temperature | Tccd2 temperature | glances | yes (config_entry) |
| sensor.jaskiercore_tctl_temperature | Tctl temperature | glances | yes (config_entry) |
| sensor.jaskiercore_threads | Threads | glances | yes (config_entry) |
| sensor.jaskiercore_total | Total | glances | yes (config_entry) |
| sensor.jaskiercore_uptime | Uptime | glances | yes (config_entry) |
| sensor.jaskiercore_veth226a196_rx | veth226a196 RX | glances | yes (config_entry) |
| sensor.jaskiercore_veth226a196_tx | veth226a196 TX | glances | yes (config_entry) |
| sensor.jaskiercore_veth804c60f_rx | veth804c60f RX | glances | yes (config_entry) |
| sensor.jaskiercore_veth804c60f_tx | veth804c60f TX | glances | yes (config_entry) |
| sensor.jaskiercore_veth923c0a3_rx | veth923c0a3 RX | glances | yes (config_entry) |
| sensor.jaskiercore_veth923c0a3_tx | veth923c0a3 TX | glances | yes (config_entry) |
| sensor.jaskiercore_vnet1_rx | vnet1 RX | glances | yes (config_entry) |
| sensor.jaskiercore_vnet1_tx | vnet1 TX | glances | yes (config_entry) |
| sensor.jaskiercore_vram_temperature | vram temperature | glances | yes (config_entry) |
| sensor.jaskiercore_xe_0_fan_speed | xe 0 fan speed | glances | yes (config_entry) |

## Outside Sensor

- Device ID: 78909263771487c782365a1ea6f6d0af
- Manufacturer: SONOFF
- Model: SNZB-02D
- Software Version: 0x00002300
- Hardware Version: -
- Area ID: outside

### Entities

| Entity ID | Name | Platform | Disabled |
|---|---|---|---|
| button.outside_sensor_identify | Identify | zha | no |
| number.outside_sensor_comfort_humidity_max | Comfort humidity max | zha | no |
| number.outside_sensor_comfort_humidity_min | Comfort humidity min | zha | no |
| number.outside_sensor_comfort_temperature_max | Comfort temperature max | zha | no |
| number.outside_sensor_comfort_temperature_min | Comfort temperature min | zha | no |
| number.outside_sensor_humidity_offset | Humidity offset | zha | no |
| number.outside_sensor_temperature_offset | Temperature offset | zha | no |
| select.outside_sensor_display_unit | Display unit | zha | no |
| sensor.outside_sensor_battery | Battery | zha | no |
| sensor.outside_sensor_humidity | Humidity | zha | no |
| sensor.outside_sensor_lqi | LQI | zha | yes (integration) |
| sensor.outside_sensor_rssi | RSSI | zha | yes (integration) |
| sensor.outside_sensor_temperature | Temperature | zha | no |
| update.outside_sensor_firmware | Firmware | zha | no |

## Entities Without Device

| Entity ID | Name | Platform |
|---|---|---|
| - | - | - |
| automation.battery_voltage | Battery Voltage | automation |
| automation.freezing_notice | Freezing Notice | automation |
| automation.light_press_notification | Light press notification | automation |
| automation.water_apply_target_mode | Water - Apply Target Mode | automation |
| automation.water_heating_control | Water - Heating Control | automation |
| binary_sensor.remote_ui | Remote UI | cloud |
| binary_sensor.water_mode_grid_filling_selected | Water Mode Grid Filling Selected | template |
| binary_sensor.water_mode_grid_selected | Water Mode Grid Selected | template |
| binary_sensor.water_mode_normal_selected | Water Mode Normal Selected | template |
| binary_sensor.water_mode_pump_filling_selected | Water Mode Pump Filling Selected | template |
| input_boolean.water_heating_enabled | Water Heating Enabled | input_boolean |
| input_number.water_heating_hysteresis | Water Heating Hysteresis | input_number |
| input_number.water_heating_target_temp | Water Heating Target Temp | input_number |
| input_select.water_mode_current | Water Mode Current | input_select |
| input_select.water_mode_target | Water Mode Target | input_select |
| person.daga | Daga | person |
| person.mswietlicki | Mateusz | person |
| script.water_mode_grid | Water - Grid | script |
| script.water_mode_grid_filling | Water - Grid Filling | script |
| script.water_mode_normal | Water - Normal | script |
| script.water_mode_pump_filling | Water - Pump Filling | script |
| script.water_set_mode | Water - Set Mode (Dispatcher) | script |
| script.water_transition_grid_filling_to_grid | Water - Transition Grid Filling -> Grid | script |
| script.water_transition_grid_filling_to_normal | Water - Transition Grid Filling -> Normal | script |
| script.water_transition_grid_filling_to_pump_filling | Water - Transition Grid Filling -> Pump Filling | script |
| script.water_transition_grid_to_grid_filling | Water - Transition Grid -> Grid Filling | script |
| script.water_transition_grid_to_normal | Water - Transition Grid -> Normal | script |
| script.water_transition_grid_to_pump_filling | Water - Transition Grid -> Pump Filling | script |
| script.water_transition_normal_to_grid | Water - Transition Normal -> Grid | script |
| script.water_transition_normal_to_grid_filling | Water - Transition Normal -> Grid Filling | script |
| script.water_transition_normal_to_pump_filling | Water - Transition Normal -> Pump Filling | script |
| script.water_transition_pump_filling_to_grid | Water - Transition Pump Filling -> Grid | script |
| script.water_transition_pump_filling_to_grid_filling | Water - Transition Pump Filling -> Grid Filling | script |
| script.water_transition_pump_filling_to_normal | Water - Transition Pump Filling -> Normal | script |
| select.inverter_mode | Inverter Mode | template |
| sensor.boiler_temp | Boiler Temp | modbus |
| sensor.dc_energy | DC Energy | integration |
| sensor.ve_bus_state | VE.Bus State | modbus |
| sensor.ve_bus_switch_position_mode | VE.Bus Switch Position Mode | template |
| sensor.victron_ac_consumption_l1 | AC Consumption L1 | modbus |
| sensor.victron_battery_current | Battery Current | modbus |
| sensor.victron_battery_power | DC Power | modbus |
| sensor.victron_battery_soc | Stan baterii | modbus |
| sensor.victron_battery_temperature | Battery Temperature | modbus |
| sensor.victron_battery_time_to_go_system | Battery Time To Go (System) | modbus |
| sensor.victron_battery_voltage | Battery Voltage | modbus |
| sensor.victron_dc_pv_power | DC PV Power | modbus |
| sensor.victron_grid_power_l1 | Grid Power L1 | modbus |
| sensor.victron_solar_224_panel_current | Solar 224 Panel Current | modbus |
| sensor.victron_solar_224_panel_power | Solar 224 Panel Power | modbus |
| sensor.victron_solar_224_panel_voltage | Solar 224 Panel Voltage | modbus |
| sensor.victron_solar_panel_current | Solar 226 Panel Current | modbus |
| sensor.victron_solar_panel_power | Solar 226 Panel Power | modbus |
| sensor.victron_solar_panel_voltage | Solar 226 Panel Voltage | modbus |
| sensor.victron_vebus_bms_allow_to_charge | VE.Bus BMS Allow To Charge | modbus |
| sensor.victron_vebus_bms_allow_to_discharge | VE.Bus BMS Allow To Discharge | modbus |
| sensor.victron_vebus_bms_error | VE.Bus BMS Error | modbus |
| sensor.victron_vebus_switch_position | VE.Bus Switch Position | modbus |
| sensor.water_temp | Water Temp | modbus |
| stt.home_assistant_cloud | Home Assistant Cloud | cloud |
| switch.gray_water_valve | Gray Water Valve | modbus |
| switch.relay_0 | Relay 0 | modbus |
| switch.relay_1 | Relay 1 | modbus |
| switch.relay_2 | Relay 2 | modbus |
| switch.relay_3 | Relay 3 | modbus |
| switch.relay_4 | Relay 4 | modbus |
| switch.relay_5 | Relay 5 | modbus |
| switch.relay_6 | Relay 6 | modbus |
| switch.relay_7 | Relay 7 | modbus |
| switch.water_heater_relay | Water Heater Relay | modbus |
| switch.water_pump_relay | Water Pump Relay | modbus |
| switch.water_valve_grid | Water Valve Grid | modbus |
| switch.water_valve_loop | Water Valve Loop | modbus |
| switch.water_valve_pump_overwrite | Water Valve Pump Overwrite | modbus |
| switch.water_valve_tank | Water Valve Tank | modbus |
| todo.shopping_list | Shopping List | shopping_list |
| todo.zadania | Zadania | local_todo |
| tts.home_assistant_cloud | Home Assistant Cloud | cloud |
| wake_word.openwakeword | openwakeword | wyoming |

