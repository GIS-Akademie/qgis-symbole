import os, sys, shutil, re, subprocess, importlib, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import Ctx, render, find_font
from PIL import Image, ImageDraw, ImageFont
from lxml import etree

ROOT = sys.argv[1]
CAT = {}
for m in ("sym_a", "sym_b"):
    CAT.update(importlib.import_module(m).CAT)

META = {
 "planzv": ("PlanZV", "Planzeichen für Bauleitpläne in Anlehnung an die Anlage zur Planzeichenverordnung (PlanZV): Gemeinbedarf, Grünflächen, Ver- und Entsorgung, Verkehr, Schutzgebiete, Nebenanlagen, Bauweise", "planzv, bauleitplanung, bebauungsplan, flaechennutzungsplan, planzeichen"),
 "strom": ("Strom", "Symbole für Stromnetze und Leitungspläne: Umspannwerk, Stationen, Kabelverteiler, Masten, Muffen, Schaltzeichen", "strom, netz, energieversorgung, leitungsplan, mittelspannung, niederspannung"),
 "eeg": ("Erneuerbare Energien", "Symbole für die Planung von Wind- und Solarparks und weitere EEG-Anlagen: Windenergieanlagen nach Status, Photovoltaik, Biogas, Wasserkraft, Speicher, Immissionsorte", "eeg, windenergie, photovoltaik, biogas, erneuerbare energien, windpark, solarpark"),
 "naturschutz": ("Naturschutz", "Symbole für Schutzgebiete, Artenschutz und Kompensation: Schutzgebietskategorien, Horst, Brutplatz, Fledermausquartier, Fundpunkte, Maßnahmentypen", "naturschutz, artenschutz, schutzgebiet, kompensation, eingriffsregelung"),
 "landschaftsplanung": ("Landschaftsplanung", "Symbole für Landschaftsplanung und landschaftspflegerische Begleitplanung: Bäume nach Maßnahme, Gehölze, Gewässer, Erholung, Maßnahmenflächen", "landschaftsplanung, lbp, gruenordnung, baum, gehoelz, massnahme"),
 "verkehr": ("Verkehr", "Symbole für Verkehr und Mobilität: Parken, ÖPNV, Bahn, Flughafen, Hafen, Rad, Bauwerke, Verkehrstechnik", "verkehr, mobilitaet, oepnv, parken, bahn, strasse"),
 "wasser": ("Wasserwirtschaft", "Symbole für Wasserwirtschaft: Pegel, Brunnen, Messstellen, Kläranlage, Pumpwerk, Hydranten, Armaturen, Schutzgebiete", "wasser, wasserwirtschaft, abwasser, pegel, hydrant, trinkwasser"),
 "vermessung": ("Vermessung", "Symbole für Vermessung und Kataster: Grenzpunkte, Festpunkte, Passpunkt, Bohrpunkt, Nordpfeil", "vermessung, kataster, festpunkt, grenzpunkt"),
 "allgemein": ("Allgemein", "Allgemeine Kartensymbole für öffentliche Einrichtungen und Orte von Interesse", "poi, oeffentliche einrichtungen, infrastruktur, allgemein"),
}
PRE = "gisak"
LIC = """Creative Commons Namensnennung 4.0 International (CC BY 4.0)

Copyright (c) 2026 GIS-Akademie

Die Symbole dieser Sammlung dürfen in jedem Format und Medium vervielfältigt,
weiterverbreitet, verändert und für beliebige Zwecke genutzt werden, auch
kommerziell, sofern die GIS-Akademie als Urheber genannt und auf die Lizenz
verwiesen wird.

Vollständiger Lizenztext: https://creativecommons.org/licenses/by/4.0/legalcode.de
Kurzfassung:             https://creativecommons.org/licenses/by/4.0/deed.de
"""

for sub in ("collections", "tools"):
    shutil.rmtree(os.path.join(ROOT, sub), ignore_errors=True)
os.makedirs(ROOT, exist_ok=True)
# Nur fuer die Vorschaubilder; Arial ist metrisch gleich und dient unter Windows als Ersatz.
font = ImageFont.truetype(find_font(["LiberationSans-Regular.ttf", "arial.ttf", "Arial.ttf"]), 13)
fontb = ImageFont.truetype(find_font(["LiberationSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf"]), 22)


def png(svgtext, size):
    data = re.sub(r"param\([^)]*\)\s*", "", svgtext)
    t = tempfile.NamedTemporaryFile(suffix=".svg", delete=False); t.write(data.encode()); t.close()
    out = t.name + ".png"
    subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size), t.name, "-o", out], check=True)
    im = Image.open(out).convert("RGBA"); os.unlink(t.name); os.unlink(out)
    return im


ini = ["[general]", "collections=" + ",".join(f"{PRE}_{c}" for c in CAT), ""]
kat = ["# Symbolkatalog", "", "Alle Dateien liegen unter `collections/<Sammlung>/svg/`.", ""]
total = 0
for cat, syms in CAT.items():
    cid = f"{PRE}_{cat}"
    name, desc, tags = META[cat]
    base = os.path.join(ROOT, "collections", cid)
    os.makedirs(os.path.join(base, "svg")); os.makedirs(os.path.join(base, "preview"))
    open(os.path.join(base, "LICENSE"), "w", encoding="utf-8").write(LIC)
    kat += [f"## {name} (`{cid}`, {len(syms)} Symbole)", "", "| Datei | Bedeutung |", "|---|---|"]
    cols, cell = 8, 96
    rows = (len(syms) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell + 24, rows * cell + 64), "white")
    d = ImageDraw.Draw(sheet)
    d.text((14, 12), f"GIS-Akademie Symbole – {name}", fill="#1F5F5B", font=fontb)
    for i, (sn, title, fill, outline, elems) in enumerate(sorted(syms, key=lambda s: s[0])):
        fn = f"{cid}_{sn}.svg"
        svg = render(elems, Ctx(fill, outline), title)
        etree.fromstring(svg.encode())  # Wohlgeformtheit
        open(os.path.join(base, "svg", fn), "w", encoding="utf-8", newline="\n").write(svg)
        im = png(svg, 72)
        sheet.paste(im, (12 + (i % cols) * cell + 12, 52 + (i // cols) * cell + 10), im)
        kat.append(f"| `{fn}` | {title} |")
        total += 1
    sheet.save(os.path.join(base, "preview", "preview.png"))
    kat.append("")
    ini += [f"[{cid}]", f"name=GIS-Akademie Symbole: {name}", "author=GIS-Akademie", f"tags={tags}",
            f"description={desc}", "version=1.0", "qgis_minimum_version=3.0", "qgis_maximum_version=4.99",
            "license=CC BY 4.0", "license_file=LICENSE", "preview=preview/preview.png", ""]
open(os.path.join(ROOT, "metadata.ini"), "w", encoding="utf-8", newline="\n").write("\n".join(ini))
open(os.path.join(ROOT, "KATALOG.md"), "w", encoding="utf-8", newline="\n").write("\n".join(kat))
open(os.path.join(ROOT, "LICENSE"), "w", encoding="utf-8", newline="\n").write(LIC)
os.makedirs(os.path.join(ROOT, "tools"))
for f in ("lib.py", "sym_a.py", "sym_b.py", "mkrepo.py"):
    shutil.copy(os.path.join(os.path.dirname(os.path.abspath(__file__)), f), os.path.join(ROOT, "tools", f))
print("total", total, {c: len(s) for c, s in CAT.items()})
