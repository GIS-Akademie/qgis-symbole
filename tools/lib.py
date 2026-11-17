"""Zeichen-Helfer fuer die GIS-Akademie-Symbolbibliothek.
Alle Symbole: viewBox 0 0 100 100. Rollen:
  F = Fuellfarbe  (QGIS: param(fill))
  S = Konturfarbe (QGIS: param(outline)), auch fuer dunkle Glyphen
  W = festes Weiss,  N = keine
"""
import math
import os
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

def _font_dirs():
    """Suchorte fuer Schriften: GISAK_FONT_DIR, dann Linux, Windows, macOS."""
    dirs = []
    if os.environ.get("GISAK_FONT_DIR"):
        dirs.append(os.environ["GISAK_FONT_DIR"])
    dirs += ["/usr/share/fonts/truetype/liberation", "/usr/share/fonts/liberation-sans",
             "/usr/share/fonts/TTF", os.path.expanduser("~/.local/share/fonts")]
    windir = os.environ.get("WINDIR", r"C:\Windows")
    dirs.append(os.path.join(windir, "Fonts"))
    if os.environ.get("LOCALAPPDATA"):  # fuer den Benutzer installierte Schriften
        dirs.append(os.path.join(os.environ["LOCALAPPDATA"], "Microsoft", "Windows", "Fonts"))
    dirs += ["/Library/Fonts", os.path.expanduser("~/Library/Fonts")]
    return dirs


def find_font(names, required=True):
    """Erste gefundene Schriftdatei aus `names` (Dateinamen, Reihenfolge = Vorrang)."""
    for name in names:
        for d in _font_dirs():
            p = os.path.join(d, name)
            if os.path.isfile(p):
                return p
    if required:
        sys.exit(f"Schrift nicht gefunden: {', '.join(names)}\n"
                 "Liberation Sans installieren (https://github.com/liberationfonts/liberation-fonts/releases)\n"
                 "oder den Ordner mit den .ttf-Dateien in der Umgebungsvariablen GISAK_FONT_DIR angeben.")
    return None


# Die Beschriftungen der Symbole werden in Pfade umgewandelt. Damit die SVGs auf jedem
# Rechner identisch entstehen, ist hier bewusst nur Liberation Sans Bold zulaessig.
_FONT = TTFont(find_font(["LiberationSans-Bold.ttf"]))
_GS = _FONT.getGlyphSet()
_CMAP = _FONT.getBestCmap()
_HMTX = _FONT["hmtx"]
_CAP = _FONT["OS/2"].sCapHeight


class Ctx:
    def __init__(self, fill, outline):
        self.fill, self.outline = fill, outline

    def f(self, role):
        if role == "F":
            return f'fill="param(fill) {self.fill}" fill-opacity="param(fill-opacity) 1"'
        if role == "S":
            return f'fill="param(outline) {self.outline}" fill-opacity="param(outline-opacity) 1"'
        if role == "W":
            return 'fill="#FFFFFF"'
        return 'fill="none"'

    def s(self, role, sw, cap="round", dash=None):
        if role == "N" or not sw:
            return 'stroke="none"'
        if role == "S":
            col = f'stroke="param(outline) {self.outline}" stroke-opacity="param(outline-opacity) 1"'
        elif role == "F":
            col = f'stroke="param(fill) {self.fill}" stroke-opacity="param(fill-opacity) 1"'
        else:
            col = 'stroke="#FFFFFF"'
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'{col} stroke-width="{sw}" stroke-linecap="{cap}" stroke-linejoin="round"{d}'


def n(v):
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ---- Grundformen: geben Funktionen zurueck, die mit Ctx gerendert werden ----
def C(cx, cy, r, f="N", s="S", sw=5, dash=None):
    return lambda c: f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}" {c.f(f)} {c.s(s, sw, dash=dash)}/>'


def E(cx, cy, rx, ry, f="N", s="S", sw=5):
    return lambda c: f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" {c.f(f)} {c.s(s, sw)}/>'


def R(x, y, w, h, f="N", s="S", sw=5, rx=0, dash=None):
    return lambda c: (f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="{n(rx)}" '
                      f'{c.f(f)} {c.s(s, sw, dash=dash)}/>')


def PG(pts, f="S", s="N", sw=0):
    p = " ".join(f"{n(x)},{n(y)}" for x, y in pts)
    return lambda c: f'<polygon points="{p}" {c.f(f)} {c.s(s, sw)}/>'


def P(d, f="N", s="S", sw=5, cap="round", dash=None, tr=None):
    t = f' transform="{tr}"' if tr else ""
    return lambda c: f'<path d="{d}" {c.f(f)} {c.s(s, sw, cap, dash)}{t}/>'


def L(x1, y1, x2, y2, sw=5, s="S", cap="round", dash=None):
    return P(f"M{n(x1)},{n(y1)} L{n(x2)},{n(y2)}", "N", s, sw, cap, dash)


def PL(pts, sw=5, s="S", f="N", close=False, cap="round"):
    d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + (" Z" if close else "")
    return P(d, f, s, sw, cap)


def T(text, cx, cy, h, role="S", maxw=None):
    """Text als Pfad, optisch zentriert auf (cx, cy); h = Versalhoehe in Einheiten."""
    scale = h / _CAP
    # Breite bestimmen
    adv, glyphs = 0, []
    for ch in text:
        g = _CMAP[ord(ch)]
        glyphs.append((g, adv))
        adv += _HMTX[g][0]
    bp = BoundsPen(_GS)
    for g, off in glyphs:
        _GS[g].draw(TransformPen(bp, (1, 0, 0, 1, off, 0)))
    x0, y0, x1, y1 = bp.bounds
    if maxw and (x1 - x0) * scale > maxw:
        scale = maxw / (x1 - x0)
    tx = cx - (x0 + x1) / 2 * scale
    ty = cy + (y0 + y1) / 2 * scale
    pen = SVGPathPen(_GS, ntos=lambda v: n(v))
    for g, off in glyphs:
        _GS[g].draw(TransformPen(pen, (scale, 0, 0, -scale, tx + off * scale, ty)))
    d = pen.getCommands()
    return lambda c: f'<path d="{d}" {c.f(role)} stroke="none"/>'


def rot(pts, a, cx=0, cy=0):
    a = math.radians(a)
    ca, sa = math.cos(a), math.sin(a)
    return [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in pts]


def mv(pts, dx, dy, k=1.0):
    return [(dx + x * k, dy + y * k) for x, y in pts]


def regpoly(cx, cy, r, k, a0=-90):
    return [(cx + r * math.cos(math.radians(a0 + i * 360 / k)),
             cy + r * math.sin(math.radians(a0 + i * 360 / k))) for i in range(k)]


def star(cx, cy, ro, ri, k, a0=-90):
    pts = []
    for i in range(2 * k):
        r = ro if i % 2 == 0 else ri
        a = math.radians(a0 + i * 180 / k)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


# ---- Rahmen ----
def fr_circle(f="F", sw=5, r=44, dash=None):
    return [C(50, 50, r, f, "S", sw, dash)]


def fr_square(f="F", sw=5, rx=8):
    return [R(7, 7, 86, 86, f, "S", sw, rx)]


def fr_diamond(f="F", sw=5):
    return [PG([(50, 5), (95, 50), (50, 95), (5, 50)], f, "S", sw)]


def fr_tri(f="F", sw=5):
    return [PG([(50, 8), (94, 88), (6, 88)], f, "S", sw)]


def fr_hex(f="F", sw=5):
    return [PG(regpoly(50, 50, 46, 6, 0), f, "S", sw)]


# ---- Piktogramm-Bausteine (liefern Listen) ----
def lightning(cx, cy, k=1.0, f="S"):
    pts = [(7, -30), (-15, 5), (-2, 5), (-8, 30), (15, -7), (2, -7)]
    return [PG(mv(pts, cx, cy, k), f)]


def rotor(cx, cy, r, f="S", hub=True, a0=0):
    blade = [(0, 0), (-0.13 * r, -0.30 * r), (-0.03 * r, -r), (0.04 * r, -r), (0.10 * r, -0.30 * r)]
    out = [PG(rot(blade, a0 + a, cx, cy), f) for a in (0, 120, 240)]
    if hub:
        out.append(C(cx, cy, 0.13 * r, f, "N", 0))
    return out


def wave(x0, y, w, amp, k=3, sw=5, s="S"):
    seg = w / (2 * k)
    d = f"M{n(x0)},{n(y)} q{n(seg / 2)},{n(-amp)} {n(seg)},0" + f" t{n(seg)},0" * (2 * k - 1)
    return P(d, "N", s, sw)


def cross(cx, cy, a, sw=5, s="S"):
    return [L(cx - a, cy, cx + a, cy, sw, s), L(cx, cy - a, cx, cy + a, sw, s)]


def xcross(cx, cy, a, sw=5, s="S"):
    return [L(cx - a, cy - a, cx + a, cy + a, sw, s), L(cx - a, cy + a, cx + a, cy - a, sw, s)]


def plane(cx, cy, k=1.0, f="S", a=0):
    pts = [(0, -32), (4, -22), (4, -8), (30, 8), (30, 14), (4, 6), (4, 20), (12, 27), (12, 31),
           (0, 28), (-12, 31), (-12, 27), (-4, 20), (-4, 6), (-30, 14), (-30, 8), (-4, -8), (-4, -22)]
    return [PG(mv(rot(pts, a), cx, cy, k), f)]


def treetop(cx, cy, r, f="F", s="S", sw=4, k=8):
    """Laubbaum in Draufsicht: Kreis mit Bogenrand."""
    pts = regpoly(cx, cy, r, k, -90)
    rr = r * math.sin(math.pi / k) * 1.15
    d = f"M{n(pts[0][0])},{n(pts[0][1])}"
    for i in range(1, k + 1):
        x, y = pts[i % k]
        d += f" A{n(rr)},{n(rr)} 0 0 1 {n(x)},{n(y)}"
    return [P(d + " Z", f, s, sw)]


def arrow(x1, y1, x2, y2, sw=5, head=9, s="S"):
    a = math.atan2(y2 - y1, x2 - x1)
    pts = [(x2, y2),
           (x2 - head * math.cos(a - 0.5), y2 - head * math.sin(a - 0.5)),
           (x2 - head * math.cos(a + 0.5), y2 - head * math.sin(a + 0.5))]
    bx, by = x2 - head * 0.8 * math.cos(a), y2 - head * 0.8 * math.sin(a)
    return [L(x1, y1, bx, by, sw, s), PG(pts, s)]


# ---- Gruppen, Boegen, Sektoren ----
def G(elems, dx=0, dy=0, k=1.0, a=0):
    """Gruppe: Elemente verschieben, drehen (Grad, im Uhrzeigersinn) und skalieren."""
    tr = f"translate({n(dx)},{n(dy)})"
    if a:
        tr += f" rotate({n(a)})"
    if k != 1:
        tr += f" scale({n(k)})"
    return lambda c: f'<g transform="{tr}">' + "".join(e(c) for e in elems) + "</g>"


def fit(elems, cx=50, cy=50, k=1.0, a=0):
    """Ein im 100er-Raster um (50, 50) gezeichnetes Piktogramm nach (cx, cy) setzen und skalieren."""
    tr = f"translate({n(cx)},{n(cy)})"
    if a:
        tr += f" rotate({n(a)})"
    if k != 1:
        tr += f" scale({n(k)})"
    tr += " translate(-50,-50)"
    return [lambda c: f'<g transform="{tr}">' + "".join(e(c) for e in elems) + "</g>"]


def pt(cx, cy, r, a):
    """Punkt auf dem Kreis; Winkel in Grad, 0 = oben, im Uhrzeigersinn."""
    a = math.radians(a)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def _arc(cx, cy, r, a0, a1):
    x0, y0 = pt(cx, cy, r, a0)
    x1, y1 = pt(cx, cy, r, a1)
    big = 1 if (a1 - a0) % 360 > 180 else 0
    return f"M{n(x0)},{n(y0)} A{n(r)},{n(r)} 0 {big} 1 {n(x1)},{n(y1)}", (x0, y0), (x1, y1)


def arc(cx, cy, r, a0, a1, sw=5, s="S", cap="round"):
    """Kreisbogen von a0 nach a1 im Uhrzeigersinn."""
    return P(_arc(cx, cy, r, a0, a1)[0], "N", s, sw, cap)


def pie(cx, cy, r, a0, a1, f="S"):
    """Kreissektor."""
    d = _arc(cx, cy, r, a0, a1)[0]
    return P(f"M{n(cx)},{n(cy)} L" + d[1:] + " Z", f, "N", 0)


def chord(cx, cy, r, a0, a1, f="S"):
    """Kreisabschnitt zwischen a0 und a1."""
    return P(_arc(cx, cy, r, a0, a1)[0] + " Z", f, "N", 0)


def cloud(circs, f="F", s="S", sw=4.5):
    """Umriss einer Kette sich ueberlappender Kreise [(cx, cy, r), ...] von links nach rechts."""
    ups, lows = [], []
    for (x0, y0, r0), (x1, y1, r1) in zip(circs, circs[1:]):
        d = math.hypot(x1 - x0, y1 - y0)
        a = (r0 * r0 - r1 * r1 + d * d) / (2 * d)
        h = math.sqrt(max(r0 * r0 - a * a, 0))
        mx, my = x0 + a * (x1 - x0) / d, y0 + a * (y1 - y0) / d
        p, q = (mx + h * (y1 - y0) / d, my - h * (x1 - x0) / d), (mx - h * (y1 - y0) / d, my + h * (x1 - x0) / d)
        ups.append(min(p, q, key=lambda v: v[1]))
        lows.append(max(p, q, key=lambda v: v[1]))

    def seg(c, p0, p1):
        t0 = math.atan2(p0[1] - c[1], p0[0] - c[0])
        t1 = math.atan2(p1[1] - c[1], p1[0] - c[0])
        big = 1 if (t1 - t0) % (2 * math.pi) > math.pi else 0
        return f" A{n(c[2])},{n(c[2])} 0 {big} 1 {n(p1[0])},{n(p1[1])}"

    k = len(circs)
    d = f"M{n(lows[0][0])},{n(lows[0][1])}" + seg(circs[0], lows[0], ups[0])
    for i in range(1, k - 1):
        d += seg(circs[i], ups[i - 1], ups[i])
    d += seg(circs[-1], ups[-1], lows[-1])
    for i in range(k - 2, 0, -1):
        d += seg(circs[i], lows[i], lows[i - 1])
    return P(d + " Z", f, s, sw)


# ---- Allgemeine Piktogramme im 100er-Raster um (50, 50); fg = Zeichenfarbe, bg = Aussparungen ----
def drop(f="F", s="S", sw=5):
    return [P("M50,10 C64,30 78,46 78,62 A28,28 0 0 1 22,62 C22,46 36,30 50,10 Z", f, s, sw)]


def flame(fg="S", bg="F"):
    return [P("M52,10 C56,28 76,40 76,62 C76,80 64,92 50,92 C36,92 24,80 24,64 C24,50 33,44 37,32 "
              "C42,42 44,44 48,44 C46,32 46,22 52,10 Z", fg, "N", 0),
            P("M50,58 C57,65 61,70 61,77 C61,84 56,88 50,88 C44,88 39,84 39,77 C39,70 46,67 50,58 Z", bg, "N", 0)]


def bucket(fg="S", sw=4):
    """Eimer (Planzeichen Spielplatz)."""
    return [PL([(33, 44), (67, 44), (61, 76), (39, 76)], sw, fg, close=True), L(29, 44, 71, 44, sw, fg),
            P("M36,44 A14,15 0 0 1 64,44", "N", fg, sw * 0.85)]


def tent(fg="S", sw=4):
    return [PL([(50, 30), (76, 76), (24, 76)], sw, fg, close=True), L(50, 30, 44, 20, sw * 0.85, fg),
            L(50, 30, 56, 20, sw * 0.85, fg)]


def person(fg="S", sw=7):
    """Gehende Person."""
    return [C(52, 17, 9, fg, "N", 0), PL([(52, 30), (48, 56)], sw + 3, fg),
            PL([(48, 56), (60, 72), (62, 90)], sw, fg), PL([(48, 56), (40, 72), (30, 88)], sw, fg),
            PL([(52, 33), (66, 44), (72, 54)], sw - 1.5, fg), PL([(52, 33), (38, 42), (32, 54)], sw - 1.5, fg)]


def house(fg="S", f="F", sw=5):
    """Haus in Ansicht."""
    return [R(26, 46, 48, 36, f, fg, sw), PL([(16, 50), (50, 18), (84, 50)], sw, fg)]


def tree_side(fg="S", f="F", sw=5):
    """Laubbaum in Ansicht."""
    return [L(50, 60, 50, 90, sw + 1, fg), C(50, 38, 27, f, fg, sw)]


def conifer_side(fg="S", f="F", sw=5):
    """Nadelbaum in Ansicht."""
    return [L(50, 74, 50, 92, sw + 1, fg), PG([(50, 8), (74, 76), (26, 76)], f, fg, sw)]


def bike(fg="S", sw=4.5):
    """Fahrrad."""
    return [C(27, 62, 15, "N", fg, sw), C(73, 62, 15, "N", fg, sw),
            PL([(27, 62), (42, 36), (64, 36), (73, 62)], sw, fg), PL([(42, 36), (50, 62), (64, 36)], sw, fg),
            L(50, 62, 27, 62, sw, fg), PL([(64, 36), (62, 26), (70, 24)], sw, fg), L(34, 31, 46, 31, sw + 0.5, fg),
            L(40, 31, 42, 36, sw, fg)]


def fish(fg="S", bg="F"):
    return [P("M16,50 Q40,26 66,50 Q40,74 16,50 Z", fg, "N", 0), PG([(60, 50), (84, 34), (84, 66)], fg),
            C(31, 46, 3.2, bg, "N", 0)]


def eye(fg="S", sw=5):
    return [P("M14,50 Q50,16 86,50 Q50,84 14,50 Z", "N", fg, sw), C(50, 50, 12, fg, "N", 0)]


def swimmer(fg="S"):
    return [C(32, 34, 9, fg, "N", 0), PL([(43, 45), (62, 38), (78, 47)], 6.5, fg), wave(14, 62, 72, 5, 3, 5, fg),
            wave(14, 78, 72, 5, 3, 5, fg)]


def gear(cx, cy, r, k=8, f="S", hole=None, bg="F"):
    """Zahnrad."""
    pts = []
    for i in range(k):
        a = i * 360 / k
        w = 360 / k / 4
        pts += [pt(cx, cy, r * 0.78, a - w * 1.5), pt(cx, cy, r, a - w * 0.8), pt(cx, cy, r, a + w * 0.8),
                pt(cx, cy, r * 0.78, a + w * 1.5)]
    out = [PG(pts, f)]
    if hole:
        out.append(C(cx, cy, hole, bg, "N", 0))
    return out


def sun(cx, cy, r, fg="S", f="F", sw=4.5, rays=8, gap=6, ln=8):
    return [C(cx, cy, r, f, fg, sw)] + [L(*pt(cx, cy, r + gap, i * 360 / rays), *pt(cx, cy, r + gap + ln, i * 360 / rays),
                                         sw, fg) for i in range(rays)]


def render(elems, ctx, title):
    body = "\n  ".join(e(ctx) for e in elems)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100" height="100" '
            'viewBox="0 0 100 100">\n'
            f"  <title>{title}</title>\n  {body}\n</svg>\n")
