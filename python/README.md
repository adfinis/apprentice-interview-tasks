# Python

Öffne die Datei [rock_paper_scissor.py](./rock_paper_scissor.py) mit einem
Text-Editor (Rechtsklick, danach öffnen mit Editor).

Navigiere in einem Terminal zum python Ordner (`cd`). Führe die python-Datei aus
(`./rock_paper_scissor.py`) und spiele eine Runde Schere, Stein, Papier.

Mach dich mir dem Spiel und dem Script bekannt. Welche Features werden bereitgestellt?

## Erste Aufgabe

Ein Bug hat sich in das Skript geschlichen. Findest du ihn? Kannst du den Bug flicken?

## Zweite Aufgabe

Mit welcher Option hast du statistisch die besten Chancen, um zu gewinnen? Kannst du
das Skript so verändern, dass keine der Optionen eine höhere Gewinnchance hat?

## Dritte Aufgabe

Wird zur Laufzeit des Programms `Ctrl+c` oder `Ctrl+d` eingegeben, wird ein
`KeyboardInterrupt`-, respektive `EOFError`-Fehler geworfen.

Kannst du diese Situationen so handeln, dass anstelle dieser Fehler der String
`Good bye!` angezeigt wird?

## Vierte Aufgabe

Das Skript beinhaltet diverse debug-logs, diese werden jedoch nicht angezeigt.

Implementiere einen CLI-Toggle, um debug-Meldungen auszugeben (`-v` / `--verbose`).

## Fünfte Aufgabe

Zurzeit besteht (wie im analogen Schere, Stein, Papier) die gleiche Wahrscheinlichkeit
für einen Sieg, eine Niederlage oder ein Unentschieden. Kannst du das Skript so
anpassen, dass eine 50:50 Wahrscheinlichkeit für Sieg und Niederlage besteht und ein
Unentschieden verunmöglicht wird?

## Hilfestellungen

 * Informationen zu [Errors und Exceptions](https://docs.python.org/3/tutorial/errors.html)
 * Informationen zu [argparse](https://docs.python.org/3/library/argparse.html)
 * Informationen zum [logging-Modul](https://docs.python.org/3/library/logging.html)
