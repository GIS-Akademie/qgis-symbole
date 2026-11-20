"""Sammlung Gruenflaechen und Friedhof: Baumkataster, Ausstattung, Spielgeraete, Friedhof, Pflege.
Orientierung: kommunale Gruenflaechen-, Baum-, Spielplatz- und Friedhofskataster. Kein einheitliches Regelwerk
fuer die Darstellung; eigene Entwuerfe. Flaecheninhalte in Anlehnung an die ueblichen Objektarten der
Gruenflaechenpflege (Rasen, Wiese, Beete, Gehoelze, Belaege), Pflegeklassen 1 (intensiv) bis 4 (extensiv).
Stil: helle Maigruenfuellung, dunkelgruener Strich 5. Die Form zeigt die Gruppe:
  Baumkrone in Draufsicht = Baumkataster (bk_), Quadrat = Ausstattung (aus_), Kreis = Spiel- und Sportgeraet
  (spiel_), Sechseck = Friedhof (fh_), Raute = Pflege und Kontrolle (pfl_).
Baumkataster (Praefix bk_, Titel "Baumkataster ..."): Baumkrone mit Zeichen in der Mitte. Vitalitaetsstufen 0 bis 3
nach Roloff (einzige Farbausnahme bei den Punkten: Kronenfarbe gruen, gelb, orange, rot), Massnahmen in Anlehnung
an die Leistungen der ZTV-Baumpflege (FLL), Wurzelschutzbereich nach DIN 18920 (Kronentraufe zuzueglich 1,5 m).
Die Regelwerke selbst lagen nicht vor.
Linien und Flaechen: gruen = Vegetation, braun und grau = Wege und Belaege, blau = Wasser; Grabfelder ueber das
Muster unterschieden, Belegung der Graeber ueber die Fuellung (einzige Farbausnahme: orange = Nutzungsrecht
laeuft ab).
Allgemeine Zeichen fuer Park, Spielplatz und Friedhof als Ort stehen in Allgemein und Topografie, Pflanzungen und
Baeume der Planung in Landschaftsplanung.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "gruenflaechen"
NAME = "Grünflächen und Friedhof"
DESC = ("Symbole für Grünflächen-, Baum-, Spielplatz- und Friedhofskataster: Baumkataster (Vitalität, Zustand, "
        "Baumpflege), Ausstattung, Spiel- und Sportgeräte, Grabarten und Friedhofseinrichtungen, Pflege und "
        "Kontrolle, Flächeninhalte, Pflegeklassen, Grabfelder und Grabbelegung")
TAGS = ("gruenflaechen, gruenflaechenkataster, baumkataster, baum, spielplatz, spielgeraet, friedhof, grab, "
        "gruenpflege, stadtgruen")

GF = ("#E4F2B4", "#557A0A")
BR = ("#E8D5B5", "#6B4423")


def au(*sh):  # Ausstattung
    return fr_square() + list(sh)


def sp(*sh):  # Spiel- und Sportgeraet
    return fr_circle() + list(sh)


def fh(*sh):  # Friedhof
    return fr_hex() + list(sh)


def pf(*sh):  # Pflege und Kontrolle
    return fr_diamond() + list(sh)


def dot(x, y, r=3.5):
    return C(x, y, r, "S", "N", 0)


def tuft(x, y, k=1.0, sw=4):
    return [L(x, y, x, y - 18 * k, sw), L(x, y, x - 10 * k, y - 13 * k, sw), L(x, y, x + 10 * k, y - 13 * k, sw)]


def stein(*sh):  # Grabstein mit Zeichen
    return fh(P("M32,76 V40 A18,18 0 0 1 68,40 V76 Z", "F", "S", 5), L(24, 76, 76, 76, 5), *sh)


def grab(txt):
    return stein(T(txt, 50, 54, 22))


# Baumkataster: Vitalitaetsstufen 0 bis 3 nach Roloff (Kronenstruktur), wie sie die Baumkontrolle nutzt.
VITAL = [("vital, Explorationsphase", "#9AD67A"), ("geschwächt, Degenerationsphase", "#E6E273"),
         ("merklich geschädigt, Stagnationsphase", "#F4B052"), ("stark geschädigt, Resignationsphase", "#E3705F")]

BANK = [L(22, 40, 78, 40, 5), L(22, 56, 78, 56, 6), L(30, 56, 30, 76, 5), L(70, 56, 70, 76, 5)]
TISCH = [L(26, 42, 74, 42, 6), L(36, 42, 26, 76, 5), L(64, 42, 74, 76, 5), L(14, 60, 34, 60, 5), L(66, 60, 86, 60, 5)]
TONNE = [PL([(31, 36), (36, 80), (64, 80), (69, 36)], 5), L(26, 32, 74, 32, 6), L(44, 22, 56, 22, 5),
         L(44, 46, 46, 70, 3.5), L(56, 46, 54, 70, 3.5)]
PFOTE = [E(50, 60, 13, 11, "S", "N", 0)] + [C(x, y, 5.5, "S", "N", 0) for x, y in ((30, 46), (42, 34), (58, 34), (70, 46))]
LEUCHTE = [L(50, 86, 50, 40, 5), C(50, 28, 11, "F", "S", 4.5)]
HAHN = [L(26, 38, 62, 38, 6.5), L(62, 38, 62, 52, 6.5), L(42, 24, 42, 38, 5), L(32, 24, 52, 24, 5)]
SPROSS = [L(50, 84, 50, 44, 5.5), P("M50,66 Q30,64 26,46 Q46,48 50,66 Z", "S", "N", 0),
          P("M50,54 Q70,52 74,34 Q54,36 50,54 Z", "S", "N", 0)]
FONTAENE = [P("M20,58 Q50,90 80,58 Z", "F", "S", 5), L(50, 58, 50, 34, 4.5), P("M50,36 Q38,18 28,42", "N", "S", 4.5),
            P("M50,36 Q62,18 72,42", "N", "S", 4.5)]
STUFEN = [PL([(22, 76), (22, 62), (36, 62), (36, 50), (50, 50), (50, 38), (64, 38), (64, 26), (78, 26)], 5)]
URNE = [P("M37,40 Q26,62 42,78 H58 Q74,62 63,40 Z", "F", "S", 5), L(34, 36, 66, 36, 5.5), C(50, 27, 4.5, "S", "N", 0)]
KANNE = [R(30, 42, 30, 30, "F", "S", 5, 3), L(60, 54, 82, 34, 5), L(76, 28, 88, 40, 5),
         P("M30,48 Q14,58 30,68", "N", "S", 4.5)]
SCHNEE = ([L(*pt(50, 50, 34, a), *pt(50, 50, 34, a + 180), 5.5) for a in (0, 60, 120)]
          + [L(*pt(50, 50, 20, a), *pt(50, 50, 32, a + d), 4.5) for a in range(0, 360, 60) for d in (-24, 24)])
HERZ = [P("M50,70 C30,54 36,38 50,48 C64,38 70,54 50,70 Z", "S", "N", 0)]

S = [
    # ---- Baumkataster (Draufsicht): Vitalitaetsstufen nach Roloff, Zustand, Massnahmen der Baumpflege ----
    ("bk_baum", "Baumkataster Baum", *GF, treetop(50, 50, 41) + [dot(50, 50, 6)]),
    *[(f"bk_vital_{i}", f"Baumkataster Vitalitätsstufe {i} ({t})", c, GF[1], treetop(50, 50, 41) + [T(str(i), 50, 50, 34)])
      for i, (t, c) in enumerate(VITAL)],
    ("bk_jungbaum", "Baumkataster Jungbaum (mit Dreibock)", *GF,
     treetop(50, 50, 21, k=6) + [dot(50, 50, 5)] + [C(x, y, 6, "N", "S", 4) for x, y in regpoly(50, 52, 38, 3)]),
    ("bk_totbaum", "Baumkataster abgestorbener Baum", *GF,
     [C(50, 50, 43, "N", "S", 3.5, "8 7")] + [L(50, 50, *pt(50, 50, 32, a), 5) for a in range(0, 360, 60)]
     + [L(*pt(50, 50, 19, a), *pt(50, 50, 31, a + 28), 4) for a in range(0, 360, 60)]),
    ("bk_stubben", "Baumkataster Stubben / Baumstumpf", *GF,
     [C(50, 50, 28, "F", "S", 5), C(50, 50, 16, "N", "S", 3.5), dot(50, 50, 5)]),
    ("bk_leerstandort", "Baumkataster freier Baumstandort / leere Baumscheibe", *GF,
     [R(12, 12, 76, 76, "N", "S", 4.5, 6), C(50, 50, 23, "N", "S", 4, "8 7")]),
    ("bk_kontrolle", "Baumkataster Regelkontrolle fällig", *GF, treetop(50, 50, 41) + [PL([(30, 52), (44, 66), (70, 34)], 7)]),
    ("bk_untersuchung", "Baumkataster eingehende Untersuchung erforderlich", *GF,
     treetop(50, 50, 41) + [C(45, 45, 13, "N", "S", 5), L(55, 55, 70, 70, 7)]),
    ("bk_gefahr", "Baumkataster Verkehrssicherheit gefährdet / Sofortmaßnahme", *GF,
     treetop(50, 50, 41) + [T("!", 50, 50, 40)]),
    ("bk_schaden", "Baumkataster Schaden (Höhlung, Riss, Faulstelle)", *GF, treetop(50, 50, 41) + lightning(50, 50, 0.8)),
    ("bk_schaedling", "Baumkataster Schädlings- oder Pilzbefall", *GF,
     treetop(50, 50, 41) + [E(50, 54, 10, 14, "S", "N", 0), C(50, 35, 6, "S", "N", 0)]
     + [L(50, y, 50 + d, y - 6, 3.5) for y in (48, 55, 62) for d in (-21, 21)]),
    ("bk_naturdenkmal", "Baumkataster Naturdenkmal / geschützter Baum", *GF,
     treetop(50, 50, 41) + [PG(star(50, 51, 24, 10, 5), "S")]),
    ("bk_kronenpflege", "Baumkataster Maßnahme Kronenpflege / Kronenschnitt", *GF,
     treetop(50, 50, 41) + [L(37, 26, 59, 62, 4.5), L(63, 26, 41, 62, 4.5), C(62, 69, 7, "N", "S", 4), C(38, 69, 7, "N", "S", 4)]),
    ("bk_kroneneinkuerzung", "Baumkataster Maßnahme Kroneneinkürzung", *GF,
     [C(50, 50, 44, "N", "S", 3.5, "8 7")] + treetop(50, 50, 27) + [dot(50, 50, 6)]),
    ("bk_totholz", "Baumkataster Maßnahme Totholzbeseitigung", *GF,
     treetop(50, 50, 41) + [L(30, 68, 68, 32, 5.5), L(46, 53, 44, 32, 4.5), L(57, 42, 72, 50, 4.5)]),
    ("bk_kronensicherung", "Baumkataster Maßnahme Kronensicherung", *GF,
     treetop(50, 50, 41) + [PL([(32, 40), (68, 40), (50, 68)], 4, close=True), dot(32, 40, 6), dot(68, 40, 6), dot(50, 68, 6)]),
    ("bk_lichtraum", "Baumkataster Maßnahme Lichtraumprofil herstellen", *GF,
     treetop(50, 50, 41) + [R(30, 32, 40, 36, "N", "S", 4.5, 0, "8 6"), *arrow(50, 78, 50, 46, 4.5, 11)]),
    ("bk_bewaesserung", "Baumkataster Maßnahme Bewässerung", *GF, treetop(50, 50, 41) + fit(drop("S", "N", 0), 50, 50, 0.5)),
    ("bk_faellung", "Baumkataster Maßnahme Fällung", *GF, treetop(50, 50, 41) + xcross(50, 50, 22, 7)),
    ("bk_nachpflanzung", "Baumkataster Maßnahme Nachpflanzung", *GF, treetop(50, 50, 41) + cross(50, 50, 22, 7)),
    # ---- Ausstattung (Quadrat) ----
    ("aus_bank", "Sitzbank", *GF, au(*fit(BANK, 50, 50, 0.92))),
    ("aus_tisch", "Picknicktisch / Bank-Tisch-Kombination", *GF, au(*fit(TISCH, 50, 50, 0.84))),
    ("aus_abfall", "Abfallbehälter", *GF, au(*fit(TONNE, 50, 50, 0.9))),
    ("aus_hundekot", "Hundekotbeutelspender", *GF, au(R(24, 16, 52, 68, "N", "S", 5, 5), *fit(PFOTE, 50, 50, 0.6))),
    ("aus_leuchte", "Leuchte", *GF,
     au(*fit(LEUCHTE, 50, 56, 0.86), *[L(*pt(50, 32, 15, a), *pt(50, 32, 23, a), 4.5) for a in (-90, -45, 0, 45, 90)])),
    ("aus_tor", "Tor / Zugang", *GF,
     au(L(20, 22, 20, 80, 6.5), L(80, 22, 80, 80, 6.5), R(24, 36, 24, 40, "N", "S", 4.5), R(52, 36, 24, 40, "N", "S", 4.5),
        L(24, 36, 48, 76, 3.5), L(76, 36, 52, 76, 3.5))),
    ("aus_schild", "Hinweisschild / Parkordnung", *GF,
     au(R(24, 18, 52, 38, "F", "S", 5, 3), T("i", 50, 37, 24), L(50, 56, 50, 82, 5.5))),
    ("aus_wasser", "Wasserentnahmestelle / Zapfstelle", *GF, au(*HAHN, *fit(drop("S", "N", 0), 62, 70, 0.26))),
    ("aus_pflanzkuebel", "Pflanzkübel / Hochbeet", *GF,
     au(PG([(26, 58), (74, 58), (67, 82), (33, 82)], "F", "S", 5), *fit(SPROSS, 50, 32, 0.56))),
    ("aus_poller", "Poller / Absperrpfosten", *GF, au(R(42, 24, 16, 52, "S", "N", 0, 7), L(24, 78, 76, 78, 5))),
    ("aus_brunnen", "Zierbrunnen / Wasserbecken", *GF, au(*fit(FONTAENE, 50, 46, 0.9))),
    ("aus_treppe", "Treppe / Rampe", *GF, au(*fit(STUFEN, 50, 50, 0.9))),
    ("aus_steg", "Steg / Brücke", *GF, au(L(16, 44, 84, 44, 6.5), P("M24,76 Q50,40 76,76", "N", "S", 5))),
    ("aus_pavillon", "Pavillon / Unterstand", *GF,
     au(PG([(50, 18), (84, 44), (16, 44)], "S"), L(26, 44, 26, 80, 5), L(74, 44, 74, 80, 5), L(20, 80, 80, 80, 5))),
    ("aus_hundewiese", "Hundewiese / Hundeauslauf", *GF, au(*fit(PFOTE, 50, 46, 0.86))),
    # ---- Spiel- und Sportgeraete (Kreis) ----
    ("spiel_schaukel", "Schaukel", *GF,
     sp(L(28, 26, 72, 26, 5.5), L(28, 26, 22, 76, 5), L(72, 26, 78, 76, 5), L(42, 26, 42, 58, 3.5), L(58, 26, 58, 58, 3.5),
        L(39, 60, 61, 60, 6))),
    ("spiel_rutsche", "Rutsche", *GF,
     sp(L(28, 78, 28, 28, 5), L(40, 78, 40, 28, 5), *[L(28, y, 40, y, 3.5) for y in (42, 54, 66)],
        P("M40,30 Q58,34 64,56 T82,72", "N", "S", 6))),
    ("spiel_klettergeruest", "Klettergerüst", *GF,
     sp(R(26, 26, 48, 48, "N", "S", 5), L(50, 26, 50, 74, 4), L(26, 50, 74, 50, 4), L(26, 26, 74, 74, 3.5))),
    ("spiel_kletternetz", "Kletternetz / Seilpyramide", *GF,
     sp(PL([(50, 18), (80, 76), (20, 76)], 5, close=True), L(50, 18, 50, 76, 3.5), L(35, 47, 65, 47, 3.5), L(27, 62, 73, 62, 3.5))),
    ("spiel_sandkasten", "Sandkasten / Sandspielfläche", *GF,
     sp(R(22, 32, 56, 38, "N", "S", 5.5), *[dot(x, y, 3) for x, y in ((34, 44), (50, 40), (66, 46), (42, 58), (60, 60))])),
    ("spiel_wippe", "Wippe", *GF, sp(L(20, 40, 80, 60, 6.5), PG([(50, 51), (38, 76), (62, 76)], "S"))),
    ("spiel_karussell", "Karussell / Drehgerät", *GF,
     sp(C(50, 50, 24, "N", "S", 5), *[L(50, 50, *pt(50, 50, 24, a), 4.5) for a in (0, 120, 240)], dot(50, 50, 7))),
    ("spiel_seilbahn", "Seilbahn", *GF,
     sp(L(20, 30, 20, 76, 5), L(80, 40, 80, 76, 5), L(20, 30, 80, 40, 4), L(52, 36, 52, 58, 3.5), C(52, 65, 7, "S", "N", 0))),
    ("spiel_federtier", "Federwipper / Wipptier", *GF,
     sp(E(50, 34, 20, 10, "S", "N", 0), PL([(50, 44), (60, 50), (40, 58), (60, 66), (40, 74), (50, 80)], 4.5), L(34, 80, 66, 80, 5))),
    ("spiel_wasser", "Wasserspiel / Matschanlage", *GF,
     sp(*fit(HAHN, 44, 42, 0.7), wave(24, 70, 52, 5, 2, 5), *fit(drop("S", "N", 0), 53, 56, 0.16))),
    ("spiel_balancieren", "Balancierstrecke", *GF,
     sp(L(18, 56, 82, 56, 7), L(30, 56, 30, 74, 5), L(70, 56, 70, 74, 5), *fit(person(), 50, 34, 0.38))),
    ("spiel_haus", "Spielhaus / Spielturm", *GF, sp(*fit(house(), 50, 50, 0.76))),
    ("spiel_tor", "Bolzplatztor", *GF,
     sp(PL([(24, 72), (24, 34), (76, 34), (76, 72)], 6), *[L(x, 34, x, 72, 2.5) for x in (37, 50, 63)],
        L(24, 47, 76, 47, 2.5), L(24, 60, 76, 60, 2.5))),
    ("spiel_basketball", "Basketballkorb / Streetball", *GF,
     sp(R(32, 20, 36, 26, "N", "S", 5), E(50, 52, 13, 4.5, "N", "S", 4.5), L(38, 54, 43, 74, 3.5), L(62, 54, 57, 74, 3.5),
        L(50, 56, 50, 76, 3.5))),
    ("spiel_tischtennis", "Tischtennisplatte", *GF,
     sp(L(18, 50, 82, 50, 6.5), L(50, 36, 50, 50, 4.5), L(30, 50, 30, 74, 5), L(70, 50, 70, 74, 5), dot(66, 34, 5))),
    ("spiel_fitness", "Fitnessgerät / Calisthenics", *GF,
     sp(L(28, 24, 28, 78, 5.5), L(72, 24, 72, 78, 5.5), L(28, 32, 72, 32, 6), L(28, 56, 50, 56, 5), L(50, 56, 50, 78, 5.5))),
    # ---- Friedhof (Sechseck) ----
    ("fh_wahlgrab", "Wahlgrab", *GF, grab("W")),
    ("fh_reihengrab", "Reihengrab", *GF, grab("R")),
    ("fh_anonym", "Anonymes Grab / anonymes Grabfeld", *GF, grab("A")),
    ("fh_urnengrab", "Urnengrab", *GF, fh(*fit(URNE, 50, 50, 0.9))),
    ("fh_urnengemeinschaft", "Urnengemeinschaftsanlage", *GF,
     fh(*fit(URNE, 50, 36, 0.48), *fit(URNE, 32, 62, 0.48), *fit(URNE, 68, 62, 0.48))),
    ("fh_kolumbarium", "Kolumbarium / Urnenwand", *GF,
     fh(R(24, 28, 52, 44, "F", "S", 5), L(41.5, 28, 41.5, 72, 4), L(58.5, 28, 58.5, 72, 4), L(24, 50, 76, 50, 4))),
    ("fh_baumgrab", "Baumbestattung / Baumgrab", *GF,
     fh(*fit(tree_side(), 50, 44, 0.66), L(26, 76, 74, 76, 4.5), dot(34, 68, 4), dot(66, 68, 4))),
    ("fh_rasengrab", "Rasengrab", *GF, fh(R(32, 30, 36, 22, "F", "S", 5, 2), *tuft(30, 78, 0.8), *tuft(50, 78, 0.8), *tuft(70, 78, 0.8))),
    ("fh_kindergrab", "Kindergrab", *GF, stein(*fit(HERZ, 50, 55, 0.7))),
    ("fh_ehrengrab", "Ehrengrab", *GF, stein(PG(star(50, 53, 13, 5.5, 5), "S"))),
    ("fh_kriegsgrab", "Kriegsgräberstätte", *GF, fh(L(50, 22, 50, 80, 8, cap="butt"), L(30, 40, 70, 40, 8, cap="butt"))),
    ("fh_gruft", "Gruft / Mausoleum", *GF,
     fh(PG([(50, 20), (78, 40), (22, 40)], "S"), *[L(x, 44, x, 74, 5.5) for x in (32, 44, 56, 68)], L(24, 78, 76, 78, 5))),
    ("fh_standsicherheit", "Grabmal nicht standsicher", *GF,
     fh(*fit([P("M32,76 V40 A18,18 0 0 1 68,40 V76 Z", "F", "S", 5)], 54, 52, 0.9, 20), L(24, 78, 76, 78, 5))),
    ("fh_trauerhalle", "Trauerhalle / Feierhalle", *GF,
     fh(*fit(house(), 50, 50, 0.72), P("M44,73 V62 A6,6 0 0 1 56,62 V73", "N", "S", 4))),
    ("fh_wasserstelle", "Wasserstelle / Gießkannenständer", *GF, fh(*fit(KANNE, 48, 50, 0.76))),
    ("fh_abfall", "Abfallsammelstelle / Kompost", *GF, fh(*fit(TONNE, 50, 50, 0.76))),
    # ---- Pflege und Kontrolle (Raute) ----
    ("pfl_mahd", "Mahd", *GF, pf(*tuft(38, 56, 0.9), *tuft(62, 56, 0.9), L(28, 66, 72, 66, 4.5))),
    ("pfl_schnitt", "Gehölzschnitt / Heckenschnitt", *GF,
     pf(L(38, 30, 58, 62, 4.5), L(62, 30, 42, 62, 4.5), C(61, 68, 6, "N", "S", 4), C(39, 68, 6, "N", "S", 4))),
    ("pfl_pflanzung", "Pflanzung / Nachpflanzung", *GF, pf(*fit(SPROSS, 44, 50, 0.6), *cross(66, 40, 7, 4.5))),
    ("pfl_bewaesserung", "Bewässerung", *GF, pf(*fit(drop("S", "N", 0), 50, 50, 0.52))),
    ("pfl_reinigung", "Reinigung / Laubbeseitigung", *GF,
     pf(L(64, 26, 48, 54, 5), PG([(36, 56), (58, 52), (62, 72), (30, 72)], "S"))),
    ("pfl_wildkraut", "Wildkrautbeseitigung", *GF, pf(*tuft(50, 66, 1.5, 4.5), L(30, 70, 70, 30, 5))),
    ("pfl_winterdienst", "Winterdienst", *GF, pf(*fit(SCHNEE, 50, 50, 0.64))),
    ("pfl_kontrolle", "Kontrolle fällig (Spielgerät, Ausstattung, Grabmal)", *GF, pf(PL([(30, 52), (44, 66), (70, 34)], 7))),
    ("pfl_schaden", "Schaden / Mangel", *GF, pf(T("!", 50, 50, 38))),
    ("pfl_gesperrt", "Gesperrt / außer Betrieb", *GF, pf(*xcross(50, 50, 17, 7))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
G0, GL, W0, GRAU, BLAU, WS = GF[1], GF[0], BR[1], "#6B6B6B", "#0B5CAD", "#FFFFFF"
PFLEGE = [("1 (intensiv)", "#3E8E2F"), ("2", "#7DB85A"), ("3", "#B9DA8F"), ("4 (extensiv)", "#E6F2CC")]

LINIEN = [
    ("Weg, wassergebundene Decke", [linie(W0, 1.5), linie(BR[0], 1.1)]),
    ("Weg, befestigt", [linie(GRAU, 1.5), linie("#E6E6E6", 1.1)]),
    ("Trampelpfad", [linie(W0, 0.4, [1.5, 1])]),
    ("Hecke, geschnitten", [linie(G0, 1.5), linie(GL, 1.0)]),
    ("Hecke, frei wachsend", [marken(mk("circle", 2.0, GL, G0, 0.25), 1.7)]),
    ("Zaun", [linie(GRAU, 0.3), marken(mk("cross2", 1.2, GRAU, rw=0.25), 4)]),
    ("Mauer", [linie(GRAU, 0.9)]),
    ("Einfassung / Bordkante", [linie(GRAU, 0.4)]),
    ("Rasenkante / Mähkante", [linie(G0, 0.3, [2, 1])]),
    ("Bewässerungsleitung", [linie(BLAU, 0.4, [4, 1, 0.5, 1])]),
    ("Grenze Pflegebezirk", [linie(G0, 0.7, [6, 1.5, 1, 1.5])]),
    ("Grenze Pflegeeinheit", [linie(G0, 0.4, [3, 1.5])]),
    ("Baumschutzzaun", [linie(G0, 0.4), marken(mk("line", 1.6, G0, rw=0.3), 3)]),
    ("Friedhofsmauer / Einfriedung", [linie(GRAU, 0.9), marken(mk("line", 0.9, WS, rw=0.25), 1.8)]),
    ("Grenze Grabfeld", [linie(G0, 0.5, [4, 1])]),
    ("Grabreihe", [linie(G0, 0.3), marken(mk("square", 1.0, GL, G0, 0.2), 2)]),
]


def feld(m, dx=3.0):  # Grabfeld: heller Grund, Art ueber das Muster
    return [voll(GL + "99"), muster(m, dx, versatz=dx / 2), linie(G0, 0.4)]


FLAECHEN = [
    ("Gebrauchsrasen", [voll("#CDEBB0"), linie(G0, 0.3)]),
    ("Landschaftsrasen / Wiese", [voll("#DDF0C8"), muster(mk("line", 1.0, G0, rw=0.25), 2.4, 3.0, versatz=1.2), linie(G0, 0.3)]),
    ("Blumenwiese", [voll("#DDF0C8"), muster(mk("cross2", 0.9, G0, rw=0.2), 2.6, versatz=1.3), linie(G0, 0.3)]),
    ("Wechselflor / Schmuckbeet", [voll(GL), muster(mk("diamond", 1.0, G0), 2.2, versatz=1.1), linie(G0, 0.3)]),
    ("Staudenfläche", [voll(GL), muster(mk("circle", 0.7, G0), 2.0, versatz=1.0), linie(G0, 0.3)]),
    ("Bodendecker", [voll(GL), schraffur(G0, 0.15, 45, 1.2), linie(G0, 0.3)]),
    ("Strauchfläche", [voll("#B9DDA0"), muster(mk("circle", 1.6, None, G0, 0.25), 2.6, versatz=1.3), linie(G0, 0.3)]),
    ("Hecke", [voll("#A3CF8E"), schraffur(G0, 0.2, 135, 1.5), linie(G0, 0.3)]),
    ("Baumbestand, waldartig", [voll("#A3CF8E"), muster(mk("circle", 2.2, None, G0, 0.3), 3.8, versatz=1.9), linie(G0, 0.3)]),
    ("Wasserfläche", [voll("#B5DCF5"), linie(BLAU, 0.3)]),
    ("Wegefläche, wassergebunden", [voll(BR[0]), linie(W0, 0.3)]),
    ("Wegefläche, befestigt", [voll("#E6E6E6"), linie(GRAU, 0.3)]),
    ("Spielsand / Fallschutz", [voll("#F5E8B8"), muster(mk("circle", 0.4, W0), 1.6, versatz=0.8), linie(W0, 0.3)]),
    ("Sportrasen", [voll("#B5DD98"), schraffur(G0, 0.15, 90, 3), linie(G0, 0.4)]),
    ("Tennenfläche", [voll("#D99A77"), linie(W0, 0.3)]),
    ("Kunststoffbelag", [voll("#C96A55"), linie(W0, 0.3)]),
    ("Hundewiese", [voll("#DDF0C8"), linie(G0, 0.5, [3, 1, 0.5, 1])]),
    ("Spielplatzfläche", [band(G0 + "59", 1.5), linie(G0, 0.4)]),
] + [(f"Pflegeklasse {t}", [voll(c), linie(G0, 0.3)]) for t, c in PFLEGE] + [
    ("Kronentraufbereich", [voll(GL + "80"), linie(G0, 0.3, [0.5, 1])]),
    ("Wurzelschutzbereich (Kronentraufe zuzüglich 1,5 m)", [schraffur(G0, 0.15, 45, 2), linie(G0, 0.5, [3, 1, 0.5, 1])]),
    ("Baumscheibe", [voll(BR[0]), linie(W0, 0.3)]),
    ("Grabfeld Wahlgräber", feld(mk("square", 1.3, None, G0, 0.25))),
    ("Grabfeld Reihengräber", feld(mk("line", 1.4, G0, rw=0.3), 2.2)),
    ("Grabfeld Urnengräber", feld(mk("circle", 1.0, G0), 2.4)),
    ("Grabfeld Rasengräber", [voll("#CDEBB0"), muster(mk("line", 1.2, G0, rw=0.3, winkel=90), 3.0, versatz=1.5), linie(G0, 0.4)]),
    ("Grabfeld Baumbestattung", feld(mk("circle", 2.0, None, G0, 0.3), 3.6)),
    ("Grabfeld anonym", feld(mk("circle", 0.45, G0), 1.8)),
    ("Kriegsgräberfeld", feld(mk("cross", 1.5, G0, rw=0.3), 3.0)),
    ("Grabfeld, abgeräumt", [schraffur(GRAU, 0.15, 45, 2.5), linie(GRAU, 0.4, [3, 1.5])]),
    ("Erweiterungsfläche Friedhof", [schraffur(G0, 0.2, 45, 3), linie(G0, 0.5, [3, 1.5])]),
    ("Grab, belegt", [voll("#7DB85A"), linie(G0, 0.3)]),
    ("Grab, frei", [voll(WS), linie(G0, 0.3)]),
    ("Grab, reserviert", [voll(WS), schraffur(G0, 0.2, 45, 1.2), linie(G0, 0.3)]),
    ("Grab, Nutzungsrecht läuft ab", [voll("#F4B052"), linie(G0, 0.3)]),
    ("Grab, Ruhefrist läuft (gesperrt)", [voll("#C4C4C4"), linie(GRAU, 0.3)]),
]
