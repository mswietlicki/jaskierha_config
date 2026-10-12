# Poranny przegląd ogrzewania — 12 października 2026

Odczyt wykonano około 08:32 Europe/Warsaw. Przejrzano pełną historię 15 wskazanych encji od 11 października 19:00 do 12 października 08:31. Wszystkie pobrane historie były kompletne (has_more=false). Konfiguracja i automatyzacje pozostały bez zmian.

## Wnioski

1. **Do poprawy: ocena świeżości temperatury.** O 05:49:00 czujnik Floor Heating Temperature Safe przełączył się na OFF, termostat i fizyczny przekaźnik zostały wyłączone. Grzanie wróciło o 06:43:04 — przerwa 54 min 05 s. Shore Power pozostawało potwierdzone, główne zezwolenie było ON, cel wynosił 18°C, a średnia około 16,4°C w chwili odcięcia.
2. **Cel 18°C nie został osiągnięty.** Po okresie konfiguracji/testów, od 00:15 do 08:00 średnia temperatura mieściła się w 15,9–16,7°C; średnia ważona czasem wyniosła 16,18°C. Grzanie było ON przez 6 h 51 min z 7 h 45 min (88,37%). Jedyna przerwa wynikała z powyższej blokady, nie z osiągnięcia temperatury docelowej. Nie wystąpiło szybkie przełączanie termostatu; histerezy wokół celu nie da się ocenić, bo temperatury nie doszły do jej progów.
3. **Obecność była stabilna po wygładzeniu.** Surowy czujnik był ON przez 99,72% okresu 00:15–08:00. Wystąpiło 12 przerw OFF: 11 trwało 0,4–2,1 s, jedna 67,4 s (06:03:07–06:04:15). Żadna nie wyłączyła wygładzonej obecności ani nie obniżyła celu do Idle. Nie było w tym okresie izolowanych krótkich impulsów ON po długiej nieobecności, więc tej strony filtra nie zweryfikowano na rzeczywistym zdarzeniu. Nie można z samego ON potwierdzić obecności ludzi ani wykluczyć fałszywych detekcji.
4. **Przejście poranne działało.** Dokładnie o 08:00 nocna pamięć obecności została zresetowana, tryb zmienił się z Nocny na Dzienny, a cel z 18 na 20°C. Około 08:32 odczyty wynosiły 17,0°C i 15,3°C, średnia 16,1°C, grzanie ON. Koty w samochodzie pozostało OFF.

## Dlaczego wystąpiła blokada

Ostatnia zmiana temperatury SONOFF przed blokadą nastąpiła o 03:48:25 (17,2°C). Reguła odcina grzanie, jeśli którykolwiek liczbowy odczyt ma last_reported starszy niż 7200 s. Odcięcie o 05:49 odpowiada temu terminowi. Temperatura SONOFF zmieniła się ponownie o 06:41:34, ale drugi czujnik miał wtedy odczyt od 04:38:18, więc blokada zniknęła dopiero po jego aktualizacji o 06:43:04.

Oba czujniki działają przez ZHA. ZHA odfiltrowuje niezmieniony stan przed przekazaniem go HA; sam last_reported nie jest więc pewnym potwierdzeniem świeżości pakietów Zigbee. Dodatkowo SONOFF raportował wilgotność o 04:59, a czujnik obecności raportował światło o 05:44/05:45 i ruch podczas przerwy. To przemawia za zbyt restrykcyjną oceną świeżości, nie dowodzi ciągłego działania konkretnego kanału temperatury.

Źródła techniczne:
- https://www.home-assistant.io/docs/configuration/state_object/
- https://raw.githubusercontent.com/zigpy/zha/dev/zha/application/platforms/__init__.py — maybe_emit_state_changed_event

Zalecam zastąpić obecny limit sygnałem dostępności/ostatniej komunikacji urządzenia, uzupełnionym świadomie dobranym limitem wieku pomiaru. Jeśli jeden czujnik rzeczywiście nie dostarcza wiarygodnej temperatury, należy odrzucić ten pomiar i regulować z drugiego, zamiast wyłączać cały układ. Utrata obu oraz przekroczenie 26°C nadal powinny odcinać grzanie.

## Pozostałe zalecenia

Temperatury SONOFF i czujnika obecności różniły się od 1,5 do 2,2°C, średnio o 1,80°C (00:15–08:00). W tym okresie SONOFF wskazywał 16,8–17,6°C, drugi czujnik 15,0–15,8°C. Warto porównać je obok siebie ze znanym termometrem, zanim zmienimy kalibrację lub sposób agregacji. Nie wiadomo jeszcze, jaka część różnicy jest rzeczywistym gradientem temperatury w samochodzie.

Podłogówka pracowała niemal cały czas, a cel nie został osiągnięty. Zwiększenie nastawy nie zwiększy jej mocy. Po poprawieniu fałszywego odcięcia należy sprawdzić rzeczywistą moc grzania, przewiewy i straty cieplne oraz położenie czujników. Statystyki mocy całego wyjścia falownika podczas grzania wynosiły około 900 W, lecz nie są pomiarem samej podłogówki.

Bateria czujnika obecności wskazuje 20%; warto ją wymienić lub sprawdzić. Sam odczyt nie potwierdza, że bateria spowodowała obserwowane zachowanie.

Nie sprawdzano fizycznego odłączenia AC, temperatury powierzchni podłogi ani tego, czy samochód był faktycznie zajęty przez całą noc. Wieczór przed północą to ręczne grzanie; krótkie przełączenia około 23:58 i 00:01 należały do wdrożenia i testów.

