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
* hilfreich beim Umgang mit großen, multidimensionalen GIS-Datenmengen - speziell Earth Observation(EO)-Daten [3]
  * speziell bei Daten mit zeitlicher Dimension
  * Schnittstelle zwischen Daten und Nutzeranwendungen
* Vereinfachung der Analyse von z.B.:
  * Abholzung/Rodung von Wäldern [3]
  * illegalem Rohstoffabbau [3]
  * Dürreregionen [4]
  * Wetterentwicklungen [4]


### 2.2 Beispiele
* Open Data Cube ([mehr Informationen](https://www.opendatacube.org))
  * internationale Open-Source Initiative
  * freie Bereitstellung von EO-Daten
   * z.B. zur Unterstützung der Analyse in Hinblick auf die SDG's
   * dadurch Liberalisierung und Erhöhung des Nutzens der Daten
   * Bereitstellung über eine auf Python basierende API
* Earth Server ([mehr Informationen](https://www.earthserver.eu))
  * Zusammenschluss mehrerer internationaler Forschungseinrichtungen
  * Bereitstellung von 3D-Satellitenbildern und 4D-Wetterdaten
* Next Generation Network Enabled Weather Project ([mehr Informationen](https://en.wikipedia.org/wiki/Next_Generation_Network_Enabled_Weather))
  * Initiative der USA
  * Bereitstellung von 4D-Wetterdaten
  * Analyse von Wetterdaten zur besseren Wettervorhersage und Optimierung des Flugverkehrs
* Euro Data Cube ([mehr Informationen](https://eurodatacube.com/#features))



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
* Akzeptanz und Skalierbarkeit [3]


## 3. Quellen

* [1] https://www.techopedia.com/definition/28530/data-cube
* [2] https://www.guru99.com/online-analytical-processing.html
* [3] https://www.opendatacube.org
* [4] https://cockpit.hub.eox.at/storage/uploads/edc-editor/Euro_Data_Cube_summary_brochure.pdf
* [5] https://galaktika-soft.com/blog/olap-cubes.html
* [6] https://www.business-geomatics.com/2019/02/04/mit-den-diensten-der-foederation/
* [7] https://blog.mcaconnect.com/trouble-data-cubes
