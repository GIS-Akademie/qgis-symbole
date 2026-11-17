# GIS-Akademie Symbolbibliothek für QGIS

542 SVG-Symbole in neun Sammlungen, aufgebaut als Repository für das QGIS-Plugin
**Resource Sharing**. Alle Symbole sind Eigenentwicklungen der GIS-Akademie und stehen
unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).

| Sammlung | ID | Symbole | Inhalt |
|---|---|---|---|
| PlanZV | `gisak_planzv` | 105 | Planzeichen für Bauleitpläne in Anlehnung an die Anlage zur PlanZV |
| Strom | `gisak_strom` | 51 | Stationen, Masten, Kabelgarnituren, Schaltzeichen |
| Erneuerbare Energien | `gisak_eeg` | 43 | Wind- und Solarparkplanung, Bioenergie, Wasserkraft, Wärme, Netzanschluss |
| Naturschutz | `gisak_naturschutz` | 58 | Schutzgebiete, Arten und Fundpunkte, Kompensation, Erfassung |
| Landschaftsplanung | `gisak_landschaftsplanung` | 62 | Gehölze, Biotop- und Nutzungstypen, Maßnahmen, Erholung |
| Verkehr | `gisak_verkehr` | 58 | Parken, ÖPNV, Bahn, Rad- und Fußverkehr, Bauwerke, Störungen |
| Wasserwirtschaft | `gisak_wasser` | 59 | Messstellen, Anlagen, Armaturen, Kanalnetz, Gewässerbauwerke, Gebiete |
| Vermessung | `gisak_vermessung` | 49 | Grenz- und Festpunkte, Aufschlüsse, Nordpfeile, Topografie im Lageplan |
| Allgemein | `gisak_allgemein` | 57 | Öffentliche Einrichtungen, Rettung, Kultur, topografische Einzelobjekte, Freizeit |

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

Die Symbole haben bis zu zwei in QGIS änderbare Farben mit fachüblicher Voreinstellung:

- **Füllfarbe** – Flächen und Hintergründe
- **Strichfarbe** – Konturen und dunkle Zeichen

Reine Strich- und Buchstabenzeichen (z. B. `WA`, Schaltzeichen, Linienelemente) haben nur die Strichfarbe.
Weiße Details (z. B. die Sinnbilder der Verkehrssymbole) sind fest. Die Strichstärken sind bewusst
nicht parametrisiert, damit das Erscheinungsbild einheitlich bleibt; die Symbole skalieren über die Größe.

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
| Allgemein | dunkles Sinnbild auf weißem Quadrat | grau = allgemein, rot = Gesundheit und Rettung, blau = Sicherheit und Dienste | Objektarten amtlicher topografischer Karten und Stadtpläne |

**Linienelemente:** Einige Zeichen sind für Markierungslinien gedacht (PlanZV-Präfixe `um_` und `lt_`,
Armaturen in Strom und Wasser, `topo_boeschung`). Bei ihnen verläuft die Linie waagerecht durch die
Symbolmitte; bei den Umgrenzungen der PlanZV zeigt die Innenseite nach unten. In QGIS als Markierungslinie
mit festem Abstand und „Markierung drehen“ verwenden.

## Aufbau

```
metadata.ini                      Beschreibung des Repositorys und der Sammlungen
collections/<ID>/svg/             SVG-Dateien, Schema gisak_<sammlung>_<name>.svg
collections/<ID>/preview/         Vorschaubild für das Plugin
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

```powershell
python tools\vorschau.py wasser C:\Temp\wasser.png    # Kontrollbild einer Sammlung mit Symbolnamen
python tools\mkrepo.py .                              # alles neu erzeugen
```

`mkrepo.py .` erzeugt im Repository alle SVGs, Vorschauen, `metadata.ini`, `LICENSE` und den Katalog neu,
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
  Lage- und Flächenzeichen sowie Elemente für Umgrenzungslinien. Flächenfarben, Flächenmuster und die
  Linienarten selbst (Baulinie, Baugrenze, Bahnanlagen usw.) werden in QGIS als Füll- bzw. Linienstil angelegt
  und sind nicht Teil dieser Bibliothek. `TGa` ist eine gebräuchliche Ergänzung und steht nicht in der Anlage.
- **Übrige Sammlungen:** Für Strom, Erneuerbare Energien, Naturschutz, Landschaftsplanung, Verkehr, Wasser,
  Vermessung und Allgemein gibt es kein bundeseinheitliches Regelwerk für Punktsymbole. Die Zeichen orientieren
  sich an den oben genannten Normen, Karten und Konventionen, sind aber eigene Entwürfe und keine normgerechten
  Wiedergaben.
- Marken- und Unternehmenslogos wurden bewusst nicht nachgebildet.

## Lizenz

© 2026 GIS-Akademie, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).
Bei Weitergabe bitte „GIS-Akademie“ als Urheber nennen.
