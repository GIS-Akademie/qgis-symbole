from lib import *

CAT = {}

# =============================== Naturschutz ===============================
GR = ("#DDF0C8", "#1E6B1E")
BL = ("#D6ECFA", "#0B5CAD")


def sq(txt, h=22, mw=64):
    return fr_square() + [T(txt, 50, 50, h, maxw=mw)]


def dia(txt, h=28, mw=44):
    return fr_diamond() + [T(txt, 50, 50, h, maxw=mw)]


BAT = [(50, 34), (54, 27), (57, 36), (67, 30), (85, 33), (94, 49), (83, 45), (77, 56), (69, 49), (62, 61),
       (55, 55), (50, 72), (45, 55), (38, 61), (31, 49), (23, 56), (17, 45), (6, 49), (15, 33), (33, 30),
       (43, 36), (46, 27)]
S = [
    ("nsg", "Naturschutzgebiet", *GR, sq("NSG")),
    ("lsg", "Landschaftsschutzgebiet", *GR, sq("LSG")),
    ("ffh_gebiet", "FFH-Gebiet", *GR, sq("FFH")),
    ("vogelschutzgebiet", "Vogelschutzgebiet", *GR, sq("VSG")),
    ("nationalpark", "Nationalpark", *GR, sq("NLP")),
    ("biosphaerenreservat", "Biosphärenreservat", *GR, sq("BR", 30, 56)),
    ("naturpark", "Naturpark", *GR, sq("NP", 30, 56)),
    ("naturdenkmal", "Naturdenkmal", *GR, sq("ND", 30, 56)),
    ("geschuetzter_landschaftsbestandteil", "Geschützter Landschaftsbestandteil", *GR, sq("GLB")),
    ("biotop_gesetzlich", "Gesetzlich geschütztes Biotop (§ 30 BNatSchG)", *GR, sq("§30")),
    ("horst", "Horststandort", *GR,
     fr_circle() + [E(34, 47, 8, 11, "F", "S", 3.5), E(66, 47, 8, 11, "F", "S", 3.5), E(50, 43, 8.5, 12, "F", "S", 3.5),
                    P("M20,54 H80 A30,22 0 0 1 20,54 Z", "S", "N", 0), L(13, 53, 87, 53, 5),
                    L(22, 60, 10, 66, 3.5), L(78, 60, 90, 66, 3.5)]),
    ("brutplatz", "Brutplatz / Niststätte", *GR,
     [P("M50,10 C66,10 78,40 78,58 C78,76 66,90 50,90 C34,90 22,76 22,58 C22,40 34,10 50,10 Z", "F", "S", 5)]),
    ("fledermausquartier", "Fledermausquartier", *GR,
     fr_circle() + [PG(mv([(x - 50, y - 49) for x, y in BAT], 50, 50, 0.84), "S")]),
    ("vogel_rast", "Rastvogel / Zugvogel", *GR,
     fr_circle() + [P("M16,56 Q32,30 50,54 Q68,30 84,56", "N", "S", 6)]),
    ("laichgewaesser", "Amphibien-Laichgewässer", *BL,
     [E(50, 54, 42, 28, "F", "S", 5)] + [C(x, y, 5, "S", "N", 0) for x, y in ((34, 50), (50, 62), (64, 46), (48, 42))]),
    ("fundpunkt_flora", "Fundpunkt Flora", *GR,
     [C(x, y, 13, "F", "S", 4) for x, y in regpoly(50, 50, 22, 5)] + [C(50, 50, 10, "S", "N", 0)]),
    ("fundpunkt_fauna", "Fundpunkt Fauna", *GR,
     fr_circle() + [E(50, 63, 16, 13, "S", "N", 0), C(29, 47, 7, "S", "N", 0), C(42, 33, 7.5, "S", "N", 0),
                    C(58, 33, 7.5, "S", "N", 0), C(71, 47, 7, "S", "N", 0)]),
    ("hoehlenbaum", "Höhlenbaum", *GR, treetop(50, 50, 40) + [C(50, 50, 12, "S", "N", 0)]),
    ("habitatbaum", "Habitatbaum", *GR, treetop(50, 50, 40) + [T("H", 50, 50, 30)]),
    ("nistkasten", "Nistkasten / Nisthilfe", *GR,
     [R(28, 30, 44, 54, "F", "S", 5), PL([(20, 34), (50, 12), (80, 34)], 5), C(50, 52, 9, "S", "N", 0),
      L(50, 68, 50, 76, 4.5)]),
    ("kompensation_ausgleich", "Ausgleichsmaßnahme", *GR, dia("A", 34)),
    ("kompensation_ersatz", "Ersatzmaßnahme", *GR, dia("E", 34)),
    ("cef_massnahme", "CEF-Maßnahme (vorgezogener Ausgleich)", *GR, dia("CEF", 20, 50)),
    ("fcs_massnahme", "FCS-Maßnahme", *GR, dia("FCS", 20, 50)),
    ("vermeidungsmassnahme", "Vermeidungsmaßnahme", *GR, dia("V", 34)),
    ("wildtierkorridor", "Wildtierkorridor / Biotopverbund", *GR,
     fr_circle() + arrow(50, 50, 84, 50, 6, 14) + arrow(50, 50, 16, 50, 6, 14)),
    ("beobachtungspunkt", "Beobachtungspunkt / Zählpunkt", *GR,
     [P("M8,50 Q50,10 92,50 Q50,90 8,50 Z", "F", "S", 5), C(50, 50, 14, "S", "N", 0)]),
]
CAT["naturschutz"] = S

# =============================== Landschaftsplanung ===============================
LG = ("#CDE8B5", "#2E6B2E")


def conifer(x, base, h, w):
    return [L(x, base - h * 0.25, x, base, 4), PG([(x, base - h), (x + w / 2, base - h * 0.22), (x - w / 2, base - h * 0.22)],
                                                  "F", "S", 4)]


def tuft(x, y, k=1.0):
    return [L(x, y, x, y - 18 * k, 4), L(x, y, x - 10 * k, y - 13 * k, 4), L(x, y, x + 10 * k, y - 13 * k, 4)]


S = [
    ("baum_laub", "Laubbaum", *LG, treetop(50, 50, 41) + [C(50, 50, 6, "S", "N", 0)]),
    ("baum_nadel", "Nadelbaum", *LG, [PG(star(50, 50, 45, 25, 8), "F", "S", 4), C(50, 50, 6, "S", "N", 0)]),
    ("baum_pflanzung", "Baum, Neupflanzung", *LG, treetop(50, 50, 41) + cross(50, 50, 20, 6)),
    ("baum_faellung", "Baum, Fällung", *LG, treetop(50, 50, 41) + xcross(50, 50, 30, 6)),
    ("baum_erhalt", "Baum, zu erhalten", *LG,
     [C(50, 50, 46, "N", "S", 3.5)] + treetop(50, 50, 33) + [C(50, 50, 6, "S", "N", 0)]),
    ("obstbaum", "Obstbaum / Streuobst", *LG,
     treetop(50, 50, 41) + [C(36, 44, 6, "S", "N", 0), C(60, 38, 6, "S", "N", 0), C(54, 64, 6, "S", "N", 0)]),
    ("strauch", "Strauch / Gebüsch", *LG, treetop(50, 50, 30, k=6)),
    ("hecke", "Hecke", *LG,
     treetop(21, 50, 15, sw=3.5, k=6) + treetop(50, 50, 15, sw=3.5, k=6) + treetop(79, 50, 15, sw=3.5, k=6)),
    ("baumreihe", "Baumreihe / Allee", *LG,
     [L(4, 50, 96, 50, 3)] + [C(x, 50, 13, "F", "S", 4) for x in (20, 50, 80)]
     + [C(x, 50, 3.5, "S", "N", 0) for x in (20, 50, 80)]),
    ("aufforstung", "Aufforstung / Waldentwicklung", *LG,
     conifer(26, 88, 52, 34) + conifer(74, 88, 52, 34) + conifer(50, 66, 56, 36)),
    ("gruenland", "Grünland / Wiese", *LG, tuft(26, 46) + tuft(66, 40) + tuft(42, 82) + tuft(80, 80)),
    ("roehricht", "Röhricht", BL[0], LG[1],
     [L(30, 86, 30, 34, 4), L(50, 86, 50, 22, 4), L(70, 86, 70, 38, 4), E(30, 30, 5, 12, "S", "N", 0),
      E(50, 20, 5, 12, "S", "N", 0), E(70, 34, 5, 12, "S", "N", 0), wave(10, 88, 80, 5, 3, 4)]),
    ("stillgewaesser", "Stillgewässer / Kleingewässer", *BL,
     [P("M14,52 C10,30 34,18 54,22 C76,18 94,36 88,56 C86,76 62,84 42,80 C24,82 16,70 14,52 Z", "F", "S", 5),
      wave(32, 46, 30, 4, 2, 3.5), wave(44, 60, 30, 4, 2, 3.5)]),
    ("quelle", "Quelle", *BL, [C(50, 30, 18, "F", "S", 5), P("M50,48 Q38,60 50,70 T50,94", "N", "S", 5)]),
    ("gewaesserrenaturierung", "Gewässerrenaturierung", *BL,
     [P("M8,62 Q22,26 40,50 T68,50", "N", "S", 7)] + arrow(68, 50, 90, 34, 7, 16)),
    ("aussichtspunkt", "Aussichtspunkt", *LG,
     [L(50, 80, *rot([(0, -58)], a, 50, 80)[0], 5) for a in (-66, -33, 0, 33, 66)] + [C(50, 80, 9, "S", "N", 0)]),
    ("rastplatz", "Rastplatz", *LG,
     [L(22, 36, 78, 36, 7), L(36, 38, 26, 82, 5), L(64, 38, 74, 82, 5), L(6, 60, 30, 60, 6), L(70, 60, 94, 60, 6)]),
    ("entsiegelung", "Entsiegelung", *LG,
     [R(10, 10, 80, 80, "F", "S", 5), PL([(34, 10), (46, 36), (36, 54), (58, 70), (50, 90)], 4.5),
      PL([(46, 36), (68, 32), (90, 44)], 4.5)]),
    ("bluehflaeche", "Blühfläche / Blühstreifen", *LG,
     [L(50, 46, 50, 92, 5), P("M50,76 Q32,74 28,58 Q46,60 50,76 Z", "S", "N", 0),
      P("M50,68 Q68,66 72,50 Q54,52 50,68 Z", "S", "N", 0)]
     + [C(x, y, 9, "F", "S", 3.5) for x, y in regpoly(50, 28, 14, 5)] + [C(50, 28, 7, "S", "N", 0)]),
    ("lesesteinhaufen", "Lesesteinhaufen / Steinriegel", "#E6E6E6", "#4D4D4D",
     [E(32, 68, 22, 15, "F", "S", 4.5), E(70, 70, 20, 14, "F", "S", 4.5), E(52, 44, 21, 15, "F", "S", 4.5)]),
    ("totholz", "Totholz", "#E8D5B5", "#6B4423",
     [R(8, 36, 76, 28, "F", "S", 5, 14), E(80, 50, 11, 14, "F", "S", 5), C(80, 50, 4.5, "N", "S", 3),
      L(22, 46, 50, 46, 3), L(30, 55, 62, 55, 3)]),
    ("massnahmenflaeche", "Maßnahmenfläche", *LG, [R(8, 8, 84, 84, "F", "S", 5, 4, "12 8"), T("M", 50, 50, 36)]),
]
CAT["landschaftsplanung"] = S

# =============================== Verkehr ===============================
VB = ("#1F5FA8", "#0D3C73")


def vq(*sh):
    return fr_square() + list(sh)


def vt(txt, h=44, mw=66):
    return vq(T(txt, 50, 50, h, "W", maxw=mw))


BIKE = [C(27, 62, 15, "N", "W", 4.5), C(73, 62, 15, "N", "W", 4.5),
        PL([(27, 62), (42, 36), (64, 36), (73, 62)], 4.5, "W"), PL([(42, 36), (50, 62), (64, 36)], 4.5, "W"),
        L(50, 62, 27, 62, 4.5, "W"), PL([(64, 36), (62, 26), (70, 24)], 4.5, "W"), L(34, 31, 46, 31, 5, "W"),
        L(40, 31, 42, 36, 4.5, "W")]
CAR = [P("M12,64 V54 Q12,49 18,48 L28,45 L39,29 H65 L77,45 L84,47 Q89,48 89,54 V64 Z", "W", "N", 0),
       PG([(43, 34), (53, 34), (53, 45), (35, 45)], "F"), PG([(57, 34), (63, 34), (71, 45), (57, 45)], "F"),
       C(31, 66, 9, "W", "F", 4), C(70, 66, 9, "W", "F", 4)]


def rb_head(a):
    tip = rot([(24, 0)], a + 16, 50, 50)[0]
    b1 = rot([(15, 0)], a, 50, 50)[0]
    b2 = rot([(33, 0)], a, 50, 50)[0]
    return PG([tip, b1, b2], "W")


S = [
    ("parkplatz", "Parkplatz", *VB, vt("P", 50)),
    ("park_and_ride", "Park and Ride", *VB, vt("P+R", 26, 70)),
    ("parkhaus", "Parkhaus / Tiefgarage", *VB, vq(PL([(18, 36), (50, 14), (82, 36)], 6, "W"), T("P", 50, 62, 36, "W"))),
    ("bushaltestelle", "Bushaltestelle", *VB,
     vq(R(24, 18, 52, 56, "W", "N", 0, 9), R(30, 26, 40, 22, "F", "N", 0, 3), C(35, 60, 4.5, "F", "N", 0),
        C(65, 60, 4.5, "F", "N", 0), R(28, 72, 11, 12, "W", "N", 0, 3), R(61, 72, 11, 12, "W", "N", 0, 3))),
    ("haltestelle", "Haltestelle allgemein", *VB, vq(C(50, 50, 32, "W", "N", 0), T("H", 50, 50, 34, "F"))),
    ("bahnhof", "Bahnhof / Haltepunkt", *VB,
     vq(R(27, 13, 46, 58, "W", "N", 0, 13), R(34, 23, 32, 20, "F", "N", 0, 4), C(37, 57, 4.5, "F", "N", 0),
        C(63, 57, 4.5, "F", "N", 0), L(36, 72, 26, 88, 5, "W"), L(64, 72, 74, 88, 5, "W"), L(31, 82, 69, 82, 4, "W"))),
    ("strassenbahn", "Straßenbahn / Stadtbahn", *VB,
     vq(R(27, 30, 46, 44, "W", "N", 0, 8), R(33, 37, 34, 16, "F", "N", 0, 3), C(37, 63, 4, "F", "N", 0),
        C(63, 63, 4, "F", "N", 0), L(50, 30, 50, 18, 4.5, "W"), L(32, 17, 68, 17, 4.5, "W"),
        L(36, 75, 30, 88, 5, "W"), L(64, 75, 70, 88, 5, "W"))),
    ("u_bahn", "U-Bahn", *VB, vt("U", 48)),
    ("s_bahn", "S-Bahn", *VB, vt("S", 48)),
    ("flughafen", "Flughafen / Flugplatz", *VB, vq(*plane(50, 50, 1.05, "W", 45))),
    ("hafen", "Hafen / Anleger", *VB,
     vq(C(50, 24, 7, "N", "W", 5), L(50, 31, 50, 80, 6, "W"), L(34, 44, 66, 44, 6, "W"),
        P("M22,56 Q24,80 50,80 Q76,80 78,56", "N", "W", 6))),
    ("faehre", "Fähre", *VB,
     vq(PG([(14, 56), (86, 56), (74, 74), (26, 74)], "W"), R(32, 38, 36, 19, "W", "N", 0, 2),
        R(45, 24, 10, 15, "W", "N", 0), wave(16, 86, 68, 4, 3, 4, "W"))),
    ("tankstelle", "Tankstelle", *VB,
     vq(R(22, 20, 36, 60, "W", "N", 0, 5), R(28, 27, 24, 17, "F", "N", 0, 2), L(16, 82, 64, 82, 6, "W"),
        P("M58,44 H66 Q74,44 74,52 V68 Q74,74 80,74 V40 L72,30", "N", "W", 4.5))),
    ("fahrradabstellanlage", "Fahrradabstellanlage / Radstation", *VB, vq(*BIKE)),
    ("taxi", "Taxistand", *VB, vt("TAXI", 20, 68)),
    ("carsharing", "Carsharing / Mietwagen", *VB, vq(*CAR)),
    ("bruecke", "Brücke", *VB,
     vq(L(10, 38, 90, 38, 7, "W"), P("M20,76 Q50,22 80,76", "N", "W", 6), L(20, 40, 20, 78, 6, "W"),
        L(80, 40, 80, 78, 6, "W"))),
    ("tunnel", "Tunnel", *VB,
     vq(P("M16,82 V50 A34,34 0 0 1 84,50 V82 Z", "W", "N", 0), P("M32,82 V54 A18,18 0 0 1 68,54 V82 Z", "F", "N", 0))),
    ("kreisverkehr", "Kreisverkehr", *VB,
     vq(C(50, 50, 24, "N", "W", 7, "36 14.27"), rb_head(86), rb_head(206), rb_head(326))),
    ("lichtsignalanlage", "Lichtsignalanlage / Ampel", *VB,
     vq(R(33, 10, 34, 80, "W", "N", 0, 9), C(50, 27, 8.5, "F", "N", 0), C(50, 50, 8.5, "F", "N", 0),
        C(50, 73, 8.5, "F", "N", 0))),
    ("baustelle", "Baustelle", "#F9B000", "#1A1A1A",
     [PG([(50, 8), (94, 88), (6, 88)], "F", "S", 6), R(45.5, 36, 9, 26, "S", "N", 0, 2), C(50, 74, 5.5, "S", "N", 0)]),
    ("bahnuebergang", "Bahnübergang", *VB,
     vq(L(20, 26, 80, 74, 11, "W", "butt"), L(20, 74, 80, 26, 11, "W", "butt"))),
    ("sperrung", "Sperrung / Durchfahrt verboten", "#D0021B", "#8B0000",
     [C(50, 50, 44, "F", "S", 5), R(20, 42, 60, 16, "W", "N", 0, 2)]),
    ("anschlussstelle", "Autobahn-Anschlussstelle", *VB, vt("AS", 36, 60)),
    ("rastanlage", "Rastanlage / Raststätte", *VB,
     vq(R(24, 40, 38, 34, "W", "N", 0, 7), P("M62,46 H69 Q78,46 78,56 Q78,66 69,66 H62", "N", "W", 5),
        L(16, 84, 76, 84, 5, "W"), P("M36,30 q4,-6 0,-12", "N", "W", 4), P("M50,30 q4,-6 0,-12", "N", "W", 4))),
    ("zaehlstelle", "Verkehrszählstelle", *VB,
     vq(R(20, 54, 14, 26, "W", "N", 0), R(43, 36, 14, 44, "W", "N", 0), R(66, 20, 14, 60, "W", "N", 0))),
]
CAT["verkehr"] = S

# =============================== Wasser ===============================
WB = ("#D6ECFA", "#0B5CAD")
S = [
    ("pegel", "Pegel / Wasserstandsmessstelle", *WB,
     [R(38, 8, 24, 84, "F", "S", 5)] + [L(38, y, 50 if i % 2 else 56, y, 4, cap="butt") for i, y in enumerate(range(20, 84, 10))]),
    ("brunnen", "Brunnen", *WB, fr_circle() + [T("B", 50, 50, 40)]),
    ("grundwassermessstelle", "Grundwassermessstelle", *WB, fr_circle() + [PG([(27, 34), (73, 34), (50, 74)], "S")]),
    ("klaeranlage", "Kläranlage", *WB, fr_square() + [T("KA", 50, 50, 32, maxw=60)]),
    ("pumpwerk", "Pumpwerk", *WB, fr_circle() + [PG([(50, 6), (88.1, 72), (11.9, 72)], "N", "S", 5)]),
    ("hochbehaelter", "Hochbehälter / Wasserturm", *WB,
     [L(32, 54, 24, 90, 5), L(68, 54, 76, 90, 5), L(50, 54, 50, 90, 5), R(18, 12, 64, 42, "F", "S", 5, 6),
      wave(26, 30, 48, 4, 2, 4)]),
    ("hydrant_unterflur", "Unterflurhydrant", *WB, fr_circle() + [T("H", 50, 50, 38)]),
    ("hydrant_ueberflur", "Überflurhydrant", *WB, fr_square() + [T("H", 50, 50, 38)]),
    ("schieber", "Schieber / Absperrarmatur", *WB,
     [PG([(12, 34), (50, 58), (12, 82)], "F", "S", 5), PG([(88, 34), (50, 58), (88, 82)], "F", "S", 5),
      L(50, 58, 50, 22, 5), L(34, 20, 66, 20, 6)]),
    ("schacht", "Schacht", *WB, [C(50, 50, 38, "F", "S", 5), L(23, 23, 77, 77, 4.5, cap="butt"), L(23, 77, 77, 23, 4.5, cap="butt")]),
    ("einleitstelle", "Einleitstelle", *WB, arrow(22, 14, 56, 56, 6, 15) + [wave(10, 78, 80, 6, 3, 5)]),
    ("wehr", "Wehr / Querbauwerk", *WB,
     [L(8, 24, 92, 24, 5), L(8, 76, 92, 76, 5), PL([(50, 24), (38, 37), (62, 50), (38, 63), (50, 76)], 5.5)]),
    ("regenrueckhaltebecken", "Regenrückhaltebecken", *WB,
     [PG([(6, 28), (94, 28), (78, 78), (22, 78)], "F", "S", 5), wave(22, 48, 56, 5, 2, 4.5)]),
    ("ueberschwemmungsgebiet", "Überschwemmungsgebiet", *WB, fr_circle() + [T("Ü", 50, 50, 38)]),
    ("wasserschutzgebiet", "Wasserschutzgebiet", *WB, fr_circle() + [T("WSG", 50, 50, 20, maxw=62)]),
    ("trinkwasserentnahme", "Trinkwasserentnahme / Wasserfassung", *WB,
     [P("M50,8 C66,32 80,48 80,62 A30,30 0 0 1 20,62 C20,48 34,32 50,8 Z", "F", "S", 5)]),
    ("niederschlagsmessstelle", "Niederschlagsmessstelle", *WB,
     [P("M28,56 A15,15 0 0 1 31,27 A20,20 0 0 1 69,25 A16,16 0 0 1 74,56 Z", "F", "S", 5),
      L(34, 68, 29, 84, 5), L(52, 68, 47, 84, 5), L(70, 68, 65, 84, 5)]),
]
CAT["wasser"] = S

# =============================== Vermessung ===============================
BK = ("#FFFFFF", "#000000")
S = [
    ("grenzpunkt", "Grenzpunkt, unvermarkt", *BK, [C(50, 50, 24, "F", "S", 5)]),
    ("grenzpunkt_vermarkt", "Grenzpunkt, vermarkt", *BK, [C(50, 50, 24, "F", "S", 5), C(50, 50, 8, "S", "N", 0)]),
    ("trigonometrischer_punkt", "Trigonometrischer Punkt", *BK,
     [PG([(50, 10), (92, 84), (8, 84)], "F", "S", 5), C(50, 59, 7, "S", "N", 0)]),
    ("hoehenfestpunkt", "Höhenfestpunkt", *BK,
     [C(50, 50, 32, "F", "N", 0), P("M18,50 A32,32 0 0 0 82,50 Z", "S", "N", 0), C(50, 50, 32, "N", "S", 5)]),
    ("aufnahmepunkt", "Aufnahmepunkt", *BK,
     [C(50, 50, 26, "F", "S", 5), L(8, 50, 92, 50, 4, cap="butt"), L(50, 8, 50, 92, 4, cap="butt")]),
    ("polygonpunkt", "Polygonpunkt", *BK,
     [C(50, 50, 32, "F", "S", 5), C(50, 50, 17, "N", "S", 4), C(50, 50, 5, "S", "N", 0)]),
    ("passpunkt", "Passpunkt", *BK,
     [C(50, 50, 38, "F", "N", 0), P("M50,50 L50,12 A38,38 0 0 1 88,50 Z", "S", "N", 0),
      P("M50,50 L50,88 A38,38 0 0 1 12,50 Z", "S", "N", 0), C(50, 50, 38, "N", "S", 5)]),
    ("gnss_referenzpunkt", "GNSS-Referenzpunkt", *BK,
     [PG([(50, 46), (78, 90), (22, 90)], "F", "S", 5), C(50, 74, 5, "S", "N", 0),
      P("M34,32 A20,20 0 0 1 66,32", "N", "S", 4.5), P("M22,22 A36,36 0 0 1 78,22", "N", "S", 4.5)]),
    ("bohrpunkt", "Bohrpunkt / Aufschluss", *BK,
     [C(50, 50, 36, "F", "N", 0), P("M50,14 A36,36 0 0 0 50,86 Z", "S", "N", 0), C(50, 50, 36, "N", "S", 5)]),
    ("nordpfeil", "Nordpfeil", *BK,
     [PG([(50, 4), (72, 66), (50, 54)], "S", "S", 3), PG([(50, 4), (28, 66), (50, 54)], "F", "S", 3), T("N", 50, 84, 20)]),
    ("messpunkt", "Messpunkt", *BK, cross(50, 50, 34, 5) + [C(50, 50, 14, "N", "S", 4)]),
    ("fotostandort", "Fotostandort", *BK,
     [R(34, 20, 24, 14, "S", "N", 0, 3), R(10, 30, 80, 52, "F", "S", 5, 8), C(50, 56, 15, "N", "S", 5),
      C(50, 56, 5, "S", "N", 0)]),
]
CAT["vermessung"] = S

# =============================== Allgemein ===============================
AG = ("#FFFFFF", "#333333")
RD = ("#FFFFFF", "#C8102E")
PB = ("#FFFFFF", "#1F4E9E")


def aq(*sh):
    return fr_square() + list(sh)


S = [
    ("rathaus", "Rathaus / Verwaltung", *AG,
     aq(PG([(50, 16), (84, 38), (16, 38)], "S"), *[R(x, 42, 8, 28, "S", "N", 0) for x in (24, 39, 53, 68)],
        R(18, 74, 64, 9, "S", "N", 0))),
    ("schule", "Schule / Bildung", *AG,
     aq(P("M50,34 Q34,22 16,28 V72 Q34,66 50,78 Q66,66 84,72 V28 Q66,22 50,34 Z", "N", "S", 5), L(50, 34, 50, 78, 4.5))),
    ("kindertagesstaette", "Kindertagesstätte", *AG, aq(T("Kita", 50, 50, 24, maxw=66))),
    ("krankenhaus", "Krankenhaus / Gesundheit", *RD,
     aq(R(40, 20, 20, 60, "S", "N", 0, 2), R(20, 40, 60, 20, "S", "N", 0, 2))),
    ("feuerwehr", "Feuerwehr", *RD,
     aq(P("M52,14 C56,30 74,40 74,60 C74,76 63,86 50,86 C37,86 26,76 26,62 C26,50 34,44 38,34 C42,42 44,44 48,44 "
          "C46,34 46,24 52,14 Z", "S", "N", 0),
        P("M50,58 C56,64 60,68 60,74 C60,80 56,84 50,84 C44,84 40,80 40,74 C40,68 46,66 50,58 Z", "W", "N", 0))),
    ("polizei", "Polizei", *PB,
     aq(P("M50,14 L80,24 V50 C80,68 66,80 50,88 C34,80 20,68 20,50 V24 Z", "N", "S", 5), PG(star(50, 50, 17, 7, 5), "S"))),
    ("kirche", "Kirche / Sakralbau", *AG, aq(R(44, 16, 12, 68, "S", "N", 0), R(27, 33, 46, 12, "S", "N", 0))),
    ("information", "Information", *PB, fr_circle() + [C(50, 27, 7, "S", "N", 0), R(43, 40, 14, 38, "S", "N", 0, 3)]),
    ("einkauf", "Einkauf / Nahversorgung", *AG,
     aq(PL([(14, 24), (26, 24), (36, 60), (74, 60), (82, 34), (29, 34)], 5), C(42, 74, 6, "S", "N", 0),
        C(68, 74, 6, "S", "N", 0))),
    ("gastronomie", "Gastronomie", *AG,
     aq(L(34, 20, 34, 82, 5), L(25, 20, 25, 38, 4), L(43, 20, 43, 38, 4), P("M25,38 Q34,50 43,38", "N", "S", 4),
        P("M62,18 Q76,30 74,54 H62 Z", "S", "S", 3), L(64, 54, 64, 82, 5))),
    ("hotel", "Hotel / Unterkunft", *AG,
     aq(L(16, 28, 16, 76, 6), L(16, 64, 84, 64, 6), L(84, 52, 84, 76, 6), C(30, 48, 8, "S", "N", 0),
        R(42, 44, 42, 14, "S", "N", 0, 5))),
    ("sportanlage", "Sportanlage", *AG,
     aq(R(16, 28, 68, 44, "N", "S", 5, 22), L(50, 28, 50, 72, 4), C(50, 50, 8, "N", "S", 4))),
    ("campingplatz", "Campingplatz", *AG,
     aq(PG([(50, 22), (84, 78), (16, 78)], "N", "S", 5), PG([(50, 50), (62, 78), (38, 78)], "S"),
        L(50, 22, 44, 14, 4), L(50, 22, 56, 14, 4))),
    ("denkmal", "Denkmal / Kulturdenkmal", *AG,
     aq(PG([(43, 28), (57, 28), (61, 72), (39, 72)], "S"), PG([(43, 28), (50, 14), (57, 28)], "S"),
        R(28, 74, 44, 10, "S", "N", 0))),
    ("aussichtsturm", "Aussichtsturm", *AG,
     aq(L(38, 84, 44, 40, 5), L(62, 84, 56, 40, 5), L(40, 70, 59, 56, 3.5), L(60, 70, 41, 56, 3.5),
        R(30, 30, 40, 10, "S", "N", 0), PG([(30, 26), (50, 12), (70, 26)], "S"))),
    ("museum", "Museum / Kultur", *AG, aq(T("M", 50, 50, 42))),
    ("toilette", "Öffentliche Toilette", *PB, aq(T("WC", 50, 50, 30, maxw=64))),
    ("wertstoffhof", "Wertstoffhof / Entsorgung", *AG,
     aq(PG([(26, 36), (74, 36), (68, 82), (32, 82)], "N", "S", 5), L(18, 30, 82, 30, 6), L(42, 22, 58, 22, 6),
        L(42, 46, 44, 72, 4), L(58, 46, 56, 72, 4))),
    ("funkmast", "Funkmast / Sendeanlage", *AG,
     [L(50, 40, 50, 92, 5), L(50, 60, 34, 92, 3.5), L(50, 60, 66, 92, 3.5), C(50, 34, 6, "S", "N", 0),
      P("M34,48 A22,22 0 0 1 34,20", "N", "S", 4.5), P("M66,48 A22,22 0 0 0 66,20", "N", "S", 4.5),
      P("M23,58 A36,36 0 0 1 23,10", "N", "S", 4.5), P("M77,58 A36,36 0 0 0 77,10", "N", "S", 4.5)]),
]
CAT["allgemein"] = S
