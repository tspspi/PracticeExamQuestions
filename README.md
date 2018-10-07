# Übungs-Prüfungsaufgabensammlung

## Anmerkung zu pull requests

In dieser Repository werden keine Pull-Requests akzeptiert, die proprietären or patentbehaftete Dateiformate (unter anderem MS Office Dokumente) akzeptiert.

## Format von Aufgaben

Aufgaben stehen unter /Angaben zur Verfügung. Alle Aufgaben werden als UTF-8 TeX Segmente abgelegt. Jede Datei beinhaltet immer nur eine einzelne Aufgabe sowie zugehörige Metadaten:

Keywords können mit Hilfe des TeX Kommandso \exkw hinzugefügt werden. Diese dienen der Suche innerhalb der Aufgaben:

```
\exkw{Keyword}
```

Kompetenzen, die von den jeweiligen Aufgaben abgedeckt werden, können mit Hilfe von

```
\excomp{FA}
\excomp{FA5}
\excomp{FA5_1}
```

hinzugefügt werden. Dies dient ebenfalls der automatisierten Suche. Die eigentliche Angabe findet sich als TeX Quellcode nach der Angabe ihres Titels unter

```
\exquestion{Titel}
```

Eine eventuell vorhandene Lösung folgt der Angabe nach Einleitung mit Hilfe von

```
\exsolution{Titel}
```

wobei der Titel der Frage und der Lösung übereinstimmen müssen.

## Format von Aufgabengeneratoren

Aufgabengeneratoren stehen unter /Generatoren als ANSI C99 Quellcode zur Verfügung.