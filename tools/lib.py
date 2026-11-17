"""Zeichen-Helfer fuer die GIS-Akademie-Symbolbibliothek.
Alle Symbole: viewBox 0 0 100 100. Rollen:
  F = Fuellfarbe  (QGIS: param(fill))
  S = Konturfarbe (QGIS: param(outline)), auch fuer dunkle Glyphen
  W = festes Weiss,  N = keine
"""
import math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

_FONT = TTFont("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf")
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


def render(elems, ctx, title):
    body = "\n  ".join(e(ctx) for e in elems)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100" height="100" '
            'viewBox="0 0 100 100">\n'
            f"  <title>{title}</title>\n  {body}\n</svg>\n")
