"""Sammlung Denkmalpflege und Archaeologie: Baudenkmale, Bodendenkmale und Fundstellen, Status und Schutz,
Erinnerung und Vermittlung.
Orientierung: Denkmallisten und Denkmalkartierungen der Landesaemter fuer Denkmalpflege, archaeologische
Fundstellenkarten, Signaturen topografischer Karten fuer Kulturdenkmale (Huegelgrab, Wallanlage, Kirche).
Eine einheitliche amtliche Zeichenvorschrift gibt es nicht; eigene Entwuerfe. Kein Kennzeichen der Haager
Konvention (blau-weisser Schild), kein UNESCO- oder Laenderlogo; Welterbe hat ein eigenes neutrales Zeichen (Stern).
Stil: ziegelrot (helle Fuellung, dunkler Strich 5). Die Rahmenform zeigt die Gruppe:
  Quadrat = Baudenkmal (Sinnbild), Kreis = Bodendenkmal oder Fundstelle, Raute = Status oder Schutz,
  Sechseck = Erinnerung und Vermittlung.
Linien und Flaechen: ziegelrot wie die Punktsymbole. Durchgezogen = erhalten oder nachgewiesen,
gestrichelt = vermutet, abgegangen oder noch nicht festgesetzt; Vollton = Bauwerk, Schraffur = Bodendenkmal.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "denkmal"
NAME = "Denkmalpflege und Archäologie"
DESC = ("Symbole für Denkmalpflege und Archäologie: Baudenkmale, Bodendenkmale und Fundstellen, Grabungen, "
        "Schutzstatus und Erinnerungsorte, dazu Grenzen, Verläufe und Schutzflächen")
TAGS = "denkmal, denkmalpflege, archaeologie, baudenkmal, bodendenkmal, fundstelle, kulturerbe, welterbe"

DK = ("#F3E3D8", "#8C2F1B")


def bd(*sh):  # Baudenkmal
    return fr_square() + list(sh)


def bo(*sh):  # Bodendenkmal, Fundstelle
    return fr_circle() + list(sh)


def st(*sh):  # Status, Schutz
    return fr_diamond() + list(sh)


def er(*sh):  # Erinnerung, Vermittlung
    return fr_hex() + list(sh)


def sf(d):
    return P(d, "S", "N", 0)


def huegel(cx, cy, w, h):
    return sf(f"M{n(cx - w / 2)},{n(cy)} Q{n(cx)},{n(cy - 2 * h)} {n(cx + w / 2)},{n(cy)} Z")


KREUZ = [L(50, 14, 50, 36, 5), L(41, 22, 59, 22, 5)]
HAUS = house("S", "W")
FACH = [L(50, 46, 50, 82, 3.5), L(26, 64, 74, 64, 3.5), L(26, 82, 50, 64, 3.5), L(74, 82, 50, 64, 3.5)]

S = [
    # ---- Baudenkmale (Quadrat) ----
    ("baudenkmal", "Baudenkmal allgemein", *DK, bd(T("D", 50, 50, 46))),
    ("kirche", "Kirche / Sakralbau", *DK,
     bd(R(22, 40, 22, 44, "S", "N", 0), PG([(20, 40), (33, 14), (46, 40)]), PG([(44, 84), (44, 60), (62, 46), (80, 60), (80, 84)]),
        P("M56,84 V72 A6,6 0 0 1 68,72 V84 Z", "F", "N", 0), R(29, 48, 8, 12, "F", "N", 0, 4))),
    ("kapelle", "Kapelle", *DK,
     bd(*KREUZ, PG([(26, 84), (26, 58), (50, 36), (74, 58), (74, 84)]), P("M42,84 V70 A8,8 0 0 1 58,70 V84 Z", "F", "N", 0))),
    ("kloster", "Kloster", *DK,
     bd(*KREUZ, R(16, 38, 68, 46, "S", "N", 0, 2),
        *[P(f"M{x},84 V64 A7,7 0 0 1 {x + 14},64 V84 Z", "F", "N", 0) for x in (23, 43, 63)])),
    ("burg", "Burg", *DK,
     bd(PG([(18, 84), (18, 20), (27, 20), (27, 29), (34, 29), (34, 20), (43, 20), (43, 44), (57, 44), (57, 20), (66, 20),
            (66, 29), (73, 29), (73, 20), (82, 20), (82, 84)]), P("M41,84 V68 A9,9 0 0 1 59,68 V84 Z", "F", "N", 0))),
    ("schloss", "Schloss", *DK,
     bd(R(24, 52, 52, 32, "S", "N", 0), R(15, 42, 16, 42, "S", "N", 0), R(69, 42, 16, 42, "S", "N", 0),
        PG([(13, 42), (23, 20), (33, 42)]), PG([(67, 42), (77, 20), (87, 42)]), PG([(36, 52), (50, 34), (64, 52)]),
        *[R(x, 62, 7, 11, "F", "N", 0, 1) for x in (33, 46.5, 60)])),
    ("stadtmauer", "Stadtmauer / Befestigung", *DK,
     bd(PG([(14, 80), (14, 34), (26, 34), (26, 46), (38, 46), (38, 34), (50, 34), (50, 46), (62, 46), (62, 34), (74, 34),
            (74, 46), (86, 46), (86, 80)]), L(14, 62, 86, 62, 3.5, "F", "butt"), L(38, 62, 38, 80, 3.5, "F", "butt"),
        L(62, 62, 62, 80, 3.5, "F", "butt"), L(50, 46, 50, 62, 3.5, "F", "butt"))),
    ("turm", "Turm", *DK,
     bd(PG([(35, 84), (35, 34), (30, 34), (30, 16), (38, 16), (38, 24), (46, 24), (46, 16), (54, 16), (54, 24), (62, 24),
            (62, 16), (70, 16), (70, 34), (65, 34), (65, 84)]), R(45, 42, 10, 15, "F", "N", 0, 5),
        P("M44,84 V74 A6,6 0 0 1 56,74 V84 Z", "F", "N", 0))),
    ("wohnhaus", "Wohnhaus / Bürgerhaus / Bauernhaus", *DK, bd(*HAUS, R(44, 62, 12, 20, "S", "N", 0))),
    ("fachwerkhaus", "Fachwerkhaus", *DK, bd(*HAUS, *FACH)),
    ("muehle", "Mühle", *DK,
     bd(PG([(38, 86), (44, 42), (56, 42), (62, 86)]), *xcross(50, 40, 25, 5.5), C(50, 40, 5, "F", "S", 3.5))),
    ("technisches_denkmal", "Technisches Denkmal / Industrie- und Verkehrsdenkmal", *DK, bd(*gear(50, 50, 32, 8, "S", 12, "F"))),
    ("bruecke", "Brücke", *DK,
     bd(R(12, 32, 76, 46, "S", "N", 0), P("M20,78 V60 A13,13 0 0 1 46,60 V78 Z", "F", "N", 0),
        P("M54,78 V60 A13,13 0 0 1 80,60 V78 Z", "F", "N", 0))),
    ("brunnen", "Brunnen", *DK,
     bd(PG([(20, 62), (80, 62), (72, 84), (28, 84)]), L(50, 36, 50, 62, 6), P("M50,36 Q50,20 36,24 Q28,27 28,44", "N", "S", 4.5),
        P("M50,36 Q50,20 64,24 Q72,27 72,44", "N", "S", 4.5))),
    ("standbild", "Denkmal / Standbild", *DK,
     bd(C(50, 21, 7.5, "S", "N", 0), PG([(41, 58), (43, 32), (57, 32), (59, 58)]), R(34, 60, 32, 18, "S", "N", 0),
        R(24, 78, 52, 7, "S", "N", 0, 1))),
    ("grabmal", "Grabmal / Friedhof", *DK,
     bd(sf("M30,84 V44 A20,20 0 0 1 70,44 V84 Z"), L(50, 38, 50, 70, 5, "F"), L(40, 49, 60, 49, 5, "F"))),
    ("bildstock", "Bildstock / Wegkreuz", *DK,
     bd(L(50, 16, 50, 76, 8, cap="butt"), L(32, 34, 68, 34, 8, cap="butt"), R(34, 74, 32, 10, "S", "N", 0, 1))),
    ("grenzstein", "Grenzstein", *DK,
     bd(P("M36,80 V36 Q36,22 50,22 Q64,22 64,36 V80", "W", "S", 5), L(20, 80, 80, 80, 5), L(50, 34, 50, 52, 4.5),
        L(42, 43, 58, 43, 4.5))),
    ("gartendenkmal", "Gartendenkmal / Park", *DK, bd(*fit(tree_side("S", "W"), 50, 50, 0.84))),
    # ---- Bodendenkmale und Archaeologie (Kreis) ----
    ("bodendenkmal", "Bodendenkmal allgemein", *DK, bo(T("B", 50, 50, 40))),
    ("fundstelle", "Fundstelle / Einzelfund", *DK, bo(*xcross(50, 50, 17, 8))),
    ("grabhuegel", "Grabhügel", *DK, bo(huegel(50, 64, 56, 20), L(18, 66, 82, 66, 5))),
    ("graeberfeld", "Gräberfeld", *DK, bo(huegel(50, 42, 26, 10), huegel(34, 68, 26, 10), huegel(66, 68, 26, 10))),
    ("siedlung", "Siedlung", *DK, bo(R(33, 50, 34, 23, "W", "S", 5), PL([(26, 53), (50, 31), (74, 53)], 5.5))),
    ("wallanlage", "Wallanlage / Ringwall", *DK, bo(arc(50, 50, 22, 18, 342, 9, cap="butt"), C(50, 50, 5, "S", "N", 0))),
    ("burgstall", "Burgstall / Motte", *DK, bo(PG([(22, 66), (38, 36), (62, 36), (78, 66)]), L(16, 66, 84, 66, 5))),
    ("wuestung", "Wüstung", *DK, bo(P("M30,72 V48 L50,30 L70,48 V72 Z", "N", "S", 5, "butt", "8 5.5"))),
    ("roemische_fundstelle", "Römische Fundstelle", *DK, bo(T("R", 50, 50, 40))),
    ("kastell", "Limes / Kastell", *DK,
     bo(R(25, 32, 50, 36, "W", "S", 5.5, 10), L(50, 32, 50, 68, 3.5), L(25, 50, 75, 50, 3.5))),
    ("altstrasse", "Altstraße / Hohlweg", *DK,
     bo(L(22, 62, 68, 26, 5, cap="butt", dash="10 6"), L(32, 74, 78, 38, 5, cap="butt", dash="10 6"))),
    ("bergbaurelikt", "Bergbaurelikt", *DK,
     bo(L(30, 72, 66, 36, 5), L(70, 72, 34, 36, 5), G([R(-11, -6, 22, 12, "S", "N", 0, 1)], 66, 35, a=45),
        G([R(-11, -6, 22, 12, "S", "N", 0, 1)], 34, 35, a=-45))),
    ("schlachtfeld", "Schlachtfeld", *DK,
     bo(L(32, 72, 70, 24, 5), L(68, 72, 30, 24, 5), L(31, 56, 47, 69, 5), L(69, 56, 53, 69, 5))),
    ("grabung_laufend", "Grabung laufend", *DK,
     bo(R(28, 28, 44, 44, "W", "S", 5), L(30, 54, 54, 30, 4), L(46, 70, 70, 46, 4), L(30, 70, 70, 30, 4))),
    ("grabung_abgeschlossen", "Grabung abgeschlossen", *DK, bo(R(28, 28, 44, 44, "S", "S", 5))),
    ("verdachtsflaeche", "Archäologische Verdachtsfläche", *DK, bo(T("?", 50, 50, 44))),
    ("unterwasserfund", "Unterwasserfund", *DK, bo(*xcross(50, 36, 11, 7), wave(24, 62, 52, 5, 2, 5), wave(28, 76, 44, 5, 2, 5))),
    # ---- Status und Schutz (Raute) ----
    ("ensemble", "Ensemble / Denkmalbereich", *DK, st(T("E", 50, 50, 34))),
    ("welterbe", "Welterbe", *DK, st(PG(star(50, 51, 25, 10, 5)))),
    ("national_wertvoll", "National wertvolles Kulturdenkmal", *DK, st(T("N", 50, 50, 34))),
    ("gefaehrdet", "Gefährdetes Denkmal", *DK, st(T("!", 50, 50, 40))),
    ("saniert", "Saniert / instand gesetzt", *DK, st(PL([(32, 52), (45, 65), (69, 37)], 8))),
    ("abbruch", "Abbruch / Verlust", *DK, st(*xcross(50, 50, 15, 8))),
    # ---- Erinnerung und Vermittlung (Sechseck) ----
    ("erinnerungsort", "Erinnerungsort / Gedenkstätte", *DK, er(*fit(flame("S", "F"), 50, 50, 0.68))),
    ("gedenktafel", "Stolperstein / Gedenktafel", *DK,
     er(R(28, 28, 44, 44, "S", "N", 0, 4), L(37, 41, 63, 41, 4.5, "F"), L(37, 51, 63, 51, 4.5, "F"), L(37, 61, 53, 61, 4.5, "F"))),
    ("infotafel", "Infotafel", *DK, er(C(50, 24, 7, "S", "N", 0), L(50, 40, 50, 74, 11, cap="butt"), L(40, 42, 50, 42, 5, cap="butt"),
                                        L(38, 74, 62, 74, 5, cap="butt"))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
D0, DF = DK[1], DK[0]

LINIEN = [
    ("Grenze Denkmalbereich, Ensemble", [linie(D0, 0.6), marken(mk("triangle", 1.5, D0, dy=0.9), 5)]),
    ("Grenze Grabungsschutzgebiet", [linie(D0, 0.5), marken(mk("line", 1.6, D0, rw=0.3, dy=0.8), 2)]),
    ("Limes, Wallverlauf nachgewiesen", [linie(D0, 1.2)]),
    ("Limes, Wallverlauf vermutet", [linie(D0, 1.2, [3, 1.5])]),
    ("Altstraße", [linie(D0, 1.4), linie(DF, 0.8)]),
    ("Stadtmauerverlauf erhalten", [linie(D0, 0.9), marken(mk("square", 1.8, D0), 4)]),
    ("Stadtmauerverlauf abgegangen", [linie(D0, 0.4, [2, 1]), marken(mk("square", 1.7, DF, rand=D0, rw=0.3), 4)]),
    ("Grabungsschnitt", [linie(D0, 0.35), marken(mk("line", 2.4, D0, rw=0.5), 10)]),
    ("Sichtbeziehung", [linie(D0, 0.3), marken(mk("filled_arrowhead", 2.0, D0), 11)]),
]

FLAECHEN = [
    ("Baudenkmal (Gebäude)", [voll(D0 + "B3"), linie(D0, 0.4)]),
    ("Ensemble, Denkmalbereich", [voll(D0 + "1F"), band(D0 + "59", 1.5), linie(D0, 0.5)]),
    ("Bodendenkmal", [schraffur(D0, 0.25, 45, 2.5), linie(D0, 0.4)]),
    ("Archäologische Verdachtsfläche", [muster(mk("circle", 0.6, D0), 2.4, versatz=1.2), linie(D0, 0.4, [3, 1.5])]),
    ("Grabungsschutzgebiet", [voll(D0 + "14"), linie(D0, 0.5), marken(mk("line", 1.6, D0, rw=0.3, dy=0.8), 2, ecken=1.5)]),
    ("Grabungsfläche", [voll(DF), schraffur(D0, 0.25, 45, 2.5), schraffur(D0, 0.25, 135, 2.5), linie(D0, 0.5)]),
    ("Gartendenkmal", [voll(DF), muster(mk("circle", 1.1, DF, rand=D0, rw=0.3), 3.5, versatz=1.75), linie(D0, 0.4)]),
    ("Pufferzone Welterbe", [band(D0 + "40", 2.0), linie(D0, 0.4, [4, 1.5])]),
    ("Umgebungsschutz", [schraffur(D0, 0.2, 135, 3.5), linie(D0, 0.4, [1, 1.2])]),
    ("Abgegangenes Bauwerk", [voll(DF), linie(D0, 0.4, [2, 1])]),
]
