"""Sammlung PlanZV: Planzeichen in Anlehnung an die Anlage zur Planzeichenverordnung (PlanZV 1990,
Stand 2025), Schwarz-Weiss-Fassung. Reihenfolge und Praefixe folgen den Nummern der Anlage:
  nu_ 1 Art der Nutzung      bw_ 3 Bauweise           gb_ 4.1 Gemeinbedarf   sp_ 4.2 Sport/Spiel
  vk_ 5/6 Verkehr            ve_ 7 Ver-/Entsorgung    lt_ 8 Leitungen        gr_ 9 Gruenflaechen
  wa_ 10 Wasser              ab_ 11 Aufschuettung     lw_ 12 Wald            pf_ 13.2 Bepflanzung
  sg_ 13.3 Schutzgebiete     dk_ 14 Denkmalschutz     so_/na_ 15 Sonstige    um_ Elemente fuer Umgrenzungslinien
Stil: schwarz auf weiss, Strich 4,5; Flaechenzeichen als liegendes Rechteck, Lagezeichen als Kreis.
Linien und Flaechen: Linienarten schwarz wie in der Schwarz-Weiss-Fassung, Flaechen in den Farben der farbigen
Fassung (Rot mittel, Braun mittel, Goldocker ...); Umgrenzungen nutzen die um_-Zeichen als Markierungslinie.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "planzv"
NAME = "PlanZV"
DESC = ("Planzeichen für Bauleitpläne in Anlehnung an die Anlage zur Planzeichenverordnung (PlanZV): Art der "
        "baulichen Nutzung, Bauweise, Gemeinbedarf, Verkehr, Ver- und Entsorgung, Grünflächen, Wasser, "
        "Bepflanzung, Schutzgebiete, Denkmalschutz, Nebenanlagen, Elemente für Umgrenzungslinien")
TAGS = "planzv, bauleitplanung, bebauungsplan, flaechennutzungsplan, planzeichen"

BW = ("#FFFFFF", "#000000")
SW = 4.5


def gb(*shapes):  # Gemeinbedarf, Sport/Spiel: schwarzes Rechteck, weisse Form
    return [R(4, 24, 92, 52, "S", "N", 0)] + list(shapes)


def gr(*shapes):  # Gruenflaeche: umrandetes Rechteck
    return [R(6, 24, 88, 52, "F", "S", SW)] + list(shapes)


def ve(*shapes, disc="F"):  # Ver- und Entsorgung: Kreis mit Flaechenteilung
    return [C(50, 50, 42, disc, "N", 0)] + list(shapes) + [C(50, 50, 42, "N", "S", SW)]


def kr(txt, h=30, mw=56):  # Kreis mit Kuerzel
    return [C(50, 50, 43, "F", "S", SW), T(txt, 50, 50, h, "S", maxw=mw)]


def nu(txt):  # Art der baulichen Nutzung: Kuerzel ohne Rahmen
    return [T(txt, 50, 50, 28, "S", maxw=94)]


def bwt(txt):  # Bauweise: Dreieck mit Buchstaben
    return [PG([(50, 8), (94, 88), (6, 88)], "F", "S", SW), T(txt, 50, 64, 24, "S", maxw=44)]


def sq(*shapes):  # Verkehrsflaeche besonderer Zweckbestimmung: schwarzes Quadrat, weisses Zeichen
    return [R(10, 10, 80, 80, "S", "N", 0)] + list(shapes)


def ring(*shapes):  # Luftverkehr u. a.: Kreis mit Zeichen
    return [C(50, 50, 43, "F", "S", SW)] + list(shapes)


def dots3(x, y, r=3.2):
    return [C(x - 6.5, y + 4, r, "S", "N", 0), C(x + 6.5, y + 4, r, "S", "N", 0), C(x, y - 6, r, "S", "N", 0)]


STRAUCH = [(27, 54, 15), (50, 46, 19), (73, 54, 15)]
BEPFL = [(25, 50, 15), (50, 50, 20), (75, 50, 15)]
BLADE = [(-4.5, -36), (4.5, -36), (4.5, -10), (-4.5, -10)]

S = []
# ---- 1 Art der baulichen Nutzung ----
for kz, txt in (("w", "Wohnbaufläche (W)"), ("ws", "Kleinsiedlungsgebiet (WS)"), ("wr", "Reines Wohngebiet (WR)"),
                ("wa", "Allgemeines Wohngebiet (WA)"), ("wb", "Besonderes Wohngebiet (WB)"),
                ("m", "Gemischte Baufläche (M)"), ("md", "Dorfgebiet (MD)"), ("mdw", "Dörfliches Wohngebiet (MDW)"),
                ("mi", "Mischgebiet (MI)"), ("mu", "Urbanes Gebiet (MU)"), ("mk", "Kerngebiet (MK)"),
                ("g", "Gewerbliche Baufläche (G)"), ("ge", "Gewerbegebiet (GE)"), ("gi", "Industriegebiet (GI)"),
                ("s", "Sonderbaufläche (S)"), ("so", "Sondergebiet (SO)")):
    S.append((f"nu_{kz}", f"Art der baulichen Nutzung: {txt}", *BW, nu(kz.upper())))
S += [
    ("nu_wind", "Art der baulichen Nutzung: Beschleunigungsgebiet für die Windenergie an Land (WIND)", *BW,
     [R(6, 26, 88, 48, "F", "S", SW, 0, "16 9"), T("WIND", 50, 50, 20, "S", maxw=70)]),
    # ---- 3 Bauweise ----
    ("bw_offen", "Bauweise: offene Bauweise", *BW, [T("o", 50, 50, 60)]),
    ("bw_geschlossen", "Bauweise: geschlossene Bauweise", *BW, [T("g", 50, 50, 52)]),
    ("bw_abweichend", "Bauweise: abweichende Bauweise", *BW, [T("a", 50, 50, 60)]),
    ("bw_einzelhaeuser", "Bauweise: nur Einzelhäuser zulässig", *BW, bwt("E")),
    ("bw_doppelhaeuser", "Bauweise: nur Doppelhäuser zulässig", *BW, bwt("D")),
    ("bw_hausgruppen", "Bauweise: nur Hausgruppen zulässig", *BW, bwt("H")),
    ("bw_einzel_doppelhaeuser", "Bauweise: nur Einzel- und Doppelhäuser zulässig", *BW, bwt("ED")),
    # ---- 4.1 Gemeinbedarf ----
    ("gb_oeffentliche_verwaltung", "Gemeinbedarf: Öffentliche Verwaltungen", *BW, gb(C(50, 50, 17, "F", "N", 0))),
    ("gb_schule", "Gemeinbedarf: Schule", *BW, gb(PG([(50, 31), (71, 68), (29, 68)], "F"))),
    ("gb_kirche", "Gemeinbedarf: Kirchen und kirchlichen Zwecken dienende Gebäude und Einrichtungen", *BW,
     gb(R(44, 29, 12, 42, "F", "N", 0), R(29, 44, 42, 12, "F", "N", 0), C(50, 50, 13, "F", "N", 0))),
    ("gb_sozial", "Gemeinbedarf: Sozialen Zwecken dienende Gebäude und Einrichtungen", *BW,
     gb(PG([(24, 50), (37, 33), (63, 33), (76, 50), (63, 67), (37, 67)], "F"))),
    ("gb_gesundheit", "Gemeinbedarf: Gesundheitlichen Zwecken dienende Gebäude und Einrichtungen", *BW,
     gb(R(43, 30, 14, 40, "F", "N", 0), R(30, 43, 40, 14, "F", "N", 0))),
    ("gb_kultur", "Gemeinbedarf: Kulturellen Zwecken dienende Gebäude und Einrichtungen", *BW,
     gb(PG([(29, 32), (71, 32), (50, 69)], "F"))),
    ("gb_sport", "Gemeinbedarf: Sportlichen Zwecken dienende Gebäude und Einrichtungen", *BW,
     gb(R(22, 38, 56, 24, "F", "N", 0, rx=12))),
    ("gb_post", "Gemeinbedarf: Post", *BW,
     gb(C(45, 55, 9, "N", "F", 5), P("M18,43 H36 Q44,43 50,47", "N", "F", 5),
        P("M53,49 Q68,46 82,33 V69 Q68,60 54,61 Z", "F", "N", 0))),
    ("gb_schutzbauwerk", "Gemeinbedarf: Schutzbauwerk", *BW,
     gb(P("M30,69 C30,44 38,31 50,31 C62,31 70,44 70,69 Z", "F", "N", 0))),
    ("gb_feuerwehr", "Gemeinbedarf: Feuerwehr", *BW, gb(T("F", 50, 50, 32, "F"))),
    # ---- 4.2 Sport- und Spielanlagen ----
    ("sp_sportanlagen", "Sport- und Spielanlagen: Sportanlagen", *BW, gb(R(22, 38, 56, 24, "F", "N", 0, rx=12))),
    ("sp_spielanlagen", "Sport- und Spielanlagen: Spielanlagen", *BW,
     gb(PG([(37, 42), (63, 42), (59, 68), (41, 68)], "F"), L(34, 42, 66, 42, 3.5, "F"),
        P("M39,42 A11,12 0 0 1 61,42", "N", "F", 3))),
    # ---- 5 und 6 Verkehr ----
    ("vk_ruhender_verkehr", "Verkehr: Ruhender Verkehr", *BW, [R(12, 12, 76, 76, "F", "S", SW), T("P", 50, 50, 44)]),
    ("vk_hauptwanderweg", "Verkehr: Überörtlicher Weg, Hauptwanderweg", *BW,
     [PG([(50, 10), (90, 50), (50, 90), (10, 50)], "F", "S", SW), T("W", 50, 50, 26)]),
    ("vk_flughafen", "Luftverkehr: Flughafen", *BW,
     ring(*plane(50, 50, 1.05), *[R(50 + x - 2.6, 50 + y - 9, 5.2, 11, "S", "N", 0, 1.5)
                                  for x, y in ((-23, 4), (-13, -2), (13, -2), (23, 4))])),
    ("vk_landeplatz", "Luftverkehr: Landeplatz", *BW, ring(*plane(50, 50, 0.92))),
    ("vk_segelfluggelaende", "Luftverkehr: Segelfluggelände", *BW,
     ring(P("M18,50 C28,38 42,38 50,58 C58,38 72,38 82,50 C70,46 60,48 50,68 C40,48 30,46 18,50 Z", "S", "N", 0))),
    ("vk_hubschrauberlandeplatz", "Luftverkehr: Hubschrauberlandeplatz", *BW,
     ring(*[PG(rot(BLADE, a, 50, 52), "F", "S", 3) for a in (0, 120, 240)], C(50, 52, 6, "F", "S", 3))),
    ("vk_parkflaeche", "Verkehrsfläche besonderer Zweckbestimmung: Öffentliche Parkfläche", *BW,
     sq(T("P", 50, 50, 52, "F"))),
    ("vk_fussgaengerbereich", "Verkehrsfläche besonderer Zweckbestimmung: Fußgängerbereich", *BW,
     sq(*fit(person("F"), 50, 50, 0.72))),
    ("vk_verkehrsberuhigter_bereich", "Verkehrsfläche besonderer Zweckbestimmung: Verkehrsberuhigter Bereich", *BW,
     sq(PG([(22, 26), (38, 26), (50, 56), (62, 26), (78, 26), (57, 76), (43, 76)], "F"))),
    ("vk_einfahrt", "Verkehr: Einfahrt (Spitze zeigt auf das Grundstück)", *BW, [PG([(20, 24), (80, 24), (50, 80)], "S")]),
    # ---- 7 Ver- und Entsorgung ----
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
    ("ve_abfall", "Ver-/Entsorgung: Abfall", *BW, ve(PG([(50, 24), (74, 66), (26, 66)], "F"), disc="S")),
    ("ve_ablagerung", "Ver-/Entsorgung: Ablagerung", *BW,
     ve(PG([(50, 20), (80, 50), (50, 80), (20, 50)], "F"), disc="S")),
    ("ve_erneuerbare_energien", "Ver-/Entsorgung: Erneuerbare Energien", *BW, kr("EE", 28)),
    ("ve_kraft_waerme_kopplung", "Ver-/Entsorgung: Kraft-Wärme-Kopplung", *BW, kr("KWK", 22, 60)),
    # ---- 8 Hauptversorgungs- und Hauptabwasserleitungen (Elemente fuer Markierungslinien) ----
    ("lt_oberirdisch", "Hauptversorgungsleitung oberirdisch (Linienelement)", *BW,
     [L(2, 50, 98, 50, 4, cap="butt"), PG([(50, 34), (68, 50), (50, 66), (32, 50)], "S")]),
    ("lt_unterirdisch", "Hauptversorgungsleitung unterirdisch (Linienelement)", *BW,
     [L(2, 50, 24, 50, 4, cap="butt"), L(76, 50, 98, 50, 4, cap="butt"),
      PG([(50, 34), (68, 50), (50, 66), (32, 50)], "F", "S", 4)]),
    # ---- 9 Gruenflaechen ----
    ("gr_parkanlage", "Grünfläche: Parkanlage", *BW, gr(*dots3(27, 41), *dots3(73, 41), *dots3(50, 61))),
    ("gr_dauerkleingaerten", "Grünfläche: Dauerkleingärten", *BW,
     gr(L(35.3, 24, 35.3, 76, 3.5), L(64.7, 24, 64.7, 76, 3.5), L(6, 50, 94, 50, 3.5),
        *[C(x, y, 3.2, "S", "N", 0) for x in (20.7, 50, 79.3) for y in (37, 63)])),
    ("gr_sportplatz", "Grünfläche: Sportplatz", *BW, gr(R(22, 37, 56, 26, "N", "S", 4, rx=13))),
    ("gr_spielplatz", "Grünfläche: Spielplatz", *BW,
     gr(PL([(37, 42), (63, 42), (59, 68), (41, 68)], 3.5, close=True), L(34, 42, 66, 42, 3.5),
        P("M39,42 A11,12 0 0 1 61,42", "N", "S", 3))),
    ("gr_zeltplatz", "Grünfläche: Zeltplatz", *BW,
     gr(PL([(50, 36), (69, 68), (31, 68)], 4, close=True), L(50, 36, 46, 29, 3.5), L(50, 36, 54, 29, 3.5))),
    ("gr_badeplatz", "Grünfläche: Badeplatz, Freibad", *BW,
     gr(*[wave(20, 36 + i * 9.3, 60, 4.5, 3, 3.5) for i in range(4)])),
    ("gr_friedhof", "Grünfläche: Friedhof", *BW,
     gr(*cross(30, 61, 6.5, 4), *cross(50, 39, 6.5, 4), *cross(70, 61, 6.5, 4))),
    # ---- 10 Wasserflaechen, Wasserwirtschaft ----
    ("wa_hafen", "Wasserfläche: Hafen", *BW, kr("H")),
    ("wa_hochwasserrueckhaltebecken", "Wasserwirtschaft: Hochwasserrückhaltebecken", *BW, kr("R")),
    ("wa_ueberschwemmungsgebiet", "Wasserwirtschaft: Überschwemmungsgebiet", *BW, kr("Ü")),
    ("wa_schutzgebiet_grundwasser", "Wasserrecht: Schutzgebiet für Grund- und Quellwassergewinnung", *BW, kr("GW", 26)),
    ("wa_schutzgebiet_oberflaechengewaesser", "Wasserrecht: Schutzgebiet für Oberflächengewässer", *BW, kr("OW", 26)),
    # ---- 11 Aufschuettungen, Abgrabungen ----
    ("ab_aufschuettung", "Fläche für Aufschüttungen", *BW,
     ring(L(22, 54, 78, 54, 4), R(37, 36, 26, 18, "S", "N", 0))),
    ("ab_abgrabung", "Fläche für Abgrabungen oder für die Gewinnung von Bodenschätzen", *BW,
     ring(L(22, 46, 78, 46, 4), R(37, 46, 26, 18, "S", "N", 0))),
    # ---- 12 Wald ----
    ("lw_erholungswald", "Wald: Erholungswald", *BW, kr("E")),
    # ---- 13.2 Anpflanzen und Erhaltung ----
    ("pf_baum_anpflanzen", "Anpflanzen: Bäume", *BW, [C(50, 50, 40, "F", "S", SW), C(50, 50, 7, "F", "S", 3.5)]),
    ("pf_strauch_anpflanzen", "Anpflanzen: Sträucher", *BW, [cloud(STRAUCH)]),
    ("pf_bepflanzung_anpflanzen", "Anpflanzen: Sonstige Bepflanzungen", *BW,
     [cloud(BEPFL), R(21, 39, 58, 22, "F", "S", 4)]),
    ("pf_baum_erhalten", "Erhaltung: Bäume", *BW, [C(50, 50, 40, "F", "S", SW), C(50, 50, 7, "S", "N", 0)]),
    ("pf_strauch_erhalten", "Erhaltung: Sträucher", *BW, [cloud(STRAUCH), C(50, 50, 6, "S", "N", 0)]),
    ("pf_bepflanzung_erhalten", "Erhaltung: Sonstige Bepflanzungen", *BW,
     [cloud(BEPFL), R(21, 39, 58, 22, "F", "S", 4), C(50, 50, 5.5, "S", "N", 0)]),
    # ---- 13.3 Schutzgebiete und Schutzobjekte im Sinne des Naturschutzrechts ----
    ("sg_naturschutzgebiet", "Schutzgebiet: Naturschutzgebiet", *BW, kr("N")),
    ("sg_nationalpark", "Schutzgebiet: Nationalpark", *BW, kr("NLP", 22, 60)),
    ("sg_landschaftsschutzgebiet", "Schutzgebiet: Landschaftsschutzgebiet", *BW, kr("L")),
    ("sg_naturpark", "Schutzgebiet: Naturpark", *BW, kr("NP", 26)),
    ("sg_naturdenkmal", "Schutzgebiet: Naturdenkmal", *BW, kr("ND", 26)),
    ("sg_geschuetzter_landschaftsbestandteil", "Schutzgebiet: Geschützter Landschaftsbestandteil", *BW, kr("LB", 26)),
    # ---- 14 Stadterhaltung und Denkmalschutz ----
    ("dk_erhaltungsbereich", "Stadterhaltung: Erhaltungsbereich", *BW, kr("E")),
    ("dk_gesamtanlage", "Denkmalschutz: Gesamtanlage (Ensemble)", *BW, kr("D")),
    ("dk_einzelanlage", "Denkmalschutz: Einzelanlage (unbewegliches Kulturdenkmal)", *BW,
     [R(12, 12, 76, 76, "F", "S", SW), T("D", 50, 50, 38)]),
    # ---- 15 Sonstige Planzeichen ----
    ("so_hoehenlage", "Sonstige: Höhenlage bei Festsetzungen (Höhenbezugspunkt)", *BW,
     [C(50, 50, 30, "F", "S", SW), L(20, 50, 80, 50, 4, cap="butt"), L(50, 20, 50, 80, 4, cap="butt")]),
    ("so_altlast", "Sonstige: Boden erheblich mit umweltgefährdenden Stoffen belastet (Lagezeichen)", *BW,
     [C(50, 50, 32, "F", "S", SW), L(14, 14, 86, 86, 7), L(14, 86, 86, 14, 7)]),
    ("na_stellplaetze", "Nebenanlagen: Stellplätze", *BW, [T("St", 50, 50, 50, maxw=90)]),
    ("na_garagen", "Nebenanlagen: Garagen", *BW, [T("Ga", 50, 50, 46, maxw=90)]),
    ("na_gemeinschaftsstellplaetze", "Nebenanlagen: Gemeinschaftsstellplätze", *BW, [T("GSt", 50, 50, 44, maxw=92)]),
    ("na_gemeinschaftsgaragen", "Nebenanlagen: Gemeinschaftsgaragen", *BW, [T("GGa", 50, 50, 40, maxw=92)]),
    ("na_tiefgaragen", "Nebenanlagen: Tiefgaragen (gebräuchliche Ergänzung)", *BW, [T("TGa", 50, 50, 40, maxw=92)]),
    # ---- Elemente fuer Umgrenzungslinien: Linie durch die Symbolmitte, Innenseite unten ----
    ("um_nutzungsgrenze", "Linienelement: Abgrenzung unterschiedlicher Nutzung (Perlschnur)", *BW,
     [C(50, 50, 11, "S", "N", 0)]),
    ("um_anpflanzung", "Linienelement: Umgrenzung von Flächen zum Anpflanzen", *BW, [C(50, 50, 15, "F", "S", SW)]),
    ("um_erhaltung", "Linienelement: Umgrenzung von Flächen mit Bindungen für die Erhaltung", *BW,
     [C(50, 50, 15, "S", "N", 0)]),
    ("um_massnahmen_natur", "Linienelement: Umgrenzung von Flächen für Maßnahmen zum Schutz, zur Pflege und zur "
     "Entwicklung von Natur und Landschaft", *BW, [L(50, 50, 50, 84, SW, cap="butt"), L(30, 84, 70, 84, SW)]),
    ("um_schutzgebiet", "Linienelement: Umgrenzung von Schutzgebieten im Sinne des Naturschutzrechts "
     "(geschlossen, wie in der Anlage)", *BW,
     [L(x, 50, x, 78, 4, cap="butt") for x in (32, 44, 56, 68)] + [L(30, 78, 70, 78, 4, cap="butt")]),
    ("um_schutzgebiet_offen", "Linienelement: Umgrenzung von Schutzgebieten, offene Variante zur Unterscheidung",
     *BW, [L(x, 50, x, 78, 4, cap="butt") for x in (32, 44, 56, 68)]),
    ("um_immissionsschutz", "Linienelement: Umgrenzung von Flächen für Vorkehrungen zum Schutz gegen schädliche "
     "Umwelteinwirkungen", *BW, [PG([(26, 50), (74, 50), (50, 84)], "S")]),
    ("um_luftreinhaltung", "Linienelement: Umgrenzung von Gebieten mit Verwendungsbeschränkung "
     "luftverunreinigender Stoffe", *BW, [PL([(26, 50), (50, 82), (74, 50)], SW)]),
    ("um_freihaltung", "Linienelement: Umgrenzung von Flächen, die von der Bebauung freizuhalten sind", *BW,
     [PG([(26, 50), (74, 50), (50, 84)], "F", "S", 4)]),
    ("um_bergbau", "Linienelement: Umgrenzung von Flächen, unter denen der Bergbau umgeht", *BW,
     [R(32, 50, 36, 26, "S", "N", 0)]),
    ("um_altlast", "Linienelement: Umgrenzung von Flächen mit erheblich belasteten Böden", *BW, xcross(50, 50, 16, 5)),
    ("um_ohne_ein_ausfahrt", "Linienelement: Bereich ohne Ein- und Ausfahrt", *BW,
     [P("M30,50 A20,20 0 0 0 70,50 Z", "S", "N", 0)]),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
K0 = "#000000"
ROT, BLAU_L, GRUEN_L = "#E8452C", "#1E96C8", "#4FE05A"      # Baulinie, Baugrenze, Strassenbegrenzungslinie
OCKER, VIOLETT, VIOLETT_D, GRAU_D = "#FFD92E", "#D790DA", "#B040B8", "#6E6E6E"


def um(name, abstand, groesse=5.0, dy=0):  # Umgrenzung: Linie mit um_-Zeichen auf der Innenseite, Ecken frei
    return [linie(K0, 0.3), marken(sv(name, groesse, dy=dy), abstand, ecken=0.4 * groesse)]


def sgb(name, start, raster=8.0, groesse=10.0):  # Schutzgebiet: Gabeln innen, Beginn auf dem Raster waehlbar
    return [linie(K0, 0.7), marken(sv(name, groesse), raster, start=start, ecken=3.0, raster=raster)]


def fa(farbe):  # farbige Flaeche mit duenner Umrandung
    return [voll(farbe), linie(K0, 0.25)]


LINIEN = [
    ("Baulinie", [linie(K0, 0.35, [6, 1.2, 0.5, 1.2, 0.5, 1.2])]),
    ("Baulinie, farbig", [linie(ROT, 1.2, versatz=0.6), linie(K0, 0.35, [6, 1.2, 0.5, 1.2, 0.5, 1.2])]),
    ("Baugrenze", [linie(K0, 0.35, [6, 1.2, 0.5, 1.2])]),
    ("Baugrenze, farbig", [linie(BLAU_L, 1.2, versatz=0.6), linie(K0, 0.35, [6, 1.2, 0.5, 1.2])]),
    ("Straßenbegrenzungslinie", [linie(K0, 0.35)]),
    ("Straßenbegrenzungslinie, farbig", [linie(GRUEN_L, 1.2, versatz=0.6), linie(K0, 0.35)]),
    ("Abgrenzung unterschiedlicher Nutzung", [linie(K0, 0.25), marken(mk("circle", 1.0, K0), 4)]),
    ("Grenze des räumlichen Geltungsbereichs", [linie(K0, 1.2, [7, 1.5])]),
    ("Bereich ohne Ein- und Ausfahrt", [linie(K0, 0.3), marken(sv("um_ohne_ein_ausfahrt", 4.5), 4.5)]),
    ("Hauptversorgungsleitung oberirdisch", [linie(K0, 0.3), marken(mk("diamond", 1.8, K0), 9)]),
    ("Hauptversorgungsleitung unterirdisch",
     [linie(K0, 0.3, [3, 1.5]), marken(mk("diamond", 1.8, "#FFFFFF", K0, 0.3), 9)]),
    ("Autobahn und autobahnähnliche Straße",
     [linie(OCKER, 3.0), linie(K0, 0.5, versatz=1.5), linie(K0, 0.5, versatz=-1.5), linie(K0, 0.2)]),
    ("Sonstige Hauptverkehrsstraße", [linie(OCKER, 2.4), linie(K0, 0.4, versatz=1.2), linie(K0, 0.4, versatz=-1.2)]),
    ("Straßenbahn", [linie(K0, 0.3), marken(mk("line", 1.6, K0, rw=0.3, dy=-0.8), 5, 2.1),
                     marken(mk("line", 1.6, K0, rw=0.3, dy=-0.8), 5, 2.9)]),
    ("Seilbahn", [linie(K0, 0.3), marken(mk("circle", 1.8, "#FFFFFF", K0, 0.3), 12)]),
    ("Hauptwanderweg", [marken(mk("circle", 0.8, K0), 2.5)]),
    ("Geh-, Fahr- und Leitungsrecht bei schmalen Flächen",
     [linie(K0, 0.3, [4, 2], versatz=0.9), linie(K0, 0.3, [4, 2], versatz=-0.9)]),
    ("Stützmauer", [linie(K0, 0.25, versatz=0.6), linie(K0, 0.25, versatz=-0.6),
                    marken(mk("line", 1.7, K0, rw=0.2, winkel=45), 1.3)]),
]

FLAECHEN = [
    ("Wohnbaufläche (Rot mittel)", fa("#F4B3AA")),
    ("Gemischte Baufläche (Braun mittel)", fa("#D8C08A")),
    ("Gewerbliche Baufläche (Grau mittel)", fa("#B4B8B4")),
    ("Sonderbaufläche (Orange mittel)", fa("#FFA51F")),
    ("Fläche für den Gemeinbedarf (Karminrot mittel)", fa("#F7A8D8")),
    ("Straßenverkehrsfläche (Goldocker)", fa(OCKER)),
    ("Verkehrsfläche besonderer Zweckbestimmung", [voll("#FFFFFF"), schraffur(OCKER, 2.2, 45, 4.4), linie(K0, 0.25)]),
    ("Bahnanlagen (Violett mittel)", fa(VIOLETT)),
    ("Fläche für den Luftverkehr", [band(VIOLETT_D, 1.5), linie(K0, 0.25)]),
    ("Fläche für Versorgungsanlagen (Gelb hell)", fa("#F6FF5A")),
    ("Grünfläche (Grün mittel)", fa("#8FE38F")),
    ("Wasserfläche (Blau mittel)", fa("#A9D9F2")),
    ("Fläche für die Wasserwirtschaft", [band("#2E9BCB", 1.5), linie(K0, 0.25)]),
    ("Fläche für die Landwirtschaft (Gelbgrün)", fa("#B4F2A6")),
    ("Fläche für Wald (Blaugrün)", fa("#1FA3A3")),
    ("Maßnahmen zum Schutz, zur Pflege und zur Entwicklung von Natur und Landschaft", um("um_massnahmen_natur", 6)),
    ("Fläche zum Anpflanzen von Bäumen und Sträuchern", um("um_anpflanzung", 3.5, 4.0, dy=1.2)),
    ("Fläche mit Bindungen für die Erhaltung von Bäumen und Sträuchern", um("um_erhaltung", 3.5, 4.0, dy=1.2)),
    # Zwei Schutzgebiete an gemeinsamer Grenze: gleiches Raster, das zweite ein halbes Raster versetzt, damit
    # die Gabeln beider Flaechen beiderseits der Linie auf Luecke stehen.
    ("Naturschutzgebiet, geschlossene Signatur", sgb("um_schutzgebiet", 4.0)),
    ("Landschaftsschutzgebiet, offene Signatur (versetzt)", sgb("um_schutzgebiet_offen", 8.0)),
    ("Erhaltungsbereich oder Denkmalschutz, farbig",
     [band(K0, 1.55), band("#E0705C", 1.4), marken(mk("line", 1.4, K0, rw=0.2, dy=0.7), 3.5, ecken=1.5), linie(K0, 0.3)]),
    ("Fläche für Nebenanlagen, Stellplätze und Garagen", [linie(ROT, 0.35, [3, 1.5])]),
    ("Mit Geh-, Fahr- und Leitungsrechten zu belastende Fläche",
     [linie(K0, 0.3), marken(mk("square", 2.2, None, K0, 0.25, dy=1.1), 3.4, ecken=2.4)]),
    ("Vorkehrungen zum Schutz gegen schädliche Umwelteinwirkungen", um("um_immissionsschutz", 5)),
    ("Gebiet mit Verwendungsbeschränkung luftverunreinigender Stoffe", um("um_luftreinhaltung", 4)),
    ("Von der Bebauung freizuhaltende Fläche", um("um_freihaltung", 5)),
    ("Fläche, unter der der Bergbau umgeht", um("um_bergbau", 5)),
    ("Fläche mit erheblich belasteten Böden", [linie(K0, 0.3), marken(sv("um_altlast", 5, dy=1.6), 5, ecken=2.6)]),
    ("Räumlicher Geltungsbereich", [linie(K0, 2.4, [7, 1.5], innen=True)]),
    ("Räumlicher Geltungsbereich, farbig", [band(GRAU_D, 1.3)]),
]
