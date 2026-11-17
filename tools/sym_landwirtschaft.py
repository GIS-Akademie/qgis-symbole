"""Sammlung Landwirtschaft: Betrieb und Gebaeude, Kulturen und Nutzung, Technik und Wasser, Schutz und Foerderung.
Orientierung: Kulturartengruppen und Nutzungscodes des Agrarantrags (InVeKoS), Feldblockkataster der Laender,
landwirtschaftliche Standortkarten; Gebietskulissen nach Duengeverordnung (nitratbelastete Gebiete),
benachteiligte Gebiete, Oeko-Regelungen der GAP. Dafuer gibt es keine einheitlichen Kartenzeichen;
eigene Entwuerfe, keine amtlichen Vorlagen.
Stil: helle ockergelbe Fuellung, olivbrauner Strich 5. Die Rahmenform zeigt die Gruppe:
  Quadrat = Betrieb und Gebaeude (Stall = Dach ueber Tier-Silhouette), Kreis = Kultur oder Nutzung (Piktogramm),
  Sechseck = Technik und Wasser, Raute = Schutz- oder Foerdermassnahme, Gebietskulisse.
Linien und Flaechen: olivbraun; Grenzen nach Rang abgestuft, Wege als Doppellinie, Leitungen mit Marken;
Nutzungen als heller Farbton (Acker gelb, Gruenland gelbgruen) mit Muster, Kulissen als Schraffur oder Randband.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "landwirtschaft"
NAME = "Landwirtschaft"
DESC = ("Symbole für Landwirtschaft: Hofstellen, Ställe und Betriebsgebäude, Kulturen und Nutzungen, "
        "Beregnung, Dränage und Weidetechnik, Schutzstreifen, Fördermaßnahmen und Gebietskulissen")
TAGS = "landwirtschaft, agrar, hof, stall, acker, gruenland, kultur, invekos, feldblock, beregnung, draenage"

LW = ("#F3EBC2", "#6B5E12")


def gb(*sh):  # Betrieb und Gebaeude
    return fr_square() + list(sh)


def ku(*sh):  # Kultur oder Nutzung
    return fr_circle() + list(sh)


def tw(*sh):  # Technik und Wasser
    return fr_hex() + list(sh)


def sf(*sh):  # Schutz- oder Foerdermassnahme
    return fr_diamond() + list(sh)


def stall(tier, k=0.62, cy=59):  # Stall: Dach ueber dem Tier
    return gb(PL([(17, 36), (50, 17), (83, 36)], 5.5), *fit(tier, 50, cy, k))


def dot(x, y, r=3.5, f="S"):
    return C(x, y, r, f, "N", 0)


def tuft(x, y, k=1.0, sw=4):
    return [L(x, y, x, y - 18 * k, sw), L(x, y, x - 10 * k, y - 13 * k, sw), L(x, y, x + 10 * k, y - 13 * k, sw)]


def korn(x, y, a):  # Getreidekorn, um a Grad geneigt
    return G([E(0, 0, 5.5, 10, "S", "N", 0)], x, y, 1, a)


def bluete(cx, cy, k=1.0):
    return ([C(x, y, 6.5 * k, "F", "S", 3.5) for x, y in regpoly(cx, cy, 9 * k, 5)] + [dot(cx, cy, 4.5 * k)])


# Tier-Silhouetten im 100er-Raster, Blick nach rechts
RIND = [R(16, 38, 54, 25, "S", "N", 0, 9), R(64, 27, 24, 18, "S", "N", 0, 6), L(68, 28, 63, 18, 4.5), L(84, 28, 89, 18, 4.5),
        L(24, 58, 24, 84, 7, cap="butt"), L(35, 58, 35, 84, 7, cap="butt"), L(54, 58, 54, 84, 7, cap="butt"),
        L(64, 58, 64, 84, 7, cap="butt"), L(17, 42, 11, 62, 4), C(45, 64, 5.5, "S", "N", 0)]
SCHWEIN = [E(44, 54, 28, 18, "S", "N", 0), C(72, 52, 14, "S", "N", 0), R(81, 47, 11, 12, "S", "N", 0, 3),
           PG([(60, 42), (68, 27), (76, 41)], "S"), L(30, 66, 30, 82, 8, cap="butt"), L(42, 68, 42, 82, 8, cap="butt"),
           L(56, 68, 56, 82, 8, cap="butt"), L(67, 64, 67, 82, 8, cap="butt"),
           P("M17,50 q-8,-1 -7,-8 q2,-6 8,-2", "N", "S", 4)]
HUHN = [E(46, 58, 21, 15, "S", "N", 0), PG([(30, 58), (14, 34), (40, 46)], "S"), PG([(56, 52), (61, 36), (75, 42), (64, 62)], "S"),
        C(68, 36, 10, "S", "N", 0), PG([(76, 32), (89, 38), (76, 42)], "S"), C(64, 25, 4.5, "S", "N", 0),
        C(71, 24, 4.5, "S", "N", 0), L(42, 70, 42, 86, 4.5), L(53, 70, 53, 86, 4.5), L(42, 86, 36, 86, 4), L(53, 86, 47, 86, 4)]
PFERD = [E(42, 52, 25, 13, "S", "N", 0), PG([(54, 44), (68, 20), (80, 28), (66, 58)], "S"),
         PG([(68, 20), (74, 18), (92, 36), (87, 43), (72, 34)], "S"), PG([(68, 22), (70, 11), (76, 20)], "S"),
         L(24, 58, 21, 88, 6, cap="butt"), L(34, 60, 34, 88, 6, cap="butt"), L(54, 60, 54, 88, 6, cap="butt"),
         L(62, 56, 66, 88, 6, cap="butt"), P("M19,48 Q9,52 11,72", "N", "S", 5.5)]
SCHAF = [L(36, 62, 36, 84, 6, cap="butt"), L(58, 62, 58, 84, 6, cap="butt"),
         cloud([(28, 54, 14), (46, 50, 18), (64, 54, 14)], "F", "S", 5), E(79, 46, 8, 11, "S", "N", 0),
         L(74, 39, 66, 36, 4.5), L(84, 39, 91, 36, 4.5)]
BIENE = [E(32, 42, 13, 8, "F", "S", 3.5), E(68, 42, 13, 8, "F", "S", 3.5), E(50, 56, 12, 19, "S", "N", 0),
         L(41, 52, 59, 52, 3.5, "F", "butt"), L(40, 61, 60, 61, 3.5, "F", "butt"), C(50, 33, 7, "S", "N", 0)]
SPROSS = [L(50, 88, 50, 40, 5), P("M50,70 Q30,68 24,48 Q44,50 50,70 Z", "S", "N", 0),
          P("M50,56 Q70,54 76,34 Q56,36 50,56 Z", "S", "N", 0)]
SILO = [R(20, 38, 24, 46, "F", "S", 5), P("M20,38 A12,12 0 0 1 44,38", "F", "S", 5), R(54, 30, 26, 54, "F", "S", 5),
        P("M54,30 A13,13 0 0 1 80,30", "F", "S", 5), L(20, 56, 44, 56, 3.5, cap="butt"), L(54, 48, 80, 48, 3.5, cap="butt"),
        L(54, 66, 80, 66, 3.5, cap="butt")]
SCHEUNE = [PG([(20, 82), (20, 48), (33, 24), (67, 24), (80, 48), (80, 82)], "F", "S", 5), R(38, 54, 24, 28, "N", "S", 4.5),
           L(38, 54, 62, 82, 3.5, cap="butt"), L(62, 54, 38, 82, 3.5, cap="butt")]
HALLE = [PG([(16, 80), (16, 46), (50, 26), (84, 46), (84, 80)], "F", "S", 5)]

S = [
    # ---- Betrieb und Gebaeude (Quadrat) ----
    ("hofstelle", "Hofstelle", *LW,
     gb(*fit(house(), 37, 56, 0.6), R(65, 36, 17, 45, "F", "S", 4.5), P("M65,36 A8.5,8.5 0 0 1 82,36", "F", "S", 4.5))),
    ("aussiedlerhof", "Aussiedlerhof", *LW,
     gb(*fit(house(), 50, 42, 0.58), L(18, 70, 82, 70, 4.5), L(18, 81, 82, 81, 4.5))),
    ("stall_rinder", "Stall Rinder", *LW, stall(RIND)),
    ("stall_schweine", "Stall Schweine", *LW, stall(SCHWEIN, 0.62, 58)),
    ("stall_gefluegel", "Stall Geflügel", *LW, stall(HUHN, 0.6, 59)),
    ("stall_pferde", "Stall Pferde / Reiterhof", *LW, stall(PFERD, 0.6, 59)),
    ("stall_schafe", "Stall Schafe / Ziegen", *LW, stall(SCHAF, 0.72, 58)),
    ("scheune", "Scheune / Feldscheune", *LW, gb(*fit(SCHEUNE, 50, 50, 0.92))),
    ("maschinenhalle", "Maschinenhalle", *LW, gb(*HALLE, *gear(50, 61, 15, 8, "S", 5.5, "F"))),
    ("silo", "Silo (Hochsilo, Fahrsilo)", *LW, gb(*fit(SILO, 50, 50, 0.94))),
    ("guellebehaelter", "Güllebehälter", *LW,
     gb(R(18, 40, 64, 38, "F", "S", 5), E(50, 40, 32, 11, "F", "S", 5), wave(27, 65, 46, 4.5, 2, 4.5))),
    ("festmistlager", "Festmistlager", *LW,
     gb(P("M18,76 Q28,44 48,48 Q70,40 82,76 Z", "S", "N", 0), L(14, 80, 86, 80, 5),
        *[P(f"M{x},{y} q-5,-5 0,-10 t0,-10", "N", "S", 4) for x, y in ((36, 40), (52, 36), (68, 42))])),
    ("biogasanlage", "Biogasanlage", *LW,
     gb(R(14, 62, 50, 20, "F", "S", 5), P("M14,62 A25,24 0 0 1 64,62", "F", "S", 5), L(76, 82, 76, 56, 5.5, cap="butt"),
        *fit(flame("S", "F"), 76, 38, 0.38))),
    ("gewaechshaus", "Gewächshaus", *LW,
     gb(PG([(18, 80), (18, 46), (50, 24), (82, 46), (82, 80)], "N", "S", 5), L(18, 46, 82, 46, 4, cap="butt"),
        L(50, 24, 50, 80, 4, cap="butt"), L(34, 46, 34, 80, 4, cap="butt"), L(66, 46, 66, 80, 4, cap="butt"))),
    ("hofladen", "Hofladen / Direktvermarktung", *LW,
     gb(P("M30,52 A20,24 0 0 1 70,52", "N", "S", 5), PG([(20, 52), (80, 52), (72, 82), (28, 82)], "F", "S", 5),
        L(38, 54, 40, 80, 3.5, cap="butt"), L(50, 54, 50, 80, 3.5, cap="butt"), L(62, 54, 60, 80, 3.5, cap="butt"),
        L(24, 66, 76, 66, 3.5, cap="butt"))),
    ("imkerei", "Imkerei / Bienenstand", *LW,
     gb(P("M24,82 V58 A26,36 0 0 1 76,58 V82 Z", "F", "S", 5), L(29, 44, 71, 44, 4, cap="butt"),
        L(24, 57, 76, 57, 4, cap="butt"), L(24, 70, 76, 70, 4, cap="butt"), C(50, 76, 5.5, "S", "N", 0))),
    # ---- Kulturen und Nutzung (Kreis) ----
    ("getreide", "Getreide", *LW,
     ku(L(50, 86, 50, 30, 4.5), korn(50, 22, 0), korn(40, 34, -32), korn(60, 34, 32), korn(40, 49, -32), korn(60, 49, 32),
        korn(40, 64, -32), korn(60, 64, 32))),
    ("mais", "Mais", *LW,
     ku(E(50, 42, 12, 26, "S", "N", 0), P("M50,86 Q24,74 27,40 Q46,58 50,86 Z", "F", "S", 4.5),
        P("M50,86 Q76,74 73,40 Q54,58 50,86 Z", "F", "S", 4.5))),
    ("raps", "Raps / Ölsaaten", *LW,
     ku(L(50, 46, 50, 86, 5), P("M50,76 Q34,74 30,60 Q46,62 50,76 Z", "S", "N", 0),
        *[G([E(0, -12, 8, 11, "S", "N", 0)], 50, 38, 1, a) for a in (45, 135, 225, 315)], dot(50, 38, 5, "F"))),
    ("kartoffeln", "Kartoffeln", *LW,
     ku(G([E(0, 0, 23, 16, "F", "S", 5), dot(-9, -3, 2.8), dot(4, 4, 2.8), dot(10, -6, 2.8)], 41, 58, 1, -20),
        G([E(0, 0, 17, 12, "F", "S", 5), dot(-5, 2, 2.8), dot(6, -3, 2.8)], 63, 36, 1, 25))),
    ("zuckerrueben", "Zuckerrüben / Hackfrüchte", *LW,
     ku(P("M30,46 Q50,38 70,46 Q66,68 50,88 Q34,68 30,46 Z", "S", "N", 0), L(50, 42, 50, 16, 5.5),
        P("M46,42 Q36,32 32,18", "N", "S", 5.5), P("M54,42 Q64,32 68,18", "N", "S", 5.5))),
    ("gemuese", "Gemüse", *LW,
     ku(G([PG([(-10, -16), (10, -16), (0, 34)], "S", "S", 4), L(-5, -4, 5, -4, 3, "F", "butt"), L(-3, 8, 3, 8, 3, "F", "butt"),
           L(0, -18, 0, -34, 5), L(-3, -18, -12, -30, 5), L(3, -18, 12, -30, 5)], 46, 52, 1, 35))),
    ("obstanlage", "Obstanlage", *LW,
     ku(C(50, 58, 23, "S", "N", 0), L(50, 38, 54, 22, 5), P("M54,30 Q68,18 76,28 Q66,38 54,30 Z", "S", "N", 0),
        dot(41, 50, 4.5, "F"))),
    ("weinbau", "Weinbau / Rebfläche", *LW,
     ku(L(50, 34, 50, 18, 5), L(50, 20, 64, 16, 5),
        *[C(x, y, 8, "S", "N", 0) for x, y in ((33, 40), (50, 40), (67, 40), (41.5, 55), (58.5, 55), (50, 70))])),
    ("hopfen", "Hopfen", *LW,
     ku(L(50, 30, 50, 16, 5), E(50, 56, 18, 26, "F", "S", 5), PL([(34, 46), (50, 58), (66, 46)], 4.5),
        PL([(35, 60), (50, 72), (65, 60)], 4.5), L(50, 30, 50, 44, 4.5))),
    ("sonderkultur", "Sonderkultur (Beeren, Spargel, Kräuter)", *LW,
     ku(P("M28,42 Q50,32 72,42 Q74,64 50,86 Q26,64 28,42 Z", "S", "N", 0),
        *[dot(x, y, 2.8, "F") for x, y in ((40, 50), (52, 48), (62, 54), (44, 62), (56, 64), (50, 75))],
        PG(star(50, 34, 16, 6, 5), "F", "S", 3.5))),
    ("gruenland", "Grünland / Mähwiese", *LW,
     ku(*tuft(30, 62, 1.1, 4.5), *tuft(50, 52, 1.2, 4.5), *tuft(70, 62, 1.1, 4.5), L(24, 74, 76, 74, 4.5))),
    ("weide", "Weide", *LW, ku(*fit(RIND, 50, 42, 0.56), *tuft(32, 82, 0.6), *tuft(50, 86, 0.6), *tuft(68, 82, 0.6))),
    ("bluehstreifen", "Blühstreifen / Blühfläche", *LW,
     ku(L(27, 58, 27, 78, 4), L(50, 42, 50, 78, 4), L(73, 58, 73, 78, 4), L(20, 78, 80, 78, 4.5), *bluete(27, 51, 0.75),
        *bluete(50, 32, 0.9), *bluete(73, 51, 0.75))),
    ("zwischenfrucht", "Zwischenfrucht / Begrünung", *LW,
     ku(*fit(SPROSS, 50, 38, 0.66), L(18, 70, 82, 70, 4.5),
        *[L(x, 70, x, 60, 4.5, cap="butt") for x in (24, 33, 67, 76)])),
    ("brache", "Brache / Stilllegung", *LW,
     ku(L(22, 62, 78, 62, 4.5, dash="9 8"), L(28, 76, 72, 76, 4.5, dash="9 8"), *tuft(36, 50, 1.0, 4.5),
        *tuft(64, 46, 1.1, 4.5))),
    # ---- Technik und Wasser (Sechseck) ----
    ("beregnung", "Beregnung / Regner", *LW,
     tw(L(50, 84, 50, 56, 6, cap="butt"), L(38, 84, 62, 84, 5), dot(50, 52, 6), P("M44,46 Q34,22 20,42", "N", "S", 4.5, dash="7 6"),
        P("M56,46 Q66,22 80,42", "N", "S", 4.5, dash="7 6"), L(50, 42, 50, 20, 4.5, dash="7 6"))),
    ("brunnen", "Brunnen", *LW,
     tw(L(34, 58, 34, 32, 4.5), L(66, 58, 66, 32, 4.5), PL([(25, 36), (50, 18), (75, 36)], 5), L(50, 22, 50, 42, 3.5),
        R(44, 40, 12, 11, "S", "N", 0, 2), R(28, 58, 44, 24, "F", "S", 5), L(28, 70, 72, 70, 3.5, cap="butt"),
        L(42, 58, 42, 70, 3.5, cap="butt"), L(58, 58, 58, 70, 3.5, cap="butt"), L(50, 70, 50, 82, 3.5, cap="butt"))),
    ("draenage", "Dränage", *LW,
     tw(L(50, 18, 50, 66, 6, cap="butt"), L(50, 36, 30, 22, 4.5), L(50, 36, 70, 22, 4.5), L(50, 54, 27, 38, 4.5),
        L(50, 54, 73, 38, 4.5), PG([(38, 66), (62, 66), (50, 86)], "S"))),
    ("traenke", "Tränke", *LW,
     tw(*fit(drop("S", "N", 0), 50, 28, 0.3), PG([(22, 50), (78, 50), (72, 72), (28, 72)], "F", "S", 5),
        wave(31, 60, 38, 3.5, 2, 4), L(33, 72, 31, 82, 5), L(67, 72, 69, 82, 5))),
    ("viehtrieb", "Viehtrieb / Viehdurchlass", *LW, tw(*fit(RIND, 50, 40, 0.56), *arrow(28, 76, 72, 76, 5.5, 14))),
    ("waage", "Fahrzeugwaage", *LW,
     tw(L(50, 54, 50, 66, 6, cap="butt"), C(50, 37, 19, "F", "S", 5), L(50, 38, 60, 27, 4.5), dot(50, 38, 4),
        R(22, 64, 56, 11, "S", "N", 0, 3))),
    ("feldrandcontainer", "Feldrandcontainer", *LW,
     tw(PG([(20, 36), (80, 36), (72, 70), (28, 70)], "F", "S", 5), L(37, 36, 40, 70, 4, cap="butt"),
        L(50, 36, 50, 70, 4, cap="butt"), L(63, 36, 60, 70, 4, cap="butt"), L(26, 80, 74, 80, 4.5))),
    # ---- Schutz und Foerderung (Raute) ----
    ("gewaesserrandstreifen", "Gewässerrandstreifen", *LW,
     sf(*tuft(38, 52, 0.85), *tuft(62, 52, 0.85), wave(26, 66, 48, 4.5, 2, 5))),
    ("erosionsschutzstreifen", "Erosionsschutzstreifen", *LW,
     sf(L(26, 70, 74, 48, 5), *fit(drop("S", "N", 0), 34, 44, 0.22),
        G(tuft(0, 0, 0.8, 4.5), 50, 57, 1, -25), G(tuft(0, 0, 0.8, 4.5), 66, 49.5, 1, -25))),
    ("oekoregelung", "Öko-Regelung / Agrarumweltmaßnahme", *LW,
     sf(P("M28,62 Q26,32 58,28 Q60,56 28,62 Z", "S", "N", 0), L(33, 57, 50, 38, 3, "F"), PL([(50, 62), (58, 71), (72, 50)], 5.5))),
    ("oeko_landbau", "Ökologischer Landbau", *LW, sf(T("ÖKO", 50, 50, 15, maxw=50))),
    ("nitratbelastetes_gebiet", "Nitratbelastetes Gebiet", *LW, sf(T("NO", 44, 48, 16), T("3", 67, 57, 11))),
    ("benachteiligtes_gebiet", "Benachteiligtes Gebiet", *LW,
     sf(PL([(26, 66), (41, 38), (50, 52), (58, 36), (74, 66)], 5, "S", "S", True))),
    ("geruchsabstand", "Tierhaltung mit Geruchsabstand", *LW,
     sf(R(37, 56, 26, 16, "S", "N", 0), PG([(32, 57), (50, 44), (68, 57)], "S", "S", 3),
        *[P(f"M{x},38 q-4,-4 0,-8 t0,-8", "N", "S", 3.5) for x in (41, 50, 59)])),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
O0, OL, WS = LW[1], LW[0], "#FFFFFF"

LINIEN = [
    ("Feldblockgrenze", [linie(O0, 0.8)]),
    ("Schlaggrenze", [linie(O0, 0.4)]),
    ("Bewirtschaftungsgrenze", [linie(O0, 0.4, [5, 1.2, 0.6, 1.2])]),
    ("Wirtschaftsweg, befestigt", [linie(O0, 1.2), linie(WS, 0.7)]),
    ("Wirtschaftsweg, unbefestigt", [linie(O0, 0.25, [3, 1], versatz=0.45), linie(O0, 0.25, [3, 1], versatz=-0.45)]),
    ("Dränage, Sammler", [linie(O0, 0.6), marken(mk("filled_arrowhead", 1.8, O0), 12)]),
    ("Dränage, Sauger", [linie(O0, 0.3, [4, 1])]),
    ("Beregnungsleitung", [linie(O0, 0.5), marken(mk("circle", 1.3, WS, O0, 0.3), 8)]),
    ("Weidezaun", [linie(O0, 0.3), marken(mk("line", 1.4, O0, rw=0.3), 3)]),
    ("Hecke, Feldgehölz", [marken(mk("circle", 2.0, OL, O0, 0.25), 1.7)]),
    ("Viehtrieb", [linie(O0 + "59", 2.0), marken(mk("arrowhead", 1.8, O0, rw=0.35), 8)]),
]

FLAECHEN = [
    ("Ackerland", [voll("#F4E6A1"), linie(O0, 0.3)]),
    ("Dauergrünland", [voll("#DCE6A6"), linie(O0, 0.3)]),
    ("Mähweide", [voll("#DCE6A6"), muster(mk("line", 1.0, O0, rw=0.25), 2.4, 3.0, versatz=1.2), linie(O0, 0.3)]),
    ("Dauerkultur Obst", [voll(OL), muster(mk("circle", 1.5, O0), 4.0, versatz=2.0), linie(O0, 0.3)]),
    ("Weinbau", [voll(OL), schraffur(O0, 0.2, 90, 1.5), linie(O0, 0.3)]),
    ("Gemüse, Sonderkultur", [voll(OL), muster(mk("diamond", 1.1, O0), 3.0, versatz=1.5), linie(O0, 0.3)]),
    ("Brache", [voll("#EFEADB"), muster(mk("circle", 0.5, O0), 2.4, versatz=1.2), linie(O0, 0.3)]),
    ("Blühfläche", [voll("#EDF0C0"), muster(mk("cross", 1.2, O0, rw=0.3), 2.8, versatz=1.4), linie(O0, 0.3)]),
    ("Ökologische Vorrangfläche", [schraffur(O0, 0.25, 135, 2.5), linie(O0, 0.4)]),
    ("Gewässerrandstreifen", [voll(O0 + "33"), schraffur(O0, 0.2, 0, 1.5), linie(O0, 0.3)]),
    ("Geruchs-Abstandsbereich Tierhaltung", [voll(O0 + "1F"), linie(O0, 0.5, [0.6, 1.2])]),
    ("Nitratbelastetes Gebiet", [schraffur(O0, 0.25, 45, 3), band(O0 + "80", 1.6), linie(O0, 0.4)]),
    ("Dränfläche", [muster(mk("line", 1.6, O0, rw=0.25, winkel=90), 3.0, 2.0, versatz=1.5), linie(O0, 0.4)]),
    ("Beregnungsfläche", [muster(mk("circle", 1.2, None, O0, 0.25), 3.2, versatz=1.6), linie(O0, 0.4)]),
]
