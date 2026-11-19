"""Sammlung Topografie: Linien und Flaechen in der Standarddarstellung der GIS-Akademie fuer ALKIS-, ATKIS- und
OSM-Daten (NAS-Standardvisualisierung), dazu wenige schlichte Punktzeichen.
Vorlage: die Stildefinition der OSM-Darstellung (aaa_osm/OSM_NAS_Style/spec.py, gelesen am 19.11.2026), die Farben,
Strichstaerken und Strichmuster aus alkis.lyrx und atkis.lyrx uebernimmt. Die Werte sind von dort abgeschrieben
und von Punkt in Millimeter umgerechnet (pt()). Die Vorlage bleibt unveraendert; diese Datei ist eine Kopie der
Werte, keine Verknuepfung. Massstabsstufen, Beschriftung und Piktogramme der Vorlage sind nicht Teil der Sammlung.
Stil: Farbe = Objektart wie in der Vorlage. Strassen schwarz mit weissem Kern, Bahn schwarz mit gestricheltem Kern,
Gewaesser blau, Wege braun, Grenzen weinrot, Gebaeude rosa mit Funktionsfarben, Vegetation gruen.
  Ohne Zusatz = Darstellung im grossen Massstab (bis etwa 1:10.000), ", Uebersicht" = schmalere Darstellung fuer
  mittlere Massstaebe (etwa 1:50.000 bis 1:250.000), ", thematisch" = kraeftige Farben der urbanen Flaechennutzung.
Punktzeichen: Piktogramme (pk_) als heller Kreis mit schwarzem Sinnbild wie in der Vorlage, Hintergrundfarbe nur nach
  Kategorie (Verkehr grau, Religion rosa, Gastronomie, Beherbergung und Handel gelblich, Technik hellgrau, Polizei
  blau, Feuerwehr rot; Gesundheit rotes Sinnbild). Die Sinnbilder kommen aus den vorhandenen Sammlungen (siehe pk()).
  Dazu die einfachen Marken der Vorlage ohne Rahmen (Mast, Bahnuebergang, Poller ...), deutlicher gezeichnet.
"""
import colorsys
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "topografie"
NAME = "Topografie"
DESC = ("Linien und Flächen für topografische Karten aus ALKIS-, ATKIS- und OSM-Daten in der Standarddarstellung "
        "der GIS-Akademie: Straßen, Wege, Bahn, Gewässer, Grenzen, Gebäude nach Funktion, Vegetation, Siedlung "
        "und Bauwerke")
TAGS = "topografie, alkis, atkis, osm, nas, basiskarte, strasse, bahn, gewaesser, gebaeude, grenze, vegetation"

SW = ("#FFFFFF", "#000000")


def rgb(r, g, b, a=None):
    return "#%02X%02X%02X" % (r, g, b) + ("" if a is None else "%02X" % round(a * 2.55))


def hsv(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, s / 100.0, v / 100.0)
    return rgb(round(r * 255), round(g * 255), round(b * 255))


def pt(v):  # Punkt -> Millimeter
    return round(v * 0.3528, 2)


def st(muster_pt):
    return [pt(v) for v in muster_pt] if muster_pt else None


BLACK, WHITE = "#000000", "#FFFFFF"
G35, G52, G78, G104, G110, G130, G156, G204, G225 = (rgb(v, v, v) for v in (35, 52, 78, 104, 110, 130, 156, 204, 225))
BG = rgb(255, 242, 217)
GEB, GEB_KULTUR, GEB_RELIGION, GEB_BILDUNG = rgb(255, 190, 190), rgb(242, 210, 204), rgb(238, 137, 142), rgb(255, 160, 140)
GEB_SPORT, GEB_SICHER, TURM = rgb(247, 131, 126), rgb(128, 119, 82), rgb(255, 127, 127)
PARK, SPIEL, SPORTFL, SPIELFELD = hsv(124, 43, 71), hsv(81, 19, 99), rgb(233, 255, 190), rgb(70, 163, 76)
SCHWIMM, HUND, FRIEDHOF, LANDW = rgb(190, 232, 255), rgb(115, 115, 58), rgb(79, 113, 92), rgb(187, 173, 110)
WALD, WALD_LAUB, WALD_NADEL, GEHOELZ = rgb(92, 184, 96), rgb(125, 184, 92), rgb(92, 184, 128), rgb(126, 206, 130)
HEIDE, UNLAND, SAND, GRAS, FELS, GLETSCHER = (rgb(171, 205, 102), rgb(180, 215, 203), rgb(215, 194, 158),
                                              rgb(206, 226, 172), G204, rgb(235, 245, 255))
FLIESS, STEHEND, GEW, HAFEN, SUMPF, SUMPF_M, MOOR = (rgb(190, 210, 255), rgb(0, 169, 230), rgb(115, 178, 255),
                                                     rgb(140, 170, 210), rgb(0, 112, 255), rgb(115, 178, 255), rgb(150, 140, 95))
WEG, FAHRWEG, RADWEG = rgb(137, 90, 68), rgb(168, 112, 0), rgb(0, 92, 230)
HALDE, HALDE_OUT, MIL, GEFAHR, SCHUTZ, GRENZE = (rgb(137, 90, 68), rgb(224, 210, 184), rgb(128, 119, 82), rgb(168, 0, 0),
                                                 rgb(0, 115, 76), rgb(115, 0, 76))
GRENZE2 = rgb(115, 0, 76, 60)
TANK, SILO, KLAER = hsv(29, 24, 100), hsv(107, 29, 99), rgb(0, 76, 115)

S = [
    # ---- Schlichte Marken der Vorlage (schwarz, ohne Rahmen) ----
    ("mast_hochspannung", "Hochspannungsmast (Gittermast)", *SW,
     [R(20, 20, 60, 60, "F", "S", 8), L(20, 20, 80, 80, 6, cap="butt"), L(20, 80, 80, 20, 6, cap="butt")]),
    ("mast", "Mast", *SW, [C(50, 50, 22, "S", "N", 0)]),
    ("bahnuebergang", "Bahnübergang", *SW, xcross(50, 50, 32, 12)),
    ("prellbock", "Prellbock (Gleis waagerecht, drehbar)", *SW, [L(10, 50, 50, 50, 8, cap="butt"), L(50, 14, 50, 86, 16, cap="butt")]),
    ("seilbahnstuetze", "Seilbahnstütze (Seil waagerecht, drehbar)", *SW,
     [L(4, 50, 96, 50, 6, cap="butt"), PG([(50, 22), (78, 50), (50, 78), (22, 50)], "S")]),
    ("schranke", "Tor / Schranke (Weg waagerecht, drehbar)", *SW,
     [L(50, 10, 50, 90, 10, cap="butt"), C(50, 14, 10, "S", "N", 0)]),
    ("poller", "Poller / Sperre", *SW, [C(50, 50, 24, "F", "S", 8), C(50, 50, 8, "S", "N", 0)]),
    ("wasserbauwerk", "Wasserbauwerk", *SW, [R(14, 14, 72, 72, "F", "S", 8), wave(24, 42, 52, 7, 2, 7), wave(24, 64, 52, 7, 2, 7)]),
]


# ---- Piktogramme im hellen Kreis (pk_) ----
# Aussehen wie in der Vorlage: heller Kreis, schwarzes Sinnbild, Hintergrundfarbe nur nach Kategorie. Die Sinnbilder
# werden nicht neu gezeichnet, sondern aus den vorhandenen Sammlungen geholt (ohne deren Rahmen) und in den Kreis
# gesetzt. Aendert sich dort ein Sinnbild, aendert es sich auch hier.
import sym_allgemein, sym_verkehr, sym_tourismus, sym_denkmal, sym_strom, sym_wasser, sym_boden

_QUELLEN = {"A": sym_allgemein, "V": sym_verkehr, "T": sym_tourismus, "D": sym_denkmal, "E": sym_strom, "W": sym_wasser,
            "B": sym_boden}
_WEISS = ("V", "T")   # Sammlungen mit weissem Sinnbild auf farbigem Quadrat: Weiss wird zur Zeichenfarbe


class _Dunkel:
    def __init__(self, c):
        self.c = c

    def f(self, role):
        return self.c.f("S" if role == "W" else role)

    def s(self, role, sw, cap="round", dash=None):
        return self.c.s("S" if role == "W" else role, sw, cap, dash)


def _sinnbild(quelle):
    q, name = quelle.split(":")
    elems = next(s[4] for s in _QUELLEN[q].SYMBOLS if s[0] == name)
    if not name.startswith("topo_"):
        elems = elems[1:]                      # Rahmen der Quellsammlung weglassen
    if q in _WEISS:
        elems = [(lambda c, e=e: e(_Dunkel(c))) for e in elems]
    return elems


def pk(name, titel, quelle, grund="#FFFFFF", farbe="#000000", k=0.68):
    return ("pk_" + name, titel, grund, farbe, [C(50, 50, 45, "F", "S", 4)] + fit(_sinnbild(quelle), 50, 50, k))


ROT = "#E60000"
B_VERKEHR, B_RELIGION, B_GASTRO, B_TECHNIK = G156, GEB_RELIGION, rgb(255, 235, 190), G225
PIKTO = [
    # Bildung
    pk("hochschule", "Hochschule", "A:hochschule"), pk("schule", "Schule", "A:schule"),
    pk("kita", "Kindergarten / Kita", "A:kindertagesstaette"), pk("bibliothek", "Bibliothek", "A:bibliothek"),
    # Gesundheit
    pk("krankenhaus", "Krankenhaus", "A:krankenhaus", farbe=ROT), pk("apotheke", "Apotheke", "A:apotheke", farbe=ROT),
    pk("arzt", "Arzt", "A:arzt", farbe=ROT), pk("zahnarzt", "Zahnarzt", "A:zahnarzt", farbe=ROT),
    pk("tierarzt", "Tierarzt", "A:tierarzt", farbe=ROT), pk("pflegeheim", "Soziale Einrichtung / Pflegeheim", "A:pflegeeinrichtung"),
    pk("rettungswache", "Rettungswache", "A:rettungswache", farbe=ROT),
    # Religion
    pk("kirche", "Kirche / Kapelle", "A:kirche", B_RELIGION), pk("moschee", "Moschee", "A:moschee", B_RELIGION),
    pk("synagoge", "Synagoge", "A:synagoge", B_RELIGION), pk("tempel", "Tempel / sonstiges Gotteshaus", "A:tempel", B_RELIGION),
    pk("friedhof", "Friedhof", "A:friedhof", G225),
    # Kultur
    pk("museum", "Museum", "A:museum"), pk("theater", "Theater / Oper", "A:theater"), pk("kino", "Kino", "A:kino"),
    pk("veranstaltung", "Veranstaltung / Gemeindezentrum", "A:veranstaltungshalle"),
    pk("denkmal", "Denkmal / Gedenkstätte", "A:denkmal"), pk("kunstwerk", "Kunstwerk", "A:kunstwerk"),
    pk("brunnen", "Brunnen", "A:topo_brunnen"),
    # Oeffentlicher Dienst und Sicherheit
    pk("rathaus", "Rathaus / Verwaltung", "A:rathaus"), pk("botschaft", "Botschaft / Konsulat", "A:botschaft"),
    pk("gericht", "Gericht", "A:gericht"), pk("polizei", "Polizei", "A:polizei", rgb(0, 77, 168), "#FFFFFF"),
    pk("feuerwehr", "Feuerwehr", "A:feuerwehr", rgb(245, 130, 136)), pk("post", "Post", "A:post"),
    pk("briefkasten", "Briefkasten", "A:briefkasten"), pk("jva", "Justizvollzugsanstalt", "A:justizvollzugsanstalt"),
    pk("militaer", "Militärische Anlage", "A:kaserne", MIL, "#FFFFFF"),
    # Mobilitaet
    pk("flughafen", "Flughafen / Flugplatz", "V:flughafen", B_VERKEHR),
    pk("hubschrauberlandeplatz", "Hubschrauberlandeplatz", "V:hubschrauberlandeplatz", B_VERKEHR),
    pk("bahnhof", "Bahnhof / Haltepunkt", "V:bahnhof", B_VERKEHR), pk("strassenbahn", "Straßenbahnhaltestelle", "V:strassenbahn", B_VERKEHR),
    pk("u_bahn", "U-Bahn-Eingang", "V:u_bahn", B_VERKEHR), pk("bushaltestelle", "Bushaltestelle", "V:bushaltestelle", B_VERKEHR),
    pk("busbahnhof", "Busbahnhof", "V:busbahnhof", B_VERKEHR), pk("faehre", "Fähranleger", "V:faehre", B_VERKEHR),
    pk("parkplatz", "Parkplatz", "V:parkplatz", B_VERKEHR), pk("parkhaus", "Parkhaus / Tiefgarage", "V:parkhaus", B_VERKEHR),
    pk("tankstelle", "Tankstelle", "V:tankstelle", B_VERKEHR), pk("ladestation", "Ladestation", "V:ladestation"),
    pk("fahrradabstellanlage", "Fahrradabstellanlage", "V:fahrradabstellanlage"),
    pk("fahrradverleih", "Fahrradverleih", "T:fahrradverleih"), pk("taxi", "Taxi", "V:taxi"),
    pk("carsharing", "Carsharing / Autovermietung", "V:carsharing"), pk("yachthafen", "Yachthafen", "V:sportboothafen"),
    # Sport und Freizeit
    pk("stadion", "Stadion", "A:stadion", rgb(91, 184, 83)), pk("sportplatz", "Sportplatz", "T:sport_fussball"),
    pk("sporthalle", "Sporthalle / Sportzentrum", "A:sporthalle"), pk("schwimmbad", "Schwimmbad", "A:schwimmbad", rgb(182, 230, 254)),
    pk("spielplatz", "Spielplatz", "A:spielplatz"), pk("golfplatz", "Golfplatz", "T:golfplatz", PARK),
    pk("reitanlage", "Reitanlage", "T:reiten"), pk("hundeplatz", "Hundeplatz", "A:hundewiese"),
    pk("tennis", "Tennis", "T:sport_tennis"), pk("leichtathletik", "Leichtathletik", "T:sport_leichtathletik"),
    pk("schiessen", "Schießen", "T:sport_schiessen"), pk("klettern", "Klettern", "T:klettergarten"), pk("ski", "Ski", "T:skipiste"),
    pk("eissport", "Eissport", "T:eislaufen"), pk("wassersport", "Wassersport", "T:segeln"),
    pk("motorsport", "Motorsport", "T:sport_motorsport"), pk("zoo", "Zoo / Tierpark", "A:zoo", PARK),
    pk("campingplatz", "Campingplatz", "A:campingplatz", PARK), pk("picknickplatz", "Picknickplatz / Rastplatz", "T:picknickplatz"),
    pk("bootsanleger", "Bootsanleger / Slipanlage", "T:bootsverleih"),
    # Tourismus und historische Orte
    pk("hotel", "Hotel", "A:hotel", B_GASTRO), pk("ferienwohnung", "Pension / Ferienwohnung", "T:ferienwohnung", B_GASTRO),
    pk("jugendherberge", "Jugendherberge", "A:jugendherberge", B_GASTRO), pk("berghuette", "Berghütte", "T:berghuette", B_GASTRO),
    pk("schutzhuette", "Schutzhütte / Unterstand", "T:schutzhuette"), pk("sehenswuerdigkeit", "Sehenswürdigkeit", "A:sehenswuerdigkeit"),
    pk("aussichtspunkt", "Aussichtspunkt", "T:aussichtspunkt"), pk("information", "Information", "A:information"),
    pk("burg", "Burg / Schloss", "A:burg_schloss"), pk("ruine", "Ruine", "A:ruine"),
    pk("archaeologie", "Archäologische Stätte", "D:fundstelle"), pk("schlachtfeld", "Schlachtfeld", "D:schlachtfeld"),
    pk("grabmal", "Grabmal", "D:grabmal"), pk("museumsbahn", "Museumsbahn", "A:museumsbahn"),
    pk("windmuehle", "Windmühle", "A:windmuehle", B_GASTRO), pk("wassermuehle", "Wassermühle", "A:wassermuehle", B_GASTRO),
    # Gastronomie, Einkaufen und Dienstleistung
    pk("restaurant", "Restaurant", "A:gastronomie", B_GASTRO), pk("cafe", "Café", "A:cafe", B_GASTRO),
    pk("imbiss", "Imbiss", "A:imbiss", B_GASTRO), pk("bar", "Bar / Kneipe / Biergarten", "A:bar", B_GASTRO),
    pk("supermarkt", "Supermarkt", "A:einkauf", B_GASTRO), pk("baumarkt", "Baumarkt", "A:baumarkt", B_GASTRO),
    pk("baeckerei", "Bäckerei", "A:baeckerei", B_GASTRO), pk("bekleidung", "Bekleidung", "A:bekleidung", B_GASTRO),
    pk("friseur", "Friseur", "A:friseur", B_GASTRO), pk("optiker", "Optiker", "A:optiker", B_GASTRO),
    pk("marktplatz", "Marktplatz", "A:markt", B_GASTRO), pk("bank", "Bank / Geldautomat", "A:bank", B_GASTRO),
    # Oeffentliche Anlagen und Entsorgung
    pk("toilette", "Toilette", "A:toilette"), pk("trinkwasser", "Trinkwasser", "A:trinkbrunnen"), pk("telefon", "Telefon", "A:telefon"),
    pk("packstation", "Packstation", "A:paketstation"), pk("sitzbank", "Sitzbank", "A:sitzbank"),
    pk("recycling", "Recycling / Wertstoffcontainer", "A:altglascontainer"), pk("abfalleimer", "Abfalleimer", "A:abfalleimer"),
    # Energie, Technik und Naturraum
    pk("windenergieanlage", "Windenergieanlage", "A:topo_windrad"), pk("kraftwerk", "Kraftwerk", "E:kraftwerk", B_TECHNIK),
    pk("umspannwerk", "Umspannwerk", "E:umspannwerk", B_TECHNIK), pk("funkmast", "Funkmast / Fernmeldeturm", "A:funkmast", B_TECHNIK),
    pk("wasserturm", "Wasserturm", "W:wasserturm", B_TECHNIK), pk("leuchtturm", "Leuchtturm", "A:leuchtturm"),
    pk("schornstein", "Schornstein", "A:topo_schornstein", B_TECHNIK), pk("bergwerk", "Bergwerk / Schacht / Stollen", "A:bergwerk", B_TECHNIK),
    pk("steinbruch", "Steinbruch / Tagebau", "A:topo_steinbruch", B_TECHNIK), pk("halde", "Halde", "B:halde", B_TECHNIK),
    pk("hoehle", "Höhleneingang", "A:hoehle"), pk("gipfel", "Gipfel", "A:gipfel"), pk("quelle", "Quelle", "A:topo_quelle"),
]

# Die schlichten Marken sind in der Vorlage deutlich kleiner als die Piktogramme: im Raster verkleinert zeichnen,
# damit eine gemeinsame Vorgabegroesse passt.
SYMBOLS = PIKTO + [(n_, t_, f_, s_, fit(e_, 50, 50, 0.55)) for n_, t_, f_, s_, e_ in S]
GROESSE = 5.0


# ---- Linien und Flaechen (QGIS-Stildatei) ----
def li(farbe, breite, strich=None):  # Linie, Masse in Punkt wie in der Vorlage
    return linie(farbe, pt(breite), st(strich))


def kern(aussen, ba, innen, bi, strich=None):  # Umrandung und Kern
    return [linie(aussen, pt(ba), ende="round"), linie(innen, pt(bi), st(strich), ende="flat" if strich else "round")]


def querstrich(farbe, laenge, staerke, abstand):
    return marken(mk("line", pt(laenge), farbe, rw=pt(staerke)), pt(abstand))


STRASSEN = [("Autobahn", 4.6, 3.0), ("Schnellstraße", 4.2, 2.6), ("Bundesstraße", 3.6, 2.2), ("Landesstraße", 3.2, 1.9),
            ("Kreisstraße", 2.8, 1.6), ("Gemeindestraße", 2.4, 1.3)]

LINIEN = [(t, kern(BLACK, a, WHITE, i)) for t, a, i in STRASSEN] + [
    ("Verkehrsberuhigte Straße / Fußgängerzone", kern(G78, 2.2, G225, 1.3)),
    ("Zufahrt / Erschließung", [li(G78, 0.8)]),
    ("Fahrweg / Wirtschaftsweg", [li(FAHRWEG, 1.2)]),
    ("Autobahn, Übersicht", kern(BLACK, 3.4, WHITE, 1.6)),
    ("Schnellstraße, Übersicht", kern(BLACK, 3.0, WHITE, 1.4)),
    ("Bundesstraße, Übersicht", kern(BLACK, 2.2, WHITE, 1.0)),
    ("Landesstraße, Übersicht", [li(BLACK, 1.2)]),
    ("Kreisstraße, Übersicht", [li(BLACK, 0.8)]),
    ("Gemeindestraße, Übersicht", [li(G52, 0.4)]),
    ("Straße im Bau", [li(G78, 1.8, [6, 3])]),
    ("Straße geplant", [li(G130, 1.2, [3, 3])]),
    ("Brücke", kern(BLACK, 3.5, WHITE, 2.2)),
    ("Fußweg / Pfad", [li(WEG, 1.0)]),
    ("Gehweg / Überweg", [li(WEG, 0.5, [3, 1.5])]),
    ("Treppe", [li(WEG, 0.8), querstrich(WEG, 3, 0.8, 2.2)]),
    ("Reitweg", [li(WEG, 1.0, [4, 2])]),
    ("Radweg", [li(RADWEG, 0.9, [5, 2])]),
    ("Gleis", kern(BLACK, 1.2, G225, 0.7, [5, 5])),
    ("Nebengleis", kern(BLACK, 0.8, G225, 0.4, [4, 4])),
    ("Bahnstrecke, Übersicht", kern(BLACK, 2.6, WHITE, 1.8, [5, 5])),
    ("Straßenbahn / Stadtbahn", [li(G78, 1.0)]),
    ("U-Bahn", [li(G78, 1.0, [6, 3])]),
    ("Standseilbahn / Sonderbahn", kern(G52, 1.2, WHITE, 0.6, [3, 3])),
    ("Bahnstrecke stillgelegt", [li(G130, 0.7, [4, 3])]),
    ("Bahnstrecke im Bau / geplant", [li(G78, 1.0, [8, 4])]),
    ("Bahnsteigkante", [li(G78, 1.2)]),
    ("Start- und Landebahn", [li(G130, 4)]),
    ("Rollweg", [li(G130, 1.5)]),
    ("Fährlinie", [li(rgb(102, 153, 205), 1.2, [5, 2])]),
    ("Steg / Pier", [li(G52, 1.2)]),
    ("Wellenbrecher / Buhne", [li(G52, 1.8)]),
    ("Schleuse / Wehr / Damm", [li(BLACK, 1.5)]),
    ("Seilbahn / Sessellift", [li(BLACK, 0.8), querstrich(BLACK, 4, 0.4, 15)]),
    ("Schlepplift", [li(BLACK, 0.8, [4, 2])]),
    ("Materialseilbahn", [li(G52, 0.6, [6, 2, 2, 2])]),
    ("Hochspannungsleitung", [li(BLACK, 0.8), marken(mk("circle", pt(4), BLACK), pt(34))]),
    ("Hochspannungsleitung, Übersicht", [li(BLACK, 0.5), marken(mk("circle", pt(2.5), BLACK), pt(30))]),
    ("Mittel- und Niederspannungsleitung", [li(G52, 0.5)]),
    ("Erdkabel", [li(G52, 0.5, [4, 2])]),
    ("Rohrleitung / Pipeline", [li(BLACK, 2, [6, 2, 2, 2, 2, 2])]),
    ("Förderband", [li(rgb(51, 51, 51), 3), marken(mk("triangle", pt(2.5), WHITE), pt(8))]),
    ("Fluss", [li(GEW, 1.6)]),
    ("Kanal", [li(GEW, 1.4)]),
    ("Bach", [li(GEW, 0.8)]),
    ("Graben", [li(GEW, 0.5)]),
    ("Küstenlinie", [li(STEHEND, 1.2)]),
    ("Deich", [li(G78, 1.0), querstrich(G78, 3, 0.6, 4)]),
    ("Böschung / Damm", [li(G78, 0.6), querstrich(G78, 2.5, 0.5, 3)]),
    ("Klippe / Steilkante", [li(G52, 0.8), marken(mk("triangle", pt(3), G52, winkel=180, dy=-pt(1.5)), pt(5))]),
    ("Grat / Tal", [li(G78, 0.6, [6, 3])]),
    ("Hecke", [li(WALD, 1.2)]),
    ("Mauer", [li(BLACK, 0.8)]),
    ("Zaun / Absperrung", [li(G52, 0.5)]),
    ("Staatsgrenze", [li(GRENZE, 2.5)]),
    ("Landesgrenze", [li(GRENZE2, 2.2)]),
    ("Grenze Regierungsbezirk", [li(GRENZE2, 1.4, [8, 3])]),
    ("Kreisgrenze", [li(GRENZE2, 1.2)]),
    ("Grenze Amt / Verbandsgemeinde", [li(GRENZE2, 0.8, [6, 2])]),
    ("Gemeindegrenze", [li(GRENZE2, 0.8)]),
    ("Grenze Ortsteil / Stadtteil", [li(GRENZE2, 0.6, [3, 2])]),
    ("Grenze Postleitzahlgebiet", [li(RADWEG, 0.8, [6, 3])]),
    ("Schutzgebietsgrenze", [li(SCHUTZ, 2)]),
    ("Wanderroute", [li(rgb(230, 0, 0), 1.2, [6, 3])]),
    ("Radroute", [li(RADWEG, 1.2, [6, 3])]),
    ("Skiroute / Piste", [li(rgb(0, 130, 200), 1.2, [2, 2])]),
    ("Reit- und Kanuroute", [li(FAHRWEG, 1.0, [6, 3])]),
    ("ÖPNV-Linie", [li(rgb(0, 77, 168), 1.2)]),
]


def fl(farbe, rand=None, br=0.7, strich=None):  # Flaeche mit optionalem Umriss
    return [voll(farbe)] + ([li(rand, br, strich)] if rand else [])


def sch(farbe, breite=1, winkel=45, abstand=5):  # Schraffur, Masse in Punkt
    return schraffur(farbe, pt(breite), winkel, pt(abstand))


FLAECHEN = [
    ("Hintergrund", fl(BG)),
    # Gebaeude
    ("Gebäude", fl(GEB, G110, 0.4)),
    ("Gebäude, Religion", fl(GEB_RELIGION, G110, 0.4)),
    ("Gebäude, Bildung", fl(GEB_BILDUNG, G110, 0.4)),
    ("Gebäude, Gesundheit", fl(WHITE, BLACK, 0.5)),
    ("Gebäude, Sicherheit und Militär", fl(GEB_SICHER, BLACK, 0.5)),
    ("Gebäude, Verkehr", fl(G156, BLACK, 0.3)),
    ("Gebäude, Sport und Freizeit", fl(GEB_SPORT, BLACK, 0.5)),
    ("Gebäude, Kultur und Verwaltung", fl(GEB_KULTUR, G110, 0.4)),
    ("Gewächshaus", fl(rgb(232, 244, 232), G110, 0.3)),
    ("Überdachung", fl(hsv(22, 25, 100), G110, 0.3)),
    ("Tank / Gasometer", fl(TANK, G110, 0.7)),
    ("Silo", fl(SILO, G110, 0.7)),
    ("Gebäude, Ruine", fl(rgb(255, 220, 220), G110, 0.3)),
    ("Gebäude im Bau", fl(rgb(240, 240, 240), G110, 0.3)),
    ("Turm", fl(TURM, G204, 1)),
    ("Werk / Fabrik", [voll(GEB), sch(G110), li(G110, 0.7)]),
    ("Brückenfläche", fl(G204, G52, 0.5)),
    # Verkehr
    ("Straßenfläche", fl(G225, G110, 0.5)),
    ("Fußgängerzone / Platz", [voll(G225), sch(WHITE, 1, 45, 4), li(G110, 0.7)]),
    ("Wegefläche", fl(G204)),
    ("Parkplatz / Rastplatz", fl(G156, G110, 0.5)),
    ("Bahnsteig / Haltestellenbereich", fl(G156, G110, 0.3)),
    ("Bahnverkehrsfläche", fl(G104)),
    ("Bahnbetriebsanlage", fl(G78, G204, 0.5)),
    ("Flughafen / Flugplatz", fl(G225, G110, 0.7)),
    ("Militärflugplatz", [voll(G225), sch(MIL, 0.8, 45, 6), li(MIL, 1)]),
    ("Start- und Landebahnfläche, Rollweg", fl(G130)),
    ("Vorfeld", fl(G156)),
    ("Baustelle", fl(G225, G78, 1, [4, 2])),
    # Gewaesser
    ("Fließgewässer", fl(FLIESS)),
    ("Stehendes Gewässer", fl(STEHEND)),
    ("Becken / Klärteich", [voll(STEHEND), sch(G110, 0.5, 45, 4), li(G110, 0.5)]),
    ("Hafenbecken / Dock", [voll(FLIESS), sch(G110), li(G110, 1)]),
    ("Yachthafen", fl(HAFEN, G110, 1)),
    ("Watt / Schlamm", fl(UNLAND, G110, 0.5)),
    ("Sumpf / Feuchtgebiet", [voll(SUMPF), muster(mk("line", pt(6), SUMPF_M, rw=pt(1), winkel=90), pt(15), versatz=pt(7.5)),
                              li(G110, 1)]),
    ("Moor", fl(MOOR, G110, 1)),
    ("Gletscher", fl(GLETSCHER, GEW, 0.7)),
    ("Deichfläche", [sch(BLACK, 0.5, 135, 5), sch(BLACK, 0.5, 45, 5), li(BLACK, 0.4)]),
    ("Dammfläche", fl(G78, BLACK, 0.5)),
    ("Klärwerk / Wasserwerk", [voll(KLAER), sch(G110, 1, 45, 4), li(FAHRWEG, 0.5)]),
    # Vegetation und Landwirtschaft
    ("Wald", fl(WALD, G110, 0.5)),
    ("Laubwald", fl(WALD_LAUB, G110, 0.5)),
    ("Nadelwald", fl(WALD_NADEL, G110, 0.5)),
    ("Gehölz / Gebüsch", fl(GEHOELZ)),
    ("Heide", fl(HEIDE)),
    ("Grasland", fl(GRAS)),
    ("Strand / Sandfläche", fl(SAND)),
    ("Düne", fl(SAND, G110, 0.3, [3, 2])),
    ("Fels", fl(FELS, G110, 0.3)),
    ("Geröll", fl(rgb(224, 224, 224), G110, 0.3)),
    ("Ackerland", fl(LANDW)),
    ("Grünland / Wiese", fl(rgb(205, 205, 140))),
    ("Obstbau / Baumschule", [voll(LANDW), muster(mk("circle", 1.2, rgb(57, 97, 35)), 3.6, versatz=1.8)]),
    ("Weinbau", [voll(LANDW), sch(rgb(115, 76, 0), 0.5, 90, 4)]),
    # Siedlung und Freizeit
    ("Wohnbaufläche", fl(GEB)),
    ("Industrie- und Gewerbefläche", [voll(GEB), sch(G110, 0.7, 45, 6)]),
    ("Fläche besonderer funktionaler Prägung", fl(rgb(255, 220, 235))),
    ("Friedhof", fl(FRIEDHOF)),
    ("Park / Grünanlage", fl(PARK)),
    ("Kleingarten", fl(PARK, G110, 0.2)),
    ("Sport-, Freizeit- und Erholungsfläche", fl(SPORTFL, G110, 0.2)),
    ("Sport- und Spielanlage", fl(SPIEL, G110, 0.7)),
    ("Spielfeld / Laufbahn", fl(SPIELFELD, G110, 0.2)),
    ("Schwimmbecken", fl(SCHWIMM, BLACK, 0.5)),
    ("Reitanlage", fl(rgb(205, 170, 102), G110, 0.5)),
    ("Hundeplatz", fl(HUND, G110, 0.7)),
    ("Bauerwartungsland / Brache", fl(rgb(236, 236, 220), G110, 0.5, [4, 2])),
    ("Halde", fl(HALDE, HALDE_OUT, 0.6)),
    ("Tagebau / Steinbruch / Grube", fl(G78)),
    ("Umspannwerk", fl(G204, G110, 0.7)),
    ("Kraftwerk / Energieanlage", fl(G225, G110, 0.7)),
    ("Solarpark", [voll(G225), sch(rgb(0, 77, 168), 0.5, 0, 3), li(G110, 0.5)]),
    ("Militärgelände", [sch(MIL, 0.8, 45, 6), li(MIL, 1.5)]),
    ("Militärische Gefahrenzone", [sch(GEFAHR, 0.6, 45, 8), li(GEFAHR, 1.2, [6, 3])]),
    ("Schutzgebiet", [sch(SCHUTZ, 0.7, 45, 6), li(SCHUTZ, 2)]),
    ("Nationalpark", [sch(SCHUTZ, 1, 45, 5), li(SCHUTZ, 3)]),
    # Urbane Flaechennutzung, thematisch
    ("Wohnbaufläche, thematisch", fl(rgb(168, 0, 0), G110, 0.7)),
    ("Industriefläche, thematisch", fl(rgb(255, 255, 0), G110, 0.7)),
    ("Gewerbe und Einzelhandel, thematisch", fl(rgb(255, 200, 0), G110, 0.7)),
    ("Fläche besonderer funktionaler Prägung, thematisch", fl(rgb(255, 0, 197), G110, 0.7)),
    ("Gemischte Nutzung, thematisch", fl(rgb(0, 197, 255), G110, 0.7)),
]
