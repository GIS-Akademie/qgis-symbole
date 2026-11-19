"""Sammlung Boden, Altlasten und Geologie: Aufschluesse und Messstellen, Altlasten, Bodenschutz, Geologie und Rohstoffe.
Orientierung: DIN 4023 (zeichnerische Darstellung von Bohrungen: Kurzzeichen und Signaturen der Bodenarten),
Bodenkundliche Kartieranleitung, Altlastenkataster der Laender (Altablagerung/Altstandort nach BBodSchG),
Bergbauzeichen der topografischen Karten (gekreuzte Haemmer, bei Stilllegung auf dem Kopf).
Eigene, schlichte Entwuerfe in Anlehnung daran; keine Wiedergabe genormter Zeichen.
Stil: hellbraune Fuellung, dunkelbrauner Strich 5. Die Rahmenform zeigt die Gruppe:
  Kreis = Aufschluss oder Messstelle (Flaechenteilung oder Kurzzeichen), Quadrat = Altlast oder Standort,
  Raute = Bodenschutz/Gebiet, Sechseck = Geologie und Rohstoffe,
  ohne Rahmen = Gefuegezeichen (Praefix gef_: Streichen und Fallen). Die Streichlinie liegt waagerecht, das
  Fallzeichen zeigt nach oben; gedreht wird um die Fallrichtung (0 = Norden, im Uhrzeigersinn).
  Formen wie in geologischen Karten ueblich: Strich = Schichtung, Dreieck = Schieferung, Rechteck = Kluft.
  Gefahrenhinweise stehen im Sinnbild, nicht in einer anderen Farbe.
Linien und Flaechen: braun; nachgewiesen/Bestand durchgezogen, vermutet/Verdacht gestrichelt. Altlasten schraffiert,
Kanten mit Zeichen zur tieferen Seite (rechts in Laufrichtung), Bodenarten als Signatur in Anlehnung an DIN 4023
(Sand gepunktet, Kies Ringe, Ton waagerecht, Schluff schraeg schraffiert). Festgesteine (Titel "Gestein ...")
ebenfalls braun und nur ueber die Signatur unterschieden; die Signaturen sind eigene, an geologischen Karten
orientierte Entwuerfe (Kristallin Kreuze, Vulkanit v-Zeichen, Sedimente waagerecht), keine Normsignaturen.
Kurzzeichen der Aufschluesse: BS = Kleinbohrung, DP = Rammsondierung, CPT = Drucksondierung.
"""
from lib import *
from qstil import linie, band, marken, voll, schraffur, muster, mk, sv

KEY = "boden"
NAME = "Boden, Altlasten und Geologie"
DESC = ("Symbole für Boden, Altlasten und Geologie: Bohrungen, Schürfe und Messstellen, Altablagerungen und "
        "Altstandorte, Bodenschutz, Rohstoffabbau, Bergbau und Georisiken, Streichen und Fallen, Signaturen für "
        "Boden- und Gesteinsarten")
TAGS = "boden, altlasten, geologie, bohrung, baugrund, bodenschutz, rohstoffe, bergbau, georisiken, gestein, streichen, fallen"

BR = ("#EAD9C3", "#6B4423")


def ms(*sh):  # Aufschluss, Messstelle
    return fr_circle() + list(sh)


def mst(txt, h=26, mw=62):
    return ms(T(txt, 50, 50, h, maxw=mw))


def teil(*sh):  # Kreis mit Flaechenteilung: Fuellung, Teilflaechen, Rand obenauf
    return fr_circle() + list(sh) + [C(50, 50, 44, "N", "S", 5)]


def al(*sh):  # Altlast, Standort
    return fr_square() + list(sh)


def alt(txt, h=34, mw=62):
    return al(T(txt, 50, 50, h, maxw=mw))


def bs(*sh):  # Bodenschutz, Gebiet
    return fr_diamond() + list(sh)


def bst(txt, h=24, mw=44):
    return bs(T(txt, 50, 50, h, maxw=mw))


def geo(*sh):  # Geologie, Rohstoffe
    return fr_hex() + list(sh)


def grube(*sh):  # Abbaugrube im Schnitt mit Signatur des Rohstoffs
    return geo(PL([(24, 24), (33, 76), (67, 76), (76, 24)], 6), *sh)


HAMMER = [L(50, 86, 50, 34, 7), R(31, 18, 38, 17, "S", "N", 0, 2)]
SCHLAEGEL = fit(HAMMER, 50, 52, 0.8, 40) + fit(HAMMER, 50, 52, 0.8, -40)
SPATEN = [L(50, 20, 50, 56, 6), L(39, 20, 61, 20, 6), P("M36,54 H64 V70 Q64,82 50,86 Q36,82 36,70 Z", "S", "S", 3)]
BOMBE = [C(45, 59, 21, "S", "N", 0), PG([(53, 38), (62, 31), (70, 40), (61, 47)], "S"),
         P("M65,34 Q70,22 80,26", "N", "S", 4), PG(star(82, 22, 8, 3.5, 6), "S")]
STREICH = L(8, 50, 92, 50, 6)
WIND = [P("M20,40 H58 a10,10 0 1 0 -10,-10", "N", "S", 6), P("M20,58 H70 a10,10 0 1 1 -10,10", "N", "S", 6)]

S = [
    # ---- Aufschluesse und Messstellen (Kreis) ----
    ("bohrung", "Bohrung", *BR, teil(pie(50, 50, 44, 0, 90), pie(50, 50, 44, 180, 270))),
    ("kernbohrung", "Kernbohrung", *BR, ms(C(50, 50, 19, "S", "N", 0))),
    ("rammkernsondierung", "Rammkernsondierung", *BR, mst("RKS", 22)),
    ("schurf", "Schurf", *BR, ms(R(27, 33, 46, 34, "F", "S", 5), PG([(27, 33), (27, 67), (73, 67)], "S"))),
    ("bodenprofil", "Bodenprofil / Profilgrube", *BR,
     teil(chord(50, 50, 44, 300, 60), L(11, 50, 89, 50, 4.5, cap="butt"), L(19, 72, 81, 72, 4.5, cap="butt"))),
    ("bodendauerbeobachtung", "Boden-Dauerbeobachtungsfläche", *BR, mst("BDF", 22)),
    ("bodenluftmessstelle", "Bodenluftmessstelle", *BR, mst("BL", 30, 50)),
    ("sickerwassermessstelle", "Sickerwassermessstelle", *BR,
     ms(*fit(drop("S", "N", 0), 50, 33, 0.38), L(26, 56, 74, 56, 5), *arrow(50, 62, 50, 86, 5, 11))),
    ("probenahmepunkt", "Probenahmepunkt", *BR, teil(chord(50, 50, 44, 180, 360))),
    ("grundwasseraufschluss", "Grundwasseraufschluss", *BR,
     ms(PG([(33, 24), (67, 24), (50, 48)], "S"), L(22, 55, 78, 55, 5), L(32, 67, 68, 67, 4.5), L(42, 78, 58, 78, 4))),
    ("kleinbohrung", "Kleinbohrung / Sondierbohrung (BS)", *BR, mst("BS", 30, 50)),
    ("rammsondierung", "Rammsondierung (DPL, DPM, DPH)", *BR, mst("DP", 30, 50)),
    ("drucksondierung", "Drucksondierung (CPT)", *BR, mst("CPT", 22)),
    ("bohrstock", "Bohrstocksondierung / Handbohrung", *BR,
     ms(L(50, 24, 50, 70, 6), L(34, 24, 66, 24, 7), PG([(44, 68), (56, 68), (50, 86)], "S"))),
    ("tiefbohrung", "Tiefbohrung", *BR, ms(C(50, 50, 29, "N", "S", 4.5), C(50, 50, 13, "S", "N", 0))),
    ("schraegbohrung", "Schrägbohrung (Richtung nach rechts, drehbar)", *BR,
     ms(C(32, 50, 11, "S", "N", 0), *arrow(44, 50, 84, 50, 5.5, 14))),
    ("bohrung_gwm", "Bohrung, zur Grundwassermessstelle ausgebaut", *BR, mst("GWM", 20)),
    ("bohrung_geplant", "Bohrung, geplant", *BR,
     [C(50, 50, 44, "F", "S", 5, "12 8"), pie(50, 50, 28, 0, 90), pie(50, 50, 28, 180, 270)]),
    ("bohrung_verfuellt", "Bohrung, verfüllt / aufgegeben", *BR, ms(*xcross(50, 50, 21, 7))),
    # ---- Altlasten und Standorte (Quadrat) ----
    ("altablagerung", "Altablagerung", *BR, alt("AA")),
    ("altstandort", "Altstandort", *BR, alt("AS")),
    ("verdachtsflaeche", "Altlastverdächtige Fläche / Verdachtsfläche", *BR, alt("?", 52)),
    ("sanierte_flaeche", "Sanierte Fläche", *BR, al(PL([(24, 52), (42, 70), (76, 30)], 9))),
    ("sanierung_laufend", "Sanierung laufend", *BR, al(*SPATEN)),
    ("kampfmittelverdacht", "Kampfmittelverdacht", *BR, al(*BOMBE)),
    ("grundwasserschaden", "Grundwasserverunreinigung", *BR,
     al(*fit(drop("S", "N", 0), 50, 50, 0.84), *xcross(50, 58, 10, 5, "F"))),
    ("deponie", "Deponie", *BR,
     al(PG([(15, 78), (33, 30), (67, 30), (85, 78)], "S", "S", 4), T("D", 50, 55, 30, "F"))),
    ("bodenaushub", "Bodenaushub / Zwischenlager", *BR,
     al(PG([(14, 76), (36, 34), (58, 76)], "F", "S", 5), PG([(44, 76), (64, 48), (84, 76)], "S", "S", 5))),
    # ---- Bodenschutz (Raute) ----
    ("bodenschutzgebiet", "Bodenschutzgebiet / Bodenplanungsgebiet", *BR, bst("BSG", 18, 50)),
    ("schutzwuerdiger_boden", "Schutzwürdiger Boden", *BR, bst("SB")),
    ("archivboden", "Archivboden (Natur- und Kulturgeschichte)", *BR, bst("AB")),
    ("erosion_wasser", "Erosionsgefährdung durch Wasser", *BR,
     bs(*fit(drop("S", "N", 0), 52, 36, 0.3), L(30, 55, 66, 69, 6), L(31, 68, 50, 76, 4.5))),
    ("erosion_wind", "Erosionsgefährdung durch Wind", *BR, bs(*fit(WIND, 51, 50, 0.72))),
    ("verdichtung", "Bodenverdichtung", *BR,
     bs(*arrow(41, 26, 41, 54, 5, 11), *arrow(59, 26, 59, 54, 5, 11), L(29, 61, 71, 61, 6), L(38, 72, 62, 72, 4.5))),
    ("versiegelung", "Versiegelung", *BR,
     bs(R(26, 40, 48, 13, "S", "N", 0, 2), *[L(x, 61, x - 5, 70, 4.5) for x in (40, 52, 64)])),
    ("entsiegelung", "Entsiegelung", *BR,
     bs(R(24, 53, 17, 12, "S", "N", 0, 2), R(59, 53, 17, 12, "S", "N", 0, 2), L(50, 70, 50, 40, 5),
        P("M50,46 Q38,46 36,30 Q50,32 50,46 Z", "S", "N", 0), P("M50,46 Q62,46 64,30 Q50,32 50,46 Z", "S", "N", 0))),
    ("moorboden", "Moorboden", *BR,
     bs(L(50, 60, 50, 30, 5), L(48, 60, 36, 37, 5), L(52, 60, 64, 37, 5), L(28, 62, 72, 62, 5), L(38, 73, 62, 73, 4.5))),
    # ---- Geologie und Rohstoffe (Sechseck) ----
    ("geotop", "Geotop", *BR, geo(T("G", 50, 50, 44))),
    ("steinbruch", "Steinbruch / Aufschluss", *BR,
     geo(PL([(20, 28), (38, 28), (38, 46), (56, 46), (56, 64), (78, 64)], 6),
         *[C(x, y, 4, "S", "N", 0) for x, y in ((64, 78), (76, 77), (70, 71))])),
    ("kiesgrube", "Kiesgrube", *BR,
     grube(*[C(x, y, 6.5, "F", "S", 4) for x, y in ((42, 36), (58, 40), (44, 57), (58, 60))])),
    ("sandgrube", "Sandgrube", *BR,
     grube(*[C(x, y, 3.8, "S", "N", 0) for y in (34, 48, 62) for x in ((39, 50, 61) if y != 48 else (45, 56))])),
    ("tongrube", "Tongrube", *BR, grube(*[L(39, y, 61, y, 5, cap="butt") for y in (35, 48, 61)])),
    ("torfabbau", "Torfabbau", *BR,
     grube(L(38, 44, 62, 44, 4.5, cap="butt"), L(40, 62, 60, 62, 4.5, cap="butt"),
           *[L(x, y, x, y + 11, 4.5, cap="butt") for x, y in ((44, 33), (56, 33), (50, 51))])),
    ("bergwerk", "Bergwerk in Betrieb", *BR, geo(*SCHLAEGEL)),
    ("bergwerk_stillgelegt", "Bergwerk stillgelegt", *BR, geo(*fit(SCHLAEGEL, 50, 50, 1, 180))),
    ("stollenmundloch", "Stollenmundloch", *BR,
     geo(P("M31,74 V46 A19,19 0 0 1 69,46 V74 Z", "S", "S", 4), L(20, 76, 80, 76, 5))),
    ("schacht", "Schacht (Bergbau)", *BR,
     geo(R(29, 29, 42, 42, "S", "S", 4), L(29, 29, 71, 71, 4.5, "F", "butt"), L(29, 71, 71, 29, 4.5, "F", "butt"))),
    ("halde", "Halde", *BR,
     geo(PG([(18, 72), (50, 24), (82, 72)], "F", "S", 5), L(50, 28, 40, 70, 4), L(50, 28, 60, 70, 4))),
    ("erdfall", "Erdfall / Doline", *BR,
     geo(C(50, 50, 28, "N", "S", 5), *[L(*pt(50, 50, 26, a), *pt(50, 50, 14, a), 4.5) for a in range(0, 360, 45)])),
    ("rutschung", "Rutschung / Massenbewegung", *BR,
     geo(P("M22,46 Q50,6 78,46", "N", "S", 6), *arrow(50, 38, 50, 82, 6, 14), L(33, 50, 33, 66, 4.5), L(67, 50, 67, 66, 4.5))),
    ("stoerung", "Geologische Störung", *BR,
     geo(L(38, 82, 62, 18, 5), L(16, 40, 44, 40, 7, cap="butt"), L(56, 60, 84, 60, 7, cap="butt"))),
    ("erdbebenmessstation", "Erdbebenmessstation / Seismometer", *BR,
     geo(PL([(14, 50), (27, 50), (34, 34), (43, 70), (52, 22), (60, 74), (67, 42), (73, 50), (86, 50)], 4.5))),
    ("erdwaermesonde", "Erdwärmesonde", *BR,
     geo(L(22, 32, 78, 32, 5), P("M41,32 V70 A9,9 0 0 0 59,70 V32", "N", "S", 5), PG([(34, 17), (48, 17), (41, 28)], "S"),
         PG([(52, 28), (66, 28), (59, 17)], "S"))),
    # ---- Gefuegezeichen: Streichen und Fallen (ohne Rahmen; Fallrichtung oben, drehbar) ----
    ("gef_schichtung", "Streichen und Fallen der Schichtung (Fallrichtung oben, drehbar)", *BR, [STREICH, L(50, 50, 50, 20, 6)]),
    ("gef_schichtung_saiger", "Schichtung saiger / senkrecht (drehbar)", *BR, [STREICH, L(50, 28, 50, 72, 6)]),
    ("gef_schichtung_soehlig", "Schichtung söhlig / horizontal", *BR, [C(50, 50, 27, "N", "S", 6)] + cross(50, 50, 40, 6)),
    ("gef_schichtung_ueberkippt", "Schichtung überkippt (Fallrichtung oben, drehbar)", *BR,
     [STREICH, P("M50,50 V28 A12,12 0 0 1 74,28 V38", "N", "S", 6)]),
    ("gef_schieferung", "Streichen und Fallen der Schieferung (Fallrichtung oben, drehbar)", *BR,
     [STREICH, PG([(36, 50), (64, 50), (50, 22)], "S", "S", 3)]),
    ("gef_schieferung_saiger", "Schieferung saiger / senkrecht (drehbar)", *BR,
     [STREICH, PG([(36, 50), (50, 26), (64, 50), (50, 74)], "S", "S", 3)]),
    ("gef_kluft", "Streichen und Fallen der Kluft (Fallrichtung oben, drehbar)", *BR,
     [STREICH, R(38, 27, 24, 23, "S", "S", 3)]),
    ("gef_kluft_saiger", "Kluft saiger / senkrecht (drehbar)", *BR, [STREICH, R(38, 30, 24, 40, "S", "S", 3)]),
    ("gef_stoerung", "Einfallen der Störungsfläche (Fallrichtung oben, drehbar)", *BR,
     [L(8, 50, 92, 50, 10, cap="butt")] + arrow(50, 46, 50, 12, 6, 16)),
    ("gef_lineation", "Lineation / Abtauchen der Faltenachse (Richtung oben, drehbar)", *BR, arrow(50, 88, 50, 12, 7, 22)),
    ("gef_sattelachse", "Sattelachse / Antiklinale (drehbar)", *BR,
     [STREICH] + arrow(50, 50, 50, 16, 5.5, 15) + arrow(50, 50, 50, 84, 5.5, 15)),
    ("gef_muldenachse", "Muldenachse / Synklinale (drehbar)", *BR,
     [STREICH] + arrow(50, 12, 50, 43, 5.5, 15) + arrow(50, 88, 50, 57, 5.5, 15)),
]

SYMBOLS = S

# ---- Linien und Flaechen (QGIS-Stildatei) ----
B0, BL = BR[1], BR[0]



def gestein(*ebenen):  # Festgestein: etwas kraeftigerer Grund als die Bodenarten, Signatur, Umriss
    return [voll(BL + "CC"), *ebenen, linie(B0, 0.3)]


LINIEN = [
    ("Geologische Störung, nachgewiesen", [linie(B0, 0.8)]),
    ("Geologische Störung, vermutet", [linie(B0, 0.8, [3, 1.5])]),
    ("Schichtgrenze", [linie(B0, 0.3)]),
    ("Schichtgrenze, vermutet", [linie(B0, 0.3, [2, 1])]),
    ("Abbaukante", [linie(B0, 0.4), marken(mk("line", 1.4, B0, rw=0.3, dy=0.7), 2)]),
    ("Rutschungskante, Abrisskante", [linie(B0, 0.5), marken(mk("triangle", 1.6, B0, winkel=180, dy=-0.8), 3)]),
    ("Erosionsrinne", [linie(B0, 0.4, [4, 1, 0.5, 1]), marken(mk("filled_arrowhead", 2.2, B0), 13, start=2)]),
    ("Grenze Altlastenfläche", [linie(B0, 0.5), marken(mk("cross2", 1.4, B0, rw=0.3), 5)]),
    ("Grenze Verdachtsfläche", [linie(B0, 0.5, [3, 2]), marken(mk("cross2", 1.4, B0, rw=0.3), 5, start=4)]),
    ("Grenze Bodenschutzgebiet", [linie(B0 + "59", 1.8), linie(B0, 0.3)]),
    ("Profilschnitt", [linie(B0, 0.5, [6, 1.5, 1, 1.5])]),
    ("Abschiebung (Zeichen zur abgesunkenen Scholle)", [linie(B0, 0.8), marken(mk("line", 1.5, B0, rw=0.35, dy=0.75), 5)]),
    ("Überschiebung (Zeichen zur überschobenen Scholle)", [linie(B0, 0.8), marken(mk("triangle", 1.6, B0, winkel=180, dy=-0.8), 5)]),
    ("Sattelachse", [linie(B0, 0.5), marken(mk("triangle", 1.4, B0, dy=-1.1), 14),
                     marken(mk("triangle", 1.4, B0, winkel=180, dy=-1.1), 14)]),
    ("Muldenachse", [linie(B0, 0.5), marken(mk("triangle", 1.4, B0, dy=1.1), 14),
                     marken(mk("triangle", 1.4, B0, winkel=180, dy=1.1), 14)]),
]

FLAECHEN = [
    ("Altablagerung", [voll(BL + "B3"), schraffur(B0, 0.3, 45, 2.5), linie(B0, 0.5)]),
    ("Altstandort", [voll(BL + "B3"), schraffur(B0, 0.3, 135, 2.5), linie(B0, 0.5)]),
    ("Altlastverdächtige Fläche", [schraffur(B0, 0.25, 45, 3), linie(B0, 0.5, [3, 1.5])]),
    ("Sanierte Fläche", [voll(BL), linie(B0, 0.5)]),
    ("Abbaufläche", [voll(BL + "80"), linie(B0, 0.4), marken(mk("line", 1.4, B0, rw=0.3, dy=0.7), 2, ecken=1.0)]),
    ("Rohstoffsicherungsfläche", [band(B0 + "66", 1.6), linie(B0, 0.4, [5, 2])]),
    ("Schutzwürdiger Boden", [band(B0 + "59", 1.5), linie(B0, 0.3)]),
    ("Erosionsgefährdete Fläche", [muster(mk("filled_arrowhead", 1.8, B0), 4, 3, versatz=2), linie(B0, 0.4, [3, 1.5])]),
    ("Auffüllung", [voll(BL + "80"), muster(mk("cross2", 1.2, B0, rw=0.25), 3, versatz=1.5), linie(B0, 0.4)]),
    ("Moorboden, Torf", [voll(B0 + "40"), schraffur(B0, 0.25, 0, 2.4),
                         muster(mk("line", 1.2, B0, rw=0.3), 3, 2.4, versatz=1.5), linie(B0, 0.3)]),
    ("Bodenart Sand", [voll(BL + "80"), muster(mk("circle", 0.45, B0), 1.6, versatz=0.8), linie(B0, 0.3)]),
    ("Bodenart Kies", [voll(BL + "80"), muster(mk("circle", 1.3, BL, rand=B0, rw=0.25), 2.6, versatz=1.3), linie(B0, 0.3)]),
    ("Bodenart Ton", [voll(BL + "80"), schraffur(B0, 0.25, 0, 1.2), linie(B0, 0.3)]),
    ("Bodenart Schluff", [voll(BL + "80"), schraffur(B0, 0.25, 135, 1.6), linie(B0, 0.3)]),
    ("Bodenart Lehm", [voll(BL + "80"), schraffur(B0, 0.25, 135, 3.2), muster(mk("circle", 0.45, B0), 1.6, versatz=0.8), linie(B0, 0.3)]),
    ("Bodenart Löss", [voll(BL + "80"), schraffur(B0, 0.2, 90, 1.6), linie(B0, 0.3)]),
    ("Bodenart Steine und Blöcke", [voll(BL + "80"), muster(mk("circle", 2.4, BL, rand=B0, rw=0.3), 3.8, versatz=1.9), linie(B0, 0.3)]),
    ("Oberboden / Mutterboden", [voll(B0 + "59"), muster(mk("line", 1.0, B0, rw=0.25), 1.8, 2.2, versatz=0.9), linie(B0, 0.3)]),
    ("Gestein Sandstein", gestein(schraffur(B0, 0.2, 0, 3.2), muster(mk("circle", 0.45, B0), 1.6, versatz=0.8))),
    ("Gestein Konglomerat", gestein(schraffur(B0, 0.2, 0, 3.2), muster(mk("circle", 1.3, BL, rand=B0, rw=0.25), 3.2, versatz=1.6))),
    ("Gestein Tonstein", gestein(muster(mk("line", 2.2, B0, rw=0.25, winkel=90), 3.2, 1.2, versatz=1.6))),
    ("Gestein Mergelstein", gestein(schraffur(B0, 0.2, 0, 2.4), muster(mk("line", 1.0, B0, rw=0.25), 3.2, 2.4, versatz=1.6))),
    ("Gestein Kalkstein", gestein(muster(mk("square", 1.7, None, rand=B0, rw=0.25), 2.8, versatz=1.4))),
    ("Gestein Steinsalz / Evaporit", gestein(muster(mk("diamond", 1.5, None, rand=B0, rw=0.25), 2.8, versatz=1.4))),
    ("Gestein Kohle", [voll("#3A2A1C"), schraffur(BL, 0.15, 0, 1.6), linie(B0, 0.3)]),
    ("Gestein Granit / Plutonit", gestein(muster(mk("cross", 1.3, B0, rw=0.25), 2.8, versatz=1.4))),
    ("Gestein Basalt / Vulkanit", gestein(muster(mk("arrowhead", 1.1, B0, rw=0.25, winkel=90), 2.8, versatz=1.4))),
    ("Gestein Gneis / kristalliner Schiefer", gestein(muster(mk("line", 1.8, B0, rw=0.25, winkel=60), 2.2, 1.5, versatz=1.1))),
    ("Gestein Tonschiefer", gestein(schraffur(B0, 0.2, 20, 1.1))),
]
