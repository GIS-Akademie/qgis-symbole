"""Sammlung Brand- und Katastrophenschutz: Feuerwehr und Loeschwasser, vorbeugender Brandschutz, Rettung und
Flucht, Katastrophenschutz und Einsatzorganisation, Gefahrenstellen.
Orientierung: Feuerwehrplaene nach DIN 14095, grafische Symbole fuer das Feuerwehrwesen nach DIN 14034-6,
Sicherheitszeichen nach DIN EN ISO 7010, taktische Zeichen (FwDV/DV 102). Keine Kopien dieser Zeichen,
sondern eigene schlichte Sinnbilder, die sich daran anlehnen; fuer Feuerwehrplaene im Sinne der DIN 14095
und fuer die Sicherheitskennzeichnung sind die genormten Zeichen zu verwenden.
Stil: immer abgerundetes Quadrat mit weissem Sinnbild. Die Farbe zeigt die Gruppe:
  rot = Feuerwehr und Brandschutz, gruen = Rettung und Flucht,
  blau = Katastrophenschutz und Einsatzorganisation.
  Ausnahme Gefahren: gelbes Dreieck (Spitze oben) mit schwarzem Sinnbild.
Linien und Flaechen: Farben der Punktsymbole (rot = Feuerwehr, Brandwand, Absperrung; gruen = Rettungsweg,
Sammelstelle; blau = Evakuierung, Hochwasser, Einsatzabschnitt; gelb-schwarz = Gefahrenbereich);
Wege mit Richtungspfeilen, durchgezogen = Bestand, gestrichelt = geplant.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "brandschutz"
NAME = "Brand- und Katastrophenschutz"
DESC = ("Symbole für Brand- und Katastrophenschutz: Feuerwehr und Löschwasserversorgung, vorbeugender "
        "Brandschutz, Rettung und Flucht, Katastrophenschutz, Einsatzorganisation und Gefahrenstellen")
TAGS = ("brandschutz, feuerwehr, katastrophenschutz, rettung, loeschwasser, hydrant, feuerwehrplan, "
        "evakuierung, gefahrenabwehr, bevoelkerungsschutz")

RT = ("#D0021B", "#8B0000")   # Feuerwehr und Brandschutz
GN = ("#1E8E3E", "#0F5A26")   # Rettung und Flucht
BL = ("#1F5FA8", "#0D3C73")   # Katastrophenschutz und Einsatzorganisation
GE = ("#FFD400", "#1A1A1A")   # Gefahren


def q(*sh):  # farbiges Quadrat
    return fr_square() + list(sh)


def qt(txt, h=36, mw=66):
    return q(T(txt, 50, 50, h, "W", maxw=mw))


def gf(*sh):  # Gefahr: gelbes Dreieck, Spitze oben
    return [PG([(50, 9), (94, 87), (6, 87)], "F", "S", 6)] + list(sh)


def wl(x1, y1, x2, y2, sw=5, cap="round"):
    return L(x1, y1, x2, y2, sw, "W", cap)


def wa(x1, y1, x2, y2, sw=7, head=18):  # weisser Pfeil
    return arrow(x1, y1, x2, y2, sw, head, "W")


def wdrop(cx, cy, k, voll_=True):
    return fit(drop("W", "N", 0) if voll_ else drop("N", "W", 4.5 / k), cx, cy, k)


GIEBEL = [(50, 16), (85, 43), (85, 83), (15, 83), (15, 43)]
HEART = ("M50,84 C22,62 14,46 14,34 C14,22 23,15 32,15 C40,15 47,19 50,27 C53,19 60,15 68,15 "
         "C77,15 86,22 86,34 C86,46 78,62 50,84 Z")
STEIG = wa(34, 84, 34, 16, 8, 20) + [wl(20, 84, 48, 84, 6.5)]
LEITER = ([wl(24, 82, 58, 18, 6), wl(44, 84, 78, 20, 6)]
          + [wl(24 + 34 * t, 82 - 64 * t, 44 + 34 * t, 84 - 64 * t, 4.5) for t in (0.14, 0.38, 0.62, 0.86)])

S = [
    # ---- Feuerwehr: Standorte und Loeschwasser (rot) ----
    ("feuerwache", "Feuerwache", *RT,
     q(R(16, 42, 50, 40, "W", "N", 0, 2), R(64, 16, 20, 66, "W", "N", 0, 2), R(22, 56, 16, 26, "F", "N", 0),
       R(43, 56, 16, 26, "F", "N", 0), R(69, 24, 10, 12, "F", "N", 0))),
    ("feuerwehrgeraetehaus", "Feuerwehrgerätehaus", *RT, q(PG(GIEBEL, "W"), R(34, 52, 32, 31, "F", "N", 0))),
    ("hydrant_unterflur", "Unterflurhydrant", *RT, q(C(50, 50, 32, "W", "N", 0), T("H", 50, 50, 34, "F"))),
    ("hydrant_ueberflur", "Überflurhydrant", *RT,
     q(R(39, 30, 22, 50, "W", "N", 0, 2), P("M37,32 A13,13 0 0 1 63,32 Z", "W", "N", 0), R(45, 12, 10, 9, "W", "N", 0, 2),
       R(26, 42, 14, 14, "W", "N", 0, 3), R(60, 42, 14, 14, "W", "N", 0, 3), R(28, 78, 44, 9, "W", "N", 0, 3))),
    ("loeschwasserteich", "Löschwasserteich", *RT,
     q(E(50, 54, 35, 25, "N", "W", 6), wave(30, 48, 40, 4.5, 2, 5, "W"), wave(30, 62, 40, 4.5, 2, 5, "W"))),
    ("loeschwasserzisterne", "Löschwasserzisterne / Löschwasserbehälter", *RT,
     q(wl(16, 26, 84, 26, 6), R(43, 26, 14, 16, "W", "N", 0), R(20, 40, 60, 44, "W", "N", 0, 12),
       *fit(drop("F", "N", 0), 50, 61, 0.38))),
    ("saugstelle", "Saugstelle / Löschwasserentnahme aus Gewässer", *RT,
     q(P("M18,24 H56 Q68,24 68,36 V58", "N", "W", 8), R(60, 54, 16, 12, "W", "N", 0, 2),
       wave(16, 76, 68, 5, 3, 5.5, "W"))),
    ("steigleitung_trocken", "Steigleitung trocken", *RT, q(*STEIG, *wdrop(68, 52, 0.52, False))),
    ("steigleitung_nass", "Steigleitung nass", *RT, q(*STEIG, *wdrop(68, 52, 0.52))),
    # ---- Feuerwehr: Flaechen, Zugang und Technik (rot) ----
    ("feuerwehrzufahrt", "Feuerwehrzufahrt", *RT, q(T("FW", 50, 33, 26, "W"), *wa(16, 70, 85, 70, 9, 22))),
    ("aufstellflaeche", "Aufstellfläche für Hubrettungsfahrzeuge", *RT, q(*LEITER)),
    ("bewegungsflaeche", "Bewegungsfläche der Feuerwehr", *RT,
     q(*wa(50, 50, 50, 15, 6.5, 16), *wa(50, 50, 50, 85, 6.5, 16), *wa(50, 50, 15, 50, 6.5, 16),
       *wa(50, 50, 85, 50, 6.5, 16))),
    ("feuerwehrschluesseldepot", "Feuerwehrschlüsseldepot (FSD)", *RT,
     q(C(33, 50, 14, "N", "W", 8), wl(47, 50, 84, 50, 8), wl(68, 50, 68, 65, 7), wl(81, 50, 81, 62, 7))),
    ("brandmeldezentrale", "Brandmeldezentrale (BMZ)", *RT, qt("BMZ", 26)),
    ("feuerwehr_bedienfeld", "Feuerwehr-Bedienfeld (FBF)", *RT, qt("FBF", 26)),
    ("feuerloescher", "Feuerlöscher", *RT,
     q(R(36, 36, 30, 50, "W", "N", 0, 9), R(46, 24, 10, 14, "W", "N", 0), wl(40, 21, 66, 21, 6.5),
       P("M36,46 Q20,46 20,60 V68", "N", "W", 5.5))),
    ("wandhydrant", "Wandhydrant", *RT,
     q(C(46, 46, 25, "N", "W", 8), C(46, 46, 7, "W", "N", 0), wl(71, 48, 71, 82, 7), R(63, 78, 16, 9, "W", "N", 0, 2))),
    ("rauchabzug", "Rauchabzug (RWA)", *RT,
     q(cloud([(32, 34, 12), (50, 28, 15), (68, 34, 12)], "W", "W", 3), *wa(50, 88, 50, 54, 9, 20))),
    ("sprinklerzentrale", "Sprinklerzentrale", *RT,
     q(wl(20, 20, 80, 20, 8), wl(50, 20, 50, 38, 8), wl(36, 42, 64, 42, 7),
       *[C(x, y, 4.5, "W", "N", 0) for x, y in ((50, 58), (30, 60), (70, 60), (40, 76), (60, 76), (20, 78), (80, 78))])),
    # ---- Rettung und Flucht (gruen) ----
    ("sammelstelle", "Sammelstelle", *GN,
     q(*wa(18, 18, 39, 39, 7, 17), *wa(82, 18, 61, 39, 7, 17), *wa(18, 82, 39, 61, 7, 17), *wa(82, 82, 61, 61, 7, 17),
       C(50, 50, 7.5, "W", "N", 0))),
    ("notausgang", "Notausgang", *GN, q(R(52, 16, 30, 68, "N", "W", 6.5), *wa(14, 50, 66, 50, 9, 22))),
    ("erste_hilfe", "Erste Hilfe", *GN, q(R(39, 17, 22, 66, "W", "N", 0), R(17, 39, 66, 22, "W", "N", 0))),
    ("rettungswache", "Rettungswache", *GN,
     q(PG(GIEBEL, "W"), R(44, 42, 12, 34, "F", "N", 0), R(33, 53, 34, 12, "F", "N", 0))),
    ("notarzt", "Notarzt / Notarztstandort", *GN, qt("NA", 38)),
    ("hubschrauberlandeplatz", "Hubschrauberlandeplatz", *GN, q(C(50, 50, 32, "N", "W", 6.5), T("H", 50, 50, 30, "W"))),
    ("defibrillator", "Defibrillator (AED)", *GN, q(P(HEART, "W", "N", 0), *lightning(50, 47, 0.78, "F"))),
    ("bereitstellungsraum", "Bereitstellungsraum", *GN, qt("BR", 38)),
    # ---- Katastrophenschutz und Einsatzorganisation (blau) ----
    ("einsatzleitung", "Einsatzleitung", *BL, qt("EL", 38)),
    ("sirene", "Sirene", *BL,
     q(PG([(16, 41), (32, 41), (54, 22), (54, 78), (32, 59), (16, 59)], "W"), arc(52, 50, 17, 45, 135, 6, "W"),
       arc(52, 50, 31, 48, 132, 6, "W"))),
    ("notunterkunft", "Notunterkunft", *BL,
     q(PL([(15, 46), (50, 17), (85, 46)], 7.5, "W"), wl(24, 54, 24, 84, 6.5), wl(24, 74, 76, 74, 6.5),
       wl(76, 66, 76, 84, 6.5), C(36, 62, 6.5, "W", "N", 0), R(46, 58, 30, 11, "W", "N", 0, 4))),
    ("evakuierungsroute", "Evakuierungsroute", *BL, q(*fit(person("W"), 50, 40, 0.6), *wa(16, 80, 85, 80, 8, 20))),
    ("sandsacklager", "Sandsacklager", *BL,
     q(*[R(x, y, 22, 16, "W", "N", 0, 7) for x, y in ((15, 65), (39, 65), (63, 65), (27, 45), (51, 45), (39, 25))])),
    ("notstromversorgung", "Notstromversorgung", *BL, q(C(50, 50, 32, "N", "W", 6.5), *lightning(50, 50, 0.8, "W"))),
    ("trinkwassernotbrunnen", "Trinkwassernotbrunnen", *BL,
     q(P("M18,36 H58 Q70,36 70,48 V54", "N", "W", 10, cap="butt"), wl(40, 18, 40, 34, 6.5), wl(28, 18, 52, 18, 6.5),
       *wdrop(70, 73, 0.34))),
    ("leuchtturm", "Katastrophenschutz-Leuchtturm / Anlaufstelle", *BL,
     q(PG([(41, 40), (59, 40), (66, 85), (34, 85)], "W"), R(40, 24, 20, 13, "W", "N", 0, 2), PG([(37, 24), (63, 24), (50, 12)], "W"),
       L(38.5, 60, 61.5, 60, 7, "F", "butt"), wl(32, 27, 16, 20, 5.5), wl(32, 35, 16, 42, 5.5), wl(68, 27, 84, 20, 5.5),
       wl(68, 35, 84, 42, 5.5))),
    # ---- Gefahrenstellen (gelbes Dreieck) ----
    ("gefahrstoff", "Gefahrstoff / Gefahrenstelle allgemein", *GE, gf(T("!", 50, 59, 36))),
    ("explosionsgefahr", "Explosionsgefahr", *GE, gf(PG(star(50, 63, 21, 9, 9), "S"))),
    ("hochspannung", "Hochspannung / elektrische Gefahr", *GE, gf(*lightning(50, 61, 0.72))),
    ("gasflaschen", "Gasflaschen / Druckgasbehälter", *GE,
     gf(R(40, 50, 20, 30, "S", "N", 0, 7), R(46, 40, 8, 12, "S", "N", 0), L(42, 39, 58, 39, 4.5, cap="butt"))),
    ("radioaktiv", "Radioaktive Stoffe (Gefahrenstelle)", *GE,
     gf(pie(50, 63, 20, -30, 30), pie(50, 63, 20, 90, 150), pie(50, 63, 20, 210, 270), C(50, 63, 7, "F", "N", 0),
        C(50, 63, 4, "S", "N", 0))),
    ("hochwassergefahr", "Hochwassergefahr", *GE,
     gf(PG([(50, 34), (40, 50), (60, 50)], "S"), wave(28, 62, 44, 4, 2, 4.5), wave(20, 75, 60, 4, 3, 4.5))),
    ("einsturzgefahr", "Einsturzgefahr", *GE,
     gf(PG([(26, 80), (26, 58), (36, 52), (40, 64), (48, 60), (50, 80)], "S"),
        PG(rot([(-6, -6), (6, -6), (6, 6), (-6, 6)], 25, 53, 44), "S"),
        PG(rot([(-6, -6), (6, -6), (6, 6), (-6, 6)], 55, 65, 67), "S"))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
R0, R1, G0, G1, B0, B1, Y0, Y1 = RT[0], RT[1], GN[0], GN[1], BL[0], BL[1], GE[0], GE[1]


def weg(farbe, dunkel, breite, strich=None):  # Weg mit Richtungspfeilen
    return [linie(farbe, breite, strich), marken(mk("filled_arrowhead", 2.4, dunkel), 10)]


LINIEN = [
    ("Feuerwehrzufahrt", weg(R0, R1, 0.9)),
    ("Rettungsweg, Fluchtweg", weg(G0, G1, 0.7)),
    ("Rettungsweg geplant", weg(G0, G1, 0.7, [3, 1.5])),
    ("Evakuierungsroute", weg(B0, B1, 0.9)),
    ("Löschwasserleitung", [linie(R0, 0.5, [5, 1, 0.5, 1])]),
    ("Schlauchleitung", [linie(R0, 0.4), marken(mk("circle", 1.4, "#FFFFFF", rand=R0, rw=0.3), 8)]),
    ("Absperrung", [linie(R0, 1.3), linie("#FFFFFF", 0.7, [2, 2])]),
    ("Brandwand, Brandabschnittsgrenze", [linie(R1, 1.4)]),
    ("Deichverteidigungslinie", [linie(B0, 0.8), marken(mk("triangle", 1.8, B1, dy=-1.1), 4)]),
    ("Einsatzabschnittsgrenze", [linie(B1, 0.6, [6, 1.5, 1, 1.5])]),
]

FLAECHEN = [
    ("Aufstellfläche Feuerwehr", [voll(R0 + "26"), schraffur(R0, 0.3, 45, 2.5), linie(R1, 0.5)]),
    ("Bewegungsfläche Feuerwehr", [voll(R0 + "33"), linie(R1, 0.5)]),
    ("Brandabschnitt", [band(R0 + "66", 1.5), linie(R1, 0.6)]),
    ("Absperrbereich", [voll(R0 + "1F"), schraffur(R0, 0.3, 45, 3), schraffur(R0, 0.3, 135, 3), linie(R1, 0.5)]),
    ("Gefahrenbereich", [voll(Y0 + "66"), schraffur(Y1, 0.3, 45, 3), linie(Y1, 0.5)]),
    ("Sammelstelle (Fläche)", [voll(G0 + "40"), linie(G1, 0.5)]),
    ("Flucht- und Rettungsweg (Fläche)", [voll(G0 + "1F"), schraffur(G0, 0.25, 135, 2.5), linie(G1, 0.4)]),
    ("Evakuierungszone", [voll(B0 + "26"), schraffur(B0, 0.25, 45, 2.5), linie(B1, 0.5)]),
    ("Überflutungsbereich", [voll(B0 + "40"), schraffur(B1, 0.25, 0, 2), linie(B1, 0.4)]),
    ("Einsatzabschnitt", [band(B0 + "66", 1.5), linie(B1, 0.5, [6, 1.5, 1, 1.5])]),
]
