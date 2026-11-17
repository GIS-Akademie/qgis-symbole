from lib import *

BW = ("#FFFFFF", "#000000")
CAT = {}

# =============================== PlanZV ===============================
S = []


def gb(*shapes):  # Gemeinbedarf: schwarzes Rechteck, weisse Form
    return [R(4, 24, 92, 52, "S", "N", 0)] + list(shapes)


def gr(*shapes):  # Gruenflaeche: umrandetes Rechteck
    return [R(6, 24, 88, 52, "F", "S", 5)] + list(shapes)


def ve(*shapes, disc="F"):  # Ver- und Entsorgung: Kreis
    return [C(50, 50, 42, disc, "N", 0)] + list(shapes) + [C(50, 50, 42, "N", "S", 5)]


def sg(txt):  # Schutzgebiet: Kreis mit Kuerzel
    return [C(50, 50, 43, "F", "S", 6), T(txt, 50, 50, 30, "S", maxw=58)]


def bwt(txt):  # Bauweise: Dreieck mit Buchstaben
    return [PG([(50, 8), (94, 88), (6, 88)], "F", "S", 5), T(txt, 50, 64, 24, "S", maxw=44)]


S += [
    ("gb_oeffentliche_verwaltung", "Gemeinbedarf: Öffentliche Verwaltungen", *BW, gb(C(50, 50, 17, "F", "N", 0))),
    ("gb_schule", "Gemeinbedarf: Schule", *BW, gb(PG([(50, 31), (71, 68), (29, 68)], "F"))),
    ("gb_kirche", "Gemeinbedarf: Kirchen und kirchlichen Zwecken dienende Einrichtungen", *BW,
     gb(R(44, 29, 12, 42, "F", "N", 0), R(29, 44, 42, 12, "F", "N", 0), C(50, 50, 13, "F", "N", 0))),
    ("gb_sozial", "Gemeinbedarf: Sozialen Zwecken dienende Einrichtungen", *BW,
     gb(PG([(24, 50), (37, 33), (63, 33), (76, 50), (63, 67), (37, 67)], "F"))),
    ("gb_gesundheit", "Gemeinbedarf: Gesundheitlichen Zwecken dienende Einrichtungen", *BW,
     gb(R(43, 30, 14, 40, "F", "N", 0), R(30, 43, 40, 14, "F", "N", 0))),
    ("gb_kultur", "Gemeinbedarf: Kulturellen Zwecken dienende Einrichtungen", *BW,
     gb(PG([(29, 32), (71, 32), (50, 69)], "F"))),
    ("gb_sport", "Gemeinbedarf: Sportlichen Zwecken dienende Einrichtungen", *BW,
     gb(R(22, 38, 56, 24, "F", "N", 0, rx=12))),
    ("gb_post", "Gemeinbedarf: Post", *BW,
     gb(C(45, 55, 9, "N", "F", 5), P("M18,43 H36 Q44,43 50,47", "N", "F", 5),
        P("M53,49 Q68,46 82,33 V69 Q68,60 54,61 Z", "F", "N", 0))),
    ("gb_feuerwehr", "Gemeinbedarf: Feuerwehr", *BW, gb(T("F", 50, 50, 32, "F"))),
    # Gruenflaechen
    ("gr_parkanlage", "Grünfläche: Parkanlage", *BW,
     gr(C(30, 61, 4.5, "S", "N", 0), C(50, 39, 4.5, "S", "N", 0), C(70, 61, 4.5, "S", "N", 0))),
    ("gr_dauerkleingaerten", "Grünfläche: Dauerkleingärten", *BW,
     gr(L(35.3, 24, 35.3, 76, 3.5), L(64.7, 24, 64.7, 76, 3.5), L(6, 50, 94, 50, 3.5),
        *[C(x, y, 3.2, "S", "N", 0) for x in (20.7, 50, 79.3) for y in (37, 63)])),
    ("gr_sportplatz", "Grünfläche: Sportplatz", *BW, gr(R(22, 37, 56, 26, "N", "S", 4, rx=13))),
    ("gr_spielplatz", "Grünfläche: Spielplatz", *BW,
     gr(PL([(35, 42), (65, 42), (60, 68), (40, 68)], 4, close=True),
        P("M37,42 A13,12 0 0 1 63,42", "N", "S", 3.5))),
    ("gr_zeltplatz", "Grünfläche: Zeltplatz", *BW,
     gr(PL([(50, 36), (69, 68), (31, 68)], 4, close=True), L(50, 36, 46, 29, 3.5), L(50, 36, 54, 29, 3.5))),
    ("gr_badeplatz", "Grünfläche: Badeplatz, Freibad", *BW,
     gr(*[wave(20, 36 + i * 9.3, 60, 4.5, 3, 3.5) for i in range(4)])),
    ("gr_friedhof", "Grünfläche: Friedhof", *BW,
     gr(*cross(30, 61, 6.5, 4), *cross(50, 39, 6.5, 4), *cross(70, 61, 6.5, 4))),
    # Ver- und Entsorgung
    ("ve_elektrizitaet", "Ver-/Entsorgung: Elektrizität", *BW,
     ve(P("M50,8 A42,42 0 0 0 50,92 L41,55 L59,49 Z", "S", "N", 0))),
    ("ve_gas", "Ver-/Entsorgung: Gas", *BW,
     ve(P("M15.53,26 A42,42 0 0 1 84.47,26 Z", "S", "N", 0), P("M15.53,74 A42,42 0 0 0 84.47,74 Z", "S", "N", 0))),
    ("ve_fernwaerme", "Ver-/Entsorgung: Fernwärme", *BW,
     ve(P("M26,15.53 A42,42 0 0 0 26,84.47 Z", "S", "N", 0), P("M74,15.53 A42,42 0 0 1 74,84.47 Z", "S", "N", 0))),
    ("ve_wasser", "Ver-/Entsorgung: Wasser", *BW,
     ve(P("M8.77,58 C24,44 38,46 50,58 S76,72 91.23,58 A42,42 0 0 1 8.77,58 Z", "S", "N", 0))),
    ("ve_abwasser", "Ver-/Entsorgung: Abwasser", *BW,
     ve(P("M17.02,24 L82.98,24 A42,42 0 0 1 88.83,34 L11.17,34 A42,42 0 0 1 17.02,24 Z", "S", "N", 0))),
    ("ve_abfall", "Ver-/Entsorgung: Abfall", *BW,
     ve(PG([(50, 24), (74, 66), (26, 66)], "F"), disc="S")),
    ("ve_ablagerung", "Ver-/Entsorgung: Ablagerung", *BW,
     ve(PG([(50, 22), (78, 50), (50, 78), (22, 50)], "F"), disc="S")),
    # Verkehr
    ("vk_flugplatz", "Verkehr: Flugplatz", *BW, [C(50, 50, 44, "F", "S", 4)] + plane(50, 50, 1.05)),
    ("vk_hubschrauberlandeplatz", "Verkehr: Hubschrauberlandeplatz", *BW,
     [C(50, 50, 44, "F", "S", 4)] + [L(50, 50, *rot([(0, -33)], a, 50, 50)[0], 6.5, cap="butt") for a in (0, 120, 240)]
     + [C(50, 50, 6, "F", "S", 3.5)]),
    ("vk_parkflaeche", "Verkehr: Öffentliche Parkfläche", *BW, [R(10, 10, 80, 80, "F", "S", 5), T("P", 50, 50, 46)]),
    # Schutzgebiete nach Naturschutzrecht
    ("sg_naturschutzgebiet", "Schutzgebiet: Naturschutzgebiet", *BW, sg("N")),
    ("sg_landschaftsschutzgebiet", "Schutzgebiet: Landschaftsschutzgebiet", *BW, sg("L")),
    ("sg_naturpark", "Schutzgebiet: Naturpark", *BW, sg("NP")),
    ("sg_nationalpark", "Schutzgebiet: Nationalpark", *BW, sg("NLP")),
    ("sg_naturdenkmal", "Schutzgebiet: Naturdenkmal", *BW, sg("ND")),
    ("sg_geschuetzter_landschaftsbestandteil", "Schutzgebiet: Geschützter Landschaftsbestandteil", *BW, sg("LB")),
    # Nebenanlagen
    ("na_stellplaetze", "Nebenanlagen: Stellplätze", *BW, [T("St", 50, 50, 50, maxw=90)]),
    ("na_garagen", "Nebenanlagen: Garagen", *BW, [T("Ga", 50, 50, 46, maxw=90)]),
    ("na_gemeinschaftsstellplaetze", "Nebenanlagen: Gemeinschaftsstellplätze", *BW, [T("GSt", 50, 50, 44, maxw=92)]),
    ("na_gemeinschaftsgaragen", "Nebenanlagen: Gemeinschaftsgaragen", *BW, [T("GGa", 50, 50, 40, maxw=92)]),
    # Bauweise
    ("bw_offen", "Bauweise: offene Bauweise", *BW, [T("o", 50, 50, 60)]),
    ("bw_geschlossen", "Bauweise: geschlossene Bauweise", *BW, [T("g", 50, 50, 52)]),
    ("bw_einzelhaeuser", "Bauweise: nur Einzelhäuser zulässig", *BW, bwt("E")),
    ("bw_doppelhaeuser", "Bauweise: nur Doppelhäuser zulässig", *BW, bwt("D")),
    ("bw_hausgruppen", "Bauweise: nur Hausgruppen zulässig", *BW, bwt("H")),
    ("bw_einzel_doppelhaeuser", "Bauweise: nur Einzel- und Doppelhäuser zulässig", *BW, bwt("ED")),
]
CAT["planzv"] = S

# =============================== Strom ===============================
RED = ("#FFFFFF", "#C8102E")
S = []
S += [
    ("umspannwerk", "Umspannwerk", *RED, fr_square() + [C(39, 50, 18, "N", "S", 4.5), C(61, 50, 18, "N", "S", 4.5)]),
    ("ortsnetzstation", "Ortsnetzstation / Trafostation", *RED,
     [R(7, 7, 86, 86, "F", "N", 0, 8), PG([(9, 91), (91, 91), (91, 9)], "S"), R(7, 7, 86, 86, "N", "S", 5, 8)]),
    ("maststation", "Maststation", *RED,
     [C(50, 50, 44, "F", "N", 0), P("M18.89,81.11 A44,44 0 0 0 81.11,18.89 Z", "S", "N", 0), C(50, 50, 44, "N", "S", 5)]),
    ("schaltstation", "Schaltstation", *RED,
     fr_square() + [L(18, 60, 38, 60), L(38, 60, 64, 40), L(64, 60, 82, 60),
                    C(38, 60, 4, "S", "N", 0), C(64, 60, 4, "S", "N", 0)]),
    ("uebergabestation", "Übergabestation / Kundenstation", *RED, fr_square() + [T("Ü", 50, 50, 40)]),
    ("kabelverteiler", "Kabelverteilerschrank", *RED, [R(12, 28, 76, 44, "F", "S", 5), L(12, 72, 88, 28, 5, cap="butt")]),
    ("hausanschluss", "Hausanschluss", *RED,
     [R(26, 48, 48, 34, "F", "S", 5), PL([(16, 52), (50, 20), (84, 52)], 5), C(50, 65, 7, "S", "N", 0)]),
    ("muffe", "Muffe", *RED, [L(6, 50, 94, 50, 5), E(50, 50, 22, 11, "S", "N", 0)]),
    ("endverschluss", "Kabelendverschluss", *RED, [L(6, 50, 46, 50, 5), PG([(46, 28), (86, 50), (46, 72)], "F", "S", 5)]),
    ("mast_gitter", "Freileitungsmast: Gittermast", *RED,
     [R(16, 16, 68, 68, "F", "S", 5), L(16, 16, 84, 84, 4.5, cap="butt"), L(16, 84, 84, 16, 4.5, cap="butt")]),
    ("mast_rohr", "Freileitungsmast: Holz-, Beton- oder Stahlrohrmast", *RED,
     [C(50, 50, 30, "F", "S", 5), C(50, 50, 10, "S", "N", 0)]),
    ("mast_abspann", "Freileitungsmast: Abspannmast", *RED,
     [R(16, 16, 68, 68, "F", "S", 5), L(16, 16, 84, 84, 4.5, cap="butt"), L(16, 84, 84, 16, 4.5, cap="butt"),
      C(50, 50, 11, "S", "N", 0)]),
    ("leuchte", "Leuchte / Lichtpunkt", *RED, [C(50, 50, 30, "F", "S", 5)] + xcross(50, 50, 21.2, 4.5)),
    ("ladesaeule", "Ladesäule Elektromobilität", *RED,
     fr_square() + [R(34, 36, 32, 24, "S", "N", 0, 5), L(42, 24, 42, 37, 6), L(58, 24, 58, 37, 6),
                    P("M50,60 V68 Q50,80 62,80 H74", "N", "S", 5)]),
    ("zaehler", "Zähler / Messeinrichtung", *RED, [R(14, 22, 72, 56, "F", "S", 5, 4), T("kWh", 50, 50, 18, maxw=54)]),
    ("erdung", "Erdungsanlage", *RED,
     [L(50, 14, 50, 46, 5), L(20, 46, 80, 46, 5.5), L(31, 62, 69, 62, 5.5), L(42, 78, 58, 78, 5.5)]),
    ("generator", "Erzeugungsanlage / Generator", *RED, fr_circle() + [T("G", 50, 50, 40)]),
    ("kraftwerk", "Kraftwerk", *RED, [R(7, 7, 86, 86, "S", "S", 5, 8)] + lightning(50, 50, 1.15, "F")),
    ("trennstelle_offen", "Trennstelle offen", *RED,
     [L(6, 56, 32, 56, 5), L(68, 56, 94, 56, 5), L(36, 52, 62, 30, 5),
      C(34, 56, 5.5, "F", "S", 4), C(66, 56, 5.5, "F", "S", 4)]),
    ("trennstelle_geschlossen", "Trennstelle geschlossen", *RED,
     [L(6, 50, 94, 50, 5), C(34, 50, 6.5, "S", "N", 0), C(66, 50, 6.5, "S", "N", 0)]),
    ("sicherung", "Sicherung", *RED, [R(24, 36, 52, 28, "F", "S", 5), L(6, 50, 94, 50, 5)]),
    ("batteriespeicher", "Batteriespeicher", *RED,
     [R(10, 28, 72, 44, "F", "S", 5, 5), R(82, 40, 9, 20, "S", "N", 0, 2), *cross(30, 50, 8, 4.5), L(54, 50, 68, 50, 4.5)]),
    ("kabelmerkstein", "Kabelmerkstein", *RED, [R(28, 28, 44, 44, "F", "S", 5), C(50, 50, 7, "S", "N", 0)]),
    ("transformator", "Transformator (Schaltzeichen)", *RED,
     [L(50, 6, 50, 20, 5), L(50, 80, 50, 94, 5), C(50, 38, 18, "N", "S", 5), C(50, 62, 18, "N", "S", 5)]),
]
CAT["strom"] = S

# =============================== EEG ===============================
WIND = ("#E3F2FD", "#0D47A1")
SUN = ("#FFF3C4", "#B45309")
BIO = ("#E2F3D5", "#2E7D32")
H2O = ("#D6ECFA", "#0B5CAD")
GEO = ("#FBE3D6", "#9A3412")
NEU = ("#FFFFFF", "#37474F")


def house(x=50, y=58, k=1.0):
    return [R(x - 20 * k, y - 6 * k, 40 * k, 28 * k, "F", "S", 4.5),
            PL([(x - 28 * k, y - 3 * k), (x, y - 30 * k), (x + 28 * k, y - 3 * k)], 4.5)]


S = []
S += [
    ("wea_bestand", "Windenergieanlage, Bestand", *WIND, fr_circle() + rotor(50, 50, 37)),
    ("wea_geplant", "Windenergieanlage, geplant", *WIND, fr_circle(dash="10 8") + rotor(50, 50, 37)),
    ("wea_genehmigt", "Windenergieanlage, genehmigt", *WIND,
     [C(50, 50, 45, "F", "S", 3.5), C(50, 50, 37, "N", "S", 3.5)] + rotor(50, 50, 31)),
    ("wea_rueckbau", "Windenergieanlage, Rückbau", *WIND,
     fr_circle() + rotor(50, 50, 37) + [L(19, 19, 81, 81, 5, cap="butt"), L(19, 81, 81, 19, 5, cap="butt")]),
    ("kleinwindanlage", "Kleinwindanlage", *WIND, [L(50, 44, 50, 94, 5)] + rotor(50, 44, 38)),
    ("windmessmast", "Windmessmast", *WIND,
     [L(50, 16, 50, 92, 5), L(50, 36, 20, 92, 3), L(50, 36, 80, 92, 3), L(32, 16, 68, 16, 4),
      C(32, 16, 6, "F", "S", 3.5), C(68, 16, 6, "F", "S", 3.5)]),
    ("rotorkreis", "Rotorkreis / Rotorradius", *WIND, [C(50, 50, 45, "N", "S", 3.5, "7 6"), C(50, 50, 6, "S", "N", 0)]),
    ("kranstellflaeche", "Kranstellfläche", *WIND, [R(8, 24, 84, 52, "F", "S", 5), T("K", 50, 50, 30)]),
    ("pv_freiflaeche", "Photovoltaik-Freiflächenanlage", *SUN,
     [PG([(24, 28), (92, 28), (76, 74), (8, 74)], "F", "S", 5), L(16, 51, 84, 51, 3.5),
      L(46.7, 28, 30.7, 74, 3.5), L(69.3, 28, 53.3, 74, 3.5)]),
    ("pv_dach", "Photovoltaik-Dachanlage", *SUN,
     house(50, 60, 1.25) + [PG([(58, 30.5), (78, 49.5), (72.5, 55), (52.5, 36)], "S")]),
    ("solarthermie", "Solarthermie", *SUN,
     [C(50, 38, 13, "F", "S", 5)] + [L(*rot([(0, -20)], a, 50, 38)[0], *rot([(0, -27)], a, 50, 38)[0], 4.5)
                                     for a in range(0, 360, 45)]
     + [wave(18, 80, 64, 6, 2, 5)]),
    ("biogasanlage", "Biogasanlage", *BIO,
     [P("M14,72 A36,36 0 0 1 86,72 Z", "F", "S", 5), L(8, 72, 92, 72, 5),
      P("M50,42 C59,51 61,58 56,64 C53,68 47,68 44,64 C39,57 44,51 50,42 Z", "S", "N", 0)]),
    ("biomasse", "Biomasseanlage", *BIO,
     [P("M22,80 C20,44 44,20 82,20 C82,58 58,82 22,80 Z", "F", "S", 5), L(22, 80, 62, 40, 4.5)]),
    ("wasserkraft", "Wasserkraftanlage", *H2O,
     fr_circle() + lightning(50, 36, 0.62) + [wave(22, 64, 56, 6, 2, 5), wave(28, 77, 44, 5, 2, 5)]),
    ("geothermie", "Geothermieanlage", *GEO,
     fr_circle() + [L(22, 36, 78, 36, 5)] + arrow(38, 44, 38, 80, 5, 11) + arrow(62, 80, 62, 44, 5, 11)),
    ("wasserstoff", "Wasserstoff / Elektrolyseur", *H2O, fr_hex() + [T("H", 42, 50, 30), T("2", 66, 62, 17)]),
    ("speicher", "Stromspeicher", *NEU,
     fr_square() + [R(22, 34, 50, 32, "N", "S", 4.5, 4), R(72, 43, 7, 14, "S", "N", 0, 1.5)] + lightning(47, 50, 0.42)),
    ("netzverknuepfungspunkt", "Netzverknüpfungspunkt", *NEU, fr_diamond() + [T("NVP", 50, 50, 17, maxw=52)]),
    ("einspeisepunkt", "Einspeisepunkt", *NEU, [L(12, 78, 88, 78, 6)] + arrow(50, 14, 50, 70, 6, 15)),
    ("immissionsort_schall", "Immissionsort Schall", *NEU,
     house(34, 60, 1.0) + [P("M68,38 A17,17 0 0 1 68,66", "N", "S", 4.5), P("M77,27 A31,31 0 0 1 77,77", "N", "S", 4.5)]),
    ("immissionsort_schatten", "Immissionsort Schattenwurf", *NEU,
     [PG([(54, 80), (94, 80), (80, 60), (54, 60)], "S")] + house(34, 60, 1.0)
     + [C(76, 26, 9, "F", "S", 4)] + [L(*rot([(0, -13.5)], a, 76, 26)[0], *rot([(0, -18)], a, 76, 26)[0], 3.5)
                                      for a in range(0, 360, 45)]),
    ("kwk_anlage", "KWK-Anlage / Blockheizkraftwerk", *NEU, fr_square() + [T("KWK", 50, 50, 20, maxw=66)]),
]
CAT["eeg"] = S
