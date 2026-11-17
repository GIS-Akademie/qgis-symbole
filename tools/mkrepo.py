"""Erzeugt SVGs, Stildateien fuer Linien und Flaechen, Vorschaubilder, metadata.ini, KATALOG.md und LICENSE.

Aufruf:  python tools/mkrepo.py <Zielordner>
  - Zielordner = dieses Repository (z. B. "."): nur collections/ und die Dateien im
    Hauptordner werden neu erzeugt, tools/ bleibt unangetastet.
  - anderer Ordner: dort entsteht ein vollstaendiges Repository inklusive tools/.
"""
import glob, os, sys, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import Ctx, render, find_font
from sammlungen import PRE, load, raster
import qstil
from PIL import Image, ImageDraw, ImageFont
from lxml import etree

if len(sys.argv) != 2:
    sys.exit(__doc__)
ROOT = sys.argv[1]


def _same_dir(a, b):
    return os.path.normcase(os.path.realpath(a)) == os.path.normcase(os.path.realpath(b))


IN_PLACE = _same_dir(ROOT, os.path.dirname(HERE))  # Ziel ist das Repository, in dem dieses Skript liegt
if _same_dir(ROOT, HERE):
    sys.exit("Zielordner ist tools/ selbst. Gemeint ist vermutlich der Repository-Ordner, z. B.: python tools/mkrepo.py .")

VERSION = "1.0"
LIC = """Creative Commons Namensnennung 4.0 International (CC BY 4.0)

Copyright (c) 2026 GIS-Akademie

Die Symbole dieser Sammlung dürfen in jedem Format und Medium vervielfältigt,
weiterverbreitet, verändert und für beliebige Zwecke genutzt werden, auch
kommerziell, sofern die GIS-Akademie als Urheber genannt und auf die Lizenz
verwiesen wird.

Vollständiger Lizenztext: https://creativecommons.org/licenses/by/4.0/legalcode.de
Kurzfassung:             https://creativecommons.org/licenses/by/4.0/deed.de
"""

MODS = load()  # vor dem Loeschen laden, damit Fehler in den Symboldateien nichts zerstoeren
for sub in ("collections",) if IN_PLACE else ("collections", "tools"):
    shutil.rmtree(os.path.join(ROOT, sub), ignore_errors=True)
os.makedirs(ROOT, exist_ok=True)
# Nur fuer die Vorschaubilder; Arial ist metrisch gleich und dient unter Windows als Ersatz.
fontb = ImageFont.truetype(find_font(["LiberationSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf"]), 22)
fontr = ImageFont.truetype(find_font(["LiberationSans-Regular.ttf", "arial.ttf", "Arial.ttf"]), 12)


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


ini = ["[general]", "collections=" + ",".join(f"{PRE}_{m.KEY}" for m in MODS), ""]
kat = ["# Symbolkatalog", "", "Punktsymbole liegen als SVG unter `collections/<Sammlung>/svg/`, Linien- und "
       f"Flächensymbole in der Stildatei `collections/<Sammlung>/symbol/{qstil.STIL_DATEI}`.", ""]
counts, stile = {}, {}
for mod in MODS:
    cid = f"{PRE}_{mod.KEY}"
    syms = mod.SYMBOLS
    base = os.path.join(ROOT, "collections", cid)
    os.makedirs(os.path.join(base, "svg"))
    os.makedirs(os.path.join(base, "preview"))
    write(os.path.join(base, "LICENSE"), LIC)
    kat += [f"## {mod.NAME} (`{cid}`, {len(syms)} Symbole)", "", "| Datei | Bedeutung |", "|---|---|"]
    cols, cell = 10, 78
    rows = (len(syms) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell + 24, rows * cell + 64), "white")
    d = ImageDraw.Draw(sheet)
    d.text((14, 12), f"GIS-Akademie Symbole – {mod.NAME}", fill="#1F5F5B", font=fontb)
    for i, (sn, title, fill, outline, elems) in enumerate(syms):
        fn = f"{cid}_{sn}.svg"
        svg = render(elems, Ctx(fill, outline), title)
        etree.fromstring(svg.encode())  # Wohlgeformtheit
        write(os.path.join(base, "svg", fn), svg)
        im = raster(svg, 60)
        sheet.paste(im, (12 + (i % cols) * cell + 9, 52 + (i // cols) * cell + 8), im)
        kat.append(f"| `{fn}` | {title} |")
    sheet.save(os.path.join(base, "preview", "preview.png"))
    kat.append("")
    previews = ["preview/preview.png"]
    stil = qstil.eintraege(mod)
    if stil:
        os.makedirs(os.path.join(base, "symbol"))
        xml = qstil.stil_xml([(typ, qstil.qgis_name(mod, t), eb) for typ, t, eb in stil], cid)
        etree.fromstring(xml.encode())  # Wohlgeformtheit
        write(os.path.join(base, "symbol", qstil.STIL_DATEI), xml)
        qstil.blatt(mod, raster, fontb, fontr).save(os.path.join(base, "preview", "linien_flaechen.png"))
        previews.append("preview/linien_flaechen.png")
        kat += [f"### {mod.NAME}: Linien und Flächen ({len(stil)} Symbole)", "", "| Symbol in QGIS | Art |", "|---|---|"]
        kat += [f"| {qstil.qgis_name(mod, t)} | {'Linie' if typ == 'line' else 'Fläche'} |" for typ, t, eb in stil]
        kat.append("")
        stile[mod.KEY] = len(stil)
    nl, nf = len(getattr(mod, "LINIEN", [])), len(getattr(mod, "FLAECHEN", []))
    desc = mod.DESC + (f". Dazu {nl} Linien- und {nf} Flächensymbole als QGIS-Stil" if stil else "")
    counts[mod.KEY] = len(syms)
    ini += [f"[{cid}]", f"name=GIS-Akademie Symbole: {mod.NAME}", "author=GIS-Akademie", f"tags={mod.TAGS}",
            f"description={desc}", f"version={VERSION}", "qgis_minimum_version=3.0", "qgis_maximum_version=4.99",
            "license=CC BY 4.0", "license_file=LICENSE", "preview=" + ",".join(previews), ""]
write(os.path.join(ROOT, "metadata.ini"), "\n".join(ini))
write(os.path.join(ROOT, "KATALOG.md"), "\n".join(kat))
write(os.path.join(ROOT, "LICENSE"), LIC)
if not IN_PLACE:
    os.makedirs(os.path.join(ROOT, "tools"))
    for f in sorted(glob.glob(os.path.join(HERE, "*.py"))):
        shutil.copy(f, os.path.join(ROOT, "tools", os.path.basename(f)))
print("total", sum(counts.values()), counts)
print("Linien und Flaechen", sum(stile.values()), stile)
print("Modus:", "im Repository (tools/ unveraendert)" if IN_PLACE else "neues Repository inkl. tools/")
