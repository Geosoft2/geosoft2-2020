# Datenwürfel für Fernerkundungsdaten, Klimamodelle und Wetterdaten
@neli98

## 1. Datenwürfel allgemein
* auch bekannt als OLAP-Würfel (OLAP = Online Analytical Processing) [2]
* relevant im Bereich des Data-Warehousing [1]
* nützlich zur Strukturierung von Daten (Big Data) [1]
* beliebig viele Dimensionen möglich [1]
  * leicht vorzustellen als 3D-Würfel (siehe untenstehende Grafik)
* Speicherung der Daten in einzelnen Elementen des Würfels [2]
* dynamische Betrachtungsweisen der Daten aus verschiedenen Perspektiven möglich [2]
* verschiedene Grundoperationen, wie z.B.:
  * Slice-Operation (Ausschneiden einer Datenscheibe) [2]
  * Dice-Operation (Erzeugen eines kleineren Würfels aus Ursprungswürfel) [2]
* graphische Veranschaulichung anhand eines Beispiels aus der Betriebswirtschaft:
![Data Cube](https://images.tecchannel.de/bdb/362924/840x473.jpg)


## 2. Datenwürfel im Kontext der Geoinformatik

### 2.1 Anwendungsfälle
* hilfreich beim Umgang mit großen, multidimensionalen GIS-Datenmengen - z.B. Earth Observation(EO)-Daten [3]
  * speziell bei Daten mit zeitlicher Dimension
  * Schnittstelle zwischen Daten und Nutzeranwendungen
* Vereinfachung der Analyse von z.B.:
  * Abholzung/Rodung von Wäldern [3]
  * illegalem Rohstoffabbau [3]
  * Dürreregionen [4]
  * Wetterentwicklungen [4]


### 2.2 Beispiele
* Open Data Cube ([mehr Informationen](https://www.opendatacube.org))
  * internationale Open-Source Initiative [3]
  * freie Bereitstellung von EO-Daten [3]
    * z.B. zur Unterstützung der Analyse in Hinblick auf die SDG's [3]
    * dadurch Liberalisierung und Erhöhung des Nutzens der Daten [3]
    * Bereitstellung über eine auf Python basierende API [3]
* Euro Data Cube ([mehr Informationen](https://eurodatacube.com/#features))
  * Initative der European Space Agency [10]
  * kommerzielle Bereitstellung von EO-Daten (u.a. Copernicus-Daten) [10]
* Earth Server Datacube Federation ([mehr Informationen](https://www.earthserver.eu))
  * Zusammenschluss mehrerer internationaler Forschungseinrichtungen [8]
  * Bereitstellung von 3D-Satellitenbildern und 4D-Wetterdaten [8]
* Next Generation Network Enabled Weather Project ([mehr Informationen](https://en.wikipedia.org/wiki/Next_Generation_Network_Enabled_Weather))
  * Initiative der USA [9]
  * Bereitstellung von 4D-Wetterdaten [9]
  * Analyse von Wetterdaten zur besseren Wettervorhersage und Optimierung des Flugverkehrs [9]




### 2.3 Vorteile und Möglichkeiten
* Bereitstellung eines zentralen Datenpools [3]
* flexibler Zugriff auf ausgewählte Datenausschnitte [5]
* Zugriff auf *Analysis Ready Data (ARD)* [3]
* flexible Anwendbarkeit, z.B. über Cloud-Services als auch lokal [5]
* einfache und schnelle Analyse verhältnismäßig großer (EO-)Datenmengen [5]
* effizientere Entwicklerzusammenarbeit bezüglich Codes und Algorithmen, ermöglicht durch festgelegte Datenstrukturen [3]
* breite Verwendbarkeit der Daten durch standardisierten Abruf über z.B. OGC Web Coverage Service (WCS) [6]


### 2.4 Nachteile und Herausforderungen
* Bildung von Datenwürfeln aufgrund großer Datenmengen oftmals zeitaufwendig [7]
* Vorstrukturierung der Daten notwendig [3]
* Performance abhängig von Datenmengen [5]
* Akzeptanz seitens der Datenlieferanten [3]
* Skalierung auf sämtliche Regionen und Länder [3]


## 3. Quellen

* [1] techopedia (o.J.): What is a Data Cube?. https://www.techopedia.com/definition/28530/data-cube Abgerufen am 01.11.2020
* [2] guru99 (o.J.): What is OLAP? Cube, Operations & Types in Data Warehouse. https://www.guru99.com/online-analytical-processing.html Abgerufen am 01.11.2020
* [3] opendatacube (o.J.): An Open Source Geospatial Data Management and Analysis Platform. https://www.opendatacube.org Abgerufen am 31.10.2020
* [4] Euro Data Cube (o.J.): Euro Data Cube Services. https://cockpit.hub.eox.at/storage/uploads/edc-editor/Euro_Data_Cube_summary_brochure.pdf Abgerufen am 01.11.2020
* [5] Galaktikasoft (o.J.): OLAP Cubes. https://galaktika-soft.com/blog/olap-cubes.html Abgerufen am 01.11.2020
* [6] Business Geomatics (2019): rasdaman: Einfache Handhabung von Big Data dank Cube-Technologie. https://www.business-geomatics.com/2019/02/04/mit-den-diensten-der-foederation/ Abgerufen am 01.11.2020
* [7] MCA Connect (2017): The Trouble with Data Cubes. https://blog.mcaconnect.com/trouble-data-cubes Abgerufen am 02.11.2020
* [8] Baumann, P. (2017): The Datacube Manifesto. https://www.earthserver.eu/tech/datacube-manifesto/The-Datacube-Manifesto.pdf Abgerufen am 01.11.2020
* [9] enacademic (o.J.): Next Generation Network Enabled Weather. https://enacademic.com/dic.nsf/enwiki/11816251 Abgerufen am 01.11.2020
* [10] Euro Data Cube (o.J.): The EO Information Factory. https://eurodatacube.com/#features Abgerufen am 02.11.2020
