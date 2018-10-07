# �bungs-Pr�fungsaufgabensammlung

## Anmerkung zu pull requests

In dieser Repository werden keine Pull-Requests akzeptiert, die propriet�ren or patentbehaftete Dateiformate (unter anderem MS Office Dokumente) akzeptiert.

## Format von Aufgaben

Aufgaben stehen unter /Angaben zur Verf�gung. Alle Aufgaben werden als UTF-8 TeX Segmente abgelegt. Jede Datei beinhaltet immer nur eine einzelne Aufgabe sowie zugeh�rige Metadaten:

Keywords k�nnen mit Hilfe des TeX Kommandso \exkw hinzugef�gt werden. Diese dienen der Suche innerhalb der Aufgaben:

```
\exkw{Keyword}
```

Kompetenzen, die von den jeweiligen Aufgaben abgedeckt werden, k�nnen mit Hilfe von

```
\excomp{FA}
\excomp{FA5}
\excomp{FA5_1}
```

hinzugef�gt werden. Dies dient ebenfalls der automatisierten Suche. Die eigentliche Angabe findet sich als TeX Quellcode nach der Angabe ihres Titels unter

```
\exquestion{Titel}
```

Eine eventuell vorhandene L�sung folgt der Angabe nach Einleitung mit Hilfe von

```
\exsolution{Titel}
```

wobei der Titel der Frage und der L�sung �bereinstimmen m�ssen.

## Format von Aufgabengeneratoren

Aufgabengeneratoren stehen unter /Generatoren als ANSI C99 Quellcode zur Verf�gung.