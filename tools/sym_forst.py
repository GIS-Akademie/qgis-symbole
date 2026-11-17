"""Sammlung Forst: Baumarten und Bestandesphasen, betriebliche Einrichtungen, Jagd und Wild, Waldfunktionen und Schutz.
Orientierung: Forstbetriebskarten und Forsteinrichtung der Laender (Baumartengruppen, Altersklassen, forstliche
Kurzzeichen Fi, Ki, Ta, Dgl, Lae, Bu, Ei), Leitfaden zur Kartierung der Schutz- und Erholungsfunktionen des Waldes
(Waldfunktionenkartierung, Projektgruppe der AG Forsteinrichtung). Die Farben und Zeichen der Forstbetriebskarten
sind Laendersache und nicht einheitlich; eigene Entwuerfe, keine amtlichen Vorlagen.
Stil: helle gruene Fuellung, dunkelgruener Strich 5. Die Form zeigt die Gruppe:
  Baumkrone ohne Rahmen = Baumart (Draufsicht: Bogenrand = Laubholz, Zackenrand = Nadelholz, mit Kurzzeichen)
  oder Bestandesphase (Seitenansicht), Quadrat = betriebliche Einrichtung, Kreis = Jagd und Wild,
  Raute = Waldfunktion oder Schutz.
Linien und Flaechen: dunkelgruen; Wege nach Ausbau abgestuft (Doppellinie, Strich, kurze Striche), Grenzen nach
Rang abgestuft; Baumartengruppen als Farbton mit Punktmuster (Kreis = Laubholz, Dreieck = Nadelholz),
Altersklassen als abgestufte Gruentoene, Waldfunktionen als Schraffur oder Randband.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "forst"
NAME = "Forst"
DESC = ("Symbole für Forstwirtschaft: Baumarten mit Kurzzeichen, Bestandesphasen und Schäden, betriebliche "
        "Einrichtungen und Erschließung, Jagd und Wild, Waldfunktionen, Waldschutz und Rettung")
TAGS = "forst, wald, forstwirtschaft, forsteinrichtung, baumart, bestand, jagd, waldfunktion, waldbrand"

FG = ("#DCE8C8", "#3B5B1F")


def dot(x, y, r=3.5):
    return C(x, y, r, "S", "N", 0)


def lb(txt=None, h=24, mw=46):  # Laubholz in Draufsicht
    return treetop(50, 50, 41) + ([T(txt, 50, 50, h, maxw=mw)] if txt else [dot(50, 50, 6)])


def nd(txt=None, h=22, mw=40):  # Nadelholz in Draufsicht
    return [PG(star(50, 50, 46, 29, 8), "F", "S", 4)] + ([T(txt, 50, 50, h, maxw=mw)] if txt else [dot(50, 50, 6)])


def be(*sh):  # betriebliche Einrichtung
    return fr_square() + list(sh)


def jw(*sh):  # Jagd und Wild
    return fr_circle() + list(sh)


def wf(*sh):  # Waldfunktion, Schutz
    return fr_diamond() + list(sh)


def tuft(x, y, k=1.0, sw=4):
    return [L(x, y, x, y - 18 * k, sw), L(x, y, x - 10 * k, y - 13 * k, sw), L(x, y, x + 10 * k, y - 13 * k, sw)]


def laub(cx, cy, k):
    return fit(tree_side(), cx, cy, k)


def nadel(cx, cy, k):
    return fit(conifer_side(), cx, cy, k)


def _misch():
    """Krone in Draufsicht: links Bogenrand (Laubholz), rechts Zackenrand (Nadelholz)."""
    st, tp = star(50, 50, 46, 29, 8), regpoly(50, 50, 40, 8, -90)
    rr = 40 * math.sin(math.pi / 8) * 1.15
    d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in st[:9] + [tp[4]])
    for i in (5, 6, 7, 0):
        d += f" A{n(rr)},{n(rr)} 0 0 1 {n(tp[i][0])},{n(tp[i][1])}"
    return [P(d + " Z", "F", "S", 4), L(50, 6, 50, 94, 3.5, cap="butt")]


SPROSS = [L(50, 88, 50, 40, 5), P("M50,70 Q30,68 24,48 Q44,50 50,70 Z", "S", "N", 0),
          P("M50,56 Q70,54 76,34 Q56,36 50,56 Z", "S", "N", 0)]
FICHTE = [L(50, 76, 50, 94, 6), PG([(50, 32), (76, 78), (24, 78)], "F", "S", 5), PG([(50, 6), (69, 46), (31, 46)], "F", "S", 5)]
KAEFER = [L(34, 44, 24, 38, 5), L(66, 44, 76, 38, 5), L(33, 56, 22, 56, 5), L(67, 56, 78, 56, 5), L(35, 68, 25, 76, 5),
          L(65, 68, 75, 76, 5), E(50, 56, 17, 21, "S", "N", 0), C(50, 30, 9, "S", "N", 0)]
POLTER = ([C(x, 72, 10.5, "F", "S", 4) for x in (27, 50, 73)] + [C(x, 52, 10.5, "F", "S", 4) for x in (38.5, 61.5)]
          + [C(50, 32, 10.5, "F", "S", 4)]
          + [dot(x, y, 3) for x, y in ((27, 72), (50, 72), (73, 72), (38.5, 52), (61.5, 52), (50, 32))])
HOCHSITZ = [R(34, 16, 32, 24, "S", "N", 0, 2), L(28, 16, 72, 16, 5), L(40, 40, 28, 86, 5), L(60, 40, 72, 86, 5),
            L(35, 60, 65, 60, 4), L(36, 60, 69, 80, 3.5), L(64, 60, 31, 80, 3.5)]
SCHILD = [P("M50,24 L69,31 V50 Q69,68 50,78 Q31,68 31,50 V31 Z", "S", "N", 0),
          PG([(50, 34), (60, 58), (40, 58)], "F"), L(50, 58, 50, 66, 4.5, "F", "butt")]

S = [
    # ---- Baumarten (Krone in Draufsicht, ohne Rahmen) ----
    ("laubholz", "Laubholz", *FG, lb()),
    ("nadelholz", "Nadelholz", *FG, nd()),
    ("mischbestand", "Mischbestand", *FG, _misch()),
    ("fichte", "Fichte (Fi)", *FG, nd("Fi", 24)),
    ("kiefer", "Kiefer (Ki)", *FG, nd("Ki", 24)),
    ("tanne", "Tanne (Ta)", *FG, nd("Ta", 24)),
    ("douglasie", "Douglasie (Dgl)", *FG, nd("Dgl")),
    ("laerche", "Lärche (Lä)", *FG, nd("Lä", 24)),
    ("buche", "Buche (Bu)", *FG, lb("Bu")),
    ("eiche", "Eiche (Ei)", *FG, lb("Ei")),
    ("edellaubholz", "Edellaubholz (ELh)", *FG, lb("ELh", 22, 50)),
    ("weichlaubholz", "Weichlaubholz (WLh)", *FG, lb("WLh", 22, 50)),
    # ---- Bestandesphasen und Schaeden (Seitenansicht, ohne Rahmen) ----
    ("verjuengung", "Verjüngung / Naturverjüngung", *FG,
     [L(6, 90, 94, 90, 4)] + laub(62, 46, 0.94) + nadel(14, 70, 0.4) + nadel(30, 74, 0.32)),
    ("kultur", "Kultur / Pflanzung", *FG,
     [L(6, 84, 94, 84, 4)] + fit(SPROSS, 20, 44, 0.56) + fit(SPROSS, 50, 44, 0.56) + fit(SPROSS, 80, 44, 0.56)),
    ("dickung", "Dickung", *FG,
     nadel(34, 42, 0.56) + nadel(66, 42, 0.56) + nadel(19, 60, 0.56) + nadel(50, 60, 0.56) + nadel(81, 60, 0.56)),
    ("stangenholz", "Stangenholz", *FG,
     [L(6, 92, 94, 92, 4)] + [e for x, y in ((18, 26), (39, 18), (61, 24), (82, 16))
                               for e in (L(x, 92, x, y + 9, 4.5, cap="butt"), C(x, y, 9.5, "F", "S", 4))]),
    ("altholz", "Altholz / Altbestand", *FG,
     [PG([(42, 50), (58, 50), (64, 92), (36, 92)], "S"), L(18, 92, 82, 92, 4),
      cloud([(24, 42, 18), (50, 32, 25), (76, 42, 18)], "F", "S", 5)]),
    ("bloesse", "Blöße", *FG,
     [L(6, 84, 94, 84, 4), PG([(34, 52), (66, 52), (72, 84), (28, 84)], "F", "S", 5), E(50, 52, 16, 7, "F", "S", 4.5),
      C(50, 52, 3, "S", "N", 0)] + tuft(14, 82, 0.9) + tuft(88, 82, 0.9)),
    ("windwurf", "Windwurf / Sturmschaden", *FG,
     [L(6, 92, 94, 92, 4), L(34, 14, 78, 14, 4), L(50, 26, 92, 26, 4)] + fit(FICHTE, 54, 64, 0.8, 78)
     + [E(19, 72, 5, 15, "S", "N", 0)]),
    ("kaeferholz", "Käferholz / Kalamität", *FG,
     [L(36, 8, 36, 94, 5.5)] + [e for i, y in enumerate((24, 42, 60, 78))
                                for e in (L(36, y, 26 - 5 * i, y + 10, 4.5), L(36, y, 46 + 5 * i, y + 10, 4.5))]
     + fit(KAEFER, 78, 30, 0.5)),
    # ---- Betriebliche Einrichtungen (Quadrat) ----
    ("forsthaus", "Forsthaus / Forstbetriebshof", *FG, be(*fit(house(), 40, 54, 0.62), *nadel(74, 52, 0.5))),
    ("holzpolter", "Holzlagerplatz / Polter", *FG, be(*fit(POLTER, 50, 50, 0.9))),
    ("nasslager", "Nasslager", *FG,
     be(*[C(x, 76, 9, "F", "S", 4) for x in (30, 50, 70)], *[C(x, 60, 9, "F", "S", 4) for x in (40, 60)],
        *[e for x in (28, 50, 72) for e in fit(drop("S", "N", 0), x, 32, 0.26)])),
    ("wendeplatz", "Wendeplatz / Wendehammer", *FG,
     be(P("M34,80 V46 A16,16 0 0 1 66,46 V60", "N", "S", 7, cap="butt"), PG([(52, 58), (80, 58), (66, 80)], "S"))),
    ("schranke", "Schranke", *FG,
     be(L(30, 44, 30, 80, 6), L(80, 52, 80, 80, 4.5), R(16, 34, 68, 13, "F", "S", 4, 2), R(16, 34, 16, 13, "S", "N", 0, 2),
        L(46, 36, 40, 45, 4, cap="butt"), L(60, 36, 54, 45, 4, cap="butt"), L(74, 36, 68, 45, 4, cap="butt"))),
    ("pflanzgarten", "Pflanzgarten / Forstbaumschule", *FG,
     be(*fit(SPROSS, 26, 40, 0.48), *fit(SPROSS, 50, 40, 0.48), *fit(SPROSS, 74, 40, 0.48), L(16, 62, 84, 62, 4.5),
        L(22, 74, 78, 74, 4.5, dash="9 8"))),
    ("saatgutbestand", "Saatgutbestand / Erntebestand", *FG,
     be(P("M35,48 Q35,78 50,84 Q65,78 65,48 Z", "S", "N", 0), P("M31,48 Q31,30 50,30 Q69,30 69,48 Z", "F", "S", 4.5),
        L(50, 30, 55, 18, 5))),
    ("versuchsflaeche", "Versuchsfläche", *FG,
     be(R(22, 22, 56, 56, "N", "S", 4, 0, "9 7"), T("V", 50, 50, 28))),
    # ---- Jagd und Wild (Kreis) ----
    ("hochsitz", "Hochsitz / Kanzel", *FG, jw(*fit(HOCHSITZ, 50, 50, 0.76))),
    ("fuetterung", "Wildfütterung", *FG,
     jw(PL([(24, 40), (50, 24), (76, 40)], 5.5), L(33, 40, 33, 78, 5), L(67, 40, 67, 78, 5),
        PG([(38, 50), (62, 50), (50, 68)], "S", "S", 3))),
    ("salzlecke", "Salzlecke", *FG,
     jw(L(50, 48, 50, 80, 7, cap="butt"), L(34, 80, 66, 80, 5), R(36, 24, 28, 24, "F", "S", 5, 3),
        dot(44, 32, 2.5), dot(55, 34, 2.5), dot(48, 41, 2.5))),
    ("wildacker", "Wildacker / Wildwiese", *FG,
     jw(*fit(SPROSS, 50, 40, 0.62), L(24, 66, 76, 66, 4.5), L(31, 77, 69, 77, 4.5))),
    ("gatter", "Wildschutzzaun / Gatter", *FG,
     jw(L(24, 28, 24, 76, 6), L(76, 28, 76, 76, 6), L(24, 36, 76, 36, 4), L(24, 68, 76, 68, 4),
        *[L(x, 36, x + 16, 68, 3.5, cap="butt") for x in (26, 42, 58)],
        *[L(x + 16, 36, x, 68, 3.5, cap="butt") for x in (26, 42, 58)])),
    # ---- Waldfunktionen und Schutz (Raute) ----
    ("erholungswald", "Erholungswald", *FG, wf(*fit(person(), 50, 50, 0.56))),
    ("schutzwald", "Schutzwald", *FG, wf(*SCHILD)),
    ("bodenschutzwald", "Bodenschutzwald", *FG,
     wf(PG([(50, 22), (61, 46), (39, 46)], "S"), L(28, 50, 72, 50, 5),
        *[L(x, 56, x - 8, 68, 4) for x in (40, 51, 62)])),
    ("wasserschutzwald", "Wasserschutzwald", *FG, wf(*fit(drop("S", "N", 0), 50, 49, 0.6))),
    ("klimaschutzwald", "Klimaschutzwald", *FG, wf(*sun(50, 50, 10, "S", "S", 4.5, 8, 5, 7))),
    ("naturwaldreservat", "Naturwaldreservat / Naturwaldzelle", *FG, wf(T("NW", 50, 50, 22, maxw=46))),
    ("habitatbaum", "Habitatbaum / Biotopbaum", *FG,
     wf(L(50, 54, 50, 78, 8, cap="butt"), C(50, 40, 17, "S", "N", 0), C(50, 40, 6.5, "F", "N", 0))),
    ("totholz", "Totholz", *FG,
     wf(L(42, 46, 35, 33, 5.5), R(26, 44, 44, 17, "S", "N", 0, 8), E(64, 52.5, 6, 8.5, "F", "S", 3.5),
        L(34, 70, 66, 70, 4))),
    ("biotopbaumgruppe", "Biotopbaumgruppe / Altholzinsel", *FG,
     wf(*[C(x, y, 11.5, "S", "N", 0) for x, y in ((37, 58), (63, 58), (50, 36))],
        *[C(x, y, 4, "F", "N", 0) for x, y in ((37, 58), (63, 58), (50, 36))])),
    ("waldbrandueberwachung", "Waldbrandüberwachung / Feuerwachturm", *FG,
     wf(*fit(eye("S", 6), 50, 36, 0.44), *fit(flame("S", "F"), 50, 64, 0.36))),
    ("loeschwasserentnahme", "Löschwasserentnahme", *FG, wf(T("LW", 50, 50, 22, maxw=46))),
    ("rettungspunkt", "Rettungspunkt Forst", *FG,
     wf(R(42, 28, 16, 44, "S", "N", 0), R(28, 42, 44, 16, "S", "N", 0))),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
G0, GL, WS = FG[1], FG[0], "#FFFFFF"

LINIEN = [
    ("Forstweg, befestigt", [linie(G0, 1.2), linie(WS, 0.7)]),
    ("Forstweg, geplant", [linie(G0, 1.2, [3, 1.5]), linie(WS, 0.7, [3, 1.5])]),
    ("Maschinenweg", [linie(G0, 0.6, [5, 1])]),
    ("Rückegasse", [linie(G0, 0.35, [2, 1])]),
    ("Seiltrasse", [linie(G0, 0.3), marken(mk("circle", 1.1, WS, G0, 0.25), 6)]),
    ("Wanderweg im Wald", [linie(G0, 0.6, [0.6, 1.2])]),
    ("Abteilungsgrenze", [linie(G0, 0.8)]),
    ("Unterabteilungsgrenze", [linie(G0, 0.4, [6, 1.2, 0.6, 1.2])]),
    ("Reviergrenze", [linie(G0 + "59", 2.2), linie(G0, 0.6, [6, 1.2, 0.6, 1.2, 0.6, 1.2])]),
    ("Wildschutzzaun", [linie(G0, 0.3), marken(mk("cross2", 1.2, G0, rw=0.25), 4)]),
    ("Waldrand, Waldmantel", [linie(G0, 0.3), marken(mk("semi_circle", 1.8, GL, G0, 0.25, winkel=180), 1.8)]),
]

FLAECHEN = [
    ("Laubholz", [voll("#CFE39A"), muster(mk("circle", 1.4, None, G0, 0.25), 3.6, versatz=1.8), linie(G0, 0.3)]),
    ("Nadelholz", [voll("#A9CDB4"), muster(mk("triangle", 1.5, G0), 3.6, versatz=1.8), linie(G0, 0.3)]),
    ("Mischbestand", [voll("#BCD8A7"), muster(mk("circle", 1.4, None, G0, 0.25), 3.6),
                      muster(mk("triangle", 1.2, G0, dy=1.8), 3.6, versatz=1.8), linie(G0, 0.3)]),
    ("Altersklasse Kultur, Verjüngungsfläche", [voll("#E9F2D9"), muster(mk("circle", 0.5, G0), 2.2, versatz=1.1),
                                                 linie(G0, 0.3)]),
    ("Altersklasse Jungbestand", [voll("#C3DBA2"), linie(G0, 0.3)]),
    ("Altersklasse mittleres Baumholz", [voll("#8FB56A"), linie(G0, 0.3)]),
    ("Altersklasse Altbestand", [voll("#5C8539"), linie(G0, 0.3)]),
    ("Blöße", [voll("#FFFFFF99"), muster(mk("cross2", 0.9, G0, rw=0.2), 3.0, versatz=1.5), linie(G0, 0.3)]),
    ("Kalamitätsfläche", [schraffur(G0, 0.2, 45, 2), schraffur(G0, 0.2, 135, 2), linie(G0, 0.5)]),
    ("Naturwaldreservat", [voll(GL + "80"), band(G0, 1.2), linie(G0, 0.3)]),
    ("Schutzwald", [schraffur(G0, 0.25, 45, 2.5), linie(G0, 0.4)]),
    ("Erholungswald", [band(G0 + "59", 1.6), linie(G0, 0.4)]),
    ("Wildacker", [voll("#EEF2C4"), schraffur(G0, 0.15, 0, 1.8), linie(G0, 0.3)]),
    ("Holzlagerfläche", [voll(GL), schraffur(G0, 0.25, 90, 1.2), linie(G0, 0.5)]),
]
