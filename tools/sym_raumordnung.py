"""Sammlung Raumordnung und Regionalplanung: Zentrale Orte, Standorte, Infrastruktur, Freiraum,
Kategorie-Kennzeichen; dazu Grenzen, Achsen und Trassen als Linien sowie Vorrang-, Vorbehalts-, Eignungs-
und Ausschlussgebiete als Flaechen.
Orientierung: Paragraf 7 ROG (Vorrang-, Vorbehalts- und Eignungsgebiete), Zentrale-Orte-System, Planzeichen
der Laender fuer Regionalplaene. Angesehen wurden die NLT-Arbeitshilfe "Planzeichen in der Regionalplanung"
(Niedersaechsischer Landkreistag, Stand Juli 2024, mit Farbtabelle in CMYK) und die Anlage 3 zur LPlG-DVO
Nordrhein-Westfalen. Die Planzeichen sind je Land verschieden; dies sind eigene, schlichte Entwuerfe und
keine amtlichen Planzeichen eines Landes.
Stil der Punktsymbole: schwarz-weiss wie in Regionalplan-Legenden, weisse Fuellung, schwarzer Strich 5.
Die Form zeigt die Gruppe:
  konzentrische bzw. gefuellte Kreise ohne Rahmen = Zentraler Ort (Rang ueber Zahl der Ringe und Fuellung),
  Quadrat mit scharfen Ecken = Standort, Kreis = Infrastruktur, Raute = Freiraum,
  kleines Quadrat mit Buchstabe = Kategorie-Kennzeichen (Z, G, N, V).
Linien: schwarz und grau; durchgezogen = Bestand, gestrichelt = Planung; Gruenzaesur gruen.
Flaechen (farbig, Ausnahme vom Schwarz-Weiss): Farben in Anlehnung an die Farbtabelle der NLT-Arbeitshilfe
(Natur und Landschaft gruen, Landwirtschaft beige, Wald mittelgruen, Rohstoffe schwarz/grau, Wasser blau,
Hochwasserschutz dunkelblau, Erholung hellgruen, Siedlung hellrot, Gewerbe hellviolett, Energie rot);
Bildschirmfarben aus den CMYK-Richtwerten geschaetzt. Solarenergie, Verdichtungsraum, laendlicher Raum,
Eignungs- und Ausschlussgebiet sind dort nicht als Flaechenfarbe belegt: eigene Wahl.
Regel: Vorranggebiet = durchgezogener Umriss mit Vollfarbe oder dichter Schraffur,
       Vorbehaltsgebiet = gestrichelter Umriss mit weiter Schraffur in derselben Farbe und Richtung.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "raumordnung"
NAME = "Raumordnung und Regionalplanung"
DESC = ("Symbole für Raumordnung und Regionalplanung: Zentrale Orte, Standorte, Infrastruktur, Freiraum und "
        "Kategorie-Kennzeichen, dazu Grenzen, Achsen und Trassen sowie Vorrang-, Vorbehalts-, Eignungs- und "
        "Ausschlussgebiete")
TAGS = "raumordnung, regionalplan, regionalplanung, landesplanung, zentrale orte, vorranggebiet, vorbehaltsgebiet, rog"

SW = ("#FFFFFF", "#000000")


# ---- Rahmen ----
def zo(*sh):  # Zentraler Ort: ohne Rahmen
    return list(sh)


def ring(r, sw=5, dash=None):
    return C(50, 50, r, "F", "S", sw, dash)


def kern(r):
    return C(50, 50, r, "S", "N", 0)


def _quad(a, b):  # Quadrat mit scharfen Ecken: schwarze Flaeche, darauf weisse Flaeche
    return [R(a, a, 100 - 2 * a, 100 - 2 * a, "S", "N", 0), R(a + b, a + b, 100 - 2 * (a + b), 100 - 2 * (a + b), "F", "N", 0)]


def st(*sh):  # Standort
    return _quad(4.5, 5) + list(sh)


def kr(*sh):  # Infrastruktur
    return fr_circle() + list(sh)


def fr(*sh):  # Freiraum
    return fr_diamond() + list(sh)


def kz(txt):  # Kategorie-Kennzeichen
    return _quad(22, 5) + [T(txt, 50, 50, 30)]


# ---- Sinnbilder im 100er-Raster ----
FABRIK = [PG([(18, 78), (18, 52), (34, 41), (34, 52), (50, 41), (50, 52), (65, 41), (65, 22), (80, 22), (80, 78)], "S")]
WAGEN = [PL([(15, 27), (26, 27), (35, 60), (72, 60), (79, 37), (29, 37)], 5.5), C(41, 74, 5.5, "S", "N", 0),
         C(67, 74, 5.5, "S", "N", 0)]
DOKTORHUT = [PG([(50, 22), (88, 39), (50, 56), (12, 39)], "S"), P("M30,57 V70 Q50,82 70,70 V57", "N", "S", 5.5),
             L(84, 42, 84, 62, 4)]
KREUZ = [PG([(40, 20), (60, 20), (60, 40), (80, 40), (80, 60), (60, 60), (60, 80), (40, 80), (40, 60), (20, 60),
             (20, 40), (40, 40)], "S")]
BRUNNEN = [P("M22,56 H78 Q74,73 50,73 Q26,73 22,56 Z", "S", "N", 0), L(50, 73, 50, 82, 7, cap="butt"),
           L(34, 84, 66, 84, 5), L(50, 50, 50, 24, 4.5), P("M50,32 Q38,16 29,38", "N", "S", 4.5),
           P("M50,32 Q62,16 71,38", "N", "S", 4.5)]
HALLE = [P("M16,70 Q50,28 84,70 V82 H16 Z", "S", "N", 0), R(43, 64, 14, 18, "F", "N", 0), L(50, 48, 50, 18, 4),
         PG([(50, 17), (70, 24), (50, 31)], "S")]
WINKEL = [PL([(24, 46), (50, 25), (76, 46)], 8.5), PL([(24, 72), (50, 51), (76, 72)], 8.5)]
ANKER = [C(50, 23, 7, "N", "S", 4.5), L(50, 30, 50, 77, 6), L(36, 42, 64, 42, 5),
         P("M25,56 Q28,78 50,78 Q72,78 75,56", "N", "S", 6)]
HAMMER = [L(50, 22, 50, 80, 6.5), R(34, 10, 32, 16, "S", "N", 0, 2)]
BLATT = [P("M24,78 Q18,26 80,20 Q76,80 24,78 Z", "S", "N", 0), L(26, 76, 58, 42, 5, "F")]

S = [
    # ---- Zentrale Orte (konzentrische Kreise, ohne Rahmen) ----
    ("oberzentrum", "Oberzentrum", *SW, zo(ring(43.5), ring(29), kern(14.5))),
    ("mittelzentrum", "Mittelzentrum", *SW, zo(ring(36), kern(19))),
    ("mittelzentrum_teilfunktion", "Mittelzentrum mit Teilfunktionen eines Oberzentrums", *SW,
     zo(ring(44, 4, "9 6.36"), ring(31), kern(16))),
    ("grundzentrum", "Grundzentrum / Unterzentrum", *SW, zo(ring(30), kern(9))),
    ("grundzentrum_teilfunktion", "Grundzentrum mit Teilfunktionen eines Mittelzentrums", *SW,
     zo(ring(40, 4, "9 5.28"), ring(26), kern(8))),
    ("kleinzentrum", "Kleinzentrum", *SW, zo(ring(22))),
    ("doppelzentrum", "Doppelzentrum / Zentren im Verbund", *SW,
     zo(L(30, 50, 70, 50, 9, cap="butt"), C(27, 50, 21.5, "F", "S", 5), C(73, 50, 21.5, "F", "S", 5),
        C(27, 50, 10, "S", "N", 0), C(73, 50, 10, "S", "N", 0))),
    ("siedlungsschwerpunkt", "Siedlungsschwerpunkt", *SW, zo(ring(34), chord(50, 50, 34, 90, 270))),
    ("entwicklungsschwerpunkt", "Entwicklungsschwerpunkt", *SW,
     zo(ring(24), kern(10), *[PG([pt(50, 50, 47, a), pt(50, 50, 33, a - 16), pt(50, 50, 33, a + 16)], "S")
                              for a in (0, 90, 180, 270)])),
    # ---- Standorte (Quadrat) ----
    ("gewerbestandort", "Gewerbe- und Industriestandort, regional bedeutsam", *SW, st(*FABRIK)),
    ("logistikstandort", "Logistikstandort / Güterverkehrszentrum", *SW, st(T("GVZ", 50, 50, 24, maxw=64))),
    ("einzelhandel", "Standort für großflächigen Einzelhandel", *SW, st(*WAGEN)),
    ("hochschule", "Hochschul- und Forschungsstandort", *SW, st(*DOKTORHUT)),
    ("krankenhaus", "Krankenhaus / Gesundheitsstandort", *SW, st(*KREUZ)),
    ("tourismusschwerpunkt", "Tourismusschwerpunkt", *SW,
     st(*sun(50, 40, 12, "S", "S", 4.5, 8, 5, 7), wave(22, 76, 56, 5, 2, 5))),
    ("kurort", "Kurort / Heilbad", *SW, st(*BRUNNEN)),
    ("messe", "Messe- und Kongressstandort", *SW, st(*HALLE)),
    ("militaer", "Militärischer Standort / Konversionsfläche", *SW, st(*WINKEL)),
    # ---- Infrastruktur (Kreis) ----
    ("flughafen", "Flughafen", *SW, kr(*plane(50, 50, 1.08))),
    ("verkehrslandeplatz", "Verkehrslandeplatz", *SW, kr(*plane(50, 43, 0.74), L(30, 77, 70, 77, 5.5))),
    ("hafen", "Hafen", *SW, kr(*ANKER)),
    ("bahnhof_fernverkehr", "Bahnhof des Fernverkehrs", *SW,
     kr(L(8.5, 50, 91.5, 50, 5, cap="butt"), R(27, 35, 46, 30, "S", "S", 5))),
    ("bahnhof_regionalverkehr", "Bahnhof des Regionalverkehrs", *SW,
     kr(L(8.5, 50, 91.5, 50, 5, cap="butt"), R(27, 35, 46, 30, "F", "S", 5))),
    ("anschlussstelle", "Anschlussstelle", *SW,
     kr(PG([(20, 50), (50, 26), (80, 50), (50, 74)], "F", "S", 4.5), L(8.5, 50, 91.5, 50, 9, cap="butt"))),
    ("umspannwerk", "Umspannwerk", *SW,
     kr(L(8.5, 50, 22, 50, 5, cap="butt"), L(78, 50, 91.5, 50, 5, cap="butt"), C(39, 50, 17, "N", "S", 5),
        C(61, 50, 17, "N", "S", 5))),
    ("kraftwerk", "Kraftwerk", *SW, kr(*lightning(50, 50, 1.15))),
    ("windenergie", "Standort Windenergie", *SW, kr(L(50, 44, 50, 84, 5.5), *rotor(50, 42, 27))),
    ("solarenergie", "Standort Solarenergie", *SW,
     kr(PG([(31, 32), (83, 32), (69, 66), (17, 66)], "F", "S", 4.5), L(57, 32, 43, 66, 3.5, cap="butt"),
        L(24, 49, 76, 49, 3.5, cap="butt"), L(50, 66, 50, 80, 5), L(36, 81, 64, 81, 5))),
    ("wasserwerk", "Wasserwerk", *SW, kr(T("WW", 50, 50, 27, maxw=58))),
    ("klaeranlage", "Kläranlage", *SW, kr(C(50, 50, 25, "N", "S", 5), L(25, 50, 75, 50, 4, cap="butt"), kern(7))),
    ("deponie", "Deponie / Abfallbehandlung", *SW,
     kr(PG([(19, 66), (36, 34), (64, 34), (81, 66)], "S", "S", 4))),
    ("rohstoffabbau", "Rohstoffabbau", *SW, kr(*fit(HAMMER, 50, 53, 0.74, 42), *fit(HAMMER, 50, 53, 0.74, -42))),
    # ---- Freiraum (Raute) ----
    ("naturpark", "Naturpark / Großschutzgebiet", *SW, fr(*fit(tree_side("S", "S"), 50, 50, 0.56))),
    ("gruenzug", "Regionaler Grünzug (Hinweis)", *SW, fr(*fit(BLATT, 50, 50, 0.56))),
    ("hochwasserrueckhaltung", "Hochwasserrückhaltung", *SW,
     fr(L(66, 31, 66, 69, 8, cap="butt"), wave(27, 44, 30, 4.5, 2, 4.5), wave(27, 59, 30, 4.5, 2, 4.5))),
    ("trinkwassergewinnung", "Trinkwassergewinnung", *SW, fr(*fit(drop("S", "N", 0), 50, 49, 0.56))),
    # ---- Kategorie-Kennzeichen (kleines Quadrat mit Buchstabe) ----
    ("kennzeichen_ziel", "Kennzeichen Z: Ziel der Raumordnung", *SW, kz("Z")),
    ("kennzeichen_grundsatz", "Kennzeichen G: Grundsatz der Raumordnung", *SW, kz("G")),
    ("kennzeichen_nachrichtlich", "Kennzeichen N: nachrichtliche Übernahme", *SW, kz("N")),
    ("kennzeichen_vorschlag", "Kennzeichen V: Vorschlag", *SW, kz("V")),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
S0, GR, WS = "#000000", "#8C8C8C", "#FFFFFF"
# Flaechenfarben in Anlehnung an die Farbtabelle der NLT-Arbeitshilfe (CMYK-Richtwerte, hier geschaetzt)
GN, GNH = "#009B55", "#B5D334"      # gruen_1, gruen_5: Natur und Landschaft, Freiraumfunktionen
BG, BGD = "#E8CD8F", "#B08A1E"      # beige_3: Landwirtschaft; dunkel fuer Umriss und Schraffur
WA, WAD = "#C3CF6E", "#6E8B1F"      # gruen_8: Wald
RO = "#B2B2B2"                      # grau_2: Rohstoffgewinnung (Umriss schwarz)
BL, BLH = "#0A9FD8", "#BEE3F7"      # blau_1, blau_2: Wasserversorgung
HW, HWH = "#27348B", "#6AA5DA"      # blau_3, blau_4: Hochwasserschutz
EH = "#6FB936"                      # gruen_2: Erholung
RT = "#E6331A"                      # rot_1: Energie
SO = "#F0A000"                      # Solarenergie: eigene Wahl (orange)
SI, SID = "#F29C9B", "#C8504B"      # rot_2: Siedlungsentwicklung
GE, GED = "#BBA3CE", "#8A5AA0"      # violett_2, violett_1: industrielle Anlagen und Gewerbe
AU = "#E0607A"                      # rot_3: Grenze der Ausschlusswirkung
LR, LRD = "#FFF7B2", "#A8A03C"      # laendlicher Raum: eigene Wahl (hellgelb)
ST = [4, 1.5]                       # Strichmuster fuer Vorbehaltsgebiete und Planung

LINIEN = [
    ("Landesgrenze", [linie(S0 + "33", 2.6), linie(S0, 0.9, [6, 1.2, 0.9, 1.2, 0.9, 1.2])]),
    ("Regionsgrenze, Grenze des Planungsraums", [linie(S0 + "33", 1.8), linie(S0, 0.7, [6, 1.2, 0.9, 1.2])]),
    ("Kreisgrenze", [linie(S0, 0.45, [5, 1.2, 0.6, 1.2])]),
    ("Grenze des Verdichtungsraums", [linie(S0, 0.4), marken(mk("triangle", 1.5, S0, dy=0.9), 4)]),
    ("Entwicklungsachse überregional", [linie(GR, 2.4), marken(mk("filled_arrowhead", 3.4, S0), 13)]),
    ("Entwicklungsachse regional", [linie(GR, 1.2), marken(mk("filled_arrowhead", 2.4, S0), 13)]),
    ("Straße regional bedeutsam, Bestand", [linie(S0, 0.4, versatz=0.5), linie(S0, 0.4, versatz=-0.5)]),
    ("Straße regional bedeutsam, Planung", [linie(S0, 0.4, ST, versatz=0.5), linie(S0, 0.4, ST, versatz=-0.5)]),
    ("Schienenstrecke, Bestand", [linie(S0, 0.6), marken(mk("line", 2.2, S0, rw=0.5), 4)]),
    ("Schienenstrecke, Planung", [linie(S0, 0.6, ST), marken(mk("line", 2.2, S0, rw=0.5), 5.5, start=2)]),
    ("Trassenkorridor Leitung", [linie(S0 + "26", 3.2), linie(S0, 0.25, [3, 1.5], versatz=1.6),
                                  linie(S0, 0.25, [3, 1.5], versatz=-1.6)]),
    ("Hochspannungsleitung", [linie(S0, 0.4), marken(mk("circle", 1.4, S0), 8)]),
    ("Grünzäsur", [marken(mk("line", 4.2, GN, rw=0.7), 1.8)]),
    ("Siedlungsbegrenzung", [linie(S0, 0.7), marken(mk("line", 1.8, S0, rw=0.4, dy=0.9), 2)]),
]


def vr_voll(farbe, rand):  # Vorranggebiet mit Vollfarbe
    return [voll(farbe), linie(rand, 0.5)]


def vr_schr(farbe, winkel, rand=None, breite=0.5, abstand=1.8, unter=()):  # Vorranggebiet mit dichter Schraffur
    return list(unter) + [schraffur(farbe, breite, winkel, abstand), linie(rand or farbe, 0.5)]


def vb(farbe, winkel, rand=None, breite=0.5, abstand=4.0):  # Vorbehaltsgebiet: weite Schraffur, Umriss gestrichelt
    return [schraffur(farbe, breite, winkel, abstand), linie(rand or farbe, 0.5, ST)]


FLAECHEN = [
    ("Vorranggebiet Natur und Landschaft", vr_schr(GN, 90)),
    ("Vorbehaltsgebiet Natur und Landschaft", vb(GN, 90)),
    ("Vorranggebiet Landwirtschaft", vr_voll(BG, BGD)),
    ("Vorbehaltsgebiet Landwirtschaft", vb(BGD, 45)),
    ("Vorranggebiet Forstwirtschaft, Wald", vr_voll(WA, WAD)),
    ("Vorbehaltsgebiet Forstwirtschaft, Wald", vb(WAD, 135)),
    ("Vorranggebiet Rohstoffsicherung", vr_schr(RO, 135, S0, unter=[band(RO, 1.2)])),
    ("Vorbehaltsgebiet Rohstoffsicherung", vb(RO, 135, S0)),
    ("Vorranggebiet Wasserwirtschaft, Trinkwasser", vr_schr(BL, 0, unter=[band(BLH, 2.0)])),
    ("Vorbehaltsgebiet Wasserwirtschaft, Trinkwasser", vb(BL, 0)),
    ("Vorranggebiet Hochwasserschutz", vr_schr(HWH, 45, HW, unter=[band(HWH, 1.0)])),
    ("Vorbehaltsgebiet Hochwasserschutz", vb(HWH, 45, HW)),
    ("Vorranggebiet Windenergie", vr_schr(RT, 45, breite=0.35)),
    ("Vorbehaltsgebiet Windenergie", vb(RT, 45, breite=0.35)),
    ("Vorranggebiet Solarenergie", vr_schr(SO, 135)),
    ("Vorbehaltsgebiet Solarenergie", vb(SO, 135)),
    ("Vorranggebiet Erholung, Tourismus", vr_schr(EH, 0, breite=0.7, abstand=2.2)),
    ("Vorbehaltsgebiet Erholung, Tourismus", vb(EH, 0, breite=0.7)),
    ("Vorranggebiet Siedlung (Allgemeiner Siedlungsbereich)", vr_voll(SI, SID)),
    ("Vorbehaltsgebiet Siedlung", vb(SID, 45)),
    ("Vorranggebiet Gewerbe und Industrie", vr_voll(GE, GED)),
    ("Vorbehaltsgebiet Gewerbe und Industrie", vb(GED, 135)),
    ("Regionaler Grünzug", [band(GNH, 2.0), linie(GN, 0.5)]),
    ("Verdichtungsraum", [muster(mk("circle", 0.7, SID), 2.4, versatz=1.2), linie(SID, 0.5)]),
    ("Ländlicher Raum", [voll(LR), linie(LRD, 0.4)]),
    ("Eignungsgebiet", [schraffur(GR, 0.3, 45, 3), linie(S0, 0.6, [5, 1.2, 0.8, 1.2])]),
    ("Ausschlussgebiet", [schraffur(AU, 0.3, 45, 3), schraffur(AU, 0.3, 135, 3), linie(AU, 0.8)]),
]
