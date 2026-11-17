"""Sammlung Laerm und Immissionen: Immissionsorte und Messstellen, Quellen, Schutzmassnahmen und Planung,
schutzbeduerftige Nutzungen, Hilfszeichen der Schallausbreitung.
Orientierung: 34. BImSchV (Laermkartierung), DIN 45682 (thematische Karten im Schallimmissionsschutz),
DIN 18005 (Schallschutz im Staedtebau), TA Laerm (Immissionsorte, Richtwerte), Fluglaermgesetz (Schutzzonen).
Fuer die Punktsymbole gibt es keine genormten Vorlagen; eigene, schlichte Entwuerfe.
Stil: hellviolette Fuellung, dunkelvioletter Strich 5. Die Rahmenform zeigt die Gruppe:
  Kreis = Immissionsort oder Messung, Quadrat = Quelle, Raute = Schutzmassnahme oder Planung,
  Sechseck = schutzbeduerftige Nutzung/Gebiet, ohne Rahmen = Hilfszeichen der Schallausbreitung.
  Wiederkehrendes Sinnbild fuer Schall: Lautsprecher mit Schallboegen (SCHALL, LAUT, BOGEN).
Linien und Flaechen: violett; Bestand durchgezogen, geplant gestrichelt. Einzige Ausnahme sind die Pegelklassen:
  Vollfarben nach der Tabelle "Farben der DIN 45682 fuer LDEN und LNight" (Tabelle 1 der LAI-Hinweise zur
  Laermkartierung, Fassung vom 08.08.2025, mit RGB- und Hex-Werten; die 34. BImSchV verweist in Paragraf 4 auf
  DIN 45682, Ausgabe April 2020). Die Norm selbst lag nicht vor; die Werte sind aus der LAI-Tabelle uebernommen.
  Klassen wie dort mit gerundeten Pegeln ("ab 55 bis 59 dB(A)" umfasst 54,5 bis 59,4).
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "laerm"
NAME = "Lärm und Immissionen"
DESC = ("Symbole für Lärm und Immissionen: Immissionsorte und Messstellen, Lärmquellen, Schallschutz und "
        "Lärmaktionsplanung, schutzbedürftige Nutzungen, Pegelklassen der Lärmkartierung")
TAGS = "laerm, schall, immissionen, immissionsschutz, laermkartierung, laermschutz, schallschutz, geruch, luft"

LV = ("#EFE3F5", "#5E2B7E")


def io(*sh):  # Immissionsort, Messung
    return fr_circle() + list(sh)


def qu(*sh):  # Quelle
    return fr_square() + list(sh)


def sm(*sh):  # Schutzmassnahme, Planung
    return fr_diamond() + list(sh)


def nu(*sh):  # schutzbeduerftige Nutzung, Gebiet
    return fr_hex() + list(sh)


def nut(txt, h=22, mw=58):
    return nu(T(txt, 50, 50, h, maxw=mw))


def bogen(cx, cy, radien, a0=40, a1=140, sw=5):  # Schallboegen, Vorgabe: nach rechts
    return [arc(cx, cy, r, a0, a1, sw) for r in radien]


# Sinnbild fuer Schall: Lautsprecher mit Schallboegen
LAUT = [PG([(18, 40), (31, 40), (47, 25), (47, 75), (31, 60), (18, 60)], "S", "S", 3)]
BOGEN = bogen(45, 50, (19, 33), sw=5.5)
SCHALL = LAUT + BOGEN

MIKRO = [R(40, 14, 20, 38, "S", "N", 0, 10), P("M30,40 A20,20 0 0 0 70,40", "N", "S", 5), L(50, 60, 50, 80, 5),
         L(36, 81, 64, 81, 5)]
STATIV = [R(42, 12, 16, 32, "S", "N", 0, 8), L(50, 44, 50, 60, 5), L(50, 58, 30, 85, 5), L(50, 58, 70, 85, 5),
          L(50, 58, 50, 85, 5)]
CAR = [P("M15,64 V53 Q15,48 21,47 L31,45 L40,31 H62 L72,45 L80,47 Q85,48 85,53 V64 Z", "S", "S", 3),
       PG([(43, 36), (49, 36), (49, 45), (38, 45)], "F"), PG([(54, 36), (60, 36), (66, 45), (54, 45)], "F"),
       C(33, 65, 8.5, "F", "S", 5), C(67, 65, 8.5, "F", "S", 5)]
TRAIN = [R(29, 14, 42, 54, "S", "N", 0, 10), R(36, 22, 28, 18, "F", "N", 0, 3), C(39, 54, 4.5, "F", "N", 0),
         C(61, 54, 4.5, "F", "N", 0), L(38, 70, 28, 86, 5.5), L(62, 70, 72, 86, 5.5)]
FABRIK = [P("M16,80 V50 L34,60 V50 L52,60 V50 L64,57 V20 H78 V80 Z", "S", "S", 3)]
BALL = [C(50, 50, 28, "F", "S", 5), L(50, 22, 50, 78, 4), L(22, 50, 78, 50, 4), P("M31,30 Q47,50 31,70", "N", "S", 4),
        P("M69,30 Q53,50 69,70", "N", "S", 4)]
NOTEN = [E(33, 72, 10.5, 8, "S", "N", 0), E(67, 64, 10.5, 8, "S", "N", 0), L(41, 72, 41, 28, 5), L(75, 64, 75, 20, 5),
         PG([(38.5, 22), (77.5, 13), (77.5, 27), (38.5, 36)], "S")]
CONE = [PG([(44, 18), (56, 18), (69, 70), (31, 70)], "S"), R(20, 70, 60, 11, "S", "N", 0, 3),
        L(39.5, 37, 60.5, 37, 6, "F", "butt"), L(35.5, 54, 64.5, 54, 6, "F", "butt")]
PIG = [E(45, 54, 25, 16, "S", "N", 0), C(72, 50, 11, "S", "N", 0), R(79, 46, 10, 9, "S", "N", 0, 2),
       PG([(64, 43), (68, 29), (76, 41)], "S"), L(32, 64, 32, 80, 5.5), L(43, 66, 43, 80, 5.5), L(55, 66, 55, 80, 5.5),
       L(63, 62, 63, 80, 5.5), P("M21,50 q-8,-3 -3,-10", "N", "S", 4), C(73, 47, 2.2, "F", "N", 0)]
FAN = [C(50, 50, 31, "N", "S", 5)] + [pie(50, 50, 24, a + 6, a + 62) for a in (0, 90, 180, 270)] + [C(50, 50, 6, "S", "N", 0)]
DUFT = [P(f"M{x},78 q-9,-14 0,-28 t0,-28", "N", "S", 5.5) for x in (32, 50, 68)]
BUCH = [P("M50,34 Q35,25 20,31 V70 Q35,64 50,73 Q65,64 80,70 V31 Q65,25 50,34 Z", "F", "S", 5), L(50, 34, 50, 73, 4.5)]

S = [
    # ---- Immissionsorte und Messung (Kreis) ----
    ("immissionsort", "Immissionsort", *LV, io(T("IO", 50, 50, 34, maxw=56))),
    ("immissionsort_massgeblich", "Maßgeblicher Immissionsort", *LV, io(C(50, 50, 34, "N", "S", 3.5), T("IO", 50, 50, 26))),
    ("messpunkt_schall", "Messpunkt Schall", *LV, io(*fit(MIKRO, 50, 51, 0.88))),
    ("dauermessstation", "Dauermessstation Schall", *LV, io(*fit(STATIV, 38, 50, 0.84), *bogen(50, 28, (11, 21), 50, 130, 4.5))),
    ("luftmessstation", "Luftmessstation", *LV,
     io(cloud([(31, 50, 12), (48, 40, 17), (67, 49, 13)], "F", "S", 5), *[C(x, 73, 3.5, "S", "N", 0) for x in (36, 50, 64)])),
    ("erschuetterungsmesspunkt", "Erschütterungsmesspunkt", *LV,
     io(PL([(13, 50), (26, 50), (34, 30), (45, 70), (55, 30), (66, 70), (74, 50), (87, 50)], 5))),
    ("geruchsmesspunkt", "Geruchsmesspunkt", *LV, io(*fit(DUFT, 50, 50, 0.9))),
    ("staubmesspunkt", "Staubmesspunkt", *LV,
     io(*[C(x, y, r, "S", "N", 0) for x, y, r in ((34, 36, 7), (56, 30, 4.5), (70, 44, 6), (48, 50, 5), (30, 58, 4.5),
                                                   (44, 70, 6.5), (64, 64, 7.5))])),
    ("lichtimmission", "Messpunkt Lichtimmission", *LV, io(*sun(50, 50, 12, "S", "S", 5, 8, 7, 9))),
    ("wetterstation", "Wetterstation", *LV,
     io(L(50, 82, 50, 36, 5), L(36, 82, 64, 82, 5), *arrow(26, 36, 80, 36, 5.5, 14), PG([(20, 25), (36, 25), (36, 47), (20, 47), (27, 36)], "S"))),
    # ---- Quellen (Quadrat) ----
    ("punktquelle", "Punktquelle / Schallquelle allgemein", *LV, qu(*fit(SCHALL, 51, 50, 1.0))),
    ("quelle_strasse", "Lärmquelle Straße", *LV, qu(*fit(CAR, 50, 52, 0.98))),
    ("quelle_schiene", "Lärmquelle Schiene", *LV, qu(*TRAIN)),
    ("quelle_flug", "Lärmquelle Flugverkehr", *LV, qu(*plane(50, 50, 1.05, "S", 45))),
    ("quelle_gewerbe", "Lärmquelle Industrie und Gewerbe", *LV, qu(*fit(FABRIK, 52, 50, 1.0))),
    ("quelle_sport", "Sportanlage", *LV, qu(*BALL)),
    ("quelle_freizeit", "Freizeitanlage / Veranstaltung", *LV, qu(*fit(NOTEN, 48, 54, 0.95))),
    ("quelle_baustelle", "Baustelle", *LV, qu(*fit(CONE, 50, 51, 1.0))),
    ("quelle_wea", "Windenergieanlage", *LV, qu(L(50, 42, 50, 86, 5.5), *rotor(50, 42, 29))),
    ("quelle_schornstein", "Schornstein / Emissionsquelle", *LV,
     qu(PG([(34, 86), (40, 42), (56, 42), (62, 86)], "S"), cloud([(50, 28, 8), (63, 22, 11), (77, 28, 8)], "F", "S", 4.5))),
    ("quelle_tierhaltung", "Tierhaltung / Geruchsquelle", *LV, qu(*fit(PIG, 50, 48, 0.92))),
    ("quelle_lueftung", "Lüftungsanlage / haustechnische Anlage", *LV, qu(*FAN)),
    # ---- Schutzmassnahmen und Planung (Raute) ----
    ("laermschutzwand", "Lärmschutzwand", *LV, sm(R(56, 28, 9, 44, "S", "N", 0, 1), *bogen(25, 50, (12, 24), 45, 135, 5))),
    ("laermschutzwall", "Lärmschutzwall", *LV, sm(PG([(27, 64), (42, 38), (58, 38), (73, 64)], "S", "S", 3))),
    ("passiver_schallschutz", "Passiver Schallschutz / Schallschutzfenster", *LV,
     sm(R(34, 30, 32, 40, "F", "S", 5), L(50, 30, 50, 70, 4, cap="butt"), L(34, 46, 66, 46, 4, cap="butt"))),
    ("fahrbahnbelag", "Lärmmindernder Fahrbahnbelag", *LV,
     sm(R(24, 41, 52, 18, "S", "N", 0, 2), *[L(x, 50, x + 9, 50, 3.5, "F", "butt") for x in (29, 45.5, 62)])),
    ("tempolimit", "Geschwindigkeitsbeschränkung aus Lärmschutzgründen", *LV,
     sm(C(50, 50, 22, "N", "S", 5), T("30", 50, 50, 15, maxw=28))),
    ("laermminderung", "Lärmminderungsmaßnahme / Lärmsanierung", *LV,
     sm(T("dB", 42, 50, 17, maxw=30), *arrow(68, 34, 68, 66, 5.5, 12))),
    ("laermbrennpunkt", "Lärmbrennpunkt / Hotspot", *LV, sm(PG(star(50, 50, 27, 19, 8), "S"), T("!", 50, 50, 21, "F"))),
    # ---- Schutzbeduerftige Nutzungen und Gebiete (Sechseck) ----
    ("nutzung_wohnen", "Schutzbedürftige Nutzung Wohnen", *LV, nu(*fit(house(), 50, 51, 0.82))),
    ("nutzung_schule", "Schutzbedürftige Nutzung Schule", *LV, nu(*fit(BUCH, 50, 50, 0.9))),
    ("nutzung_kita", "Schutzbedürftige Nutzung Kindertagesstätte", *LV, nut("KITA", 19)),
    ("nutzung_krankenhaus", "Schutzbedürftige Nutzung Krankenhaus", *LV,
     nu(R(41, 23, 18, 54, "S", "N", 0), R(23, 41, 54, 18, "S", "N", 0))),
    ("nutzung_kurgebiet", "Kurgebiet", *LV, nut("KUR")),
    ("ruhiges_gebiet", "Ruhiges Gebiet", *LV, nu(*fit(LAUT + xcross(66, 50, 10, 6), 54, 50, 0.95))),
    # ---- Schallausbreitung (ohne Rahmen) ----
    ("schallausbreitung", "Schallausbreitungsrichtung", *LV,
     [C(13, 50, 8, "S", "N", 0), *bogen(13, 50, (21, 35), 45, 135, 5.5), *arrow(58, 50, 96, 50, 6, 15)]),
    ("reflexion", "Reflexion", *LV,
     [R(80, 6, 11, 88, "S", "N", 0, 1), *arrow(10, 14, 76, 50, 5.5, 15), *arrow(76, 50, 14, 84, 5.5, 15)]),
    ("abschirmkante", "Abschirmkante / Beugungskante", *LV,
     [R(45, 40, 10, 54, "S", "N", 0, 1), L(6, 94, 94, 94, 5), C(12, 74, 7, "S", "N", 0),
      P("M12,74 L50,28 L90,74", "N", "S", 4.5, dash="7 7"), C(50, 30, 7, "F", "S", 4)]),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
V0, VL = LV[1], LV[0]

LINIEN = [
    ("Lärmschutzwand", [linie(V0, 0.9), marken(mk("line", 1.4, V0, rw=0.3, dy=0.7), 2.5)]),
    ("Lärmschutzwand, geplant", [linie(V0, 0.9, [3, 1.5])]),
    ("Lärmschutzwall", [linie(V0 + "40", 2.6), marken(mk("line", 2.6, V0, rw=0.3), 1.8), linie(V0, 0.25, versatz=1.3),
                        linie(V0, 0.25, versatz=-1.3)]),
    ("Lärmschutzwall, geplant", [linie(V0 + "40", 2.6), linie(V0, 0.25, [3, 1.5], versatz=1.3),
                                 linie(V0, 0.25, [3, 1.5], versatz=-1.3)]),
    ("Isophone, Hauptlinie", [linie(V0, 0.6)]),
    ("Isophone, Zwischenlinie", [linie(V0, 0.25)]),
    ("Emissionsband Straße", [linie(V0 + "59", 2.4), linie(V0, 0.4)]),
    ("Emissionsband Schiene", [linie(V0 + "59", 2.4), linie(V0, 0.4), marken(mk("line", 1.6, V0, rw=0.35), 3)]),
    ("Grenze Lärmschutzbereich", [linie(V0, 0.6, [6, 1.5, 1, 1.5])]),
    ("Baugrenze aus Lärmschutzgründen", [linie(V0, 0.5, [4, 1, 0.6, 1, 0.6, 1])]),
    ("Schallausbreitungsweg", [linie(V0, 0.3, [1.5, 1]), marken(mk("filled_arrowhead", 2.0, V0), 12)]),
]

# Pegelklassen: Farben der DIN 45682 fuer LDEN und LNight nach Tabelle 1 der LAI-Hinweise zur Laermkartierung
PEGEL = [("ab 45 bis 49 dB(A), nur LNight", "#A0BABF"), ("ab 50 bis 54 dB(A), nur LNight", "#B8D6D1"),
         ("ab 55 bis 59 dB(A)", "#E2F2BF"), ("ab 60 bis 64 dB(A)", "#F3C683"), ("ab 65 bis 69 dB(A)", "#CD463E"),
         ("ab 70 bis 74 dB(A), LNight ab 70 dB(A)", "#75085C"), ("ab 75 dB(A), nur LDEN", "#430A4A")]

FLAECHEN = [(f"Pegelklasse {t}", [voll(c)]) for t, c in PEGEL] + [
    ("Ruhiges Gebiet", [voll(VL + "80"), band(V0 + "59", 1.5), linie(V0, 0.3)]),
    ("Lärmschutzbereich Tag-Schutzzone 1", [voll(V0 + "66"), linie(V0, 0.4)]),
    ("Lärmschutzbereich Tag-Schutzzone 2", [voll(V0 + "26"), linie(V0, 0.4)]),
    ("Lärmschutzbereich Nacht-Schutzzone", [schraffur(V0, 0.25, 45, 2.5), linie(V0, 0.4, [4, 1.5])]),
    ("Geruchsimmissionsbereich", [muster(mk("circle", 0.6, V0), 2.2, versatz=1.1), linie(V0, 0.4, [3, 1.5])]),
    ("Richtwertüberschreitung", [schraffur(V0, 0.25, 45, 2.5), schraffur(V0, 0.25, 135, 2.5), linie(V0, 0.5)]),
]
