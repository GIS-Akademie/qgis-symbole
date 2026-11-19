"""Liste der Sammlungen und gemeinsame Helfer fuer mkrepo.py und vorschau.py.

Jede Sammlung ist ein Modul sym_<schluessel>.py mit
  KEY      Schluessel, wird Teil der Dateinamen (gisak_<KEY>_<name>.svg)
  NAME     Anzeigename
  DESC     Beschreibung fuer metadata.ini
  TAGS     Schlagworte fuer metadata.ini
  SYMBOLS  Liste von (name, titel, fuellfarbe, strichfarbe, [grundformen])
und wahlweise (siehe qstil.py)
  LINIEN   Liste von (titel, [ebenen]) fuer Liniensymbole
  FLAECHEN Liste von (titel, [ebenen]) fuer Flaechensymbole
"""
import importlib, os, re, subprocess, sys, tempfile
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MODULES = ["sym_planzv", "sym_raumordnung", "sym_realnutzung", "sym_strom", "sym_leitungen", "sym_eeg", "sym_waermeplanung", "sym_wasser", "sym_boden",
           "sym_laerm", "sym_stadtklima", "sym_naturschutz", "sym_landschaftsplanung", "sym_forst", "sym_landwirtschaft",
           "sym_verkehr", "sym_tourismus", "sym_denkmal", "sym_brandschutz", "sym_vermessung", "sym_nordpfeile",
           "sym_layout", "sym_allgemein"]
PRE = "gisak"


def load(only=None):
    """Sammlungen laden und pruefen. only = Schluessel einer einzelnen Sammlung."""
    import qstil
    mods = []
    for m in MODULES:
        if only and m != f"sym_{only}":
            continue
        mod = importlib.import_module(m)
        seen = set()
        for sym in mod.SYMBOLS:
            name = sym[0]
            if not re.fullmatch(r"[a-z0-9_]+", name):
                sys.exit(f"{m}: ungueltiger Symbolname '{name}' (nur a-z, 0-9, _)")
            if name in seen:
                sys.exit(f"{m}: Symbolname '{name}' doppelt vergeben")
            seen.add(name)
        titel = set()
        for typ, t, ebenen in qstil.eintraege(mod):
            if t in titel or re.search(r"[&<>\"]", t):
                sys.exit(f"{m}: Titel '{t}' doppelt vergeben oder mit unzulaessigem Zeichen")
            titel.add(t)
            try:
                qstil.pruefe(typ, t, ebenen)
            except ValueError as err:
                sys.exit(f"{m}: {err}")
        mods.append(mod)
    if not mods:
        sys.exit(f"Sammlung '{only}' nicht gefunden. Vorhanden: " + ", ".join(m[4:] for m in MODULES))
    return mods


def raster(svgtext, size, height=None):
    """SVG mit rsvg-convert in ein RGBA-Bild umwandeln (param()-Angaben werden auf die Vorgabe reduziert)."""
    data = re.sub(r"param\([^)]*\)\s*", "", svgtext)
    t = tempfile.NamedTemporaryFile(suffix=".svg", delete=False)
    t.write(data.encode())
    t.close()
    out = t.name + ".png"
    try:
        subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(height or size), t.name, "-o", out], check=True,
                       timeout=120)
    except FileNotFoundError:
        os.unlink(t.name)
        sys.exit("rsvg-convert nicht gefunden. Das Programm (Paket librsvg) muss im PATH liegen.")
    im = Image.open(out).convert("RGBA")
    im.load()
    os.unlink(t.name)
    os.unlink(out)
    return im
