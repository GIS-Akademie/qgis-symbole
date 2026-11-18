# GIS-Akademie Symbolbibliothek für QGIS

1025 Punktsymbole (SVG) sowie 498 Linien- und Flächensymbole in zwanzig Sammlungen, aufgebaut als Repository
für das QGIS-Plugin **Resource Sharing**. Alle Symbole sind Eigenentwicklungen der GIS-Akademie und stehen
unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).

| Sammlung | ID | Punkte | Linien | Flächen | Inhalt |
|---|---|---|---|---|---|
| PlanZV | `gisak_planzv` | 106 | 18 | 30 | Planzeichen für Bauleitpläne in Anlehnung an die Anlage zur PlanZV |
| Strom | `gisak_strom` | 51 | 14 | 7 | Stationen, Masten, Kabelgarnituren, Schaltzeichen, Leitungen nach Spannungsebene |
| Erneuerbare Energien | `gisak_eeg` | 43 | 10 | 14 | Wind- und Solarparkplanung, Bioenergie, Wasserkraft, Wärme, Netzanschluss |
| Naturschutz | `gisak_naturschutz` | 58 | 9 | 19 | Schutzgebiete, Arten und Fundpunkte, Kompensation, Erfassung |
| Landschaftsplanung | `gisak_landschaftsplanung` | 62 | 13 | 18 | Gehölze, Biotop- und Nutzungstypen, Maßnahmen, Erholung |
| Verkehr | `gisak_verkehr` | 58 | 16 | 10 | Parken, ÖPNV, Bahn, Rad- und Fußverkehr, Bauwerke, Störungen, Straßen nach Klasse |
| Wasserwirtschaft | `gisak_wasser` | 59 | 14 | 13 | Messstellen, Anlagen, Armaturen, Kanalnetz, Gewässerbauwerke, Gebiete |
| Vermessung | `gisak_vermessung` | 49 | 16 | 11 | Grenz- und Festpunkte, Aufschlüsse, Grenzen, Gebäude, Topografie im Lageplan |
| Raumordnung und Regionalplanung | `gisak_raumordnung` | 40 | 14 | 27 | Zentrale Orte, Standorte, Infrastruktur, Vorrang- und Vorbehaltsgebiete |
| Gas, Fernwärme, Telekommunikation | `gisak_leitungen` | 43 | 14 | 11 | Stationen, Armaturen und Netzelemente der drei Sparten, Leitungen nach Druckstufe und Art |
| Boden, Altlasten und Geologie | `gisak_boden` | 44 | 11 | 14 | Aufschlüsse, Altlasten, Bodenschutz, Rohstoffe, Bodenarten als Signatur |
| Lärm und Immissionen | `gisak_laerm` | 38 | 11 | 13 | Immissionsorte, Quellen, Schutzmaßnahmen, Pegelklassen der Lärmkartierung |
| Forst | `gisak_forst` | 45 | 11 | 14 | Baumarten und Bestand, Betrieb, Jagd, Waldfunktionen, Altersklassen |
| Landwirtschaft | `gisak_landwirtschaft` | 45 | 11 | 14 | Betrieb und Ställe, Kulturen, Technik und Wasser, Schutz- und Förderkulissen |
| Tourismus und Freizeit | `gisak_tourismus` | 45 | 14 | 10 | Unterkunft und Service, Wandern und Rad, Wasser und Winter, Sehenswertes, Wegearten |
| Denkmalpflege und Archäologie | `gisak_denkmal` | 45 | 9 | 10 | Baudenkmale, Bodendenkmale und Fundstellen, Status, Erinnerung |
| Brand- und Katastrophenschutz | `gisak_brandschutz` | 42 | 10 | 10 | Feuerwehr und Löschwasser, Rettung, Katastrophenschutz, Gefahrenstellen |
| Nordpfeile | `gisak_nordpfeile` | 34 | – | – | Schlichte Nordpfeile für Karten und Drucklayouts |
| Kartengestaltung | `gisak_layout` | 61 | 9 | 10 | Nummern 1–20 und Buchstaben A–L als Marker, Hinweiszeichen, Pfeile, Rahmen und Ausschnitte |
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

**Fehler nach einer Aktualisierung des Repositorys:** Meldet das Plugin beim Installieren nur
`Error: (b'…', b'…')` mit zwei Prüfsummen, kann es seinen lokalen Klon nicht auf den neuen Stand bringen
(es klont nur den letzten Stand und scheitert dann am Nachziehen). Abhilfe: QGIS schließen, den Ordner
`resource_sharing/repositories/github.com/GIS-Akademie/qgis-symbole` im QGIS-Profilordner löschen
(**Einstellungen › Benutzerprofile › Aktuellen Profilordner öffnen**) und die Sammlung erneut installieren.

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
| Raumordnung | Verwaltungs- und Regionsgrenzen, Entwicklungsachsen, Straße und Schiene (Bestand, Planung), Trassenkorridor, Grünzäsur | Vorrang- und Vorbehaltsgebiete je Thema, Grünzug, Verdichtungsraum, Eignungs- und Ausschlussgebiet |
| Gas, Fernwärme, Telekommunikation | Gas nach Druckstufe, Fernwärme Vor- und Rücklauf, Glasfaser, Kupfer, Leerrohr, Richtfunk | Schutzstreifen, Versorgungs- und Ausbaugebiete, Betriebsgelände |
| Boden | Störung, Schichtgrenze, Abbau- und Rutschungskante, Altlastengrenze | Altlasten nach Status, Abbau, Schutzflächen, Bodenarten |
| Lärm | Lärmschutzwand und -wall, Isophonen, Emissionsbänder | Pegelklassen in den Farben der DIN 45682, Schutzzonen, ruhiges Gebiet |
| Forst | Wege nach Ausbau, Abteilungs- und Reviergrenzen, Zaun, Waldrand | Baumartengruppen, Altersklassen, Waldfunktionen, Kalamität |
| Landwirtschaft | Schlag- und Feldblockgrenze, Wege, Dränage, Beregnung, Weidezaun | Nutzungen und Kulturen, Förder- und Gebietskulissen |
| Tourismus | Wander-, Rad- und Reitwege nach Art, Loipe, Piste, Lift, Kanuroute | Erholungs-, Kur- und Skigebiet, Badezone, Wildruhezone |
| Denkmalpflege | Grenzen von Denkmalbereich und Grabungsschutzgebiet, Wall- und Mauerverlauf, Altstraße | Baudenkmal, Ensemble, Bodendenkmal, Grabungs- und Verdachtsfläche, Pufferzone |
| Brand- und Katastrophenschutz | Feuerwehrzufahrt, Rettungsweg, Evakuierungsroute, Löschwasser- und Schlauchleitung, Absperrung | Aufstell- und Bewegungsfläche, Brandabschnitt, Gefahren- und Absperrbereich, Evakuierungszone |
| Kartengestaltung | Schnittlinie, Blattschnitt, Hinweis-, Pfeil- und Maßlinie, Hervorhebung | Kartenrahmen, Detail- und Übersichtsausschnitt, Legendenkasten, Abdeckung |
| Allgemein | Verwaltungsgrenzen, Projektgrenze, Route, Rettungsweg | Gebäude, Untersuchungs- und Projektgebiet, Gefahren- und Hinweisfläche |

**Innen und außen:** Bei Flächen mit Randzeichen (z. B. Umgrenzungen der PlanZV) stehen die Zeichen immer auf
der Innenseite, unabhängig von der Digitalisierrichtung. Bei Linien mit einseitigen Zeichen oder Farbbändern
(z. B. Baugrenze farbig, Böschung, Deich) liegen diese in Digitalisierrichtung rechts; zum Wechseln der Seite
die Linie umdrehen.

**Ecken bleiben frei:** Bei den Umgrenzungen mit Randzeichen prüft das Symbol die Geometrie beim Zeichnen: Der
Umriss wird zuerst um bis zu 0,5 mm geglättet, dann an jedem Knick über 55° aufgetrennt, und die Zeichen werden auf jeder Kante mittig verteilt, mit
Abstand zu den Ecken. Kurze Kanten bekommen ein einzelnes Zeichen in der Mitte, sehr kurze bleiben leer; an Bögen aus vielen kurzen
Stücken laufen die Zeichen durch. Dafür nutzt das Symbol einen Geometriegenerator in Millimetern (ab QGIS 3.24),
das Ergebnis hängt also vom Kartenmaßstab ab und passt sich beim Zoomen an. Schwellenwinkel und Eckenabstand
stehen im Ausdruck des Geometriegenerators und lassen sich dort ändern.

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
| Raumordnung | schwarz-weiß, Flächen farbig | konzentrische Kreise = Zentraler Ort (Rang über Ringe und Füllung), Quadrat = Standort, Kreis = Infrastruktur, Raute = Freiraum, kleines Quadrat mit Buchstabe = Kategorie (Z, G, N, V); Vorranggebiet durchgezogen und dicht, Vorbehaltsgebiet gestrichelt und weit schraffiert | § 7 ROG, Zentrale-Orte-System, NLT-Arbeitshilfe Planzeichen in der Regionalplanung (Niedersachsen 2024), Anlage 3 LPlG-DVO NRW |
| Gas, Fernwärme, Telekommunikation | Farbe je Sparte | gelb = Gas, orangerot = Fernwärme, grün = Telekommunikation; Quadrat = Station, Kreis = Messstelle oder Einrichtung, ohne Rahmen = Armatur auf der Leitung | Rohrnetzpläne nach DIN 2425, übliche Spartenfarben der Leitungsauskunft |
| Boden | braun | Kreis = Aufschluss oder Messstelle, Quadrat = Altlast oder Standort, Raute = Bodenschutz, Sechseck = Geologie und Rohstoffe | DIN 4023, Bodenkundliche Kartieranleitung, Altlastenkataster der Länder |
| Lärm | violett | Kreis = Immissionsort oder Messung, Quadrat = Quelle, Raute = Schutzmaßnahme, Sechseck = schutzbedürftige Nutzung, ohne Rahmen = Hilfszeichen der Schallausbreitung | 34. BImSchV, DIN 45682, DIN 18005, TA Lärm |
| Forst | dunkelgrün | Baumkrone ohne Rahmen = Baumart oder Bestand, Quadrat = betriebliche Einrichtung, Kreis = Jagd und Wild, Raute = Waldfunktion oder Schutz | Forstbetriebskarten der Länder, Waldfunktionenkartierung |
| Landwirtschaft | ocker | Quadrat = Betrieb und Gebäude, Kreis = Kultur oder Nutzung, Sechseck = Technik und Wasser, Raute = Schutz, Förderung, Gebietskulisse | Kulturartengruppen des Agrarantrags (InVeKoS), Feldblockkataster |
| Tourismus | weißes Sinnbild auf farbigem Quadrat | grau = Unterkunft und Service, grün = Wandern, Rad und Natur, blau = Wasser und Winter, braun = Sehenswertes und Erlebnis | touristische Hinweiszeichen der StVO, amtliche Wander- und Freizeitkarten |
| Denkmalpflege | ziegelrot | Quadrat = Baudenkmal, Kreis = Bodendenkmal oder Fundstelle, Raute = Status oder Schutz, Sechseck = Erinnerung und Vermittlung; gestrichelt = vermutet oder abgegangen | Denkmalkartierungen der Landesämter, archäologische Fundstellenkarten |
| Brand- und Katastrophenschutz | weißes Sinnbild auf farbigem Quadrat | rot = Feuerwehr und Brandschutz, grün = Rettung und Flucht, blau = Katastrophenschutz, gelbes Dreieck = Gefahrenstelle | DIN 14095, DIN 14034, ISO 7010, taktische Zeichen |
| Kartengestaltung | schwarz-weiß | Kreis = Nummer, Quadrat = Buchstabe, Raute = Hinweiszeichen, ohne Rahmen = Pfeil oder Marke; rot = Hervorhebung | übliche Verweiszeichen in Plänen |
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
  Aufschüttungen und Abgrabungen und der Einfahrtbereich. Die Umgrenzung von Schutzgebieten (Nr. 13.3) zeigt die
  Anlage mit innen geschlossenen Strichgruppen und lässt „Differenzierungen in der Umgrenzungssignatur“ zur
  Unterscheidung der Schutzgebiete zu, ohne sie festzulegen. Als Flächensymbol gibt es ein Paar für
  aneinandergrenzende Schutzgebiete, wie es in Plänen verbreitet ist: „Naturschutzgebiet“ mit geschlossenen und
  „Landschaftsschutzgebiet“ mit offenen Strichgruppen (`um_schutzgebiet_offen`), jeweils auf der Innenseite. Beide
  nutzen dasselbe Raster, das zweite ist um ein halbes Raster versetzt. Der Abstand der Zeichen hängt vom
  Kartenmaßstab ab: 8 mm ab 1:20000, ansteigend bis 13 mm bei 1:1000 und größer; an einer gemeinsamen Grenze stehen die
  Zeichen der beiden Flächen dadurch beiderseits der Linie auf Lücke. Welche Schutzgebietsart welche Variante
  erhält, legt die Zeichenerklärung des Plans fest. `TGa` ist eine gebräuchliche Ergänzung und steht
  nicht in der Anlage.
- **Übrige Sammlungen:** Für Strom, Erneuerbare Energien, Naturschutz, Landschaftsplanung, Verkehr, Wasser,
  Vermessung und Allgemein gibt es kein bundeseinheitliches Regelwerk für Punktsymbole. Die Zeichen orientieren
  sich an den oben genannten Normen, Karten und Konventionen, sind aber eigene Entwürfe und keine normgerechten
  Wiedergaben.
- **Brand- und Katastrophenschutz:** Die Zeichen sind eigene Sinnbilder und keine Normzeichen. Für Feuerwehrpläne
  nach DIN 14095 und für die Sicherheitskennzeichnung gelten die genormten Zeichen. Löschwasser ist hier rot
  (Gruppe Feuerwehr), in Feuerwehrplänen üblicherweise blau.
- **Lärm:** Die Farben der Pegelklassen sind der Farbtabelle der DIN 45682 in den LAI-Hinweisen zur Lärmkartierung
  (Fassung 08.08.2025) entnommen; die Norm selbst lag nicht vor.
- **Raumordnung:** Die Planzeichen für Regionalpläne unterscheiden sich je Land. Die Flächenfarben folgen
  überwiegend der niedersächsischen Arbeitshilfe, die Farbwerte sind aus deren Richtwerten abgeleitet.
- **Boden:** Die Signaturen der Bodenarten folgen der gängigen Praxis nach DIN 4023, nicht dem Normtext.
- **Linien- und Flächensymbole** sind in Millimetern bemessen und in QGIS 3.44 und 4.2 geprüft. Die Vorschaubilder
  zeigen eine Nachbildung; Punktmuster und Schraffuren können in QGIS leicht versetzt beginnen.
- Marken- und Unternehmenslogos wurden bewusst nicht nachgebildet.

## Lizenz

© 2026 GIS-Akademie, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).
Bei Weitergabe bitte „GIS-Akademie“ als Urheber nennen.
