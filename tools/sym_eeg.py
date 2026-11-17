"""Sammlung Erneuerbare Energien: Anlagen und Planungselemente fuer Wind- und Solarparks, Bioenergie,
Wasserkraft, Geothermie, Speicher und Netzanschluss.
Orientierung: Energieatlanten der Laender (Kreis mit Piktogramm, Farbe je Energietraeger). Kein
bundeseinheitliches Regelwerk; eigene Entwuerfe.
Stil: immer Kreisrahmen (r = 44, Strich 5) mit heller Fuellung und dunklem Piktogramm. Die Farbe zeigt den
Energietraeger (blau Wind, gelb Solar, gruen Bioenergie, tuerkis Wasser, rotbraun Waerme, grau Netz/Planung),
der Rahmen den Status (durchgezogen Bestand, gestrichelt geplant, gepunktet beantragt, doppelt genehmigt).
Linien und Flaechen: Farbe = Energietraeger wie bei den Punktsymbolen, durchgezogen = Bestand,
gestrichelt = geplant; Vorrang- und Potenzialflaechen schraffiert.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "eeg"
NAME = "Erneuerbare Energien"
DESC = ("Symbole für die Planung von Wind- und Solarparks und weitere Anlagen erneuerbarer Energien: "
        "Windenergieanlagen nach Status, Photovoltaik, Bioenergie, Wasserkraft, Geothermie, Speicher, "
        "Netzanschluss, Immissionsorte und Planungselemente")
TAGS = "eeg, windenergie, photovoltaik, biogas, erneuerbare energien, windpark, solarpark, energieatlas"

WIND = ("#E3F2FD", "#0D47A1")
SUN = ("#FFF3C4", "#B45309")
BIO = ("#E2F3D5", "#2E7D32")
H2O = ("#D4F1F4", "#00707F")
GEO = ("#FBE3D6", "#9A3412")
NEU = ("#ECEFF1", "#37474F")


def kr(*sh, dash=None):
    return fr_circle(dash=dash) + list(sh)


def krt(txt, h=24, mw=60):
    return kr(T(txt, 50, 50, h, maxw=mw))


def pv(cx=50, cy=50, k=1.0):
    return fit([PG([(32, 32), (84, 32), (68, 68), (16, 68)], "F", "S", 4.5), L(24, 50, 76, 50, 3.5),
                L(49.3, 32, 33.3, 68, 3.5), L(66.7, 32, 50.7, 68, 3.5)], cx, cy, k)


def tuft(x, y, k=1.0):
    return [L(x, y, x, y - 13 * k, 3.5), L(x, y, x - 7 * k, y - 9 * k, 3.5), L(x, y, x + 7 * k, y - 9 * k, 3.5)]


def rhead(a):  # Pfeilspitze auf dem Rahmenkreis, im Uhrzeigersinn
    return PG([pt(50, 50, 44, a + 16), pt(50, 50, 33, a), pt(50, 50, 55, a)], "S")


ROT = rotor(50, 50, 35)

S = [
    # ---- Windenergie ----
    ("wea_bestand", "Windenergieanlage, Bestand", *WIND, kr(*ROT)),
    ("wea_geplant", "Windenergieanlage, geplant", *WIND, kr(*ROT, dash="10 8")),
    ("wea_beantragt", "Windenergieanlage, beantragt", *WIND, kr(*ROT, dash="0.1 9")),
    ("wea_genehmigt", "Windenergieanlage, genehmigt", *WIND,
     [C(50, 50, 45, "F", "S", 3.5), C(50, 50, 37, "N", "S", 3.5)] + rotor(50, 50, 30)),
    ("wea_im_bau", "Windenergieanlage, im Bau", *WIND,
     [C(50, 50, 44, "F", "N", 0), chord(50, 50, 44, 128, 232), C(50, 50, 44, "N", "S", 5)] + rotor(50, 46, 32)),
    ("wea_rueckbau", "Windenergieanlage, Rückbau", *WIND,
     kr(*ROT, L(19, 19, 81, 81, 5, cap="butt"), L(19, 81, 81, 19, 5, cap="butt"))),
    ("wea_repowering", "Windenergieanlage, Repowering", *WIND,
     [C(50, 50, 44, "F", "N", 0), arc(50, 50, 44, 20, 150, 5, cap="butt"), arc(50, 50, 44, 200, 330, 5, cap="butt"),
      rhead(150), rhead(330)] + rotor(50, 50, 30)),
    ("kleinwindanlage", "Kleinwindanlage", *WIND, kr(L(50, 42, 50, 84, 5), *rotor(50, 42, 27))),
    ("windmessmast", "Windmessmast", *WIND,
     kr(L(50, 24, 50, 82, 5), L(50, 40, 30, 80, 3), L(50, 40, 70, 80, 3), L(36, 24, 64, 24, 4),
        C(34, 24, 5.5, "F", "S", 3.5), C(66, 24, 5.5, "F", "S", 3.5))),
    ("rotorkreis", "Rotorkreis / Rotorradius", *WIND, [C(50, 50, 44, "N", "S", 3.5, "7 6"), C(50, 50, 6, "S", "N", 0)]),
    ("kranstellflaeche", "Kranstellfläche", *WIND, kr(R(24, 32, 52, 36, "N", "S", 4.5), T("K", 50, 50, 20))),
    # ---- Solarenergie ----
    ("pv_freiflaeche", "Photovoltaik-Freiflächenanlage, Bestand", *SUN, kr(*pv())),
    ("pv_freiflaeche_geplant", "Photovoltaik-Freiflächenanlage, geplant", *SUN, kr(*pv(), dash="10 8")),
    ("pv_dach", "Photovoltaik-Dachanlage", *SUN,
     kr(*fit(house(), 50, 54, 0.72), PG([(56, 34), (72, 49), (67, 54), (51, 39)], "S"))),
    ("agri_pv", "Agri-Photovoltaik", *SUN, kr(*pv(50, 38, 0.66), *tuft(30, 78), *tuft(50, 80), *tuft(70, 78))),
    ("floating_pv", "Schwimmende Photovoltaik (Floating-PV)", *SUN, kr(*pv(50, 40, 0.7), wave(22, 74, 56, 5, 2, 4.5))),
    ("solarthermie", "Solarthermie", *SUN, kr(*sun(50, 40, 9, sw=4, gap=5, ln=6), wave(24, 76, 52, 5, 2, 4.5))),
    # ---- Bioenergie ----
    ("biogasanlage", "Biogasanlage", *BIO,
     kr(P("M24,66 A26,26 0 0 1 76,66 Z", "N", "S", 5), L(18, 66, 82, 66, 5), *fit(flame("S", "F"), 50, 53, 0.24))),
    ("biomasse", "Biomasseanlage", *BIO,
     kr(P("M28,74 C26,46 44,28 74,26 C74,56 56,74 28,74 Z", "N", "S", 5), L(28, 74, 60, 42, 4.5))),
    ("biomethan", "Biomethan-Einspeisung", *BIO, kr(T("CH", 43, 48, 24), T("4", 70, 60, 14))),
    ("holzenergie", "Holzheizwerk / Holzhackschnitzel", *BIO,
     kr(*[C(x, y, 12, "N", "S", 4.5) for x, y in ((37, 62), (63, 62), (50, 39))],
        *[C(x, y, 3.5, "S", "N", 0) for x, y in ((37, 62), (63, 62), (50, 39))])),
    # ---- Wasserkraft ----
    ("wasserkraft", "Wasserkraftanlage", *H2O, kr(*lightning(50, 36, 0.62), wave(22, 64, 56, 6, 2, 5), wave(28, 77, 44, 5, 2, 5))),
    ("pumpspeicher", "Pumpspeicherkraftwerk", *H2O,
     kr(PL([(20, 30), (24, 42), (44, 42), (48, 30)], 4.5), PL([(52, 60), (56, 72), (76, 72), (80, 60)], 4.5),
        *arrow(40, 50, 58, 62, 4, 9), *arrow(58, 62, 40, 50, 4, 9))),
    # ---- Waerme und Geothermie ----
    ("geothermie", "Geothermieanlage", *GEO, kr(L(24, 34, 76, 34, 5), *arrow(40, 42, 40, 80, 5, 11), *arrow(60, 80, 60, 42, 5, 11))),
    ("erdwaermesonde", "Erdwärmesonde", *GEO, kr(L(22, 30, 78, 30, 5), P("M41,30 V70 A9,9 0 0 0 59,70 V30", "N", "S", 5))),
    ("waermepumpe", "Wärmepumpe", *GEO, krt("WP", 28)),
    ("heizwerk", "Heizwerk / Wärmeerzeugung", *GEO, kr(*fit(flame("S", "F"), 50, 50, 0.64))),
    ("waermespeicher", "Wärmespeicher", *GEO,
     kr(R(33, 20, 34, 60, "N", "S", 5, 12), wave(39, 42, 22, 3.5, 1, 4), wave(39, 58, 22, 3.5, 1, 4))),
    ("kwk_anlage", "KWK-Anlage / Blockheizkraftwerk", *GEO, krt("KWK", 20, 62)),
    # ---- Wasserstoff, Speicher, Netzanschluss ----
    ("wasserstoff", "Wasserstoff / Elektrolyseur", *H2O, kr(T("H", 42, 50, 30), T("2", 66, 62, 16))),
    ("speicher", "Stromspeicher / Batteriespeicher", *NEU,
     kr(R(22, 34, 50, 32, "N", "S", 4.5, 4), R(72, 43, 7, 14, "S", "N", 0, 1.5), *lightning(47, 50, 0.42))),
    ("umspannwerk", "Umspannwerk", *NEU, kr(C(40, 50, 16, "N", "S", 4.5), C(60, 50, 16, "N", "S", 4.5))),
    ("uebergabestation", "Übergabestation", *NEU, krt("ÜS", 28)),
    ("netzverknuepfungspunkt", "Netzverknüpfungspunkt", *NEU, krt("NVP", 20, 62)),
    ("einspeisepunkt", "Einspeisepunkt", *NEU, kr(L(26, 72, 74, 72, 6), *arrow(50, 22, 50, 64, 6, 14))),
    # ---- Planung und Immissionen ----
    ("vorranggebiet", "Vorrang- oder Eignungsgebiet", *NEU, krt("VRG", 20, 62)),
    ("ausschlussflaeche", "Ausschlussfläche / Tabuzone", *NEU, kr(*rotor(50, 50, 30), L(19, 81, 81, 19, 6, cap="butt"))),
    ("immissionsort_schall", "Immissionsort Schall", *NEU,
     kr(*fit(house(), 36, 54, 0.46), arc(40, 54, 26, 55, 125, 4.5), arc(40, 54, 38, 60, 120, 4.5))),
    ("immissionsort_schatten", "Immissionsort Schattenwurf", *NEU,
     kr(PG([(46, 70), (78, 70), (68, 56), (46, 56)], "S"), *fit(house(), 36, 54, 0.46),
        *sun(68, 30, 6, sw=3.5, gap=4, ln=5))),
    ("hindernisbefeuerung", "Hindernisbefeuerung", *NEU,
     kr(L(50, 56, 50, 82, 5), C(50, 48, 10, "S", "N", 0),
        *[L(*pt(50, 48, 17, a), *pt(50, 48, 27, a), 4.5) for a in (-90, -45, 0, 45, 90)])),
    ("flugsicherung_radar", "Flugsicherung / Radaranlage", *NEU,
     kr(PG([(50, 58), (62, 82), (38, 82)], "S"), P("M28,46 Q50,70 72,46 Z", "S", "N", 0),
        arc(50, 48, 14, -40, 40, 4), arc(50, 48, 25, -40, 40, 4))),
    ("eiswurf", "Eiswurf / Eisfall", *NEU,
     kr(*[L(*pt(50, 50, 30, a), *pt(50, 50, 30, a + 180), 4.5) for a in (0, 60, 120)],
        *[L(*pt(50, 50, 20, a), *pt(50, 50, 28, a + d), 3.5) for a in range(0, 360, 60) for d in (-22, 22)])),
    ("visualisierungspunkt", "Visualisierungspunkt / Sichtbarkeitsanalyse", *NEU,
     kr(P("M18,50 Q50,20 82,50 Q50,80 18,50 Z", "N", "S", 5), C(50, 50, 11, "S", "N", 0))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
WD, SD, BD, GD, ND = WIND[1], SUN[1], BIO[1], GEO[1], NEU[1]

LINIEN = [
    ("Kabeltrasse Netzanschluss", [linie(ND, 0.6)]),
    ("Kabeltrasse Netzanschluss, geplant", [linie(ND, 0.6, [4, 1.5])]),
    ("Parkverkabelung", [linie(ND, 0.3)]),
    ("Zuwegung", [linie(ND, 1.3), linie(NEU[0], 0.8)]),
    ("Zuwegung, geplant", [linie(ND, 1.3, [3, 1.5]), linie(NEU[0], 0.8)]),
    ("Zaun Solarpark", [linie(SD, 0.3), marken(mk("cross2", 1.2, SD, rw=0.25), 4)]),
    ("Abstandslinie", [linie(WD, 0.4, [5, 1.5, 0.5, 1.5])]),
    ("Rotorüberstrich", [linie(WD, 0.3, [1, 1])]),
    ("Wärmeleitung", [linie(GD, 0.5)]),
    ("Biogasleitung", [linie(BD, 0.5, [4, 1, 0.5, 1])]),
]

FLAECHEN = [
    ("Windvorranggebiet", [voll(WIND[0] + "B3"), schraffur(WD, 0.25, 45, 3), linie(WD, 0.5)]),
    ("Potenzialfläche Wind", [voll(WIND[0] + "B3"), linie(WD, 0.5, [4, 1.5])]),
    ("Windpark", [voll(WIND[0]), linie(WD, 0.5)]),
    ("Solarpark", [voll(SUN[0]), linie(SD, 0.5)]),
    ("Solarpark, geplant", [voll(SUN[0] + "B3"), linie(SD, 0.5, [4, 1.5])]),
    ("Modulfläche", [voll(SUN[0]), schraffur(SD, 0.2, 0, 1.2), linie(SD, 0.3)]),
    ("Potenzialfläche Solar", [voll(SUN[0] + "B3"), schraffur(SD, 0.25, 45, 3), linie(SD, 0.5, [4, 1.5])]),
    ("Agri-PV-Fläche", [voll(BIO[0]), schraffur(SD, 0.5, 0, 2.5), linie(SD, 0.4)]),
    ("Bioenergie, Betriebsfläche", [voll(BIO[0]), linie(BD, 0.5)]),
    ("Kranstellfläche, Baufläche", [voll(NEU[0]), linie(ND, 0.4)]),
    ("Ausschlussfläche", [schraffur(ND, 0.25, 45, 2.5), schraffur(ND, 0.25, 135, 2.5), linie(ND, 0.5)]),
    ("Abstandszone", [band(ND + "40", 1.5), linie(ND, 0.4, [3, 1.5])]),
    ("Schattenwurfbereich", [voll(ND + "33"), linie(ND, 0.3, [1, 1])]),
    ("Ausgleichsfläche", [schraffur(BD, 0.25, 135, 3), linie(BD, 0.5, [3, 1.5])]),
]
