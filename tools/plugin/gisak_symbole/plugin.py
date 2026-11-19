"""Oberflaeche: Menueeintrag und Dialog zur Auswahl der Sammlungen."""
import os

from qgis.core import Qgis, QgsStyle
from qgis.PyQt.QtCore import Qt, QTimer
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import (QApplication, QCheckBox, QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
                                 QListWidget, QListWidgetItem, QProgressDialog, QPushButton, QVBoxLayout)

try:  # Qt 6
    from qgis.PyQt.QtGui import QAction
except ImportError:  # Qt 5
    from qgis.PyQt.QtWidgets import QAction

from . import kern

TITEL = "GIS-Akademie Symbole"
AN, AUS = Qt.CheckState.Checked, Qt.CheckState.Unchecked


def _zahlen(s):
    teile = []
    for n, ein, mehr in ((s["punkte"], "Punkt", "Punkte"), (s["linien"], "Linie", "Linien"),
                         (s["flaechen"], "Fläche", "Flächen")):
        if n:
            teile.append(f"{n} {ein if n == 1 else mehr}")
    return ", ".join(teile)


class Auswahl(QDialog):
    """Liste der Sammlungen zum An- und Abwaehlen."""

    def __init__(self, sammlungen, gewaehlt, parent=None):
        super().__init__(parent)
        self.setWindowTitle(TITEL)
        self.resize(560, 620)
        lay = QVBoxLayout(self)
        text = QLabel("Angehakte Sammlungen stehen in der Symbolauswahl von QGIS bereit: die Punkt-, Linien- und "
                      "Flächensymbole unter dem Namen der Sammlung als Schlagwort (z. B. „Forst“), die SVG-Dateien zusätzlich "
                      "in der SVG-Auswahl. Abgewählte Sammlungen werden aus der Symbolauswahl entfernt; "
                      "Projekte, die deren Symbole schon verwenden, bleiben unverändert.")
        text.setWordWrap(True)
        lay.addWidget(text)
        self.liste = QListWidget()
        for s in sammlungen:
            it = QListWidgetItem(f"{s['titel']}  –  {_zahlen(s)}")
            it.setToolTip(s["beschreibung"])
            it.setData(Qt.ItemDataRole.UserRole, s["key"])
            it.setFlags(it.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            it.setCheckState(AN if s["key"] in gewaehlt else AUS)
            self.liste.addItem(it)
        self.liste.itemChanged.connect(self._summe)
        lay.addWidget(self.liste)
        zeile = QHBoxLayout()
        for beschriftung, zustand in (("Alle", AN), ("Keine", AUS)):
            b = QPushButton(beschriftung)
            b.clicked.connect(lambda _=False, z=zustand: self._alle(z))
            zeile.addWidget(b)
        self.summe = QLabel()
        zeile.addWidget(self.summe, 1, Qt.AlignmentFlag.AlignRight)
        lay.addLayout(zeile)
        self.neu = QCheckBox("Bereits eingetragene Sammlungen neu eintragen (setzt geänderte Symbole zurück)")
        lay.addWidget(self.neu)
        knoepfe = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        knoepfe.accepted.connect(self.accept)
        knoepfe.rejected.connect(self.reject)
        lay.addWidget(knoepfe)
        self._sammlungen = {s["key"]: s for s in sammlungen}
        self._summe()

    def _alle(self, zustand):
        for i in range(self.liste.count()):
            self.liste.item(i).setCheckState(zustand)

    def gewaehlt(self):
        return [self.liste.item(i).data(Qt.ItemDataRole.UserRole) for i in range(self.liste.count())
                if self.liste.item(i).checkState() == AN]

    def _summe(self, *_):
        keys = self.gewaehlt()
        n = sum(kern.anzahl(self._sammlungen[k]) for k in keys)
        self.summe.setText(f"{len(keys)} Sammlungen, {n} Symbole")


class GisakSymbole:
    def __init__(self, iface):
        self.iface = iface
        self.aktion = None

    # ---- Plugin-Schnittstelle ----

    def initGui(self):
        self.aktion = QAction(QIcon(os.path.join(kern.ORDNER, "icon.svg")), "Sammlungen auswählen …",
                              self.iface.mainWindow())
        self.aktion.triggered.connect(self.dialog)
        self.iface.addPluginToMenu(TITEL, self.aktion)
        kern.svg_suchpfad(True)
        if self.iface.mainWindow().isVisible():      # im laufenden QGIS installiert
            QTimer.singleShot(0, self.pruefen)
        else:                                        # beim Start von QGIS: erst, wenn die Oberflaeche steht
            self.iface.initializationCompleted.connect(self.pruefen)

    def unload(self):
        # Die Symbole bleiben in der Stildatenbank (unload laeuft auch beim Beenden von QGIS).
        try:
            self.iface.initializationCompleted.disconnect(self.pruefen)
        except (TypeError, RuntimeError):
            pass
        if self.aktion is not None:
            self.iface.removePluginMenu(TITEL, self.aktion)
            self.aktion = None

    # ---- Ablauf ----

    def pruefen(self):
        """Erster Start: Auswahl anbieten. Neue Plugin-Version: geaenderte Sammlungen auffrischen."""
        alle = kern.sammlungen()
        keys = kern.installiert()
        if keys is None:
            self.dialog()
        else:
            if kern.veraltet(alle):
                self.anwenden(keys)
            neu = kern.unbekannt(alle)
            if neu:
                self.iface.messageBar().pushMessage(
                    TITEL, "Neue Sammlungen verfügbar: " + ", ".join(s["titel"] for s in neu)
                    + ". Eintragen über Erweiterungen › GIS-Akademie Symbole › Sammlungen auswählen …",
                    Qgis.MessageLevel.Info, 30)
        kern.bekannt_merken(alle)

    def dialog(self):
        alle = kern.sammlungen()
        keys = kern.installiert()
        dlg = Auswahl(alle, [s["key"] for s in alle] if keys is None else keys, self.iface.mainWindow())
        if dlg.exec():
            self.anwenden(dlg.gewaehlt(), neu=dlg.neu.isChecked())

    def anwenden(self, gewaehlt, neu=False):
        alle = kern.sammlungen()
        vorher = kern.installiert() or []
        alt = [s["key"] for s in kern.veraltet(alle)]
        weg = [s for s in alle if s["key"] in vorher and s["key"] not in gewaehlt]
        dazu = [s for s in alle if s["key"] in gewaehlt and (neu or s["key"] not in vorher or s["key"] in alt)]
        st = {k: v for k, v in kern.staende().items() if k in vorher}   # was gerade eingetragen ist
        if not weg and not dazu:
            kern.merken(st)
            return
        stil = QgsStyle.defaultStyle()
        gesamt = sum(kern.anzahl(s) for s in dazu + weg)
        fortschritt = QProgressDialog("Symbole werden eingetragen …", "Abbrechen", 0, gesamt, self.iface.mainWindow())
        fortschritt.setWindowTitle(TITEL)
        fortschritt.setWindowModality(Qt.WindowModality.WindowModal)
        fortschritt.setMinimumDuration(0)
        stand = [0]

        def schritt():
            stand[0] += 1
            if stand[0] % 10 == 0:
                fortschritt.setValue(min(stand[0], gesamt - 1))
                QApplication.processEvents()
            return not fortschritt.wasCanceled()

        n_weg = n_dazu = 0
        fehler = None
        try:
            for s in weg:
                if fortschritt.wasCanceled():
                    break
                fortschritt.setLabelText(f"{s['titel']} wird entfernt …")
                QApplication.processEvents()
                n_weg += kern.entfernen(stil, s, schritt)
                if not fortschritt.wasCanceled():
                    st.pop(s["key"], None)
            for s in dazu:
                if fortschritt.wasCanceled():
                    break
                fortschritt.setLabelText(f"{s['titel']} wird eingetragen …")
                QApplication.processEvents()
                st[s["key"]] = ""                        # ab jetzt (teilweise) eingetragen
                namen = kern.eintragen(stil, s, schritt)
                if namen is None:                        # abgebrochen: beim naechsten Mal auffrischen
                    break
                n_dazu += len(namen)
                kern.entfernen(stil, s, behalten=namen)  # Symbole, die es in dieser Fassung nicht mehr gibt
                st[s["key"]] = kern.stand(s)
        except Exception as e:  # Stildatenbank gesperrt, Datei fehlt ...
            fehler = str(e)
        fortschritt.setValue(gesamt)
        kern.merken(st)
        leiste = self.iface.messageBar()
        if fehler:
            leiste.pushMessage(TITEL, "Fehler beim Eintragen: " + fehler, Qgis.MessageLevel.Critical)
            return
        teile = []
        if n_dazu:
            teile.append(f"{n_dazu} Symbole eingetragen")
        if n_weg:
            teile.append(f"{n_weg} Symbole entfernt")
        if fortschritt.wasCanceled():
            teile.append("abgebrochen")
        leiste.pushMessage(TITEL, ", ".join(teile) or "keine Änderung", Qgis.MessageLevel.Success)
