"""Sammlung Radverkehr und Mobilitaet: Abstell- und Serviceanlagen, Sharing, Erhebung, Maengel, Knoten und
Wegweisung, Massnahmen; Fuehrungsformen des Radverkehrs als Linien.
Orientierung: Begriffe der Fuehrungsformen wie in den Empfehlungen fuer Radverkehrsanlagen (ERA) und der StVO
(Radweg, Radfahrstreifen, Schutzstreifen, Fahrradstrasse, Fahrradzone), Bestands- und Maengelkarten kommunaler
Radverkehrskonzepte. Die ERA lag nicht vor; Zeichen und Farben sind nirgends festgelegt, eigene Entwuerfe.
Stil: helle Magentafuellung, dunkler Magentastrich 5. Die Rahmenform zeigt die Gruppe:
  Quadrat = Anlage oder Angebot (anl_), Kreis = Erhebung (erh_), Raute = Mangel (mg_),
  Sechseck = Knoten und Wegweisung (kn_), gestricheltes Quadrat = Massnahme (mas_).
Allgemeine Zeichen stehen woanders: Fahrradabstellanlage, Ladestation, Carsharing in Verkehr, E-Bike-Ladestation
und Fahrradverleih in Tourismus, touristische Radrouten in Tourismus und Topografie.
Linien und Flaechen: magenta = Radverkehrsanlage (durchgezogen = baulich, lang gestrichelt = markiert,
kurz gestrichelt = Schutzstreifen oder geplant), grau = Fuehrung im Mischverkehr oder auf fremder Flaeche.
Ausnahme von der Farbe: Zustand der Oberflaeche gruen, gelb, rot.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "radverkehr"
NAME = "Radverkehr und Mobilität"
DESC = ("Symbole für Radverkehr und Mobilität: Abstell- und Serviceanlagen, Sharing und Mobilstationen, Zählung "
        "und Erhebung, Mängel und Gefahrenstellen, Knoten und Wegweisung, Maßnahmen, Führungsformen des "
        "Radverkehrs, Radnetz, Zustand und Erreichbarkeit")
TAGS = ("radverkehr, fahrrad, mobilitaet, radweg, radverkehrskonzept, fahrradstrasse, abstellanlage, sharing, "
        "mobilstation, nahmobilitaet")

RM = ("#FADCEB", "#B4136A")


def an(*sh):  # Anlage, Angebot
    return fr_square() + list(sh)


def er(*sh):  # Erhebung
    return fr_circle() + list(sh)


def mg(*sh):  # Mangel
    return fr_diamond() + list(sh)


def kn(*sh):  # Knoten, Wegweisung
    return fr_hex() + list(sh)


def mn(*sh):  # Massnahme
    return [R(7, 7, 86, 86, "F", "S", 5, 8, "12 8")] + list(sh)


def rad(cx=50, cy=50, k=0.7):
    return fit(bike(), cx, cy, k)


def dot(x, y, r=3.5):
    return C(x, y, r, "S", "N", 0)


def tausch(y=24):  # Ausleihe und Rueckgabe
    return arrow(30, y, 72, y, 4, 10) + arrow(70, y + 11, 28, y + 11, 4, 10)


BUEGEL = [P("M22,78 V42 A13,13 0 0 1 48,42 V78", "N", "S", 5.5), P("M52,78 V42 A13,13 0 0 1 78,42 V78", "N", "S", 5.5)]
LASTENRAD = [C(20, 66, 12, "N", "S", 4.5), C(82, 66, 12, "N", "S", 4.5), R(28, 40, 30, 24, "N", "S", 4.5, 3),
             PL([(20, 66), (60, 66), (68, 36), (82, 66)], 4.5), L(62, 30, 76, 30, 5)]
ROLLER = [C(24, 74, 9, "N", "S", 4.5), C(76, 74, 9, "N", "S", 4.5), PL([(34, 74), (62, 74), (72, 26)], 5),
          L(62, 26, 82, 26, 5)]
PUMPE = [L(38, 18, 62, 18, 5), L(50, 18, 50, 42, 4.5), R(43, 42, 14, 36, "S", "N", 0, 2), L(32, 82, 68, 82, 5),
         P("M57,72 Q76,72 74,50", "N", "S", 4)]
KNOTEN = ([L(50, 50, x, y, 4.5) for x, y in ((50, 20), (24, 68), (76, 68))] + [C(50, 50, 11, "S", "N", 0)]
          + [C(x, y, 9, "F", "S", 4) for x, y in ((50, 20), (24, 68), (76, 68))])
BANK = [L(22, 42, 78, 42, 5), L(22, 56, 78, 56, 6), L(30, 56, 30, 74, 5), L(70, 56, 70, 74, 5)]
KAMERA = [R(22, 36, 56, 38, "N", "S", 5, 5), C(50, 55, 11, "N", "S", 4.5), R(40, 27, 20, 9, "S", "N", 0, 2)]
BLASE = [P("M20,24 H80 V64 H52 L36,80 V64 H20 Z", "N", "S", 5)]
AMPEL = [R(38, 20, 24, 60, "N", "S", 4.5, 8), C(50, 34, 5.5, "S", "N", 0), C(50, 50, 5.5, "S", "N", 0),
         C(50, 66, 5.5, "S", "N", 0)]
SCHILD = [L(40, 22, 40, 82, 5), PG([(40, 26), (68, 26), (80, 37), (68, 48), (40, 48)], "F", "S", 4.5)]
LEUCHTE = [L(50, 84, 50, 40, 5), C(50, 28, 11, "F", "S", 4.5)]
STUFEN = [PL([(22, 76), (22, 62), (36, 62), (36, 50), (50, 50), (50, 38), (64, 38), (64, 26), (78, 26)], 5)]

S = [
    # ---- Anlagen und Angebote (Quadrat) ----
    ("anl_buegel", "Fahrradbügel / Anlehnbügel", *RM, an(*BUEGEL, L(16, 80, 84, 80, 4))),
    ("anl_ueberdacht", "Fahrradabstellanlage, überdacht", *RM, an(PL([(16, 36), (50, 18), (84, 36)], 5.5), *rad(50, 60, 0.62))),
    ("anl_box", "Fahrradbox / Fahrradgarage", *RM, an(R(17, 28, 66, 50, "N", "S", 5, 4), *rad(50, 54, 0.5))),
    ("anl_parkhaus", "Fahrradparkhaus / Radstation", *RM, an(T("P", 30, 34, 30), *rad(56, 62, 0.6))),
    ("anl_doppelstock", "Doppelstockparker", *RM, an(*rad(50, 32, 0.44), L(18, 50, 82, 50, 4.5), *rad(50, 70, 0.44))),
    ("anl_lastenrad", "Abstellplatz für Lastenräder", *RM, an(*fit(LASTENRAD, 50, 50, 0.76))),
    ("anl_bike_ride", "Bike and Ride", *RM, an(T("B+R", 50, 30, 20, maxw=64), *rad(50, 66, 0.52))),
    ("anl_schliessfach", "Schließfach / Gepäckfach", *RM,
     an(R(22, 22, 56, 56, "N", "S", 5, 3), L(50, 22, 50, 78, 4.5), L(22, 50, 78, 50, 4.5),
        *[dot(x, y, 3) for x in (42, 70) for y in (36, 64)])),
    ("anl_service", "Radservicestation (Luftpumpe, Werkzeug)", *RM, an(*fit(PUMPE, 50, 50, 0.9))),
    ("anl_schlauchautomat", "Schlauchautomat", *RM,
     an(R(27, 16, 46, 68, "N", "S", 5, 4), C(50, 40, 13, "N", "S", 5), L(38, 70, 62, 70, 5))),
    ("anl_bikesharing", "Bikesharing-Station", *RM, an(*tausch(), *rad(50, 64, 0.58))),
    ("anl_lastenradverleih", "Lastenrad-Verleih", *RM, an(*tausch(), *fit(LASTENRAD, 50, 62, 0.62))),
    ("anl_escooter", "E-Scooter-Abstellfläche", *RM, an(*fit(ROLLER, 50, 50, 0.8))),
    ("anl_mobilstation", "Mobilstation", *RM, an(*fit(KNOTEN, 50, 52, 0.92))),
    ("anl_rufbus", "Haltepunkt Rufbus / On-Demand-Verkehr", *RM,
     an(T("H", 40, 50, 40), arc(58, 50, 16, 40, 140, 4.5), arc(58, 50, 27, 40, 140, 4.5))),
    ("anl_mitfahrbank", "Mitfahrbank", *RM, an(*fit(BANK, 50, 58, 0.8), *arrow(34, 34, 66, 20, 4.5, 11))),
    # ---- Erhebung (Kreis) ----
    ("erh_dauerzaehlstelle", "Dauerzählstelle Radverkehr", *RM,
     er(*rad(50, 36, 0.46), R(31, 66, 9, 12, "S", "N", 0), R(45.5, 56, 9, 22, "S", "N", 0), R(60, 61, 9, 17, "S", "N", 0))),
    ("erh_kurzzeitzaehlung", "Kurzzeitzählung / Knotenstromzählung", *RM,
     er(*[L(x, 32, x, 68, 5) for x in (32, 44, 56, 68)], L(24, 64, 76, 36, 5))),
    ("erh_unfall", "Unfall mit Radverkehrsbeteiligung", *RM, er(*rad(44, 62, 0.5), PG(star(66, 30, 16, 7, 8), "S"))),
    ("erh_meldung", "Bürgermeldung / Mängelmelder", *RM, er(*fit(BLASE + [T("!", 50, 44, 26)], 50, 52, 0.8))),
    ("erh_befahrung", "Befahrung / Fotostandort", *RM, er(*fit(KAMERA, 50, 49, 0.86))),
    ("erh_geschwindigkeit", "Geschwindigkeitsmessung", *RM,
     er(arc(50, 60, 28, -90, 90, 5), L(50, 60, 66, 40, 5), dot(50, 60, 6))),
    ("erh_befragung", "Befragung / Haushaltsbefragung", *RM, er(*fit(BLASE + [T("?", 50, 44, 26)], 50, 52, 0.8))),
    # ---- Maengel (Raute) ----
    ("mg_gefahrenstelle", "Gefahrenstelle", *RM, mg(T("!", 50, 50, 38))),
    ("mg_unfallhaeufung", "Unfallhäufungsstelle", *RM, mg(PG(star(50, 50, 24, 11, 8), "S"))),
    ("mg_oberflaeche", "Oberflächenschaden / Schlagloch", *RM, mg(P("M24,46 H38 Q50,74 62,46 H76", "N", "S", 5.5))),
    ("mg_engstelle", "Engstelle / zu geringe Breite", *RM,
     mg(PL([(26, 37), (40, 50), (26, 63)], 5), PL([(74, 37), (60, 50), (74, 63)], 5), L(50, 30, 50, 70, 4.5))),
    ("mg_netzluecke", "Netzlücke", *RM, mg(L(22, 50, 38, 50, 7), L(62, 50, 78, 50, 7), *xcross(50, 50, 6, 4.5))),
    ("mg_querung", "Fehlende oder unsichere Querung", *RM,
     mg(L(40, 26, 40, 74, 4.5), L(60, 26, 60, 74, 4.5), L(22, 50, 78, 50, 5, dash="5 8"))),
    ("mg_hindernis", "Hindernis (Poller, Umlaufsperre)", *RM, mg(R(43, 30, 14, 38, "S", "N", 0, 6), L(30, 70, 70, 70, 5))),
    ("mg_bordstein", "Bordstein nicht abgesenkt / Kante", *RM, mg(PL([(24, 60), (50, 60), (50, 42), (76, 42)], 6))),
    ("mg_sicht", "Eingeschränkte Sicht", *RM, mg(*fit(eye(), 50, 50, 0.56), L(32, 68, 68, 32, 5))),
    ("mg_beleuchtung", "Fehlende Beleuchtung", *RM, mg(*fit(LEUCHTE, 50, 50, 0.62), L(32, 68, 68, 32, 5))),
    ("mg_konflikt_fuss", "Konflikt mit Fußverkehr", *RM, mg(*fit(person(), 36, 50, 0.4), *rad(62, 54, 0.36))),
    ("mg_parken", "Konflikt mit ruhendem Verkehr (Falschparker, Dooring)", *RM, mg(T("P", 50, 50, 34), L(30, 70, 70, 30, 5))),
    ("mg_wegweisung", "Fehlende oder falsche Wegweisung", *RM, mg(*fit(SCHILD, 50, 50, 0.6), L(32, 68, 68, 32, 5))),
    ("mg_signal", "Lange Wartezeit / fehlende Radsignalisierung", *RM, mg(*fit(AMPEL, 50, 50, 0.72))),
    ("mg_bewuchs", "Bewuchs / Verschmutzung", *RM,
     mg(*[L(x, 66, x + d, 66 - h, 4.5) for x in (38, 62) for d, h in ((0, 26), (-10, 18), (10, 18))], L(26, 66, 74, 66, 4.5))),
    # ---- Knoten und Wegweisung (Sechseck) ----
    ("kn_knotenpunkt", "Knotenpunkt im Knotenpunktnetz", *RM, kn(C(50, 50, 25, "N", "S", 5), T("K", 50, 50, 26))),
    ("kn_wegweiser", "Pfeilwegweiser / Wegweiserstandort", *RM,
     kn(L(50, 20, 50, 82, 5), PG([(50, 24), (70, 24), (79, 33), (70, 42), (50, 42)], "S"),
        PG([(50, 48), (30, 48), (21, 57), (30, 66), (50, 66)], "S"))),
    ("kn_zwischenwegweiser", "Zwischenwegweiser", *RM,
     kn(L(50, 58, 50, 84, 5), R(30, 20, 40, 38, "F", "S", 4.5, 3), *arrow(38, 39, 62, 39, 4.5, 11))),
    ("kn_infotafel", "Infotafel / Knotenpunkttafel", *RM,
     kn(R(26, 20, 48, 42, "F", "S", 4.5, 3), T("i", 50, 41, 26), L(36, 62, 36, 82, 5), L(64, 62, 64, 82, 5))),
    ("kn_querungshilfe", "Querungshilfe / Mittelinsel", *RM,
     kn(L(22, 30, 78, 30, 4.5), L(22, 70, 78, 70, 4.5), E(50, 50, 17, 8, "S", "N", 0), L(50, 22, 50, 78, 4, dash="4 7"))),
    ("kn_radampel", "Lichtsignalanlage mit Radsignal", *RM, kn(*fit(AMPEL, 32, 50, 0.8), *rad(64, 50, 0.4))),
    ("kn_aras", "Aufgeweiteter Radaufstellstreifen (ARAS)", *RM,
     kn(L(22, 24, 78, 24, 6, cap="butt"), R(24, 30, 52, 28, "N", "S", 4), *rad(50, 44, 0.34),
        L(50, 62, 50, 82, 4, dash="6 6"))),
    ("kn_kreisverkehr", "Kreisverkehr mit Radführung", *RM,
     kn(arc(50, 50, 22, 15, 105, 5), arc(50, 50, 22, 135, 225, 5), arc(50, 50, 22, 255, 345, 5), dot(50, 50, 7))),
    ("kn_unterfuehrung", "Unterführung / Tunnel", *RM,
     kn(L(22, 26, 78, 26, 7, cap="butt"), P("M30,78 V54 A20,20 0 0 1 70,54 V78", "N", "S", 5))),
    ("kn_bruecke", "Rad- und Fußgängerbrücke", *RM, kn(L(18, 42, 82, 42, 6.5), P("M26,74 Q50,36 74,74", "N", "S", 5))),
    ("kn_treppe", "Treppe mit Schieberinne / Schiebestrecke", *RM, kn(*fit(STUFEN, 50, 50, 0.84), L(28, 80, 76, 34, 4))),
    # ---- Massnahmen (gestricheltes Quadrat) ----
    ("mas_neubau", "Maßnahme Neubau Radverkehrsanlage", *RM, mn(*rad(46, 60, 0.6), *cross(74, 26, 9, 5))),
    ("mas_ausbau", "Maßnahme Ausbau / Verbreiterung", *RM,
     mn(L(50, 26, 50, 74, 4.5), *arrow(44, 50, 18, 50, 5, 13), *arrow(56, 50, 82, 50, 5, 13))),
    ("mas_decke", "Maßnahme Deckenerneuerung", *RM,
     mn(L(20, 38, 80, 38, 9, cap="butt"), L(20, 55, 80, 55, 4.5), L(20, 68, 80, 68, 4.5, dash="8 7"))),
    ("mas_markierung", "Maßnahme Markierung / Roteinfärbung", *RM,
     mn(R(38, 20, 24, 60, "S", "N", 0), L(26, 20, 26, 80, 4.5, dash="11 8"), L(74, 20, 74, 80, 4.5, dash="11 8"))),
    ("mas_beschilderung", "Maßnahme Beschilderung / Wegweisung", *RM, mn(*fit(SCHILD, 46, 50, 0.9))),
    ("mas_knoten", "Maßnahme Knotenpunktumbau", *RM,
     mn(L(20, 50, 80, 50, 9, cap="butt"), L(50, 20, 50, 80, 9, cap="butt"), C(50, 50, 13, "F", "S", 4.5))),
    ("mas_abstellanlage", "Maßnahme Abstellanlage errichten", *RM, mn(*fit(BUEGEL, 44, 58, 0.66), *cross(74, 26, 9, 5))),
    ("mas_beleuchtung", "Maßnahme Beleuchtung", *RM,
     mn(*fit(LEUCHTE, 50, 54, 0.8), *[L(*pt(50, 32, 15, a), *pt(50, 32, 23, a), 4.5) for a in (-90, -45, 0, 45, 90)])),
    ("mas_sofort", "Sofortmaßnahme", *RM, mn(*lightning(50, 50, 1.0))),
    ("mas_pruefauftrag", "Prüfauftrag / Planung erforderlich", *RM, mn(T("?", 50, 50, 42))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
M0, ML = RM[1], RM[0]
GRAU, ROT, WS = "#7A7A7A", "#D0021B", "#FFFFFF"
ZUSTAND = [("gut", "#3E9B4F"), ("mittel", "#F2C200"), ("schlecht", ROT)]
STAERKE = [("gering", 0.4), ("mittel", 0.9), ("hoch", 1.5), ("sehr hoch", 2.3)]
ERREICHBAR = [("bis 5 Minuten", "#B4136A"), ("5 bis 10 Minuten", "#D3589A"), ("10 bis 15 Minuten", "#E79BC4"),
              ("15 bis 20 Minuten", "#F6D3E5")]

LINIEN = [
    ("Radschnellverbindung", [linie(M0, 1.9), linie(WS, 0.45)]),
    ("Radvorrangroute", [linie(M0, 1.5), linie(WS, 0.35, [3, 2])]),
    ("Radweg, baulich getrennt", [linie(M0, 1.0)]),
    ("Zweirichtungsradweg", [linie(M0, 0.45, versatz=0.45), linie(M0, 0.45, versatz=-0.45)]),
    ("Gemeinsamer Geh- und Radweg", [linie(M0, 1.1), marken(mk("circle", 0.6, WS), 2.5)]),
    ("Getrennter Geh- und Radweg", [linie(M0, 0.7, versatz=0.3), linie(GRAU, 0.4, versatz=-0.45)]),
    ("Radfahrstreifen", [linie(M0, 0.8, [6, 1])]),
    ("Geschützter Radfahrstreifen", [linie(M0, 0.8, [6, 1]), linie(M0, 0.25, versatz=0.85)]),
    ("Schutzstreifen", [linie(M0, 0.6, [2, 1.5])]),
    ("Fahrradstraße", [linie(M0 + "59", 2.4), linie(M0, 0.5)]),
    ("Gehweg, Radverkehr frei", [linie(GRAU, 0.9), marken(mk("circle", 0.7, M0), 3)]),
    ("Bussonderfahrstreifen, Radverkehr frei", [linie(GRAU, 0.9, [6, 1]), marken(mk("square", 0.7, M0), 7, start=3)]),
    ("Einbahnstraße, für Radverkehr geöffnet", [linie(GRAU, 0.6), marken(mk("arrowhead", 1.6, M0, rw=0.35, winkel=180), 8)]),
    ("Mischverkehr bis 30 km/h", [linie(GRAU, 0.6)]),
    ("Mischverkehr über 30 km/h ohne Radverkehrsanlage", [linie(GRAU, 0.6, [3, 1.5])]),
    ("Selbständiger Weg / Wirtschaftsweg", [linie(M0, 0.5, [4, 1, 0.6, 1])]),
    ("Schiebestrecke", [linie(M0, 0.5, [0.6, 1.2])]),
    ("Radnetz, Hauptroute", [linie(M0 + "66", 2.6)]),
    ("Radnetz, Nebenroute", [linie(M0 + "66", 1.3)]),
    ("Netzlücke", [linie(M0, 0.7, [1, 1.5]), marken(mk("cross2", 1.6, M0, rw=0.35), 8)]),
    ("Geplante Radverkehrsverbindung", [linie(M0, 0.9, [3, 1.5])]),
    ("Wunschlinie / Luftlinienverbindung", [linie(M0, 0.3, [5, 2]), marken(mk("filled_arrowhead", 1.8, M0), 14)]),
] + [(f"Zustand der Oberfläche {t}", [linie(c, 1.0)]) for t, c in ZUSTAND] + [
    (f"Radverkehrsstärke {t}", [linie(M0, b)]) for t, b in STAERKE]

FLAECHEN = [
    ("Fahrradzone", [voll(M0 + "26"), linie(M0, 0.5)]),
    ("Radverkehrsfurt / Roteinfärbung", [voll("#D0463A")]),
    ("Aufstellfläche Radverkehr", [voll(M0 + "59"), linie(M0, 0.3)]),
    ("Fahrradabstellfläche", [muster(mk("line", 1.4, M0, rw=0.3), 1.6, 2.6), linie(M0, 0.4)]),
    ("Sharing-Abstellfläche", [schraffur(M0, 0.25, 45, 1.6), linie(M0, 0.4)]),
    ("Sharing-Geschäftsgebiet", [band(M0 + "59", 1.5), linie(M0, 0.4)]),
    ("Abstellverbotszone", [schraffur(ROT, 0.2, 45, 2.5), schraffur(ROT, 0.2, 135, 2.5), linie(ROT, 0.4)]),
    ("Einzugsbereich Mobilstation", [voll(M0 + "1A"), linie(M0, 0.5, [1, 1])]),
] + [(f"Erreichbarkeit mit dem Rad {t}", [voll(c)]) for t, c in ERREICHBAR] + [
    ("Unfallhäufungsbereich", [band(ROT + "59", 1.5), linie(ROT, 0.5)]),
    ("Maßnahmenbereich Radverkehr", [schraffur(M0, 0.2, 45, 3), linie(M0, 0.5, [3, 1.5])]),
    ("Tempo-30-Zone", [voll(GRAU + "26"), linie(GRAU, 0.4, [4, 1.5])]),
    ("Verkehrsberuhigter Bereich", [muster(mk("circle", 0.5, GRAU), 2.2, versatz=1.1), linie(GRAU, 0.4)]),
    ("Fußgängerzone, Radverkehr frei", [voll(GRAU + "26"), muster(mk("circle", 0.6, M0), 3, versatz=1.5), linie(GRAU, 0.4)]),
    ("Untersuchungsraum Radverkehrskonzept", [linie(M0, 0.7, [6, 1.5, 1, 1.5])]),
]
