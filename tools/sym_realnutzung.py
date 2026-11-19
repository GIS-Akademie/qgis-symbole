"""Sammlung Realnutzung: Flaechen der tatsaechlichen Nutzung fuer Realnutzungs- und Flaechennutzungskartierungen.
Gliederung und Bezeichnungen: Katalog der tatsaechlichen Nutzungsarten im Liegenschaftskataster
(AdV-Nutzungsartenkatalog, GeoInfoDok 7.0.1, Stand 08.04.2015): vier Bereiche (10000 Siedlung, 20000 Verkehr,
30000 Vegetation, 40000 Gewaesser) mit 26 Nutzungsartengruppen, fuenfstelliger Schluessel.
Farben und Zeichen: ALKIS-Signaturenkatalog der AdV, Teil B, Signaturenbibliothek Farbe (Version 6.0):
Flaechenfarben der Signaturen 1401 bis 1414 (dort in CMYK-Prozent, hier in RGB umgerechnet), Vegetationszeichen
der Signaturen 3413 bis 3478 in Gruen. Eigene Nachkonstruktionen in Anlehnung daran, keine amtlichen Vorlagen.

Stil der Punktsymbole: gruen #00853C, ohne Rahmen, Strich 6; Praefix veg_ = Vegetationszeichen. Sie dienen
zugleich als Fuellmuster der Flaechen.
Flaechen: Titel = Schluessel und Bezeichnung des Katalogs. Zwei Reihen:
  ohne Zusatz   blasse Flaechenfarbe wie in der Liegenschaftskarte (Verkehr ohne Fuellung), Vegetation mit Zeichen
  ", kraeftig"  eigene, kraeftigere Farben fuer Uebersichtskarten (nicht amtlich); Siedlung rot bis violett,
                Gewerbe grau, Verkehr grau, Landwirtschaft gelb, Wald gruen, Gewaesser blau
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "realnutzung"
NAME = "Realnutzung"
DESC = ("Flächensymbole für Realnutzungskartierungen nach dem AdV-Nutzungsartenkatalog (tatsächliche Nutzung im "
        "Liegenschaftskataster): Siedlung, Verkehr, Vegetation und Gewässer mit Schlüsselnummer, in den blassen "
        "Farben der Liegenschaftskarte (ALKIS-Signaturenkatalog) und in kräftigen Farben für Übersichtskarten; "
        "dazu die Vegetationszeichen als Punktsymbole")
TAGS = "realnutzung, tatsächliche nutzung, nutzungsart, flächennutzung, landnutzung, alkis, adv, kataster"

GRN = "#00853C"            # Vegetationszeichen (Signaturenkatalog: Gruen 100-0-100-0)
VG = ("#FFFFFF", GRN)
RAND = "#7A7A7A"

# Flaechenfarben des ALKIS-Signaturenkatalogs (CMYK-Prozent -> RGB)
WOHN = "#FFEBF5"     # 1401  0-8-4-0    Wohnbauflaeche, gemischte Nutzung, besondere funktionale Praegung
IND = "#EDEDED"      # 1403  0-0-0-7    Industrie und Gewerbe, Halde, Bergbau, Tagebau
BRACH = "#F2EBE8"    # 1404  5-8-9-0    Brachland, Heide, Moor, Sumpf
ERH = "#E0FFD9"      # 1405  12-0-15-0  Sport, Freizeit, Erholung, Friedhof, Gruenanlage
GRUEN = "#EBFFD4"    # 1406  8-0-17-0   Gruenland, Gartenland, Obst, Weingarten, Flugverkehr
ACKER = "#FFF7BF"    # 1409  0-3-25-0   Ackerland, Landwirtschaft
WASSER = "#E3FFFF"   # 1410  11-0-0-0   Gewaesser
WALD = "#D9FFD9"     # 1414  15-0-15-0  Wald, Gehoelz


def blade(x, top, lean=0, w=5):  # Halm: unten breit, oben spitz; lean neigt die Spitze nach links/rechts
    return P(f"M{x - w},80 Q{x - w + lean * 0.3},{(80 + top) / 2} {x + lean},{top} "
             f"Q{x + w + lean * 0.5},{(80 + top) / 2} {x + w},80 Z", "S", "N", 0)


LAUB = [C(44, 44, 24, "N", "S", 6), L(44, 68, 80, 68, 6)]                       # Ring mit Fusslinie
NADEL = [PL([(26, 72), (46, 16), (60, 72)], 6, close=True), L(60, 72, 82, 72, 6)]  # Dreieck mit Fusslinie
BAUM = [C(50, 32, 19, "N", "S", 6), L(50, 51, 50, 88, 6)]                        # Ring auf Stamm

S = [
    # ---- Wald und Gehoelz ----
    ("veg_wald", "Wald", *VG,
     [PL([(12, 76), (30, 28), (44, 76), (54, 76)], 6), arc(70, 40, 15, -140, 140, 6), L(78, 53, 92, 53, 6)]),
    ("veg_laubholz", "Laubholz", *VG, LAUB),
    ("veg_nadelholz", "Nadelholz", *VG, NADEL),
    ("veg_laub_nadelholz", "Laub- und Nadelholz", *VG,
     fit(NADEL, 30, 58, 0.62) + fit(LAUB, 70, 40, 0.62)),
    ("veg_gehoelz", "Gehölz", *VG,
     [arc(32, 56, 17, -140, 140, 6), PL([(58, 74), (72, 26), (86, 74)], 6)]),
    # ---- Landwirtschaft ----
    ("veg_gruenland", "Grünland", *VG, [C(30, 50, 9, "S", "N", 0), C(70, 50, 9, "S", "N", 0)]),
    ("veg_gartenland", "Gartenland", *VG,
     [C(50, 28, 9, "S", "N", 0), C(26, 68, 9, "S", "N", 0), C(74, 68, 9, "S", "N", 0)]),
    ("veg_obst", "Obstbaum, Streuobst", *VG, BAUM),
    ("veg_obstplantage", "Obstplantage", *VG, fit(BAUM, 64, 46, 0.85) + fit(BAUM, 28, 64, 0.5)),
    ("veg_baumschule", "Baumschule", *VG,
     fit(BAUM, 34, 48, 0.85) + [PG([(60, 62), (72, 30), (84, 62)], "S"), L(72, 62, 72, 82, 6)]),
    ("veg_weingarten", "Weingarten", *VG, [L(34, 18, 34, 84, 7), PG([(48, 84), (62, 36), (76, 84)], "S")]),
    ("veg_hopfen", "Hopfen", *VG, [L(22, 20, 78, 82, 6), L(78, 20, 22, 82, 6)]),
    # ---- Heide, Moor, Sumpf ----
    ("veg_heide", "Heide", *VG, [blade(50, 22), blade(28, 44, -14), blade(72, 44, 14)]),
    ("veg_moor", "Moor", *VG,
     [blade(50, 26, 0, 4), blade(33, 36, -9, 4), blade(67, 36, 9, 4), blade(16, 52, -12, 4), blade(84, 52, 12, 4)]),
    ("veg_sumpf", "Sumpf", *VG,
     [blade(50, 28, 10), blade(30, 42, -14), blade(72, 42, 16), L(14, 90, 86, 90, 6)]),
]

SYMBOLS = S


def zeichen(name, dx=9.0, dy=7.0, g=3.2):
    return muster(sv(name, g, "#FFFFFF", GRN), dx, dy, versatz=dx / 2)


def um(breite=0.2):
    return linie(RAND, breite)


LINIEN = [
    ("Grenze der Nutzungsart", [linie(RAND, 0.25)]),
    ("Grenze der Nutzungsartengruppe", [linie("#4D4D4D", 0.5)]),
    ("Grenze des Nutzungsartenbereichs", [linie("#4D4D4D", 0.9)]),
    ("Grenze der Kartiereinheit", [linie("#4D4D4D", 0.4, [4, 1.5])]),
    ("Grenze, unsicher", [linie(RAND, 0.3, [1.5, 1.5])]),
    ("Baumreihe, Laubholz", [marken(sv("veg_laubholz", 3.2, "#FFFFFF", GRN), 6)]),
    ("Baumreihe, Nadelholz", [marken(sv("veg_nadelholz", 3.2, "#FFFFFF", GRN), 6)]),
]

# (Schluessel und Bezeichnung, Ebenen wie in der Liegenschaftskarte, kraeftige Farbe oder None)
_F = [
    # ---- 10000 Siedlung ----
    ("11000 Wohnbaufläche", [voll(WOHN)], "#E58B8B"),
    ("12000 Industrie- und Gewerbefläche", [voll(IND)], "#9E9E9E"),
    ("13000 Halde", [voll(IND)], "#B8A68F"),
    ("14000 Bergbaubetrieb", [voll(IND)], "#8C7B6B"),
    ("15000 Tagebau, Grube, Steinbruch", [voll(IND)], "#C9B28F"),
    ("16000 Fläche gemischter Nutzung", [voll(WOHN)], "#E8A76B"),
    ("17000 Fläche besonderer funktionaler Prägung", [voll(WOHN)], "#C58BC5"),
    ("18000 Sport-, Freizeit- und Erholungsfläche", [voll(ERH)], "#8FD18A"),
    ("18500 Grünanlage", [voll(ERH), zeichen("veg_gruenland", 8, 6, 2.6)], "#A9DB8F"),
    ("19000 Friedhof", [voll(ERH)], "#5E9E6B"),
    # ---- 20000 Verkehr ----
    ("21000 Straßenverkehr", [voll("#FFFFFF")], "#D9D9D9"),
    ("22000 Weg", [voll("#FFFFFF")], "#E6DCC8"),
    ("23000 Platz", [voll("#FFFFFF")], "#CFCFCF"),
    ("24000 Bahnverkehr", [voll("#FFFFFF")], "#B39BB3"),
    ("25000 Flugverkehr", [voll(GRUEN)], "#C8C8DC"),
    ("26000 Schiffsverkehr", [voll("#FFFFFF")], "#9FB8D9"),
    # ---- 30000 Vegetation ----
    ("31000 Landwirtschaft", [voll(ACKER)], "#F2DE7A"),
    ("31100 Ackerland", [voll(ACKER)], "#F2DE7A"),
    ("31200 Grünland", [voll(GRUEN), zeichen("veg_gruenland", 8, 6, 2.6)], "#B5DE7A"),
    ("31300 Gartenland", [voll(GRUEN), zeichen("veg_gartenland", 8, 7, 2.8)], "#C9E08A"),
    ("31400 Weingarten", [voll(GRUEN), zeichen("veg_weingarten", 7, 7, 3.0)], "#C7D46A"),
    ("31500 Obstplantage", [voll(GRUEN), zeichen("veg_obstplantage", 9, 8, 3.6)], "#A8D46A"),
    ("31600 Kurzumtriebsplantage", [voll(GRUEN), zeichen("veg_baumschule", 9, 8, 3.6)], None),
    ("31700 Brachland", [voll(BRACH)], "#D8C9A8"),
    ("32000 Wald", [voll(WALD), zeichen("veg_wald", 10, 8, 3.8)], "#4F9E4F"),
    ("32100 Laubholz", [voll(WALD), zeichen("veg_laubholz")], "#63B35A"),
    ("32200 Nadelholz", [voll(WALD), zeichen("veg_nadelholz")], "#2F7F4A"),
    ("32300 Laub- und Nadelholz", [voll(WALD), zeichen("veg_laub_nadelholz", 10, 8, 3.8)], "#478F4C"),
    ("33000 Gehölz", [voll(WALD), zeichen("veg_gehoelz", 10, 8, 3.6)], "#86BF73"),
    ("34000 Heide", [voll(BRACH), zeichen("veg_heide", 8, 7, 3.0)], "#C9A3C4"),
    ("35000 Moor", [voll(BRACH), zeichen("veg_moor", 9, 7, 3.2)], "#B08F6E"),
    ("36000 Sumpf", [voll(BRACH), zeichen("veg_sumpf", 9, 7, 3.2)], "#8FC2B0"),
    ("37000 Unland, Vegetationslose Fläche", [voll("#FFFFFF")], "#D9D2C3"),
    # ---- 40000 Gewaesser ----
    ("41000 Fließgewässer", [voll(WASSER)], "#6FB7E8"),
    ("42000 Hafenbecken", [voll(WASSER)], "#5C9FD1"),
    ("43000 Stehendes Gewässer", [voll(WASSER)], "#8CCBF0"),
    ("44000 Meer", [voll(WASSER)], "#4F93C9"),
]

FLAECHEN = ([(t, eb + [um()]) for t, eb, _ in _F]
            + [(t + ", kräftig", [voll(k), linie(RAND, 0.25)]) for t, _, k in _F if k])
