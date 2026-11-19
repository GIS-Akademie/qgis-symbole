"""Baut aus dem erzeugten Repository das QGIS-Plugin "GIS-Akademie Symbole" als ZIP.

Aufruf:  python tools\\mkplugin.py [<zielordner>]        (Vorgabe: dist im Repository)

Vorher `python tools\\mkrepo.py .` laufen lassen: Das Plugin enthaelt die SVGs und Stildateien aus collections/
und die Angaben aus metadata.ini, dazu den Code aus tools/plugin/gisak_symbole. Das ZIP laesst sich in QGIS ueber
"Erweiterungen > Aus ZIP installieren" einspielen. Die Versionsnummer ist VERSION aus mkrepo.py. Das Plugin
merkt sich je Sammlung eine Kennung der Stildateien (`stand` in sammlungen.json) und traegt nach einem Update nur
die Sammlungen neu ein, deren Stildateien sich geaendert haben.
"""
import configparser
import hashlib
import json
import os
import re
import sys
import zipfile

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
QUELLE = os.path.join(HIER, "plugin", "gisak_symbole")
NAME = "gisak_symbole"
ZEIT = (2026, 1, 1, 0, 0, 0)  # fester Zeitstempel: gleicher Inhalt ergibt das gleiche ZIP

LIZENZ = """GIS-Akademie Symbole (QGIS-Plugin)

Programmcode (*.py): GNU General Public License, Version 2 oder (nach Wahl) jede spaetere Version,
https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

Symbole (Ordner symbole und stile): Creative Commons Namensnennung 4.0 International (CC BY 4.0),
siehe LICENSE_SYMBOLE. Namensnennung: GIS-Akademie, https://github.com/GIS-Akademie/qgis-symbole
"""


def _konstante(name):
    text = open(os.path.join(HIER, "mkrepo.py"), encoding="utf-8").read()
    return re.search(rf'^{name} = "([^"]*)"', text, re.M).group(1)


def _lesen(pfad):
    with open(pfad, "rb") as f:
        return f.read()


def main():
    ziel = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "dist")
    version = _konstante("VERSION")
    ini = configparser.ConfigParser(interpolation=None)
    ini.read(os.path.join(REPO, "metadata.ini"), encoding="utf-8")
    dateien = {}  # Pfad im ZIP -> bytes
    liste = []
    for cid in [c.strip() for c in ini.get("general", "collections").split(",")]:
        key = cid.split("_", 1)[1]
        coll = os.path.join(REPO, "collections", cid)
        svgs = sorted(f for f in os.listdir(os.path.join(coll, "svg")) if f.endswith(".svg"))
        for f in svgs:
            dateien[f"symbole/{key}/{f}"] = _lesen(os.path.join(coll, "svg", f))
        zahl = {"line": 0, "fill": 0, "marker": 0}
        stand = hashlib.sha1()
        for f in sorted(os.listdir(os.path.join(coll, "symbol"))):
            if f.endswith(".xml"):
                daten = _lesen(os.path.join(coll, "symbol", f))
                dateien[f"stile/{key}/{f}"] = daten
                stand.update(f.encode("utf-8") + b"\0" + daten)
                for art in re.findall(r'^    <symbol type="(\w+)"', daten.decode("utf-8"), re.M):
                    zahl[art] += 1
        if zahl["marker"] != len(svgs):
            sys.exit(f"{cid}: {len(svgs)} SVGs, aber {zahl['marker']} Punktsymbole in der Stildatei")
        name = ini.get(cid, "name")
        liste.append(dict(key=key, name=name, titel=name.split(": ", 1)[1], beschreibung=ini.get(cid, "description"),
                          punkte=zahl["marker"], linien=zahl["line"], flaechen=zahl["fill"],
                          stand=stand.hexdigest()[:16]))
    dateien["sammlungen.json"] = (json.dumps(liste, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    dateien["LICENSE"] = LIZENZ.encode("utf-8")
    dateien["LICENSE_SYMBOLE"] = _lesen(os.path.join(REPO, "LICENSE"))
    for f in sorted(os.listdir(QUELLE)):
        p = os.path.join(QUELLE, f)
        if os.path.isfile(p) and not f.endswith(".pyc"):
            dateien[f] = _lesen(p).replace(b"\r\n", b"\n")
    meta = dateien["metadata.txt"].decode("utf-8")
    for platz, wert in (("VERSION", version), ("EMAIL", _konstante("EMAIL")), ("SAMMLUNGEN", len(liste)),
                        ("PUNKTE", sum(s["punkte"] for s in liste)),
                        ("STILE", sum(s["linien"] + s["flaechen"] for s in liste))):
        meta = meta.replace(f"@{platz}@", str(wert))
    dateien["metadata.txt"] = meta.encode("utf-8")

    os.makedirs(ziel, exist_ok=True)
    pfad = os.path.join(ziel, f"{NAME}-{version}.zip")
    with zipfile.ZipFile(pfad, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for rel in sorted(dateien):
            info = zipfile.ZipInfo(f"{NAME}/{rel}", ZEIT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, dateien[rel])
    print(f"{pfad}: {len(dateien)} Dateien, {os.path.getsize(pfad) / 1e6:.1f} MB, Version {version}, "
          f"{len(liste)} Sammlungen, {sum(s['punkte'] for s in liste)} Punkte, "
          f"{sum(s['linien'] for s in liste)} Linien, {sum(s['flaechen'] for s in liste)} Flächen")


if __name__ == "__main__":
    main()
