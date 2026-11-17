"""Sammlung Kartengestaltung: Nummern- und Buchstabenmarker, Hinweiszeichen und Pfeile fuer Karten und Layouts.
Orientierung: uebliche Verweiszeichen in Plaenen und Legenden (Positionsnummern, Detailverweise, Schnittlinien).
Eigene Entwuerfe.
Stil: schwarz auf weiss, Strich 5. Die Form zeigt die Gruppe:
  Kreis = Nummer (hell: nr_, gefuellt: nrv_), Quadrat = Buchstabe (bu_), Raute = Hinweiszeichen (hw_),
  ohne Rahmen = Pfeil oder Marke (drehbar, Spitze bzw. Bezugspunkt nach oben).
Linien und Flaechen: schwarz fuer Rahmen und Schnitte, rot (#C8102E) fuer Hervorhebungen und Ausschnitte.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "layout"
NAME = "Kartengestaltung"
DESC = ("Zeichen für die Kartengestaltung: Nummern 1 bis 20 im Kreis (hell und gefüllt), Buchstaben A bis L im "
        "Quadrat, Hinweiszeichen, Pfeile und Standortmarken, schwarz-weiß mit änderbaren Farben")
TAGS = "layout, kartengestaltung, nummer, buchstabe, marker, pfeil, hinweis, legende, drucklayout"

BK = ("#FFFFFF", "#000000")
ROT = "#C8102E"


def nr(txt):  # Nummer im hellen Kreis
    return [C(50, 50, 42, "F", "S", 5), T(txt, 50, 50, 40, "S", maxw=54)]


def nrv(txt):  # Nummer im gefuellten Kreis
    return [C(50, 50, 44, "S", "N", 0), T(txt, 50, 50, 40, "F", maxw=54)]


def bu(txt):  # Buchstabe im Quadrat
    return [R(9, 9, 82, 82, "F", "S", 5, 6), T(txt, 50, 50, 44, "S", maxw=56)]


def hw(*shapes):  # Hinweiszeichen in der Raute
    return [PG([(50, 5), (95, 50), (50, 95), (5, 50)], "F", "S", 5)] + list(shapes)


S = (
    # ---- Nummern im hellen Kreis ----
    [(f"nr_{i:02d}", f"Nummer {i} im Kreis", *BK, nr(str(i))) for i in range(1, 21)]
    # ---- Nummern im gefuellten Kreis ----
    + [(f"nrv_{i:02d}", f"Nummer {i} im gefüllten Kreis", *BK, nrv(str(i))) for i in range(1, 11)]
    # ---- Buchstaben im Quadrat ----
    + [(f"bu_{c.lower()}", f"Buchstabe {c} im Quadrat", *BK, bu(c)) for c in "ABCDEFGHIJKL"]
    + [
        # ---- Hinweiszeichen ----
        ("hw_achtung", "Hinweis: Achtung", *BK, hw(L(50, 28, 50, 56, 8), C(50, 72, 5, "S", "N", 0))),
        ("hw_frage", "Hinweis: Klärungsbedarf", *BK, hw(T("?", 50, 50, 44))),
        ("hw_info", "Hinweis: Information", *BK, hw(C(50, 30, 5.5, "S", "N", 0), L(50, 46, 50, 72, 8))),
        ("hw_erledigt", "Hinweis: erledigt / in Ordnung", *BK, hw(PL([(30, 52), (44, 66), (70, 36)], 8))),
        ("hw_mangel", "Hinweis: Mangel / nicht in Ordnung", *BK, hw(*xcross(50, 50, 16, 8))),
        ("hw_stern", "Hinweis: besonders wichtig", *BK, hw(PG(star(50, 50, 26, 11, 5), "S"))),
        # ---- Pfeile und Marken ----
        ("pfeil", "Pfeil (drehbar)", *BK, [L(50, 94, 50, 40, 8, cap="butt"), PG([(50, 5), (76, 44), (24, 44)], "S")]),
        ("pfeil_schlank", "Pfeil, schlank (drehbar)", *BK,
         [L(50, 94, 50, 34, 4, cap="butt"), PG([(50, 5), (64, 38), (36, 38)], "S")]),
        ("pfeil_doppelt", "Doppelpfeil (drehbar)", *BK,
         [L(50, 70, 50, 30, 6, cap="butt"), PG([(50, 5), (70, 34), (30, 34)], "S"),
          PG([(50, 95), (70, 66), (30, 66)], "S")]),
        ("pfeil_umriss", "Pfeil im Umriss (drehbar)", *BK,
         [PG([(50, 6), (82, 46), (62, 46), (62, 94), (38, 94), (38, 46), (18, 46)], "F", "S", 5)]),
        ("pfeil_spitze", "Pfeilspitze (drehbar)", *BK, [PG([(50, 14), (80, 82), (50, 66), (20, 82)], "S")]),
        ("standort", "Standortmarke", *BK,
         [P("M50,94 C30,62 20,50 20,36 C20,18 34,6 50,6 C66,6 80,18 80,36 C80,50 70,62 50,94 Z", "F", "S", 5),
          C(50, 36, 11, "S", "N", 0)]),
        ("standort_voll", "Standortmarke, gefüllt", *BK,
         [P("M50,94 C30,62 20,50 20,36 C20,18 34,6 50,6 C66,6 80,18 80,36 C80,50 70,62 50,94 Z", "S", "S", 5),
          C(50, 36, 11, "F", "N", 0)]),
        ("fadenkreuz", "Fadenkreuz / Bezugspunkt", *BK,
         [C(50, 50, 28, "N", "S", 5), L(50, 6, 50, 38, 5, cap="butt"), L(50, 62, 50, 94, 5, cap="butt"),
          L(6, 50, 38, 50, 5, cap="butt"), L(62, 50, 94, 50, 5, cap="butt")]),
        ("detail", "Detailverweis (Lupe)", *BK, [C(42, 42, 28, "F", "S", 6), L(63, 63, 90, 90, 10)]),
        ("schnittmarke", "Schnittmarke (drehbar, Blickrichtung nach oben)", *BK,
         [L(8, 78, 92, 78, 8, cap="butt"), PG([(50, 14), (72, 60), (28, 60)], "S")]),
        ("blickrichtung", "Blickrichtung / Fotostandpunkt (drehbar)", *BK,
         [PG([(50, 62), (16, 12), (84, 12)], "F", "S", 4.5), C(50, 72, 14, "S", "N", 0)]),
        ("punkt", "Punktmarke", *BK, [C(50, 50, 20, "S", "N", 0)]),
        ("punkt_ring", "Punktmarke mit Ring", *BK, [C(50, 50, 34, "F", "S", 5), C(50, 50, 13, "S", "N", 0)]),
    ]
)

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
K0 = "#000000"

LINIEN = [
    ("Schnittlinie", [linie(K0, 0.7, [8, 1.5, 0.7, 1.5])]),
    ("Blattschnitt", [linie(K0, 0.35, [5, 1.5])]),
    ("Hinweislinie", [linie(K0, 0.25)]),
    ("Verbindungslinie", [linie(K0, 0.3, [1, 1])]),
    ("Pfeillinie", [linie(K0, 0.4), marken(mk("filled_arrowhead", 2.2, K0), 10)]),
    ("Maßlinie", [linie(K0, 0.25), marken(mk("line", 1.8, K0, rw=0.25, winkel=45), 10)]),
    ("Hervorhebung", [linie(ROT, 0.9)]),
    ("Hervorhebung, gestrichelt", [linie(ROT, 0.9, [4, 2])]),
    ("Markierband", [linie("#FFE60099", 3.0)]),
]

FLAECHEN = [
    ("Kartenrahmen", [linie(K0, 0.7)]),
    ("Kartenrahmen, doppelt", [linie(K0, 3.2, innen=True), linie("#FFFFFF", 2.4, innen=True), linie(K0, 0.5)]),
    ("Detailausschnitt", [linie(ROT, 0.8)]),
    ("Detailausschnitt, gestrichelt", [linie(ROT, 0.8, [4, 2])]),
    ("Übersichtsausschnitt", [voll(ROT + "26"), linie(ROT, 0.6)]),
    ("Hervorhebung, Fläche", [voll("#FFE60066"), linie("#B8A500", 0.3)]),
    ("Legendenkasten", [voll("#FFFFFF"), linie(K0, 0.35)]),
    ("Abdeckung, halbtransparent", [voll("#FFFFFFB3"), linie(K0, 0.2, [1, 1])]),
    ("Plangebiet", [band(K0 + "33", 2.0), linie(K0, 0.6, [6, 2])]),
    ("Schraffur, neutral", [schraffur(K0, 0.2, 45, 2.5), linie(K0, 0.3)]),
]
