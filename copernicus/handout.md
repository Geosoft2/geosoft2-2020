@a2beckj
# Copernicus

Copernicus ist das Erdbeobachtungsprogramm der Europäischen Union, das sich mit unserem Planeten und seiner Umwelt zum größtmöglichen Nutzen aller europäischen Bürger befasst. Es bietet Informationsdienste auf der Grundlage von satellitengestützter Erdbeobachtung und In-situ-Daten (Nicht-Weltraumdaten) an.

Ziele:
* Umweltschutz
* Unterstützung von Zivilschutz und Sicherheitsbemühungen
* Unterstützung eines nachhaltigen Zuwachses der EU-Wirtschaft

## which satellites are involved, for which purposes

Insgesamt 5 eigenständige Satelliten und 2 spezielle Messinstrumente, die auf Satelliten von Eumetsat mitfliegen.

### Satelliten
#### Sentinel-1:
* Bis zu 5 Meter hochauflösendes Radarinstrument
* Lieferung von Daten über Land- und Wasseroberflächen, unabhängig von Helligkeit und Wolkenbedeckung
* Ermöglicht zeitnahe Aufnahmen von: 
  - Überschwemmungen an Land
  - Ölverschmutzungen auf dem Meer
  - Zeitreihen kleinster Bodenbewegungen oder der Vegetationsdichte
* Sentinel-1B wurde 2016 gestartet
  
#### Sentinel-2:
* liefern Aufnahmen im sichtaren und infraroten Spektrum (443 - 2190nm)
* 13 Kanäle zur Beobachtung der Landoberflächen
* Auflösung von bis zu 10m, Abtastbreite von 290km
* Ermöglicht Veränderungen der Vegetation zu erkennen, um:
  - Erntevorhersagen zu erstellen
  - Waldbestände zu kartieren 
  - Wachstum von Wild- und Nutzpflanzen zu bestimmen
  - Algenwachstum an Küsten- un Binnengewässern beobachten
  - Sedimenteintrag in Flussdeltas nachzuverfolgen
* Sentinel-2B wurde 2017 gestartet

#### Sentinel-3
* nutzt ein Paket aus 5 Instrumenten
* hochpräzise Bestimmung der Temperatur, der Farbe und des Pegels der Meeresoberfläche
* Ermöglicht Erkenntnisse über:
  - Unterwasserströmungen
  - Wellenhöhen
  - Nährstoffverteilung in den Weltmeeren
  - Energiehaushalt des Planeten
  - Wasserqualität oder Umweltverschmutzung an den Küsten
* Sentinel-3B wurde 2018 gestartet

#### Sentinel-5P
* Messungen siehe Sentinel-5
* Fliegt nurnoch solange, bis Messinstrumente auf EUMETSAT mitfliegen werden.
* Ist seit 2017 im Einsatz



#### Sentinel-6
* Jahreszeitliche Messreihen zu den Meeresspiegehöhen
* Set aus hochpräzsen Ortungsinstrumenten (Radar-Höhenmesser, Mikrowellen-Radiometer -> zentimetergenaue Bestimmung der Meeresoberflächen)
* Daten zu Windgeschwindigkeiten, Meeresströmungen und Wellen
* Noch in der Entwicklung, Start ist für den 15.11.2020 geplant
* Vorläufersystem 2016 gestartet, wird von EUMETSAT betrieben


### Messinstrumente EUMETSAT-betrieben

#### Sentinel-4
* Präzise Daten über Konzentration von Schadstoffen in der Luft
* Stündliche Messungen von Ozonbelastung, Feinstaubgehalt, Luftqualität
* Erster Einsatz auf einem Meteosat soll 2022 erfolgen

#### Sentinel-5
* Mission zu Messung von Atmosphärengasen weltweit (Methan, Ozon, Stickstoff, Aerosole)
* will komplexe Prozesse in der Erdatmosphäre sichtbar machen
* Erster Einsatz soll 2022 auf neuer Generation des polaren EUMETSAT Systems,MetOp-SG geplant


## what was/is the time line

## what are the data volumes
Dateigröße ca. 1GB pro Datei.

## Allgemeine Geschäftsbedingungen für die Nutzung der Copernicus-Daten
Nutzer der Daten haben das Recht:
* die Daten in einer beliebigen Weise zu Nutzen, zu verändern und zu modifizieren und dadurch geänderte Produkte herzustellen
* die Daten an weitere Nutzer, Auftragnehmer und andere Teilnehmer in Rahmen von Projekten weiterzugeben, solange diese die Allgemeinen Geschäftsbedingungen akzeptieren.
* die Daten in unbegrenzter Anzahl zu kopieren.
* Sentinel-Daten, abgeänderte Produkte und abgeleitete Werke in gedruckten oder digitalen Medien zu veröffentlichen. Dies umfasst nicht den Download oder die Rekonstruktion der Sentinel-Daten oder veränderter Produkte, solange die Anforderungen der Datenweiterleitung nicht erfüllt sind.
* Sentinel-Daten, und die von ihnen geänderten Produkte und abgeleiteten Werke zu verteilen, solange die Empfänger die Allgemeinen Geschäftsbedingungen zur Kenntniss nehmen.

* Das geistige Eigentum der primären und veränderten Produkte bleibt beim Besitzer der Satelliten. Wann immer die Daten geteilt, veröffentlicht oder auf andere Weise zur Verfügung gestellt werden, muss der Nutzer diese eindeutig mit einem Copyright-Zeichen wie folgt versehen: „© Copernicus Daten (Jahr des Abrufs) “
* Das geistige Eigentum von Derivaten, die vom Benutzer erstellt wurden
gehört dem Benutzer. Abgeleitete Werke sind bei Veröffentlichung, Teilen oder jeglicher anderer Form der Bereitstellung wie folgt zu kennzeichnen: “enthält Copernicus-Daten (Jahr des Abrufs) ”.


## how can one get access to the data
1. Auf Copernicus Open Access Hub registrieren (https://scihub.copernicus.eu/userguide/SelfRegistration)
**Wichtig! Es dauert bis zu einer Woche bis die Nuterdaten für die API Nutzung aktiviert/aktualisiert werden. Frühzeitig registrieren!**


## where can one process the data

Protokoll: Open Data Protocol (OData), Schnittstelle für den Zugriff auf Copernicus Sentinel.

### Lokal
#### Manuell
1. Einloggen (https://scihub.copernicus.eu/dhus/#/home)
2. Bereich selektieren
3. Produkte suchen
4. Produkte auswählen und herunterladen

#### Python API
1. Metadaten: https://github.com/sentinelsat/sentinelsat

**Daten werden lediglich 12 Monate online vorgehalten. Beim versuchten Zugriff auf ältere Daten wird automatisch ein Abruf aus dem Langzeitarchiv angefordert. Der eigentliche Download kann vom Benutzer nach Wiederherstellung der Daten (innerhalb von 24 Stunden) initiiert werden. Ein Benutzerkontingent für die maximale Anzahl von Anforderungen pro Stunde und Benutzer wird festgelegt. Aus den Langzeitarchiven restaurierte Produkte werden mindestens 3 Tage lang online aufbewahrt.**

### Cloud

* Europäische Kommission den Einsatz von fünf Cloud-basierten Plattformen finanziert, die einen zentralen Zugang zu Copernicus-Daten und -Informationen sowie zu Verarbeitungswerkzeugen ermöglichen. Diese Plattformen werden als DIAS (Data and Information Access Services) bezeichnet.
* ermöglichen es den Nutzern, Copernicus-Daten und -Informationen aufzufinden, zu handhaben, zu verarbeiten und herunterzuladen. Alle DIAS-Plattformen bieten Zugang zu den Daten von Copernicus Sentinel sowie zu den Informationsprodukten aus den sechs Betriebsdiensten von Copernicus sowie zu Cloud-basierten Tools.
* Jede der fünf konkurrierenden Plattformen bietet auch Zugang zu zusätzlichen kommerziellen Satelliten- oder Nicht-Weltraum-Datensätzen sowie Premium-Angeboten in Bezug auf Support oder Priorität. 
* Dank eines einzigen Zugangspunktes für die gesamten Copernicus-Daten und -Informationen **ermöglicht DIAS den Benutzern die Entwicklung und das Hosting ihrer eigenen Anwendungen in der Cloud, ohne dass voluminöse Dateien von mehreren Zugangspunkten heruntergeladen und lokal verarbeitet werden müssen.**


| DIAS                            | Free          | Cost  | Abilities to interact |
| :------------------------------:|:-------------:| :----:| :-------------------: |
| ![wekeo](images/wekeo.png)      | right-aligned | $1600 |                       |
| ![sobloo](images/cobloo.png)    | centered      |   $12 |                       |
| ![creodias](images/creodias.png)| are neat      |    $1 |                       |
| ![onda](images/onda.png)        |               |       |                       |
| ![mundi](images/mundi.png)      |               |       |                       |


![wekeo](images/wekeo.png)

Begriffe:lokal = du lädst die Daten auf deinen Computer herunter; cloud = du nutzt eine Schnittstelle (API) oder eine Platform um die Berechnungen auf einem oder vielen Servern im Internet auszuführen.

Zu Lokal gehören dann die APIs und Möglichkeiten zum Datendownload, ggf. auch sowas wie Nutzungsrechte.

Und ja, es wäre gut wenn du die existierenden Lösungen beschreibst: wer bietet da was an, ist das alles kostenlos/öffentlich, gibt es da nur Unis oder auch Firmen? Welche Produkte gibt es die versprechen Copernicus-Daten verarbeiten zu können, welche Forschungsprojekte arbeiten an welchen Daten oder neuen Funktionen?

Generelle Vorteile ist nicht so spannend, weil der klare Vorteil ja ist: Ohne Cloud geht es gar nicht, zumindest nicht lokal. Du kannst natürlich noch Cloud vs. Rechenzentrum unterscheiden, dann hättest du bei Cloud noch Aspekte dynamische Skalierbarkeit und viele verschiedene Nutzer.
