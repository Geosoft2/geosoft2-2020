# Datenwürfel für Fernerkundungsdaten, Klimamodelle und Wetterdaten
@neli98

## Datenwürfel allgemein
* auch bekannt als OLAP-Würfel (OLAP = Online Analytical Processing)
* relevant im Bereich des Data-Warehousing
* nützlich zur Strukturierung von Daten
* beliebig viele Dimensionen möglich
* Speicherung der Daten in einzelnen Elementen des Würfels
  * leicht vorzustellen bei 3D-Würfel (siehe untenstehende Grafik)
* unterschiedliche Dimensionen ermöglichen dynamische Betrachtungsweisen der Daten aus verschiedenen Perspektiven
* verschiedene Grundoperationen, wie z.B.:
  * Slice-Operation (Ausschneiden einer Datenscheibe)
  * Dice-Operation (Erzeugen eines kleineren Würfels aus Ursprungswürfel)
  * Drill-Down-Operation (Hineinzoomen und Auslesen detaillierterer Daten)
* graphische Veranschaulichung anhand eines Beispiels aus der Betriebswirtschaft:
![Data Cube](https://images.tecchannel.de/bdb/362924/840x473.jpg)


## Datenwürfel im geographischen Kontext

### Anwendungsfälle
* hilfreich beim Umgang mit großen, multidimensionalen GIS-Datenmengen - speziell Earth Observation(EO)-Daten
* Analyse von z.B.:
  * Abholzung/Rodung von Wäldern
  * illegalem Rohstoffabbau
  * Dürreregionen
  * Bedeckung des Bodens durch Schnee
  * Wetterentwicklungen


### Beispiele
* Open Data Cube ([mehr Informationen](https://www.opendatacube.org))
  * internationale Open-Source Initiative
  * Bereitstellung und Analyse von EO-Daten, z.B. zur Unterstützung der Analyse in Hinblick auf die SDG's
* Next Generation Network Enabled Weather Project ([mehr Informationen](https://en.wikipedia.org/wiki/Next_Generation_Network_Enabled_Weather))
  * Initiative der USA
  * 4D-Wetterdaten-Würfel
  * Analyse von Wetterdaten zur besseren Wettervorhersage und Optimierung des Flugverkehrs
* Earth Server ([mehr Informationen](https://www.earthserver.eu))
  * Initiative unterstützt durch die EU
  * Bereitstellung von 3D-Satellitendaten und 4D-Wetterdaten


### Vorteile
* Bereitstellung eines zentralen Datenpools
* Zugriff auf *Analysis Ready Data (ARD)*
* flexibler Zugriff auf ausgewählte Datenausschnitte möglich
* flexible Anwendbarkeit, z.B. über Cloud-Services oder lokal
* Ermöglichung der (einfachen) Analyse großer Datenmengen


### Nachteile
* Bildung von Datenwürfeln aufgrund großer Datenmengen oftmals zeitaufwendig
* Vorstrukturierung der Daten notwendig
* Performance abhängig von Datenmengen
