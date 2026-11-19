"""Sammlung Stadtklima: Messung, Belastung, klimatische Ausgleichsraeume, Klimaanpassung, Stroemungspfeile.
Orientierung: VDI 3787 Blatt 1 (Klima- und Lufthygienekarten fuer Staedte und Regionen: Klimaanalysekarte mit
Klimatopen, Kaltluft- und Luftaustauschprozessen, Planungshinweiskarte). Die Richtlinie selbst lag nicht vor;
die Liste der Klimatope folgt der Klimaanalyse Nordrhein-Westfalen (LANUV, Methodikpapier Klimatopkarte, Stand
13.12.2023), die sich auf die Richtlinie beruft, ergaenzt um Industrie und Gleisanlagen. Zeichen und Farben sind
nirgends verbindlich festgelegt; eigene Entwuerfe in ueblicher Farbgebung.
Stil: helle Petrolfuellung, dunkler Petrolstrich 5. Die Rahmenform zeigt die Gruppe:
  Kreis = Messung (mess_), Quadrat = Belastung im Siedlungsraum (last_), Sechseck = Ausgleichsraum (ausgl_),
  Raute = Massnahme der Klimaanpassung (anp_), ohne Rahmen = Stroemungspfeil (pfeil_, zeigt nach rechts, drehbar).
Linien und Flaechen: Farbe = Bedeutung. Blau = Kaltluft, gruen = Frischluft und Gruen, orangerot = Waerme und
Belastung, grau = Lufthygiene, petrol = Grenzen und Massnahmen (gestrichelt). Klimatope von blau und gruen
(Gewaesser, Freiland, Wald) ueber gelb und orange bis rot (Innenstadt), Gewerbe und Industrie grau.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "stadtklima"
NAME = "Stadtklima"
DESC = ("Symbole für Stadtklima und Klimaanpassung: Messstellen, Wärme- und Luftbelastung, Kaltluft- und "
        "Frischluftgebiete, Luftleitbahnen, Klimatope, Maßnahmen der Klimaanpassung und Hitzevorsorge")
TAGS = "stadtklima, klima, klimaanpassung, hitze, kaltluft, frischluft, klimatop, klimaanalyse, luft, waermeinsel"

SK = ("#D5EEF0", "#0E6E78")


def ms(*sh):  # Messung
    return fr_circle() + list(sh)


def la(*sh):  # Belastung im Siedlungsraum
    return fr_square() + list(sh)


def au(*sh):  # Ausgleichsraum
    return fr_hex() + list(sh)


def ap(*sh):  # Massnahme der Klimaanpassung
    return fr_diamond() + list(sh)


def tuft(x, y, k=1.0, sw=4):
    return [L(x, y, x, y - 18 * k, sw), L(x, y, x - 10 * k, y - 13 * k, sw), L(x, y, x + 10 * k, y - 13 * k, sw)]


THERMO = [R(42, 10, 16, 56, "F", "S", 5, 8), C(50, 74, 15, "S", "N", 0), L(50, 34, 50, 72, 6)]
SCHNEE = ([L(*pt(50, 50, 34, a), *pt(50, 50, 34, a + 180), 5.5) for a in (0, 60, 120)]
          + [L(*pt(50, 50, 20, a), *pt(50, 50, 32, a + d), 4.5) for a in range(0, 360, 60) for d in (-24, 24)])
MOND = [P("M56,16 A34,34 0 1 0 84,60 A27,27 0 0 1 56,16 Z", "S", "N", 0)]
WIND = [P("M14,40 H60 A10,10 0 1 0 50,30", "N", "S", 5.5), P("M14,58 H74 A10,10 0 1 1 64,68", "N", "S", 5.5)]
STADT = [PG([(16, 84), (16, 56), (32, 56), (32, 40), (52, 40), (52, 62), (66, 62), (66, 48), (84, 48), (84, 84)], "S")]
SPROSS = [L(50, 84, 50, 44, 5.5), P("M50,66 Q30,64 26,46 Q46,48 50,66 Z", "S", "N", 0),
          P("M50,54 Q70,52 74,34 Q54,36 50,54 Z", "S", "N", 0)]
RISS = [PL([(38, 16), (46, 38), (38, 54), (58, 68), (52, 84)], 6), PL([(46, 38), (66, 34), (82, 44)], 6)]

S = [
    # ---- Messung (Kreis) ----
    ("mess_klimastation", "Klimamessstation", *SK,
     ms(*fit(THERMO, 36, 50, 0.74), L(66, 78, 66, 26, 5), PG([(66, 24), (84, 32), (66, 40)], "S"))),
    ("mess_temperatur", "Temperaturmesspunkt", *SK, ms(*fit(THERMO, 50, 50, 0.8))),
    ("mess_wind", "Windmessung", *SK,
     ms(L(50, 46, 50, 84, 5), *[L(50, 44, *pt(50, 44, 20, a), 4.5) for a in (0, 120, 240)],
        *[C(*pt(50, 44, 24, a), 7, "S", "N", 0) for a in (0, 120, 240)])),
    ("mess_strahlung", "Strahlungsmessung", *SK, ms(*sun(50, 50, 12, "S", "S", 5, 8, 7, 9))),
    ("mess_luft", "Luftmessstation", *SK,
     ms(cloud([(31, 50, 12), (48, 40, 17), (67, 49, 13)], "F", "S", 5), *[C(x, 73, 3.5, "S", "N", 0) for x in (36, 50, 64)])),
    ("mess_no2", "Passivsammler Stickstoffdioxid", *SK, ms(T("NO2", 50, 50, 20, maxw=60))),
    ("mess_feinstaub", "Feinstaubmessung", *SK, ms(T("PM", 50, 50, 28, maxw=58))),
    ("mess_messfahrt", "Messfahrt / Profilmesspunkt", *SK,
     ms(PL([(20, 66), (38, 38), (60, 62), (80, 34)], 4.5), *[C(x, y, 6, "S", "N", 0) for x, y in ((20, 66), (38, 38), (60, 62), (80, 34))])),
    # ---- Belastung im Siedlungsraum (Quadrat) ----
    ("last_waermeinsel", "Städtische Wärmeinsel / Hitze-Hotspot", *SK, la(*STADT, *sun(68, 27, 6, "S", "S", 4, 8, 4, 6))),
    ("last_hitze", "Hitzebelastung am Tag", *SK, la(*fit(THERMO, 36, 50, 0.76), *sun(68, 36, 8, "S", "S", 4, 8, 5, 7))),
    ("last_tropennacht", "Nächtliche Überwärmung / Tropennacht", *SK, la(*fit(THERMO, 36, 50, 0.76), *fit(MOND, 66, 36, 0.46))),
    ("last_versiegelung", "Hoher Versiegelungsgrad", *SK,
     la(R(22, 22, 56, 56, "S", "N", 0, 3), L(22, 50, 78, 50, 3.5, "F", "butt"), L(50, 22, 50, 78, 3.5, "F", "butt"))),
    ("last_luft", "Lufthygienische Belastung", *SK,
     la(cloud([(31, 46, 12), (48, 36, 17), (67, 45, 13)], "S", "S", 4), *[C(x, 72, 4.5, "S", "N", 0) for x in (34, 50, 66)])),
    ("last_durchlueftung", "Durchlüftungsmangel / Strömungshindernis", *SK,
     la(*arrow(16, 50, 52, 50, 5.5, 13), R(60, 22, 18, 56, "S", "N", 0, 2))),
    ("last_duese", "Düseneffekt / Windkomfort eingeschränkt", *SK,
     la(R(30, 16, 40, 22, "S", "N", 0, 2), R(30, 62, 40, 22, "S", "N", 0, 2), *arrow(15, 50, 86, 50, 5.5, 14))),
    ("last_sensibel", "Hitzesensible Einrichtung (Pflegeheim, Krankenhaus, Kita)", *SK,
     la(*fit(house(), 50, 48, 0.8), *cross(50, 61, 8, 5.5))),
    # ---- Ausgleichsraum (Sechseck) ----
    ("ausgl_kaltluftentstehung", "Kaltluftentstehungsgebiet", *SK, au(*fit(SCHNEE, 50, 42, 0.62), wave(28, 76, 44, 4, 2, 4.5))),
    ("ausgl_frischluft", "Frischluftentstehungsgebiet", *SK, au(*fit(tree_side(), 38, 50, 0.62), *fit(WIND, 68, 50, 0.4))),
    ("ausgl_gruen", "Klimaaktive Grünfläche / Parkklima", *SK, au(*fit(tree_side(), 50, 47, 0.68), L(28, 78, 72, 78, 4.5))),
    ("ausgl_wasser", "Klimaaktive Wasserfläche", *SK, au(*[wave(22, y, 56, 5, 2, 5) for y in (36, 51, 66)])),
    ("ausgl_kaltluftsee", "Kaltluftsammelgebiet / Kaltluftsee", *SK,
     au(P("M20,44 Q50,92 80,44", "N", "S", 5), L(33, 58, 67, 58, 4), L(42, 68, 58, 68, 4), *fit(SCHNEE, 50, 30, 0.3))),
    ("ausgl_leitbahn", "Luftleitbahn / Ventilationsbahn (nach rechts, drehbar)", *SK,
     au(*arrow(18, 50, 84, 50, 6, 16), wave(24, 32, 40, 4, 2, 4), wave(24, 70, 40, 4, 2, 4))),
    # ---- Massnahmen der Klimaanpassung (Raute) ----
    ("anp_dachbegruenung", "Dachbegrünung", *SK,
     ap(R(31, 54, 38, 18, "N", "S", 4.5), *tuft(40, 52, 0.7), *tuft(50, 52, 0.9), *tuft(60, 52, 0.7))),
    ("anp_fassadenbegruenung", "Fassadenbegrünung", *SK,
     ap(R(46, 28, 20, 46, "N", "S", 4.5), L(38, 74, 38, 32, 3.5), *[C(x, y, 5.5, "S", "N", 0) for x, y in ((36, 36), (41, 49), (35, 62))])),
    ("anp_baumpflanzung", "Baumpflanzung / Stadtgrün", *SK, ap(*fit(tree_side(), 44, 52, 0.54), *cross(68, 40, 7, 4.5))),
    ("anp_entsiegelung", "Entsiegelung", *SK, ap(*fit(RISS, 50, 50, 0.6))),
    ("anp_verschattung", "Verschattung / Sonnenschutz", *SK,
     ap(P("M24,54 A26,26 0 0 1 76,54 Z", "S", "N", 0), L(50, 54, 50, 76, 4.5))),
    ("anp_trinkbrunnen", "Trinkwasserbrunnen", *SK, ap(*fit(drop("S", "N", 0), 50, 50, 0.56))),
    ("anp_kuehler_ort", "Kühler Ort", *SK, ap(*fit(SCHNEE, 50, 50, 0.7))),
    ("anp_wasserspiel", "Wasserspiel / Sprühnebel", *SK,
     ap(L(30, 70, 70, 70, 5), L(50, 68, 50, 42, 4.5), P("M50,42 Q40,26 31,48", "N", "S", 4.5),
        P("M50,42 Q60,26 69,48", "N", "S", 4.5))),
    ("anp_retention", "Regenwasserrückhalt / Schwammstadt", *SK,
     ap(P("M28,50 Q50,82 72,50", "N", "S", 5), *fit(drop("S", "N", 0), 50, 36, 0.3))),
    ("anp_helle_oberflaeche", "Helle Oberfläche / Rückstrahlung erhöhen", *SK,
     ap(L(34, 68, 66, 68, 7, cap="butt"), *arrow(32, 36, 46, 60, 4.5, 10), *arrow(54, 60, 68, 36, 4.5, 10))),
    ("anp_hitzeaktionsplan", "Maßnahme des Hitzeaktionsplans", *SK, ap(T("HAP", 50, 50, 18, maxw=46))),
    # ---- Stroemungspfeile (ohne Rahmen, nach rechts) ----
    ("pfeil_kaltluft", "Kaltluftabfluss (nach rechts, drehbar)", *SK,
     [PG([(6, 36), (58, 36), (58, 18), (95, 50), (58, 82), (58, 64), (6, 64)], "F", "S", 5)]),
    ("pfeil_frischluft", "Frischluftzufuhr (nach rechts, drehbar)", *SK,
     [PG([(6, 40), (58, 40), (58, 22), (95, 50), (58, 78), (58, 60), (6, 60)], "S", "S", 4)]),
    ("pfeil_flurwind", "Flurwind (nach rechts, drehbar)", *SK,
     [L(8, 50, 62, 50, 7, dash="12 9"), PG([(95, 50), (64, 33), (64, 67)], "S", "S", 3)]),
    ("pfeil_hangabwind", "Hangabwind (nach rechts, drehbar)", *SK,
     arrow(8, 50, 94, 50, 7, 22) + [L(x, 50, x - 11, 28, 5.5) for x in (22, 38, 54)]),
    ("pfeil_wechselwind", "Berg- und Talwind / Wechselströmung (drehbar)", *SK,
     [L(26, 50, 74, 50, 7, cap="butt"), PG([(96, 50), (70, 34), (70, 66)], "S", "S", 3), PG([(4, 50), (30, 34), (30, 66)], "S", "S", 3)]),
    ("pfeil_hauptwind", "Hauptwindrichtung (nach rechts, drehbar)", *SK,
     arrow(22, 50, 94, 50, 7, 22) + [PL([(8, 32), (24, 50), (8, 68)], 6), PL([(24, 32), (40, 50), (24, 68)], 6)]),
    ("pfeil_barriere", "Strömungsbarriere (Anströmung von links, drehbar)", *SK,
     arrow(6, 50, 50, 50, 6.5, 16) + [L(62, 10, 62, 90, 12, cap="butt")]),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
T0, TL = SK[1], SK[0]
KALT, FRISCH, WARM, GRAU = "#2B7BBF", "#3E9B4F", "#D9482B", "#6B6B6B"

LINIEN = [
    ("Kaltluftleitbahn", [linie(KALT + "59", 2.6), marken(mk("filled_arrowhead", 2.4, KALT), 9)]),
    ("Frischluftleitbahn", [linie(FRISCH + "59", 2.6), marken(mk("filled_arrowhead", 2.4, FRISCH), 9)]),
    ("Kaltluftabfluss am Hang", [linie(KALT, 0.4), marken(mk("filled_arrowhead", 1.8, KALT), 6)]),
    ("Flurwind", [linie(KALT, 0.4, [2, 1]), marken(mk("arrowhead", 1.8, KALT, rw=0.35), 8)]),
    ("Hauptwindrichtung", [linie(T0, 0.5), marken(mk("filled_arrowhead", 2.2, T0), 14)]),
    ("Strömungsbarriere / Riegelbebauung", [linie(WARM, 1.0), marken(mk("line", 2.0, WARM, rw=0.35), 2.5)]),
    ("Lufthygienisch belasteter Straßenabschnitt", [linie(GRAU + "59", 2.4), linie(GRAU, 0.4)]),
    ("Isotherme, Hauptlinie", [linie(WARM, 0.6)]),
    ("Isotherme, Zwischenlinie", [linie(WARM, 0.25)]),
    ("Grenze Luftaustauschbereich", [linie(T0, 0.5, [6, 1.5, 1, 1.5])]),
    ("Bebauungsgrenze aus klimatischen Gründen", [linie(T0, 0.6, [4, 1, 0.6, 1, 0.6, 1])]),
    ("Messfahrtroute", [linie(T0, 0.4, [1.5, 1]), marken(mk("circle", 0.9, T0), 6)]),
]

KLIMATOPE = [("Gewässer", "#9CCBEE"), ("Freiland", "#E4EFB0"), ("Wald", "#5E9E5A"), ("Grünanlage / Park", "#A8D58C"),
             ("Gartenstadt / Vorstadt", "#FBE9A6"), ("Stadtrand", "#F8C97A"), ("Stadt", "#EE9550"),
             ("Innenstadt", "#D9543A"), ("Gewerbe", "#C4C4C4"), ("Industrie", "#8C8C8C"), ("Gleisanlagen", "#B79AC8")]
BELASTUNG = [("gering", "#FCE9A0"), ("mäßig", "#F8B85C"), ("hoch", "#E8622E"), ("sehr hoch", "#A8162A")]
AUSGLEICH = [("mittlere", "#C5E3C0"), ("hohe", "#6DB67F"), ("sehr hohe", "#1F7A4D")]

FLAECHEN = ([(f"Klimatop {t}", [voll(c)]) for t, c in KLIMATOPE]
            + [(f"Thermische Belastung {t}", [voll(c)]) for t, c in BELASTUNG]
            + [(f"Ausgleichsraum, {t} Bedeutung", [voll(c)]) for t, c in AUSGLEICH] + [
    ("Kaltluftentstehungsgebiet", [schraffur(KALT, 0.2, 0, 2), linie(KALT, 0.4)]),
    ("Frischluftentstehungsgebiet", [schraffur(FRISCH, 0.2, 0, 2), linie(FRISCH, 0.4)]),
    ("Kaltluftsammelgebiet", [voll(KALT + "33"), schraffur(KALT, 0.2, 90, 2.5), linie(KALT, 0.4)]),
    ("Kaltlufteinwirkbereich", [muster(mk("circle", 0.5, KALT), 2.2, versatz=1.1), linie(KALT, 0.4, [3, 1.5])]),
    ("Luftleitbahn, Freihaltebereich", [band(KALT + "59", 1.5), linie(KALT, 0.4, [4, 1.5])]),
    ("Überwärmungsgebiet / städtische Wärmeinsel", [schraffur(WARM, 0.25, 45, 2.5), linie(WARM, 0.5)]),
    ("Gebiet mit Durchlüftungsmangel", [schraffur(WARM, 0.2, 45, 3), schraffur(WARM, 0.2, 135, 3), linie(WARM, 0.4, [3, 1.5])]),
    ("Lufthygienischer Belastungsbereich", [muster(mk("circle", 0.6, GRAU), 2.2, versatz=1.1), linie(GRAU, 0.4)]),
    ("Dachbegrünung, Bestand", [voll(FRISCH + "80"), linie(FRISCH, 0.3)]),
    ("Dachbegrünung, Potenzial", [schraffur(FRISCH, 0.2, 45, 2), linie(FRISCH, 0.4, [3, 1.5])]),
    ("Entsiegelungs- und Begrünungspotenzial", [muster(mk("cross", 1.2, T0, rw=0.25), 3, versatz=1.5), linie(T0, 0.5, [3, 1.5])]),
    ("Maßnahmenfläche Klimaanpassung", [schraffur(T0, 0.2, 45, 3), linie(T0, 0.5, [3, 1.5])]),
    ("Fokusgebiet Hitzevorsorge", [band(WARM + "59", 1.5), linie(WARM, 0.5, [3, 1.5])]),
])
