"""GIS-Akademie Symbole: Symbolbibliothek als QGIS-Plugin."""


def classFactory(iface):
    from .plugin import GisakSymbole
    return GisakSymbole(iface)
