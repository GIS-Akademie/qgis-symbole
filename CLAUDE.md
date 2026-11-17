# CLAUDE.md – GIS-Akademie Symbolbibliothek für QGIS

Symbolbibliothek der GIS-Akademie (SVG-Punktsymbole, dazu Linien- und Flächensymbole als QGIS-Stildatei),
aufgebaut als Repository für das QGIS-Plugin **Resource Sharing**. Repo: `GIS-Akademie/qgis-symbole` (derzeit privat, soll später öffentlich werden).
Lizenz der Symbole: CC BY 4.0. Nutzerdoku steht in `README.md`, die Symbolliste in `KATALOG.md`.

## Grundregel: Alles wird erzeugt

`collections/`, `metadata.ini`, `KATALOG.md` und `LICENSE` sind **Ergebnisse des Generators**.
Nie von Hand bearbeiten. Änderungen immer in `tools/` vornehmen und neu erzeugen:

```powershell
python tools\vorschau.py <sammlung> <bild.png>        # Kontrollbild der Punktsymbole mit Symbolnamen
python tools\vorschau_stil.py <sammlung> <bild.png>   # Kontrollbild der Linien- und Flächensymbole
python tools\mkrepo.py .                              # alles neu erzeugen
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
| `sym_<sammlung>.py` | Eine Datei je Sammlung mit `KEY`, `NAME`, `DESC`, `TAGS`, `SYMBOLS`, wahlweise `LINIEN` und `FLAECHEN` |
| `qstil.py` | Ebenen für Linien- und Flächensymbole (`linie`, `marken`, `voll`, `schraffur`, `muster`, `band`, Marker `mk`, `sv`), schreibt die QGIS-Stildatei und zeichnet deren Vorschau als SVG nach |
| `mkrepo.py` | Schreibt SVGs, Stildateien, Vorschaubilder, `metadata.ini`, `KATALOG.md`, `LICENSE`; enthält `VERSION` |
| `vorschau.py` | Kontrollbild der Punktsymbole einer Sammlung zum Prüfen beim Zeichnen |
| `vorschau_stil.py` | Kontrollbild der Linien- und Flächensymbole einer Sammlung |

Ein Symbol ist ein Tupel `(name, titel, füllfarbe, strichfarbe, [grundformen])` in `SYMBOLS`.
Dateiname: `gisak_<KEY>_<name>.svg`, `titel` landet im `<title>` der SVG und im Katalog. Die Reihenfolge in
`SYMBOLS` ist die Reihenfolge in Vorschaubild und Katalog, also thematisch gruppieren.

Piktogramme werden im 100er-Raster um (50, 50) gezeichnet und mit `fit(elems, cx, cy, k, a)` gesetzt,
skaliert und gedreht. Winkel bei `pt`, `arc`, `pie`, `chord`: Grad, 0 = oben, im Uhrzeigersinn.

Ein Linien- oder Flächensymbol ist ein Tupel `(titel, [ebenen])` in `LINIEN` bzw. `FLAECHEN`; die Ebenen werden
von unten nach oben gezeichnet, Maße in Millimetern, Farben `#RRGGBB` oder `#RRGGBBAA`. In QGIS heißt das Symbol
`<NAME>: <titel>`, die Datei `collections/<ID>/symbol/Linien_und_Flaechen.xml`. Die Beschreibung aller Ebenen
steht im Kopf von `qstil.py`.

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
| nordpfeile | schwarz-weiß, ohne Rahmen, Spitze oben, Achse x = 50, N (Versalhöhe 18) über der Spitze; Präfix = Bauart (`pfeil_`, `nadel_`, `kreis_`, `rose_`), Endung `_ohne_n` = ohne Buchstabe; keine Linien und Flächen |
| allgemein | immer weißes Quadrat mit dunklem Sinnbild; grau, rot (Rettung), blau (Dienste) |
| raumordnung | Punktsymbole schwarz-weiß: konzentrische Kreise = Zentraler Ort, Quadrat mit scharfen Ecken = Standort, Kreis = Infrastruktur, Raute = Freiraum, kleines Quadrat = Kategorie (Z, G, N, V); Flächen farbig: Vorranggebiet durchgezogen und dicht, Vorbehaltsgebiet gestrichelt und weit |
| leitungen | Farbe = Sparte (Gas gelb `#FFF3B0`/`#9A6B00`, Fernwärme `#FBE0D2`/`#C2410C`, Telekommunikation `#DDF0E0`/`#1B7F3B`); Quadrat = Station, Kreis = Messstelle, ohne Rahmen = Armatur auf der Leitung; Präfixe `gas_`, `fw_`, `tk_` |
| boden | braun `#EAD9C3`/`#6B4423`; Kreis = Aufschluss/Messstelle, Quadrat = Altlast/Standort, Raute = Bodenschutz, Sechseck = Geologie und Rohstoffe |
| laerm | violett `#EFE3F5`/`#5E2B7E`; Kreis = Immissionsort/Messung, Quadrat = Quelle, Raute = Schutzmaßnahme, Sechseck = schutzbedürftige Nutzung, ohne Rahmen = Hilfszeichen; einzige Ausnahme: Pegelklassen in den Farben der DIN 45682 |
| forst | dunkelgrün `#DCE8C8`/`#3B5B1F`; Baumkrone ohne Rahmen = Baumart/Bestand (Bogenrand Laub-, Zackenrand Nadelholz), Quadrat = Einrichtung, Kreis = Jagd und Wild, Raute = Waldfunktion |
| landwirtschaft | ocker `#F3EBC2`/`#6B5E12`; Quadrat = Betrieb/Gebäude, Kreis = Kultur, Sechseck = Technik und Wasser, Raute = Schutz/Förderung |
| tourismus | immer Quadrat mit weißem Sinnbild; grau = Unterkunft/Service, grün = Wandern/Rad/Natur, blau = Wasser/Winter, braun = Sehenswertes |
| denkmal | ziegelrot `#F3E3D8`/`#8C2F1B`; Quadrat = Baudenkmal, Kreis = Bodendenkmal/Fundstelle, Raute = Status, Sechseck = Erinnerung; gestrichelt = vermutet oder abgegangen (nicht „geplant“) |
| brandschutz | immer Quadrat mit weißem Sinnbild; rot = Feuerwehr, grün = Rettung/Flucht, blau = Katastrophenschutz; Gefahren als gelbes Dreieck mit schwarzem Sinnbild |
| layout | schwarz-weiß; Kreis = Nummer (`nr_`, gefüllt `nrv_`), Quadrat = Buchstabe (`bu_`), Raute = Hinweis (`hw_`), ohne Rahmen = Pfeil oder Marke; rot `#C8102E` nur für Hervorhebungen bei Linien und Flächen |

Neue Symbole in die passende Gruppe einordnen und deren Rahmen-Helfer der Datei verwenden (z. B. `vq()`, `kr()`).
Keinen neuen Rahmentyp oder eine neue Farbe einführen, ohne die Tabellen hier und in der README zu ergänzen.

Linien und Flächen nutzen die Farben der Punktsymbole ihrer Sammlung (die Farbkonstanten der Datei verwenden).
Durchgezogen = Bestand, gestrichelt = geplant oder Maßnahme. Ausnahmen, die so bleiben sollen:

| Sammlung | Linien und Flächen |
|---|---|
| planzv | Linienarten schwarz wie in der Schwarz-Weiß-Fassung, dazu Baulinie, Baugrenze und Straßenbegrenzungslinie farbig; Flächen in den Farben der farbigen Fassung; Umgrenzungen als Linie mit den `um_`-SVGs auf der Innenseite |
| strom | Strichstärke = Spannungsebene, durchgezogen = Freileitung, gestrichelt = Kabel |
| eeg | Farbe = Energieträger (Konstanten `WIND`, `SUN`, `BIO`, `GEO`, `NEU`) |
| verkehr | Straßen blau nach Klasse abgestuft, orange = Baustelle und Umleitung, rot = Sperrung und Stau |
| wasser | Trinkwasser und Gebiete dunkelblau, Gewässer und Regenwasser hellblau `#3FA9F5`, Schmutzwasser braun `#8B5A2B`, Mischwasser violett `#7B3FA0` |
| landschaftsplanung | Gehölze als Kreisreihe, Wege braun, Siedlung grau |

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

## Konventionen für Linien und Flächen

- Die Stildatei schreibt Eigenschaften bewusst als `<prop k v>` und nicht als `<Option>`: Nur so ersetzt
  Resource Sharing beim Installieren die SVG-Dateinamen durch den Pfad der installierten Sammlung
  (`fix_xml_node` im Plugin). QGIS 3.44 und 4.2 lesen diese Schreibweise weiterhin.
- SVG-Markierungen (`sv(name, …)`) nur mit Symbolen der eigenen Sammlung; in der Datei steht nur der Dateiname.
- Markierungen stehen so, wie sie auf einer Linie von links nach rechts erscheinen. `dy > 0` und `versatz > 0`
  liegen rechts in Laufrichtung, bei Flächen innen (Symbole mit `marken` setzen dafür `force_rhr`).
  Dreht man eine Markierung mit `winkel`, dreht sich ihr `dy` mit.
- Randzeichen an Flächen immer mit `marken(…, ecken=<mm>)`: Das schreibt zwei ineinander gesetzte
  Geometriegeneratoren (Einheit mm): Der äußere trennt den Umriss an Knicken über 25° auf, der innere kürzt jeden
  Abschnitt so, dass die Zeichen mittig sitzen (`qstil.ecken_ausdruecke`).
  Der Generator rechnet in Zeichenkoordinaten (y nach unten), deshalb `force_polygon_ccw`, damit rechts innen ist.
- **Ausdrücke flach halten.** Der Parser von QGIS 3.x (geprüft 3.44) braucht je Ebene verschachtelter
  Funktionsaufrufe etwa doppelt so lange: 14 Ebenen 4 ms, 18 Ebenen 0,1 s, rund 24 Ebenen 1,5 s – und QGIS parst
  bei jedem Kopieren eines Symbols neu. Ein einziger tiefer Ausdruck ließ die Symbolauswahl einfrieren
  („Application Hang“ im Windows-Ereignisprotokoll). QGIS 4.2 zeigt das nicht, deshalb immer auch in der
  LTR-Version messen: `QgsSymbolLayerUtils.symbolPreviewPixmap()` je Symbol muss unter 0,05 s bleiben.
  Beim Test ohne Oberfläche braucht der Render-Kontext einen Ausdruckskontext mit dem Feature, sonst zeichnet
  der Generator nichts.
- Randbänder innen mit `band()`; Versätze bei Flächenumrissen vermeiden, sie hängen von der Umlaufrichtung ab.
- Striche (`strich=[…]`) sind Längen in Millimetern mit flachen Enden; ein Punkt ist ein kurzer Strich.
- Die Vorschau (`qstil.vorschau_svg`) bildet QGIS nach. Neue Ebenenarten oder Markerformen immer in beiden
  Teilen ergänzen (XML und Vorschau) und in QGIS gegenprüfen.
- Symbolnamen dürfen sich ändern (Projekte speichern das Symbol, nicht den Namen); Titel je Sammlung eindeutig.

## Bei neuen Symbolen oder Sammlungen

1. Symbol in `tools/sym_<sammlung>.py` ergänzen. Neue Sammlung: neue Datei und Eintrag in `MODULES` in `sammlungen.py`.
2. `python tools\vorschau.py <sammlung> <bild.png>` (Linien und Flächen: `vorschau_stil.py`) und das Bild ansehen;
   erst danach `python tools\mkrepo.py .`.
3. **Von Hand nachziehen** (wird nicht erzeugt): Tabelle mit den Symbolzahlen und die Gesamtzahlen in `README.md`
   (Punkte, Linien, Flächen; `mkrepo.py` gibt sie am Ende aus), bei neuen Gruppen auch die Stil-Tabellen in
   `README.md` und hier.
4. Nach der Veröffentlichung bei inhaltlichen Änderungen `VERSION` in `mkrepo.py` erhöhen (gilt für alle Sammlungen).

## Pflichtfelder der metadata.ini

Resource Sharing liest je Sammlung `author`, `email`, `name`, `tags` und `description` ohne Rückfallwert; fehlt
eines, scheitert schon das Hinzufügen des Repositorys („No option … in section“). `email` kommt aus `EMAIL` in
`mkrepo.py`. Prüfen lässt sich das mit `configparser.ConfigParser().read_file(…)` und `get()` auf diese Felder.

## Bekannte Schwäche des Plugins nach einem Push

Resource Sharing 1.2.0 klont mit `depth=1` und zieht später mit `dulwich.porcelain.pull` nach. Nach jedem neuen
Commit scheitert das mit `Error: (b'<alt>', b'<neu>')` (DivergedBranches), bis der lokale Klon unter
`<Profil>/resource_sharing/repositories/github.com/GIS-Akademie/qgis-symbole` gelöscht oder mit
`git fetch --depth=1 <url> master` und `git reset --hard FETCH_HEAD` nachgezogen wird. Deshalb Änderungen
gesammelt pushen, nicht in vielen kleinen Schritten.

## Prüfen in QGIS

QGIS liegt unter `C:\OSGeo4W`. Ob QGIS alle SVGs darstellen kann, lässt sich ohne Oberfläche prüfen:
mit `C:\OSGeo4W\bin\python-qgis.bat` ein Skript starten, das jede Datei über
`QgsApplication.svgCache().svgAsImage(pfad, 96, füllfarbe, strichfarbe, 1.0, 1.0, 0, True)` rendert, und das
Ergebnis mit der `rsvg-convert`-Darstellung vergleichen. Stand 17.11.2026: alle 1025 Symbole in QGIS 4.2.3
pixelgleich zur Referenz (auch `<g transform>`, Strichmuster und Bögen).

Stildateien: mit `QgsStyle().importXml(pfad)` in eine Speicher-Stildatenbank laden (`createMemoryDatabase()`),
jedes Symbol mit `renderFeature()` auf eine Testlinie und ein Testrechteck zeichnen (auch gegen den
Uhrzeigersinn digitalisiert) und mit dem Bild aus `vorschau_stil.py` vergleichen. Stand 17.11.2026: alle
499 Symbole laden in QGIS 4.2.3 und 3.44.15 und sehen aus wie die Vorschau; die Pfadersetzung des Plugins
(Version 1.2.0, `fix_xml_node` und `SymbolXMLExtractor`) löst alle SVG-Markierungen auf. Das Plugin 1.2.0
selbst läuft nur bis QGIS 3.99. Nicht geprüft: Installation über die Oberfläche des Plugins.

## Umgebung (Windows)

- Python: die ArcGIS-Pro-Umgebung (`arcgispro-py3`) hat `fonttools`, `Pillow` und `lxml` bereits.
- Schrift **Liberation Sans 2.1.5** (bei anderer Version weichen die Textpfade ab). Wird in den Schriftordnern von
  Windows/Linux/macOS gesucht oder über `GISAK_FONT_DIR`. Ohne die Schrift bricht der Generator bewusst ab;
  kein Ersatz durch Arial für Symbole.
- `rsvg-convert` für die Vorschaubilder ist unter Windows nicht vorinstalliert. Bewährt: eigene conda-Umgebung
  mit `librsvg` von conda-forge, deren `Library\bin` vor dem Lauf in den `PATH` nehmen. Ein Lauf dauert etwa
  40 Sekunden; bleibt er stehen, hängt ein `rsvg-convert`-Prozess (abbrechen und neu starten).
- In der Git Bash Windows-Pfade für Umgebungsvariablen mit `cygpath -w` umwandeln; im `PATH` die Form `/c/...` nutzen.
- Zeilenenden: `.gitattributes` erzwingt LF für SVG, XML, INI, MD, PY und LICENSE. Dateien immer mit `newline="\n"` schreiben.

## Git

- Branch **`master`** (nicht umbenennen, die README nennt ihn für Resource Sharing).
- Ein-Personen-Projekt: Arbeiten direkt auf `master` ist in Ordnung.
- Commit-Nachrichten nach Muster `typ: was und warum` auf Deutsch (`feat`, `fix`, `docs`, `chore`).
- Keine Dateien aus Chat-Downloads committen: Diese tragen einen C2PA-Herkunftsnachweis (`xmlns:c2pa`,
  `<metadata><c2pa:manifest>`). Stattdessen mit dem Generator neu erzeugen. Prüfen mit `grep -rl c2pa collections`.
- Öffentlich schalten (erst nach Rücksprache):
  `gh repo edit GIS-Akademie/qgis-symbole --visibility public --accept-visibility-change-consequences`
