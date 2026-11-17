# CLAUDE.md – GIS-Akademie Symbolbibliothek für QGIS

SVG-Symbolbibliothek der GIS-Akademie, aufgebaut als Repository für das QGIS-Plugin
**Resource Sharing**. Repo: `GIS-Akademie/qgis-symbole` (derzeit privat, soll später öffentlich werden).
Lizenz der Symbole: CC BY 4.0. Nutzerdoku steht in `README.md`, die Symbolliste in `KATALOG.md`.

## Grundregel: Alles wird erzeugt

`collections/`, `metadata.ini`, `KATALOG.md` und `LICENSE` sind **Ergebnisse des Generators**.
Nie von Hand bearbeiten. Änderungen immer in `tools/` vornehmen und neu erzeugen:

```powershell
python tools\mkrepo.py .
```

- Ziel `.` (das eigene Repo): erzeugt nur `collections/` und die Dateien im Hauptordner neu, `tools/` bleibt.
- Anderer Zielordner: dort entsteht ein vollständiges Repo samt Kopie von `tools/`.
- `collections/` wird vor dem Neuerzeugen gelöscht. Danach mit `git diff --stat` prüfen, dass sich nur das
  Erwartete geändert hat. Ein Lauf ohne Änderungen an `tools/` muss einen leeren Diff ergeben.

## Aufbau von tools/

| Datei | Inhalt |
|---|---|
| `lib.py` | Grundformen (`C`, `E`, `R`, `PG`, `P`, `L`, `PL`, `T` …), Rahmen (`fr_circle` …), Helfer, `render()`, Schriftsuche `find_font()` |
| `sym_a.py` | Sammlungen `planzv`, `strom`, `eeg` |
| `sym_b.py` | Sammlungen `naturschutz`, `landschaftsplanung`, `verkehr`, `wasser`, `vermessung`, `allgemein` |
| `mkrepo.py` | Schreibt SVGs, Vorschaubilder, `metadata.ini`, `KATALOG.md`, `LICENSE`; enthält `META` (Name, Beschreibung, Tags je Sammlung) |

Ein Symbol ist ein Tupel `(name, titel, füllfarbe, strichfarbe, [grundformen])` in der Liste `S`,
die am Ende als `CAT["<sammlung>"] = S` registriert wird. Dateiname: `gisak_<sammlung>_<name>.svg`,
`titel` landet im `<title>` der SVG und im Katalog.

## Konventionen für Symbole

- Raster 100 × 100 (`viewBox="0 0 100 100"`), Strichstärke meist 5, runde Enden und Ecken.
- Farbrollen: `F` = Füllfarbe (`param(fill)`), `S` = Strichfarbe (`param(outline)`, auch für dunkle Zeichen),
  `W` = festes Weiß, `N` = keine. Nur `F` und `S` sind in QGIS änderbar. Strichstärken bewusst nicht parametrisieren.
- Text nur über `T()`: wird mit **Liberation Sans Bold** in Pfade umgewandelt, keine `<text>`-Elemente.
- **Dateinamen nach der Veröffentlichung nie ändern oder löschen** – QGIS-Projekte verweisen auf den Pfad.
  Stattdessen ein neues Symbol ergänzen.
- Keine Marken- oder Unternehmenslogos nachbilden (z. B. DB, Verkehrsverbünde).
- PlanZV-Zeichen sind Nachkonstruktionen in Anlehnung an die Anlage zur PlanZV, keine amtlichen Vorlagen.

## Bei neuen Symbolen oder Sammlungen

1. Symbol in `sym_a.py`/`sym_b.py` ergänzen. Neue Sammlung: zusätzlich Eintrag in `META` in `mkrepo.py`.
2. `python tools\mkrepo.py .` und das Vorschaubild `collections/<id>/preview/preview.png` ansehen.
3. **Von Hand nachziehen** (wird nicht erzeugt): Tabelle mit den Symbolzahlen und die Gesamtzahl in `README.md`.
4. Bei inhaltlichen Änderungen einer Sammlung `version=` in `mkrepo.py` erhöhen (steht derzeit fest auf `1.0`
   für alle Sammlungen).

## Umgebung (Windows)

- Python: die ArcGIS-Pro-Umgebung (`arcgispro-py3`) hat `fonttools`, `Pillow` und `lxml` bereits.
- Schrift **Liberation Sans 2.1.5** (bei anderer Version weichen die Textpfade ab). Wird in den Schriftordnern von
  Windows/Linux/macOS gesucht oder über `GISAK_FONT_DIR`. Ohne die Schrift bricht der Generator bewusst ab;
  kein Ersatz durch Arial für Symbole.
- `rsvg-convert` für die Vorschaubilder ist unter Windows nicht vorinstalliert. Bewährt: eigene conda-Umgebung
  mit `librsvg` von conda-forge, deren `Library\bin` vor dem Lauf in den `PATH` nehmen.
- In der Git Bash Windows-Pfade für Umgebungsvariablen mit `cygpath -w` umwandeln.
- Zeilenenden: `.gitattributes` erzwingt LF für SVG, INI, MD, PY. Dateien immer mit `newline="\n"` schreiben.

## Git

- Branch **`master`** (nicht umbenennen, die README nennt ihn für Resource Sharing).
- Ein-Personen-Projekt: Arbeiten direkt auf `master` ist in Ordnung.
- Commit-Nachrichten nach Muster `typ: was und warum` auf Deutsch (`feat`, `fix`, `docs`, `chore`).
- Keine Dateien aus Chat-Downloads committen: Diese tragen einen C2PA-Herkunftsnachweis (`xmlns:c2pa`,
  `<metadata><c2pa:manifest>`). Stattdessen mit dem Generator neu erzeugen. Prüfen mit `grep -rl c2pa collections`.
- Öffentlich schalten (erst nach Rücksprache):
  `gh repo edit GIS-Akademie/qgis-symbole --visibility public --accept-visibility-change-consequences`
