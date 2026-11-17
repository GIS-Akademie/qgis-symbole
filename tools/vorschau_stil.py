"""Kontrollbild der Linien- und Flaechensymbole einer Sammlung, zum Pruefen beim Entwerfen.

Aufruf:  python tools/vorschau_stil.py <sammlung> <ausgabe.png>
  z. B.  python tools/vorschau_stil.py planzv C:\\Temp\\planzv_stil.png
Die Vorschau ist eine Nachbildung der QGIS-Darstellung; es wird nichts im Repository veraendert.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import find_font
from sammlungen import load, raster
import qstil
from PIL import ImageFont

if len(sys.argv) != 3:
    sys.exit(__doc__)
mod = load(sys.argv[1])[0]
if not qstil.eintraege(mod):
    sys.exit(f"Sammlung '{mod.KEY}' hat keine Linien- oder Flaechensymbole.")
fontb = ImageFont.truetype(find_font(["LiberationSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf"]), 22)
fontr = ImageFont.truetype(find_font(["LiberationSans-Regular.ttf", "arial.ttf", "Arial.ttf"]), 12)
qstil.blatt(mod, raster, fontb, fontr).save(sys.argv[2])
print(mod.KEY, len(qstil.eintraege(mod)), "Linien- und Flaechensymbole ->", sys.argv[2])
