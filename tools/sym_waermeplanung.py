"""Sammlung Waermeplanung: Erzeugungsanlagen, Waermequellen und Potenziale, Speicher und Infrastruktur,
Verbraucher und Massnahmen, dezentrale Waermeerzeuger; Netze, Waermeliniendichten, voraussichtliche
Waermeversorgungsgebiete, Eignungsstufen, Waermedichten und Potenzialflaechen fuer die kommunale Waermeplanung.
Quellen (19.11.2026 gelesen):
  Waermeplanungsgesetz (WPG) vom 20.12.2023, gesetze-im-internet.de/wpg: Begriffe nach § 3 (Waermenetzgebiet mit
  Verdichtungs-, Ausbau- und Neubaugebiet, Wasserstoffnetzgebiet, Gebiet fuer die dezentrale Waermeversorgung,
  Pruefgebiet), Eignungsstufen nach § 19, Pflichtdarstellungen nach Anlage 2 (Waermeverbrauchsdichten je Baublock,
  Waermeliniendichten je Strassenabschnitt, Energietraeger, dezentrale Waermeerzeuger, Grossverbraucher, Waerme-,
  Gas- und Abwassernetze, Erzeugungsanlagen, Speicher, Elektrolyseure ueber 1 MW, Potenziale, Ausschlussgebiete).
  Leitfaden Waermeplanung (BMWK/BMWSB, bearbeitet von ifeu, Oeko-Institut u. a., Juni 2024): Tabelle 11
  (Waermedichte, fuenf Klassen), Tabelle 12 (Waermeliniendichte, vier Klassen), Abbildungen 18, 21 und 24
  (Beispielkarten: Waermenetz gruen, Wasserstoffnetz violett, dezentrale Versorgung gelb; Eignung als Abstufung
  derselben Farbe; Waermedichte von hellgelb bis dunkelrot).
Weder Gesetz noch Leitfaden schreiben Zeichen oder Farben vor; die Farben folgen den Beispielkarten des Leitfadens,
die Punktsymbole sind eigene Entwuerfe.
Stil der Punktsymbole: weinrot, Strich 5. Die Form zeigt die Gruppe:
  Quadrat (abgerundet) = Erzeugungsanlage (erz_), Kreis = Waermequelle oder Potenzial (pot_),
  Sechseck = Speicher und Infrastruktur (inf_), Raute = Verbraucher und Massnahme (vb_),
  Hausumriss = dezentraler Waermeerzeuger im Gebaeude (dez_).
Linien und Flaechen: Farbe = Versorgungsart (Waermenetz gruen, Wasserstoff violett, dezentral gelb, Pruefgebiet
grau, Gas graubraun, Abwasser blau); Eignungsstufen als vier Toene derselben Farbe; Waerme- und Waermeliniendichte
von hellgelb bis dunkelrot; durchgezogen = Bestand, lang gestrichelt = genehmigt, kurz gestrichelt = geplant.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "waermeplanung"
NAME = "Wärmeplanung"
DESC = ("Symbole für die kommunale Wärmeplanung nach dem Wärmeplanungsgesetz: Erzeugungsanlagen, Wärmequellen und "
        "Potenziale, Speicher, Großverbraucher, dezentrale Wärmeerzeuger, Netze, Wärmeliniendichten, "
        "Wärmedichten, voraussichtliche Wärmeversorgungsgebiete und Eignungsstufen")
TAGS = ("waermeplanung, waermeplan, kommunale waermeplanung, wpg, waermenetz, fernwaerme, wasserstoff, abwaerme, "
        "waermedichte, waermeliniendichte, waermewende, energie")

WR = ("#F7DDE0", "#9B1B30")


def erz(*sh):  # Erzeugungsanlage
    return fr_square() + list(sh)


def pot(*sh):  # Waermequelle, Potenzial
    return fr_circle() + list(sh)


def inf(*sh):  # Speicher, Infrastruktur
    return fr_hex() + list(sh)


def vb(*sh):  # Verbraucher, Massnahme
    return fr_diamond() + list(sh)


def dez(*sh):  # dezentraler Waermeerzeuger: Hausumriss
    return [PG([(50, 7), (93, 44), (93, 93), (7, 93), (7, 44)], "F", "S", 5)] + list(sh)


def dezt(txt, h=22):
    return dez(T(txt, 50, 66, h, maxw=66))


def dampf(xs, y, h=10, k=2, sw=5):
    """Aufsteigende Waerme: gewellte senkrechte Striche, y = unteres Ende."""
    return [P(f"M{n(x)},{n(y)} q{n(-h * 0.6)},{n(-h / 2)} 0,{n(-h)}" + f" t0,{n(-h)}" * (k - 1), "N", "S", sw)
            for x in xs]


H2 = [T("H", 42, 46, 36), T("2", 70, 64, 20)]
FABRIK = [PG([(18, 80), (18, 52), (34, 62), (34, 52), (50, 62), (50, 52), (66, 62), (66, 26), (80, 26), (80, 80)], "S")]
# Dublette der tiefen Geothermie: Gelaende, Foerder- und Schluckbohrung
DUBLETTE = [L(14, 28, 86, 28, 6), *arrow(36, 88, 36, 40, 6, 15), *arrow(64, 34, 64, 84, 6, 15)]
KOLLEKTOR = [PG([(22, 84), (38, 52), (86, 52), (70, 84)], "N", "S", 5), L(46, 52, 30, 84, 4, cap="butt"),
             L(62, 52, 46, 84, 4, cap="butt"), L(74, 52, 58, 84, 4, cap="butt")]
TAUSCHER = [C(50, 50, 27, "N", "S", 5), PL([(14, 50), (36, 50), (44, 34), (56, 66), (64, 50), (86, 50)], 5)]
TANK = [R(30, 14, 40, 72, "N", "S", 5, 16), P("M30,50 H70 V70 A16,16 0 0 1 54,86 H46 A16,16 0 0 1 30,70 Z", "S", "N", 0)]
KUGEL = [L(36, 58, 30, 84, 5), L(64, 58, 70, 84, 5), C(50, 42, 25, "S", "N", 0), L(18, 84, 82, 84, 5)]
ANKER = [C(50, 20, 8, "N", "S", 5), L(50, 28, 50, 82, 6), L(34, 42, 66, 42, 6),
         P("M22,58 A28,26 0 0 0 78,58", "N", "S", 6)]
BLATT = [P("M24,78 C20,40 46,18 80,22 C84,56 62,82 24,78 Z", "N", "S", 5), L(24, 78, 58, 44, 5)]

S = [
    # ---- Erzeugungsanlagen (Quadrat) ----
    ("erz_heizwerk", "Heizwerk", *WR, erz(*fit(flame("S", "F"), 50, 50, 0.78))),
    ("erz_heizkraftwerk", "Heizkraftwerk (Kraft-Wärme-Kopplung)", *WR, erz(T("KWK", 50, 50, 24, maxw=66))),
    ("erz_biomasse", "Biomasseheizwerk", *WR,
     erz(T("BIO", 50, 28, 19, maxw=60), *fit(flame("S", "F"), 50, 64, 0.5))),
    ("erz_grosswaermepumpe", "Großwärmepumpe", *WR, erz(T("WP", 50, 50, 34, maxw=66))),
    ("erz_solarthermie", "Solarthermieanlage", *WR,
     erz(*sun(32, 30, 8, "S", "F", 4, 8, 4, 5), *fit(KOLLEKTOR, 54, 58, 0.82))),
    ("erz_geothermie", "Geothermieanlage (tiefe Geothermie)", *WR, erz(*fit(DUBLETTE, 50, 50, 0.78))),
    ("erz_power_to_heat", "Power-to-Heat-Anlage (Elektrodenkessel)", *WR, erz(*lightning(50, 50, 1.05))),
    ("erz_abfall", "Thermische Abfallbehandlung (Müllheizkraftwerk)", *WR, erz(T("MHKW", 50, 50, 20, maxw=70))),
    ("erz_elektrolyseur", "Elektrolyseur (Wasserstofferzeugung über 1 MW)", *WR, erz(*H2)),
    # ---- Waermequellen und Potenziale (Kreis) ----
    ("pot_abwaerme_industrie", "Unvermeidbare Abwärme (Industrie, Gewerbe)", *WR,
     pot(*fit(FABRIK, 48, 56, 0.72), *dampf([67], 30, 8, 2, 4.5))),
    ("pot_abwaerme_rechenzentrum", "Abwärme Rechenzentrum", *WR, pot(T("RZ", 50, 50, 30, maxw=60))),
    ("pot_abwasser", "Abwasserwärme (Kanal)", *WR,
     pot(R(18, 56, 64, 22, "N", "S", 5, 11), *dampf([36, 50, 64], 46, 10, 2))),
    ("pot_klaeranlage", "Kläranlage (Wärme aus dem Ablauf)", *WR,
     pot(C(50, 60, 21, "N", "S", 5), L(29, 60, 71, 60, 4.5, cap="butt"), C(50, 60, 5, "S", "N", 0),
         *dampf([38, 50, 62], 30, 7, 2, 4.5))),
    ("pot_gewaesser", "Gewässerwärme (Fluss, See)", *WR,
     pot(wave(22, 62, 56, 5, 2), wave(22, 76, 56, 5, 2), *dampf([36, 50, 64], 48, 10, 2))),
    ("pot_grundwasser", "Grundwasserwärme (Brunnen)", *WR,
     pot(L(18, 36, 82, 36, 5.5), *arrow(50, 66, 50, 16, 5.5, 13), wave(26, 76, 48, 4.5, 2))),
    ("pot_erdwaerme", "Oberflächennahe Geothermie (Erdsonde, Kollektor)", *WR,
     pot(L(18, 32, 82, 32, 5.5), P("M42,32 V70 A8,8 0 0 0 58,70 V32", "N", "S", 5.5))),
    ("pot_tiefengeothermie", "Tiefe Geothermie", *WR, pot(*fit(DUBLETTE, 50, 52, 0.7))),
    ("pot_solarthermie", "Solarthermie", *WR, pot(*sun(50, 50, 13, "S", "F", 5, 8, 6, 10))),
    ("pot_biomasse", "Biomasse", *WR, pot(*fit(BLATT, 50, 50, 0.82))),
    ("pot_umweltluft", "Umgebungsluft (Luft-Wärmepumpe)", *WR,
     pot(C(50, 50, 27, "N", "S", 4.5), *rotor(50, 50, 23))),
    # ---- Speicher und Infrastruktur (Sechseck) ----
    ("inf_waermespeicher", "Wärmespeicher", *WR, inf(*fit(TANK, 50, 50, 0.74))),
    ("inf_erdbeckenspeicher", "Saisonaler Wärmespeicher (Erdbecken, Aquifer)", *WR,
     inf(L(18, 38, 82, 38, 5.5), PG([(28, 38), (72, 38), (62, 70), (38, 70)], "S", "S", 4))),
    ("inf_gasspeicher", "Gasspeicher", *WR, inf(*fit(KUGEL, 50, 50, 0.74))),
    ("inf_wasserstoffspeicher", "Wasserstoffspeicher", *WR,
     inf(C(50, 50, 28, "N", "S", 5), T("H", 45, 48, 24), T("2", 63, 60, 14))),
    ("inf_uebergabe", "Wärmeübergabestation (Netzkopplung)", *WR, inf(*fit(TAUSCHER, 50, 50, 0.9))),
    ("inf_umspannwerk", "Umspannwerk (Netzanschlusskapazität Strom)", *WR,
     inf(C(40, 50, 17, "N", "S", 5), C(60, 50, 17, "N", "S", 5))),
    ("inf_einspeisung", "Einspeisepunkt in das Wärmenetz", *WR,
     inf(L(20, 70, 80, 70, 6, cap="butt"), *arrow(50, 20, 50, 62, 6, 15))),
    # ---- Verbraucher und Massnahmen (Raute) ----
    ("vb_grossverbraucher", "Großverbraucher", *WR, vb(*fit(FABRIK, 50, 50, 0.56))),
    ("vb_ankerkunde", "Ankerkunde", *WR, vb(*fit(ANKER, 50, 50, 0.6))),
    ("vb_oeffentlich", "Öffentliche Liegenschaft", *WR, vb(*fit(house("S", "S"), 50, 50, 0.56))),
    ("vb_prozesswaerme", "Prozesswärme", *WR, vb(*gear(50, 50, 21, 8, "S", 7))),
    ("vb_einsparung", "Sanierungsschwerpunkt (Energieeinsparung)", *WR,
     vb(L(32, 30, 68, 30, 6), *arrow(50, 30, 50, 74, 6, 15))),
    ("vb_massnahme", "Maßnahme der Umsetzungsstrategie", *WR, vb(T("M", 50, 50, 30))),
    ("vb_fokusgebiet", "Fokusgebiet", *WR, vb(T("F", 50, 50, 30))),
    # ---- Dezentrale Waermeerzeuger (Hausumriss) ----
    ("dez_gas", "Gasheizung", *WR, dezt("Gas")),
    ("dez_oel", "Ölheizung", *WR, dezt("Öl", 24)),
    ("dez_biomasse", "Biomasseheizung (Pellets, Holz)", *WR, dezt("Bio")),
    ("dez_waermepumpe", "Wärmepumpe", *WR, dezt("WP", 26)),
    ("dez_strom", "Stromdirektheizung (Nachtspeicher)", *WR, dez(*lightning(50, 64, 0.8))),
    ("dez_waermenetz", "Hausübergabestation (Wärmenetzanschluss)", *WR, dezt("WN", 26)),
    ("dez_solarthermie", "Solarthermie auf dem Dach", *WR, dez(*sun(50, 64, 9, "S", "F", 4.5, 8, 5, 7))),
    ("dez_hybrid", "Hybridheizung", *WR, dezt("Hyb")),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
W0 = WR[1]
NETZ, NETZ_D = "#2E9B3E", "#1E6B2A"     # Waermenetz
WST, WST_D = "#A23BB5", "#6F2380"       # Wasserstoff
DEZ, DEZ_D = "#E8A917", "#8A6200"       # dezentrale Versorgung
GRAU, GRAU_D = "#9A9A9A", "#555555"     # Pruefgebiet, Hilfslinien
GAS = "#7A6A58"
ABW = "#2F7FC1"
# Waermedichte nach Tabelle 11 des Leitfadens (fuenf Klassen) und Waermeliniendichte nach Tabelle 12 (vier Klassen)
DICHTE = ["#FFF6DC", "#FBDF9A", "#F6A54A", "#D7191C", "#6B0F12"]
LDICHTE = ["#F0CF8A", "#F6A54A", "#D7191C", "#6B0F12"]
STUFEN = [("sehr wahrscheinlich geeignet", 1.0), ("wahrscheinlich geeignet", 0.62),
          ("wahrscheinlich ungeeignet", 0.34), ("sehr wahrscheinlich ungeeignet", 0.12)]


def ton(farbe, a):
    """Farbe mit Weiss gemischt: a = 1 volle Farbe, a = 0 Weiss."""
    return "#" + "".join(f"{round(255 - (255 - int(farbe[i:i + 2], 16)) * a):02X}" for i in (1, 3, 5))


def gebiet(farbe, rand, a=0.55):
    return [voll(ton(farbe, a)), linie(rand, 0.4)]


def eignung(art, farbe, rand):
    return [(f"Eignung {art}, {name}", [voll(ton(farbe, a)), linie(rand, 0.25)]) for name, a in STUFEN]


def traeger(farbe):
    return [voll(farbe), linie("#FFFFFF", 0.25)]


LINIEN = [
    ("Wärmeliniendichte unter 700 kWh/(m·a)", [linie(LDICHTE[0], 0.6)]),
    ("Wärmeliniendichte 700 bis 1500 kWh/(m·a)", [linie(LDICHTE[1], 0.9)]),
    ("Wärmeliniendichte 1500 bis 2000 kWh/(m·a)", [linie(LDICHTE[2], 1.2)]),
    ("Wärmeliniendichte über 2000 kWh/(m·a)", [linie(LDICHTE[3], 1.6)]),
    ("Wärmenetz (Wasser), Bestand", [linie(NETZ_D, 0.8)]),
    ("Wärmenetz (Dampf), Bestand", [linie(NETZ_D, 0.8), marken(mk("circle", 1.5, "#FFFFFF", NETZ_D, 0.3), 6)]),
    ("Wärmenetz genehmigt", [linie(NETZ_D, 0.8, [5, 1.2])]),
    ("Wärmenetz geplant", [linie(NETZ_D, 0.8, [2.5, 1.5])]),
    ("Gasnetz (Methan), Bestand", [linie(GAS, 0.7)]),
    ("Gasnetz (Methan), Stilllegung vorgesehen", [linie(GAS, 0.5), marken(mk("cross2", 1.6, GAS, rw=0.3), 6)]),
    ("Wasserstoffnetz, Bestand", [linie(WST_D, 0.8)]),
    ("Wasserstoffnetz, geplant", [linie(WST_D, 0.8, [2.5, 1.5])]),
    ("Abwassersammler (ab DN 800)", [linie(ABW, 0.9)]),
    ("Grenze des beplanten Gebiets", [linie("#222222", 0.9, [6, 1.5, 1, 1.5])]),
    ("Grenze eines beplanten Teilgebiets", [linie(GRAU_D, 0.5, [3, 1.5])]),
    ("Baublockgrenze", [linie(GRAU, 0.25)]),
]

FLAECHEN = [
    # voraussichtliche Waermeversorgungsgebiete (§ 3, § 18 WPG)
    ("Wärmenetzgebiet", gebiet(NETZ, NETZ_D)),
    ("Wärmenetzverdichtungsgebiet", gebiet(NETZ, NETZ_D, 0.85)),
    ("Wärmenetzausbaugebiet", [voll(ton(NETZ, 0.4)), schraffur(NETZ_D, 0.3, 45, 2.5), linie(NETZ_D, 0.4)]),
    ("Wärmenetzneubaugebiet", [voll(ton(NETZ, 0.2)), schraffur(NETZ_D, 0.3, 45, 2.5), schraffur(NETZ_D, 0.3, 135, 2.5),
                               linie(NETZ_D, 0.4)]),
    ("Wasserstoffnetzgebiet", gebiet(WST, WST_D)),
    ("Gebiet für die dezentrale Wärmeversorgung", gebiet(DEZ, DEZ_D)),
    ("Prüfgebiet", [voll(ton(GRAU, 0.35)), schraffur(GRAU_D, 0.25, 45, 3), linie(GRAU_D, 0.4, [3, 1.5])]),
    # Eignungsstufen fuer das Zieljahr (§ 19 WPG), je Versorgungsart eine Farbe
    *eignung("Wärmenetz", NETZ, NETZ_D),
    *eignung("Wasserstoffnetz", WST, WST_D),
    *eignung("dezentrale Versorgung", DEZ, DEZ_D),
    # Bestandsanalyse (Anlage 2 WPG)
    ("Wärmedichte unter 70 MWh/(ha·a)", [voll(DICHTE[0]), linie(GRAU, 0.2)]),
    ("Wärmedichte 70 bis 175 MWh/(ha·a)", [voll(DICHTE[1]), linie(GRAU, 0.2)]),
    ("Wärmedichte 175 bis 415 MWh/(ha·a)", [voll(DICHTE[2]), linie(GRAU, 0.2)]),
    ("Wärmedichte 415 bis 1050 MWh/(ha·a)", [voll(DICHTE[3]), linie(GRAU, 0.2)]),
    ("Wärmedichte über 1050 MWh/(ha·a)", [voll(DICHTE[4]), linie(GRAU, 0.2)]),
    ("Überwiegender Energieträger Heizöl", traeger("#3A3A3A")),
    ("Überwiegender Energieträger Erdgas", traeger("#8A7B6A")),
    ("Überwiegender Energieträger Wärmenetz", traeger(NETZ)),
    ("Überwiegender Energieträger Biomasse", traeger("#9A5B13")),
    ("Überwiegender Energieträger Strom", traeger("#F2C200")),
    ("Überwiegender Energieträger Sonstige", traeger("#2F8FC1")),
    ("Vom Gasnetz versorgtes Gebiet (Bestand)", [voll(GAS + "99"), linie(GAS, 0.4)]),
    ("Vom Wärmenetz versorgtes Gebiet (Bestand)", [band(NETZ + "80", 1.5), linie(NETZ_D, 0.5)]),
    # Eignungspruefung, Einteilung und Ausweisung
    ("Teilgebiet mit verkürzter Wärmeplanung (§ 14)", [schraffur(GRAU_D, 0.25, 135, 3), linie(GRAU_D, 0.4)]),
    ("Gebiet mit erhöhtem Energieeinsparpotenzial", [schraffur(W0, 0.3, 45, 2.5), linie(W0, 0.5, [3, 1.5])]),
    ("Gebiet mit Anschluss- und Benutzungszwang", [band(NETZ_D + "66", 1.5), linie(NETZ_D, 0.5),
                                                   marken(mk("triangle", 1.6, NETZ_D, dy=1.0), 8, ecken=1.5)]),
    ("Gebiet zum Neu- oder Ausbau von Wärmenetzen (§ 26)", [band(NETZ + "99", 2), linie(NETZ_D, 0.8)]),
    ("Wasserstoffnetzausbaugebiet (§ 26)", [band(WST + "99", 2), linie(WST_D, 0.8)]),
    # Potenzialanalyse
    ("Potenzialfläche Solarthermie", [voll("#FFE84D" + "B3"), linie(DEZ_D, 0.4)]),
    ("Potenzialfläche oberflächennahe Geothermie", [voll("#C9A27A" + "66"), schraffur("#7A4A1E", 0.25, 0, 2.5),
                                                    linie("#7A4A1E", 0.4)]),
    ("Potenzial Abwasserwärme (Kanal)", [voll(ABW + "59"), linie(ABW, 0.3)]),
    ("Potenzial Gewässerwärme", [voll(ABW + "33"), schraffur(ABW, 0.25, 0, 2), linie(ABW, 0.4)]),
    ("Potenzial unvermeidbare Abwärme", [voll("#B5121B" + "CC"), linie("#6B0F12", 0.4)]),
    ("Potenzialfläche Biomasse", [voll(ton(NETZ, 0.2)), schraffur(NETZ_D, 0.25, 90, 2.5), linie(NETZ_D, 0.4)]),
    ("Potenzialfläche Großwärmespeicher", [voll(WR[0] + "B3"), linie(W0, 0.5, [3, 1.5])]),
    ("Ausschlussgebiet (Potenzialanalyse)", [schraffur(GRAU_D, 0.2, 45, 2), schraffur(GRAU_D, 0.2, 135, 2),
                                             linie(GRAU_D, 0.5)]),
]
