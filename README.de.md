
# Übungsaufgaben für Schnupperlehrlinge

Dieses Repository enthält verschiedene Aufgaben, die von Schnupperlehrlingen
durchgeführt werden können. Das Ziel ist, einen ersten Einblick in die Arbeit
als Software-Entwickler/in zu erhalten.

## Einführung - Linux

Wir verwenden als Arbeits-Betriebssystem Linux. Hast du davon schon gehört?
Versuche dich auf dem Desktop zurechtzufinden. Welche Unterschiede zu deinem
eigenen PC findest du?

## Übung 1 - HTML, CSS und Formulare

Öffne den Ordner [html_css](./html_css/). Darin findest du eine Datei namens 
[index.html](./html_css/index.html). Öffne diese mit einem Webbrowser (Firefox, Chrome) und nebenbei
mit einem Text-Editor (Rechtsklick, danach öffnen mit Editor).

### Erste Aufgabe

Verändere die Datei im Editor, speichere sie und lade die Seite im Browser neu.
Was passiert? Wie wirkt sich die Änderung aus?

### Zweite Aufgabe

Versuche, im Formular ein neues Eingabefeld hinzuzufügen. Welche
Eingabefelder-Arten gibt es? Wie werden sie angezeigt?

### Dritte Aufgabe

Versuche, das Aussehen des Formulars zu verändern. Verwende dazu CSS-Regeln.

Mögliche Anpassungen:

* Versuche, den Hintergrund der Seite zu verändern (Bild oder Farbe)
* Verändere die Ränder der Eingabefelder
* Verändere die Schriftart einzelner Elemente, oder der ganzen Seite


### Hilfestellungen

Zum Verständnis von HTML und CSS kannst du im [SelfHTML](https://wiki.selfhtml.org/)
nachlesen.

* Hier geht's direkt zum [Thema Formulare](https://wiki.selfhtml.org/wiki/HTML/Formulare)
* Hier geht's direkt zum [Thema CSS](https://wiki.selfhtml.org/wiki/CSS)


## Übung 2 - Javascript, Codeverständnis

Öffne den Ordner [javascript](./javascript/). Darin findest du eine Datei namens
[index.html](./javascript/index.html). Öffne diese mit einem Webbrowser (Firefox,
Chrome) und nebenbei mit einem Text-Editor (Rechtsklick, danach öffnen mit Editor).


### Aufgabe 1

Versuche zu verstehen, was der Javascript-Code macht. Spiele mit den Zahlen,
speichere das Dokument und prüfe im Browser, was es für Auswirkungen hat.

Wofür stehen die Zahlen? Wie ist das Koordinatensystem orientiert?

### Aufgabe 2

Versuche, die Schrift `adfinis` ins Rechteck zu verschieben. Was musst du am
Code anpassen, damit dies geschieht?

### Aufgabe 3

Versuche, den weissen Bereich im Quadrat grösser oder kleiner zu machen.

### Aufgabe 4

Füge eine zweite Linie hinzu, sodass sie mit der bestehenden diagonalen Linie
ein Kreuz bildet.

### Aufgabe 5

Versuche, andere Figuren zu zeichnen. Welche gibt es? Wie werden sie erstellt?
Kannst du die Farben ändern?

### Hilfestellungen

Im [SelfHTML](https://wiki.selfhtml.org/) gibt es auch zu diesem Thema eine
ausführliche Dokumentation:

* Informationen zum Thema [Canvas im Allgemeinen](https://wiki.selfhtml.org/wiki/JavaScript/Canvas)
* Informationen zum Thema [Formen und Pfade](https://wiki.selfhtml.org/wiki/JavaScript/Canvas/Formen_und_Pfade)

## Übung 3 - Python

Öffne den Ordner [python](./python). Darin findest du eine Datei namens
[rock_paper_scissor.py](python/rock_paper_scissor.py). Öffne diese mit einem
Text-Editor (Rechtsklick, danach öffnen mit Editor).

Navigiere in einem Terminal zum python Ordner (`cd`). Führe die python-Datei aus
(`./rock_paper_scissor.py`) und spiele eine Runde Schere, Stein, Papier.

Mach dich mir dem Spiel und dem Script bekannt. Welche Features werden bereitgestellt?

### Erste Aufgabe

Ein Bug hat sich in das Skript geschlichen. Findest du ihn? Kannst du den Bug flicken?

### Zweite Aufgabe

Mit welcher Option hast du statistisch die besten Chancen, um zu gewinnen? Kannst du
das Skript so verändern, dass keine der Optionen eine höhere Gewinnchance hat?

### Dritte Aufgabe

Wird zur Laufzeit des Programms `Ctrl+c` oder `Ctrl+d` eingegeben, wird ein
`KeyboardInterrupt`-, respektive `EOFError`-Fehler geworfen.

Kannst du diese Situationen so handeln, dass anstelle dieser Fehler der String
`Good bye!` angezeigt wird?

### Vierte Aufgabe

Das Skript beinhaltet diverse debug-logs, diese werden jedoch nicht angezeigt.

Implementiere einen CLI-Toggle, um debug-Meldungen auszugeben (`-v` / `--verbose`).

### Fünfte Aufgabe

Zurzeit besteht (wie im analogen Schere, Stein, Papier) die gleiche Wahrscheinlichkeit
für einen Sieg, eine Niederlage oder ein Unentschieden. Kannst du das Skript so
anpassen, dass eine 50:50 Wahrscheinlichkeit für Sieg und Niederlage besteht und ein
Unentschieden verunmöglicht wird?

### Hilfestellungen

 * Informationen zu [Errors und Exceptions](https://docs.python.org/3/tutorial/errors.html)
 * Informationen zu [argparse](https://docs.python.org/3/library/argparse.html)
 * Informationen zum [logging-Modul](https://docs.python.org/3/library/logging.html)
