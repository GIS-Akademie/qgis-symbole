# GIS-Akademie Symbolbibliothek für QGIS

211 SVG-Symbole in neun Sammlungen, aufgebaut als Repository für das QGIS-Plugin
**Resource Sharing**. Alle Symbole sind Eigenentwicklungen der GIS-Akademie und stehen
unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).

| Sammlung | ID | Symbole | Inhalt |
|---|---|---|---|
| PlanZV | `gisak_planzv` | 42 | Planzeichen für Bauleitpläne in Anlehnung an die Anlage zur PlanZV |
| Strom | `gisak_strom` | 24 | Stromnetze und Leitungspläne |
| Erneuerbare Energien | `gisak_eeg` | 22 | Wind- und Solarparkplanung, weitere EEG-Anlagen |
| Naturschutz | `gisak_naturschutz` | 27 | Schutzgebiete, Artenschutz, Kompensation |
| Landschaftsplanung | `gisak_landschaftsplanung` | 22 | Gehölze, Gewässer, Erholung, Maßnahmen |
| Verkehr | `gisak_verkehr` | 26 | Parken, ÖPNV, Bahn, Bauwerke, Verkehrstechnik |
| Wasserwirtschaft | `gisak_wasser` | 17 | Messstellen, Anlagen, Armaturen, Schutzgebiete |
| Vermessung | `gisak_vermessung` | 12 | Grenz- und Festpunkte, Nordpfeil |
| Allgemein | `gisak_allgemein` | 19 | Öffentliche Einrichtungen, Orte von Interesse |

Die vollständige Liste aller Dateien mit Bedeutung steht in [KATALOG.md](KATALOG.md).
Jede Sammlung enthält unter `preview/preview.png` eine Übersicht.

## Einbinden in QGIS

1. Plugin **QGIS Resource Sharing** installieren.
2. Im Plugin unter **Settings › Add repository…** die URL eintragen:
   - Git: `https://github.com/GIS-Akademie/qgis-symbole.git` (Repository muss öffentlich sein, Branch `master`)
   - Netzlaufwerk: `file://G:/Pfad/zum/Repository`
3. Unter **All collections** die gewünschten Sammlungen installieren.
4. Die Symbole erscheinen im Symboleditor bei **SVG-Markierung** unter den SVG-Gruppen (**User Symbols**).

## Farben ändern

Jedes Symbol hat zwei in QGIS änderbare Farben mit fachüblicher Voreinstellung:

- **Füllfarbe** – Flächen und Hintergründe
- **Strichfarbe** – Konturen und dunkle Zeichen

Weiße Details (z. B. die Zeichen der Verkehrssymbole) sind fest. Die Strichstärken sind bewusst
nicht parametrisiert, damit das Erscheinungsbild einheitlich bleibt; die Symbole skalieren über die Größe.

## Aufbau

```
metadata.ini                      Beschreibung des Repositorys und der Sammlungen
collections/<ID>/svg/             SVG-Dateien, Schema gisak_<kategorie>_<name>.svg
collections/<ID>/preview/         Vorschaubild für das Plugin
collections/<ID>/LICENSE          Lizenz der Sammlung
KATALOG.md                        Liste aller Symbole
tools/                            Generator (Python), aus dem alle SVGs erzeugt werden
```

Alle Symbole nutzen ein Raster von 100 × 100 Einheiten. Beschriftungen sind in Pfade umgewandelt,
es werden also keine Schriften auf dem Zielrechner benötigt. Die Dateinamen sind eindeutig und
sollten nach der Veröffentlichung nicht mehr geändert werden, weil Projekte darauf verweisen.

## Erweitern

Neue Symbole werden in `tools/sym_a.py` bzw. `tools/sym_b.py` als Liste von Grundformen ergänzt.
Danach im Repository-Ordner `python tools/mkrepo.py .` ausführen: Das erzeugt alle SVGs, Vorschauen,
`metadata.ini`, `LICENSE` und den Katalog neu, `tools/` bleibt dabei unverändert. Mit einem anderen
Zielordner (`python tools/mkrepo.py C:\Temp\neu`) entsteht dort ein vollständiges Repository samt `tools/`.
Vorher committen: `collections/` wird vor dem Neuerzeugen gelöscht, mit `git diff` sieht man danach, was sich geändert hat.
Benötigt werden Python 3 mit `fonttools`, `Pillow`, `lxml` (unter Windows z. B. die Python-Umgebung von
ArcGIS Pro), das Programm `rsvg-convert` für die Vorschaubilder und die Schrift **Liberation Sans**
([Download](https://github.com/liberationfonts/liberation-fonts/releases), SIL Open Font License).

Die Schrift wird automatisch in den üblichen Schriftordnern von Linux, Windows (auch „nur für mich
installiert“) und macOS gesucht. Liegt sie woanders, den Ordner mit den `.ttf`-Dateien angeben:

```powershell
$env:GISAK_FONT_DIR = "C:\Pfad\zu\liberation-fonts"
python tools\mkrepo.py .
```

Für die Symbole ist nur Liberation Sans Bold zulässig, damit die SVGs auf jedem Rechner identisch entstehen.
Für die Beschriftung der Vorschaubilder genügt notfalls Arial.

## Hinweise und Grenzen

- **PlanZV:** Die Zeichen sind Nachkonstruktionen anhand der Anlage zur Planzeichenverordnung, keine amtlichen
  Vorlagen. Vor dem Einsatz in rechtsverbindlichen Plänen bitte gegen die Anlage prüfen. Enthalten ist eine
  Auswahl der punktförmigen Zeichen; Liniensignaturen, Flächenfarben und Umgrenzungen sind nicht Teil dieser Version.
- **Übrige Kategorien:** Für Strom, EEG, Naturschutz, Landschaftsplanung, Verkehr, Wasser und Vermessung gibt es
  kein bundeseinheitliches Regelwerk für Punktsymbole. Die Zeichen folgen verbreiteten Konventionen
  (Schaltzeichen, Legenden von Netzbetreibern, Musterlegenden), sind aber eigene Entwürfe.
- Bei Verkehr wurden bewusst keine Marken- oder Unternehmenslogos nachgebildet.

## Lizenz

© 2026 GIS-Akademie, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).
Bei Weitergabe bitte „GIS-Akademie“ als Urheber nennen.
