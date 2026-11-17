"""Sammlung Naturschutz: Schutzgebiete, Arten und Fundpunkte, Kompensation, Schutz- und Erfassungseinrichtungen.
Orientierung: Schutzgebietskategorien des BNatSchG mit den ueblichen Kurzzeichen, Statusangaben der
Brutvogelkartierung, Massnahmentypen der Eingriffsregelung. Kein bundeseinheitliches Regelwerk; eigene Entwuerfe.
Stil: hellgruene Fuellung, dunkelgruener Strich 5. Die Rahmenform zeigt die Gruppe:
  Quadrat = Schutzgebiet/Schutzobjekt (Kurzzeichen), Kreis = Art, Fundpunkt oder Lebensstaette (Piktogramm),
  Raute = Massnahme (Kurzzeichen), Sechseck = Einrichtung oder Erfassung, Baumkrone = Einzelbaum.
Linien und Flaechen: gruen; Schutzgebiete mit Randband oder Schraffur, Massnahmen gestrichelt umrandet.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "naturschutz"
NAME = "Naturschutz"
DESC = ("Symbole für Schutzgebiete, Artenschutz und Kompensation: Schutzgebietskategorien, Brutvögel nach "
        "Status, Fundpunkte für Artengruppen, Lebensstätten, Maßnahmentypen, Schutz- und Erfassungseinrichtungen")
TAGS = "naturschutz, artenschutz, schutzgebiet, kompensation, eingriffsregelung, kartierung, natura 2000"

GR = ("#DDF0C8", "#1E6B1E")


def sq(txt, h=22, mw=64):
    return fr_square() + [T(txt, 50, 50, h, maxw=mw)]


def dia(txt, h=28, mw=44):
    return fr_diamond() + [T(txt, 50, 50, h, maxw=mw)]


def kr(*sh, dash=None):
    return fr_circle(dash=dash) + list(sh)


def hx(*sh):
    return fr_hex() + list(sh)


def bird(fg="S"):
    return [E(46, 56, 20, 13, fg, "N", 0), C(64, 42, 10, fg, "N", 0), PG([(72, 37), (86, 42), (72, 47)], fg),
            PG([(32, 50), (13, 42), (18, 62)], fg), L(42, 66, 42, 78, 4, fg), L(52, 66, 52, 78, 4, fg)]


BAT = [(50, 34), (54, 27), (57, 36), (67, 30), (85, 33), (94, 49), (83, 45), (77, 56), (69, 49), (62, 61),
       (55, 55), (50, 72), (45, 55), (38, 61), (31, 49), (23, 56), (17, 45), (6, 49), (15, 33), (33, 30),
       (43, 36), (46, 27)]
FROG = [E(50, 54, 13, 17, "S", "N", 0), C(43, 36, 5, "S", "N", 0), C(57, 36, 5, "S", "N", 0),
        PL([(41, 64), (27, 58), (23, 72), (33, 78)], 5), PL([(59, 64), (73, 58), (77, 72), (67, 78)], 5),
        PL([(40, 46), (29, 42), (27, 31)], 4.5), PL([(60, 46), (71, 42), (73, 31)], 4.5)]
LIZARD = [P("M50,22 Q64,36 50,50 Q36,64 54,82", "N", "S", 8), C(50, 20, 7, "S", "N", 0),
          L(56, 34, 68, 28, 4.5), L(46, 36, 34, 30, 4.5), L(46, 58, 34, 62, 4.5), L(54, 60, 66, 66, 4.5)]
DRAGONFLY = [L(50, 26, 50, 80, 5.5), C(50, 23, 6, "S", "N", 0), E(33, 38, 16, 6, "F", "S", 3.5),
             E(67, 38, 16, 6, "F", "S", 3.5), E(35, 51, 14, 5.5, "F", "S", 3.5), E(65, 51, 14, 5.5, "F", "S", 3.5)]
BUTTERFLY = [C(36, 41, 13, "F", "S", 4), C(64, 41, 13, "F", "S", 4), C(39, 61, 10, "F", "S", 4), C(61, 61, 10, "F", "S", 4),
             L(50, 32, 50, 72, 6), L(50, 32, 43, 22, 3.5), L(50, 32, 57, 22, 3.5)]
BEETLE = [L(34, 44, 24, 38, 4), L(66, 44, 76, 38, 4), L(33, 56, 22, 56, 4), L(67, 56, 78, 56, 4), L(35, 68, 25, 76, 4),
          L(65, 68, 75, 76, 4), E(50, 56, 17, 21, "F", "S", 4.5), L(50, 37, 50, 77, 3.5), C(50, 30, 8, "S", "N", 0)]
BEE = [E(32, 42, 13, 8, "F", "S", 3.5), E(68, 42, 13, 8, "F", "S", 3.5), E(50, 56, 12, 19, "S", "N", 0),
       L(41, 52, 59, 52, 3.5, "F", "butt"), L(40, 61, 60, 61, 3.5, "F", "butt"), C(50, 33, 7, "S", "N", 0)]
PAW = [E(50, 63, 16, 13, "S", "N", 0), C(29, 47, 7, "S", "N", 0), C(42, 33, 7.5, "S", "N", 0),
       C(58, 33, 7.5, "S", "N", 0), C(71, 47, 7, "S", "N", 0)]
FLOWER = [C(x, y, 10, "F", "S", 3.5) for x, y in regpoly(50, 50, 16, 5)] + [C(50, 50, 8, "S", "N", 0)]
EGG = [P("M50,10 C66,10 78,40 78,58 C78,76 66,90 50,90 C34,90 22,76 22,58 C22,40 34,10 50,10 Z", "N", "S", 7)]
NEST = [E(34, 47, 8, 11, "F", "S", 3.5), E(66, 47, 8, 11, "F", "S", 3.5), E(50, 43, 8.5, 12, "F", "S", 3.5),
        P("M20,54 H80 A30,22 0 0 1 20,54 Z", "S", "N", 0), L(13, 53, 87, 53, 5), L(22, 60, 10, 66, 3.5), L(78, 60, 90, 66, 3.5)]

S = [
    # ---- Schutzgebiete und Schutzobjekte (Quadrat) ----
    ("nsg", "Naturschutzgebiet", *GR, sq("NSG")),
    ("lsg", "Landschaftsschutzgebiet", *GR, sq("LSG")),
    ("nationalpark", "Nationalpark", *GR, sq("NLP")),
    ("nationales_naturmonument", "Nationales Naturmonument", *GR, sq("NNM")),
    ("biosphaerenreservat", "Biosphärenreservat", *GR, sq("BR", 30, 56)),
    ("naturpark", "Naturpark", *GR, sq("NP", 30, 56)),
    ("naturdenkmal", "Naturdenkmal", *GR, sq("ND", 30, 56)),
    ("geschuetzter_landschaftsbestandteil", "Geschützter Landschaftsbestandteil", *GR, sq("GLB")),
    ("biotop_gesetzlich", "Gesetzlich geschütztes Biotop (§ 30 BNatSchG)", *GR, sq("§30")),
    ("ffh_gebiet", "FFH-Gebiet", *GR, sq("FFH")),
    ("vogelschutzgebiet", "Vogelschutzgebiet", *GR, sq("VSG")),
    ("ffh_lebensraumtyp", "FFH-Lebensraumtyp", *GR, sq("LRT")),
    ("naturwaldreservat", "Naturwaldreservat / Bannwald", *GR, sq("NWR")),
    ("geotop", "Geotop", *GR, sq("GEO")),
    ("kernzone", "Kernzone", *GR, sq("KZ", 30, 56)),
    ("pflegezone", "Pflegezone", *GR, sq("PZ", 30, 56)),
    ("entwicklungszone", "Entwicklungszone", *GR, sq("EZ", 30, 56)),
    # ---- Arten, Fundpunkte, Lebensstaetten (Kreis) ----
    ("vogel_brutnachweis", "Brutvogel: Brutnachweis", *GR,
     [C(50, 50, 44, "S", "S", 5)] + fit(bird("F"), 50, 50, 0.7)),
    ("vogel_brutverdacht", "Brutvogel: Brutverdacht", *GR, kr(*fit(bird(), 50, 50, 0.7))),
    ("vogel_brutzeitfeststellung", "Brutvogel: Brutzeitfeststellung", *GR, kr(*fit(bird(), 50, 50, 0.7), dash="10 8")),
    ("horst", "Horststandort", *GR, kr(*fit(NEST, 50, 50, 0.8))),
    ("brutplatz", "Brutplatz / Niststätte", *GR, kr(*fit(EGG, 50, 50, 0.6))),
    ("vogel_rast", "Rastvogel / Zugvogel", *GR, kr(P("M20,56 Q34,32 50,54 Q66,32 80,56", "N", "S", 6))),
    ("greifvogel", "Greifvogel", *GR,
     kr(PG([(50, 30), (56, 42), (84, 36), (80, 48), (60, 56), (55, 76), (45, 76), (40, 56), (20, 48), (16, 36), (44, 42)], "S"))),
    ("eule", "Eule", *GR,
     kr(P("M30,30 L39,38 Q50,33 61,38 L70,30 V58 Q70,78 50,78 Q30,78 30,58 Z", "N", "S", 4.5),
        C(41, 52, 7, "N", "S", 3.5), C(59, 52, 7, "N", "S", 3.5), C(41, 52, 2.5, "S", "N", 0), C(59, 52, 2.5, "S", "N", 0),
        PG([(46, 61), (54, 61), (50, 69)], "S"))),
    ("fledermausquartier", "Fledermausquartier", *GR, kr(PG(mv([(x - 50, y - 49) for x, y in BAT], 50, 50, 0.84), "S"))),
    ("saeugetier", "Fundpunkt Säugetier", *GR, kr(*PAW)),
    ("amphibien", "Fundpunkt Amphibien", *GR, kr(*fit(FROG, 50, 50, 0.9))),
    ("laichgewaesser", "Amphibien-Laichgewässer", *GR,
     kr(E(50, 54, 30, 19, "N", "S", 4.5), *[C(x, y, 4.5, "S", "N", 0) for x, y in ((38, 52), (50, 60), (61, 50), (49, 46))])),
    ("reptilien", "Fundpunkt Reptilien", *GR, kr(*fit(LIZARD, 50, 50, 0.92))),
    ("fische", "Fundpunkt Fische", *GR, kr(*fit(fish(), 50, 50, 0.8))),
    ("libellen", "Fundpunkt Libellen", *GR, kr(*fit(DRAGONFLY, 50, 48, 0.95))),
    ("tagfalter", "Fundpunkt Tagfalter", *GR, kr(*fit(BUTTERFLY, 50, 52, 1.0))),
    ("kaefer", "Fundpunkt Käfer", *GR, kr(*fit(BEETLE, 50, 48, 0.95))),
    ("wildbienen", "Fundpunkt Wildbienen / Insekten", *GR, kr(*fit(BEE, 50, 50, 1.0))),
    ("fundpunkt_flora", "Fundpunkt Flora", *GR, kr(*fit(FLOWER, 50, 50, 1.0))),
    ("pilze", "Fundpunkt Pilze", *GR, kr(R(43, 50, 14, 27, "N", "S", 4.5, 3), P("M22,52 A28,24 0 0 1 78,52 Z", "S", "S", 4))),
    ("hoehlenbaum", "Höhlenbaum", *GR, treetop(50, 50, 40) + [C(50, 50, 12, "S", "N", 0)]),
    ("habitatbaum", "Habitatbaum", *GR, treetop(50, 50, 40) + [T("H", 50, 50, 30)]),
    # ---- Massnahmen (Raute) ----
    ("kompensation_ausgleich", "Ausgleichsmaßnahme", *GR, dia("A", 34)),
    ("kompensation_ersatz", "Ersatzmaßnahme", *GR, dia("E", 34)),
    ("vermeidungsmassnahme", "Vermeidungsmaßnahme", *GR, dia("V", 34)),
    ("gestaltungsmassnahme", "Gestaltungsmaßnahme", *GR, dia("G", 34)),
    ("schutzmassnahme", "Schutzmaßnahme", *GR, dia("S", 34)),
    ("cef_massnahme", "CEF-Maßnahme (vorgezogener Ausgleich)", *GR, dia("CEF", 20, 50)),
    ("fcs_massnahme", "FCS-Maßnahme", *GR, dia("FCS", 20, 50)),
    ("oekokonto", "Ökokontofläche", *GR, dia("ÖK", 24, 46)),
    # ---- Einrichtungen und Erfassung (Sechseck) ----
    ("nistkasten", "Nistkasten / Nisthilfe", *GR,
     hx(R(35, 36, 30, 38, "N", "S", 4.5), PL([(29, 38), (50, 22), (71, 38)], 4.5), C(50, 52, 6.5, "S", "N", 0))),
    ("fledermauskasten", "Fledermauskasten", *GR,
     hx(R(34, 24, 32, 46, "N", "S", 4.5, 3), L(40, 60, 60, 60, 4.5, cap="butt"), L(50, 70, 50, 80, 4))),
    ("insektenhotel", "Insektenhotel / Insektennisthilfe", *GR,
     hx(R(30, 40, 40, 36, "N", "S", 4.5), PL([(24, 42), (50, 22), (76, 42)], 4.5),
        *[C(x, y, 3.5, "S", "N", 0) for x in (40, 50, 60) for y in (52, 64)])),
    ("amphibienzaun", "Amphibienschutzzaun / Leiteinrichtung", *GR,
     hx(L(20, 62, 80, 62, 5), *[L(x, 62, x, 40, 4.5) for x in (30, 50, 70)], L(22, 46, 78, 46, 3.5))),
    ("amphibientunnel", "Kleintierdurchlass / Amphibientunnel", *GR,
     hx(L(18, 70, 82, 70, 5), P("M34,70 V52 A16,16 0 0 1 66,52 V70", "N", "S", 5))),
    ("querungshilfe", "Querungshilfe / Grünbrücke", *GR,
     hx(P("M18,62 Q50,42 82,62", "N", "S", 6), L(22, 76, 78, 76, 4, dash="8 7"),
        PG([(38, 22), (46, 44), (30, 44)], "S"), PG([(60, 18), (70, 42), (50, 42)], "S"))),
    ("wildtierkorridor", "Wildtierkorridor / Biotopverbund", *GR,
     hx(*arrow(50, 50, 82, 50, 6, 14), *arrow(50, 50, 18, 50, 6, 14))),
    ("beobachtungspunkt", "Beobachtungspunkt / Zählpunkt", *GR, hx(*fit(eye(), 50, 50, 0.8))),
    ("fotofalle", "Fotofalle / Wildkamera", *GR,
     hx(R(42, 30, 14, 8, "S", "N", 0, 2), R(26, 36, 48, 32, "N", "S", 4.5, 5), C(50, 52, 8, "N", "S", 4.5))),
    ("horchbox", "Horchbox / akustische Erfassung", *GR,
     hx(R(42, 34, 16, 32, "S", "N", 0, 5), arc(50, 50, 20, 55, 125, 4), arc(50, 50, 31, 60, 120, 4),
        arc(50, 50, 20, 235, 305, 4), arc(50, 50, 31, 240, 300, 4))),
    ("transekt", "Transekt / Probefläche", *GR,
     hx(L(26, 66, 74, 34, 4.5), C(26, 66, 7, "S", "N", 0), C(74, 34, 7, "S", "N", 0), C(50, 50, 4.5, "S", "N", 0))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
G0, GL = GR[1], GR[0]

LINIEN = [
    ("Schutzgebietsgrenze", [linie(G0, 0.6)]),
    ("Schutzgebietsgrenze, geplant", [linie(G0, 0.6, [4, 1.5])]),
    ("Zonengrenze", [linie(G0, 0.35, [5, 1.5, 0.5, 1.5])]),
    ("Biotopverbundachse", [linie(G0 + "59", 2.0), marken(mk("filled_arrowhead", 2.0, G0), 9)]),
    ("Wildtierkorridor", [linie(G0, 0.5, [3, 1.5]), marken(mk("arrowhead", 2.2, G0, rw=0.4), 9)]),
    ("Flugroute", [linie(G0, 0.4, [0.5, 1.2]), marken(mk("arrowhead", 2.0, G0, rw=0.35), 9)]),
    ("Amphibienschutzzaun", [linie(G0, 0.4), marken(mk("line", 1.4, G0, rw=0.3, dy=0.7), 2.5)]),
    ("Transekt", [linie(G0, 0.4, [2, 1]), marken(mk("line", 1.8, G0, rw=0.35), 10)]),
    ("Gewässerrandstreifen", [linie(G0 + "59", 1.8), linie(G0, 0.3)]),
]

FLAECHEN = [
    ("Naturschutzgebiet", [voll(GL + "80"), band(G0, 1.2), linie(G0, 0.3)]),
    ("Landschaftsschutzgebiet", [band(G0 + "66", 1.6), linie(G0, 0.4)]),
    ("Nationalpark", [voll(GL + "80"), schraffur(G0, 0.2, 0, 2), band(G0, 1.2), linie(G0, 0.3)]),
    ("Biosphärenreservat", [schraffur(G0, 0.2, 90, 2.5), linie(G0, 0.5, [6, 1.5])]),
    ("Naturpark", [band(G0 + "40", 1.6), linie(G0, 0.5, [5, 2])]),
    ("FFH-Gebiet", [schraffur(G0, 0.25, 45, 2.5), linie(G0, 0.4)]),
    ("Vogelschutzgebiet", [schraffur(G0, 0.25, 135, 2.5), linie(G0, 0.4)]),
    ("Natura 2000, FFH- und Vogelschutzgebiet",
     [schraffur(G0, 0.25, 45, 2.5), schraffur(G0, 0.25, 135, 2.5), linie(G0, 0.4)]),
    ("Gesetzlich geschütztes Biotop", [voll(GL), schraffur(G0, 0.2, 45, 1.2), linie(G0, 0.4)]),
    ("FFH-Lebensraumtyp", [voll(GL + "80"), muster(mk("circle", 0.6, G0), 2.2, versatz=1.1), linie(G0, 0.3)]),
    ("Naturdenkmal, flächenhaft", [voll(GL), linie(G0, 0.8)]),
    ("Geschützter Landschaftsbestandteil", [linie(G0, 0.3), marken(mk("semi_circle", 1.6, G0, winkel=180), 3.5)]),
    ("Kernzone", [voll(G0 + "99"), linie(G0, 0.3)]),
    ("Pflegezone", [voll(G0 + "59"), linie(G0, 0.3)]),
    ("Entwicklungszone", [voll(G0 + "26"), linie(G0, 0.3)]),
    ("Kompensationsfläche", [schraffur(G0, 0.25, 135, 3), linie(G0, 0.5, [3, 1.5])]),
    ("Ökokontofläche", [muster(mk("diamond", 1.2, G0), 3.5, versatz=1.75), linie(G0, 0.5, [3, 1.5])]),
    ("Habitatfläche, Revier", [voll(GL + "80"), linie(G0, 0.3, [1, 1])]),
    ("Untersuchungsgebiet", [linie(G0, 0.6, [6, 2, 1, 2])]),
]
