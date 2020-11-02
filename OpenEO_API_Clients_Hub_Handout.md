# Handout: "OpenEO API, Clients, Hub"

@FelixGI1516


## Was ist OpenEO

Moderne GeoDaten sind zu groß um sie auf den eigenen PC zu laden und zu analysieren.

Die Art und Weise wie wir Geoinformatik in DigiKarto oder dem GIS-Grundkurs gemacht haben (Analyse einzelner Kartenabschnitte zu statischen Zeitpunkten) ist nicht wirklich praktikabel.
Die Lösung ist GeoDaten in "der Cloud" (*someone else's bigger computer*/Server) zu **speichern**, im *back-end* zu **verarbeiten**, zu **betrachten** und dann entsprechende Ergebnisse **herunterzuladen**.

## API
### Allgemein
Ausgeschrieben *application programming interface*.
Eine API definiert eine Sprache, mit der Client und Server untereinander kommunizieren können.
Problem: Server von unterschiedlichen Anbietern "sprechen" unterschiedliche Sprachen und Clients sowieso.

OpenEO ist ein Projekt zur Schaffung einer gemeinsamen Sprache/Schnittstelle für verschiedene GeoDaten-Server und zur Vereinfachung der Zugriffe auf diese Server mit unterschiedlichen Clients.
![Structure with openEO](https://openeo.org/images/api2.png)

[Link zur OpenEO Website](https://openeo.org/about.html#openeo)


### Funktionsumfang der openEO-API
 - Discovery (unter anderem mit [Stac](https://api.openeo.org/#tag/EO-Data-Discovery))
 - Autentifizierung
 - Workflow management und User-definierte Prozesse
 - Filemanagement
 - DataProcessing (Synchron und via Batchjobs)
 - Webservice und Export
 - [Link zur OpenEO Dokumentation](https://openeo.org/documentation/1.0/developers/api/reference.html)

## Clients

 - R
 - python
 - JavaScript
 
Unter [openEO Getting started](https://openeo.org/documentation/1.0/getting-started.html) findet man Beispiele und weiterführende Links zur Dokumentation für die oberen 3 Clients.
Außerdem gibt es weitere Clients:
 - QGIS
 - WebEditor [(Browser)](https://open-eo.github.io/openeo-web-editor/demo/) 
### Beispielcode
Aus dem **[openeo-earthengine-driver](https://github.com/Open-EO/openeo-earthengine-driver)** git-repo
Ein von einem beliebigen Client bereits durch die API prozessierter Code könnte so aussehen:
[sample-processgraph.json](https://github.com/Open-EO/openeo-earthengine-driver/blob/master/tests/data/sample-processgraph.json)

Im WebEditor lässt sich von der API verarbeiteter Code wieder als *Visual Model* darstellen und verändern.

## Hub

- Teil des openEO-Ecosystems. 
- Eine [Plattform](https://hub.openeo.org/)   um Server, Daten und schon implementierte Prozesse zu überschauen und anzubieten.
	- Unter anderem _Google Earth Engine Proxy for openEO_
- Prüft eigenen Code und kann anzeigen mit welchen Servern dieser kompatibel ist.
- Eigene Prozesse können mit der Community geteilt werden.
- Bietet Zugriff auf Prozessdokumentationen.
