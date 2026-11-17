"""Sammlung Gas, Fernwaerme, Telekommunikation: Stationen, Messstellen und Einrichtungen, Armaturen und
Netzelemente fuer Leitungs- und Bestandsplaene der drei Sparten.
Orientierung: Rohrnetzplaene nach DIN 2425 (Teil 1 Gas und Wasser, Teil 2 Fernwaerme; Teil 1 ist inzwischen
zurueckgezogen), Netzdokumentation nach DVGW GW 120, Fliessbild-Schaltzeichen fuer Armaturen, uebliche
Spartenfarben und Kurzzeichen der Leitungsauskunft. Ein verbindliches Regelwerk fuer Punktsymbole im GIS
gibt es nicht; eigene Entwuerfe.
Stil: Strich 5. Die Farbe zeigt die Sparte:
  Gas = gelb mit ockerbraunem Strich, Fernwaerme = hellrot mit orangerotem Strich,
  Telekommunikation = hellgruen mit gruenem Strich.
Die Form zeigt die Gruppe:
  Quadrat (abgerundet) = Station oder Anlage, Kreis = Messstelle oder Einrichtung,
  ohne Rahmen = Armatur oder Netzelement auf der Leitung (Leitung waagerecht durch die Symbolmitte).
Symbolnamen mit Praefix gas_, fw_, tk_.
Linien und Flaechen: Strichfarbe der Sparte. Gas: Strichstaerke = Druckstufe; Fernwaerme: Vorlauf voll,
Ruecklauf strichpunktiert; durchgezogen = Bestand, gestrichelt = geplant, Kreuze = stillgelegt.
Flaechen: Schutzstreifen schraffiert, Versorgungs- und Ausbaugebiet mit Randband oder heller Fuellung,
Betriebsgelaende in der Fuellfarbe der Sparte.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "leitungen"
NAME = "Gas, Fernwärme, Telekommunikation"
DESC = ("Symbole für Leitungspläne der Sparten Gas, Fernwärme und Telekommunikation: Stationen und Anlagen, "
        "Messstellen, Armaturen und Netzelemente, Leitungen, Schutzstreifen und Versorgungsgebiete")
TAGS = "leitungen, gas, fernwaerme, telekommunikation, glasfaser, leitungsplan, leitungsauskunft, netz, breitband"

GAS = ("#FFF3B0", "#9A6B00")
FW = ("#FBE0D2", "#C2410C")
TK = ("#DDF0E0", "#1B7F3B")


def st(*sh):  # Station, Anlage
    return fr_square() + list(sh)


def stt(txt, h=26, mw=66):
    return st(T(txt, 50, 50, h, maxw=mw))


def kr(*sh):  # Messstelle, Einrichtung
    return fr_circle() + list(sh)


def ltg(x0=4, x1=96):  # Leitung durch die Symbolmitte
    return L(x0, 50, x1, 50, 5, cap="butt")


def kennz(txt):  # Kennzeichen auf der Leitung
    return [ltg(4, 20), ltg(80, 96), T(txt, 50, 50, 26, maxw=52)]


BOWTIE = [PG([(24, 30), (50, 50), (24, 70)], "F", "S", 5), PG([(76, 30), (50, 50), (76, 70)], "F", "S", 5)]
ARMATUR = [ltg(4, 24), ltg(76, 96)] + BOWTIE
# Hausanschluss: Abzweig von der Leitung zum Gebaeude
ANSCHLUSS = [ltg(), L(50, 50, 50, 34, 5, cap="butt"), R(34, 8, 32, 28, "S", "N", 0, 2)]
PUMPE = [C(50, 50, 28, "N", "S", 4.5), PG([(38, 30), (38, 70), (74, 50)], "S")]
DISH = [chord(50, 44, 28, 135, 315), L(50, 44, 70, 24, 5), C(72, 22, 6, "S", "N", 0),
        PL([(38, 66), (30, 88)], 5.5), L(18, 88, 52, 88, 5.5)]

S = [
    # ---- Gas: Stationen und Anlagen (Quadrat) ----
    ("gas_druckregelanlage", "Gasdruckregelanlage (GDRA)", *GAS,
     st(L(16, 62, 30, 62, 5, cap="butt"), L(70, 62, 84, 62, 5, cap="butt"),
        PG([(30, 46), (50, 62), (30, 78)], "S", "S", 4), PG([(70, 46), (50, 62), (70, 78)], "S", "S", 4),
        L(50, 62, 50, 36, 4.5, cap="butt"), P("M32,36 A18,18 0 0 1 68,36 Z", "S", "S", 4))),
    ("gas_uebergabestation", "Gas-Übergabestation / Übernahmestation", *GAS, stt("ÜS", 32)),
    ("gas_verdichter", "Verdichterstation", *GAS,
     st(C(50, 50, 28, "N", "S", 5), L(31, 30, 74, 40, 4.5), L(31, 70, 74, 60, 4.5))),
    ("gas_speicher", "Gasspeicher", *GAS,
     st(L(36, 58, 30, 82, 5), L(64, 58, 70, 82, 5), C(50, 42, 25, "S", "N", 0), L(20, 82, 80, 82, 5))),
    ("gas_odorieranlage", "Odorieranlage", *GAS, stt("OD", 32)),
    ("gas_biogaseinspeisung", "Biogaseinspeisung", *GAS,
     st(T("BIO", 50, 34, 22, maxw=62), *arrow(20, 70, 80, 70, 6, 16))),
    ("gas_wasserstoff", "Wasserstoff-Einspeisung / Wasserstoffanlage", *GAS,
     st(T("H", 40, 46, 38), T("2", 70, 64, 22))),
    # ---- Gas: Messstellen und Einrichtungen (Kreis) ----
    ("gas_messstelle", "Gasmessstelle / Gaszähler", *GAS, kr(T("m³", 50, 50, 20, maxw=56))),
    ("gas_kathodenschutz", "Kathodischer Korrosionsschutz (Messstelle, Schutzanlage)", *GAS,
     kr(T("KKS", 50, 50, 20, maxw=60))),
    ("gas_ausblaeser", "Ausbläser", *GAS, kr(*arrow(50, 76, 50, 16, 6, 17), L(32, 76, 68, 76, 5.5))),
    # ---- Gas: Armaturen und Netzelemente (auf der Leitung) ----
    ("gas_absperrarmatur", "Gas-Absperrarmatur / Schieber", *GAS, list(ARMATUR)),
    ("gas_kugelhahn", "Gas-Kugelhahn", *GAS, ARMATUR + [C(50, 50, 11, "S", "N", 0)]),
    ("gas_isolierstueck", "Isolierstück / Isolierflansch", *GAS,
     [ltg(4, 43), ltg(57, 96), L(43, 26, 43, 74, 6, cap="butt"), L(57, 26, 57, 74, 6, cap="butt")]),
    ("gas_molchschleuse", "Molchschleuse", *GAS,
     [ltg(4, 34), R(34, 32, 48, 36, "F", "S", 5, 4), R(46, 42, 22, 16, "S", "N", 0, 8),
      L(88, 24, 88, 76, 7, cap="butt")]),
    ("gas_hausanschluss", "Gas-Hausanschluss", *GAS, list(ANSCHLUSS)),
    ("gas_leitung_nd", "Kennzeichen Niederdruckleitung (ND)", *GAS, kennz("ND")),
    ("gas_leitung_md", "Kennzeichen Mitteldruckleitung (MD)", *GAS, kennz("MD")),
    ("gas_leitung_hd", "Kennzeichen Hochdruckleitung (HD)", *GAS, kennz("HD")),
    # ---- Fernwaerme: Stationen und Anlagen (Quadrat) ----
    ("fw_heizwerk", "Heizwerk / Heizkraftwerk", *FW, st(*fit(flame("S", "F"), 50, 50, 0.78))),
    ("fw_uebergabestation", "Fernwärme-Übergabestation (Wärmetauscher)", *FW,
     st(C(50, 50, 27, "N", "S", 5), PL([(14, 50), (36, 50), (44, 34), (56, 66), (64, 50), (86, 50)], 5))),
    ("fw_pumpstation", "Pumpstation / Druckerhöhung", *FW, st(*PUMPE)),
    ("fw_speicher", "Wärmespeicher", *FW,
     st(R(30, 16, 40, 68, "N", "S", 5, 16), P("M30,50 H70 V68 A16,16 0 0 1 54,84 H46 A16,16 0 0 1 30,68 Z", "S", "N", 0))),
    ("fw_hausstation", "Hausstation / Hausübergabestation", *FW, st(*fit(house("S", "S"), 50, 50, 0.8))),
    # ---- Fernwaerme: Messstellen (Kreis) ----
    ("fw_messstelle", "Messstelle (Temperatur, Druck, Leckwarnung)", *FW,
     kr(L(50, 22, 50, 60, 9), C(50, 68, 12, "S", "N", 0), L(62, 28, 70, 28, 4), L(62, 40, 70, 40, 4))),
    # ---- Fernwaerme: Armaturen und Netzelemente (auf der Leitung) ----
    ("fw_absperrarmatur", "Fernwärme-Absperrarmatur", *FW, list(ARMATUR)),
    ("fw_schacht", "Fernwärmeschacht", *FW,
     [ltg(4, 24), ltg(76, 96), R(24, 24, 52, 52, "F", "S", 5), L(24, 76, 76, 24, 4.5, cap="butt")]),
    ("fw_kompensator", "Kompensator (Axialkompensator)", *FW,
     [ltg(4, 24), ltg(76, 96), L(24, 30, 24, 70, 5), L(76, 30, 76, 70, 5),
      PL([(24, 50), (32, 32), (41, 68), (50, 32), (59, 68), (68, 32), (76, 50)], 4.5)]),
    ("fw_dehnungsbogen", "Dehnungsbogen (U-Bogen)", *FW,
     [PL([(4, 50), (30, 50), (30, 20), (70, 20), (70, 50), (96, 50)], 5, cap="butt")]),
    ("fw_festpunkt", "Festpunkt", *FW, [ltg(), PG([(50, 52), (33, 80), (67, 80)], "S"), L(26, 84, 74, 84, 5)]),
    ("fw_vorlauf", "Kennzeichen Vorlauf (VL)", *FW, kennz("VL")),
    ("fw_ruecklauf", "Kennzeichen Rücklauf (RL)", *FW, kennz("RL")),
    # ---- Telekommunikation: Stationen und Anlagen (Quadrat) ----
    ("tk_vermittlungsstelle", "Vermittlungsstelle / Hauptverteiler (HVt)", *TK, stt("HVt")),
    ("tk_kabelverzweiger", "Kabelverzweiger (KVz)", *TK, stt("KVz")),
    ("tk_multifunktionsgehaeuse", "Multifunktionsgehäuse (MFG)", *TK, stt("MFG", 24)),
    ("tk_glasfaser_pop", "Glasfaser-PoP (Point of Presence)", *TK, stt("PoP")),
    ("tk_netzverteiler", "Glasfaser-Netzverteiler (NVt)", *TK, stt("NVt")),
    # ---- Telekommunikation: Einrichtungen (Kreis) ----
    ("tk_funkmast", "Funkmast / Mobilfunkstandort", *TK,
     kr(PL([(38, 80), (50, 36), (62, 80)], 5), L(43, 62, 57, 62, 4), C(50, 34, 5, "S", "N", 0),
        arc(50, 34, 13, 50, 130, 4.5), arc(50, 34, 13, 230, 310, 4.5),
        arc(50, 34, 23, 52, 128, 4.5), arc(50, 34, 23, 232, 308, 4.5))),
    ("tk_richtfunk", "Richtfunkstation", *TK, kr(*fit(DISH, 51, 49, 0.76))),
    ("tk_wlan", "WLAN-Zugangspunkt", *TK,
     kr(C(50, 72, 6.5, "S", "N", 0), arc(50, 72, 18, -45, 45, 5.5), arc(50, 72, 31, -45, 45, 5.5),
        arc(50, 72, 44, -40, 40, 5.5))),
    # ---- Telekommunikation: Netzelemente (auf der Leitung) ----
    ("tk_muffe", "Muffe", *TK, [ltg(4, 22), ltg(78, 96), R(22, 34, 56, 32, "F", "S", 5, 16)]),
    ("tk_schacht", "Kabelschacht", *TK,
     [ltg(4, 18), ltg(82, 96), R(18, 28, 64, 44, "F", "S", 5), L(18, 28, 82, 72, 4.5, cap="butt"),
      L(18, 72, 82, 28, 4.5, cap="butt")]),
    ("tk_hausanschluss", "Hausanschluss / Abschlusspunkt Linientechnik (APL)", *TK, list(ANSCHLUSS)),
    ("tk_leerrohr", "Leerrohr / Rohrverband (Rohrende)", *TK,
     [ltg(4, 36), C(62, 50, 26, "F", "S", 5), C(62, 50, 9, "W", "S", 4.5)]),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
G0, F0, T0 = GAS[1], FW[1], TK[1]


def schutz(farbe):  # Schutzstreifen
    return [voll(farbe + "1F"), schraffur(farbe, 0.2, 45, 2.5), linie(farbe, 0.3)]


def gelaende(sparte):  # Betriebsgelaende
    return [voll(sparte[0]), linie(sparte[1], 0.5)]


LINIEN = [
    ("Gasleitung Hochdruck (HD)", [linie(G0, 1.1)]),
    ("Gasleitung Mitteldruck (MD)", [linie(G0, 0.7)]),
    ("Gasleitung Niederdruck (ND)", [linie(G0, 0.35)]),
    ("Gasleitung geplant", [linie(G0, 0.7, [3, 1.5])]),
    ("Gasleitung stillgelegt", [linie(G0, 0.4), marken(mk("cross2", 1.6, G0, rw=0.3), 6)]),
    ("Fernwärme Vorlauf", [linie(F0, 0.7)]),
    ("Fernwärme Rücklauf", [linie(F0, 0.7, [5, 1, 0.7, 1])]),
    ("Fernwärme Doppelrohr", [linie(F0, 0.35, versatz=0.45), linie(F0, 0.35, versatz=-0.45)]),
    ("Fernwärmeleitung geplant", [linie(F0, 0.7, [3, 1.5])]),
    ("Glasfaserkabel", [linie(T0, 0.7)]),
    ("Glasfaserkabel geplant", [linie(T0, 0.7, [3, 1.5])]),
    ("Kupferkabel", [linie(T0, 0.3)]),
    ("Leerrohr", [linie(T0, 1.1), linie("#FFFFFF", 0.6)]),
    ("Richtfunkstrecke", [linie(T0, 0.3, [0.8, 1.2]), marken(mk("circle", 1.2, T0), 10)]),
]

FLAECHEN = [
    ("Schutzstreifen Gasleitung", schutz(G0)),
    ("Schutzstreifen Fernwärmeleitung", schutz(F0)),
    ("Schutzstreifen Telekommunikation", schutz(T0)),
    ("Versorgungsgebiet Gas", [band(G0 + "66", 1.5), linie(G0, 0.4)]),
    ("Versorgungsgebiet Fernwärme", [band(F0 + "66", 1.5), linie(F0, 0.4)]),
    ("Versorgungsgebiet Fernwärme geplant", [band(F0 + "40", 1.5), linie(F0, 0.4, [3, 1.5])]),
    ("Ausbaugebiet Glasfaser (Bestand)", [voll(T0 + "40"), linie(T0, 0.4)]),
    ("Ausbaugebiet Glasfaser (geplant)", [schraffur(T0, 0.25, 135, 2.5), linie(T0, 0.4, [3, 1.5])]),
    ("Betriebsgelände Gas", gelaende(GAS)),
    ("Betriebsgelände Fernwärme", gelaende(FW)),
    ("Betriebsgelände Telekommunikation", gelaende(TK)),
]
