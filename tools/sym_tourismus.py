"""Sammlung Tourismus und Freizeit: Unterkunft und Service, Wandern und Rad, Wasser und Winter,
Sehenswertes und Erlebnis, Sport und Sportstaetten.
Orientierung: touristische Hinweiszeichen der StVO (Zeichen 386.1 bis 386.3, weisses Sinnbild auf braunem
Grund), Legenden amtlicher Wander- und Freizeitkarten der Landesvermessungen, uebliche Kategorien der
Wegemarkierung (Wanderweg, Fernwanderweg, Themenweg, Steig). Eigene, schlichte Entwuerfe, keine amtlichen
Vorlagen. Keine Logos von Wanderverbaenden, Radrouten, Herbergswerken oder Qualitaetssiegeln.
Stil: immer abgerundetes Quadrat mit weissem Sinnbild. Die Farbe zeigt die Gruppe:
  grau-anthrazit = Unterkunft und Service, gruen = Wandern, Rad und Natur, blau = Wasser und Winter,
  braun = Sehenswertes und Erlebnis, orangerot = Sport und Sportstaetten (Ball-, Schlaeger-, Ziel-, Lauf-,
  Hallen-, Roll- und Luftsport; Wasser- und Wintersport bleiben blau).
Sportsinnbilder: moeglichst das Sportgeraet (Ball, Schlaeger, Scheibe, Kugel), sonst eine einfache Figur.
Sie orientieren sich an ueblichen Sportpiktogrammen (Sportstaettenleitsysteme, Freizeitkarten), sind aber
eigene Entwuerfe.
Linien und Flaechen: Farben der Punktsymbole (gruen = Wander- und Radwege, braun = Reiten und Erlebnis,
blau = Wasser und Winter, grau = Service). Wege durchgezogen, die Wegeart zeigen Breite und Markierungen;
gestrichelt bleibt geplanten Wegen vorbehalten.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "tourismus"
NAME = "Tourismus und Freizeit"
DESC = ("Symbole für Tourismus und Freizeit: Unterkunft und Service, Wandern und Radfahren, Baden, Wasser- und "
        "Wintersport, Sehenswürdigkeiten, Freizeitangebote sowie Sportarten und Sportstätten, dazu Wege, Routen "
        "und Erholungsflächen")
TAGS = ("tourismus, freizeit, wandern, radfahren, unterkunft, sehenswuerdigkeit, wintersport, erholung, sport, "
        "sportstaette, ballsport, boule")

AN = ("#455A64", "#263238")   # Unterkunft und Service
GN = ("#2E7D32", "#1B4D1E")   # Wandern, Rad und Natur
BL = ("#1976A8", "#0D4A6B")   # Wasser und Winter
BR = ("#7B4A1E", "#4A2A0E")   # Sehenswertes und Erlebnis
SP = ("#C2410C", "#7A2807")   # Sport und Sportstaetten (ohne Wasser- und Wintersport)


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


def wc(cx, cy, r):
    """Weisse Scheibe (Ball, Kopf)."""
    return C(cx, cy, r, "W", "N", 0)


def wpl(pts, sw=6):
    return PL(pts, sw, "W")


def fl(x1, y1, x2, y2, sw=3.5, cap="round"):
    """Linie in Grundfarbe (Aussparung im weissen Sinnbild)."""
    return L(x1, y1, x2, y2, sw, "F", cap)


def fp(d, sw=3.5):
    return P(d, "N", "F", sw)


def fq(p0, c, p1, sw=3.5):
    """Bogen in Grundfarbe von p0 nach p1 mit Stuetzpunkt c."""
    return fp(f"M{n(p0[0])},{n(p0[1])} Q{n(c[0])},{n(c[1])} {n(p1[0])},{n(p1[1])}", sw)


BIKE = bike("W")
WALKER = person("W")
CAMPER = [wf("M12,66 V40 Q12,32 20,32 H66 Q72,32 76,38 L88,54 V66 Z"), R(20, 40, 18, 12, "F", "N", 0, 2),
          R(44, 40, 16, 12, "F", "N", 0, 2), PG([(66, 40), (72, 40), (80, 52), (66, 52)], "F"),
          C(30, 68, 8, "W", "F", 4), C(70, 68, 8, "W", "F", 4)]
WHEELCHAIR = [C(42, 20, 8, "W", "N", 0), PL([(42, 32), (44, 54), (62, 54), (70, 76)], 7, "W"), wl(44, 42, 60, 42, 6),
              arc(44, 62, 21, 78, 356, 6, "W")]
HUT = [PG([(50, 20), (86, 52), (76, 52), (76, 82), (24, 82), (24, 52), (14, 52)], "W"),
       R(43, 60, 14, 22, "F", "N", 0, 2)]
PIN = [wf("M50,14 C56,14 58,20 56,26 C54,32 62,44 62,58 C62,70 58,80 56,82 H44 C42,80 38,70 38,58 "
          "C38,44 46,32 44,26 C42,20 44,14 50,14 Z"), fl(43, 28, 57, 28, 3.5, "butt")]

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
    # ---- Ballsport (orangerot) ----
    ("sport_fussball", "Fußball / Fußballplatz", *SP,
     tq(wc(50, 50, 31), PG(regpoly(50, 50, 11, 5), "F"),
        *[fl(*pt(50, 50, 11, a), *pt(50, 50, 22, a), 3.5) for a in range(0, 360, 72)],
        *[PG([pt(50, 50, 21, a), pt(50, 50, 31.5, a - 17), pt(50, 50, 31.5, a + 17)], "F") for a in range(0, 360, 72)])),
    ("sport_handball", "Handball", *SP,
     tq(wpl([(18, 82), (18, 24), (82, 24), (82, 82)], 8),
        *[L(x, y, x, y + 10, 8.4, "F", "butt") for x in (18, 82) for y in (38, 60)],
        *[L(x, 24, x + 10, 24, 8.4, "F", "butt") for x in (28, 45, 62)],
        wc(50, 62, 14), fq((40, 54), (50, 62), (40, 71), 3), fq((60, 54), (50, 62), (60, 71), 3))),
    ("sport_basketball", "Basketball / Streetball", *SP,
     tq(wc(50, 50, 31), fl(50, 19, 50, 81), fl(19, 50, 81, 50), fq((28, 28), (46, 50), (28, 72)),
        fq((72, 28), (54, 50), (72, 72)))),
    ("sport_volleyball", "Volleyball", *SP,
     tq(wc(50, 50, 31),
        *[fq((50, 50), pt(50, 50, 22, a + 45), pt(50, 50, 31, a)) for a in (0, 120, 240)],
        *[fq(pt(50, 50, 31, a + 62), pt(50, 50, 27, a + 25), pt(50, 50, 15, a + 8), 3) for a in (0, 120, 240)])),
    ("sport_beachvolleyball", "Beachvolleyball", *SP,
     tq(wl(20, 42, 20, 84, 5), wl(80, 42, 80, 84, 5), R(20, 44, 60, 20, "N", "W", 4),
        *[wl(x, 44, x, 64, 2.5) for x in (32, 44, 56, 68)], wl(20, 54, 80, 54, 2.5), wc(38, 25, 10),
        *sun(72, 25, 5, "W", "W", 3, 8, 3.5, 4))),
    ("sport_hockey", "Hockey", *SP,
     tq(G([wp("M0,-34 V24 Q0,34 -10,34 Q-19,34 -19,25", 6)], 50, 46, a=30),
        G([wp("M0,-34 V24 Q0,34 10,34 Q19,34 19,25", 6)], 50, 46, a=-30), wc(50, 78, 6.5))),
    ("sport_rugby_football", "Rugby / American Football", *SP,
     tq(G([wf("M-36,0 Q0,-34 36,0 Q0,34 -36,0 Z"), fl(-16, 0, 16, 0), fl(-10, -5, -10, 5, 3), fl(0, -5, 0, 5, 3),
           fl(10, -5, 10, 5, 3)], 50, 50, a=-35))),
    ("sport_baseball", "Baseball / Softball", *SP,
     tq(G([PG([(-34, -3), (-28, -3.5), (0, -4.5), (22, -8), (31, -8), (36, -4), (36, 4), (31, 8), (22, 8), (0, 4.5),
               (-28, 3.5), (-34, 3)], "W"), wc(-35, 0, 5)], 46, 50, a=-45),
        wc(72, 72, 11), fq((66, 64), (71, 72), (66, 80), 2.5), fq((78, 64), (73, 72), (78, 80), 2.5))),
    # ---- Schlaegersport (orangerot) ----
    ("sport_tennis", "Tennis / Tennisplatz", *SP,
     tq(G([E(0, -14, 19, 24, "N", "W", 5), *[wl(x, -14 - h, x, -14 + h, 2.5) for x, h in ((-8, 21), (0, 23), (8, 21))],
           *[wl(-w, y, w, y, 2.5) for y, w in ((-24, 16), (-14, 18), (-4, 16))],
           wpl([(-10, 6), (0, 20), (10, 6)], 4), wl(0, 20, 0, 40, 7.5)], 46, 48, a=35), wc(74, 72, 7.5))),
    ("sport_tischtennis", "Tischtennis / Tischtennisplatte", *SP,
     tq(G([wc(0, -10, 23), L(0, 12, 0, 36, 10, "W", "butt"), fl(-9, 16, 9, 16, 3, "butt")], 44, 46, a=35),
        wc(76, 68, 6.5))),
    ("sport_badminton", "Badminton / Federball", *SP,
     tq(G([PG([(-7, 12), (7, 12), (24, -30), (-24, -30)], "W"), wc(0, 20, 11), fl(-8, 9, 8, 9, 3.5, "butt"),
           fl(-3, 6, -9, -30, 3, "butt"), fl(3, 6, 9, -30, 3, "butt"), fl(-18, -12, 18, -12, 3, "butt")], 50, 54, a=25))),
    ("sport_minigolf", "Minigolf", *SP,
     tq(wl(14, 82, 86, 82, 5), wl(30, 16, 38, 70, 4.5), wl(38, 73, 50, 73, 7), wc(60, 73, 5.5),
        wp("M68,80 V60 A8,8 0 0 1 84,60 V80", 5), wl(76, 52, 76, 34, 3.5), PG([(76, 32), (90, 38), (76, 44)], "W"))),
    # ---- Kugel- und Zielsport (orangerot) ----
    ("sport_boule", "Bouleplatz / Boule / Pétanque", *SP,
     tq(*[e for cx, cy in ((31, 36), (66, 31), (42, 70)) for e in
          (wc(cx, cy, 15.5), fq((cx - 13, cy - 4), (cx, cy + 4), (cx + 13, cy - 4), 2.5),
           fq((cx - 11, cy + 5), (cx, cy + 12), (cx + 11, cy + 5), 2.5))], wc(72, 68, 6.5))),
    ("sport_kegeln", "Kegelbahn / Bowling", *SP,
     tq(*fit(PIN, 28, 46, 0.85), *fit(PIN, 51, 46, 0.85), wc(73, 70, 13), C(69, 65, 2.3, "F", "N", 0),
        C(76, 64, 2.3, "F", "N", 0), C(74, 71, 2.3, "F", "N", 0))),
    ("sport_billard", "Billard", *SP,
     tq(wc(60, 60, 21), T("8", 60, 60, 22, "F"), PG([(14, 19), (17, 15), (41, 36), (36, 41)], "W"), wc(26, 74, 9))),
    ("sport_bogenschiessen", "Bogenschießen", *SP,
     tq(wp("M36,14 Q80,50 36,86", 6), wl(36, 14, 36, 86, 3), *arrow(18, 50, 86, 50, 4, 13, "W"),
        wl(18, 50, 12, 44, 3.5), wl(18, 50, 12, 56, 3.5), wl(24, 50, 18, 44, 3.5), wl(24, 50, 18, 56, 3.5))),
    ("sport_schiessen", "Schießsport / Schießstand", *SP,
     tq(C(50, 50, 25, "N", "W", 5), C(50, 50, 12, "N", "W", 4.5), wc(50, 50, 4), wl(50, 14, 50, 29), wl(50, 71, 50, 86),
        wl(14, 50, 29, 50), wl(71, 50, 86, 50))),
    ("sport_darts", "Darts", *SP,
     tq(wc(44, 56, 29), C(44, 56, 18, "N", "F", 3), *[fl(*pt(44, 56, 8, a), *pt(44, 56, 29, a), 2.5, "butt") for a in range(15, 360, 30)],
        C(44, 56, 5, "W", "F", 3), fl(44, 56, 64, 36, 3), wl(64, 36, 76, 24, 5),
        PG([(72, 28), (76, 16), (84, 16), (84, 24)], "W"))),
    ("sport_schach", "Freiluftschach / Schach", *SP,
     tq(wc(50, 24, 10), wl(39, 37, 61, 37, 5), PG([(44, 38), (56, 38), (63, 60), (37, 60)], "W"),
        R(31, 58, 38, 8, "W", "N", 0, 2), R(20, 72, 60, 12, "N", "W", 3),
        *[R(20 + 12 * i, 72, 12, 12, "W", "N", 0) for i in (0, 2, 4)])),
    # ---- Laufen, Fitness und Turnen (orangerot) ----
    ("sport_leichtathletik", "Leichtathletik / Laufbahn / Stadion", *SP,
     tq(R(13, 24, 74, 52, "N", "W", 5, 26), R(23, 34, 54, 32, "N", "W", 3.5, 16), R(33, 44, 34, 12, "W", "N", 0, 6),
        wl(50, 62, 50, 80, 3, "butt"))),
    ("sport_laufen", "Laufstrecke / Jogging", *SP,
     tq(wc(62, 20, 8), wpl([(57, 33), (47, 55)], 10), wpl([(47, 55), (64, 62), (60, 82)], 6.5),
        wpl([(47, 55), (34, 68), (17, 66)], 6.5), wpl([(57, 35), (72, 42), (80, 32)], 5.5),
        wpl([(57, 35), (40, 36), (33, 49)], 5.5))),
    ("sport_nordic_walking", "Nordic Walking", *SP,
     tq(*fit(WALKER, 52, 50, 0.8), wl(69.5, 53, 60, 86, 3.5), wl(37.5, 53, 20, 86, 3.5))),
    ("sport_fitnessparcours", "Fitnessparcours / Trimm-dich-Pfad / Calisthenics", *SP,
     tq(wpl([(20, 86), (20, 20), (80, 20), (80, 86)], 6), wl(39, 22, 43, 42, 5), wl(61, 22, 57, 42, 5), wc(50, 33, 7),
        wl(50, 46, 50, 62, 12), wl(47, 62, 44, 82, 6), wl(53, 62, 56, 82, 6))),
    ("sport_fitnessstudio", "Fitnessstudio / Kraftraum", *SP,
     tq(G([wl(-22, 0, 22, 0, 6), R(-31, -17, 10, 34, "W", "N", 0, 3), R(21, -17, 10, 34, "W", "N", 0, 3),
           R(-40, -10, 7, 20, "W", "N", 0, 2.5), R(33, -10, 7, 20, "W", "N", 0, 2.5)], 50, 50, a=-30))),
    ("sport_turnen", "Turnen / Turnhalle / Sporthalle", *SP,
     tq(wl(34, 12, 34, 30, 3.5), wl(66, 12, 66, 30, 3.5), C(34, 36, 6, "N", "W", 4), C(66, 36, 6, "N", "W", 4),
        wc(50, 30, 7), wl(36, 44, 64, 44, 6), wl(50, 46, 50, 64, 11), wl(50, 64, 50, 85, 8))),
    ("sport_yoga", "Yoga / Gymnastik", *SP,
     tq(wc(50, 22, 8), wl(50, 36, 50, 58, 10), wp("M22,76 Q50,56 78,76", 8), wpl([(50, 38), (34, 50), (27, 64)], 5),
        wpl([(50, 38), (66, 50), (73, 64)], 5))),
    # ---- Kampfsport (orangerot) ----
    ("sport_kampfsport", "Kampfsport / Judo / Karate", *SP,
     tq(wc(33, 22, 8), wpl([(37, 34), (46, 56)], 10), wpl([(46, 56), (41, 70), (43, 86)], 6.5),
        wpl([(46, 56), (64, 50), (85, 42)], 6.5), wpl([(38, 36), (52, 38), (57, 27)], 5.5),
        wpl([(38, 36), (26, 46), (24, 58)], 5.5))),
    ("sport_boxen", "Boxen", *SP,
     tq(wf("M36,60 V36 Q36,16 56,16 Q76,16 76,36 V60 Z"), wf("M38,42 Q20,36 21,52 Q22,64 38,62 Z"),
        fp("M40,42 Q40,54 49,56", 3), R(38, 66, 36, 17, "W", "N", 0, 3))),
    ("sport_fechten", "Fechten", *SP,
     tq(*[G([wl(0, -38, 0, 14, 4), wf("M-11,21 A11,11 0 0 1 11,21 Z"), wl(0, 22, 0, 36, 6.5)], 50, 50, a=a) for a in (35, -35)])),
    # ---- Rollen und Rad (orangerot) ----
    ("sport_skatepark", "Skatepark / Skateanlage", *SP,
     tq(wp("M14,84 H42 Q82,84 86,40", 5),
        G([wp("M-27,-7 Q-23,0 -15,0 H15 Q23,0 27,-7", 6), wc(-14, 9, 5.5), wc(14, 9, 5.5)], 42, 44, a=-18))),
    ("sport_inlineskaten", "Inlineskaten / Skaterstrecke", *SP,
     tq(wf("M32,14 H50 V38 L68,46 Q78,50 78,60 V66 H32 Z"), fl(32, 24, 46, 24, 3, "butt"), fl(32, 33, 46, 33, 3, "butt"),
        wl(32, 69, 78, 69, 4), *[wc(x, 78, 6) for x in (34, 48, 62, 76)])),
    ("sport_rennrad", "Radsport / Rennradstrecke / Radrennbahn", *SP,
     tq(*fit(BIKE, 50, 62, 0.75), wc(66, 22, 7), wl(43, 43, 58, 30, 8), wl(58, 31, 66, 42, 4.5))),
    # ---- Luftsport und Motorsport (orangerot) ----
    ("sport_gleitschirm", "Gleitschirmfliegen / Drachenfliegen", *SP,
     tq(wf("M10,42 Q50,2 90,42 Q50,24 10,42 Z"), wl(17, 40, 50, 68, 2.5), wl(50, 32, 50, 68, 2.5), wl(83, 40, 50, 68, 2.5),
        wc(50, 70, 5.5), wl(50, 77, 50, 86, 7))),
    ("sport_fallschirm", "Fallschirmspringen", *SP,
     tq(wf("M18,46 A32,32 0 0 1 82,46 Q74,39 66,46 Q58,39 50,46 Q42,39 34,46 Q26,39 18,46 Z"), wl(19, 46, 50, 70, 2.5),
        wl(34, 46, 50, 70, 2.5), wl(66, 46, 50, 70, 2.5), wl(81, 46, 50, 70, 2.5), wc(50, 71, 5.5), wl(50, 78, 50, 86, 7))),
    ("sport_segelflug", "Segelflug / Segelfluggelände", *SP,
     tq(G([wl(0, -30, 0, 30, 5), wc(0, -27, 5), PG([(-42, -9), (42, -9), (42, -5.5), (5, 0), (-5, 0), (-42, -5.5)], "W"),
           wl(-11, 30, 11, 30, 4.5)], 50, 50, a=40))),
    ("sport_ballonfahrt", "Ballonfahrt / Ballonstartplatz", *SP,
     tq(wf("M50,12 C72,12 80,30 76,44 C72,56 60,62 56,70 H44 C40,62 28,56 24,44 C20,30 28,12 50,12 Z"),
        fl(50, 14, 50, 68, 3, "butt"), fq((38, 16), (28, 42), (46, 68), 3), fq((62, 16), (72, 42), (54, 68), 3),
        wl(45, 70, 45, 77, 2.5), wl(55, 70, 55, 77, 2.5), R(42, 76, 16, 11, "W", "N", 0, 2))),
    ("sport_motorsport", "Motorsport / Kartbahn", *SP,
     tq(wl(22, 16, 22, 86, 5), R(24, 18, 60, 39, "W", "N", 0),
        *[R(24 + 15 * i, 18 + 13 * j, 15, 13, "F", "N", 0) for i in range(4) for j in range(3) if (i + j) % 2])),
    # ---- Wassersport (blau) ----
    ("rudern", "Rudern / Ruderstrecke", *BL,
     tq(wf("M8,60 H92 Q84,69 72,69 H28 Q16,69 8,60 Z"), *[e for x in (36, 62) for e in
        (wc(x, 33, 6.5), wl(x, 44, x - 5, 57, 8), wl(x - 1, 46, x + 12, 52, 4.5), wl(x + 10, 46, x + 22, 76, 3.5))],
        wave(16, 84, 68, 4, 3, 4.5, "W"))),
    ("stand_up_paddling", "Stand-up-Paddling", *BL,
     tq(wc(42, 17, 7), wl(42, 29, 42, 48, 9), wl(40, 48, 36, 64, 6), wl(44, 48, 50, 64, 6), E(44, 69, 32, 4.5, "W", "N", 0),
        wl(66, 14, 63, 68, 3.5), wl(63, 64, 62.5, 79, 7.5), wpl([(42, 31), (55, 28), (65, 24)], 4.5),
        wpl([(42, 33), (54, 42), (64, 44)], 4.5), wave(16, 87, 68, 3, 3, 4, "W"))),
    ("tauchen", "Tauchen / Schnorcheln", *BL,
     tq(R(14, 32, 56, 32, "W", "N", 0, 13), R(21, 39, 18, 18, "F", "N", 0, 6), R(45, 39, 18, 18, "F", "N", 0, 6),
        wp("M84,16 V64 Q84,76 72,76 H60", 6))),
    ("kitesurfen", "Kitesurfen / Wasserski / Wakeboard", *BL,
     tq(wp("M48,17 Q78,14 85,42", 9), wl(48, 17, 40, 52, 2.5), wl(85, 42, 40, 52, 2.5), wc(27, 42, 6.5),
        wl(30, 52, 37, 65, 8), wl(31, 52, 40, 52, 4.5), wl(37, 65, 48, 72, 6), wl(22, 78, 62, 72, 6),
        wave(16, 87, 68, 3, 3, 4, "W"))),
    # ---- Wintersport (blau) ----
    ("snowboard", "Snowboard / Funpark", *BL,
     tq(G([R(-38, -11, 76, 22, "W", "N", 0, 11), fl(-14, -9, -14, 9, 5), fl(14, -9, 14, 9, 5)], 50, 50, a=-40))),
    ("eishockey", "Eishockey / Eishalle", *BL,
     tq(G([wpl([(0, -36), (0, 30), (-15.6, 39)], 6)], 50, 46, a=30), G([wpl([(0, -36), (0, 30), (15.6, 39)], 6)], 50, 46, a=-30),
        R(41, 76, 18, 8, "W", "N", 0, 2.5))),
    ("eisstockschiessen", "Eisstockschießen / Curling", *BL,
     tq(R(20, 50, 60, 30, "W", "N", 0, 14), fl(21, 65, 79, 65, 3.5, "butt"), wp("M40,50 V35 H66", 7.5),
        wl(16, 87, 84, 87, 3.5))),
    ("skisprungschanze", "Skisprungschanze / Skispringen", *BL,
     tq(wp("M14,22 Q44,24 56,58 L66,61", 7), wl(22, 28, 22, 86, 4), wl(42, 40, 42, 86, 4), wl(14, 86, 86, 86, 4),
        wl(60, 46, 87, 33, 4), wl(65, 36, 79, 28, 7), wc(84, 22, 5))),
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
