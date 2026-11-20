"""Sammlung Wasserwirtschaft: Messstellen, Anlagen, Armaturen, Kanalnetz, Bauwerke am Gewaesser, Gebiete.
Orientierung: Leitungs- und Kanalnetzplaene (DIN 2425), Fliessbild-Schaltzeichen fuer Armaturen,
gebraeuchliche Kurzzeichen der Wasserwirtschaft. Eigene Entwuerfe, keine amtlichen Vorlagen.
Stil: hellblaue Fuellung, blauer Strich 5. Die Rahmenform zeigt die Gruppe:
  Kreis = Messstelle/Entnahme, Quadrat = Anlage oder Bauwerk, Raute = Gebiet,
  ohne Rahmen = Armatur oder Netzelement auf der Leitung (Leitung waagerecht durch die Symbolmitte).
Linien und Flaechen: Trinkwasser und Gebiete dunkelblau, Gewaesser und Regenwasser hellblau, Schmutzwasser
braun, Mischwasser violett (uebliche Kanalnetzfarben); Kanaele mit Fliessrichtungspfeil.
Starkregen (Praefix sr_, Titel "Starkregen ..."): Klassen der Ueberflutungstiefe und der Fliessgeschwindigkeit
nach dem Leitfaden "Kommunales Starkregenrisikomanagement in Baden-Wuerttemberg" (LUBW 2016), Szenarien
selten, aussergewoehnlich, extrem; die Hinweiskarte Starkregengefahren des BKG kennt nur die beiden letzten.
Gewaesseroekologie (Praefix oek_, Titel "Gewaesseroekologie, ..."): Zustandsklassen und Farben nach der
Wasserrahmenrichtlinie (Anhang V Nr. 1.4.2 und 2.5, uebernommen in die OGewV): oekologischer Zustand blau, gruen,
gelb, orange, rot; oekologisches Potenzial in denselben Farben mit grauen Streifen (dunkelgrau = erheblich
veraendert, hellgrau = kuenstlich); chemischer Zustand blau oder rot; Grundwasser gruen oder rot. Strukturklassen
1 bis 7 in den Farben der LAWA-Gewaesserstrukturkartierung. Begriffe Strahlursprung und Trittstein aus dem
Strahlwirkungskonzept. Die Regelwerke lagen nicht vor (Angaben aus Vorwissen). Massnahmen im gestrichelten Quadrat.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "wasser"
NAME = "Wasserwirtschaft"
DESC = ("Symbole für Wasserwirtschaft: Messstellen, Wasserversorgung und Abwasser (Anlagen, Armaturen, "
        "Kanalnetz), Bauwerke am Gewässer, Wasserschutz- und Überschwemmungsgebiete, Starkregengefahren, "
        "Gewässerökologie nach Wasserrahmenrichtlinie (Zustand, Strukturgüte, Durchgängigkeit, Maßnahmen)")
TAGS = "wasser, wasserwirtschaft, abwasser, kanal, pegel, hydrant, trinkwasser, hochwasser, starkregen, wrrl, gewaesseroekologie, strukturguete"

WB = ("#D6ECFA", "#0B5CAD")


def ms(*sh):  # Messstelle
    return fr_circle() + list(sh)


def an(*sh):  # Anlage, Bauwerk
    return fr_square() + list(sh)


def ant(txt, h=30, mw=64):
    return an(T(txt, 50, 50, h, maxw=mw))


def geb(txt, h=28, mw=46):  # Gebiet
    return fr_diamond() + [T(txt, 50, 50, h, maxw=mw)]


def pipe(x0=4, x1=96):
    return L(x0, 50, x1, 50, 5, cap="butt")


def ufer(*sh):  # Bauwerk am Gewaesser: zwei Uferlinien
    return an(L(20, 28, 80, 28, 4.5), L(20, 72, 80, 72, 4.5), *sh)


BOWTIE = [PG([(24, 30), (50, 50), (24, 70)], "F", "S", 5), PG([(76, 30), (50, 50), (76, 70)], "F", "S", 5)]
def mn(*sh):  # Massnahme der Gewaesserentwicklung
    return [R(7, 7, 86, 86, "F", "S", 5, 8, "12 8")] + list(sh)


def tuft(x, y, k=1.0, sw=4):
    return [L(x, y, x, y - 18 * k, sw), L(x, y, x - 10 * k, y - 13 * k, sw), L(x, y, x + 10 * k, y - 13 * k, sw)]


OEK = "Gewässerökologie, "
QUER = L(56, 28, 56, 72, 8, cap="butt")
STAMM = [L(30, 66, 70, 34, 9), L(46, 53, 40, 36, 4.5), L(58, 44, 72, 50, 4.5)]
FISH = [P("M18,50 Q40,28 64,50 Q40,72 18,50 Z", "S", "N", 0), PG([(60, 50), (82, 36), (82, 64)], "S"),
        C(32, 46, 3, "F", "N", 0)]

S = [
    # ---- Messstellen und Entnahme (Kreis) ----
    ("pegel", "Pegel / Wasserstandsmessstelle", *WB,
     ms(R(40, 16, 20, 68, "F", "S", 4), *[L(40, y, 54 if i % 2 else 49, y, 3.5, cap="butt")
                                           for i, y in enumerate(range(25, 80, 8))])),
    ("abflussmessstelle", "Abflussmessstelle", *WB, ms(T("Q", 50, 50, 36))),
    ("grundwassermessstelle", "Grundwassermessstelle", *WB, ms(PG([(27, 34), (73, 34), (50, 74)], "S"))),
    ("guetemessstelle", "Gütemessstelle / Probenahmestelle", *WB,
     ms(PG([(37.5, 58), (62.5, 58), (69, 72), (66, 77), (34, 77), (31, 72)], "S"),
        P("M45,22 V42 L31,72 Q29,77 34,77 H66 Q71,77 69,72 L55,42 V22", "N", "S", 4.5), L(40, 22, 60, 22, 4.5))),
    ("niederschlagsmessstelle", "Niederschlagsmessstelle", *WB,
     ms(cloud([(35, 44, 11), (50, 38, 14), (65, 44, 11)], "F", "S", 4.5), L(36, 62, 32, 75, 4.5), L(50, 62, 46, 75, 4.5),
        L(64, 62, 60, 75, 4.5))),
    ("brunnen", "Brunnen", *WB, ms(T("B", 50, 50, 38))),
    ("trinkwasserentnahme", "Trinkwasserentnahme / Wasserfassung", *WB, ms(*fit(drop("S", "N", 0), 50, 50, 0.66))),
    # ---- Anlagen (Quadrat) ----
    ("wasserwerk", "Wasserwerk", *WB, ant("WW", 28)),
    ("hochbehaelter", "Hochbehälter", *WB, ant("HB")),
    ("wasserturm", "Wasserturm", *WB,
     an(R(27, 20, 46, 24, "S", "N", 0, 4), PG([(43, 44), (57, 44), (64, 82), (36, 82)], "S"))),
    ("pumpwerk", "Pumpwerk", *WB, an(C(50, 50, 28, "N", "S", 4.5), PG([(38, 30), (38, 70), (74, 50)], "S"))),
    ("druckerhoehungsanlage", "Druckerhöhungsanlage", *WB, ant("DEA", 22, 66)),
    ("klaeranlage", "Kläranlage", *WB, ant("KA")),
    ("kleinklaeranlage", "Kleinkläranlage", *WB, ant("KKA", 22, 66)),
    ("regenueberlauf", "Regenüberlauf", *WB, ant("RÜ")),
    ("regenueberlaufbecken", "Regenüberlaufbecken", *WB, ant("RÜB", 22, 66)),
    ("regenrueckhaltebecken", "Regenrückhaltebecken", *WB, ant("RRB", 22, 66)),
    ("regenklaerbecken", "Regenklärbecken", *WB, ant("RKB", 22, 66)),
    ("hochwasserrueckhaltebecken", "Hochwasserrückhaltebecken", *WB, ant("HRB", 22, 66)),
    ("versickerungsanlage", "Versickerungsanlage / Mulde", *WB,
     an(P("M18,32 Q50,52 82,32", "N", "S", 5), *arrow(34, 50, 34, 82, 4.5, 11), *arrow(50, 56, 50, 84, 4.5, 11),
        *arrow(66, 50, 66, 82, 4.5, 11))),
    ("abscheider", "Abscheider (Leichtflüssigkeit, Fett)", *WB, ant("LFA", 22, 66)),
    ("loeschwasserentnahme", "Löschwasserentnahmestelle", *WB, ant("LW", 28)),
    ("trinkbrunnen", "Trinkbrunnen / Zapfstelle", *WB,
     an(R(44, 58, 12, 26, "S", "N", 0), P("M26,48 H74 Q72,62 50,62 Q28,62 26,48 Z", "S", "N", 0),
        P("M50,46 Q50,22 68,32", "N", "S", 4.5))),
    # ---- Armaturen und Einbauten der Wasserversorgung (auf der Leitung) ----
    ("schieber", "Schieber / Absperrarmatur", *WB, [pipe(4, 24), pipe(76, 96)] + BOWTIE),
    ("absperrklappe", "Absperrklappe", *WB,
     [pipe(4, 30), pipe(70, 96), L(30, 28, 30, 72, 5), L(70, 28, 70, 72, 5), L(30, 72, 70, 28, 5), C(50, 50, 6, "S", "N", 0)]),
    ("rueckflussverhinderer", "Rückflussverhinderer", *WB,
     [pipe(4, 30), pipe(70, 96), PG([(30, 30), (30, 70), (68, 50)], "S", "S", 4), L(70, 28, 70, 72, 5.5)]),
    ("druckminderer", "Druckminderer", *WB,
     [pipe(4, 24), pipe(76, 96), PG([(24, 30), (50, 50), (24, 70)], "S", "S", 5), BOWTIE[1]]),
    ("hydrant_unterflur", "Unterflurhydrant", *WB,
     [pipe(4, 20), pipe(80, 96), C(50, 50, 30, "F", "S", 5), T("H", 50, 50, 28)]),
    ("hydrant_ueberflur", "Überflurhydrant", *WB,
     [pipe(4, 22), pipe(78, 96), R(22, 22, 56, 56, "F", "S", 5), T("H", 50, 50, 28)]),
    ("entlueftung", "Be- und Entlüftungsventil", *WB, [pipe(), L(50, 50, 50, 34, 5, cap="butt"), C(50, 22, 12, "F", "S", 5)]),
    ("entleerung", "Entleerung / Spülauslass", *WB,
     [pipe(), L(50, 50, 50, 68, 5, cap="butt"), PG([(38, 66), (62, 66), (50, 88)], "S")]),
    ("wasserzaehler", "Wasserzähler", *WB,
     [pipe(4, 24), pipe(76, 96), R(24, 30, 52, 40, "F", "S", 5, 4), T("m³", 50, 50, 14)]),
    ("hausanschluss", "Hausanschluss", *WB,
     [L(4, 72, 96, 72, 5, cap="butt"), L(50, 72, 50, 42, 5, cap="butt"), R(38, 18, 24, 24, "S", "N", 0)]),
    ("reduzierung", "Reduzierung / Übergangsstück", *WB,
     [L(4, 50, 34, 50, 8, cap="butt"), pipe(66, 96), PG([(34, 30), (66, 42), (66, 58), (34, 70)], "F", "S", 5)]),
    ("endkappe", "Leitungsende / Endkappe", *WB, [pipe(4, 62), L(62, 30, 62, 70, 8, cap="butt")]),
    ("rohrbruch", "Rohrbruch / Schadstelle", *WB, [pipe(4, 26), pipe(74, 96), PG(star(50, 50, 30, 15, 8), "F", "S", 4.5)]),
    # ---- Kanalnetz ----
    ("schacht", "Schacht", *WB,
     [C(50, 50, 34, "F", "S", 5), L(26, 26, 74, 74, 4.5, cap="butt"), L(26, 74, 74, 26, 4.5, cap="butt")]),
    ("strassenablauf", "Straßenablauf", *WB,
     [R(16, 30, 68, 40, "F", "S", 5)] + [L(x, 30, x, 70, 4, cap="butt") for x in (33, 50, 67)]),
    ("einleitstelle", "Einleitstelle / Auslauf", *WB, arrow(22, 14, 56, 56, 6, 15) + [wave(10, 78, 80, 6, 3, 5)]),
    ("dueker", "Düker", *WB, [PL([(4, 34), (26, 34), (38, 68), (62, 68), (74, 34), (96, 34)], 5, cap="butt")]),
    ("drosselbauwerk", "Drosselbauwerk", *WB,
     [pipe(4, 46), pipe(54, 96), PL([(32, 28), (46, 50), (32, 72)], 5), PL([(68, 28), (54, 50), (68, 72)], 5)]),
    # ---- Bauwerke und Orte am Gewaesser (Quadrat) ----
    ("wehr", "Wehr / Querbauwerk", *WB, ufer(PL([(50, 28), (40, 39), (60, 50), (40, 61), (50, 72)], 5))),
    ("schleuse", "Schleuse", *WB, ufer(PL([(34, 28), (46, 50), (34, 72)], 5), PL([(56, 28), (68, 50), (56, 72)], 5))),
    ("sohlgleite", "Sohlgleite / Sohlrampe", *WB,
     ufer(*[C(x, y, 4.5, "S", "N", 0) for x, y in ((36, 40), (52, 44), (66, 38), (42, 58), (60, 60))])),
    ("durchlass", "Durchlass", *WB,
     an(L(16, 50, 84, 50, 5, cap="butt"), P("M36,24 Q48,50 36,76", "N", "S", 5), P("M64,24 Q52,50 64,76", "N", "S", 5))),
    ("fischaufstieg", "Fischaufstiegsanlage", *WB,
     an(*fit(FISH, 50, 40, 0.8), PL([(20, 84), (38, 84), (38, 76), (58, 76), (58, 68), (80, 68)], 4.5))),
    ("schoepfwerk", "Schöpfwerk", *WB,
     an(C(50, 40, 20, "N", "S", 4.5), PG([(42, 27), (42, 53), (65, 40)], "S"), wave(22, 76, 56, 5, 2, 4.5))),
    ("talsperre", "Talsperre / Staudamm", *WB,
     an(P("M64,18 Q44,50 64,82", "N", "S", 9, cap="butt"), wave(16, 40, 30, 4, 2, 4), wave(16, 60, 30, 4, 2, 4))),
    ("hochwassermarke", "Hochwassermarke / Wasserstand", *WB,
     an(PG([(38, 24), (62, 24), (50, 44)], "S"), L(20, 52, 80, 52, 5), L(30, 64, 70, 64, 4.5), L(41, 76, 59, 76, 4))),
    ("furt", "Furt", *WB,
     an(wave(18, 50, 64, 6, 3, 5), *[C(50, y, 4, "S", "N", 0) for y in (20, 32, 68, 80)])),
    ("quelle", "Quelle", *WB, an(C(50, 32, 13, "N", "S", 5), P("M50,45 Q40,56 50,64 T50,86", "N", "S", 5))),
    ("badestelle", "Badestelle / Badegewässer", *WB,
     an(C(34, 36, 8.5, "S", "N", 0), PL([(44, 46), (62, 40), (76, 48)], 6), wave(18, 62, 64, 5, 3, 4.5),
        wave(18, 76, 64, 5, 3, 4.5))),
    # ---- Gebiete (Raute) ----
    ("wasserschutzgebiet", "Wasserschutzgebiet", *WB, geb("WSG", 18, 52)),
    ("wasserschutzgebiet_zone_1", "Wasserschutzgebiet Zone I (Fassungsbereich)", *WB, geb("I", 32)),
    ("wasserschutzgebiet_zone_2", "Wasserschutzgebiet Zone II (engere Schutzzone)", *WB, geb("II", 32)),
    ("wasserschutzgebiet_zone_3", "Wasserschutzgebiet Zone III (weitere Schutzzone)", *WB, geb("III", 32)),
    ("heilquellenschutzgebiet", "Heilquellenschutzgebiet", *WB, geb("HQS", 18, 52)),
    ("ueberschwemmungsgebiet", "Überschwemmungsgebiet", *WB, geb("ÜSG", 18, 52)),
    ("hochwasserrisikogebiet", "Hochwasserrisikogebiet (HQ100)", *WB, geb("HQ100", 14, 56)),
    # ---- Starkregen (Quadrat = Bauwerk oder Objekt, Kreis = Messung, Raute = Gebiet, Pfeil ohne Rahmen) ----
    ("sr_fruehwarnsensor", "Starkregen, Frühwarnsensor / Warnpegel", *WB,
     ms(L(50, 82, 50, 60, 5), C(50, 56, 7, "S", "N", 0), arc(50, 56, 18, -50, 50, 4.5), arc(50, 56, 30, -50, 50, 4.5))),
    ("sr_notwasserweg", "Starkregen, Notwasserweg / Notabflussweg", *WB, ufer(*arrow(22, 50, 80, 50, 6, 15))),
    ("sr_retentionsflaeche", "Starkregen, Retentionsfläche / multifunktionale Fläche", *WB,
     an(PL([(16, 32), (30, 74), (70, 74), (84, 32)], 5), wave(27, 52, 46, 4, 2, 4.5))),
    ("sr_gelaendesenke", "Starkregen, Geländesenke / Überflutungsschwerpunkt", *WB,
     an(E(50, 52, 33, 24, "N", "S", 4.5), E(50, 55, 16, 10, "S", "N", 0))),
    ("sr_kanalueberstau", "Starkregen, Kanalüberstau / Rückstau", *WB,
     an(L(18, 74, 82, 74, 5), R(37, 64, 26, 10, "S", "N", 0), *arrow(50, 62, 50, 20, 5, 13),
        P("M40,56 Q34,38 24,46", "N", "S", 4.5), P("M60,56 Q66,38 76,46", "N", "S", 4.5))),
    ("sr_unterfuehrung", "Starkregen, Überflutungsgefährdete Unterführung", *WB,
     an(L(16, 26, 84, 26, 7, cap="butt"), P("M28,82 V54 A22,22 0 0 1 72,54 V82", "N", "S", 5),
        wave(32, 70, 36, 4, 2, 4.5))),
    ("sr_einlaufbauwerk", "Starkregen, Einlaufbauwerk mit Rechen (Verklausungsgefahr)", *WB,
     an(*arrow(16, 50, 46, 50, 5.5, 13), R(52, 24, 30, 52, "N", "S", 4.5),
        *[L(x, 24, x, 76, 4, cap="butt") for x in (62, 72)])),
    ("sr_risikoobjekt", "Starkregen, Risikoobjekt / gefährdetes Gebäude", *WB,
     an(*fit(house(), 50, 40, 0.62), wave(18, 80, 64, 5, 3, 5))),
    ("sr_objektschutz", "Starkregen, Objektschutz / Schutzeinrichtung", *WB,
     an(*fit(house(), 50, 42, 0.56), PL([(20, 56), (20, 82), (80, 82), (80, 56)], 6))),
    ("sr_gefahrenbereich", "Starkregengefahrenbereich", *WB, geb("SR", 26)),
    ("sr_fliessrichtung", "Starkregen, Fließrichtung (nach rechts, drehbar)", *WB,
     [wave(6, 50, 40, 8, 2, 7)] + arrow(46, 50, 95, 50, 7, 22)),
    # ---- Gewaesseroekologie (Kreis = Messstelle, Quadrat = Bauwerk oder Struktur, gestricheltes Quadrat =
    #      Massnahme, Raute = Wasserkoerper) ----
    ("oek_ueberblick", OEK + "Überblicksmessstelle", *WB, ms(T("Ü", 50, 50, 36))),
    ("oek_operativ", OEK + "operative Messstelle", *WB, ms(T("O", 50, 50, 36))),
    ("oek_makrozoobenthos", OEK + "Probestelle Makrozoobenthos", *WB,
     ms(E(50, 56, 11, 16, "S", "N", 0), C(50, 33, 7, "S", "N", 0),
        *[L(50, y, 50 + d, y - 7, 4) for y in (48, 57, 66) for d in (-24, 24)])),
    ("oek_fische", OEK + "Probestelle Fische / Befischungsstrecke", *WB, ms(*fit(FISH, 50, 50, 0.86))),
    ("oek_wasserpflanzen", OEK + "Probestelle Wasserpflanzen und Algen", *WB,
     ms(P("M36,78 Q26,58 38,44 Q46,34 38,22", "N", "S", 5), P("M52,78 Q62,60 52,46 Q46,36 54,26", "N", "S", 5),
        P("M66,78 Q74,66 66,54", "N", "S", 5))),
    ("oek_strukturkartierung", OEK + "Aufnahmepunkt Strukturkartierung", *WB,
     ms(P("M20,58 Q34,26 50,50 T80,42", "N", "S", 6), L(50, 32, 50, 68, 4, cap="butt"))),
    ("oek_durchgaengig", OEK + "Querbauwerk durchgängig", *WB, ufer(QUER, *arrow(20, 50, 84, 50, 5.5, 14))),
    ("oek_eingeschraenkt_durchgaengig", OEK + "Querbauwerk eingeschränkt durchgängig", *WB,
     ufer(QUER, *arrow(18, 50, 46, 50, 5.5, 13), L(66, 50, 82, 50, 5, dash="2 8"))),
    ("oek_nicht_durchgaengig", OEK + "Querbauwerk nicht durchgängig", *WB,
     ufer(QUER, *arrow(18, 50, 46, 50, 5.5, 13), *xcross(74, 50, 7, 5))),
    ("oek_absturz", OEK + "Absturz / Sohlschwelle", *WB,
     an(PL([(18, 44), (50, 44), (50, 70), (82, 70)], 6), wave(18, 30, 30, 4, 2, 4.5), P("M50,36 Q62,38 62,58", "N", "S", 4.5))),
    ("oek_verrohrung", OEK + "Verrohrung", *WB,
     ufer(L(32, 40, 68, 40, 4.5), L(32, 60, 68, 60, 4.5), E(32, 50, 5, 10, "F", "S", 4.5), E(68, 50, 5, 10, "F", "S", 4.5))),
    ("oek_wasserkraft", OEK + "Wasserkraftanlage", *WB, an(C(50, 50, 30, "N", "S", 5), *rotor(50, 50, 26))),
    ("oek_fischschutz", OEK + "Fischschutz und Fischabstieg", *WB,
     an(*fit(FISH, 36, 50, 0.5), *[L(x, 24, x, 76, 4.5, cap="butt") for x in (62, 72, 82)])),
    ("oek_einleitung", OEK + "Einleitung (Kläranlage, Regenwasser, Industrie)", *WB,
     an(*arrow(50, 16, 50, 58, 7, 17), wave(18, 74, 64, 5, 3, 5))),
    ("oek_entnahme", OEK + "Wasserentnahme / Ausleitung", *WB, an(*arrow(50, 60, 50, 16, 7, 17), wave(18, 74, 64, 5, 3, 5))),
    ("oek_rueckstau", OEK + "Rückstaubereich", *WB,
     an(L(72, 22, 72, 78, 8, cap="butt"), *[L(20, y, 58, y, 4.5) for y in (36, 50, 64)])),
    ("oek_uferverbau", OEK + "Ufer- oder Sohlverbau", *WB,
     an(wave(18, 28, 64, 5, 3, 5), R(20, 44, 60, 30, "N", "S", 4.5), L(20, 59, 80, 59, 4), L(40, 44, 40, 59, 4),
        L(62, 44, 62, 59, 4), L(30, 59, 30, 74, 4), L(52, 59, 52, 74, 4), L(70, 59, 70, 74, 4))),
    ("oek_totholz", OEK + "Totholz / Strukturelement", *WB, ufer(*STAMM)),
    ("oek_laichplatz", OEK + "Kieslaichplatz", *WB,
     an(*fit(FISH, 50, 36, 0.6), *[C(x, y, 4.5, "S", "N", 0) for x, y in ((26, 64), (40, 70), (54, 64), (68, 70), (33, 80), (61, 80), (76, 80))])),
    ("oek_strahlursprung", OEK + "Strahlursprung", *WB, an(*sun(50, 50, 13, "S", "S", 5, 8, 7, 12))),
    ("oek_trittstein", OEK + "Trittstein", *WB, ufer(E(30, 50, 9, 6, "S", "N", 0), E(50, 50, 9, 6, "S", "N", 0), E(70, 50, 9, 6, "S", "N", 0))),
    ("oek_m_durchgaengigkeit", OEK + "Maßnahme Durchgängigkeit herstellen", *WB,
     mn(L(50, 18, 50, 38, 8, cap="butt"), L(50, 62, 50, 82, 8, cap="butt"), *arrow(20, 50, 82, 50, 6, 16))),
    ("oek_m_randstreifen", OEK + "Maßnahme Gewässerrandstreifen anlegen", *WB,
     mn(wave(18, 30, 64, 5, 3, 5.5), L(18, 46, 82, 46, 4, dash="8 7"), *tuft(30, 80, 0.9), *tuft(50, 80, 0.9), *tuft(70, 80, 0.9))),
    ("oek_m_ufer", OEK + "Maßnahme Ufer- oder Sohlverbau entfernen", *WB,
     mn(R(20, 34, 60, 32, "N", "S", 4.5), L(20, 50, 80, 50, 4), L(40, 34, 40, 50, 4), L(60, 50, 60, 66, 4), L(22, 78, 78, 22, 6))),
    ("oek_m_aue", OEK + "Maßnahme Auenanbindung / Altarm anschließen", *WB,
     mn(L(18, 68, 82, 68, 7), P("M30,68 Q50,10 70,68", "N", "S", 5, dash="9 7"))),
    ("oek_m_struktur", OEK + "Maßnahme Strukturelemente einbringen (Totholz, Kies)", *WB,
     mn(*fit(STAMM, 44, 56, 0.9), *cross(74, 26, 9, 5))),
    ("oek_m_unterhaltung", OEK + "Maßnahme angepasste Gewässerunterhaltung", *WB, mn(T("GU", 50, 50, 30, maxw=60))),
    ("oek_owk", OEK + "Oberflächenwasserkörper", *WB, geb("OWK", 17, 52)),
    ("oek_gwk", OEK + "Grundwasserkörper", *WB, geb("GWK", 17, 52)),
    ("oek_hmwb", OEK + "erheblich veränderter Wasserkörper (HMWB)", *WB, geb("HMWB", 13, 56)),
    ("oek_awb", OEK + "künstlicher Wasserkörper (AWB)", *WB, geb("AWB", 17, 52)),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
B0, RW, SWK, MWK = WB[1], "#3FA9F5", "#8B5A2B", "#7B3FA0"


def kanal(farbe):  # Kanal mit Fliessrichtungspfeilen
    return [linie(farbe, 0.6), marken(mk("filled_arrowhead", 1.8, farbe), 12)]


# Starkregen: Klassen wie in den Starkregengefahrenkarten nach dem Leitfaden "Kommunales Starkregenrisikomanagement
# in Baden-Wuerttemberg" (LUBW 2016): Ueberflutungstiefe ab 5 cm in vier Klassen, Fliessgeschwindigkeit in vier
# Klassen. Farben nicht vorgeschrieben: Tiefen in Blautoenen, Geschwindigkeiten gruen bis rot (einzige Ausnahme
# vom Blau der Sammlung, weil die Karten die Gefahr ueber die Farbe zeigen).
SRT = [("5 bis 10 cm", "#C6E2F7"), ("10 bis 50 cm", "#7DB9EC"), ("50 bis 100 cm", "#2F80D0"), ("über 100 cm", "#0A3A82")]
SRV = [("unter 0,2 m/s", "#4CAF50"), ("0,2 bis 0,5 m/s", "#F2C200"), ("0,5 bis 2 m/s", "#F07D00"),
       ("über 2 m/s", "#D0021B")]


# Gewaesseroekologie: Farben der Zustandsklassen nach Wasserrahmenrichtlinie Anhang V, Strukturklassen nach LAWA.
ZUST = [("sehr gut", "#2166C0"), ("gut", "#3DAA35"), ("mäßig", "#F7E000"), ("unbefriedigend", "#F29400"),
        ("schlecht", "#E2001A")]
POT = [("gut und besser", ZUST[1][1])] + ZUST[2:]
STRUKTUR = [("1 (unverändert)", "#0A3A9A"), ("2 (gering verändert)", "#5AB4F0"), ("3 (mäßig verändert)", "#1E8C3A"),
            ("4 (deutlich verändert)", "#9BD34A"), ("5 (stark verändert)", "#F7E000"),
            ("6 (sehr stark verändert)", "#F29400"), ("7 (vollständig verändert)", "#E2001A")]
GUT, SCHLECHT, DGRAU, HGRAU = ZUST[1][1], ZUST[4][1], "#5A5A5A", "#C8C8C8"
OEKL = "Gewässerökologie, "


def fliess(farbe, breite):  # Fliessweg mit Richtungspfeilen, Staerke nach Klasse
    return [linie(farbe, breite), marken(mk("filled_arrowhead", 1.4 + breite, farbe), 9)]


LINIEN = [
    ("Trinkwasser-Hauptleitung", [linie(B0, 0.8)]),
    ("Trinkwasser-Versorgungsleitung", [linie(B0, 0.5)]),
    ("Trinkwasser-Hausanschluss", [linie(B0, 0.25)]),
    ("Rohwasserleitung", [linie(B0, 0.5, [5, 1, 0.5, 1])]),
    ("Leitung geplant", [linie(B0, 0.5, [3, 1.5])]),
    ("Leitung stillgelegt", [linie(B0, 0.4), marken(mk("cross2", 1.5, B0, rw=0.3), 6)]),
    ("Schmutzwasserkanal", kanal(SWK)),
    ("Regenwasserkanal", kanal(RW)),
    ("Mischwasserkanal", kanal(MWK)),
    ("Abwasserdruckleitung", [linie(SWK, 0.5, [5, 1, 0.5, 1])]),
    ("Fließgewässer", [linie(RW, 1.0)]),
    ("Graben", [linie(RW, 0.4)]),
    ("Verrohrtes Gewässer", [linie(RW, 0.8, [3, 1.5])]),
    ("Deich", [linie(B0, 0.4), marken(mk("line", 1.6, B0, rw=0.3, dy=0.8), 1.6)]),
] + [(f"Starkregen, Fließgeschwindigkeit {t}", fliess(c, b)) for (t, c), b in zip(SRV, (0.3, 0.45, 0.6, 0.8))] + [
    ("Starkregen, Fließweg / Abflussbahn", [linie(RW, 0.6, [4, 1]), marken(mk("filled_arrowhead", 1.8, RW), 10)]),
    ("Starkregen, Notwasserweg", [linie(B0 + "59", 2.2), linie(B0, 0.4, [3, 1.5]), marken(mk("filled_arrowhead", 2.0, B0), 12)]),
    ("Starkregen, Schutzlinie / Objektschutz", [linie(B0, 0.8), marken(mk("triangle", 1.4, B0, dy=0.9), 3)]),
] + [(OEKL + f"ökologischer Zustand {t}", [linie(c, 1.2)]) for t, c in ZUST] + [
    (OEKL + f"ökologisches Potenzial {t}, erheblich verändert", [linie(c, 1.2), linie(DGRAU, 1.2, [2, 2])]) for t, c in POT] + [
    (OEKL + f"ökologisches Potenzial {t}, künstlich", [linie(c, 1.2), linie(HGRAU, 1.2, [2, 2])]) for t, c in POT] + [
    (OEKL + "chemischer Zustand gut", [linie(ZUST[0][1], 0.7)]),
    (OEKL + "chemischer Zustand nicht gut", [linie(SCHLECHT, 0.7)]),
] + [(OEKL + f"Strukturklasse {t}", [linie(c, 1.0)]) for t, c in STRUKTUR] + [
    (OEKL + "Strahlursprung", [linie(GUT + "80", 2.6), linie(B0, 0.5)]),
    (OEKL + "Strahlweg", [linie(GUT + "80", 2.6, [3, 1.5]), linie(B0, 0.5)]),
    (OEKL + "Degradationsstrecke", [linie(DGRAU + "66", 2.6), linie(B0, 0.5)]),
    (OEKL + "Gewässerrandstreifen", [linie(RW, 0.6), linie(GUT, 0.5, versatz=1.0), linie(GUT, 0.5, versatz=-1.0)]),
    (OEKL + "Rückstaustrecke", [linie(RW, 1.0), marken(mk("line", 1.8, B0, rw=0.3), 2)]),
    (OEKL + "Renaturierungsstrecke", [linie(RW, 0.8), marken(mk("circle", 1.3, "#FFFFFF", B0, 0.25), 4)]),
    (OEKL + "nicht durchgängiger Abschnitt", [linie(SCHLECHT, 0.8), marken(mk("line", 2.2, SCHLECHT, rw=0.4), 6)]),
]

FLAECHEN = [
    ("Gewässerfläche", [voll("#A9D4F5"), linie(B0, 0.3)]),
    ("Wasserschutzgebiet Zone I", [voll(B0 + "99"), linie(B0, 0.4)]),
    ("Wasserschutzgebiet Zone II", [voll(B0 + "59"), linie(B0, 0.4)]),
    ("Wasserschutzgebiet Zone III", [voll(B0 + "26"), linie(B0, 0.4)]),
    ("Heilquellenschutzgebiet", [schraffur(B0, 0.25, 135, 2.5), linie(B0, 0.4, [4, 1.5])]),
    ("Überschwemmungsgebiet", [voll(RW + "33"), schraffur(B0, 0.25, 0, 2), linie(B0, 0.4)]),
    ("Hochwasserrisikogebiet", [schraffur(B0, 0.25, 45, 3), linie(B0, 0.4, [4, 1.5])]),
    ("Einzugsgebiet", [linie(B0, 0.6, [6, 1.5, 1, 1.5])]),
    ("Versorgungsgebiet, Druckzone", [band(B0 + "59", 1.5), linie(B0, 0.3)]),
    ("Entwässerungsgebiet Mischsystem", [voll(MWK + "26"), linie(MWK, 0.4)]),
    ("Entwässerungsgebiet Trennsystem", [voll(SWK + "26"), linie(SWK, 0.4)]),
    ("Rückhaltebecken, Anlagenfläche", [voll(WB[0]), linie(B0, 0.5)]),
    ("Versickerungsfläche", [muster(mk("circle", 0.6, B0), 2.2, versatz=1.1), linie(B0, 0.4, [3, 1.5])]),
] + [(f"Starkregen, Überflutungstiefe {t}", [voll(c)]) for t, c in SRT] + [
    ("Starkregen, Überflutungsausdehnung seltenes Ereignis", [voll(RW + "99"), linie(B0, 0.3)]),
    ("Starkregen, Überflutungsausdehnung außergewöhnliches Ereignis", [voll(RW + "59"), linie(B0, 0.3, [3, 1])]),
    ("Starkregen, Überflutungsausdehnung extremes Ereignis", [voll(RW + "26"), linie(B0, 0.3, [1, 1])]),
    ("Starkregen, Retentionsfläche / Notüberflutungsfläche", [schraffur(RW, 0.25, 0, 1.6), linie(B0, 0.5, [3, 1.5])]),
    ("Starkregen, Geländesenke", [schraffur(B0, 0.2, 45, 2.2), schraffur(B0, 0.2, 135, 2.2), linie(B0, 0.3)]),
    ("Starkregen, Risikobereich", [band(SRV[3][1] + "59", 1.5), linie(SRV[3][1], 0.4)]),
] + [(OEKL + f"See, ökologischer Zustand {t}", [voll(c), linie(B0, 0.3)]) for t, c in ZUST] + [
    (OEKL + "Grundwasserkörper, mengenmäßiger Zustand gut", [voll(GUT + "80"), linie(B0, 0.3)]),
    (OEKL + "Grundwasserkörper, mengenmäßiger Zustand schlecht", [voll(SCHLECHT + "80"), linie(B0, 0.3)]),
    (OEKL + "Grundwasserkörper, chemischer Zustand gut", [schraffur(GUT, 0.3, 45, 1.8), linie(B0, 0.3)]),
    (OEKL + "Grundwasserkörper, chemischer Zustand schlecht", [schraffur(SCHLECHT, 0.3, 45, 1.8), linie(B0, 0.3)]),
    (OEKL + "Gewässerrandstreifen, Fläche", [voll(GUT + "59"), linie(GUT, 0.3)]),
    (OEKL + "Aue, rezent", [voll(RW + "33"), muster(mk("line", 1.2, B0, rw=0.25), 3, versatz=1.5), linie(B0, 0.3)]),
    (OEKL + "Altaue", [muster(mk("line", 1.2, B0, rw=0.25), 3, versatz=1.5), linie(B0, 0.3, [3, 1.5])]),
    (OEKL + "Entwicklungskorridor", [band(GUT + "59", 1.5), linie(GUT, 0.5, [4, 1.5])]),
    (OEKL + "Maßnahmenfläche Gewässerentwicklung", [schraffur(B0, 0.2, 45, 3), linie(B0, 0.5, [3, 1.5])]),
    (OEKL + "Einzugsgebiet Wasserkörper", [linie(B0, 0.5, [4, 1, 1, 1])]),
]
