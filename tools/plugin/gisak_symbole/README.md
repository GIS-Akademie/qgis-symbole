# GIS-Akademie Symbole

QGIS plugin that adds the GIS-Akademie symbol library to the symbol selector: SVG point symbols plus line and
fill symbols for German planning and utility maps (zoning plan signs after PlanZV, regional planning, land use mapping,
electricity, pipelines, renewable energy, water, soil, noise, nature conservation, landscape planning, forestry,
agriculture, traffic, tourism and sports, heritage, fire and disaster control, surveying, north arrows, map
layout, general signs). Symbol names and the dialog are in German.

## Usage

1. Install the plugin. On first start a list of all collections appears; tick the ones you need and confirm.
2. The symbols are then available in the symbol selector of point, line and polygon layers. Each collection has
   one tag named after the collection (e.g. `Forst`, `PlanZV`); symbols are named `<collection>: <title>`.
3. The point symbols are also available as SVG files in the SVG selector (group `symbole`). Fill and stroke
   colour can be changed in QGIS.
4. Change the selection at any time via **Plugins › GIS-Akademie Symbole › Sammlungen auswählen …**.
   Unticked collections are removed from the symbol selector; projects that already use their symbols keep them.

Before uninstalling the plugin, untick all collections; otherwise the entries stay in the style database without
their SVG files. After a plugin update only collections whose symbols have changed are written again; symbols
you modified under the same name are overwritten.

## Kurzfassung auf Deutsch

Das Plugin trägt die Symbolbibliothek der GIS-Akademie in die Symbolauswahl von QGIS ein. Beim ersten Start die
gewünschten Sammlungen anhaken; später über **Erweiterungen › GIS-Akademie Symbole › Sammlungen auswählen …**.
Jede Sammlung hat ein Schlagwort mit ihrem Namen, die Symbole heißen `<Sammlung>: <Bezeichnung>`. Vor dem
Deinstallieren alle Sammlungen abwählen. Ausführliche Anleitung, Symbolkatalog und Quellen:
<https://github.com/GIS-Akademie/qgis-symbole>

## Licence

- Code: GNU General Public License, version 2 or (at your option) any later version, see `LICENSE`.
- Symbols (folders `symbole` and `stile`): © GIS-Akademie, at your option either under the GNU General Public
  License, version 2 or later (`LICENSE`), or under Creative Commons Attribution 4.0 International
  (`LICENSE_SYMBOLE`). When using CC BY 4.0, credit “GIS-Akademie”.
