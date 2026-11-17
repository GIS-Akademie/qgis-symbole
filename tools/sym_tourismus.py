"""Sammlung Tourismus und Freizeit: Unterkunft und Service, Wandern und Rad, Wasser und Winter,
Sehenswertes und Erlebnis.
Orientierung: touristische Hinweiszeichen der StVO (Zeichen 386.1 bis 386.3, weisses Sinnbild auf braunem
Grund), Legenden amtlicher Wander- und Freizeitkarten der Landesvermessungen, uebliche Kategorien der
Wegemarkierung (Wanderweg, Fernwanderweg, Themenweg, Steig). Eigene, schlichte Entwuerfe, keine amtlichen
Vorlagen. Keine Logos von Wanderverbaenden, Radrouten, Herbergswerken oder Qualitaetssiegeln.
Stil: immer abgerundetes Quadrat mit weissem Sinnbild. Die Farbe zeigt die Gruppe:
  grau-anthrazit = Unterkunft und Service, gruen = Wandern, Rad und Natur, blau = Wasser und Winter,
  braun = Sehenswertes und Erlebnis.
Linien und Flaechen: Farben der Punktsymbole (gruen = Wander- und Radwege, braun = Reiten und Erlebnis,
blau = Wasser und Winter, grau = Service). Wege durchgezogen, die Wegeart zeigen Breite und Markierungen;
gestrichelt bleibt geplanten Wegen vorbehalten.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "tourismus"
NAME = "Tourismus und Freizeit"
DESC = ("Symbole für Tourismus und Freizeit: Unterkunft und Service, Wandern und Radfahren, Baden, Wasser- und "
        "Wintersport, Sehenswürdigkeiten und Freizeitangebote, dazu Wege, Routen und Erholungsflächen")
TAGS = "tourismus, freizeit, wandern, radfahren, unterkunft, sehenswuerdigkeit, wintersport, erholung"

AN = ("#455A64", "#263238")   # Unterkunft und Service
GN = ("#2E7D32", "#1B4D1E")   # Wandern, Rad und Natur
BL = ("#1976A8", "#0D4A6B")   # Wasser und Winter
BR = ("#7B4A1E", "#4A2A0E")   # Sehenswertes und Erlebnis


def tq(*sh):
    """Rahmen der Sammlung: abgerundetes Quadrat in Gruppenfarbe, darauf das weisse Sinnbild."""
    return fr_square() + list(sh)


def tt(txt, h=44, mw=64):
    return tq(T(txt, 50, 50, h, "W", maxw=mw))


def wl(x1, y1, x2, y2, sw=5, cap="round"):
    return L(x1, y1, x2, y2, sw, "W", cap)


def wp(d, sw=5):
    return P(d, "N", "W", sw)


def wf(d):
    return P(d, "W", "N", 0)


BIKE = bike("W")
WALKER = person("W")
CAMPER = [wf("M12,66 V40 Q12,32 20,32 H66 Q72,32 76,38 L88,54 V66 Z"), R(20, 40, 18, 12, "F", "N", 0, 2),
          R(44, 40, 16, 12, "F", "N", 0, 2), PG([(66, 40), (72, 40), (80, 52), (66, 52)], "F"),
          C(30, 68, 8, "W", "F", 4), C(70, 68, 8, "W", "F", 4)]
WHEELCHAIR = [C(42, 20, 8, "W", "N", 0), PL([(42, 32), (44, 54), (62, 54), (70, 76)], 7, "W"), wl(44, 42, 60, 42, 6),
              arc(44, 62, 21, 78, 356, 6, "W")]
HUT = [PG([(50, 20), (86, 52), (76, 52), (76, 82), (24, 82), (24, 52), (14, 52)], "W"),
       R(43, 60, 14, 22, "F", "N", 0, 2)]

S = [
    # ---- Unterkunft und Service (grau-anthrazit) ----
    ("touristinfo", "Tourist-Information", *AN, tq(C(50, 23, 8, "W", "N", 0), wl(50, 42, 50, 78, 13, "butt"),
                                                    wl(38, 44, 50, 44, 6, "butt"), wl(36, 78, 64, 78, 6, "butt"))),
    ("hotel", "Hotel / Pension / Gasthof", *AN,
     tq(wl(18, 28, 18, 78, 6), wl(82, 60, 82, 78, 6), R(18, 56, 64, 11, "W", "N", 0, 2), C(31, 46, 7, "W", "N", 0),
        R(42, 42, 40, 14, "W", "N", 0, 6))),
    ("ferienwohnung", "Ferienwohnung / Ferienhaus", *AN,
     tq(PG([(50, 16), (86, 46), (76, 46), (76, 82), (24, 82), (24, 46), (14, 46)], "W"), T("FeWo", 50, 64, 15, "F", maxw=44))),
    ("campingplatz", "Campingplatz / Zeltplatz", *AN,
     tq(PG([(50, 24), (86, 80), (14, 80)], "W"), PG([(50, 50), (63, 80), (37, 80)], "F"), wl(50, 24, 44, 15, 4.5),
        wl(50, 24, 56, 15, 4.5))),
    ("wohnmobilstellplatz", "Wohnmobilstellplatz", *AN, tq(*CAMPER)),
    ("berghuette", "Berghütte (bewirtschaftet)", *AN,
     tq(PL([(14, 40), (30, 18), (42, 32)], 5, "W"), PL([(58, 32), (70, 18), (86, 40)], 5, "W"), *fit(HUT, 50, 60, 0.78))),
    ("schutzhuette", "Schutzhütte / Biwak", *AN,
     tq(PL([(14, 50), (50, 20), (86, 50)], 7, "W"), wl(26, 46, 26, 82, 6), wl(74, 46, 74, 82, 6), wl(26, 68, 74, 68, 5))),
    ("gastronomie", "Gastronomie / Restaurant", *AN,
     tq(wl(36, 20, 36, 82, 6), wl(26, 20, 26, 38, 4), wl(46, 20, 46, 38, 4), wp("M26,38 Q26,48 36,48 Q46,48 46,38", 4),
        wf("M62,16 Q76,24 76,50 H62 Z"), wl(64, 20, 64, 82, 6))),
    ("biergarten", "Biergarten / Einkehr / Jausenstation", *AN,
     tq(R(26, 36, 34, 46, "W", "N", 0, 4), wp("M60,46 H67 Q76,46 76,55 V61 Q76,70 67,70 H60", 5.5),
        C(31, 33, 7, "W", "N", 0), C(43, 29, 8, "W", "N", 0), C(55, 33, 7, "W", "N", 0),
        L(37, 50, 37, 72, 4, "F"), L(49, 50, 49, 72, 4, "F"))),
    ("picknickplatz", "Picknickplatz / Rastplatz", *AN,
     tq(wl(24, 38, 76, 38, 7), wl(15, 60, 85, 60, 6), wl(40, 38, 26, 82, 5.5), wl(60, 38, 74, 82, 5.5))),
    ("grillplatz", "Grillplatz / Feuerstelle", *AN,
     tq(*fit(flame("W", "F"), 50, 36, 0.56), wf("M22,62 H78 Q78,80 50,80 Q22,80 22,62 Z"), wl(36, 78, 30, 88, 4.5),
        wl(64, 78, 70, 88, 4.5))),
    ("trinkwasser", "Trinkwasser / Brunnen", *AN,
     tq(wl(20, 36, 56, 36, 10, "butt"), P("M54,36 Q68,36 68,50", "N", "W", 10, "butt"), wl(38, 36, 38, 22, 5),
        wl(28, 20, 48, 20, 6), *fit(drop("W", "N", 0), 68, 72, 0.3))),
    ("toilette", "Toilette", *AN, tt("WC", 34, 62)),
    ("e_bike_ladestation", "E-Bike-Ladestation", *AN, tq(*lightning(50, 26, 0.42, "W"), *fit(BIKE, 50, 64, 0.72))),
    ("fahrradverleih", "Fahrradverleih / Radservice", *AN,
     tq(*fit(BIKE, 50, 42, 0.72), *arrow(50, 78, 80, 78, 5, 11, "W"), *arrow(50, 78, 20, 78, 5, 11, "W"))),
    # ---- Wandern, Rad und Natur (gruen) ----
    ("wanderparkplatz", "Wanderparkplatz / Startpunkt", *GN, tq(T("P", 30, 34, 26, "W"), *fit(WALKER, 62, 56, 0.66))),
    ("wegweiser", "Wegweiser", *GN,
     tq(wl(50, 14, 50, 86, 6), PG([(28, 22), (68, 22), (82, 32), (68, 42), (28, 42)], "W"),
        PG([(72, 50), (32, 50), (18, 60), (32, 70), (72, 70)], "W"))),
    ("gipfel", "Gipfel", *GN,
     tq(PG([(12, 82), (44, 34), (58, 54), (66, 44), (88, 82)], "W"), wl(44, 14, 44, 34, 4.5), wl(36, 21, 52, 21, 4.5))),
    ("aussichtspunkt", "Aussichtspunkt", *GN,
     tq(C(50, 74, 9, "W", "N", 0), *[wl(*pt(50, 74, 19, a), *pt(50, 74, {0: 54, 33: 47, 66: 38}[abs(a)], a), 6) for a in (-66, -33, 0, 33, 66)])),
    ("aussichtsturm", "Aussichtsturm", *GN,
     tq(PG([(30, 28), (50, 12), (70, 28)], "W"), R(32, 32, 36, 11, "W", "N", 0, 2), wl(44, 43, 38, 84, 5), wl(56, 43, 62, 84, 5),
        wl(43, 54, 60, 70, 3.5), wl(57, 54, 40, 70, 3.5), wl(28, 84, 72, 84, 5))),
    ("klettersteig", "Klettersteig", *GN,
     tq(wl(36, 16, 36, 84, 6), wl(64, 16, 64, 84, 6), *[wl(36, y, 64, y, 5) for y in (28, 43, 58, 73)])),
    ("klettergarten", "Klettergarten / Kletterfels", *GN,
     tq(P("M42,18 H56 Q70,18 70,32 V68 Q70,82 56,82 H46 Q32,82 32,68 V34 Q32,18 42,18 Z", "N", "W", 8, tr="rotate(20 50 50)"),
        P("M32,40 V62", "N", "F", 3.5, "butt", tr="rotate(20 50 50)"))),
    ("mountainbike", "Mountainbike-Strecke / Pumptrack", *GN,
     tq(*fit(BIKE, 50, 42, 0.7, -14), PL([(14, 84), (34, 70), (50, 80), (68, 64), (86, 72)], 5, "W"))),
    ("themenweg", "Themenweg / Lehrpfad", *GN,
     tq(R(20, 20, 60, 40, "W", "N", 0, 4), wl(34, 60, 34, 84, 6), wl(66, 60, 66, 84, 6), L(30, 32, 70, 32, 4.5, "F"),
        L(30, 42, 70, 42, 4.5, "F"), L(30, 51, 54, 51, 4.5, "F"))),
    ("barrierefrei", "Barrierefreier Weg", *GN, tq(*fit(WHEELCHAIR, 52, 52, 0.9))),
    ("stempelstelle", "Stempelstelle", *GN,
     tq(C(50, 24, 11, "W", "N", 0), PG([(45, 30), (55, 30), (62, 58), (38, 58)], "W"), R(24, 56, 52, 13, "W", "N", 0, 3),
        wl(22, 82, 78, 82, 5))),
    # ---- Wasser und Winter (blau) ----
    ("badestelle", "Badestelle", *BL, tq(*swimmer("W"))),
    ("schwimmbad", "Freibad / Hallenbad / Therme", *BL,
     tq(wp("M34,66 V30 A8,8 0 0 1 50,30", 5.5), wp("M58,66 V30 A8,8 0 0 1 74,30", 5.5), wl(34, 42, 58, 42, 5),
        wl(34, 55, 58, 55, 5), wave(16, 80, 68, 4.5, 3, 5, "W"))),
    ("bootsverleih", "Bootsverleih / Kanueinstieg", *BL,
     tq(wf("M10,54 H90 Q78,72 50,72 Q22,72 10,54 Z"), wl(34, 20, 62, 50, 5), G([E(0, 0, 6.5, 11, "W", "N", 0)], 30, 21, a=-43),
        wave(16, 84, 68, 4, 3, 4.5, "W"))),
    ("segeln", "Segeln / Surfen", *BL,
     tq(PG([(16, 68), (84, 68), (72, 82), (28, 82)], "W"), wl(48, 16, 48, 66, 4.5), PG([(53, 18), (53, 62), (80, 62)], "W"),
        PG([(43, 30), (43, 62), (22, 62)], "W"))),
    ("angeln", "Angeln", *BL,
     tq(*fit(fish("W", "F"), 50, 62, 0.8), wl(50, 13, 50, 27, 4), wp("M50,27 Q50,38 40,34", 4))),
    ("loipe", "Loipe / Skilanglauf", *BL,
     tq(*fit(WALKER, 50, 44, 0.7), wl(20, 80, 86, 80, 5), wl(65, 48, 71, 79, 3.5), wl(38, 48, 20, 66, 3.5))),
    ("skilift", "Skilift / Sessellift", *BL,
     tq(wl(14, 24, 86, 14, 4.5), wl(50, 19, 50, 50, 4.5), PL([(36, 48), (36, 70), (64, 70)], 7, "W"), wl(36, 50, 62, 50, 4.5),
        wl(64, 70, 64, 82, 4.5))),
    ("skipiste", "Skipiste / Abfahrt", *BL,
     tq(wp("M26,84 L66,24 Q70,18 76,18", 7), wp("M74,84 L34,24 Q30,18 24,18", 7))),
    ("rodelbahn", "Rodelbahn", *BL,
     tq(wp("M16,74 H72 Q86,74 86,58", 5.5), wl(22, 50, 70, 50, 7), wl(32, 50, 32, 74, 5), wl(58, 50, 58, 74, 5))),
    ("eislaufen", "Eislaufen", *BL,
     tq(wf("M34,16 H52 V42 L70,50 Q78,54 78,64 H34 Z"), wp("M24,80 H74 Q82,80 82,74", 5), wl(42, 64, 42, 80, 4.5),
        wl(66, 64, 66, 80, 4.5))),
    # ---- Sehenswertes und Erlebnis (braun) ----
    ("sehenswuerdigkeit", "Sehenswürdigkeit", *BR, tq(PG(star(50, 52, 38, 15.5, 5), "W"))),
    ("burg_schloss", "Burg / Schloss", *BR,
     tq(PG([(18, 84), (18, 20), (27, 20), (27, 29), (34, 29), (34, 20), (43, 20), (43, 44), (57, 44), (57, 20), (66, 20),
            (66, 29), (73, 29), (73, 20), (82, 20), (82, 84)], "W"), P("M41,84 V68 A9,9 0 0 1 59,68 V84 Z", "F", "N", 0))),
    ("museum", "Museum", *BR,
     tq(PG([(12, 38), (50, 14), (88, 38)], "W"), *[R(x, 43, 9, 30, "W", "N", 0) for x in (20, 37, 54, 71)],
        R(13, 76, 74, 9, "W", "N", 0, 1))),
    ("wildgehege", "Wildgehege / Tierpark / Naturerlebnis", *BR,
     tq(E(50, 64, 17, 14, "W", "N", 0), C(26, 48, 7, "W", "N", 0), C(41, 32, 8, "W", "N", 0), C(59, 32, 8, "W", "N", 0),
        C(74, 48, 7, "W", "N", 0))),
    ("hoehle", "Höhle", *BR,
     tq(PG([(10, 84), (20, 48), (36, 24), (58, 18), (78, 38), (90, 84)], "W"), P("M36,84 V62 A14,14 0 0 1 64,62 V84 Z", "F", "N", 0))),
    ("wasserfall", "Wasserfall", *BR,
     tq(R(14, 20, 26, 64, "W", "N", 0, 2), wp("M40,25 Q62,25 62,46 V66", 6), wp("M40,38 Q50,38 50,50 V66", 4.5),
        wave(42, 82, 44, 4.5, 2, 5, "W"))),
    ("golfplatz", "Golfplatz / Minigolf", *BR,
     tq(wl(42, 16, 42, 76, 5), PG([(42, 14), (76, 26), (42, 38)], "W"), E(48, 78, 30, 7, "N", "W", 4.5), C(68, 62, 5.5, "W", "N", 0))),
    ("reiten", "Reiten / Reiterhof", *BR,
     tq(arc(50, 46, 24, 212, 148, 11, "W"), *[C(*pt(50, 46, 24, a), 2.6, "F", "N", 0) for a in (245, 295, 345, 15, 65, 115)])),
    ("spielplatz", "Spielplatz / Freizeitpark", *BR,
     tq(PL([(16, 84), (30, 20), (70, 20), (84, 84)], 6, "W"), wl(42, 20, 40, 62, 3.5), wl(58, 20, 60, 62, 3.5), wl(36, 63, 64, 63, 7))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
A0, AD, G0, GD, B0, BD, R0, RD, WS = AN[0], AN[1], GN[0], GN[1], BL[0], BL[1], BR[0], BR[1], "#FFFFFF"

LINIEN = [
    ("Wanderweg", [linie(G0, 0.6)]),
    ("Fernwanderweg", [linie(GD, 1.3), linie(WS, 0.4)]),
    ("Themenweg, Lehrpfad", [linie(G0, 0.6), marken(mk("square", 1.5, WS, rand=G0, rw=0.35), 7)]),
    ("Alpiner Steig", [linie(GD, 0.4), marken(mk("triangle", 1.5, GD), 5)]),
    ("Klettersteig", [linie(GD, 0.5), marken(mk("line", 2.0, GD, rw=0.4), 2.2)]),
    ("Radweg", [linie(G0, 1.1), linie(WS, 0.35, [2, 1.5])]),
    ("Radfernweg", [linie(GD, 1.8), linie(G0, 1.2), linie(WS, 0.35, [2, 1.5])]),
    ("Mountainbike-Route", [linie(G0, 0.7), marken(mk("diamond", 1.8, GD), 6)]),
    ("Reitweg", [linie(R0, 0.6), marken(mk("semi_circle", 1.8, R0), 6)]),
    ("Loipe", [linie(B0, 1.3), linie(WS, 0.5)]),
    ("Skipiste", [linie(BD, 1.8), linie(B0, 1.2)]),
    ("Lift, Seilbahn", [linie(BD, 0.4), marken(mk("line", 2.0, BD, rw=0.45), 5)]),
    ("Kanuroute", [linie(B0, 0.6), marken(mk("circle", 1.4, WS, rand=B0, rw=0.35), 6)]),
    ("Rundweg mit Richtungspfeil", [linie(G0, 0.6), marken(mk("filled_arrowhead", 2.4, GD), 9)]),
]

FLAECHEN = [
    ("Erholungsgebiet", [voll(G0 + "26"), linie(G0, 0.4)]),
    ("Kurgebiet", [schraffur(A0, 0.25, 45, 2.5), linie(A0, 0.4)]),
    ("Skigebiet", [voll(B0 + "1F"), schraffur(B0, 0.25, 135, 3), linie(B0, 0.4)]),
    ("Badezone", [voll(B0 + "40"), muster(mk("circle", 0.6, B0), 2.4, versatz=1.2), linie(B0, 0.5)]),
    ("Campingfläche", [voll(A0 + "26"), muster(mk("triangle", 1.5, A0), 4, versatz=2), linie(A0, 0.4)]),
    ("Golfplatzfläche", [voll(R0 + "22"), muster(mk("circle", 0.7, R0), 3.5, versatz=1.75), linie(R0, 0.4)]),
    ("Wildruhezone (Betretungsverbot)", [voll(GD + "26"), linie(GD, 0.5),
                                         marken(mk("cross2", 1.8, GD, rw=0.4, dy=1.6), 5, ecken=2.5)]),
    ("Parkanlage", [voll(G0 + "40"), muster(mk("circle", 1.0, G0), 3.5, versatz=1.75), linie(GD, 0.3)]),
    ("Veranstaltungsfläche", [band(R0 + "59", 1.5), linie(R0, 0.4)]),
    ("Naturpark-Zone", [band(G0 + "59", 1.5), linie(GD, 0.6)]),
]
