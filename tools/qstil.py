"""Linien- und Flaechensymbole: QGIS-Stildatei (XML) und Vorschau.

Ein Symbol ist eine Liste von Ebenen, die von unten nach oben gezeichnet werden.
Masse in Millimetern, Farben als "#RRGGBB" oder "#RRGGBBAA" (mit Deckkraft).

Ebenen fuer Linien und fuer den Umriss von Flaechen:
  linie(farbe, breite, strich=None, ende="flat", versatz=0)   einfache Linie; strich = [Strich, Luecke, ...],
                                                              versatz > 0 = nach rechts in Laufrichtung
  marken(marker, abstand, start=None, versatz=0, ecken=None)  Markierungen entlang der Linie, mitgedreht;
                                                              ecken = Mindestabstand zu Ecken in mm: Die Linie
                                                              wird an Knicken aufgetrennt und die Markierungen
                                                              werden je Abschnitt mittig verteilt
Ebenen nur fuer Flaechen:
  voll(farbe)                                                 Vollfarbe
  schraffur(farbe, breite, winkel, abstand)                   Schraffur; winkel gegen den Uhrzeigersinn, 45 = "/"
  muster(marker, dx, dy=None, versatz=0)                      Punktmuster; versatz verschiebt jede zweite Zeile
  band(farbe, breite)                                         Randband innerhalb der Flaeche
Marker:
  mk(form, groesse, farbe, rand=None, rw=0.25, winkel=0, dy=0)   einfache Markierung
  sv(name, groesse, fuell, strich, dy=0)                         SVG-Symbol der eigenen Sammlung (Symbolname)

Formen fuer mk: circle, square, diamond, triangle, semi_circle, filled_arrowhead (gefuellt, optional mit Rand)
sowie line, cross, cross2, arrowhead (nur Strich in farbe, Strichstaerke rw).
Markierungen stehen so, wie sie auf einer Linie von links nach rechts erscheinen. dy > 0 schiebt sie auf die
rechte Seite der Linie; bei Flaechen ist das die Innenseite (die Stildatei erzwingt dafuer die Umlaufrichtung).

Die Eigenschaften stehen als <prop k v> in der Stildatei: Nur in dieser Schreibweise ersetzt das Plugin
Resource Sharing beim Installieren die SVG-Dateinamen durch den Pfad der installierten Sammlung.
"""
import math, re
from xml.sax.saxutils import quoteattr
from lib import Ctx

K = 4            # Vorschau: Pixel je Millimeter
LW, LH = 40, 8   # Vorschau: Probe eines Linien- bzw. Flaechensymbols in Millimetern
FW, FH = 40, 17
STIL_DATEI = "Linien_und_Flaechen.xml"
NUR_STRICH = ("line", "cross", "cross2", "arrowhead")
# Umlaufrichtung im Geometriegenerator, damit rechts der Linie innen ist. Der Generator rechnet in
# Zeichenkoordinaten (y nach unten), deshalb gegen den Uhrzeigersinn.
UMLAUF = "force_polygon_ccw"
FORMEN = ("circle", "square", "diamond", "triangle", "semi_circle", "filled_arrowhead") + NUR_STRICH


# ---- Ebenen ----
def linie(farbe, breite, strich=None, ende="flat", versatz=0, innen=False):
    return ("linie", dict(farbe=farbe, breite=breite, strich=strich, ende=ende, versatz=versatz, innen=innen))


def band(farbe, breite):
    """Randband innerhalb der Flaeche: Linie doppelter Breite, auf die Flaeche beschnitten."""
    return linie(farbe, 2 * breite, innen=True)


def marken(marker, abstand, start=None, versatz=0, ecken=None):
    if ecken is not None and (start is not None or versatz):
        raise ValueError("marken: ecken laesst sich nicht mit start oder versatz kombinieren")
    return ("marken", dict(marker=marker, abstand=abstand, start=abstand / 2 if start is None else start,
                           versatz=versatz, ecken=ecken))


def _var(name, value, body):
    return f"with_variable('{name}', {value}, {body})"


def ecken_ausdruck(abstand, ecke, winkel=25):
    """QGIS-Ausdruck fuer den Geometriegenerator (Einheit Millimeter): trennt Umriss oder Linie an Knicken ueber
    `winkel` Grad auf und kuerzt jeden Abschnitt beidseitig so, dass ein ganzzahliges Vielfaches von `abstand`
    bleibt und mindestens `ecke` frei ist. Abschnitte, die fuer eine Markierung zu kurz sind, entfallen.
    Bewusst wenige geschachtelte Variablen: QGIS wertet tief geschachtelte with_variable sehr langsam aus."""
    i, d = repr(float(abstand)), repr(float(ecke))
    n, ln, zu = "num_points(@r)", "length(@r)", "is_closed(@r)"
    w = (f"abs(azimuth(point_n(@r, if(@element = 1, {n} - 1, @element - 1)), point_n(@r, @element))"
         " - azimuth(point_n(@r, @element), point_n(@r, @element + 1)))")
    cd = (f"array_filter(array_foreach(generate_series(if({zu}, 1, 2), {n} - 1), "
          f"if(if({w} > pi(), 2 * pi() - {w}, {w}) > radians({winkel}), distance_to_vertex(@r, @element - 1), NULL)"
          "), @element IS NOT NULL)")
    k = "array_length(@cd)"
    st = f"if({zu}, if({k} = 0, array(0), @cd), array_cat(array(0), @cd))"
    en = (f"if({zu}, if({k} = 0, array({ln}), array_cat(array_slice(@cd, 1, {k} - 1), array({ln} + @cd[0]))), "
          f"array_cat(@cd, array({ln})))")
    t = f"(@e - @a - floor((@e - @a - 2 * {d}) / {i}) * {i}) / 2"
    stueck = (f"if(@e - @a - 2 * {d} < {i}, NULL, if(@e - @t <= {ln}, line_substring(@r, @a + @t, @e - @t), "
              f"if(@a + @t >= {ln}, line_substring(@r, @a + @t - {ln}, @e - @t - {ln}), "
              f"line_merge(collect_geometries(array(line_substring(@r, @a + @t, {ln}), "
              f"line_substring(@r, 0, @e - @t - {ln})))))))")
    teile = ("array_filter(array_foreach(generate_series(0, array_length(@st) - 1), "
             + _var("a", "@st[@element]", _var("e", "@en[@element]", _var("t", t, stueck)))
             + "), @element IS NOT NULL)")
    ring = _var("p", teile, "if(array_length(@p) = 0, NULL, collect_geometries(@p))")  # leerer Ring (z. B. kleines Loch)
    for name, val in reversed([("r", "coalesce(geometry_n(@b, @element), @b)"), ("cd", cd), ("st", st), ("en", en)]):
        ring = _var(name, val, ring)
    body = ("collect_geometries(array_filter(array_foreach(generate_series(1, coalesce(num_geometries(@b), 1)), "
            f"{ring}), @element IS NOT NULL))")
    return _var("b", f"if(geometry_type($geometry) = 'Polygon', boundary({UMLAUF}($geometry)), $geometry)", body)


def voll(farbe):
    return ("voll", dict(farbe=farbe))


def schraffur(farbe, breite, winkel, abstand):
    return ("schraffur", dict(farbe=farbe, breite=breite, winkel=winkel, abstand=abstand))


def muster(marker, dx, dy=None, versatz=0):
    return ("muster", dict(marker=marker, dx=dx, dy=dx if dy is None else dy, versatz=versatz))


def mk(form, groesse, farbe, rand=None, rw=0.25, winkel=0, dy=0):
    if form not in FORMEN:
        raise ValueError(f"unbekannte Markerform '{form}'")
    return ("mk", dict(form=form, groesse=groesse, farbe=farbe, rand=rand, rw=rw, winkel=winkel, dy=dy))


def sv(name, groesse, fuell="#FFFFFF", strich="#000000", dy=0):
    return ("sv", dict(name=name, groesse=groesse, fuell=fuell, strich=strich, dy=dy))


# ---- Hilfen ----
def _n(v):
    return f"{v:.3f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)


def _hex(c):
    c = c.lstrip("#")
    return [int(c[i:i + 2], 16) for i in range(0, len(c), 2)]


def _rgba(c):
    v = _hex(c)
    return ",".join(str(x) for x in (v + [255])[:4])


def _paint(kind, c):
    if c is None:
        return f'{kind}="none"'
    v = _hex(c)
    s = f'{kind}="#{c.lstrip("#")[:6]}"'
    return s + (f' {kind}-opacity="{_n(v[3] / 255)}"' if len(v) == 4 else "")


def pruefe(typ, titel, ebenen):
    """Bricht mit einer verstaendlichen Meldung ab, wenn eine Ebene nicht zur Symbolart passt."""
    for art, p in ebenen:
        if typ == "line" and (art not in ("linie", "marken") or p.get("innen")):
            raise ValueError(f"Liniensymbol '{titel}': Ebene '{art}' ist nur in Flaechensymbolen moeglich")


# ---- QGIS-Stildatei ----
def _layer(cls, props, ind, sub=""):
    p = "".join(f'{ind}  <prop k="{k}" v={quoteattr(_n(v))}/>\n' for k, v in props.items())
    return f'{ind}<layer class="{cls}" enabled="1" locked="0" pass="0">\n{p}{sub}{ind}</layer>\n'


def _symbol(typ, name, layers, ind, rhr=0):
    return (f'{ind}<symbol type="{typ}" name={quoteattr(name)} alpha="1" clip_to_extent="1" force_rhr="{rhr}">\n'
            f'{layers}{ind}</symbol>\n')


def _marker_xml(m, ind, cid):
    art, p = m
    if art == "sv":
        return _layer("SvgMarker", {
            "name": f"{cid}_{p['name']}.svg", "size": p["groesse"], "size_unit": "MM", "scale_method": "diameter",
            "fixedAspectRatio": 0, "color": _rgba(p["fuell"]), "outline_color": _rgba(p["strich"]),
            "outline_width": 0, "outline_width_unit": "MM", "angle": 0, "offset": f"0,{_n(p['dy'])}",
            "offset_unit": "MM", "horizontal_anchor_point": 1, "vertical_anchor_point": 1}, ind)
    strich = p["form"] in NUR_STRICH
    rand = p["farbe"] if strich else p["rand"]
    return _layer("SimpleMarker", {
        "name": p["form"], "size": p["groesse"], "size_unit": "MM", "scale_method": "diameter",
        "color": _rgba(p["farbe"]) if p["farbe"] and not strich else "0,0,0,0",
        "outline_color": _rgba(rand) if rand else "0,0,0,0", "outline_style": "solid" if rand else "no",
        "outline_width": p["rw"] if rand else 0, "outline_width_unit": "MM", "joinstyle": "miter",
        "cap_style": "flat" if p["form"] == "line" else "round", "angle": p["winkel"],
        "offset": f"0,{_n(p['dy'])}", "offset_unit": "MM", "horizontal_anchor_point": 1,
        "vertical_anchor_point": 1}, ind)


def _linie_props(p):
    d = {"line_color": _rgba(p["farbe"]), "line_style": "solid", "line_width": p["breite"], "line_width_unit": "MM",
         "capstyle": p["ende"], "joinstyle": "round", "offset": p["versatz"], "offset_unit": "MM",
         "use_custom_dash": 1 if p["strich"] else 0,
         "customdash": ";".join(_n(float(v)) for v in p["strich"]) if p["strich"] else "5;2",
         "customdash_unit": "MM", "draw_inside_polygon": 1 if p["innen"] else 0, "ring_filter": 0}
    return d


def symbol_xml(typ, name, ebenen, cid, ind="    "):
    """Ein Symbol (typ = line oder fill) als XML fuer die Stildatei."""
    out, i2 = "", ind + "  "
    for i, (art, p) in enumerate(ebenen):
        sub = f"@{name}@{i}"
        if art == "linie":
            out += _layer("SimpleLine", _linie_props(p), i2)
        elif art == "marken" and p["ecken"] is not None:
            i4 = i2 + "    "
            ml = _layer("MarkerLine", {
                "placement": "interval", "placements": "Interval", "interval": p["abstand"], "interval_unit": "MM",
                "offset_along_line": p["abstand"] / 2, "offset_along_line_unit": "MM", "offset": 0,
                "offset_unit": "MM", "rotate": 1, "average_angle_length": 0, "average_angle_unit": "MM",
                "place_on_every_part": 1, "ring_filter": 0}, i4,
                _symbol("marker", f"@{sub}@0", _marker_xml(p["marker"], i4 + "    ", cid), i4 + "  "))
            out += _layer("GeometryGenerator", {
                "SymbolType": "Line", "geometryModifier": ecken_ausdruck(p["abstand"], p["ecken"]), "units": "MM"},
                i2, _symbol("line", sub, ml, i2 + "  "))
        elif art == "marken":
            out += _layer("MarkerLine", {
                "placement": "interval", "placements": "Interval", "interval": p["abstand"], "interval_unit": "MM",
                "offset_along_line": p["start"], "offset_along_line_unit": "MM", "offset": p["versatz"],
                "offset_unit": "MM", "rotate": 1, "average_angle_length": 0, "average_angle_unit": "MM",
                "ring_filter": 0}, i2,
                _symbol("marker", sub, _marker_xml(p["marker"], i2 + "    ", cid), i2 + "  "))
        elif art == "voll":
            out += _layer("SimpleFill", {"color": _rgba(p["farbe"]), "style": "solid", "outline_style": "no",
                                         "outline_color": "0,0,0,0", "outline_width": 0,
                                         "outline_width_unit": "MM"}, i2)
        elif art == "schraffur":
            ln = _layer("SimpleLine", _linie_props(linie(p["farbe"], p["breite"])[1]), i2 + "    ")
            out += _layer("LinePatternFill", {
                "angle": p["winkel"], "distance": p["abstand"], "distance_unit": "MM", "line_width": p["breite"],
                "line_width_unit": "MM", "color": _rgba(p["farbe"]), "offset": 0, "offset_unit": "MM"}, i2,
                _symbol("line", sub, ln, i2 + "  "))
        elif art == "muster":
            out += _layer("PointPatternFill", {
                "distance_x": p["dx"], "distance_x_unit": "MM", "distance_y": p["dy"], "distance_y_unit": "MM",
                "displacement_x": p["versatz"], "displacement_x_unit": "MM", "displacement_y": 0,
                "displacement_y_unit": "MM", "offset_x": 0, "offset_x_unit": "MM", "offset_y": 0,
                "offset_y_unit": "MM"}, i2,
                _symbol("marker", sub, _marker_xml(p["marker"], i2 + "    ", cid), i2 + "  "))
        else:
            raise ValueError(f"unbekannte Ebene '{art}'")
    rhr = 1 if typ == "fill" and any(a == "marken" for a, _ in ebenen) else 0
    return _symbol(typ, name, out, ind, rhr)


def stil_xml(symbole, cid):
    """Stildatei aus [(typ, name, ebenen), ...]."""
    body = "".join(symbol_xml(t, nm, e, cid) for t, nm, e in symbole)
    return f'<!DOCTYPE qgis_style>\n<qgis_style version="2">\n  <symbols>\n{body}  </symbols>\n</qgis_style>\n'


def eintraege(mod):
    """Alle Linien- und Flaechensymbole einer Sammlung als [(typ, titel, ebenen), ...]."""
    return ([("line", t, e) for t, e in getattr(mod, "LINIEN", [])]
            + [("fill", t, e) for t, e in getattr(mod, "FLAECHEN", [])])


def qgis_name(mod, titel):
    return f"{mod.NAME}: {titel}"


# ---- Vorschau als SVG ----
def _marker_svg(m, lookup):
    art, p = m
    if art == "sv":
        s = p["groesse"]
        return (f'<g transform="translate({_n(-s / 2)},{_n(p["dy"] - s / 2)}) scale({_n(s / 100)})">'
                f'{lookup(p["name"], p["fuell"], p["strich"])}</g>')
    h, form = p["groesse"] / 2, p["form"]
    if form in NUR_STRICH:
        cap = "butt" if form == "line" else "round"
        d = {"line": f"M0,{-h} L0,{h}", "cross": f"M{-h},0 L{h},0 M0,{-h} L0,{h}",
             "cross2": f"M{-h},{-h} L{h},{h} M{-h},{h} L{h},{-h}", "arrowhead": f"M{-h},{-h} L0,0 L{-h},{h}"}[form]
        shape = (f'<path d="{d}" fill="none" {_paint("stroke", p["farbe"])} stroke-width="{_n(p["rw"])}" '
                 f'stroke-linecap="{cap}" stroke-linejoin="miter"/>')
    else:
        d = {"circle": f"M{-h},0 A{h},{h} 0 1 1 {h},0 A{h},{h} 0 1 1 {-h},0 Z",
             "square": f"M{-h},{-h} H{h} V{h} H{-h} Z", "diamond": f"M0,{-h} L{h},0 L0,{h} L{-h},0 Z",
             "triangle": f"M{-h},{h} L{h},{h} L0,{-h} Z", "semi_circle": f"M{-h},0 A{h},{h} 0 0 1 {h},0 Z",
             "filled_arrowhead": f"M0,0 L{-h},{h} L{-h},{-h} Z"}[form]
        st = (f'{_paint("stroke", p["rand"])} stroke-width="{_n(p["rw"])}" stroke-linejoin="miter"'
              if p["rand"] else 'stroke="none"')
        shape = f'<path d="{d}" {_paint("fill", p["farbe"])} {st}/>'
    return f'<g transform="rotate({_n(p["winkel"])}) translate(0,{_n(p["dy"])})">{shape}</g>'


def _versetzt(pts, zu, off):
    """Linienzug parallel verschieben; off > 0 = nach rechts in Laufrichtung (wie in QGIS)."""
    if not off:
        return pts
    def nrm(a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln = math.hypot(dx, dy)
        return -dy / ln, dx / ln
    res, k = [], len(pts)
    for i, p in enumerate(pts):
        ns = []
        if zu or i > 0:
            ns.append(nrm(pts[i - 1], p))
        if zu or i < k - 1:
            ns.append(nrm(p, pts[(i + 1) % k]))
        if len(ns) == 2:
            d = 1 + ns[0][0] * ns[1][0] + ns[0][1] * ns[1][1]
            v = ((ns[0][0] + ns[1][0]) / d, (ns[0][1] + ns[1][1]) / d)
        else:
            v = ns[0]
        res.append((p[0] + off * v[0], p[1] + off * v[1]))
    return res


def _d(pts, zu):
    return "M" + " L".join(f"{_n(float(x))},{_n(float(y))}" for x, y in pts) + (" Z" if zu else "")


def _ebene_svg(art, p, pts, zu, lookup, clip):
    cl = f' clip-path="url(#{clip})"'
    if art == "linie":
        q = _versetzt(pts, zu, p["versatz"])
        dash = f' stroke-dasharray="{" ".join(_n(float(v)) for v in p["strich"])}"' if p["strich"] else ""
        cap = {"flat": "butt", "round": "round", "square": "square"}[p["ende"]]
        return (f'<path d="{_d(q, zu)}" fill="none" {_paint("stroke", p["farbe"])} stroke-width="{_n(p["breite"])}" '
                f'stroke-linecap="{cap}" stroke-linejoin="round"{dash}{cl if p["innen"] else ""}/>')
    if art == "marken":
        q = _versetzt(pts, zu, p["versatz"])
        segs = [(q[i], q[(i + 1) % len(q)]) for i in range(len(q) if zu else len(q) - 1)]
        total = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in segs)
        m, out, s = _marker_svg(p["marker"], lookup), [], p["start"]
        if p["ecken"] is not None:  # je Abschnitt mittig, Ecken frei (wie ecken_ausdruck)
            for a, b in segs:
                ln = math.hypot(b[0] - a[0], b[1] - a[1])
                k = math.floor((ln - 2 * p["ecken"]) / p["abstand"] + 1e-9)
                ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
                for j in range(max(k, 0)):
                    t = ((ln - k * p["abstand"]) / 2 + (j + 0.5) * p["abstand"]) / ln
                    out.append(f'<g transform="translate({_n(a[0] + t * (b[0] - a[0]))},{_n(a[1] + t * (b[1] - a[1]))}) '
                               f'rotate({_n(ang)})">{m}</g>')
            return "".join(out)
        while s < total - 1e-6 if zu else s <= total + 1e-6:
            rest = s
            for a, b in segs:
                ln = math.hypot(b[0] - a[0], b[1] - a[1])
                if rest <= ln + 1e-9:
                    t = rest / ln
                    ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
                    out.append(f'<g transform="translate({_n(a[0] + t * (b[0] - a[0]))},{_n(a[1] + t * (b[1] - a[1]))}) '
                               f'rotate({_n(ang)})">{m}</g>')
                    break
                rest -= ln
            s += p["abstand"]
        return "".join(out)
    x0, y0 = min(x for x, _ in pts), min(y for _, y in pts)
    x1, y1 = max(x for x, _ in pts), max(y for _, y in pts)
    if art == "voll":
        return f'<path d="{_d(pts, True)}" {_paint("fill", p["farbe"])}/>'
    if art == "schraffur":
        a = math.radians(p["winkel"])
        ux, uy, vx, vy = math.cos(a), -math.sin(a), math.sin(a), math.cos(a)
        cx, cy, r = (x0 + x1) / 2, (y0 + y1) / 2, math.hypot(x1 - x0, y1 - y0) / 2
        k = int(r / p["abstand"]) + 1
        d = " ".join(f"M{_n(cx + i * p['abstand'] * vx - r * ux)},{_n(cy + i * p['abstand'] * vy - r * uy)} "
                     f"L{_n(cx + i * p['abstand'] * vx + r * ux)},{_n(cy + i * p['abstand'] * vy + r * uy)}"
                     for i in range(-k, k + 1))
        return (f'<path d="{d}" fill="none" {_paint("stroke", p["farbe"])} stroke-width="{_n(p["breite"])}"{cl}/>')
    if art == "muster":
        m, out, j, y = _marker_svg(p["marker"], lookup), [], 0, y0 + p["dy"] / 2
        while y < y1 + p["dy"]:
            x = x0 + p["dx"] / 2 + (p["versatz"] if j % 2 else 0) - p["dx"]
            while x < x1 + p["dx"]:
                out.append(f'<g transform="translate({_n(x)},{_n(y)})">{m}</g>')
                x += p["dx"]
            y += p["dy"]
            j += 1
        return f'<g{cl}>' + "".join(out) + "</g>"
    raise ValueError(art)


def vorschau_svg(typ, ebenen, lookup, uid):
    """SVG-Fragment (Einheit Millimeter) mit einer Probe des Symbols."""
    if typ == "line":
        pts, zu = [(2.0, LH / 2), (LW - 2.0, LH / 2)], False
    else:
        pts, zu = [(4.0, 3.5), (FW - 4.0, 3.5), (FW - 4.0, FH - 3.5), (4.0, FH - 3.5)], True  # im Uhrzeigersinn
    clip = f"c{uid}"
    out = f'<clipPath id="{clip}"><path d="{_d(pts, True)}"/></clipPath>' if zu else ""
    return out + "".join(_ebene_svg(art, p, pts, zu, lookup, clip) for art, p in ebenen)


def svg_lookup(mod):
    """Liefert die Funktion, die den Inhalt eines SVG-Symbols der Sammlung mit festen Farben zurueckgibt."""
    syms = {s[0]: s[4] for s in mod.SYMBOLS}

    def lookup(name, fuell, strich):
        if name not in syms:
            raise ValueError(f"{mod.KEY}: SVG-Symbol '{name}' fuer eine Markierung nicht gefunden")
        body = "".join(e(Ctx("#" + fuell.lstrip("#")[:6], "#" + strich.lstrip("#")[:6])) for e in syms[name])
        return re.sub(r"param\([^)]*\)\s*", "", body)
    return lookup


def blatt(mod, raster, font_titel, font_text, spalten=4):
    """Vorschaubild aller Linien- und Flaechensymbole einer Sammlung (PIL-Bild)."""
    from PIL import Image, ImageDraw
    lookup, cw, pad, y = svg_lookup(mod), 196, 12, 56
    pos, frag = [], []
    for typ, h in (("line", LH), ("fill", FH)):
        grp = [e for e in eintraege(mod) if e[0] == typ]
        rowh = h * K + 44
        for i, (_, titel, ebenen) in enumerate(grp):
            x, yy = pad + (i % spalten) * cw, y + (i // spalten) * rowh
            pos.append((titel, x, yy + h * K + 4))
            frag.append(f'<g transform="translate({x + (cw - LW * K) // 2},{yy}) scale({K})">'
                        f'{vorschau_svg(typ, ebenen, lookup, len(pos))}</g>')
        y += ((len(grp) + spalten - 1) // spalten) * rowh + (10 if grp else 0)
    w, h = spalten * cw + 2 * pad, y + 4
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
           + "".join(frag) + "</svg>")
    sheet = Image.new("RGB", (w, h), "white")
    im = raster(svg, w, h)
    sheet.paste(im, (0, 0), im)
    d = ImageDraw.Draw(sheet)
    d.text((14, 12), f"GIS-Akademie Symbole – {mod.NAME}: Linien und Flächen", fill="#1F5F5B", font=font_titel)
    for titel, x, ty in pos:
        zeilen, akt = [], ""
        for wort in titel.split():
            test = (akt + " " + wort).strip()
            if akt and d.textlength(test, font=font_text) > cw - 12:
                zeilen.append(akt)
                akt = wort
            else:
                akt = test
        zeilen.append(akt)
        if len(zeilen) > 2:
            zeilen = zeilen[:2]
            while d.textlength(zeilen[1] + " …", font=font_text) > cw - 12:
                zeilen[1] = zeilen[1][:-1]
            zeilen[1] += " …"
        for k, z in enumerate(zeilen):
            d.text((x + cw / 2 - d.textlength(z, font=font_text) / 2, ty + k * 15), z, fill="#333333", font=font_text)
    return sheet
