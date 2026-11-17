"""Sammlung Wasserwirtschaft: Messstellen, Anlagen, Armaturen, Kanalnetz, Bauwerke am Gewaesser, Gebiete.
Orientierung: Leitungs- und Kanalnetzplaene (DIN 2425), Fliessbild-Schaltzeichen fuer Armaturen,
gebraeuchliche Kurzzeichen der Wasserwirtschaft. Eigene Entwuerfe, keine amtlichen Vorlagen.
Stil: hellblaue Fuellung, blauer Strich 5. Die Rahmenform zeigt die Gruppe:
  Kreis = Messstelle/Entnahme, Quadrat = Anlage oder Bauwerk, Raute = Gebiet,
  ohne Rahmen = Armatur oder Netzelement auf der Leitung (Leitung waagerecht durch die Symbolmitte).
"""
from lib import *

KEY = "wasser"
NAME = "Wasserwirtschaft"
DESC = ("Symbole für Wasserwirtschaft: Messstellen, Wasserversorgung und Abwasser (Anlagen, Armaturen, "
        "Kanalnetz), Bauwerke am Gewässer, Wasserschutz- und Überschwemmungsgebiete")
TAGS = "wasser, wasserwirtschaft, abwasser, kanal, pegel, hydrant, trinkwasser, hochwasser"

WB = ("#D6ECFA", "#0B5CAD")


def ms(*sh):  # Messstelle
    return fr_circle() + list(sh)


def an(*sh):  # Anlage, Bauwerk
    return fr_square() + list(sh)


def ant(txt, h=30, mw=64):
    return an(T(txt, 50, 50, h, maxw=mw))


def geb(txt, h=28, mw=46):  # Gebiet
    return fr_diamond() + [T(txt, 50, 50, h, maxw=mw)]


def pipe(x0=4, x1=96):
    return L(x0, 50, x1, 50, 5, cap="butt")


def ufer(*sh):  # Bauwerk am Gewaesser: zwei Uferlinien
    return an(L(20, 28, 80, 28, 4.5), L(20, 72, 80, 72, 4.5), *sh)


BOWTIE = [PG([(24, 30), (50, 50), (24, 70)], "F", "S", 5), PG([(76, 30), (50, 50), (76, 70)], "F", "S", 5)]
FISH = [P("M18,50 Q40,28 64,50 Q40,72 18,50 Z", "S", "N", 0), PG([(60, 50), (82, 36), (82, 64)], "S"),
        C(32, 46, 3, "F", "N", 0)]

S = [
    # ---- Messstellen und Entnahme (Kreis) ----
    ("pegel", "Pegel / Wasserstandsmessstelle", *WB,
     ms(R(40, 16, 20, 68, "F", "S", 4), *[L(40, y, 54 if i % 2 else 49, y, 3.5, cap="butt")
                                           for i, y in enumerate(range(25, 80, 8))])),
    ("abflussmessstelle", "Abflussmessstelle", *WB, ms(T("Q", 50, 50, 36))),
    ("grundwassermessstelle", "Grundwassermessstelle", *WB, ms(PG([(27, 34), (73, 34), (50, 74)], "S"))),
    ("guetemessstelle", "Gütemessstelle / Probenahmestelle", *WB,
     ms(PG([(37.5, 58), (62.5, 58), (69, 72), (66, 77), (34, 77), (31, 72)], "S"),
        P("M45,22 V42 L31,72 Q29,77 34,77 H66 Q71,77 69,72 L55,42 V22", "N", "S", 4.5), L(40, 22, 60, 22, 4.5))),
    ("niederschlagsmessstelle", "Niederschlagsmessstelle", *WB,
     ms(cloud([(35, 44, 11), (50, 38, 14), (65, 44, 11)], "F", "S", 4.5), L(36, 62, 32, 75, 4.5), L(50, 62, 46, 75, 4.5),
        L(64, 62, 60, 75, 4.5))),
    ("brunnen", "Brunnen", *WB, ms(T("B", 50, 50, 38))),
    ("trinkwasserentnahme", "Trinkwasserentnahme / Wasserfassung", *WB, ms(*fit(drop("S", "N", 0), 50, 50, 0.66))),
    # ---- Anlagen (Quadrat) ----
    ("wasserwerk", "Wasserwerk", *WB, ant("WW", 28)),
    ("hochbehaelter", "Hochbehälter", *WB, ant("HB")),
    ("wasserturm", "Wasserturm", *WB,
     an(R(27, 20, 46, 24, "S", "N", 0, 4), PG([(43, 44), (57, 44), (64, 82), (36, 82)], "S"))),
    ("pumpwerk", "Pumpwerk", *WB, an(C(50, 50, 28, "N", "S", 4.5), PG([(38, 30), (38, 70), (74, 50)], "S"))),
    ("druckerhoehungsanlage", "Druckerhöhungsanlage", *WB, ant("DEA", 22, 66)),
    ("klaeranlage", "Kläranlage", *WB, ant("KA")),
    ("kleinklaeranlage", "Kleinkläranlage", *WB, ant("KKA", 22, 66)),
    ("regenueberlauf", "Regenüberlauf", *WB, ant("RÜ")),
    ("regenueberlaufbecken", "Regenüberlaufbecken", *WB, ant("RÜB", 22, 66)),
    ("regenrueckhaltebecken", "Regenrückhaltebecken", *WB, ant("RRB", 22, 66)),
    ("regenklaerbecken", "Regenklärbecken", *WB, ant("RKB", 22, 66)),
    ("hochwasserrueckhaltebecken", "Hochwasserrückhaltebecken", *WB, ant("HRB", 22, 66)),
    ("versickerungsanlage", "Versickerungsanlage / Mulde", *WB,
     an(P("M18,32 Q50,52 82,32", "N", "S", 5), *arrow(34, 50, 34, 82, 4.5, 11), *arrow(50, 56, 50, 84, 4.5, 11),
        *arrow(66, 50, 66, 82, 4.5, 11))),
    ("abscheider", "Abscheider (Leichtflüssigkeit, Fett)", *WB, ant("LFA", 22, 66)),
    ("loeschwasserentnahme", "Löschwasserentnahmestelle", *WB, ant("LW", 28)),
    ("trinkbrunnen", "Trinkbrunnen / Zapfstelle", *WB,
     an(R(44, 58, 12, 26, "S", "N", 0), P("M26,48 H74 Q72,62 50,62 Q28,62 26,48 Z", "S", "N", 0),
        P("M50,46 Q50,22 68,32", "N", "S", 4.5))),
    # ---- Armaturen und Einbauten der Wasserversorgung (auf der Leitung) ----
    ("schieber", "Schieber / Absperrarmatur", *WB, [pipe(4, 24), pipe(76, 96)] + BOWTIE),
    ("absperrklappe", "Absperrklappe", *WB,
     [pipe(4, 30), pipe(70, 96), L(30, 28, 30, 72, 5), L(70, 28, 70, 72, 5), L(30, 72, 70, 28, 5), C(50, 50, 6, "S", "N", 0)]),
    ("rueckflussverhinderer", "Rückflussverhinderer", *WB,
     [pipe(4, 30), pipe(70, 96), PG([(30, 30), (30, 70), (68, 50)], "S", "S", 4), L(70, 28, 70, 72, 5.5)]),
    ("druckminderer", "Druckminderer", *WB,
     [pipe(4, 24), pipe(76, 96), PG([(24, 30), (50, 50), (24, 70)], "S", "S", 5), BOWTIE[1]]),
    ("hydrant_unterflur", "Unterflurhydrant", *WB,
     [pipe(4, 20), pipe(80, 96), C(50, 50, 30, "F", "S", 5), T("H", 50, 50, 28)]),
    ("hydrant_ueberflur", "Überflurhydrant", *WB,
     [pipe(4, 22), pipe(78, 96), R(22, 22, 56, 56, "F", "S", 5), T("H", 50, 50, 28)]),
    ("entlueftung", "Be- und Entlüftungsventil", *WB, [pipe(), L(50, 50, 50, 34, 5, cap="butt"), C(50, 22, 12, "F", "S", 5)]),
    ("entleerung", "Entleerung / Spülauslass", *WB,
     [pipe(), L(50, 50, 50, 68, 5, cap="butt"), PG([(38, 66), (62, 66), (50, 88)], "S")]),
    ("wasserzaehler", "Wasserzähler", *WB,
     [pipe(4, 24), pipe(76, 96), R(24, 30, 52, 40, "F", "S", 5, 4), T("m³", 50, 50, 14)]),
    ("hausanschluss", "Hausanschluss", *WB,
     [L(4, 72, 96, 72, 5, cap="butt"), L(50, 72, 50, 42, 5, cap="butt"), R(38, 18, 24, 24, "S", "N", 0)]),
    ("reduzierung", "Reduzierung / Übergangsstück", *WB,
     [L(4, 50, 34, 50, 8, cap="butt"), pipe(66, 96), PG([(34, 30), (66, 42), (66, 58), (34, 70)], "F", "S", 5)]),
    ("endkappe", "Leitungsende / Endkappe", *WB, [pipe(4, 62), L(62, 30, 62, 70, 8, cap="butt")]),
    ("rohrbruch", "Rohrbruch / Schadstelle", *WB, [pipe(4, 26), pipe(74, 96), PG(star(50, 50, 30, 15, 8), "F", "S", 4.5)]),
    # ---- Kanalnetz ----
    ("schacht", "Schacht", *WB,
     [C(50, 50, 34, "F", "S", 5), L(26, 26, 74, 74, 4.5, cap="butt"), L(26, 74, 74, 26, 4.5, cap="butt")]),
    ("strassenablauf", "Straßenablauf", *WB,
     [R(16, 30, 68, 40, "F", "S", 5)] + [L(x, 30, x, 70, 4, cap="butt") for x in (33, 50, 67)]),
    ("einleitstelle", "Einleitstelle / Auslauf", *WB, arrow(22, 14, 56, 56, 6, 15) + [wave(10, 78, 80, 6, 3, 5)]),
    ("dueker", "Düker", *WB, [PL([(4, 34), (26, 34), (38, 68), (62, 68), (74, 34), (96, 34)], 5, cap="butt")]),
    ("drosselbauwerk", "Drosselbauwerk", *WB,
     [pipe(4, 46), pipe(54, 96), PL([(32, 28), (46, 50), (32, 72)], 5), PL([(68, 28), (54, 50), (68, 72)], 5)]),
    # ---- Bauwerke und Orte am Gewaesser (Quadrat) ----
    ("wehr", "Wehr / Querbauwerk", *WB, ufer(PL([(50, 28), (40, 39), (60, 50), (40, 61), (50, 72)], 5))),
    ("schleuse", "Schleuse", *WB, ufer(PL([(34, 28), (46, 50), (34, 72)], 5), PL([(56, 28), (68, 50), (56, 72)], 5))),
    ("sohlgleite", "Sohlgleite / Sohlrampe", *WB,
     ufer(*[C(x, y, 4.5, "S", "N", 0) for x, y in ((36, 40), (52, 44), (66, 38), (42, 58), (60, 60))])),
    ("durchlass", "Durchlass", *WB,
     an(L(16, 50, 84, 50, 5, cap="butt"), P("M36,24 Q48,50 36,76", "N", "S", 5), P("M64,24 Q52,50 64,76", "N", "S", 5))),
    ("fischaufstieg", "Fischaufstiegsanlage", *WB,
     an(*fit(FISH, 50, 40, 0.8), PL([(20, 84), (38, 84), (38, 76), (58, 76), (58, 68), (80, 68)], 4.5))),
    ("schoepfwerk", "Schöpfwerk", *WB,
     an(C(50, 40, 20, "N", "S", 4.5), PG([(42, 27), (42, 53), (65, 40)], "S"), wave(22, 76, 56, 5, 2, 4.5))),
    ("talsperre", "Talsperre / Staudamm", *WB,
     an(P("M64,18 Q44,50 64,82", "N", "S", 9, cap="butt"), wave(16, 40, 30, 4, 2, 4), wave(16, 60, 30, 4, 2, 4))),
    ("hochwassermarke", "Hochwassermarke / Wasserstand", *WB,
     an(PG([(38, 24), (62, 24), (50, 44)], "S"), L(20, 52, 80, 52, 5), L(30, 64, 70, 64, 4.5), L(41, 76, 59, 76, 4))),
    ("furt", "Furt", *WB,
     an(wave(18, 50, 64, 6, 3, 5), *[C(50, y, 4, "S", "N", 0) for y in (20, 32, 68, 80)])),
    ("quelle", "Quelle", *WB, an(C(50, 32, 13, "N", "S", 5), P("M50,45 Q40,56 50,64 T50,86", "N", "S", 5))),
    ("badestelle", "Badestelle / Badegewässer", *WB,
     an(C(34, 36, 8.5, "S", "N", 0), PL([(44, 46), (62, 40), (76, 48)], 6), wave(18, 62, 64, 5, 3, 4.5),
        wave(18, 76, 64, 5, 3, 4.5))),
    # ---- Gebiete (Raute) ----
    ("wasserschutzgebiet", "Wasserschutzgebiet", *WB, geb("WSG", 18, 52)),
    ("wasserschutzgebiet_zone_1", "Wasserschutzgebiet Zone I (Fassungsbereich)", *WB, geb("I", 32)),
    ("wasserschutzgebiet_zone_2", "Wasserschutzgebiet Zone II (engere Schutzzone)", *WB, geb("II", 32)),
    ("wasserschutzgebiet_zone_3", "Wasserschutzgebiet Zone III (weitere Schutzzone)", *WB, geb("III", 32)),
    ("heilquellenschutzgebiet", "Heilquellenschutzgebiet", *WB, geb("HQS", 18, 52)),
    ("ueberschwemmungsgebiet", "Überschwemmungsgebiet", *WB, geb("ÜSG", 18, 52)),
    ("hochwasserrisikogebiet", "Hochwasserrisikogebiet (HQ100)", *WB, geb("HQ100", 14, 56)),
]

SYMBOLS = S
