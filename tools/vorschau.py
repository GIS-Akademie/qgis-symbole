"""Kontrollbild einer Sammlung mit Symbolnamen, zum Pruefen beim Zeichnen.

Aufruf:  python tools/vorschau.py <sammlung> <ausgabe.png> [spalten] [symbolgroesse]
  z. B.  python tools/vorschau.py planzv C:\\Temp\\planzv.png
Die Symbole stehen in der Reihenfolge der Symboldatei; es wird nichts im Repository veraendert.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Ctx, render, find_font
from sammlungen import load, raster
from PIL import Image, ImageDraw, ImageFont

if len(sys.argv) < 3:
    sys.exit(__doc__)
mod = load(sys.argv[1])[0]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 10
size = int(sys.argv[4]) if len(sys.argv) > 4 else 72
cw, ch = size + 28, size + 30
font = ImageFont.truetype(find_font(["LiberationSans-Regular.ttf", "arial.ttf", "Arial.ttf"]), 10)
syms = mod.SYMBOLS
rows = (len(syms) + cols - 1) // cols
sheet = Image.new("RGB", (cols * cw + 8, rows * ch + 8), "white")
d = ImageDraw.Draw(sheet)
for i, (sn, title, fill, outline, elems) in enumerate(syms):
    x, y = 4 + (i % cols) * cw, 4 + (i // cols) * ch
    d.rectangle([x + 13, y + 1, x + 14 + size + 1, y + 2 + size + 1], outline="#DDDDDD")
    im = raster(render(elems, Ctx(fill, outline), title), size)
    sheet.paste(im, (x + 14, y + 2), im)
    label = sn if len(sn) <= 19 else sn[:18] + "…"
    w = d.textlength(label, font=font)
    d.text((x + cw / 2 - w / 2, y + size + 6), label, fill="#333333", font=font)
sheet.save(sys.argv[2])
print(mod.KEY, len(syms), "Symbole ->", sys.argv[2])
