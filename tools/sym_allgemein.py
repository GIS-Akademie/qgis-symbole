"""Sammlung Allgemein: oeffentliche Einrichtungen, Gesundheit und Rettung, Kultur, topografische
Einzelobjekte, Freizeit, Dienste.
Orientierung: Objektarten amtlicher topografischer Karten und Stadtplaene (z. B. Kirche, Burg, Bergwerk,
Windmuehle, Aussichtsturm) und gaengige Sinnbilder fuer Orte von Interesse. Eigene Entwuerfe.
Stil: immer abgerundetes weisses Quadrat mit dunklem Sinnbild, Strich 5. Die Farbe zeigt die Gruppe:
  grau = allgemein, rot = Gesundheit und Rettung, blau = Sicherheit, Auskunft, Dienste.
"""
from lib import *

KEY = "allgemein"
NAME = "Allgemein"
DESC = ("Allgemeine Kartensymbole: Verwaltung und Bildung, Gesundheit und Rettung, Religion und Kultur, "
        "topografische Einzelobjekte, Freizeit und Tourismus, Dienste und Infrastruktur")
TAGS = "poi, oeffentliche einrichtungen, infrastruktur, tourismus, topografie, allgemein"

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
]

SYMBOLS = S
