# OOP_Skriptsprachen_TreeWalk
TreeWalk ESA

## Aufgabe:

*Erstellen Sie ein Programm, welches einen Verzeichnisbaum durchwandert (inkl. der Unterverzeichnisse -- also rekursiv). Ermitteln Sie für jeden gefundenen Eintrag die MD5-Summe.  Das Programm soll auf der Standardausgabe für jeden gefundenen Eintrag (Datei, Verzeichnis, Link, ..) den Dateinamen, den Dateipfad (relativ zum Startverzeichnis) sowie  die MD5-Summe (nur für die Datei)  ausgeben. Das Startverzeichnis soll als Kommandozeilen-Parameter an das Skript übergeben werden. 

*Es soll auch möglich sein, das die Funktion oder Methode in andere Python-Skripte zu importieren.

*Verwenden Sie nicht os.walk oder os.path.walk. Fangen Sie Exceptions, die zum Beispiel auftreten, wenn die Leserechte fehlen.

*Nützliche Module bzw. Funktionen sind hashlib, os.listdir.



## Beispiel-Kommandos & Ausgabe:

> DirTreeWalk.py

usage: DirTreeWalk.py [-h] path



positional argument:

  path        path to show



optional arguments:

  -h, --help  show this help message and exit



>DirTreeWalk.py mich_gibt_es_nicht

Error: Path not found: mich_gibt_es_nicht!



>DirTreeWalk.py c:/Downloads/informatik-in-brandenburg


css                    <dir>

bootstrap.min.css      css/bootstrap.min.css      6e1130d2b2cb83d549ab428771a7e44e

font-awesome.css       css/font-awesome.css       1f9e9d1a5a1d347d945ef4b7727f2ea0
