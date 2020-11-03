# Datenwürfel für Fernerkundungsdaten, Klimamodelle und Wetterdaten
@neli98

## Datenwürfel allgemein
* auch bekannt als OLAP-Würfel (OLAP = Online Analytical Processing)
* relevant im Bereich des Data-Warehousing
* nützlich zur Strukturierung von Daten (Big Data)
* beliebig viele Dimensionen möglich
  * leicht vorzustellen als 3D-Würfel (siehe untenstehende Grafik)
* Speicherung der Daten in einzelnen Elementen des Würfels
* dynamische Betrachtungsweisen der Daten aus verschiedenen Perspektiven möglich
* verschiedene Grundoperationen, wie z.B.:
  * Slice-Operation (Ausschneiden einer Datenscheibe)
  * Dice-Operation (Erzeugen eines kleineren Würfels aus Ursprungswürfel)
* graphische Veranschaulichung anhand eines Beispiels aus der Betriebswirtschaft:
![Data Cube](https://images.tecchannel.de/bdb/362924/840x473.jpg)


## Datenwürfel im Kontext der Geoinformatik

### Anwendungsfälle
* hilfreich beim Umgang mit großen, multidimensionalen GIS-Datenmengen - speziell Earth Observation(EO)-Daten
  * speziell bei Daten mit zeitlicher Dimension
  * Schnittstelle zwischen Daten und Nutzeranwendungen
* Vereinfachung der Analyse von z.B.:
  * Abholzung/Rodung von Wäldern
  * illegalem Rohstoffabbau
  * Dürreregionen
  * Bedeckung des Bodens durch Schnee
  * Wetterentwicklungen


### Beispiele
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



### Vorteile und Möglichkeiten
* Bereitstellung eines zentralen Datenpools
* flexibler Zugriff auf ausgewählte Datenausschnitte
* Zugriff auf *Analysis Ready Data (ARD)*
* flexible Anwendbarkeit, z.B. über Cloud-Services als auch lokal
* Ermöglichung der einfachen und schnellen Analyse verhältnismäßig großer (EO-)Datenmengen
* effizientere Entwicklerzusammenarbeit bezüglich Codes und Algorithmen, ermöglicht durch festgelegte Datenstrukturen
* breite Verwendbarkeit der Daten durch standardisierten Abruf über z.B. OGC Web Coverage Service (WCS)


### Nachteile und Herausforderungen
* Bildung von Datenwürfeln aufgrund großer Datenmengen oftmals zeitaufwendig
* Vorstrukturierung der Daten notwendig
* Performance abhängig von Datenmengen
* Akzeptanz und Skalierbarkeit (des Open Data Cube)
