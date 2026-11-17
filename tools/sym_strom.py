"""Sammlung Strom: Stationen, Masten, Kabelgarnituren und Schaltzeichen fuer Netz- und Leitungsplaene.
Orientierung: gebraeuchliche Legenden von Netzbetreibern, Schaltzeichen nach DIN EN 60617, Leitungsplaene
nach DIN 2425. Ein bundeseinheitliches Regelwerk fuer Punktsymbole gibt es nicht; eigene Entwuerfe.
Stil: rot auf weiss, Strich 5. Die Form zeigt die Gruppe:
  Quadrat = Station oder Anlage, Mastzeichen in Draufsicht, ohne Rahmen = Garnitur oder Schaltzeichen
  auf der Leitung (Leitung waagerecht durch die Symbolmitte).
Linien und Flaechen: rot; die Strichstaerke zeigt die Spannungsebene, durchgezogen = Freileitung,
gestrichelt = Kabel, Flaechen hellrot oder rot schraffiert.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "strom"
NAME = "Strom"
DESC = ("Symbole für Stromnetze und Leitungspläne: Kraftwerk, Umspannwerk, Stationen, Kabelverteiler, "
        "Freileitungsmasten, Muffen und Kabelgarnituren, Schaltzeichen, Ladeinfrastruktur")
TAGS = "strom, netz, energieversorgung, leitungsplan, mittelspannung, niederspannung, freileitung, kabel"

RED = ("#FFFFFF", "#C8102E")


def st(*sh):  # Station, Anlage
    return fr_square() + list(sh)


def stt(txt, h=24, mw=66):
    return st(T(txt, 50, 50, h, maxw=mw))


def ltg(x0=6, x1=94):
    return L(x0, 50, x1, 50, 5, cap="butt")


def gm(*sh):  # Gittermast in Draufsicht
    return [R(18, 18, 64, 64, "F", "S", 5), L(18, 18, 82, 82, 4.5, cap="butt"), L(18, 82, 82, 18, 4.5, cap="butt")] + list(sh)


PLUG = [R(34, 36, 32, 24, "S", "N", 0, 5), L(42, 24, 42, 37, 6), L(58, 24, 58, 37, 6),
        P("M50,60 V68 Q50,80 62,80 H74", "N", "S", 5)]

S = [
    # ---- Stationen und Anlagen (Quadrat) ----
    ("kraftwerk", "Kraftwerk", *RED, st(*lightning(50, 50, 1.1))),
    ("umspannwerk", "Umspannwerk", *RED, st(C(39, 50, 18, "N", "S", 4.5), C(61, 50, 18, "N", "S", 4.5))),
    ("schaltstation", "Schaltstation / Schaltanlage", *RED,
     st(L(18, 60, 38, 60), L(38, 60, 64, 40), L(64, 60, 82, 60), C(38, 60, 4, "S", "N", 0), C(64, 60, 4, "S", "N", 0))),
    ("ortsnetzstation", "Ortsnetzstation / Trafostation", *RED,
     [R(7, 7, 86, 86, "F", "N", 0, 8), PG([(9, 91), (91, 91), (91, 9)], "S"), R(7, 7, 86, 86, "N", "S", 5, 8)]),
    ("maststation", "Maststation", *RED,
     [C(50, 50, 44, "F", "N", 0), chord(50, 50, 44, 45, 225), C(50, 50, 44, "N", "S", 5)]),
    ("uebergabestation", "Übergabestation / Kundenstation", *RED, stt("Ü", 40)),
    ("netzersatzanlage", "Netzersatzanlage / Notstromaggregat", *RED, stt("NEA")),
    ("batteriespeicher", "Batteriespeicher", *RED,
     st(R(18, 34, 56, 32, "N", "S", 4.5, 4), R(74, 43, 8, 14, "S", "N", 0, 2), *cross(33, 50, 7, 4.5), L(52, 50, 64, 50, 4.5))),
    ("kabelverteiler", "Kabelverteilerschrank", *RED, [R(12, 28, 76, 44, "F", "S", 5), L(12, 72, 88, 28, 5, cap="butt")]),
    ("hausanschluss", "Hausanschluss", *RED, st(*fit(house(), 50, 50, 0.78), C(50, 60, 6, "S", "N", 0))),
    ("zaehler", "Zähler / Messeinrichtung", *RED, stt("kWh", 18, 62)),
    ("ladesaeule", "Ladesäule Elektromobilität", *RED, st(*PLUG)),
    ("ladesaeule_schnell", "Schnellladesäule (DC)", *RED, st(*fit(PLUG, 38, 50, 0.78), *lightning(72, 50, 0.62))),
    ("leuchte", "Leuchte / Lichtpunkt", *RED, [C(50, 50, 30, "F", "S", 5)] + xcross(50, 50, 21.2, 4.5)),
    ("stoerung", "Störung / Fehlerort", *RED, [PG([(50, 8), (94, 88), (6, 88)], "F", "S", 6)] + lightning(50, 60, 0.62)),
    # ---- Freileitungsmasten (Draufsicht) ----
    ("mast_holz", "Freileitungsmast: Holzmast", *RED, [C(50, 50, 16, "S", "N", 0)]),
    ("mast_beton", "Freileitungsmast: Betonmast", *RED, [C(50, 50, 26, "F", "S", 5), C(50, 50, 9, "S", "N", 0)]),
    ("mast_stahlrohr", "Freileitungsmast: Stahlrohrmast", *RED, [C(50, 50, 28, "F", "S", 5), C(50, 50, 13, "N", "S", 4.5)]),
    ("mast_a", "Freileitungsmast: A-Mast / Doppelmast", *RED,
     [L(30, 50, 70, 50, 5), C(28, 50, 13, "S", "N", 0), C(72, 50, 13, "S", "N", 0)]),
    ("mast_portal", "Freileitungsmast: Portalmast", *RED,
     [L(26, 50, 74, 50, 5), R(10, 34, 32, 32, "F", "S", 5), R(58, 34, 32, 32, "F", "S", 5)]),
    ("mast_gitter", "Freileitungsmast: Gittermast (Tragmast)", *RED, gm()),
    ("mast_abspann", "Freileitungsmast: Abspannmast", *RED, gm(C(50, 50, 11, "S", "N", 0))),
    ("mast_winkel", "Freileitungsmast: Winkelmast", *RED, gm(PG([(50, 50), (82, 18), (82, 82)], "S"))),
    ("mast_end", "Freileitungsmast: Endmast", *RED, gm(R(18, 18, 16, 64, "S", "N", 0))),
    ("dachstaender", "Dachständer", *RED,
     [PL([(14, 76), (50, 44), (86, 76)], 5), L(50, 44, 50, 22, 5, cap="butt"), C(50, 16, 8, "S", "N", 0)]),
    # ---- Kabel und Garnituren (auf der Leitung) ----
    ("muffe", "Verbindungsmuffe", *RED, [ltg(), E(50, 50, 22, 11, "S", "N", 0)]),
    ("abzweigmuffe", "Abzweigmuffe", *RED, [ltg(), L(50, 50, 50, 92, 5, cap="butt"), E(50, 50, 22, 11, "S", "N", 0)]),
    ("uebergangsmuffe", "Übergangsmuffe", *RED,
     [ltg(6, 26), ltg(74, 94), E(50, 50, 24, 13, "F", "S", 4.5), P("M50,37 A24,13 0 0 0 50,63 Z", "S", "N", 0)]),
    ("endverschluss", "Kabelendverschluss", *RED, [ltg(6, 46), PG([(46, 28), (86, 50), (46, 72)], "F", "S", 5)]),
    ("leitungsende", "Leitungsende / Blindende", *RED, [ltg(6, 62), L(62, 30, 62, 70, 8, cap="butt")]),
    ("netzknoten", "Netzknoten / Abzweig", *RED,
     [ltg(), L(50, 50, 50, 92, 5, cap="butt"), C(50, 50, 10, "S", "N", 0)]),
    ("kabelkreuzung", "Kabelkreuzung (ohne Verbindung)", *RED,
     [ltg(), P("M50,6 V36 A14,14 0 0 1 50,64 V94", "N", "S", 5, cap="butt")]),
    ("kabelreserve", "Kabelreserve / Kabelschlaufe", *RED, [L(6, 60, 94, 60, 5, cap="butt"), C(50, 42, 18, "N", "S", 5)]),
    ("schutzrohr", "Schutzrohr / Leerrohr", *RED, [ltg(), L(24, 36, 76, 36, 4.5), L(24, 64, 76, 64, 4.5)]),
    ("kabelschacht", "Kabelschacht", *RED, [ltg(6, 20), ltg(80, 94), R(20, 26, 60, 48, "F", "S", 5), T("K", 50, 50, 26)]),
    ("kabelmerkstein", "Kabelmerkstein", *RED, [R(28, 28, 44, 44, "F", "S", 5), C(50, 50, 7, "S", "N", 0)]),
    ("einspeisung", "Einspeisung / dezentrale Erzeugung", *RED, [L(12, 80, 88, 80, 6)] + arrow(50, 14, 50, 72, 6, 15)),
    # ---- Schaltzeichen ----
    ("transformator", "Transformator (Schaltzeichen)", *RED,
     [L(50, 6, 50, 20, 5, cap="butt"), L(50, 80, 50, 94, 5, cap="butt"), C(50, 38, 18, "N", "S", 5), C(50, 62, 18, "N", "S", 5)]),
    ("generator", "Generator (Schaltzeichen)", *RED, fr_circle(r=34) + [T("G", 50, 50, 32), ltg(6, 16), ltg(84, 94)]),
    ("motor", "Motor (Schaltzeichen)", *RED, fr_circle(r=34) + [T("M", 50, 50, 32), ltg(6, 16), ltg(84, 94)]),
    ("spannungsmessung", "Spannungsmessung (Schaltzeichen)", *RED, fr_circle(r=34) + [T("V", 50, 50, 32), ltg(6, 16), ltg(84, 94)]),
    ("strommessung", "Strommessung (Schaltzeichen)", *RED, fr_circle(r=34) + [T("A", 50, 50, 32), ltg(6, 16), ltg(84, 94)]),
    ("sicherung", "Sicherung", *RED, [R(24, 36, 52, 28, "F", "S", 5), ltg()]),
    ("trennstelle_offen", "Trennstelle offen / Trennschalter", *RED,
     [L(6, 56, 32, 56, 5), L(68, 56, 94, 56, 5), L(36, 52, 62, 30, 5), C(34, 56, 5.5, "F", "S", 4), C(66, 56, 5.5, "F", "S", 4)]),
    ("trennstelle_geschlossen", "Trennstelle geschlossen", *RED,
     [ltg(), C(34, 50, 6.5, "S", "N", 0), C(66, 50, 6.5, "S", "N", 0)]),
    ("leistungsschalter", "Leistungsschalter", *RED,
     [L(6, 56, 34, 56, 5), L(66, 56, 94, 56, 5), L(34, 56, 62, 32, 5)] + xcross(66, 56, 8, 5)),
    ("lasttrennschalter", "Lasttrennschalter", *RED,
     [L(6, 56, 34, 56, 5), L(66, 56, 94, 56, 5), L(34, 56, 60, 34, 5), L(66, 42, 66, 70, 5), C(66, 50, 6, "F", "S", 4)]),
    ("erdung", "Erdungsanlage", *RED,
     [L(50, 14, 50, 46, 5), L(20, 46, 80, 46, 5.5), L(31, 62, 69, 62, 5.5), L(42, 78, 58, 78, 5.5)]),
    ("ueberspannungsableiter", "Überspannungsableiter", *RED,
     [L(50, 6, 50, 22, 5, cap="butt"), R(35, 22, 30, 40, "F", "S", 5), *arrow(50, 28, 50, 56, 4, 10),
      L(50, 62, 50, 76, 5, cap="butt"), L(30, 76, 70, 76, 5.5), L(40, 88, 60, 88, 5)]),
    ("kondensator", "Kondensator / Kompensation", *RED,
     [ltg(6, 42), ltg(58, 94), L(42, 26, 42, 74, 6, cap="butt"), L(58, 26, 58, 74, 6, cap="butt")]),
    ("drosselspule", "Drosselspule", *RED,
     [ltg(6, 20), ltg(80, 94), P("M20,50 A10,10 0 0 1 40,50 A10,10 0 0 1 60,50 A10,10 0 0 1 80,50", "N", "S", 5)]),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
R0 = "#C8102E"

LINIEN = [
    ("Höchstspannungsfreileitung 380 kV", [linie(R0, 1.2)]),
    ("Höchstspannungsfreileitung 220 kV", [linie(R0, 0.9)]),
    ("Hochspannungsfreileitung 110 kV", [linie(R0, 0.65)]),
    ("Mittelspannungsfreileitung", [linie(R0, 0.4)]),
    ("Niederspannungsfreileitung", [linie(R0, 0.25)]),
    ("Freileitung mit Maststandorten", [linie(R0, 0.5), marken(mk("circle", 1.5, "#FFFFFF", R0, 0.3), 10)]),
    ("Hochspannungskabel 110 kV", [linie(R0, 0.65, [4, 1.5])]),
    ("Mittelspannungskabel", [linie(R0, 0.4, [4, 1.5])]),
    ("Niederspannungskabel", [linie(R0, 0.25, [4, 1.5])]),
    ("Hausanschlusskabel", [linie(R0, 0.25, [1.5, 1])]),
    ("Straßenbeleuchtungskabel", [linie(R0, 0.25, [4, 1, 0.4, 1])]),
    ("Kabel im Schutzrohr", [linie(R0, 1.5), linie("#FFFFFF", 1.0), linie(R0, 0.3, [4, 1.5])]),
    ("Leitung geplant", [linie(R0, 0.5, [0.5, 1])]),
    ("Leitung außer Betrieb", [linie(R0, 0.4), marken(mk("cross2", 1.6, R0, rw=0.3), 6)]),
]

FLAECHEN = [
    ("Schutzstreifen", [voll(R0 + "1F"), schraffur(R0, 0.2, 45, 2.5), linie(R0, 0.3, [3, 1.5])]),
    ("Trassenkorridor", [voll(R0 + "1A"), linie(R0, 0.4, [6, 2])]),
    ("Umspannwerk, Betriebsgelände", [voll("#F6D5DA"), linie(R0, 0.5)]),
    ("Stationsgebäude", [voll(R0)]),
    ("Netzgebiet", [band(R0 + "59", 1.5), linie(R0, 0.4)]),
    ("Kabelgraben, Baufeld", [schraffur(R0, 0.2, 135, 2), linie(R0, 0.3)]),
    ("Störungsgebiet", [voll(R0 + "40"), linie(R0, 0.6)]),
]
