# GIS-Akademie Symbolbibliothek für QGIS

1278 Punktsymbole (SVG) sowie 703 Linien- und Flächensymbole in 23 Sammlungen, aufgebaut als Repository
für das QGIS-Plugin **Resource Sharing**. Alle Symbole sind Eigenentwicklungen der GIS-Akademie und stehen
unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).

| Sammlung | ID | Punkte | Linien | Flächen | Inhalt |
|---|---|---|---|---|---|
| PlanZV | `gisak_planzv` | 106 | 18 | 30 | Planzeichen für Bauleitpläne in Anlehnung an die Anlage zur PlanZV |
| Strom | `gisak_strom` | 51 | 14 | 7 | Stationen, Masten, Kabelgarnituren, Schaltzeichen, Leitungen nach Spannungsebene |
| Erneuerbare Energien | `gisak_eeg` | 43 | 10 | 14 | Wind- und Solarparkplanung, Bioenergie, Wasserkraft, Wärme, Netzanschluss |
| Naturschutz | `gisak_naturschutz` | 58 | 9 | 19 | Schutzgebiete, Arten und Fundpunkte, Kompensation, Erfassung |
| Landschaftsplanung | `gisak_landschaftsplanung` | 82 | 14 | 21 | Gehölze, Baumkataster (Vitalität, Zustand, Baumpflege), Biotop- und Nutzungstypen, Maßnahmen, Erholung |
| Verkehr | `gisak_verkehr` | 58 | 16 | 10 | Parken, ÖPNV, Bahn, Rad- und Fußverkehr, Bauwerke, Störungen, Straßen nach Klasse |
| Wasserwirtschaft | `gisak_wasser` | 70 | 21 | 23 | Messstellen, Anlagen, Armaturen, Kanalnetz, Gewässerbauwerke, Gebiete, Starkregengefahren |
| Vermessung | `gisak_vermessung` | 49 | 16 | 11 | Grenz- und Festpunkte, Aufschlüsse, Grenzen, Gebäude, Topografie im Lageplan |
| Raumordnung und Regionalplanung | `gisak_raumordnung` | 40 | 14 | 27 | Zentrale Orte, Standorte, Infrastruktur, Vorrang- und Vorbehaltsgebiete |
| Realnutzung | `gisak_realnutzung` | 15 | 7 | 73 | Tatsächliche Nutzung nach AdV-Nutzungsartenkatalog: Siedlung, Verkehr, Vegetation, Gewässer; Vegetationszeichen |
| Gas, Fernwärme, Telekommunikation | `gisak_leitungen` | 43 | 14 | 11 | Stationen, Armaturen und Netzelemente der drei Sparten, Leitungen nach Druckstufe und Art |
| Wärmeplanung | `gisak_waermeplanung` | 42 | 16 | 45 | Erzeugungsanlagen, Wärmequellen und Potenziale, Speicher, Großverbraucher, dezentrale Wärmeerzeuger, Netze, Wärmedichten, Wärmeversorgungsgebiete und Eignungsstufen nach Wärmeplanungsgesetz |
| Boden, Altlasten und Geologie | `gisak_boden` | 44 | 11 | 14 | Aufschlüsse, Altlasten, Bodenschutz, Rohstoffe, Bodenarten als Signatur |
| Lärm und Immissionen | `gisak_laerm` | 38 | 11 | 13 | Immissionsorte, Quellen, Schutzmaßnahmen, Pegelklassen der Lärmkartierung |
| Stadtklima | `gisak_stadtklima` | 40 | 12 | 31 | Messstellen, Wärme- und Luftbelastung, Kaltluft- und Frischluftgebiete, Maßnahmen der Klimaanpassung, Strömungspfeile, Klimatope |
| Forst | `gisak_forst` | 45 | 11 | 14 | Baumarten und Bestand, Betrieb, Jagd, Waldfunktionen, Altersklassen |
| Landwirtschaft | `gisak_landwirtschaft` | 45 | 11 | 14 | Betrieb und Ställe, Kulturen, Technik und Wasser, Schutz- und Förderkulissen |
| Tourismus und Freizeit | `gisak_tourismus` | 90 | 14 | 10 | Unterkunft und Service, Wandern und Rad, Wasser und Winter, Sehenswertes, 45 Sportarten (darunter Boule), Wegearten |
| Denkmalpflege und Archäologie | `gisak_denkmal` | 45 | 9 | 10 | Baudenkmale, Bodendenkmale und Fundstellen, Status, Erinnerung |
| Brand- und Katastrophenschutz | `gisak_brandschutz` | 42 | 10 | 10 | Feuerwehr und Löschwasser, Rettung, Katastrophenschutz, Gefahrenstellen |
| Nordpfeile | `gisak_nordpfeile` | 34 | – | – | Schlichte Nordpfeile für Karten und Drucklayouts |
| Kartengestaltung | `gisak_layout` | 61 | 9 | 10 | Nummern 1–20 und Buchstaben A–L als Marker, Hinweiszeichen, Pfeile, Rahmen und Ausschnitte |
| Allgemein | `gisak_allgemein` | 137 | 10 | 9 | Öffentliche Einrichtungen, Rettung, Kultur, topografische Einzelzeichen, runde Punktmarker, freie Formen und Standortnadeln, Grenzen |

Die vollständige Liste aller Symbole mit Bedeutung steht in [KATALOG.md](KATALOG.md).
Jede Sammlung enthält unter `preview/` eine Übersicht der Punktsymbole (`preview.png`) und der Linien- und
Flächensymbole (`linien_flaechen.png`).

## Einbinden in QGIS

### Installieren

1. In QGIS das Plugin **QGIS Resource Sharing** installieren (**Erweiterungen › Erweiterungen verwalten und
   installieren**). Version 1.2.0 des Plugins läuft in QGIS 3.34 bis 3.x.
2. Im Plugin unter **Settings › Add repository…** einen Namen vergeben und die URL eintragen:
   - Git: `https://github.com/GIS-Akademie/qgis-symbole.git` (Branch `master`)
   - Netzlaufwerk: `file://G:/Pfad/zum/Repository`
3. Unter **All collections** die gewünschten Sammlungen auswählen und **Install** anklicken. Am besten bei
   leerem Projekt, nicht während ein Projekt mit vielen Layern geöffnet ist.

### Symbole finden

| Symbolart | Wo in QGIS | Name bzw. Gruppe |
|---|---|---|
| Punktsymbole | Symbolauswahl eines Punktlayers | `<Sammlung>: <Bezeichnung>`, z. B. `Tourismus und Freizeit: Bouleplatz / Boule / Pétanque` |
| Punktsymbole als SVG | Symboleditor › **SVG-Markierung** › SVG-Gruppen | Gruppe `GIS-Akademie Symbole <Sammlung>`, Datei `gisak_<sammlung>_<name>.svg` |
| Linien- und Flächensymbole | Symbolauswahl eines Linien- bzw. Flächenlayers | `<Sammlung>: <Bezeichnung>`, z. B. `PlanZV: Baugrenze` |
| Nordpfeile | Drucklayout › **Element hinzufügen › Nordpfeil hinzufügen** › SVG-Gruppen | Gruppe `GIS-Akademie Symbole Nordpfeile` |

- **Suchen:** Das Suchfeld der Symbolauswahl findet Symbole über Teile des Namens, z. B. `schutzgebiet`.
- **Filtern:** Jede Sammlung hat zwei Schlagworte, `…/Punkte` und `…/Linien_und_Flaechen`; in der
  **Stilverwaltung** lässt sich danach filtern.
- **Zusatz im Namen:** Das Plugin hängt an Symbolnamen, Schlagworte und SVG-Gruppen den Namen an, den man dem
  Repository in Schritt 2 gegeben hat, z. B. `PlanZV: Baugrenze (GIS-Akademie)`.
- **Zusatz `(Punkt)`:** Heißt ein Punktsymbol wie ein Linien- oder Flächensymbol derselben Sammlung, trägt es
  diesen Zusatz, z. B. `Naturschutz: Naturschutzgebiet (Punkt)`.
- **Vorgabegröße** der Punktsymbole ist 6 mm (Nordpfeile 12 mm); Größe und Farben lassen sich wie gewohnt ändern.

### Aktualisieren

Nach einer Aktualisierung der Bibliothek im Plugin **Reload repositories** wählen und die Sammlung unter
**Installed collections** mit **Reinstall** neu installieren. Layer in bestehenden Projekten behalten ihr
gespeichertes Symbol, bis man es neu aus der Auswahl zuweist.

**Fehler `Error: (b'…', b'…')` mit zwei Prüfsummen:** Das Plugin kann seinen lokalen Klon nicht auf den neuen
Stand bringen (es klont nur den letzten Stand und scheitert dann am Nachziehen). Abhilfe: QGIS schließen, den
Ordner `resource_sharing/repositories/github.com/GIS-Akademie/qgis-symbole` im QGIS-Profilordner löschen
(**Einstellungen › Benutzerprofile › Aktuellen Profilordner öffnen**) und die Sammlung erneut installieren.

### Als eigenes Plugin (ohne Resource Sharing und ohne Git)

Die Bibliothek gibt es auch als eigenes QGIS-Plugin **GIS-Akademie Symbole** (QGIS 3.34 bis 4.x). Es braucht
keine Git-Verbindung zu GitHub und eignet sich deshalb für Netze mit Proxy oder Firewall, in denen Resource
Sharing mit `Connection to github.com timed out` scheitert.

1. Das ZIP `gisak_symbole-<Version>.zip` von der Seite
   [Releases](https://github.com/GIS-Akademie/qgis-symbole/releases/latest) herunterladen und nicht entpacken.
   (Selbst bauen: `python tools\mkplugin.py`, das ZIP liegt danach unter `dist\`.)
2. In QGIS **Erweiterungen › Erweiterungen verwalten und installieren › Aus ZIP installieren** wählen.
3. Beim ersten Start erscheint die Liste der Sammlungen; angehakte werden in die Symbolauswahl eingetragen
   (alle 23 Sammlungen: etwa eine Viertelminute). Später erreichbar über **Erweiterungen › GIS-Akademie Symbole ›
   Sammlungen auswählen …**.

Die Symbole heißen wie oben, nur ohne den Klammerzusatz von Resource Sharing. Jede Sammlung hat genau ein
Schlagwort, ihren Namen (z. B. `Forst` oder `Erneuerbare Energien`); die Symbolauswahl zeigt darunter von selbst
nur die Symbole der passenden Art (Punkt, Linie oder Fläche). Die SVG-Dateien stehen in der SVG-Auswahl in der
Gruppe `symbole` nach Sammlung geordnet. Nach einem Update des Plugins werden
nur die Sammlungen neu eingetragen, deren Symbole sich geändert haben. Abgewählte Sammlungen verschwinden aus der
Symbolauswahl; vor dem Deinstallieren des Plugins am besten alle abwählen, sonst bleiben die Einträge ohne ihre
SVG-Dateien zurück. Wer die Sammlungen schon über Resource Sharing installiert hat, deinstalliert sie dort
zuerst, sonst stehen die Symbole doppelt in der Auswahl.

### Ohne das Plugin

Die Stildateien `collections/<ID>/symbol/Punkte.xml` und `Linien_und_Flaechen.xml` lassen sich in der
Stilverwaltung über **Importieren** laden. Damit die Symbole ihre SVG-Dateien finden, vorher den Ordner
`collections/<ID>/svg` unter **Einstellungen › Optionen › System › SVG-Pfade** eintragen.

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
| Landschaftsplanung | Hecke, Baumreihe, Allee, Ufergehölz, Gewässer, Wege, Sichtachse, Kaltluftbahn, Baumschutzzaun | Wald, Grünland, Acker, Feuchtbiotope, Gewässer, Maßnahmenflächen, Kronentrauf- und Wurzelschutzbereich |
| Verkehr | Straßen nach Klasse, Rad- und Fußweg, Bahn, Bus, Fähre, Baustelle, Umleitung, Sperrung | Park- und Verkehrsflächen, Zonen, Baustellen- und Sperrbereich |
| Wasserwirtschaft | Trinkwasserleitungen, Schmutz-, Regen- und Mischwasserkanal mit Fließrichtung, Gewässer, Deich, Starkregen: Fließgeschwindigkeit in vier Klassen, Fließweg, Notwasserweg | Schutzgebietszonen, Überschwemmungs- und Risikogebiet, Einzugs- und Entwässerungsgebiete, Starkregen: Überflutungstiefe in vier Klassen, Überflutungsausdehnung für drei Szenarien |
| Vermessung | Flurstücks-, Flur-, Gemarkungs- und Gemeindegrenze, Höhenlinien, Böschung, Zaun, Mauer, Hecke | Flurstück, Gebäude nach Art, geplant, abgebrochen, befestigte Fläche |
| Raumordnung | Verwaltungs- und Regionsgrenzen, Entwicklungsachsen, Straße und Schiene (Bestand, Planung), Trassenkorridor, Grünzäsur | Vorrang- und Vorbehaltsgebiete je Thema, Grünzug, Verdichtungsraum, Eignungs- und Ausschlussgebiet |
| Realnutzung | Grenzen von Nutzungsart, Gruppe, Bereich und Kartiereinheit, Baumreihen | 26 Nutzungsartengruppen und die Arten von Landwirtschaft und Wald mit Schlüssel, je in Katasterfarbe und kräftig |
| Gas, Fernwärme, Telekommunikation | Gas nach Druckstufe, Fernwärme Vor- und Rücklauf, Glasfaser, Kupfer, Leerrohr, Richtfunk | Schutzstreifen, Versorgungs- und Ausbaugebiete, Betriebsgelände |
| Wärmeplanung | Wärmeliniendichte in vier Klassen, Wärme-, Gas- und Wasserstoffnetz (Bestand, genehmigt, geplant), Abwassersammler, Grenzen des beplanten Gebiets | Wärmenetz-, Wasserstoffnetz-, dezentrales und Prüfgebiet, Eignungsstufen je Versorgungsart, Wärmedichte in fünf Klassen, überwiegender Energieträger, Potenzialflächen, Ausschlussgebiet |
| Boden | Störung, Schichtgrenze, Abbau- und Rutschungskante, Altlastengrenze | Altlasten nach Status, Abbau, Schutzflächen, Bodenarten |
| Lärm | Lärmschutzwand und -wall, Isophonen, Emissionsbänder | Pegelklassen in den Farben der DIN 45682, Schutzzonen, ruhiges Gebiet |
| Stadtklima | Kaltluft- und Frischluftleitbahn, Kaltluftabfluss, Flurwind, Hauptwindrichtung, Strömungsbarriere, Isothermen | Klimatope, thermische Belastung in vier Stufen, Ausgleichsräume, Kaltluftentstehungs- und Sammelgebiete, Überwärmungsgebiet, Maßnahmenflächen |
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
| Landschaftsplanung | grün, Wasser blau; Vitalitätsstufen im Baumkataster grün, gelb, orange, rot | Draufsicht = Gehölz und Baumkataster (`bk_`), Quadrat = Biotop- oder Nutzungstyp, gestricheltes Quadrat = Maßnahme, Kreis = Erholung | Bestands- und Maßnahmenpläne der Landschaftsplanung; Baumkataster: Vitalitätsstufen nach Roloff, Leistungen der ZTV-Baumpflege |
| Verkehr | weißes Sinnbild auf farbigem Quadrat | blau = Anlage oder Angebot, orange = Baustelle und Störung, rot = Sperrung und Beschränkung | Hinweiszeichen der StVO, amtliche Stadt- und Verkehrskarten |
| Wasserwirtschaft | blau | Kreis = Messstelle, Quadrat = Anlage oder Bauwerk, Raute = Gebiet, ohne Rahmen = Armatur auf der Leitung; Starkregen mit Präfix `sr_` | Leitungs- und Kanalnetzpläne (DIN 2425), übliche Kurzzeichen; Starkregen: Leitfaden Kommunales Starkregenrisikomanagement in Baden-Württemberg |
| Vermessung | schwarz-weiß | geometrische Grundformen ohne Rahmen | Liegenschaftskarte, Vermessungsriss (DIN 18702), Aufschlüsse nach DIN 4023 |
| Nordpfeile | schwarz-weiß, ohne Rahmen | Präfix = Bauart: `pfeil_` mit Schaft, `nadel_` ohne Schaft, `kreis_` im Kreis, `rose_` Windrose; das N steht über der Spitze, `_ohne_n` = ohne Buchstabe | Nordpfeile amtlicher Karten, Lagepläne und Bauleitpläne |
| Raumordnung | schwarz-weiß, Flächen farbig | konzentrische Kreise = Zentraler Ort (Rang über Ringe und Füllung), Quadrat = Standort, Kreis = Infrastruktur, Raute = Freiraum, kleines Quadrat mit Buchstabe = Kategorie (Z, G, N, V); Vorranggebiet durchgezogen und dicht, Vorbehaltsgebiet gestrichelt und weit schraffiert | § 7 ROG, Zentrale-Orte-System, NLT-Arbeitshilfe Planzeichen in der Regionalplanung (Niedersachsen 2024), Anlage 3 LPlG-DVO NRW |
| Realnutzung | grün `#00853C` (Zeichen), Flächen in Katasterfarben | Vegetationszeichen ohne Rahmen (`veg_`) wie in der Liegenschaftskarte; Flächen heißen `<Schlüssel> <Bezeichnung>` nach AdV-Nutzungsartenkatalog; ohne Zusatz = blasse Farbe des ALKIS-Signaturenkatalogs mit Vegetationszeichen, „kräftig“ = eigene Farben für Übersichtskarten | AdV-Nutzungsartenkatalog (GeoInfoDok 7.0.1), ALKIS-Signaturenkatalog der AdV (Version 6.0) |
| Gas, Fernwärme, Telekommunikation | Farbe je Sparte | gelb = Gas, orangerot = Fernwärme, grün = Telekommunikation; Quadrat = Station, Kreis = Messstelle oder Einrichtung, ohne Rahmen = Armatur auf der Leitung | Rohrnetzpläne nach DIN 2425, übliche Spartenfarben der Leitungsauskunft |
| Wärmeplanung | weinrot (Zeichen), Flächen je Versorgungsart | Quadrat = Erzeugungsanlage (`erz_`), Kreis = Wärmequelle oder Potenzial (`pot_`), Sechseck = Speicher und Infrastruktur (`inf_`), Raute = Verbraucher und Maßnahme (`vb_`), Hausumriss = dezentraler Wärmeerzeuger (`dez_`); Flächen und Linien: Wärmenetz grün, Wasserstoff violett, dezentral gelb, Prüfgebiet grau; Eignungsstufen als vier Töne derselben Farbe; Dichten von hellgelb bis dunkelrot | Wärmeplanungsgesetz (§§ 3, 18, 19, Anlage 2), Leitfaden Wärmeplanung des Bundes (2024) |
| Boden | braun | Kreis = Aufschluss oder Messstelle, Quadrat = Altlast oder Standort, Raute = Bodenschutz, Sechseck = Geologie und Rohstoffe | DIN 4023, Bodenkundliche Kartieranleitung, Altlastenkataster der Länder |
| Lärm | violett | Kreis = Immissionsort oder Messung, Quadrat = Quelle, Raute = Schutzmaßnahme, Sechseck = schutzbedürftige Nutzung, ohne Rahmen = Hilfszeichen der Schallausbreitung | 34. BImSchV, DIN 45682, DIN 18005, TA Lärm |
| Stadtklima | petrol (Zeichen), Linien und Flächen nach Bedeutung | Kreis = Messung (`mess_`), Quadrat = Belastung (`last_`), Sechseck = Ausgleichsraum (`ausgl_`), Raute = Maßnahme der Klimaanpassung (`anp_`), ohne Rahmen = Strömungspfeil (`pfeil_`); blau = Kaltluft, grün = Frischluft, orangerot = Wärme und Belastung, grau = Lufthygiene | VDI 3787 Blatt 1 (Klimaanalyse- und Planungshinweiskarten), Klimaanalyse Nordrhein-Westfalen |
| Forst | dunkelgrün | Baumkrone ohne Rahmen = Baumart oder Bestand, Quadrat = betriebliche Einrichtung, Kreis = Jagd und Wild, Raute = Waldfunktion oder Schutz | Forstbetriebskarten der Länder, Waldfunktionenkartierung |
| Landwirtschaft | ocker | Quadrat = Betrieb und Gebäude, Kreis = Kultur oder Nutzung, Sechseck = Technik und Wasser, Raute = Schutz, Förderung, Gebietskulisse | Kulturartengruppen des Agrarantrags (InVeKoS), Feldblockkataster |
| Tourismus | weißes Sinnbild auf farbigem Quadrat | grau = Unterkunft und Service, grün = Wandern, Rad und Natur, blau = Wasser und Winter (auch Wasser- und Wintersport), braun = Sehenswertes und Erlebnis, orangerot = Sport (`sport_`) | touristische Hinweiszeichen der StVO, amtliche Wander- und Freizeitkarten |
| Denkmalpflege | ziegelrot | Quadrat = Baudenkmal, Kreis = Bodendenkmal oder Fundstelle, Raute = Status oder Schutz, Sechseck = Erinnerung und Vermittlung; gestrichelt = vermutet oder abgegangen | Denkmalkartierungen der Landesämter, archäologische Fundstellenkarten |
| Brand- und Katastrophenschutz | weißes Sinnbild auf farbigem Quadrat | rot = Feuerwehr und Brandschutz, grün = Rettung und Flucht, blau = Katastrophenschutz, gelbes Dreieck = Gefahrenstelle | DIN 14095, DIN 14034, ISO 7010, taktische Zeichen |
| Kartengestaltung | schwarz-weiß | Kreis = Nummer, Quadrat = Buchstabe, Raute = Hinweiszeichen, ohne Rahmen = Pfeil oder Marke; rot = Hervorhebung | übliche Verweiszeichen in Plänen |
| Allgemein | dunkles Sinnbild auf weißer Fläche | Quadrat = Einrichtung oder Ort von Interesse, Kreis (`kr_`) = Punktmarker, ohne Rahmen (`topo_`) = topografisches Einzelzeichen, Formen und Nadeln (`form_`, `nadel_`) = freie Marker ohne feste Bedeutung; grau = allgemein, rot = Gesundheit und Rettung, blau = Sicherheit, Auskunft, Dienste | Objektarten amtlicher topografischer Karten und Stadtpläne |

**Farben der Leitungen in der Wasserwirtschaft:** Trinkwasser und Gebiete dunkelblau, Gewässer und Regenwasser
hellblau, Schmutzwasser braun, Mischwasser violett (übliche Farben in Kanalnetzplänen). Bei Starkregen zeigen
Blautöne die Überflutungstiefe, die Farben grün, gelb, orange und rot die Fließgeschwindigkeit.

**Linienelemente:** Einige Punktsymbole sind für Markierungslinien gedacht (PlanZV-Präfixe `um_` und `lt_`,
Armaturen in Strom und Wasser, `topo_boeschung`). Bei ihnen verläuft die Linie waagerecht durch die
Symbolmitte; bei den Umgrenzungen der PlanZV zeigt die Innenseite nach unten. In QGIS als Markierungslinie
mit festem Abstand und „Markierung drehen“ verwenden. Für die Umgrenzungen der PlanZV und die Böschung gibt es
das bereits fertig als Linien- bzw. Flächensymbol.

## Aufbau

```
metadata.ini                      Beschreibung des Repositorys und der Sammlungen
collections/<ID>/svg/             SVG-Dateien, Schema gisak_<sammlung>_<name>.svg
collections/<ID>/symbol/          QGIS-Stildateien: Linien_und_Flaechen.xml und Punkte.xml (Punktsymbole als Markierungssymbole)
collections/<ID>/preview/         Vorschaubilder für das Plugin
collections/<ID>/LICENSE          Lizenz der Sammlung
KATALOG.md                        Liste aller Symbole
tools/                            Generator (Python), aus dem alle SVGs erzeugt werden
tools/plugin/gisak_symbole/       Code des QGIS-Plugins „GIS-Akademie Symbole“
tools/mkplugin.py                 baut aus collections/ und dem Plugin-Code das Plugin-ZIP (nach dist/)
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
- **Starkregen (Wasserwirtschaft):** Die Klassen der Überflutungstiefe (5 bis 10 cm, 10 bis 50 cm, 50 bis 100 cm,
  über 100 cm) und der Fließgeschwindigkeit (unter 0,2, bis 0,5, bis 2, über 2 m/s) sowie die Szenarien selten,
  außergewöhnlich und extrem folgen den Starkregengefahrenkarten nach dem Leitfaden „Kommunales
  Starkregenrisikomanagement in Baden-Württemberg“. Andere Länder und die Hinweiskarte Starkregengefahren des
  Bundes nutzen teils andere Klassen und nur zwei Szenarien. Die Farben sind nicht vorgeschrieben.
- **Stadtklima:** Die Gliederung in Klimatope, Kaltluft- und Luftaustauschprozesse und Planungshinweise lehnt
  sich an die VDI 3787 Blatt 1 an; die Richtlinie selbst lag nicht vor. Die Klimatope folgen der Klimaanalyse
  Nordrhein-Westfalen, ergänzt um Industrie und Gleisanlagen. Zeichen und Farben sind eigene Entwürfe in
  üblicher Farbgebung; die Stufen der thermischen Belastung sind nicht an Kennwerte gebunden.
- **Baumkataster (Landschaftsplanung):** Die Vitalitätsstufen 0 bis 3 folgen dem Modell von Roloff, die
  Maßnahmen den üblichen Leistungen der Baumpflege, der Wurzelschutzbereich der DIN 18920. Die Zeichen sind
  eigene Entwürfe; die Regelwerke selbst lagen nicht vor.
- **Wärmeplanung:** Begriffe, Gebietsarten und Eignungsstufen folgen dem Wärmeplanungsgesetz (§§ 3, 18, 19,
  Anlage 2), die Klassen der Wärmedichte und der Wärmeliniendichte den Tabellen 11 und 12 des Leitfadens
  Wärmeplanung des Bundes (Juni 2024). Zeichen und Farben sind dort nicht vorgeschrieben; die Flächenfarben
  lehnen sich an die Beispielkarten des Leitfadens an, die Punktsymbole sind eigene Entwürfe. Andere
  Klassengrenzen (z. B. der Länderleitfäden) lassen sich über die Farben der Symbole abbilden.
- **Realnutzung:** Gliederung, Schlüssel und Bezeichnungen folgen dem AdV-Nutzungsartenkatalog (Stand 2015),
  die blassen Flächenfarben und die Vegetationszeichen dem ALKIS-Signaturenkatalog der AdV (Version 6.0, CMYK in
  RGB umgerechnet). Die Reihe „kräftig“ ist ein eigener Farbvorschlag für Übersichtskarten und nicht amtlich.
  Regionale Kartierschlüssel (z. B. Berlin, Regionalverband Ruhr) weichen davon ab.
- **Raumordnung:** Die Planzeichen für Regionalpläne unterscheiden sich je Land. Die Flächenfarben folgen
  überwiegend der niedersächsischen Arbeitshilfe, die Farbwerte sind aus deren Richtwerten abgeleitet.
- **Boden:** Die Signaturen der Bodenarten folgen der gängigen Praxis nach DIN 4023, nicht dem Normtext.
- **Linien- und Flächensymbole** sind in Millimetern bemessen und in QGIS 3.44 und 4.2 geprüft. Die Vorschaubilder
  zeigen eine Nachbildung; Punktmuster und Schraffuren können in QGIS leicht versetzt beginnen.
- Marken- und Unternehmenslogos wurden bewusst nicht nachgebildet.

## Lizenz

© 2026 GIS-Akademie, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de).
Bei Weitergabe bitte „GIS-Akademie“ als Urheber nennen.

Das QGIS-Plugin „GIS-Akademie Symbole“ (Code unter `tools/plugin/`) steht unter der GNU General Public License,
Version 2 oder später. Die im Plugin enthaltenen Symbole dürfen wahlweise unter dieser GPL oder unter CC BY 4.0
genutzt werden.
