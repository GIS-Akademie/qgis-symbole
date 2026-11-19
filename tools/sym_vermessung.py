"""Sammlung Vermessung: Grenz- und Vermessungspunkte, Plan- und Topografiezeichen.
Orientierung: Darstellung in Liegenschaftskarten (ALKIS) und Vermessungsrissen (DIN 18702).
Eigene Nachkonstruktionen, keine amtlichen Vorlagen. Nordpfeile stehen in der Sammlung Nordpfeile,
Bohrungen, Sondierungen und Schuerfe in der Sammlung Boden.
Stil: schwarz auf weiss, Strich 5 (Details 4), geometrische Grundformen ohne Rahmen.
Praefix topo_ = Topografie im Lageplan.
Linien und Flaechen: schwarz-weiss; Grenzen nach Rang breiter, Gebaeude schraffiert, Topografie mit Marken
auf der Linie (Boeschung nutzt topo_boeschung).
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "vermessung"
NAME = "Vermessung"
DESC = ("Symbole für Vermessung, Kataster und Lagepläne: Grenzpunkte, Fest- und Aufnahmepunkte, Passpunkte, "
        "Planzeichen sowie Topografiezeichen (Bäume, Masten, Schächte, Hydranten) in Anlehnung an "
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
    # ---- Planzeichen ----
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

# ---- Linien und Flaechen (QGIS-Stildatei) ----
K0 = "#000000"

LINIEN = [
    ("Flurstücksgrenze", [linie(K0, 0.25)]),
    ("Flurstücksgrenze, strittig", [linie(K0, 0.25, [2, 1])]),
    ("Flurgrenze", [linie(K0, 0.5, [6, 1.5, 0.5, 1.5])]),
    ("Gemarkungsgrenze", [linie(K0, 0.7, [6, 1.5, 0.7, 1.5, 0.7, 1.5])]),
    ("Gemeindegrenze", [linie(K0, 0.9, [8, 2])]),
    ("Nutzungsartengrenze", [linie(K0, 0.2, [1, 1])]),
    ("Gebäudeumriss", [linie(K0, 0.5)]),
    ("Messungslinie", [linie(K0, 0.2, [3, 1])]),
    ("Höhenlinie", [linie(K0, 0.2)]),
    ("Höhenlinie, Zähllinie", [linie(K0, 0.45)]),
    ("Böschung, Oberkante", [linie(K0, 0.25), marken(sv("topo_boeschung", 5), 3.2)]),
    ("Zaun", [linie(K0, 0.25), marken(mk("cross2", 1.2, K0, rw=0.25), 5)]),
    ("Mauer", [linie(K0, 1.0), linie("#FFFFFF", 0.5)]),
    ("Hecke", [marken(mk("semi_circle", 2.0, None, K0, 0.25), 2.0)]),
    ("Gleis", [linie(K0, 0.3), marken(mk("line", 1.6, K0, rw=0.3), 2.5)]),
    ("Leitung unterirdisch", [linie(K0, 0.3, [4, 1, 1, 1])]),
]

FLAECHEN = [
    ("Flurstück", [linie(K0, 0.25)]),
    ("Wohngebäude", [voll("#FFFFFF"), schraffur(K0, 0.2, 45, 1.2), linie(K0, 0.5)]),
    ("Nebengebäude", [voll("#FFFFFF"), schraffur(K0, 0.2, 45, 2.5), linie(K0, 0.4)]),
    ("Öffentliches Gebäude", [voll("#B0B0B0"), linie(K0, 0.5)]),
    ("Gebäude geplant", [linie(K0, 0.4, [3, 1.5])]),
    ("Gebäude abgebrochen", [muster(mk("cross2", 1.2, K0, rw=0.2), 3.2, versatz=1.6), linie(K0, 0.3, [1.5, 1])]),
    ("Überdachung", [linie(K0, 0.3, [1.5, 1])]),
    ("Unterirdisches Bauwerk", [linie(K0, 0.3, [4, 1, 1, 1])]),
    ("Befestigte Fläche", [muster(mk("circle", 0.4, K0), 2.0, versatz=1.0), linie(K0, 0.25)]),
    ("Wasserfläche", [schraffur(K0, 0.15, 0, 1.5), linie(K0, 0.3)]),
    ("Baulast, Dienstbarkeit", [schraffur(K0, 0.2, 135, 3), linie(K0, 0.3, [3, 1.5])]),
]
