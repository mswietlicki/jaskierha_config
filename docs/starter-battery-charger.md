# Ładowanie akumulatora rozruchowego przy AC

12 października 2026 przebudowano i włączono istniejącą `automation.starter_battery_charging`, zachowując jej ID, nazwę i kategorię. Poprzednia automatyzacja była wyłączona i oparta na napięciu akumulatora. Nie ma teraz warunków zależnych od tego napięcia ani od alarmu poziomu akumulatora głównego.

Sterowanie: `switch.front_controller_starter_battery_charger`.
Źródło AC: `sensor.gx_device_ac_active_input_source`, akceptowane wartości `shore_power`, `grid`, `generator`. Wybrany rodzaj źródła musi utrzymywać się przez 30 sekund. Dodatkowo wymagane są połączenie falownika, nieignorowane wejście AC i napięcie wejściowe >190 V oraz <255 V.

Utrata aktywnego źródła AC, jego unknown/unavailable/not_connected, utrata połączenia falownika albo niespełnione warunki wejścia powodują wyłączenie ładowarki. Odcięcie nie ma celowego opóźnienia. Automatyzacja reaguje na zmianę źródła, stanu falownika, napięcia i samego przekaźnika; sprawdza stan po starcie HA oraz co minutę. Nie zależy od ustawień ogrzewania podłogowego. Ręczne wyłączenie ładowarki przy aktywnym AC jest korygowane przez automatykę; aby celowo wyłączyć tę funkcję, należy wyłączyć automatyzację Starter Battery Charging.

Potwierdzono zapisaną konfigurację, poprawność warunków dla bieżącego Shore Power oraz ON automatyzacji i ładowarki. Fizycznego odłączenia AC nie wykonywano. Wcześniejsza konfiguracja i stan wyłączenia są zapisane w starter-battery-charger-before.json. Aktualna specyfikacja jest w starter-battery-charger-config.json; plik nie jest automatycznie ładowany przez HA.

Cofnięcie: wyłączyć automatyzację, przywrócić poprzednie config przez API z bieżącym hashem i pozostawić automatyzację wyłączoną, jak przed zmianą. Zabezpieczenie jest realizowane przez działający Home Assistant.
