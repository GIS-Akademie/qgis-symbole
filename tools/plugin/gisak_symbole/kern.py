"""Traegt die Sammlungen in eine QGIS-Stildatenbank ein und entfernt sie wieder (ohne Oberflaeche nutzbar).

Aufbau des Plugins:
  sammlungen.json          Liste der Sammlungen (Schluessel, Name, Beschreibung, Symbolzahlen)
  symbole/<key>/*.svg      Punktsymbole
  stile/<key>/*.xml        QGIS-Stildateien; SVG-Markierungen stehen darin nur mit ihrem Dateinamen

Symbolname "<Sammlung>: <Titel>" wie bei der Installation ueber Resource Sharing (ohne dessen Klammerzusatz).
Schlagwort ist allein der Name der Sammlung, z. B. "Forst": kurz genug fuer die Auswahlliste der Symbolauswahl,
und QGIS zeigt dort ohnehin nur die Symbole der passenden Art (Punkt, Linie oder Flaeche).
"""
import json
import os

from qgis.core import QgsReadWriteContext, QgsSettings, QgsStyle, QgsSymbolLayerUtils
from qgis.PyQt.QtXml import QDomDocument

ORDNER = os.path.dirname(os.path.abspath(__file__))
SYMBOLE = os.path.join(ORDNER, "symbole")
STILE = os.path.join(ORDNER, "stile")
SVG_SCHLUESSEL = "svg/searchPathsForSVG"
EINSTELLUNG = "gisak_symbole/"
SYMBOL = QgsStyle.SymbolEntity
TAG = QgsStyle.TagEntity


def sammlungen():
    """Liste der Sammlungen als dict mit key, name, titel, beschreibung, punkte, linien, flaechen."""
    with open(os.path.join(ORDNER, "sammlungen.json"), encoding="utf-8") as f:
        return json.load(f)


def version():
    with open(os.path.join(ORDNER, "metadata.txt"), encoding="utf-8") as f:
        for zeile in f:
            if zeile.startswith("version="):
                return zeile.split("=", 1)[1].strip()
    return ""


def anzahl(s):
    return s["punkte"] + s["linien"] + s["flaechen"]


def _stildateien(s):
    d = os.path.join(STILE, s["key"])
    return [os.path.join(d, fn) for fn in sorted(os.listdir(d)) if fn.endswith(".xml")]


SCHEMA = "2"  # Fassung der Schlagworte; geht in stand() ein, damit alte Eintraege umgestellt werden


def _alte_schlagworte(stil, s):
    """Schlagworte frueherer Fassungen: "GIS-Akademie Symbole: <Sammlung>/Punkte" und ".../Linien_und_Flaechen"."""
    return [t for t in stil.tags() if t.startswith(s["name"] + "/")]


def _lesen(s, datei):
    """Symbole einer Stildatei als Liste (name, QgsSymbol); SVG-Dateinamen werden zu vollen Pfaden."""
    doc = QDomDocument()
    with open(datei, "rb") as f:
        if not doc.setContent(f.read()):
            raise ValueError("Stildatei nicht lesbar: " + datei)
    svg = os.path.join(SYMBOLE, s["key"])
    props = doc.elementsByTagName("prop")
    for i in range(props.count()):
        e = props.at(i).toElement()
        v = e.attribute("v")
        if e.attribute("k") == "name" and v.lower().endswith(".svg") and "/" not in v and "\\" not in v:
            e.setAttribute("v", os.path.join(svg, v).replace("\\", "/"))
    kontext = QgsReadWriteContext()
    aus = []
    e = doc.documentElement().firstChildElement("symbols").firstChildElement("symbol")
    while not e.isNull():
        sym = QgsSymbolLayerUtils.loadSymbol(e, kontext)
        if sym is not None:
            aus.append((e.attribute("name"), sym))
        e = e.nextSiblingElement("symbol")
    return aus


def entfernen(stil, s, schritt=None, behalten=()):
    """Entfernt die Symbole einer Sammlung samt ihren Schlagworten; gibt die Zahl der Symbole zurueck.
    Geloescht wird nur, was das Schlagwort der Sammlung traegt und wie ihre Symbole heisst.
    behalten: Namen, die bleiben (zum Aufraeumen nach dem Auffrischen). schritt: wie bei eintragen."""
    n = 0
    vorsatz = s["titel"] + ": "
    for tag in [t for t in stil.tags() if t == s["titel"]] + _alte_schlagworte(stil, s):
        tid = stil.tagId(tag)
        for name in stil.symbolsWithTag(SYMBOL, tid):
            if name in behalten:
                continue
            if name.startswith(vorsatz) and stil.removeSymbol(name):
                n += 1
            if schritt is not None and schritt() is False:
                return n
        if not stil.symbolsWithTag(SYMBOL, tid):
            stil.remove(TAG, tid)
    return n


def eintragen(stil, s, schritt=None):
    """Traegt die Symbole einer Sammlung ein (gleichnamige werden ersetzt); gibt die Menge ihrer Namen zurueck,
    bei Abbruch None. schritt: Funktion ohne Argumente, wird nach jedem Symbol gerufen; gibt sie False zurueck,
    wird abgebrochen."""
    namen = set()
    tag = s["titel"]
    if not stil.tagId(tag):
        stil.addTag(tag)
    alt = _alte_schlagworte(stil, s)
    for datei in _stildateien(s):
        for name, sym in _lesen(s, datei):
            if stil.addSymbol(name, sym, True):
                if alt:
                    stil.detagSymbol(SYMBOL, name, alt)
                stil.tagSymbol(SYMBOL, name, [tag])
                namen.add(name)
            if schritt is not None and schritt() is False:
                return None
    return namen


# ---- Einstellungen ----

def installiert():
    """Schluessel der eingetragenen Sammlungen; None, solange das Plugin noch nie etwas eingetragen hat."""
    w = QgsSettings().value(EINSTELLUNG + "sammlungen", None)
    if w is None:
        return None
    if isinstance(w, str):
        w = [w] if w else []
    return [k for k in w if k]


def stand(s):
    """Kennung des Inhalts einer Sammlung samt Ort der SVGs: aendert sie sich, muss neu eingetragen werden."""
    return SCHEMA + "|" + str(s["stand"]) + "|" + SYMBOLE.replace("\\", "/")


def staende():
    """Gemerkte Kennungen der eingetragenen Sammlungen als dict key -> stand."""
    try:
        w = json.loads(QgsSettings().value(EINSTELLUNG + "stand", "{}") or "{}")
        return w if isinstance(w, dict) else {}
    except ValueError:
        return {}


def merken(st):
    """st: dict key -> stand der Sammlungen, die jetzt eingetragen sind."""
    e = QgsSettings()
    e.setValue(EINSTELLUNG + "sammlungen", list(st))
    e.setValue(EINSTELLUNG + "stand", json.dumps(st))


def unbekannt(alle):
    """Sammlungen, die seit dem letzten Start neu im Plugin sind und noch nicht eingetragen wurden."""
    w = QgsSettings().value(EINSTELLUNG + "bekannt", None)
    if isinstance(w, str):
        w = [w] if w else []
    keys = set(w or []) | set(installiert() or [])
    return [s for s in alle if s["key"] not in keys]


def bekannt_merken(alle):
    QgsSettings().setValue(EINSTELLUNG + "bekannt", [s["key"] for s in alle])


def veraltet(alle):
    """Eingetragene Sammlungen, deren Inhalt sich seit dem Eintragen geaendert hat (neue Plugin-Version)."""
    st = staende()
    keys = installiert() or []
    return [s for s in alle if s["key"] in keys and st.get(s["key"]) != stand(s)]


def svg_suchpfad(an=True):
    """Nimmt den Ordner der Punktsymbole in die SVG-Suchpfade von QGIS auf (oder heraus). Damit erscheinen die
    Symbole in der SVG-Auswahl, und Projekte speichern den Pfad relativ zu diesem Ordner."""
    e = QgsSettings()
    w = e.value(SVG_SCHLUESSEL, [])
    if w is None:
        w = []
    if isinstance(w, str):
        w = [w] if w else []
    eigen = os.path.normcase(os.path.normpath(SYMBOLE))
    rest = [p for p in w if p and os.path.normcase(os.path.normpath(p)) != eigen]
    neu = rest + [SYMBOLE.replace("\\", "/")] if an else rest
    if neu != list(w):
        e.setValue(SVG_SCHLUESSEL, neu)
