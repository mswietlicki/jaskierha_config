# Ogrzewanie podłogowe Jaskra

Wdrożone w działającym Home Assistant 12 października 2026, bez restartu.
Panel: https://jaskierha.swietlicki.net/dashboard-jaskier/climate

## Obsługa

- `input_boolean.floor_heating_enabled` — główne zezwolenie, domyślnie włączone przy wdrożeniu. Ręczne wyłączenie jest zachowane przez restart i ponowne podłączenie AC.
- `input_boolean.cats_in_van` — Koty w samochodzie; komfort bez wykrywania ludzi. Pozostaje włączone do ręcznego wyłączenia, także po restarcie.
- `input_select.floor_heating_override` — Auto / Nocny / Dzienny / Idle. Ręczny wybór ma pierwszeństwo także nad kotami i nocnym podtrzymaniem obecności; nadal respektuje główne wyłączenie i wszystkie blokady bezpieczeństwa.
- Temperatury regulowane w panelu: noc 18°C, dzień 20°C, idle 10°C. Zakres 5–24°C.
- Noc 22:00–08:00 wg strefy HA Europe/Warsaw. Godziny można zmienić w helperze `binary_sensor.floor_heating_night` (Time of Day).

## Wybór trybu

Auto wybiera noc/dzień, gdy są koty, potwierdzona obecność albo nocne podtrzymanie obecności. W pozostałych przypadkach wybiera Idle.
Obecność wymaga 2 minut ciągłego sygnału ON. Każdy krótszy impuls jest ignorowany. Znacznik ostatniej obecności odświeża się co minutę tylko wtedy, gdy sygnał utrzymuje ON nieprzerwanie przez co najmniej 2 minuty; kontrola okresowa nie omija filtra. Jest zachowywany w `input_datetime.jaskier_last_presence`; podtrzymanie trwa 45 minut, także przez restarty HA. Awaria czujnika obecności jest traktowana zachowawczo jako obecność.
Od 12 października obecność jest wspólna dla całego Jaskra: `binary_sensor.jaskier_occupied` (Jaskier Occupied, dawniej `binary_sensor.floor_heating_occupied`) i automatyzacja `automation.occupancy_presence_memory` (Occupancy - Presence Memory). Korzysta z niej ogrzewanie podłogowe oraz wyłączanie pompy wody pod nieobecność (`automation.water_pump_off_when_unoccupied`).
Nocne wykrycie obecności włącza pamięć `input_boolean.floor_heating_night_occupied`, która jest resetowana rano. Brak ruchu w czasie snu nie zmienia wtedy trybu na Idle. Nocny wyjazd ludzi wymaga ręcznego Idle, jeśli ma nastąpić obniżenie temperatury przed 08:00.

## Regulacja i zabezpieczenia

Średnia dostępnych czujników `sensor.sensor_internal_temperature` i `sensor.presents_sensor_zg_204zx_temperature` pochodzi z natywnego helpera Min/Max. Jeden niedostępny czujnik jest pomijany; brak obu blokuje ogrzewanie. Niewiarygodna wartość poniżej -30°C albo >=26°C na dowolnym czujniku również blokują grzanie. Dostępność pomiarów opiera się na stanie encji ZHA: unknown/unavailable są pomijane, a brak obu prawidłowych pomiarów blokuje grzanie. Poprawka z 12 października usunęła limit 2 godzin oparty na last_reported, ponieważ ZHA może nie przekazywać niezmienionych wartości jako nowego stanu HA. Stabilna temperatura nie powoduje odcięcia; rzeczywiste wykrywanie utraty urządzenia zależy od mechanizmu dostępności ZHA.

`climate.floor_heating` jest natywnym Generic Thermostat: załączenie przy celu minus 0,3°C, wyłączenie przy celu plus 0,2°C; minimum cyklu grzania 10 minut i minimum przerwy 5 minut. Zmiana celu i wymuszone wyłączenie mogą ominąć zwykłe ograniczenia cyklu. Dokumentacja: https://www.home-assistant.io/integrations/generic_thermostat/

Shore Power wymaga dokładnie `sensor.gx_device_ac_active_input_source = shore_power`, działającego połączenia falownika, nieignorowanego wejścia AC, napięcia 190–255 V, częstotliwości 45–55 Hz i raportu napięcia nie starszego niż 5 minut. Załączenie wymaga 60 sekund stabilnego sygnału; odcięcie nie ma opóźnienia. Grid, generator, unknown, unavailable i not_connected nie zezwalają na grzanie.

Termostat steruje przez `switch.floor_heating_protected_relay`, którego akcja załączania sprawdza zezwolenie, główny przełącznik i surowy sygnał Shore Power. Osobna automatyzacja odcina fizyczny `switch.floorheating` po utracie zezwolenia i sprawdza stan co minutę oraz po starcie HA. Automatyzacja zarządzająca wyłącza wtedy także termostat. Zabezpieczenia mają pierwszeństwo przed minimalnym czasem grzania.

Stara automatyzacja oparta na progu 500 W została zastąpiona powyższym odcięciem, z zachowaniem jej ID. Druga stara automatyzacja, oparta na `sensor.inverter_active_ac_input`, jest wyłączona; w tej instalacji ten czujnik raportował unknown mimo aktywnego Shore Power.

Panel pokazuje ostrzeżenie, gdy Koty w samochodzie i Ogrzewanie są włączone, lecz nie ma Shore Power. Nie wysyłano wiadomości ani powiadomień push.

## Sprawdzenie

27 scenariuszy logiki przetestowano w silniku szablonów HA: tryby, koty, sen, ręczne wymuszenie, utrata AC, nieaktualna telemetria, przegrzanie i awarie czujników. Rzeczywisty test głównego OFF zatrzymał przekaźnik i termostat; próba załączenia przez chroniony przekaźnik została zablokowana. Po przywróceniu ON grzanie wróciło z celem 18°C. Konfiguracja HA przeszła `config_check`. Fizycznego odłączenia Shore Power i całonocnego zachowania czujnika obecności nie testowano.

## Odtworzenie i zakres plików

Źródłem obowiązującej konfiguracji jest działający HA: helpery powstały w jego UI/config flows, automatyzacje i panel przez API. Nie dodano definicji tych helperów do lokalnego `configuration.yaml`, aby nie tworzyć duplikatów ani wymagać restartu. `floor-heating-config.json` zawiera specyfikację konfiguracji; nie jest automatycznie ładowanym pakietem HA.
`floor-heating-before.json` zawiera wcześniejsze dwie automatyzacje i wcześniejszy dashboard. Aby cofnąć zmianę: wyłączyć nowy główny przełącznik i trzy nowe automatyzacje, przywrócić dawną konfigurację pierwszej automatyzacji przez API, ponownie włączyć drugą oraz przywrócić wcześniejsze karty Heating i Diesel Heater w panelu. Przed przywróceniem całego dashboardu porównać bieżący hash, aby nie nadpisać późniejszych zmian.

## Kolejne etapy

Webasto ma w przyszłości realizować ten sam cel komfortu bez AC. Logika obecności i cele są oddzielone od sterowania podłogówką i mogą zostać wykorzystane ponownie. Należy dodać osobne zezwolenie i sterowanie urządzeniem, minimum czasu pracy/przerwy oraz pełny cykl rozruchu i wygaszania; nie odcinać jego zasilania jak przekaźnika podłogi.
Obecne zabezpieczenia działają w HA i nie są sprzętową blokadą ani ogranicznikiem temperatury powierzchni podłogi. Czujnik podłogi i niezależny ogranicznik temperatury pozwolą rozbudować ochronę. Warto też porównać czujniki temperatury: w chwili wdrożenia wskazywały 17,8°C i 15,4°C, a średnia wynosiła 16,6°C.


