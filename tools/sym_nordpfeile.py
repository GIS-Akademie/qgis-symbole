"""Sammlung Nordpfeile: schlichte Nordpfeile fuer Karten und Drucklayouts.
Orientierung: Nordpfeile amtlicher Karten, Lageplaene und Bauleitplaene. Eigene Entwuerfe.
Stil: schwarz auf weiss, ohne Rahmen, Strich 5 (Umrisse 4). Die Spitze zeigt nach oben, die Achse liegt
in der Symbolmitte (x = 50). Das N (Versalhoehe 18) steht ueber der Spitze.
Praefix = Bauart: pfeil_ = Pfeil mit Schaft, nadel_ = Nadel ohne Schaft, kreis_ = im Kreis,
rose_ = Windrose. Endung _ohne_n = ohne Buchstabe, dafuer ueber die ganze Symbolhoehe.
Fuellungen: geteilt = rechte Haelfte schwarz, voll = schwarz, umriss = weiss.
"""
from lib import *

KEY = "nordpfeile"
NAME = "Nordpfeile"
DESC = ("Schlichte Nordpfeile für Karten und Drucklayouts: Pfeile mit Schaft, Nadeln, Nordpfeile im Kreis "
        "und Windrosen, jeweils schwarz-weiß mit änderbarer Füll- und Strichfarbe")
TAGS = "nordpfeil, norden, nordrichtung, kompass, windrose, layout, drucklayout, karte"

BK = ("#FFFFFF", "#000000")
GROESSE = 12.0  # Vorgabegroesse des Markierungssymbols in mm


def nn():
    """Das N ueber der Spitze."""
    return T("N", 50, 12, 18)


def shaft(y0, y1=94):
    return L(50, y1, 50, y0, 5)


def head(y, h=30, w=15):
    """Gefuellte Pfeilspitze mit der Spitze bei y."""
    return PG([(50, y), (50 + w, y + h), (50 - w, y + h)], "S")


def needle(y0, y1, w, notch, mode="geteilt", sw=4):
    """Nadel von y0 (Spitze) bis y1, halbe Breite w, Kerbe am Fuss (0 = Dreieck)."""
    a, b, c, d = (50, y0), (50 + w, y1), (50, y1 - notch), (50 - w, y1)
    if mode == "voll":
        return [PG([a, b, c, d], "S", "S", sw)]
    if mode == "umriss":
        return [PG([a, b, c, d], "F", "S", sw)]
    return [PG([a, c, d], "F"), PG([a, b, c], "S"), PG([a, b, c, d], "N", "S", sw)]


def raute(y0, y1, w, mode="halb", sw=4):
    """Kompassnadel als Raute; halb = Nordhaelfte schwarz, viertel = wechselnd geteilt."""
    ym = (y0 + y1) / 2
    no, ea, so, we, m = (50, y0), (50 + w, ym), (50, y1), (50 - w, ym), (50, ym)
    e = [PG([no, ea, so, we], "F")]
    e += [PG([no, ea, we], "S")] if mode == "halb" else [PG([no, ea, m], "S"), PG([so, we, m], "S")]
    return e + [PG([no, ea, so, we], "N", "S", sw)]


def rose(cx, cy, ro, ri, a0=0, sw=3.5):
    """Vierstrahliger Stern, jeder Strahl zur Haelfte schwarz."""
    e = [PG(star(cx, cy, ro, ri, 4, a0 - 90), "F", "S", sw)]
    return e + [PG([pt(cx, cy, ro, a0 + i * 90), pt(cx, cy, ri, a0 + i * 90 + 45), (cx, cy)], "S") for i in range(4)]


def kr(r=33, cy=61, f="F"):
    return C(50, cy, r, f, "S", 4.5)


BLOCK = [(50, 28), (74, 58), (60, 58), (60, 95), (40, 95), (40, 58), (26, 58)]

S = [
    # ---- Pfeile mit Schaft ----
    ("pfeil_linie", "Nordpfeil, Linienpfeil", *BK, [nn(), shaft(31), PL([(35, 49), (50, 31), (65, 49)], 5)]),
    ("pfeil_spitze", "Nordpfeil, Pfeil mit gefüllter Spitze", *BK, [nn(), shaft(54), head(28)]),
    ("pfeil_halbspitze", "Nordpfeil, Pfeil mit halber Spitze", *BK,
     [nn(), shaft(44), PG([(52.5, 27), (52.5, 62), (30, 68)], "S")]),
    ("pfeil_kreuz", "Nordpfeil, Pfeil mit Querstrich", *BK, [nn(), shaft(54), head(28), L(27, 72, 73, 72, 5)]),
    ("pfeil_ring", "Nordpfeil, Pfeil mit Ring", *BK, [nn(), C(50, 74, 15, "F", "S", 4), shaft(54), head(28)]),
    ("pfeil_gefiedert", "Nordpfeil, Pfeil mit Befiederung", *BK,
     [nn(), shaft(54, 84), head(28), PL([(37, 96), (50, 83), (63, 96)], 4.5), PL([(37, 85), (50, 72), (63, 85)], 4.5)]),
    ("pfeil_block", "Nordpfeil, Blockpfeil im Umriss", *BK, [nn(), PG(BLOCK, "F", "S", 4)]),
    ("pfeil_block_voll", "Nordpfeil, Blockpfeil gefüllt", *BK, [nn(), PG(BLOCK, "S", "S", 4)]),
    ("pfeil_block_n", "Nordpfeil, Blockpfeil mit N im Schaft", *BK,
     [PG([(50, 5), (88, 46), (70, 46), (70, 95), (30, 95), (30, 46), (12, 46)], "S", "S", 4), T("N", 50, 72, 24, "F")]),
    ("pfeil_gross_n", "Nordpfeil, Pfeil über großem N", *BK,
     [L(50, 56, 50, 34, 5), head(5, 32, 16), T("N", 50, 80, 30)]),
    # ---- Nadeln ----
    ("nadel_geteilt", "Nordpfeil, Nadel geteilt", *BK, [nn()] + needle(30, 94, 21, 16)),
    ("nadel_voll", "Nordpfeil, Nadel gefüllt", *BK, [nn()] + needle(30, 94, 21, 16, "voll")),
    ("nadel_umriss", "Nordpfeil, Nadel im Umriss", *BK, [nn()] + needle(30, 94, 21, 16, "umriss")),
    ("nadel_dreieck_geteilt", "Nordpfeil, Dreieck geteilt", *BK, [nn()] + needle(30, 94, 17, 0)),
    ("nadel_dreieck_voll", "Nordpfeil, Dreieck gefüllt", *BK, [nn()] + needle(30, 94, 17, 0, "voll")),
    ("nadel_dreieck_umriss", "Nordpfeil, Dreieck im Umriss", *BK, [nn()] + needle(30, 94, 17, 0, "umriss")),
    ("nadel_raute", "Nordpfeil, Kompassnadel mit schwarzer Nordhälfte", *BK, [nn()] + raute(30, 95, 15)),
    ("nadel_raute_geteilt", "Nordpfeil, Kompassnadel wechselnd geteilt", *BK, [nn()] + raute(30, 95, 15, "viertel")),
    # ---- Im Kreis ----
    ("kreis_pfeil", "Nordpfeil im Kreis, Pfeil", *BK,
     [nn(), kr(), L(50, 83, 50, 60, 5), PG([(50, 38), (62, 63), (38, 63)], "S")]),
    ("kreis_nadel", "Nordpfeil im Kreis, Nadel geteilt", *BK, [nn(), kr()] + needle(40, 82, 14, 11, sw=3.5)),
    ("kreis_voll", "Nordpfeil im gefüllten Kreis, helle Nadel", *BK,
     [nn(), C(50, 61, 35, "S", "N", 0), PG([(50, 37), (66, 83), (50, 71), (34, 83)], "F")]),
    ("kreis_kreuz", "Nordpfeil im Kreis, Achsenkreuz mit Pfeil", *BK,
     [nn(), C(50, 69, 18, "F", "S", 4.5), L(20, 69, 80, 69, 4), L(50, 96, 50, 44, 4),
      PG([(50, 27), (60, 47), (40, 47)], "S")]),
    ("kreis_kompass", "Nordpfeil im Kreis, Kompass mit Teilung", *BK,
     [nn(), C(50, 62, 23, "F", "S", 4.5)]
     + [L(*pt(50, 62, 29, a), *pt(50, 62, 36 if a % 90 == 0 else 34, a), 4, cap="butt") for a in range(0, 360, 45)]
     + raute(45, 79, 8, sw=3)),
    ("kreis_n", "Nordpfeil, N im Kreis mit Spitze", *BK,
     [PG([(50, 5), (63, 31), (37, 31)], "S"), C(50, 63, 32, "F", "S", 4.5), T("N", 50, 63, 30)]),
    # ---- Windrosen ----
    ("rose_4", "Windrose, vier Strahlen geteilt", *BK, [nn()] + rose(50, 61, 33, 10)),
    ("rose_4_nord", "Windrose, vier Strahlen mit schwarzem Nordstrahl", *BK,
     [nn(), PG(star(50, 61, 33, 10, 4), "F", "S", 3.5),
      PG([pt(50, 61, 33, 0), pt(50, 61, 10, 45), (50, 61), pt(50, 61, 10, -45)], "S")]),
    ("rose_4_voll", "Windrose, vier Strahlen gefüllt", *BK, [nn(), PG(star(50, 61, 33, 9, 4), "S", "S", 3)]),
    ("rose_8", "Windrose, acht Strahlen geteilt", *BK, [nn()] + rose(50, 61, 23, 7, 45, 3) + rose(50, 61, 33, 8)),
    ("rose_kreis", "Windrose mit Ring", *BK, [nn(), C(50, 61, 21, "N", "S", 4)] + rose(50, 61, 33, 8)),
    ("rose_kreuz", "Achsenkreuz mit Himmelsrichtungen N, O, S, W", *BK,
     [T("N", 50, 9, 12), T("S", 50, 91, 12), T("W", 10, 50, 12), T("O", 91, 50, 12),
      L(24, 50, 76, 50, 4.5), L(50, 78, 50, 38, 4.5), PG([(50, 20), (59, 41), (41, 41)], "S")]),
    # ---- Ohne Buchstabe ----
    ("pfeil_spitze_ohne_n", "Nordpfeil ohne Buchstabe, Pfeil mit gefüllter Spitze", *BK, [shaft(40, 95), head(5, 38, 18)]),
    ("nadel_geteilt_ohne_n", "Nordpfeil ohne Buchstabe, Nadel geteilt", *BK, needle(7, 94, 26, 20)),
    ("nadel_raute_ohne_n", "Nordpfeil ohne Buchstabe, Kompassnadel", *BK, raute(6, 94, 17)),
    ("rose_4_ohne_n", "Windrose ohne Buchstabe, vier Strahlen geteilt", *BK, rose(50, 50, 44, 13)),
]

SYMBOLS = S
