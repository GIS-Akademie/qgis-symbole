"""Sammlung Landschaftsplanung: Gehoelze, Biotop- und Nutzungstypen, Massnahmen, Erholung und Landschaftsbild.
Orientierung: Bestands- und Massnahmenplaene der Landschaftsplanung und der landschaftspflegerischen
Begleitplanung, Gehoelzdarstellung wie in Lageplaenen. Kein bundeseinheitliches Regelwerk; eigene Entwuerfe.
Stil: hellgruene Fuellung, dunkelgruener Strich 5 (Wasser blau). Die Form zeigt die Gruppe:
  Draufsicht ohne Rahmen = Gehoelz, Quadrat = Biotop- oder Nutzungstyp, gestricheltes Quadrat = Massnahme,
  Kreis = Erholung, Landschaftsbild, Klima.
"""
from lib import *

KEY = "landschaftsplanung"
NAME = "Landschaftsplanung"
DESC = ("Symbole für Landschaftsplanung und landschaftspflegerische Begleitplanung: Bäume und Gehölze nach "
        "Maßnahme, Biotop- und Nutzungstypen, Maßnahmenarten, Erholung, Landschaftsbild und Klima")
TAGS = "landschaftsplanung, lbp, gruenordnung, baum, gehoelz, biotoptyp, massnahme, erholung"

LG = ("#CDE8B5", "#2E6B2E")
BL = ("#D6ECFA", "#0B5CAD")
ST = ("#E6E6E6", "#4D4D4D")
BR = ("#E8D5B5", "#6B4423")


def bt(*sh):  # Biotop- oder Nutzungstyp
    return fr_square() + list(sh)


def mn(*sh):  # Massnahme
    return [R(7, 7, 86, 86, "F", "S", 5, 8, "12 8")] + list(sh)


def kr(*sh):  # Erholung, Landschaftsbild
    return fr_circle() + list(sh)


def tuft(x, y, k=1.0, sw=4):
    return [L(x, y, x, y - 18 * k, sw), L(x, y, x - 10 * k, y - 13 * k, sw), L(x, y, x + 10 * k, y - 13 * k, sw)]


def dot(x, y, r=3.5):
    return C(x, y, r, "S", "N", 0)


def laub(cx, cy, k):
    return fit(tree_side(), cx, cy, k)


def nadel(cx, cy, k):
    return fit(conifer_side(), cx, cy, k)


BLUME = ([L(50, 46, 50, 92, 5), P("M50,76 Q32,74 28,58 Q46,60 50,76 Z", "S", "N", 0),
          P("M50,68 Q68,66 72,50 Q54,52 50,68 Z", "S", "N", 0)]
         + [C(x, y, 9, "F", "S", 3.5) for x, y in regpoly(50, 28, 14, 5)] + [C(50, 28, 7, "S", "N", 0)])
SCHILF = [L(30, 86, 30, 34, 4), L(50, 86, 50, 22, 4), L(70, 86, 70, 38, 4), E(30, 30, 5, 12, "S", "N", 0),
          E(50, 20, 5, 12, "S", "N", 0), E(70, 34, 5, 12, "S", "N", 0), wave(10, 88, 80, 5, 3, 4)]
TEICH = [P("M14,52 C10,30 34,18 54,22 C76,18 94,36 88,56 C86,76 62,84 42,80 C24,82 16,70 14,52 Z", "N", "S", 5),
         wave(32, 46, 30, 4, 2, 3.5), wave(44, 60, 30, 4, 2, 3.5)]
STEINE = [E(32, 68, 22, 15, "N", "S", 4.5), E(70, 70, 20, 14, "N", "S", 4.5), E(52, 44, 21, 15, "N", "S", 4.5)]
STAMM = [R(8, 36, 76, 28, "N", "S", 5, 14), E(80, 50, 11, 14, "F", "S", 5), C(80, 50, 4.5, "N", "S", 3),
         L(22, 46, 50, 46, 3), L(30, 55, 62, 55, 3)]
TISCH = [L(22, 36, 78, 36, 7), L(36, 38, 26, 82, 5), L(64, 38, 74, 82, 5), L(6, 60, 30, 60, 6), L(70, 60, 94, 60, 6)]
MAEANDER = [P("M8,62 Q22,26 40,50 T68,50", "N", "S", 7)] + arrow(68, 50, 90, 34, 7, 16)

S = [
    # ---- Gehoelze (Draufsicht) ----
    ("baum_laub", "Laubbaum", *LG, treetop(50, 50, 41) + [dot(50, 50, 6)]),
    ("baum_nadel", "Nadelbaum", *LG, [PG(star(50, 50, 45, 25, 8), "F", "S", 4), dot(50, 50, 6)]),
    ("obstbaum", "Obstbaum", *LG, treetop(50, 50, 41) + [dot(36, 44, 6), dot(60, 38, 6), dot(54, 64, 6)]),
    ("kopfbaum", "Kopfbaum", *LG, treetop(50, 50, 30, k=6) + [dot(50, 50, 12)]),
    ("baum_solitaer", "Solitärbaum / prägender Einzelbaum", *LG,
     treetop(50, 50, 41) + [C(50, 50, 21, "N", "S", 4), dot(50, 50, 6)]),
    ("baum_pflanzung", "Baum, Neupflanzung", *LG, treetop(50, 50, 41) + cross(50, 50, 20, 6)),
    ("baum_erhalt", "Baum, zu erhalten", *LG, [C(50, 50, 46, "N", "S", 3.5)] + treetop(50, 50, 33) + [dot(50, 50, 6)]),
    ("baum_faellung", "Baum, Fällung", *LG, treetop(50, 50, 41) + xcross(50, 50, 30, 6)),
    ("baum_schutz", "Baum, Schutz während der Bauzeit", *LG,
     [R(6, 6, 88, 88, "N", "S", 4, 0, "11 7")] + treetop(50, 50, 31) + [dot(50, 50, 6)]),
    ("baumgruppe", "Baumgruppe", *LG,
     treetop(33, 62, 24, sw=3.5, k=7) + treetop(67, 62, 24, sw=3.5, k=7) + treetop(50, 34, 24, sw=3.5, k=7)),
    ("baumreihe", "Baumreihe", *LG,
     [L(4, 50, 96, 50, 3)] + [C(x, 50, 13, "F", "S", 4) for x in (20, 50, 80)] + [dot(x, 50) for x in (20, 50, 80)]),
    ("allee", "Allee", *LG,
     [L(4, 50, 96, 50, 3, dash="6 6")] + [C(x, y, 11, "F", "S", 4) for x in (20, 50, 80) for y in (28, 72)]
     + [dot(x, y, 3) for x in (20, 50, 80) for y in (28, 72)]),
    ("strauch", "Strauch / Gebüsch", *LG, treetop(50, 50, 30, k=6)),
    ("hecke", "Hecke", *LG,
     treetop(21, 50, 15, sw=3.5, k=6) + treetop(50, 50, 15, sw=3.5, k=6) + treetop(79, 50, 15, sw=3.5, k=6)),
    ("feldgehoelz", "Feldgehölz", *LG,
     [cloud([(26, 56, 19), (50, 44, 25), (74, 56, 19)], "F", "S", 4.5), dot(34, 56), dot(50, 42), dot(66, 56)]),
    # ---- Biotop- und Nutzungstypen (Quadrat) ----
    ("wald_laub", "Laubwald", *LG, bt(*laub(34, 54, 0.5), *laub(64, 48, 0.66))),
    ("wald_nadel", "Nadelwald", *LG, bt(*nadel(34, 54, 0.5), *nadel(64, 48, 0.66))),
    ("wald_misch", "Mischwald", *LG, bt(*laub(35, 52, 0.58), *nadel(66, 50, 0.62))),
    ("aufforstung", "Aufforstung / Waldentwicklung", *LG,
     bt(L(18, 76, 82, 76, 4), *nadel(30, 60, 0.3), *nadel(50, 54, 0.42), *nadel(70, 60, 0.3))),
    ("gruenland", "Grünland / Wiese", *LG, bt(*tuft(32, 46, 0.8), *tuft(64, 42, 0.8), *tuft(44, 76, 0.8), *tuft(72, 74, 0.8))),
    ("extensivgruenland", "Extensivgrünland / artenreiche Wiese", *LG,
     bt(*tuft(30, 78, 0.8), *tuft(70, 78, 0.8), *tuft(50, 74, 0.7), *fit(BLUME, 50, 40, 0.5))),
    ("acker", "Acker", *LG, bt(*[L(22, y, 78, y, 4) for y in (30, 43, 57, 70)])),
    ("brache", "Brache / Sukzessionsfläche", *LG,
     bt(L(22, 70, 78, 70, 4, dash="9 8"), L(22, 82, 78, 82, 4, dash="9 8"), *tuft(34, 56, 0.9), *tuft(64, 50, 1.0))),
    ("bluehflaeche", "Blühfläche / Blühstreifen", *LG, bt(*fit(BLUME, 50, 50, 0.72))),
    ("streuobstwiese", "Streuobstwiese", *LG,
     bt(*laub(50, 46, 0.6), dot(44, 36, 3), dot(57, 40, 3), dot(48, 48, 3), *tuft(26, 82, 0.6), *tuft(76, 82, 0.6))),
    ("magerrasen", "Magerrasen / Trockenrasen", *LG,
     bt(*tuft(32, 52, 0.55), *tuft(62, 44, 0.55), *tuft(48, 78, 0.55), dot(30, 72), dot(70, 68), dot(46, 34), dot(74, 82))),
    ("heide", "Heide", *LG,
     bt(*treetop(34, 60, 12, sw=3.5, k=5), *treetop(64, 62, 12, sw=3.5, k=5), *treetop(50, 38, 12, sw=3.5, k=5))),
    ("moor", "Moor / Sumpf", *LG,
     bt(L(22, 62, 78, 62, 4.5), L(32, 73, 68, 73, 4.5), L(42, 83, 58, 83, 4), *tuft(50, 54, 1.4))),
    ("roehricht", "Röhricht", *LG, bt(*fit(SCHILF, 50, 50, 0.72))),
    ("feuchtwiese", "Feuchtwiese / Nasswiese", *LG, bt(*tuft(34, 52, 0.9), *tuft(64, 48, 0.9), wave(22, 74, 56, 5, 2, 4.5))),
    ("stillgewaesser", "Stillgewässer / Kleingewässer", *BL, bt(*fit(TEICH, 50, 50, 0.76))),
    ("fliessgewaesser", "Fließgewässer", *BL, bt(P("M18,62 Q32,30 50,50 T82,38", "N", "S", 7))),
    ("graben", "Graben", *BL,
     bt(L(18, 50, 82, 50, 5), *[L(x, 50, x, 38 if i % 2 else 62, 4, cap="butt") for i, x in enumerate((26, 38, 50, 62, 74))])),
    ("ufergehoelz", "Ufergehölz", *LG,
     bt(wave(18, 74, 64, 5, 3, 4.5), *treetop(32, 44, 14, sw=3.5, k=6), *treetop(62, 40, 17, sw=3.5, k=6))),
    ("lesesteinhaufen", "Lesesteinhaufen / Steinriegel", *ST, bt(*fit(STEINE, 50, 50, 0.72))),
    ("trockenmauer", "Trockenmauer", *ST,
     bt(R(20, 34, 60, 32, "N", "S", 4.5), L(20, 50, 80, 50, 4), L(40, 34, 40, 50, 4), L(62, 34, 62, 50, 4),
        L(30, 50, 30, 66, 4), L(52, 50, 52, 66, 4), L(70, 50, 70, 66, 4))),
    ("totholz", "Totholz", *BR, bt(*fit(STAMM, 50, 50, 0.72))),
    # ---- Massnahmen (gestricheltes Quadrat) ----
    ("massnahmenflaeche", "Maßnahmenfläche", *LG, mn(T("M", 50, 50, 36))),
    ("pflanzung", "Pflanzung / Gehölzpflanzung", *LG,
     mn(L(46, 82, 46, 44, 5), P("M46,64 Q28,62 24,46 Q42,48 46,64 Z", "S", "N", 0),
        P("M46,54 Q64,52 68,36 Q50,38 46,54 Z", "S", "N", 0), *cross(72, 72, 9, 4.5))),
    ("entsiegelung", "Entsiegelung", *LG,
     mn(PL([(38, 16), (46, 38), (38, 54), (58, 68), (52, 84)], 4.5), PL([(46, 38), (66, 34), (82, 44)], 4.5))),
    ("rueckbau", "Rückbau / Abriss", *LG, mn(*fit(house(), 50, 52, 0.62), L(22, 80, 78, 24, 5.5))),
    ("mahd", "Mahd / Grünlandpflege", *LG,
     mn(*tuft(32, 48, 0.9), *tuft(64, 48, 0.9), L(20, 60, 80, 60, 4.5), *arrow(28, 76, 72, 76, 4, 11))),
    ("beweidung", "Beweidung", *LG,
     mn(L(18, 40, 82, 40, 4), L(18, 56, 82, 56, 4), L(30, 28, 30, 70, 5.5), L(70, 28, 70, 70, 5.5), *tuft(50, 84, 0.6))),
    ("sukzession", "Sukzession / Eigenentwicklung", *LG,
     mn(*tuft(26, 76, 0.7), *treetop(48, 66, 11, sw=3.5, k=5), *laub(72, 52, 0.46), L(18, 80, 82, 80, 3.5))),
    ("waldumbau", "Waldumbau", *LG, mn(*nadel(26, 50, 0.44), *arrow(40, 52, 58, 52, 4.5, 10), *laub(74, 50, 0.44))),
    ("wiedervernaessung", "Wiedervernässung", *BL, mn(*fit(drop("N", "S", 6), 40, 52, 0.56), *arrow(70, 76, 70, 28, 5, 13))),
    ("gewaesserrenaturierung", "Gewässerrenaturierung", *BL, mn(*fit(MAEANDER, 50, 50, 0.76))),
    # ---- Erholung, Landschaftsbild, Klima (Kreis) ----
    ("aussichtspunkt", "Aussichtspunkt", *LG,
     kr(*[L(50, 70, *pt(50, 70, 44, a), 4.5) for a in (-66, -33, 0, 33, 66)], dot(50, 70, 8))),
    ("sichtachse", "Sichtachse / Blickbeziehung (nach rechts, drehbar)", *LG,
     kr(PL([(78, 28), (28, 50), (78, 72)], 4.5), dot(28, 50, 8), *arrow(40, 50, 76, 50, 4, 11))),
    ("landmarke", "Landmarke / prägendes Landschaftselement", *LG, kr(PG(star(50, 52, 32, 13, 5), "S"))),
    ("rastplatz", "Rastplatz", *LG, kr(*fit(TISCH, 50, 50, 0.66))),
    ("bank", "Bank", *LG,
     kr(L(24, 54, 76, 54, 6), L(24, 38, 76, 38, 5), L(30, 54, 30, 72, 5), L(70, 54, 70, 72, 5), L(28, 38, 28, 54, 4),
        L(72, 38, 72, 54, 4))),
    ("schutzhuette", "Schutzhütte", *LG, kr(*fit(house(), 50, 50, 0.66), R(44, 52, 12, 19, "S", "N", 0))),
    ("grillplatz", "Grillplatz / Feuerstelle", *LG,
     kr(*fit(flame("S", "F"), 50, 42, 0.44), L(28, 80, 72, 68, 5.5), L(28, 68, 72, 80, 5.5))),
    ("spielplatz", "Spielplatz", *LG, kr(*fit(bucket("S", 4), 50, 52, 1.25))),
    ("badestelle", "Badestelle", *BL, kr(*fit(swimmer(), 50, 50, 0.66))),
    ("infotafel", "Infotafel / Lehrpfad", *LG,
     kr(L(34, 56, 34, 80, 5), L(66, 56, 66, 80, 5), R(24, 24, 52, 34, "N", "S", 4.5, 3), dot(50, 32, 3),
        L(50, 39, 50, 50, 4.5))),
    ("wanderweg", "Wanderweg", *LG, kr(*fit(person(), 50, 50, 0.66))),
    ("radweg", "Radweg", *LG, kr(*fit(bike(), 50, 50, 0.68))),
    ("reitweg", "Reitweg", *LG,
     kr(P("M32,72 V48 A18,18 0 0 1 68,48 V72", "N", "S", 9, cap="butt"), dot(32, 60, 2.5), dot(68, 60, 2.5))),
    ("wanderparkplatz", "Wanderparkplatz", *LG, kr(T("P", 50, 50, 40))),
    ("kaltluftbahn", "Kaltluftbahn / Frischluftschneise (nach rechts, drehbar)", *BL,
     kr(*arrow(22, 50, 78, 50, 5.5, 14), wave(24, 32, 44, 4, 2, 4), wave(24, 70, 44, 4, 2, 4))),
]

SYMBOLS = S
