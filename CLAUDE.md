# CLAUDE.md – GIS-Akademie Symbolbibliothek für QGIS

SVG-Symbolbibliothek der GIS-Akademie, aufgebaut als Repository für das QGIS-Plugin
**Resource Sharing**. Repo: `GIS-Akademie/qgis-symbole` (derzeit privat, soll später öffentlich werden).
Lizenz der Symbole: CC BY 4.0. Nutzerdoku steht in `README.md`, die Symbolliste in `KATALOG.md`.

## Grundregel: Alles wird erzeugt

`collections/`, `metadata.ini`, `KATALOG.md` und `LICENSE` sind **Ergebnisse des Generators**.
Nie von Hand bearbeiten. Änderungen immer in `tools/` vornehmen und neu erzeugen:

```powershell
python tools\vorschau.py <sammlung> <bild.png>   # Kontrollbild einer Sammlung mit Symbolnamen
python tools\mkrepo.py .                         # alles neu erzeugen
```

- Ziel `.` (das eigene Repo): erzeugt nur `collections/` und die Dateien im Hauptordner neu, `tools/` bleibt.
- Anderer Zielordner: dort entsteht ein vollständiges Repo samt Kopie von `tools/`.
- `collections/` wird vor dem Neuerzeugen gelöscht. Danach mit `git diff --stat` prüfen, dass sich nur das
  Erwartete geändert hat. Ein Lauf ohne Änderungen an `tools/` muss einen leeren Diff ergeben.

## Aufbau von tools/

| Datei | Inhalt |
|---|---|
| `lib.py` | Grundformen (`C`, `E`, `R`, `PG`, `P`, `L`, `PL`, `T`), Bögen und Sektoren (`arc`, `pie`, `chord`, `cloud`), Gruppen (`G`, `fit`), Rahmen (`fr_circle`, `fr_square`, `fr_diamond`, `fr_hex`), wiederverwendbare Piktogramme (`person`, `house`, `bike`, `flame`, `drop` …), `render()`, Schriftsuche `find_font()` |
| `sammlungen.py` | Liste `MODULES` (Reihenfolge der Sammlungen), Laden und Prüfen, Rasterung mit `rsvg-convert` |
| `sym_<sammlung>.py` | Eine Datei je Sammlung mit `KEY`, `NAME`, `DESC`, `TAGS`, `SYMBOLS` |
| `mkrepo.py` | Schreibt SVGs, Vorschaubilder, `metadata.ini`, `KATALOG.md`, `LICENSE`; enthält `VERSION` |
| `vorschau.py` | Kontrollbild einer Sammlung zum Prüfen beim Zeichnen |

Ein Symbol ist ein Tupel `(name, titel, füllfarbe, strichfarbe, [grundformen])` in `SYMBOLS`.
Dateiname: `gisak_<KEY>_<name>.svg`, `titel` landet im `<title>` der SVG und im Katalog. Die Reihenfolge in
`SYMBOLS` ist die Reihenfolge in Vorschaubild und Katalog, also thematisch gruppieren.

Piktogramme werden im 100er-Raster um (50, 50) gezeichnet und mit `fit(elems, cx, cy, k, a)` gesetzt,
skaliert und gedreht. Winkel bei `pt`, `arc`, `pie`, `chord`: Grad, 0 = oben, im Uhrzeigersinn.

## Stil je Sammlung (unbedingt einhalten)

Der Stil steht im Kopfkommentar jeder `sym_*.py` und in der README-Tabelle „Stil und Vorbilder“. Kurzfassung:

| Sammlung | Regel |
|---|---|
| planzv | schwarz-weiß wie die Anlage zur PlanZV; Flächenzeichen im liegenden Rechteck, Lagezeichen im Kreis; Präfixe nach Abschnitt der Anlage (`nu_`, `bw_`, `gb_`, `vk_`, `ve_`, `gr_`, `wa_`, `pf_`, `sg_`, `dk_`, `um_` …) |
| strom | rot auf weiß; Quadrat = Station, Draufsicht = Mast, ohne Rahmen = Garnitur/Schaltzeichen auf der Leitung |
| eeg | immer Kreisrahmen; Farbe = Energieträger, Rahmenart = Status |
| naturschutz | grün; Quadrat = Schutzgebiet (Kurzzeichen), Kreis = Art (Piktogramm), Raute = Maßnahme, Sechseck = Einrichtung |
| landschaftsplanung | grün (Wasser blau); Draufsicht = Gehölz, Quadrat = Biotoptyp, gestricheltes Quadrat = Maßnahme, Kreis = Erholung |
| verkehr | immer Quadrat mit weißem Sinnbild; blau, orange (Störung), rot (Sperrung) |
| wasser | blau; Kreis = Messstelle, Quadrat = Anlage, Raute = Gebiet, ohne Rahmen = Armatur auf der Leitung |
| vermessung | schwarz-weiß, geometrische Grundformen ohne Rahmen; `topo_` = Topografie im Lageplan |
| allgemein | immer weißes Quadrat mit dunklem Sinnbild; grau, rot (Rettung), blau (Dienste) |

Neue Symbole in die passende Gruppe einordnen und deren Rahmen-Helfer der Datei verwenden (z. B. `vq()`, `kr()`).
Keinen neuen Rahmentyp oder eine neue Farbe einführen, ohne die Tabellen hier und in der README zu ergänzen.

## Konventionen für Symbole

- Raster 100 × 100 (`viewBox="0 0 100 100"`), Strichstärke meist 5, runde Enden und Ecken.
- Farbrollen: `F` = Füllfarbe (`param(fill)`), `S` = Strichfarbe (`param(outline)`, auch für dunkle Zeichen),
  `W` = festes Weiß, `N` = keine. Nur `F` und `S` sind in QGIS änderbar. Strichstärken bewusst nicht parametrisieren.
- Text nur über `T()`: wird mit **Liberation Sans Bold** in Pfade umgewandelt, keine `<text>`-Elemente.
- Linienelemente (für Markierungslinien): Linie waagerecht durch die Symbolmitte (y = 50); bei PlanZV-`um_`
  liegt die Innenseite unten.
- **Amtliche Vorlage zuerst ansehen**, wenn es eine gibt. PlanZV: Anlage unter
  `https://www.gesetze-im-internet.de/planzv_90/anlage.html` (Zeichen als Grafiken eingebettet).
- **Dateinamen nach der Veröffentlichung nie ändern oder löschen** – QGIS-Projekte verweisen auf den Pfad.
  Stattdessen ein neues Symbol ergänzen. (Bis zur Veröffentlichung sind Umbenennungen noch möglich.)
- Keine Marken- oder Unternehmenslogos nachbilden (z. B. DB, Verkehrsverbünde, Apotheken-A, Post).
- Titel ohne `&`, `<`, `>` (werden ungeprüft in die SVG geschrieben).

## Bei neuen Symbolen oder Sammlungen

1. Symbol in `tools/sym_<sammlung>.py` ergänzen. Neue Sammlung: neue Datei und Eintrag in `MODULES` in `sammlungen.py`.
2. `python tools\vorschau.py <sammlung> <bild.png>` und das Bild ansehen; erst danach `python tools\mkrepo.py .`.
3. **Von Hand nachziehen** (wird nicht erzeugt): Tabelle mit den Symbolzahlen und die Gesamtzahl in `README.md`,
   bei neuen Gruppen auch die Stil-Tabellen in `README.md` und hier.
4. Nach der Veröffentlichung bei inhaltlichen Änderungen `VERSION` in `mkrepo.py` erhöhen (gilt für alle Sammlungen).

## Prüfen in QGIS

QGIS liegt unter `C:\OSGeo4W`. Ob QGIS alle SVGs darstellen kann, lässt sich ohne Oberfläche prüfen:
mit `C:\OSGeo4W\bin\python-qgis.bat` ein Skript starten, das jede Datei über
`QgsApplication.svgCache().svgAsImage(pfad, 96, füllfarbe, strichfarbe, 1.0, 1.0, 0, True)` rendert, und das
Ergebnis mit der `rsvg-convert`-Darstellung vergleichen. Stand 17.11.2026: alle 542 Symbole in QGIS 4.2.3
pixelgleich zur Referenz (auch `<g transform>`, Strichmuster und Bögen).

## Umgebung (Windows)

- Python: die ArcGIS-Pro-Umgebung (`arcgispro-py3`) hat `fonttools`, `Pillow` und `lxml` bereits.
- Schrift **Liberation Sans 2.1.5** (bei anderer Version weichen die Textpfade ab). Wird in den Schriftordnern von
  Windows/Linux/macOS gesucht oder über `GISAK_FONT_DIR`. Ohne die Schrift bricht der Generator bewusst ab;
  kein Ersatz durch Arial für Symbole.
- `rsvg-convert` für die Vorschaubilder ist unter Windows nicht vorinstalliert. Bewährt: eigene conda-Umgebung
  mit `librsvg` von conda-forge, deren `Library\bin` vor dem Lauf in den `PATH` nehmen.
- In der Git Bash Windows-Pfade für Umgebungsvariablen mit `cygpath -w` umwandeln; im `PATH` die Form `/c/...` nutzen.
- Zeilenenden: `.gitattributes` erzwingt LF für SVG, INI, MD, PY. Dateien immer mit `newline="\n"` schreiben.

## Git

- Branch **`master`** (nicht umbenennen, die README nennt ihn für Resource Sharing).
- Ein-Personen-Projekt: Arbeiten direkt auf `master` ist in Ordnung.
- Commit-Nachrichten nach Muster `typ: was und warum` auf Deutsch (`feat`, `fix`, `docs`, `chore`).
- Keine Dateien aus Chat-Downloads committen: Diese tragen einen C2PA-Herkunftsnachweis (`xmlns:c2pa`,
  `<metadata><c2pa:manifest>`). Stattdessen mit dem Generator neu erzeugen. Prüfen mit `grep -rl c2pa collections`.
- Öffentlich schalten (erst nach Rücksprache):
  `gh repo edit GIS-Akademie/qgis-symbole --visibility public --accept-visibility-change-consequences`
