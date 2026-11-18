"""Sammlung Allgemein: oeffentliche Einrichtungen, Gesundheit und Rettung, Kultur, topografische
Einzelobjekte, Freizeit, Dienste, dazu runde Punktmarker, freie Formmarker und Standortnadeln.
Orientierung: Objektarten amtlicher topografischer Karten und Stadtplaene (z. B. Kirche, Burg, Bergwerk,
Windmuehle, Aussichtsturm) und gaengige Sinnbilder fuer Orte von Interesse. Die topo_-Zeichen lehnen sich an
die Signaturen topografischer Karten an, sind aber eigene Entwuerfe und keine amtlichen Signaturen.
Stil: weisse Flaeche mit dunklem Sinnbild, Strich 5. Die Form zeigt die Gruppe:
  abgerundetes Quadrat = Einrichtung oder Ort von Interesse, Kreis (kr_) = Punktmarker,
  ohne Rahmen topo_ = topografisches Einzelzeichen, form_/nadel_ = freie Marker (Flaeche = Fuellfarbe,
  Kontur und Sinnbild = Strichfarbe, beide in QGIS aenderbar; Nadelspitze unten bei y = 95).
Die Farbe zeigt das Thema: grau = allgemein, rot = Gesundheit und Rettung, blau = Sicherheit, Auskunft, Dienste.
Linien und Flaechen: grau = Grenzen und Gebaeude, rot = Untersuchungs- und Gefahrenbereiche, blau = Routen
und Einzugsbereiche.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "allgemein"
NAME = "Allgemein"
DESC = ("Allgemeine Kartensymbole: Verwaltung und Bildung, Gesundheit und Rettung, Religion und Kultur, "
        "topografische Einzelobjekte, Freizeit und Tourismus, Dienste und Infrastruktur, dazu topografische "
        "Einzelzeichen ohne Rahmen, runde Punktmarker, Formmarker und Standortnadeln mit änderbaren Farben")
TAGS = ("poi, oeffentliche einrichtungen, infrastruktur, tourismus, topografie, allgemein, punktmarker, marker, "
        "formen, standortnadel, pin")

AG = ("#FFFFFF", "#333333")
RD = ("#FFFFFF", "#C8102E")
PB = ("#FFFFFF", "#1F4E9E")


def aq(*sh):
    return fr_square() + list(sh)


def at(txt, h=30, mw=64):
    return aq(T(txt, 50, 50, h, maxw=mw))


def sl(x1, y1, x2, y2, sw=5, cap="round"):
    return L(x1, y1, x2, y2, sw, "S", cap)


def sf(x, y, w, h, rx=0):
    return R(x, y, w, h, "S", "N", 0, rx)


def wf(x, y, w, h, rx=0):
    return R(x, y, w, h, "F", "N", 0, rx)


HEART = "M50,80 C28,62 20,48 24,36 C28,24 44,24 50,38 C56,24 72,24 76,36 C80,48 72,62 50,80 Z"
HAMMER = [sl(50, 86, 50, 30, 5.5), sf(34, 16, 32, 15, 2)]
PAW = [E(50, 63, 16, 13, "S", "N", 0), C(29, 47, 7, "S", "N", 0), C(42, 33, 7.5, "S", "N", 0),
       C(58, 33, 7.5, "S", "N", 0), C(71, 47, 7, "S", "N", 0)]
MAST = [sl(50, 40, 50, 92), sl(50, 60, 34, 92, 3.5), sl(50, 60, 66, 92, 3.5), C(50, 34, 6, "S", "N", 0),
        arc(50, 34, 21, 229, 311, 4.5), arc(50, 34, 21, 49, 131, 4.5), arc(50, 34, 36, 229, 311, 4.5), arc(50, 34, 36, 49, 131, 4.5)]
TOWER = [PG([(42, 86), (58, 86), (55, 42), (45, 42)], "S")]


def merlons(x):
    return [sf(x, 36, 18, 48), sf(x, 27, 5, 9), sf(x + 6.5, 27, 5, 9), sf(x + 13, 27, 5, 9)]


def kq(*sh):  # Punktmarker im Kreis
    return [C(50, 50, 43, "F", "S", 5)] + list(sh)


def kt(txt, h=30, mw=58):
    return kq(T(txt, 50, 50, h, maxw=mw))


def fm(pts, sw=6):  # Formmarker: Flaeche in der Fuellfarbe, Kontur in der Strichfarbe
    return [PG(pts, "F", "S", sw)]


PIN = "M50,95 C32,64 18,52 18,37 C18,19 32,5 50,5 C68,5 82,19 82,37 C82,52 68,64 50,95 Z"


def nd(*sh):  # Standortnadel, Spitze unten
    return [P(PIN, "F", "S", 5)] + list(sh)


SHIELD = "M50,14 L80,24 V50 C80,68 66,80 50,88 C34,80 20,68 20,50 V24 Z"
PLUS = [(38, 12), (62, 12), (62, 38), (88, 38), (88, 62), (62, 62), (62, 88), (38, 88), (38, 62), (12, 62),
        (12, 38), (38, 38)]
RING = ("M50,10 A40,40 0 1 1 50,90 A40,40 0 1 1 50,10 Z "
        "M50,31 A19,19 0 1 0 50,69 A19,19 0 1 0 50,31 Z")


S = [
    # ---- Verwaltung und Bildung ----
    ("rathaus", "Rathaus / Verwaltung", *AG,
     aq(sf(24, 48, 52, 34), sf(41, 28, 18, 20), sl(50, 28, 50, 14, 3.5), PG([(50, 14), (66, 18), (50, 23)], "S"),
        wf(31, 56, 8, 10), wf(61, 56, 8, 10), wf(45, 62, 10, 20))),
    ("gericht", "Gericht / Justiz", *AG,
     aq(sl(50, 20, 50, 78, 4.5), sl(26, 28, 74, 28, 4.5), sl(34, 80, 66, 80, 5.5), sl(28, 28, 18, 52, 3), sl(28, 28, 38, 52, 3),
        sl(72, 28, 62, 52, 3), sl(72, 28, 82, 52, 3), P("M15,52 A13,12 0 0 0 41,52 Z", "S", "N", 0),
        P("M59,52 A13,12 0 0 0 85,52 Z", "S", "N", 0))),
    ("schule", "Schule", *AG,
     aq(P("M50,34 Q34,22 16,28 V72 Q34,66 50,78 Q66,66 84,72 V28 Q66,22 50,34 Z", "N", "S", 5), sl(50, 34, 50, 78, 4.5))),
    ("hochschule", "Hochschule / Universität", *AG,
     aq(PG([(50, 24), (88, 40), (50, 56), (12, 40)], "S"), P("M30,52 V66 Q50,80 70,66 V52", "N", "S", 5), sl(82, 42, 82, 64, 3.5),
        C(82, 66, 4, "S", "N", 0))),
    ("kindertagesstaette", "Kindertagesstätte", *AG, at("Kita", 24, 66)),
    ("bibliothek", "Bibliothek / Archiv", *AG,
     aq(sf(22, 26, 13, 52, 2), sf(39, 20, 13, 58, 2), PG(rot([(-6.5, -27), (6.5, -27), (6.5, 27), (-6.5, 27)], 18, 68, 52), "S"),
        sl(16, 82, 84, 82, 5))),
    ("post", "Post / Postfiliale", *AG, aq(R(16, 28, 68, 44, "N", "S", 5, 3), PL([(17, 31), (50, 56), (83, 31)], 4.5))),
    ("bank", "Bank / Geldautomat", *AG, at("€", 44)),
    # ---- Gesundheit und Rettung (rot), Sicherheit (blau) ----
    ("krankenhaus", "Krankenhaus", *RD, aq(sf(40, 20, 20, 60, 2), sf(20, 40, 60, 20, 2))),
    ("arzt", "Arztpraxis / Gesundheitszentrum", *RD,
     aq(sl(50, 14, 50, 86, 5.5), P("M50,24 Q70,30 50,40 Q30,50 50,58 Q68,64 50,74", "N", "S", 4.5), C(50, 14, 4, "S", "N", 0))),
    ("apotheke", "Apotheke", *RD,
     aq(*fit([R(18, 36, 64, 28, "F", "S", 5, 14), P("M50,36 H68 A14,14 0 0 1 68,64 H50 Z", "S", "N", 0)], 50, 50, 1.0, -35))),
    ("pflegeeinrichtung", "Pflegeeinrichtung / Seniorenheim", *RD,
     aq(PL([(18, 48), (50, 18), (82, 48)], 5), R(26, 48, 48, 34, "N", "S", 5), *fit([P(HEART, "S", "N", 0)], 50, 64, 0.42))),
    ("tierarzt", "Tierarzt / Tierheim", *RD, aq(*fit(PAW, 46, 54, 0.82), sl(72, 18, 72, 34, 5, "butt"), sl(64, 26, 80, 26, 5, "butt"))),
    ("rettungswache", "Rettungswache / Rettungsdienst", *RD,
     aq(P("M14,68 V38 Q14,34 18,34 H62 V68 Z", "S", "N", 0), P("M62,44 H74 L86,56 V68 H62 Z", "S", "N", 0),
        wf(34, 40, 8, 22), wf(27, 47, 22, 8), C(30, 70, 8, "S", "F", 4), C(70, 70, 8, "S", "F", 4))),
    ("defibrillator", "Defibrillator (AED)", *RD, aq(P(HEART, "S", "N", 0), *lightning(50, 50, 0.52, "F"))),
    ("notruf", "Notruf / Notrufeinrichtung", *RD, at("112", 28, 66)),
    ("feuerwehr", "Feuerwehr", *RD, aq(*fit(flame("S", "F"), 50, 50, 0.9))),
    ("polizei", "Polizei", *PB,
     aq(P("M50,14 L80,24 V50 C80,68 66,80 50,88 C34,80 20,68 20,50 V24 Z", "N", "S", 5), PG(star(50, 50, 17, 7, 5), "S"))),
    # ---- Religion und Kultur ----
    ("kirche", "Kirche", *AG, aq(sf(44, 16, 12, 68), sf(27, 33, 46, 12))),
    ("kapelle", "Kapelle", *AG,
     aq(sl(50, 14, 50, 36, 4.5), sl(42, 22, 58, 22, 4.5), PL([(22, 60), (50, 36), (78, 60)], 5), R(30, 60, 40, 24, "N", "S", 5),
        P("M44,84 V72 A6,6 0 0 1 56,72 V84 Z", "S", "N", 0))),
    ("moschee", "Moschee", *AG,
     aq(P("M22,84 V62 A20,20 0 0 1 62,62 V84 Z", "S", "N", 0), sf(68, 38, 10, 46), PG([(66, 38), (80, 38), (73, 22)], "S"),
        C(42, 28, 9, "S", "N", 0), C(46, 26, 7.5, "F", "N", 0))),
    ("synagoge", "Synagoge", *AG,
     aq(PG(regpoly(50, 50, 32, 3, -90), "N", "S", 4.5), PG(regpoly(50, 50, 32, 3, 90), "N", "S", 4.5))),
    ("friedhof", "Friedhof", *AG,
     aq(P("M33,80 V44 A17,17 0 0 1 67,44 V80", "N", "S", 5), sl(18, 82, 82, 82, 5), sl(50, 40, 50, 66, 4.5, "butt"),
        sl(41, 49, 59, 49, 4.5, "butt"))),
    ("museum", "Museum", *AG,
     aq(PG([(50, 16), (84, 38), (16, 38)], "S"), *[sf(x, 42, 8, 28) for x in (24, 39, 53, 68)], sf(18, 74, 64, 9))),
    ("theater", "Theater / Kulturzentrum", *AG,
     aq(P("M26,24 Q50,34 74,24 V52 Q74,80 50,84 Q26,80 26,52 Z", "S", "N", 0), E(40, 48, 7, 4.5, "F", "N", 0),
        E(60, 48, 7, 4.5, "F", "N", 0), P("M36,62 Q50,76 64,62 Q50,68 36,62 Z", "F", "N", 0))),
    ("denkmal", "Denkmal / Kulturdenkmal", *AG,
     aq(PG([(43, 28), (57, 28), (61, 72), (39, 72)], "S"), PG([(43, 28), (50, 14), (57, 28)], "S"), sf(28, 74, 44, 10))),
    ("burg_schloss", "Burg / Schloss", *AG,
     aq(*merlons(16), *merlons(66), sf(34, 52, 32, 32), P("M43,84 V70 A7,7 0 0 1 57,70 V84 Z", "F", "N", 0))),
    ("ruine", "Ruine", *AG,
     aq(PG([(26, 84), (26, 32), (36, 32), (36, 42), (46, 42), (46, 30), (56, 40), (60, 54), (74, 60), (74, 84)], "S"),
        P("M42,84 V70 A7,7 0 0 1 56,70 V84 Z", "F", "N", 0))),
    ("sehenswuerdigkeit", "Sehenswürdigkeit", *AG, aq(PG(star(50, 53, 36, 15, 5), "S"))),
    # ---- Topografische Einzelobjekte ----
    ("aussichtsturm", "Aussichtsturm", *AG,
     aq(sl(38, 84, 44, 40), sl(62, 84, 56, 40), sl(40, 70, 59, 56, 3.5), sl(60, 70, 41, 56, 3.5), sf(30, 30, 40, 10),
        PG([(30, 26), (50, 12), (70, 26)], "S"))),
    ("funkmast", "Funkmast / Sendeanlage", *AG, aq(*fit(MAST, 50, 46, 0.8))),
    ("windmuehle", "Windmühle", *AG,
     aq(PG([(41, 86), (59, 86), (55, 46), (45, 46)], "S"), sl(26, 16, 74, 64, 5), sl(74, 16, 26, 64, 5), C(50, 40, 6, "S", "N", 0))),
    ("wassermuehle", "Wassermühle", *AG,
     aq(*gear(50, 44, 30, 10, "S", 15, "F"), C(50, 44, 5, "S", "N", 0), wave(18, 84, 64, 4, 3, 4.5))),
    ("bergwerk", "Bergwerk / Tagebau", *AG, aq(*fit(HAMMER, 50, 54, 0.84, 40), *fit(HAMMER, 50, 54, 0.84, -40))),
    ("hoehle", "Höhle", *AG,
     aq(P("M16,82 Q18,28 50,24 Q82,28 84,82 Z", "S", "N", 0), P("M36,82 Q38,52 50,50 Q62,52 64,82 Z", "F", "N", 0))),
    ("leuchtturm", "Leuchtturm", *AG,
     aq(*TOWER, R(43, 28, 14, 14, "N", "S", 4), PG([(39, 28), (61, 28), (50, 16)], "S"), sl(66, 32, 84, 26, 4), sl(66, 39, 84, 44, 4),
        sl(34, 32, 16, 26, 4), sl(34, 39, 16, 44, 4), L(44.4, 56, 55.6, 56, 6, "F", "butt"), L(43.4, 71, 56.6, 71, 6, "F", "butt"))),
    ("gipfel", "Berggipfel / Gipfelkreuz", *AG,
     aq(PL([(14, 82), (40, 38), (52, 58), (62, 46), (86, 82)], 5, close=True), sl(40, 38, 40, 18, 4.5), sl(32, 25, 48, 25, 4.5))),
    # ---- Freizeit und Tourismus ----
    ("information", "Information / Tourist-Information", *PB, aq(C(50, 26, 7.5, "S", "N", 0), sf(43, 40, 14, 40, 3))),
    ("hotel", "Hotel / Unterkunft", *AG,
     aq(sl(16, 28, 16, 76, 6), sl(16, 64, 84, 64, 6), sl(84, 52, 84, 76, 6), C(30, 48, 8, "S", "N", 0), sf(42, 44, 42, 14, 5))),
    ("jugendherberge", "Jugendherberge / Gruppenunterkunft", *AG, at("JH", 32, 60)),
    ("campingplatz", "Campingplatz", *AG,
     aq(PG([(50, 22), (84, 78), (16, 78)], "N", "S", 5), PG([(50, 50), (62, 78), (38, 78)], "S"), sl(50, 22, 44, 14, 4),
        sl(50, 22, 56, 14, 4))),
    ("gastronomie", "Gastronomie", *AG,
     aq(sl(34, 20, 34, 82), sl(25, 20, 25, 38, 4), sl(43, 20, 43, 38, 4), P("M25,38 Q34,50 43,38", "N", "S", 4),
        P("M62,18 Q76,30 74,54 H62 Z", "S", "S", 3), sl(64, 54, 64, 82))),
    ("cafe", "Café", *AG,
     aq(sf(24, 42, 38, 32, 7), P("M62,48 H69 Q78,48 78,57 Q78,66 69,66 H62", "N", "S", 5), sl(16, 84, 76, 84),
        P("M36,32 q4,-6 0,-12", "N", "S", 4), P("M50,32 q4,-6 0,-12", "N", "S", 4))),
    ("einkauf", "Einkauf / Nahversorgung", *AG,
     aq(PL([(14, 24), (26, 24), (36, 60), (74, 60), (82, 34), (29, 34)], 5), C(42, 74, 6, "S", "N", 0), C(68, 74, 6, "S", "N", 0))),
    ("markt", "Markt / Wochenmarkt", *AG,
     aq(P("M16,42 L24,22 H76 L84,42 Z", "S", "N", 0), sl(24, 44, 24, 84), sl(76, 44, 76, 84), sf(24, 60, 52, 9))),
    ("sportanlage", "Sportanlage / Sportplatz", *AG,
     aq(R(16, 28, 68, 44, "N", "S", 5, 22), sl(50, 28, 50, 72, 4), C(50, 50, 8, "N", "S", 4))),
    ("sporthalle", "Sporthalle", *AG, aq(P("M16,80 V54 Q50,18 84,54 V80 Z", "N", "S", 5), C(50, 62, 10, "S", "N", 0))),
    ("schwimmbad", "Schwimmbad / Freibad", *PB, aq(*fit(swimmer(), 50, 52, 0.84))),
    ("spielplatz", "Spielplatz", *AG,
     aq(sl(18, 24, 82, 24, 5.5), sl(24, 24, 16, 84), sl(76, 24, 84, 84), sl(41, 24, 41, 64, 3.5), sl(59, 24, 59, 64, 3.5),
        sl(37, 64, 63, 64, 6.5))),
    ("park", "Park / Grünanlage", *AG, aq(*fit(tree_side(), 50, 46, 0.8), sl(20, 84, 80, 84, 5))),
    # ---- Dienste und Infrastruktur ----
    ("toilette", "Öffentliche Toilette", *PB, at("WC", 30, 64)),
    ("wlan", "WLAN / Hotspot", *PB,
     aq(C(50, 76, 6, "S", "N", 0), arc(50, 76, 18, -45, 45, 5.5), arc(50, 76, 32, -45, 45, 5.5), arc(50, 76, 46, -45, 45, 5.5))),
    ("briefkasten", "Briefkasten", *AG, aq(sf(22, 20, 56, 38, 8), L(32, 34, 68, 34, 5, "F", "butt"), sl(50, 58, 50, 86, 7, "butt"))),
    ("paketstation", "Paketstation", *AG,
     aq(R(20, 30, 60, 50, "N", "S", 5, 3), sl(50, 30, 50, 80, 4.5, "butt"), sl(20, 48, 80, 48, 4.5, "butt"))),
    ("wertstoffhof", "Wertstoffhof / Entsorgung", *AG,
     aq(PG([(26, 36), (74, 36), (68, 82), (32, 82)], "N", "S", 5), sl(18, 30, 82, 30, 6), sl(42, 22, 58, 22, 6),
        sl(42, 46, 44, 72, 4), sl(58, 46, 56, 72, 4))),
    ("altglascontainer", "Altglas- / Wertstoffcontainer", *AG,
     aq(P("M44,14 H56 V30 Q66,38 66,50 V84 H34 V50 Q34,38 44,30 Z", "S", "N", 0), wf(34, 56, 32, 14))),
    ("bauhof", "Bauhof / Betriebshof", *AG, aq(*gear(50, 50, 34, 8, "S", 12, "F"))),
    # ---- Weitere Einrichtungen und Orte (Quadrat) ----
    ("buergerhaus", "Bürgerhaus / Gemeindezentrum", *AG,
     aq(PL([(16, 46), (50, 16), (84, 46)], 5), R(24, 46, 52, 38, "N", "S", 5), C(39, 58, 5.5, "S", "N", 0),
        C(61, 58, 5.5, "S", "N", 0), P("M31,82 V74 Q31,66 39,66 Q47,66 47,74 V82 Z", "S", "N", 0),
        P("M53,82 V74 Q53,66 61,66 Q69,66 69,74 V82 Z", "S", "N", 0))),
    ("buergerbuero", "Bürgerbüro / Bürgerservice", *PB,
     aq(C(50, 30, 10, "S", "N", 0), P("M30,62 V58 Q30,44 50,44 Q70,44 70,58 V62 Z", "S", "N", 0), sf(16, 66, 68, 12, 2))),
    ("standesamt", "Standesamt", *AG,
     aq(C(38, 56, 17, "N", "S", 5), C(62, 56, 17, "N", "S", 5), *fit([P(HEART, "S", "N", 0)], 50, 25, 0.3))),
    ("seniorentreff", "Seniorentreff / Begegnungsstätte", *AG,
     aq(C(44, 24, 8, "S", "N", 0), PL([(44, 38), (46, 58)], 9), PL([(46, 58), (39, 84)], 6.5), PL([(46, 58), (55, 84)], 6.5),
        PL([(45, 41), (58, 51), (67, 52)], 5), sl(67, 50, 67, 84, 4))),
    ("zoll", "Zoll", *PB, at("ZOLL", 20, 64)),
    ("justizvollzugsanstalt", "Justizvollzugsanstalt", *PB,
     aq(R(20, 20, 60, 60, "N", "S", 5, 3), sl(35, 20, 35, 80, 4.5, "butt"), sl(50, 20, 50, 80, 4.5, "butt"),
        sl(65, 20, 65, 80, 4.5, "butt"))),
    ("kaserne", "Kaserne / Militärische Einrichtung", *AG,
     aq(PL([(26, 42), (50, 24), (74, 42)], 7), PL([(26, 60), (50, 42), (74, 60)], 7), PL([(26, 78), (50, 60), (74, 78)], 7))),
    ("forschung", "Forschung / Labor", *AG,
     aq(PG([(33, 60), (67, 60), (76, 80), (24, 80)], "S"),
        P("M42,20 V40 L23,76 Q20,84 28,84 H72 Q80,84 77,76 L58,40 V20", "N", "S", 5), sl(37, 20, 63, 20, 5))),
    ("industrie", "Industrie / Fabrik", *AG,
     aq(PG([(14, 84), (14, 56), (32, 44), (32, 56), (50, 44), (50, 56), (66, 56), (66, 84)], "S"), sf(66, 20, 14, 64),
        wf(22, 66, 8, 9), wf(40, 66, 8, 9))),
    ("lager", "Lager / Logistik", *AG,
     aq(R(17, 54, 31, 28, "N", "S", 4.5), R(52, 54, 31, 28, "N", "S", 4.5), R(34.5, 22, 31, 28, "N", "S", 4.5),
        sl(32.5, 54, 32.5, 65, 4, "butt"), sl(67.5, 54, 67.5, 65, 4, "butt"), sl(50, 22, 50, 33, 4, "butt"))),
    ("stadion", "Stadion / Arena", *AG,
     aq(E(50, 50, 37, 28, "N", "S", 5), sf(35, 41, 30, 18, 3), sl(50, 22, 50, 32, 3.5, "butt"),
        sl(50, 68, 50, 78, 3.5, "butt"), sl(13, 50, 26, 50, 3.5, "butt"), sl(74, 50, 87, 50, 3.5, "butt"))),
    ("kino", "Kino", *AG,
     aq(C(50, 47, 30, "S", "N", 0), *[C(x, y, 6.5, "F", "N", 0) for x, y in regpoly(50, 47, 17, 5)], C(50, 47, 4, "F", "N", 0),
        P("M50,77 Q74,80 84,70", "N", "S", 5))),
    ("veranstaltungshalle", "Veranstaltungshalle / Konzert", *AG,
     aq(E(34, 72, 10, 7.5, "S", "N", 0), E(66, 64, 10, 7.5, "S", "N", 0), sl(41.5, 72, 41.5, 28, 5, "butt"),
        sl(73.5, 64, 73.5, 20, 5, "butt"), PG([(39, 22), (76, 14), (76, 27), (39, 35)], "S"))),
    ("zoo", "Zoo / Tierpark", *AG,
     aq(E(44, 52, 24, 17, "S", "N", 0), C(68, 44, 13, "S", "N", 0), P("M78,46 Q86,58 80,74", "N", "S", 6), sf(26, 60, 10, 24, 2),
        sf(48, 60, 10, 24, 2), E(63, 44, 5, 8.5, "F", "N", 0), sl(21, 48, 15, 60, 3.5))),
    ("botanischer_garten", "Botanischer Garten", *AG,
     aq(sl(50, 50, 50, 84, 4.5), *[C(x, y, 8.5, "S", "N", 0) for x, y in regpoly(50, 32, 13, 5)], C(50, 32, 6, "F", "N", 0),
        P("M50,78 Q34,76 30,60 Q46,62 50,78 Z", "S", "N", 0), P("M50,70 Q66,68 70,52 Q54,54 50,70 Z", "S", "N", 0))),
    ("hundewiese", "Hundewiese / Hundeauslauf", *AG,
     aq(sf(26, 46, 42, 17, 7), sf(28, 56, 8, 26, 3), sf(58, 56, 8, 26, 3),
        PG([(58, 50), (62, 30), (72, 24), (76, 32), (88, 38), (86, 45), (72, 46), (70, 56)], "S"), sl(28, 50, 18, 34, 5))),
    ("grillplatz", "Grillplatz", *AG,
     aq(P("M22,48 A28,26 0 0 0 78,48 Z", "S", "N", 0), sl(38, 70, 30, 86, 4.5), sl(62, 70, 70, 86, 4.5),
        *[P(f"M{x},38 q5,-7 0,-14", "N", "S", 4) for x in (36, 50, 64)])),
    ("sitzbank", "Sitzbank / Rastplatz", *AG,
     aq(sf(18, 28, 64, 8, 2), sf(18, 41, 64, 8, 2), sf(14, 56, 72, 9, 2), sl(24, 65, 24, 84, 5), sl(76, 65, 76, 84, 5),
        sl(27, 32, 27, 58, 4), sl(73, 32, 73, 58, 4))),
    ("trinkbrunnen", "Trinkbrunnen / Trinkwasser", *PB,
     aq(P("M18,38 H58 Q70,38 70,50 V56", "N", "S", 10, "butt"), sl(40, 36, 40, 22, 5), sl(30, 20, 50, 20, 6),
        *fit(drop("S", "N", 0), 70, 74, 0.28))),
    ("telefon", "Öffentliches Telefon", *PB,
     aq(P("M22,46 Q50,14 78,46", "N", "S", 9), sf(11, 40, 22, 17, 5), sf(67, 40, 22, 17, 5),
        PG([(30, 84), (70, 84), (63, 60), (37, 60)], "S", "S", 4), C(50, 72, 5.5, "F", "N", 0))),
    # ---- Topografische Einzelzeichen (ohne Rahmen) ----
    ("topo_kirche", "Topografie: Kirche", *AG,
     [L(50, 42, 50, 9, 6, cap="butt"), L(36, 22, 64, 22, 6, cap="butt"), C(50, 66, 24, "F", "S", 6)]),
    ("topo_kapelle", "Topografie: Kapelle", *AG,
     [L(50, 60, 50, 14, 6, cap="butt"), L(37, 29, 63, 29, 6, cap="butt"), C(50, 70, 15, "S", "N", 0)]),
    ("topo_wegkreuz", "Topografie: Wegkreuz / Bildstock", *AG,
     [L(50, 82, 50, 9, 7, cap="butt"), L(30, 30, 70, 30, 7, cap="butt"), sf(31, 80, 38, 12, 2)]),
    ("topo_gipfelkreuz", "Topografie: Gipfel mit Gipfelkreuz", *AG,
     [PL([(8, 90), (50, 46), (92, 90)], 6), L(50, 46, 50, 8, 5.5, cap="butt"), L(37, 20, 63, 20, 5.5, cap="butt")]),
    ("topo_turm", "Topografie: Turm", *AG,
     [PG([(37, 92), (63, 92), (59, 30), (41, 30)], "S"), sf(33, 18, 34, 14), sf(33, 8, 8, 11), sf(46, 8, 8, 11), sf(59, 8, 8, 11)]),
    ("topo_burg", "Topografie: Burg / Schloss", *AG,
     [sf(22, 46, 56, 46), sf(22, 32, 12, 15), sf(44, 32, 12, 15), sf(66, 32, 12, 15), sl(50, 32, 50, 8, 4),
      PG([(50, 7), (70, 13), (50, 20)], "S"), P("M41,92 V74 A9,9 0 0 1 59,74 V92 Z", "F", "N", 0)]),
    ("topo_ruine", "Topografie: Ruine", *AG,
     [PG([(16, 90), (16, 22), (31, 22), (31, 38), (45, 38), (45, 20), (60, 36), (64, 58), (84, 64), (84, 90)], "F", "S", 5.5),
      sl(30, 60, 44, 60, 4), sl(40, 74, 54, 74, 4)]),
    ("topo_schornstein", "Topografie: Schornstein", *AG,
     [PG([(34, 92), (66, 92), (59, 36), (41, 36)], "S"), P("M50,28 C36,20 64,16 52,5", "N", "S", 6)]),
    ("topo_windrad", "Topografie: Windrad / Windenergieanlage", *AG,
     [L(50, 92, 50, 40, 6, cap="butt"), sl(38, 92, 62, 92, 5), *rotor(50, 40, 36)]),
    ("topo_windmuehle", "Topografie: Windmühle", *AG,
     [PG([(37, 92), (63, 92), (57, 50), (43, 50)], "S"), sl(20, 12, 80, 72, 5.5), sl(80, 12, 20, 72, 5.5),
      C(50, 42, 7, "S", "N", 0)]),
    ("topo_bergwerk", "Topografie: Bergwerk, in Betrieb", *AG, fit(HAMMER, 50, 52, 1.1, 40) + fit(HAMMER, 50, 52, 1.1, -40)),
    ("topo_bergwerk_stillgelegt", "Topografie: Bergwerk, stillgelegt", *AG,
     fit(HAMMER, 50, 48, 1.1, 140) + fit(HAMMER, 50, 48, 1.1, -140)),
    ("topo_steinbruch", "Topografie: Steinbruch / Grube", *AG,
     [arc(50, 100, 58, -50, 50, 6.5)] + [L(*pt(50, 100, 58, a), *pt(50, 100, 30, a), 5.5) for a in (-36, -18, 0, 18, 36)]),
    ("topo_fels", "Topografie: Fels / Felsgruppe", *AG,
     [PG([(8, 88), (25, 46), (38, 58), (54, 16), (71, 52), (80, 44), (92, 88)], "F", "S", 5.5),
      PL([(54, 16), (50, 50), (60, 70)], 4)]),
    ("topo_grenzstein", "Topografie: Grenzstein", *AG,
     [PG([(35, 90), (35, 30), (50, 14), (65, 30), (65, 90)], "F", "S", 5.5), sl(50, 40, 50, 62, 4.5, "butt"),
      sl(39, 51, 61, 51, 4.5, "butt"), sl(16, 90, 84, 90, 5.5)]),
    ("topo_quelle", "Topografie: Quelle", *AG,
     [wave(40, 50, 52, 9, 2, 6), C(26, 50, 17, "F", "S", 6)]),
    ("topo_brunnen", "Topografie: Brunnen", *AG,
     [sl(30, 60, 30, 28), sl(70, 60, 70, 28), PL([(18, 32), (50, 10), (82, 32)], 5.5), sl(50, 22, 50, 40, 3.5),
      sf(43, 40, 14, 11, 2), R(22, 60, 56, 30, "F", "S", 5.5)]),
    ("topo_laubbaum", "Topografie: Laubbaum (Ansicht)", *AG, tree_side() + [sl(34, 91, 66, 91, 5)]),
    ("topo_nadelbaum", "Topografie: Nadelbaum (Ansicht)", *AG, conifer_side() + [sl(34, 92, 66, 92, 5)]),
    ("topo_einzelbaum", "Topografie: markanter Einzelbaum / Naturdenkmal", *AG,
     [L(50, 60, 50, 90, 9, cap="butt"), sl(24, 91, 76, 91, 5.5)] + treetop(50, 37, 27, "F", "S", 5.5, 7)),
    ("topo_schutzhuette", "Topografie: Schutzhütte / Unterstand", *AG,
     [sl(24, 48, 24, 90, 5.5), sl(76, 48, 76, 90, 5.5), PL([(10, 52), (50, 18), (90, 52)], 6.5), sf(33, 68, 34, 8, 2),
      sl(38, 76, 38, 90, 4), sl(62, 76, 62, 90, 4)]),
    ("topo_wegweiser", "Topografie: Wegweiser", *AG,
     [L(50, 93, 50, 8, 6, cap="butt"), PG([(50, 16), (78, 16), (89, 26), (78, 36), (50, 36)], "F", "S", 5),
      PG([(50, 46), (22, 46), (11, 56), (22, 66), (50, 66)], "F", "S", 5)]),
    # ---- Punktmarker (Kreis) ----
    ("kr_information", "Punktmarker: Information", *PB, kq(C(50, 27, 7.5, "S", "N", 0), sf(43, 41, 14, 37, 3))),
    ("kr_achtung", "Punktmarker: Achtung", *RD, kq(L(50, 22, 50, 56, 10), C(50, 74, 6.5, "S", "N", 0))),
    ("kr_frage", "Punktmarker: Frage / Klärungsbedarf", *PB, kt("?", 48)),
    ("kr_start", "Punktmarker: Start", *AG, kq(PG([(38, 27), (76, 50), (38, 73)], "S", "S", 4))),
    ("kr_ziel", "Punktmarker: Ziel (Zielflagge)", *AG,
     kq(sl(29, 22, 29, 80, 5), R(31, 24, 45, 30, "N", "S", 3.5), sf(31, 24, 15, 15), sf(61, 24, 15, 15), sf(46, 39, 15, 15))),
    ("kr_treffpunkt", "Punktmarker: Treffpunkt / Sammelstelle", *AG,
     kq(*arrow(24, 24, 41, 41, 5.5, 13), *arrow(76, 24, 59, 41, 5.5, 13), *arrow(24, 76, 41, 59, 5.5, 13),
        *arrow(76, 76, 59, 59, 5.5, 13), C(50, 50, 5.5, "S", "N", 0))),
    ("kr_standort", "Punktmarker: Standort / Sie sind hier", *AG,
     kq(*fit([P(PIN, "S", "N", 0), C(50, 37, 12, "F", "N", 0)], 50, 51, 0.66))),
    ("kr_foto", "Punktmarker: Foto / Fotopunkt", *AG,
     kq(sf(38, 26, 24, 12, 3), sf(20, 34, 60, 40, 6), C(50, 54, 13, "F", "N", 0), C(50, 54, 6, "S", "N", 0))),
    ("kr_aussicht", "Punktmarker: Aussicht / Aussichtspunkt", *AG, kq(*fit(eye(), 50, 50, 0.78))),
    ("kr_parken", "Punktmarker: Parken", *PB, kt("P", 46)),
    ("kr_wc", "Punktmarker: WC", *PB, kt("WC", 28, 58)),
    ("kr_notruf", "Punktmarker: Notruf", *RD, kt("SOS", 24, 60)),
    ("kr_erste_hilfe", "Punktmarker: Erste Hilfe", *RD, kq(sf(41, 22, 18, 56, 2), sf(22, 41, 56, 18, 2))),
    ("kr_polizei", "Punktmarker: Polizei", *PB,
     kq(*fit([P(SHIELD, "N", "S", 6.5), PG(star(50, 50, 17, 7, 5), "S")], 50, 50, 0.76))),
    # ---- Formmarker (Flaeche in der Fuellfarbe, Kontur in der Strichfarbe) ----
    ("form_kreis", "Formmarker: Kreis", *AG, [C(50, 50, 40, "F", "S", 6)]),
    ("form_ring", "Formmarker: Ring", *AG, [P(RING, "F", "S", 5)]),
    ("form_zielscheibe", "Formmarker: Zielscheibe", *AG,
     [C(50, 50, 41, "F", "S", 5), C(50, 50, 24, "N", "S", 5), C(50, 50, 8, "S", "N", 0)]),
    ("form_quadrat", "Formmarker: Quadrat", *AG, [R(13, 13, 74, 74, "F", "S", 6)]),
    ("form_raute", "Formmarker: Raute", *AG, fm([(50, 7), (93, 50), (50, 93), (7, 50)])),
    ("form_dreieck", "Formmarker: Dreieck", *AG, fm([(50, 10), (93, 85), (7, 85)])),
    ("form_dreieck_spitze", "Formmarker: Dreieck auf der Spitze", *AG, fm([(7, 15), (93, 15), (50, 90)])),
    ("form_fuenfeck", "Formmarker: Fünfeck", *AG, fm(regpoly(50, 53, 44, 5))),
    ("form_sechseck", "Formmarker: Sechseck", *AG, fm(regpoly(50, 50, 44, 6, 0))),
    ("form_stern", "Formmarker: Stern", *AG, fm(star(50, 54, 46, 19, 5), 5)),
    ("form_kreuz", "Formmarker: Kreuz / Plus", *AG, fm(PLUS, 5)),
    ("form_schraegkreuz", "Formmarker: Schrägkreuz", *AG, fm(rot(mv(PLUS, -50, -50), 45, 50, 50), 5)),
    ("form_herz", "Formmarker: Herz", *AG, fit([P(HEART, "F", "S", 4)], 50, 46, 1.45)),
    ("form_tropfen", "Formmarker: Tropfen", *AG, drop("F", "S", 6)),
    ("form_flagge", "Formmarker: Flagge", *AG,
     [P("M24,13 H86 L72,32 L86,51 H24 Z", "F", "S", 5), L(24, 8, 24, 93, 6)]),
    ("form_haus", "Formmarker: Haus", *AG, fm([(50, 9), (92, 46), (79, 46), (79, 89), (21, 89), (21, 46), (8, 46)])),
    # ---- Standortnadeln (Spitze unten) ----
    ("nadel_leer", "Standortnadel, leer", *AG, nd()),
    ("nadel_punkt", "Standortnadel mit Punkt", *AG, nd(C(50, 37, 12, "S", "N", 0))),
    ("nadel_stern", "Standortnadel mit Stern", *AG, nd(PG(star(50, 38, 21, 9, 5), "S"))),
    ("nadel_haus", "Standortnadel mit Haus", *AG,
     nd(PG([(50, 19), (71, 38), (64, 38), (64, 53), (36, 53), (36, 38), (29, 38)], "S"))),
    ("nadel_kreuz", "Standortnadel mit Kreuz", *AG, nd(sf(44, 19, 12, 36, 1.5), sf(32, 31, 36, 12, 1.5))),
    ("nadel_info", "Standortnadel mit i (Information)", *AG, nd(C(50, 21, 6, "S", "N", 0), sf(44.5, 31, 11, 25, 2))),
    ("nadel_achtung", "Standortnadel mit Ausrufezeichen", *AG, nd(L(50, 20, 50, 40, 8.5), C(50, 54, 5.5, "S", "N", 0))),
    ("nadel_person", "Standortnadel mit Person", *AG,
     nd(C(50, 25, 8, "S", "N", 0), P("M35,56 V48 Q35,37 50,37 Q65,37 65,48 V56 Z", "S", "N", 0))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
A0, R0, P0 = AG[1], RD[1], PB[1]

LINIEN = [
    ("Staatsgrenze", [linie(A0 + "40", 2.6), linie(A0, 0.8, [8, 2, 0.8, 2])]),
    ("Landesgrenze", [linie(A0, 0.7, [8, 2, 0.7, 2, 0.7, 2])]),
    ("Kreisgrenze", [linie(A0, 0.5, [6, 2, 0.5, 2])]),
    ("Gemeindegrenze", [linie(A0, 0.35, [4, 1.5])]),
    ("Ortsteilgrenze", [linie(A0, 0.3, [0.5, 1])]),
    ("Projektgrenze", [linie(R0, 0.8, [6, 2])]),
    ("Rettungsweg", [linie(R0, 0.6), marken(mk("filled_arrowhead", 2.2, R0), 9)]),
    ("Route", [linie(P0, 0.7)]),
    ("Route, Variante", [linie(P0, 0.7, [2, 1])]),
    ("Bezugslinie", [linie(A0, 0.25)]),
]

FLAECHEN = [
    ("Gebäude", [voll("#BDBDBD"), linie(A0, 0.3)]),
    ("Öffentliches Gebäude", [voll(P0 + "66"), linie(P0, 0.3)]),
    ("Verwaltungsgebiet", [band(A0 + "40", 2), linie(A0, 0.5, [6, 2, 0.5, 2])]),
    ("Untersuchungsgebiet", [band(R0 + "59", 1.5), linie(R0, 0.6)]),
    ("Projektgebiet", [voll(R0 + "1A"), linie(R0, 0.6, [6, 2])]),
    ("Gefahrenbereich", [schraffur(R0, 0.3, 45, 2.5), linie(R0, 0.5)]),
    ("Hinweisfläche", [schraffur(A0, 0.25, 45, 2.5), linie(A0, 0.4)]),
    ("Einzugsbereich", [voll(P0 + "26"), linie(P0, 0.4, [3, 1.5])]),
    ("Abdeckung, Maske", [voll("#FFFFFFB3"), linie(A0, 0.2, [1, 1])]),
]
