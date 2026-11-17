# GIS-Akademie Symbolbibliothek für QGIS

576 Punktsymbole (SVG) sowie 250 Linien- und Flächensymbole in zehn Sammlungen, aufgebaut als Repository
für das QGIS-Plugin **Resource Sharing**. Alle Symbole sind Eigenentwicklungen der GIS-Akademie und stehen
unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).

| Sammlung | ID | Punkte | Linien | Flächen | Inhalt |
|---|---|---|---|---|---|
| PlanZV | `gisak_planzv` | 105 | 18 | 29 | Planzeichen für Bauleitpläne in Anlehnung an die Anlage zur PlanZV |
| Strom | `gisak_strom` | 51 | 14 | 7 | Stationen, Masten, Kabelgarnituren, Schaltzeichen, Leitungen nach Spannungsebene |
| Erneuerbare Energien | `gisak_eeg` | 43 | 10 | 14 | Wind- und Solarparkplanung, Bioenergie, Wasserkraft, Wärme, Netzanschluss |
| Naturschutz | `gisak_naturschutz` | 58 | 9 | 19 | Schutzgebiete, Arten und Fundpunkte, Kompensation, Erfassung |
| Landschaftsplanung | `gisak_landschaftsplanung` | 62 | 13 | 18 | Gehölze, Biotop- und Nutzungstypen, Maßnahmen, Erholung |
| Verkehr | `gisak_verkehr` | 58 | 16 | 10 | Parken, ÖPNV, Bahn, Rad- und Fußverkehr, Bauwerke, Störungen, Straßen nach Klasse |
| Wasserwirtschaft | `gisak_wasser` | 59 | 14 | 13 | Messstellen, Anlagen, Armaturen, Kanalnetz, Gewässerbauwerke, Gebiete |
| Vermessung | `gisak_vermessung` | 49 | 16 | 11 | Grenz- und Festpunkte, Aufschlüsse, Grenzen, Gebäude, Topografie im Lageplan |
| Nordpfeile | `gisak_nordpfeile` | 34 | – | – | Schlichte Nordpfeile für Karten und Drucklayouts |
| Allgemein | `gisak_allgemein` | 57 | 10 | 9 | Öffentliche Einrichtungen, Rettung, Kultur, topografische Einzelobjekte, Grenzen |

Die vollständige Liste aller Symbole mit Bedeutung steht in [KATALOG.md](KATALOG.md).
Jede Sammlung enthält unter `preview/` eine Übersicht der Punktsymbole (`preview.png`) und der Linien- und
Flächensymbole (`linien_flaechen.png`).

## Einbinden in QGIS

1. Plugin **QGIS Resource Sharing** installieren.
2. Im Plugin unter **Settings › Add repository…** die URL eintragen:
   - Git: `https://github.com/GIS-Akademie/qgis-symbole.git` (Repository muss öffentlich sein, Branch `master`)
   - Netzlaufwerk: `file://G:/Pfad/zum/Repository`
3. Unter **All collections** die gewünschten Sammlungen installieren.
4. Die Punktsymbole erscheinen im Symboleditor bei **SVG-Markierung** unter den SVG-Gruppen (**User Symbols**).
5. Die Linien- und Flächensymbole stehen in der Symbolauswahl und in der **Stilverwaltung**. Dort tragen sie
   das Schlagwort `<Name der Sammlung> (<Name des Repositorys>)/Linien_und_Flaechen`, der Symbolname beginnt mit
   der Sammlung, z. B. `PlanZV: Baugrenze`.
6. Nordpfeile im Drucklayout: **Element hinzufügen › Nordpfeil hinzufügen**, dann in den Elementeigenschaften
   unter den SVG-Gruppen einen Nordpfeil der Sammlung wählen.

Ohne das Plugin lässt sich die Stildatei `collections/<ID>/symbol/Linien_und_Flaechen.xml` auch in der
Stilverwaltung über **Importieren** laden. Damit die wenigen Symbole mit SVG-Markierungen (Umgrenzungen der
PlanZV, Böschung) ihre Zeichen finden, vorher den Ordner `collections/<ID>/svg` unter
**Einstellungen › Optionen › System › SVG-Pfade** eintragen.

## Farben ändern

Die Symbole haben bis zu zwei in QGIS änderbare Farben mit fachüblicher Voreinstellung:

- **Füllfarbe** – Flächen und Hintergründe
- **Strichfarbe** – Konturen und dunkle Zeichen

Reine Strich- und Buchstabenzeichen (z. B. `WA`, Schaltzeichen, Linienelemente) haben nur die Strichfarbe.
Weiße Details (z. B. die Sinnbilder der Verkehrssymbole) sind fest. Die Strichstärken sind bewusst
nicht parametrisiert, damit das Erscheinungsbild einheitlich bleibt; die Symbole skalieren über die Größe.

## Linien- und Flächensymbole

Neben den Punktsymbolen bringt jede Fachsammlung fertige Linien- und Flächensymbole mit, in denselben Farben
wie die Punktsymbole. Sie sind normale QGIS-Symbole aus einfachen Linien, Markierungslinien, Füllungen,
Schraffuren und Punktmustern und lassen sich im Symboleditor beliebig anpassen. Alle Maße sind in Millimetern
angelegt, die Symbole sind also für den Druckmaßstab gedacht.

| Sammlung | Linien | Flächen |
|---|---|---|
| PlanZV | Baulinie, Baugrenze und Straßenbegrenzungslinie (schwarz-weiß und farbig), Perlschnur, Geltungsbereich, Leitungen, Straßenbahn, Seilbahn, Stützmauer | Bauflächen in den Farben der Anlage (Rot mittel, Braun mittel, Goldocker …), Umgrenzungen mit den Zeichen der Anlage auf der Innenseite |
| Strom | Freileitungen und Kabel nach Spannungsebene, Schutzrohr, geplant, außer Betrieb | Schutzstreifen, Trassenkorridor, Betriebsgelände, Netzgebiet |
| Erneuerbare Energien | Kabeltrasse, Zuwegung, Zaun, Abstandslinie, Wärme- und Biogasleitung | Vorrang- und Potenzialflächen, Wind- und Solarpark, Modulfläche, Ausschluss- und Abstandsflächen |
| Naturschutz | Schutzgebiets- und Zonengrenze, Biotopverbund, Wildtierkorridor, Schutzzaun, Transekt | Schutzgebietskategorien, Natura 2000, Zonen, Kompensations- und Ökokontoflächen |
| Landschaftsplanung | Hecke, Baumreihe, Allee, Ufergehölz, Gewässer, Wege, Sichtachse, Kaltluftbahn | Wald, Grünland, Acker, Feuchtbiotope, Gewässer, Maßnahmenflächen |
| Verkehr | Straßen nach Klasse, Rad- und Fußweg, Bahn, Bus, Fähre, Baustelle, Umleitung, Sperrung | Park- und Verkehrsflächen, Zonen, Baustellen- und Sperrbereich |
| Wasserwirtschaft | Trinkwasserleitungen, Schmutz-, Regen- und Mischwasserkanal mit Fließrichtung, Gewässer, Deich | Schutzgebietszonen, Überschwemmungs- und Risikogebiet, Einzugs- und Entwässerungsgebiete |
| Vermessung | Flurstücks-, Flur-, Gemarkungs- und Gemeindegrenze, Höhenlinien, Böschung, Zaun, Mauer, Hecke | Flurstück, Gebäude nach Art, geplant, abgebrochen, befestigte Fläche |
| Allgemein | Verwaltungsgrenzen, Projektgrenze, Route, Rettungsweg | Gebäude, Untersuchungs- und Projektgebiet, Gefahren- und Hinweisfläche |

**Innen und außen:** Bei Flächen mit Randzeichen (z. B. Umgrenzungen der PlanZV) stehen die Zeichen immer auf
der Innenseite, unabhängig von der Digitalisierrichtung. Bei Linien mit einseitigen Zeichen oder Farbbändern
(z. B. Baugrenze farbig, Böschung, Deich) liegen diese in Digitalisierrichtung rechts; zum Wechseln der Seite
die Linie umdrehen.

## Stil und Vorbilder je Sammlung

Jede Sammlung hat einen einheitlichen Stil. Innerhalb einer Sammlung zeigt die Rahmenform oder die Farbe,
zu welcher Gruppe ein Symbol gehört.

| Sammlung | Stil | Bedeutung von Form und Farbe | Orientierung |
|---|---|---|---|
| PlanZV | schwarz-weiß | liegendes Rechteck = Flächenzeichen, Kreis = Lagezeichen, Buchstaben ohne Rahmen | Anlage zur PlanZV (Stand 2025), Schwarz-Weiß-Fassung |
| Strom | rot auf weiß | Quadrat = Station, Draufsicht = Mast, ohne Rahmen = Garnitur oder Schaltzeichen auf der Leitung | Legenden von Netzbetreibern, Schaltzeichen nach DIN EN 60617 |
| Erneuerbare Energien | Kreis mit Piktogramm | Farbe = Energieträger, Rahmen = Status (durchgezogen Bestand, gestrichelt geplant, gepunktet beantragt, doppelt genehmigt) | Energieatlanten der Länder |
| Naturschutz | grün | Quadrat = Schutzgebiet, Kreis = Art oder Lebensstätte, Raute = Maßnahme, Sechseck = Einrichtung oder Erfassung | Schutzkategorien des BNatSchG, Status der Brutvogelkartierung, Eingriffsregelung |
| Landschaftsplanung | grün, Wasser blau | Draufsicht = Gehölz, Quadrat = Biotop- oder Nutzungstyp, gestricheltes Quadrat = Maßnahme, Kreis = Erholung | Bestands- und Maßnahmenpläne der Landschaftsplanung |
| Verkehr | weißes Sinnbild auf farbigem Quadrat | blau = Anlage oder Angebot, orange = Baustelle und Störung, rot = Sperrung und Beschränkung | Hinweiszeichen der StVO, amtliche Stadt- und Verkehrskarten |
| Wasserwirtschaft | blau | Kreis = Messstelle, Quadrat = Anlage oder Bauwerk, Raute = Gebiet, ohne Rahmen = Armatur auf der Leitung | Leitungs- und Kanalnetzpläne (DIN 2425), übliche Kurzzeichen |
| Vermessung | schwarz-weiß | geometrische Grundformen ohne Rahmen | Liegenschaftskarte, Vermessungsriss (DIN 18702), Aufschlüsse nach DIN 4023 |
| Nordpfeile | schwarz-weiß, ohne Rahmen | Präfix = Bauart: `pfeil_` mit Schaft, `nadel_` ohne Schaft, `kreis_` im Kreis, `rose_` Windrose; das N steht über der Spitze, `_ohne_n` = ohne Buchstabe | Nordpfeile amtlicher Karten, Lagepläne und Bauleitpläne |
| Allgemein | dunkles Sinnbild auf weißem Quadrat | grau = allgemein, rot = Gesundheit und Rettung, blau = Sicherheit und Dienste | Objektarten amtlicher topografischer Karten und Stadtpläne |

**Farben der Leitungen in der Wasserwirtschaft:** Trinkwasser und Gebiete dunkelblau, Gewässer und Regenwasser
hellblau, Schmutzwasser braun, Mischwasser violett (übliche Farben in Kanalnetzplänen).

**Linienelemente:** Einige Punktsymbole sind für Markierungslinien gedacht (PlanZV-Präfixe `um_` und `lt_`,
Armaturen in Strom und Wasser, `topo_boeschung`). Bei ihnen verläuft die Linie waagerecht durch die
Symbolmitte; bei den Umgrenzungen der PlanZV zeigt die Innenseite nach unten. In QGIS als Markierungslinie
mit festem Abstand und „Markierung drehen“ verwenden. Für die Umgrenzungen der PlanZV und die Böschung gibt es
das bereits fertig als Linien- bzw. Flächensymbol.

## Aufbau

```
metadata.ini                      Beschreibung des Repositorys und der Sammlungen
collections/<ID>/svg/             SVG-Dateien, Schema gisak_<sammlung>_<name>.svg
collections/<ID>/symbol/          QGIS-Stildatei Linien_und_Flaechen.xml mit den Linien- und Flächensymbolen
collections/<ID>/preview/         Vorschaubilder für das Plugin
collections/<ID>/LICENSE          Lizenz der Sammlung
KATALOG.md                        Liste aller Symbole
tools/                            Generator (Python), aus dem alle SVGs erzeugt werden
```

Alle Symbole nutzen ein Raster von 100 × 100 Einheiten. Beschriftungen sind in Pfade umgewandelt,
es werden also keine Schriften auf dem Zielrechner benötigt. Die Dateinamen sind eindeutig und
sollten nach der Veröffentlichung nicht mehr geändert werden, weil Projekte darauf verweisen.

## Erweitern

Jede Sammlung hat eine eigene Datei `tools/sym_<sammlung>.py`. Ein Symbol ist dort ein Eintrag aus Name, Titel,
Füll- und Strichfarbe und einer Liste von Grundformen aus `tools/lib.py`. Am Anfang jeder Datei steht, welchen
Stil die Sammlung hat.

Linien- und Flächensymbole stehen in derselben Datei in den Listen `LINIEN` und `FLAECHEN`. Ein Eintrag besteht
aus dem Titel und einer Liste von Ebenen (`linie`, `marken`, `voll`, `schraffur`, `muster`, `band`), die in
`tools/qstil.py` beschrieben sind.

```powershell
python tools\vorschau.py wasser C:\Temp\wasser.png         # Kontrollbild der Punktsymbole mit Symbolnamen
python tools\vorschau_stil.py wasser C:\Temp\wasser_l.png  # Kontrollbild der Linien- und Flächensymbole
python tools\mkrepo.py .                                   # alles neu erzeugen
```

`mkrepo.py .` erzeugt im Repository alle SVGs, Stildateien, Vorschauen, `metadata.ini`, `LICENSE` und den Katalog neu,
`tools/` bleibt dabei unverändert. Mit einem anderen Zielordner (`python tools\mkrepo.py C:\Temp\neu`) entsteht
dort ein vollständiges Repository samt `tools/`. Vorher committen: `collections/` wird vor dem Neuerzeugen
gelöscht, mit `git diff` sieht man danach, was sich geändert hat.

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
  Vorlagen. Vor dem Einsatz in rechtsverbindlichen Plänen bitte gegen die Anlage prüfen. Enthalten sind die
  Lage- und Flächenzeichen, Elemente für Umgrenzungslinien sowie Linienarten, Flächenfarben und Umgrenzungen
  als Linien- und Flächensymbole. Die Anlage nennt die Farben nur mit Namen („Rot mittel“, „Goldocker“); die
  Farbwerte sind danach gewählt und nicht verbindlich. Nicht enthalten sind unter anderem die Flächen für
  Aufschüttungen und Abgrabungen und der Einfahrtbereich. `TGa` ist eine gebräuchliche Ergänzung und steht
  nicht in der Anlage.
- **Übrige Sammlungen:** Für Strom, Erneuerbare Energien, Naturschutz, Landschaftsplanung, Verkehr, Wasser,
  Vermessung und Allgemein gibt es kein bundeseinheitliches Regelwerk für Punktsymbole. Die Zeichen orientieren
  sich an den oben genannten Normen, Karten und Konventionen, sind aber eigene Entwürfe und keine normgerechten
  Wiedergaben.
- **Linien- und Flächensymbole** sind in Millimetern bemessen und in QGIS 3.44 und 4.2 geprüft. Die Vorschaubilder
  zeigen eine Nachbildung; Punktmuster und Schraffuren können in QGIS leicht versetzt beginnen.
- Marken- und Unternehmenslogos wurden bewusst nicht nachgebildet.

## Lizenz

© 2026 GIS-Akademie, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).
Bei Weitergabe bitte „GIS-Akademie“ als Urheber nennen.
