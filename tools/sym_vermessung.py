"""Sammlung Vermessung: Grenz- und Vermessungspunkte, Aufschluesse, Plan- und Topografiezeichen.
Orientierung: Darstellung in Liegenschaftskarten (ALKIS) und Vermessungsrissen (DIN 18702), Aufschluesse
nach DIN 4023. Eigene Nachkonstruktionen, keine amtlichen Vorlagen.
Stil: schwarz auf weiss, Strich 5 (Details 4), geometrische Grundformen ohne Rahmen.
Praefix topo_ = Topografie im Lageplan.
"""
from lib import *

KEY = "vermessung"
NAME = "Vermessung"
DESC = ("Symbole für Vermessung, Kataster und Lagepläne: Grenzpunkte, Fest- und Aufnahmepunkte, Passpunkte, "
        "Aufschlüsse, Nordpfeile sowie Topografiezeichen (Bäume, Masten, Schächte, Hydranten) in Anlehnung an "
        "Liegenschaftskarte und DIN 18702")
TAGS = "vermessung, kataster, lageplan, festpunkt, grenzpunkt, topografie, din 18702"

BK = ("#FFFFFF", "#000000")


def tick4(r0, r1, a0=45, sw=4.5):
    return [L(*pt(50, 50, r0, a0 + i * 90), *pt(50, 50, r1, a0 + i * 90), sw) for i in range(4)]


S = [
    # ---- Grenzpunkte ----
    ("grenzpunkt_abgemarkt", "Grenzpunkt, abgemarkt (Grenzstein, Grenzmarke)", *BK, [C(50, 50, 22, "F", "S", 5)]),
    ("grenzpunkt_rohr", "Grenzpunkt, abgemarkt mit Rohr oder Eisen", *BK,
     [C(50, 50, 22, "F", "S", 5), C(50, 50, 7, "S", "N", 0)]),
    ("grenzpunkt_bolzen", "Grenzpunkt, abgemarkt mit Bolzen oder Nagel", *BK, [C(50, 50, 20, "S", "N", 0)]),
    ("grenzpunkt_meisselzeichen", "Grenzpunkt, Meißelzeichen (Kreuz)", *BK, cross(50, 50, 22, 5)),
    ("grenzpunkt_unvermarkt", "Grenzpunkt, nicht abgemarkt", *BK, [C(50, 50, 9, "S", "N", 0)]),
    # ---- Fest- und Vermessungspunkte ----
    ("trigonometrischer_punkt", "Lagefestpunkt / Trigonometrischer Punkt", *BK,
     [PG([(50, 10), (92, 84), (8, 84)], "F", "S", 5), C(50, 59, 7, "S", "N", 0)]),
    ("hoehenfestpunkt", "Höhenfestpunkt / Nivellementpunkt", *BK,
     [C(50, 50, 32, "F", "N", 0), chord(50, 50, 32, 90, 270), C(50, 50, 32, "N", "S", 5)]),
    ("gnss_referenzpunkt", "GNSS-Referenzpunkt / Referenzstation", *BK,
     [PG([(50, 46), (78, 90), (22, 90)], "F", "S", 5), C(50, 74, 5, "S", "N", 0),
      arc(50, 46, 20, -53, 53, 4.5), arc(50, 46, 36, -51, 51, 4.5)]),
    ("aufnahmepunkt", "Aufnahmepunkt", *BK,
     [C(50, 50, 26, "F", "S", 5), L(8, 50, 92, 50, 4, cap="butt"), L(50, 8, 50, 92, 4, cap="butt")]),
    ("sicherungspunkt", "Sicherungspunkt", *BK, [R(26, 26, 48, 48, "F", "S", 5), C(50, 50, 7, "S", "N", 0)]),
    ("polygonpunkt", "Polygonpunkt", *BK,
     [C(50, 50, 32, "F", "S", 5), C(50, 50, 17, "N", "S", 4), C(50, 50, 5, "S", "N", 0)]),
    ("kleinpunkt", "Kleinpunkt / Sonstiger Vermessungspunkt", *BK, [C(50, 50, 12, "F", "S", 4.5)]),
    ("gebaeudepunkt", "Gebäudepunkt / Bauwerkspunkt", *BK, [R(37, 37, 26, 26, "S", "N", 0)]),
    ("messpunkt", "Messpunkt", *BK, cross(50, 50, 34, 5) + [C(50, 50, 14, "F", "S", 4)]),
    ("standpunkt", "Instrumentenstandpunkt (Stativ)", *BK,
     [L(50, 34, 22, 90, 5), L(50, 34, 78, 90, 5), L(50, 34, 50, 90, 5), R(36, 12, 28, 22, "S", "N", 0, 4),
      C(50, 23, 5, "F", "N", 0)]),
    # ---- Passpunkte und Bildflug ----
    ("passpunkt", "Passpunkt", *BK,
     [C(50, 50, 38, "F", "N", 0), pie(50, 50, 38, 0, 90), pie(50, 50, 38, 180, 270), C(50, 50, 38, "N", "S", 5)]),
    ("zielmarke", "Zielmarke / signalisierter Passpunkt", *BK,
     [R(14, 14, 72, 72, "F", "S", 5), PG([(14, 14), (86, 14), (50, 50)], "S"), PG([(14, 86), (86, 86), (50, 50)], "S")]),
    ("fotostandort", "Fotostandort", *BK,
     [R(34, 20, 24, 14, "S", "N", 0, 3), R(10, 30, 80, 52, "F", "S", 5, 8), C(50, 56, 15, "N", "S", 5),
      C(50, 56, 5, "S", "N", 0)]),
    ("fotostandort_blickrichtung", "Fotostandort mit Blickrichtung (nach rechts, drehbar)", *BK,
     [PG([(28, 50), (90, 20), (90, 80)], "F", "S", 4.5), C(28, 50, 13, "S", "N", 0)]),
    ("drohnenstartpunkt", "Start- und Landepunkt Drohne (UAV)", *BK,
     [L(27, 27, 73, 73, 5), L(27, 73, 73, 27, 5)]
     + [C(x, y, 14, "F", "S", 4) for x in (27, 73) for y in (27, 73)] + [R(40, 40, 20, 20, "S", "N", 0, 5)]),
    # ---- Aufschluesse ----
    ("bohrpunkt", "Bohrung / Bohrpunkt", *BK,
     [C(50, 50, 36, "F", "N", 0), chord(50, 50, 36, 180, 360), C(50, 50, 36, "N", "S", 5)]),
    ("sondierung", "Sondierung (Ramm- oder Drucksondierung)", *BK,
     [PG([(12, 18), (88, 18), (50, 88)], "F", "N", 0), PG([(12, 18), (50, 18), (50, 88)], "S"),
      PG([(12, 18), (88, 18), (50, 88)], "N", "S", 5)]),
    ("schurf", "Schurf", *BK,
     [R(16, 16, 68, 68, "F", "N", 0), R(16, 16, 34, 68, "S", "N", 0), R(16, 16, 68, 68, "N", "S", 5)]),
    # ---- Planzeichen ----
    ("nordpfeil", "Nordpfeil", *BK,
     [PG([(50, 4), (72, 66), (50, 54)], "S", "S", 3), PG([(50, 4), (28, 66), (50, 54)], "F", "S", 3), T("N", 50, 84, 20)]),
    ("nordpfeil_schlicht", "Nordpfeil, schlicht", *BK,
     [T("N", 50, 13, 18), L(50, 94, 50, 52, 5, cap="butt"), PG([(50, 28), (66, 62), (50, 54), (34, 62)], "S")]),
    ("nordstern", "Nordstern / Windrose", *BK,
     [PG(star(50, 58, 38, 10, 4), "F", "S", 3.5), PG([(50, 20), (57, 51), (50, 58)], "S"),
      PG([(88, 58), (57, 65), (50, 58)], "S"), PG([(50, 96), (43, 65), (50, 58)], "S"),
      PG([(12, 58), (43, 51), (50, 58)], "S"), T("N", 50, 9, 14)]),
    ("gitterkreuz", "Gitterkreuz / Koordinatenkreuz", *BK,
     [L(18, 50, 82, 50, 3.5, cap="butt"), L(50, 18, 50, 82, 3.5, cap="butt")]),
    ("flurstueckshaken", "Zusammengehörigkeitshaken (Flurstückshaken)", *BK,
     [P("M26,68 C26,38 74,62 74,32", "N", "S", 5)]),
    ("zuordnungspfeil", "Zuordnungspfeil (drehbar)", *BK, arrow(10, 50, 90, 50, 4, 16)),
    ("hoehenpunkt", "Höhenpunkt / Höhenkote", *BK, xcross(50, 50, 14, 4.5) + [C(50, 50, 4.5, "S", "N", 0)]),
    ("fliessrichtung", "Fließrichtung / Gefällepfeil (drehbar)", *BK, arrow(12, 50, 90, 50, 6, 20)),
    # ---- Topografie im Lageplan ----
    ("topo_laubbaum", "Topografie: Laubbaum", *BK, treetop(50, 50, 38) + [C(50, 50, 5, "S", "N", 0)]),
    ("topo_nadelbaum", "Topografie: Nadelbaum", *BK, [PG(star(50, 50, 43, 23, 8), "F", "S", 4), C(50, 50, 5, "S", "N", 0)]),
    ("topo_strauch", "Topografie: Strauch / Busch", *BK, treetop(50, 50, 24, k=6)),
    ("topo_laterne", "Topografie: Laterne / Straßenleuchte", *BK, [C(50, 50, 15, "F", "S", 5)] + tick4(24, 40, sw=5)),
    ("topo_mast", "Topografie: Mast (Holz, Beton, Stahlrohr)", *BK,
     [C(50, 50, 26, "F", "S", 4), C(50, 50, 11, "S", "N", 0)]),
    ("topo_gittermast", "Topografie: Gittermast", *BK,
     [R(18, 18, 64, 64, "F", "S", 5), L(18, 18, 82, 82, 4, cap="butt"), L(18, 82, 82, 18, 4, cap="butt")]),
    ("topo_schacht_rund", "Topografie: Schacht, rund", *BK,
     [C(50, 50, 32, "F", "S", 5), L(27.4, 27.4, 72.6, 72.6, 4, cap="butt"), L(27.4, 72.6, 72.6, 27.4, 4, cap="butt")]),
    ("topo_schacht_eckig", "Topografie: Schacht, eckig", *BK,
     [R(20, 20, 60, 60, "F", "S", 5), L(20, 80, 80, 20, 4, cap="butt")]),
    ("topo_strasseneinlauf", "Topografie: Straßeneinlauf", *BK,
     [R(16, 30, 68, 40, "F", "S", 5)] + [L(x, 30, x, 70, 4, cap="butt") for x in (33, 50, 67)]),
    ("topo_hydrant_unterflur", "Topografie: Unterflurhydrant", *BK, [E(50, 50, 38, 25, "F", "S", 5), T("H", 50, 50, 24)]),
    ("topo_hydrant_ueberflur", "Topografie: Überflurhydrant", *BK,
     [R(8, 42, 84, 16, "S", "N", 0, 3), C(50, 50, 24, "F", "S", 5), C(50, 50, 8, "S", "N", 0)]),
    ("topo_schieberkappe", "Topografie: Schieberkappe / Armatur", *BK,
     [R(22, 22, 56, 56, "F", "S", 5), PG([(30, 34), (30, 66), (50, 50)], "S"), PG([(70, 34), (70, 66), (50, 50)], "S")]),
    ("topo_verteilerkasten", "Topografie: Verteilerkasten / Schaltschrank", *BK,
     [R(12, 30, 76, 40, "F", "S", 5), L(12, 70, 88, 30, 4, cap="butt")]),
    ("topo_verkehrsschild", "Topografie: Verkehrsschild", *BK, [L(50, 94, 50, 48, 5), C(50, 28, 20, "F", "S", 5)]),
    ("topo_ampel", "Topografie: Lichtsignalanlage", *BK,
     [L(50, 74, 50, 94, 5), R(34, 8, 32, 66, "F", "S", 4.5, 8)] + [C(50, y, 6, "S", "N", 0) for y in (23, 41, 59)]),
    ("topo_bank", "Topografie: Bank", *BK, [R(14, 42, 72, 24, "F", "S", 4.5), L(14, 32, 86, 32, 7, cap="butt")]),
    ("topo_eingang", "Topografie: Eingang / Zufahrt (Spitze zeigt auf das Gebäude)", *BK,
     [PG([(50, 24), (78, 74), (22, 74)], "S")]),
    ("topo_boeschung", "Topografie: Böschung (Linienelement, Oberkante durch die Symbolmitte)", *BK,
     [L(34, 50, 34, 92, 4, cap="butt"), L(66, 50, 66, 70, 4, cap="butt")]),
]

SYMBOLS = S
