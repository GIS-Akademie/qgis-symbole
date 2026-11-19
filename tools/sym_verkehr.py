"""Sammlung Verkehr: Parken, OEPNV, Bahn, Luft- und Schiffsverkehr, Rad- und Fussverkehr, Bauwerke,
Verkehrstechnik, Stoerungen.
Orientierung: Hinweiszeichen der StVO (weisses Sinnbild auf blauem Quadrat) und Legenden amtlicher
Stadt- und Verkehrskarten. Keine Marken- oder Unternehmenslogos. Eigene Entwuerfe.
Stil: immer abgerundetes Quadrat mit weissem Sinnbild. Die Farbe zeigt die Gruppe:
  blau = Anlage oder Angebot, orange = Baustelle und Stoerung, rot = Sperrung, Gefahr, Beschraenkung.
Linien und Flaechen: blau wie die Punktsymbole (Strassen nach Klasse abgestuft), orange = Baustelle und
Umleitung, rot = Sperrung und Stau.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "verkehr"
NAME = "Verkehr"
DESC = ("Symbole für Verkehr und Mobilität: Parken, ÖPNV, Bahn, Flug- und Schiffsverkehr, Rad- und Fußverkehr, "
        "Bauwerke, Verkehrstechnik, Baustellen, Sperrungen und Beschränkungen")
TAGS = "verkehr, mobilitaet, oepnv, parken, bahn, strasse, radverkehr, baustelle"

VB = ("#1F5FA8", "#0D3C73")
OR = ("#EF7D00", "#A85400")
RT = ("#D0021B", "#8B0000")


def vq(*sh):
    return fr_square() + list(sh)


def vt(txt, h=44, mw=66):
    return vq(T(txt, 50, 50, h, "W", maxw=mw))


def wl(x1, y1, x2, y2, sw=5, cap="round"):
    return L(x1, y1, x2, y2, sw, "W", cap)


def rb_head(a):
    tip = rot([(24, 0)], a + 16, 50, 50)[0]
    return PG([tip, rot([(15, 0)], a, 50, 50)[0], rot([(33, 0)], a, 50, 50)[0]], "W")


CAR = [P("M12,64 V54 Q12,49 18,48 L28,45 L39,29 H65 L77,45 L84,47 Q89,48 89,54 V64 Z", "W", "N", 0),
       PG([(43, 34), (53, 34), (53, 45), (35, 45)], "F"), PG([(57, 34), (63, 34), (71, 45), (57, 45)], "F"),
       C(31, 66, 9, "W", "F", 4), C(70, 66, 9, "W", "F", 4)]
BUS = [R(24, 18, 52, 56, "W", "N", 0, 9), R(30, 26, 40, 22, "F", "N", 0, 3), C(35, 60, 4.5, "F", "N", 0),
       C(65, 60, 4.5, "F", "N", 0), R(28, 72, 11, 12, "W", "N", 0, 3), R(61, 72, 11, 12, "W", "N", 0, 3)]
TRAIN = [R(27, 13, 46, 58, "W", "N", 0, 13), R(34, 23, 32, 20, "F", "N", 0, 4), C(37, 57, 4.5, "F", "N", 0),
         C(63, 57, 4.5, "F", "N", 0), wl(36, 72, 26, 88), wl(64, 72, 74, 88), wl(31, 82, 69, 82, 4)]
TRAM = [R(27, 30, 46, 44, "W", "N", 0, 8), R(33, 37, 34, 16, "F", "N", 0, 3), C(37, 63, 4, "F", "N", 0),
        C(63, 63, 4, "F", "N", 0), wl(50, 30, 50, 18, 4.5), wl(32, 17, 68, 17, 4.5), wl(36, 75, 30, 88), wl(64, 75, 70, 88)]
WHEELCHAIR = [C(42, 20, 8, "W", "N", 0), PL([(42, 32), (44, 54), (62, 54), (70, 76)], 7, "W"), wl(44, 42, 60, 42, 6),
              arc(44, 62, 21, 78, 356, 6, "W")]
TRUCK = [R(12, 30, 46, 36, "W", "N", 0, 3), P("M61,42 H74 L86,56 V66 H61 Z", "W", "N", 0), PG([(65, 46), (73, 46), (80, 55), (65, 55)], "F"),
         C(28, 70, 8, "W", "F", 4), C(72, 70, 8, "W", "F", 4)]
CAMPER = [P("M12,66 V40 Q12,32 20,32 H66 Q72,32 76,38 L88,54 V66 Z", "W", "N", 0), R(20, 40, 18, 12, "F", "N", 0, 2),
          R(44, 40, 16, 12, "F", "N", 0, 2), PG([(66, 40), (72, 40), (80, 52), (66, 52)], "F"),
          C(30, 68, 8, "W", "F", 4), C(70, 68, 8, "W", "F", 4)]
PLUG = [R(34, 36, 32, 24, "W", "N", 0, 5), wl(42, 24, 42, 37, 6), wl(58, 24, 58, 37, 6),
        P("M50,60 V68 Q50,80 62,80 H74", "N", "W", 5)]
HELI = [wl(20, 28, 80, 28, 5), wl(50, 28, 50, 40, 4.5), E(46, 54, 22, 14, "W", "N", 0), wl(64, 50, 86, 42, 5.5),
        C(86, 42, 5, "W", "N", 0), E(38, 52, 8, 6, "F", "N", 0), wl(28, 78, 64, 78, 4.5), wl(38, 66, 38, 78, 4), wl(54, 66, 54, 78, 4)]
CONE = [PG([(44, 16), (56, 16), (70, 72), (30, 72)], "W"), R(18, 72, 64, 12, "W", "N", 0, 3),
        L(39.5, 36, 60.5, 36, 7, "F", "butt"), L(35, 55, 65, 55, 7, "F", "butt")]
CUP = [R(24, 40, 38, 34, "W", "N", 0, 7), P("M62,46 H69 Q78,46 78,56 Q78,66 69,66 H62", "N", "W", 5), wl(16, 84, 76, 84),
       P("M36,30 q4,-6 0,-12", "N", "W", 4), P("M50,30 q4,-6 0,-12", "N", "W", 4)]

S = [
    # ---- Parken ----
    ("parkplatz", "Parkplatz", *VB, vt("P", 50)),
    ("park_and_ride", "Park and Ride", *VB, vt("P+R", 26, 70)),
    ("mitfahrerparkplatz", "Mitfahrerparkplatz", *VB, vt("P+M", 26, 70)),
    ("parkhaus", "Parkhaus", *VB, vq(PL([(18, 36), (50, 14), (82, 36)], 6, "W"), T("P", 50, 62, 36, "W"))),
    ("tiefgarage", "Tiefgarage", *VB, vq(T("P", 50, 38, 36, "W"), PL([(24, 68), (50, 86), (76, 68)], 6, "W"))),
    ("behindertenparkplatz", "Behindertenparkplatz", *VB, vq(T("P", 30, 34, 24, "W"), *fit(WHEELCHAIR, 60, 56, 0.66))),
    ("lkw_parkplatz", "Lkw-Parkplatz", *VB, vq(T("P", 28, 30, 22, "W"), *fit(TRUCK, 54, 64, 0.72))),
    # ---- OEPNV und Bahn ----
    ("haltestelle", "Haltestelle allgemein", *VB, vq(C(50, 50, 32, "W", "N", 0), T("H", 50, 50, 34, "F"))),
    ("bushaltestelle", "Bushaltestelle", *VB, vq(*BUS)),
    ("busbahnhof", "Busbahnhof / ZOB", *VB, vt("ZOB", 24, 68)),
    ("strassenbahn", "Straßenbahn / Stadtbahn", *VB, vq(*TRAM)),
    ("u_bahn", "U-Bahn", *VB, vt("U", 48)),
    ("s_bahn", "S-Bahn", *VB, vt("S", 48)),
    ("bahnhof", "Bahnhof / Haltepunkt", *VB, vq(*TRAIN)),
    ("seilbahn", "Seilbahn", *VB,
     vq(wl(14, 26, 86, 16, 4.5), wl(50, 21, 50, 38, 4.5), R(31, 38, 38, 38, "W", "N", 0, 9), R(37, 45, 26, 13, "F", "N", 0, 3))),
    ("taxi", "Taxistand", *VB, vt("TAXI", 20, 68)),
    ("carsharing", "Carsharing / Mietwagen", *VB, vq(*CAR)),
    # ---- Luft- und Schiffsverkehr ----
    ("flughafen", "Flughafen / Flugplatz", *VB, vq(*plane(50, 50, 1.05, "W", 45))),
    ("hubschrauberlandeplatz", "Hubschrauberlandeplatz", *VB, vq(*HELI)),
    ("hafen", "Hafen", *VB,
     vq(C(50, 24, 7, "N", "W", 5), wl(50, 31, 50, 80, 6), wl(34, 44, 66, 44, 6), P("M22,56 Q24,80 50,80 Q76,80 78,56", "N", "W", 6))),
    ("faehre", "Fähre", *VB,
     vq(PG([(14, 56), (86, 56), (74, 74), (26, 74)], "W"), R(32, 38, 36, 19, "W", "N", 0, 2), R(45, 24, 10, 15, "W", "N", 0),
        wave(16, 86, 68, 4, 3, 4, "W"))),
    ("sportboothafen", "Sportboothafen / Anleger", *VB,
     vq(PG([(16, 66), (84, 66), (72, 80), (28, 80)], "W"), wl(48, 16, 48, 64, 4.5), PG([(53, 20), (53, 60), (80, 60)], "W"),
        PG([(43, 30), (43, 60), (22, 60)], "W"))),
    ("schleuse", "Schleuse", *VB,
     vq(wl(18, 26, 82, 26), wl(18, 74, 82, 74), PL([(34, 26), (46, 50), (34, 74)], 5.5, "W"), PL([(56, 26), (68, 50), (56, 74)], 5.5, "W"))),
    # ---- Kraftfahrzeugverkehr ----
    ("tankstelle", "Tankstelle", *VB,
     vq(R(22, 20, 36, 60, "W", "N", 0, 5), R(28, 27, 24, 17, "F", "N", 0, 2), wl(16, 82, 64, 82, 6),
        P("M58,44 H66 Q74,44 74,52 V68 Q74,74 80,74 V40 L72,30", "N", "W", 4.5))),
    ("ladestation", "Ladestation Elektromobilität", *VB, vq(*PLUG)),
    ("werkstatt", "Werkstatt / Pannenhilfe", *VB,
     vq(wl(32, 72, 62, 42, 10), C(68, 34, 14, "W", "N", 0), PG([(68, 34), (90, 24), (78, 10)], "F"), C(32, 72, 3.5, "F", "N", 0))),
    ("autobahn", "Autobahn", *VB,
     vq(PG([(28, 86), (41, 86), (47, 38), (43, 38)], "W"), PG([(59, 86), (72, 86), (57, 38), (53, 38)], "W"),
        R(16, 20, 68, 9, "W", "N", 0), R(22, 29, 6, 13, "W", "N", 0), R(72, 29, 6, 13, "W", "N", 0))),
    ("anschlussstelle", "Autobahn-Anschlussstelle", *VB, vt("AS", 36, 60)),
    ("autobahnkreuz", "Autobahnkreuz / Autobahndreieck", *VB, vt("AK", 36, 60)),
    ("rastanlage", "Rastanlage / Raststätte", *VB, vq(*CUP)),
    ("grenzuebergang", "Grenzübergang / Schranke", *VB,
     vq(R(22, 40, 10, 42, "W", "N", 0, 2), wl(27, 46, 84, 28, 8), C(27, 46, 8, "W", "N", 0))),
    # ---- Rad- und Fussverkehr ----
    ("radweg", "Radweg / Radverkehr", *VB, vq(*bike("W"))),
    ("fahrradabstellanlage", "Fahrradabstellanlage / Radstation", *VB,
     vq(PL([(16, 30), (50, 14), (84, 30)], 5.5, "W"), *fit(bike("W"), 50, 60, 0.8))),
    ("e_scooter", "E-Scooter / Mikromobilität", *VB,
     vq(wl(34, 74, 64, 74, 6), wl(64, 74, 56, 26, 6), wl(46, 26, 64, 26, 6), C(28, 76, 8, "N", "W", 5), C(72, 76, 8, "N", "W", 5))),
    ("fussgaengerzone", "Fußgängerzone / Fußweg", *VB, vq(*fit(person("W"), 50, 50, 0.8))),
    ("fussgaengerueberweg", "Fußgängerüberweg / Querungshilfe", *VB,
     vq(*fit(person("W"), 50, 38, 0.56), *[R(x, 70, 8, 16, "W", "N", 0) for x in (18, 32, 46, 60, 74)])),
    ("treppe", "Treppe / Unterführung", *VB,
     vq(PL([(18, 80), (34, 80), (34, 64), (50, 64), (50, 48), (66, 48), (66, 32), (82, 32)], 6, "W"))),
    ("aufzug", "Aufzug", *VB,
     vq(R(26, 16, 48, 68, "N", "W", 5, 4), PG([(50, 24), (62, 42), (38, 42)], "W"), PG([(50, 76), (62, 58), (38, 58)], "W"))),
    ("barrierefrei", "Barrierefreier Zugang", *VB, vq(*fit(WHEELCHAIR, 52, 52, 0.9))),
    # ---- Bauwerke und Verkehrstechnik ----
    ("bruecke", "Brücke", *VB,
     vq(wl(10, 38, 90, 38, 7), P("M20,76 Q50,22 80,76", "N", "W", 6), wl(20, 40, 20, 78, 6), wl(80, 40, 80, 78, 6))),
    ("tunnel", "Tunnel", *VB,
     vq(P("M16,82 V50 A34,34 0 0 1 84,50 V82 Z", "W", "N", 0), P("M32,82 V54 A18,18 0 0 1 68,54 V82 Z", "F", "N", 0))),
    ("kreisverkehr", "Kreisverkehr", *VB, vq(C(50, 50, 24, "N", "W", 7, "36 14.27"), rb_head(86), rb_head(206), rb_head(326))),
    ("bahnuebergang", "Bahnübergang", *VB, vq(wl(20, 26, 80, 74, 11, "butt"), wl(20, 74, 80, 26, 11, "butt"))),
    ("lichtsignalanlage", "Lichtsignalanlage / Ampel", *VB,
     vq(R(33, 10, 34, 80, "W", "N", 0, 9), C(50, 27, 8.5, "F", "N", 0), C(50, 50, 8.5, "F", "N", 0), C(50, 73, 8.5, "F", "N", 0))),
    ("zaehlstelle", "Verkehrszählstelle", *VB,
     vq(R(20, 54, 14, 26, "W", "N", 0), R(43, 36, 14, 44, "W", "N", 0), R(66, 20, 14, 60, "W", "N", 0))),
    ("verkehrskamera", "Verkehrskamera", *VB,
     vq(R(18, 30, 44, 28, "W", "N", 0, 5), PG([(62, 40), (82, 30), (82, 58), (62, 48)], "W"), wl(40, 58, 40, 82, 6), wl(28, 82, 52, 82, 5))),
    ("geschwindigkeitsueberwachung", "Geschwindigkeitsüberwachung", *VB,
     vq(R(28, 16, 44, 44, "W", "N", 0, 6), C(50, 34, 10, "F", "N", 0), R(40, 50, 20, 5, "F", "N", 0), wl(50, 60, 50, 84, 7))),
    ("notrufsaeule", "Notrufsäule", *OR, vt("SOS", 24, 66)),
    ("einbahnstrasse", "Einbahnstraße (nach rechts, drehbar)", *VB, vq(*arrow(18, 50, 84, 50, 11, 26, "W"))),
    # ---- Baustellen und Stoerungen (orange) ----
    ("baustelle", "Baustelle", *OR, vq(*CONE)),
    ("umleitung", "Umleitung", *OR, vq(PL([(28, 82), (28, 44), (40, 44)], 8, "W"), *arrow(28, 44, 82, 44, 8, 20, "W"))),
    ("stau", "Stau / Verkehrsstörung", *OR, vq(*fit(CAR, 34, 34, 0.5), *fit(CAR, 66, 34, 0.5), *fit(CAR, 34, 68, 0.5), *fit(CAR, 66, 68, 0.5))),
    ("unfall", "Unfall / Unfallhäufungsstelle", *OR, vq(PG(star(50, 50, 38, 22, 10), "W"), T("!", 50, 50, 30, "F"))),
    # ---- Sperrungen, Gefahr, Beschraenkungen (rot) ----
    ("sperrung", "Sperrung / Durchfahrt verboten", *RT, vq(R(18, 41, 64, 18, "W", "N", 0, 2))),
    ("gefahrstelle", "Gefahrstelle", *RT, vq(T("!", 50, 50, 54, "W"))),
    ("hoehenbeschraenkung", "Höhenbeschränkung", *RT,
     vq(PG([(36, 16), (64, 16), (50, 32)], "W"), PG([(36, 84), (64, 84), (50, 68)], "W"), T("m", 50, 50, 20, "W"))),
    ("gewichtsbeschraenkung", "Gewichtsbeschränkung", *RT, vq(T("t", 50, 50, 46, "W"))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
V0, VD, VL, O0, OD, R0, R1 = VB[0], VB[1], "#C9DCF2", OR[0], OR[1], RT[0], RT[1]

LINIEN = [
    ("Autobahn", [linie(VD, 2.4), linie(V0, 1.8), linie("#FFFFFF", 0.3)]),
    ("Bundesstraße", [linie(VD, 1.8), linie(V0, 1.2)]),
    ("Landes- und Kreisstraße", [linie(VD, 1.4), linie(VL, 0.9)]),
    ("Gemeindestraße", [linie(VD, 1.0), linie("#FFFFFF", 0.6)]),
    ("Wirtschaftsweg", [linie(VD, 0.3, [4, 1.5])]),
    ("Radweg", [linie(V0, 0.6, [3, 1])]),
    ("Fußweg", [linie(V0, 0.4, [1, 1])]),
    ("Bahnstrecke", [linie(VD, 1.1), linie("#FFFFFF", 0.6, [3, 3])]),
    ("Straßenbahn, Stadtbahn", [linie(VD, 0.5), marken(mk("line", 1.6, VD, rw=0.3), 2.5)]),
    ("Buslinie", [linie(V0, 0.8)]),
    ("Fährlinie", [linie(V0, 0.5, [1, 1.5])]),
    ("Einbahnstraße, Fahrtrichtung", [linie(V0, 0.6), marken(mk("filled_arrowhead", 2.2, VD), 9)]),
    ("Baustelle", [linie(O0, 1.2, [2, 1])]),
    ("Umleitung", [linie(O0, 0.8), marken(mk("filled_arrowhead", 2.4, OD), 9)]),
    ("Sperrung", [linie(R0, 1.0), marken(mk("cross2", 2.0, R1, rw=0.45), 6)]),
    ("Stau, stockender Verkehr", [linie(R0, 1.6)]),
]

FLAECHEN = [
    ("Parkfläche", [voll(VL), linie(V0, 0.4)]),
    ("Verkehrsfläche", [voll("#E3ECF7"), linie(V0, 0.3)]),
    ("Fußgängerzone", [voll("#E3ECF7"), muster(mk("circle", 0.6, V0), 2.4, versatz=1.2), linie(V0, 0.4)]),
    ("Verkehrsberuhigter Bereich", [schraffur(V0, 0.25, 45, 2.5), linie(V0, 0.4)]),
    ("Tempo-30-Zone", [band(V0 + "59", 1.5), linie(V0, 0.4, [3, 1.5])]),
    ("Bewohnerparkzone", [voll(V0 + "26"), linie(V0, 0.4, [3, 1.5])]),
    ("Bahngelände", [voll(VD + "40"), linie(VD, 0.4)]),
    ("Baustellenbereich", [voll(O0 + "33"), schraffur(O0, 0.4, 45, 2.5), linie(OD, 0.4)]),
    ("Sperrbereich", [voll(R0 + "26"), schraffur(R0, 0.4, 45, 2.5), schraffur(R0, 0.4, 135, 2.5), linie(R1, 0.4)]),
    ("Halteverbotszone", [schraffur(R0, 0.3, 135, 2.5), linie(R1, 0.4, [3, 1.5])]),
]
