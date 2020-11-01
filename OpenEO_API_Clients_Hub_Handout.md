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
[Link zur OpenEO Website und den Grafiken](https://openeo.org/about.html#openeo)


### Funktionsumfang der openEO-API
 - Discovery (unter anderem mit [Stac](https://api.openeo.org/#tag/EO-Data-Discovery))
 - Autentifizierung
 - Workflow management und User-definierte Prozesse
 - Filemanagement
 - DataProcessing (Synchron und via Batchjobs)
 - Webservice und Export

## Clients
 - R
 - python
 - JavaScript
 - QGIS
 - WebEditor [(Browser)](https://open-eo.github.io/openeo-web-editor/demo/) 
### Beispielcode
Aus dem **[openeo-earthengine-driver](https://github.com/Open-EO/openeo-earthengine-driver)** git-repo
Ein von einem beliebigen Client bereits durch die API prozessierter Code könnte so aussehen:
[sample-processgraph.json](https://github.com/Open-EO/openeo-earthengine-driver/blob/master/tests/data/sample-processgraph.json)

    {
      "process_graph": {
        "load_collection": {
          "process_id": "load_collection",
          "arguments": {
            "id": "COPERNICUS/S2",
            "spatial_extent": null,
            "temporal_extent": [
              "2018-01-01",
              "2018-01-31"
            ],
            "bands": [
              "B4",
              "B8"
            ]
          },
          "description": "Loading the data; The order of the specified bands is important for the following reduce operation."
        },
        "reduce_bands": {
          "process_id": "reduce_dimension",
          "arguments": {
            "data": {
              "from_node": "load_collection"
            },
            "reducer": {
              "process_graph": {
                "red": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "label": "B4"
                  }
                },
                "nir": {
                  "process_id": "array_element",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    },
                    "label": "B8"
                  }
                },
                "ndvi": {
                  "process_id": "normalized_difference",
                  "arguments": {
                    "x": {
                      "from_node": "nir"
                    },
                    "y": {
                      "from_node": "red"
                    }
                  },
                  "result": true
                }
              }
            },
            "dimension": "bands"
          },
          "description": "Compute the NDVI: (NIR - RED) / (NIR + RED)"
        },
        "reduce_time": {
          "process_id": "reduce_dimension",
          "arguments": {
            "data": {
              "from_node": "reduce_bands"
            },
            "reducer": {
              "process_graph": {
                "max": {
                  "process_id": "max",
                  "arguments": {
                    "data": {
                      "from_parameter": "data"
                    }
                  },
                  "result": true
                }
              }
            },
            "dimension": "t"
          },
          "description": "Compute a minimum time composite by reducing the temporal dimension"
        },
        "save": {
          "process_id": "save_result",
          "arguments": {
            "data": {
              "from_node": "reduce_time"
            },
            "format": "GTIFF-THUMB"
          },
          "result": true
        }
      }
    }
Der Code würde dann für einen bestimmten Server weiter übersetzt werden.
Im WebEditor lässt sich der Code auch als *Visual Model* darstellen und verändern.

## Hub

- Teil des openEO-Ecosystems. 
- Eine [Plattform](https://hub.openeo.org/)   um Server, Daten und schon implementierte Prozesse zu überschauen und anzubieten.
	- Unter anderem _Google Earth Engine Proxy for openEO_
- Prüft eigenen Code und kann anzeigen mit welchen Servern dieser kompatibel ist.
- Eigene Prozesse können mit der Community geteilt werden.
