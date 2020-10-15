@digilog11

# STAC

## Was ist STAC?

- Eine **Spezifikation** / Ein **Standard**

STAC ist eine Sprache zur Beschreibung von räumlichen Information, sodass diese leichter entdeckt werden können.

Mit „Spatiotemporal Asset“ sind alle Dokumente gemeint, die Information mit Raum- und Zeitbezug über die Erde repräsentieren. Momentan sind dies hauptsächlich Fernerkundungsaufnahmen (Satellit, Flugzeug, Drohne etc.), aber STAC ist erweiterbar auf SAR, Full Motion Pictures, Point Clouds, Hyperspectral, LiDAR und abgeleitete Daten wie NDVI, Digital Elevation Models, Mosaics etc. STAC arbeitet nicht mit Vektordaten.

- Eine **Community**

STAC ist ebenfalls eine Community von Developern, siehe das [STAC Github Repository](https://github.com/radiantearth/stac-spec). Die Unternehmen in der Darstellung unterstützen die Entwicklung von STAC.

![STAC Unternehmen](https://stacspec.org/images/STAC_companies.png)

## Gründe für die Entwicklung von STAC

Geodaten existieren heutzutage in vielen verschiedenen Formaten. Es gibt keinen einheitlichen Weg Geodaten zu finden, was die Suche und Nutzung der Geodaten erschwert.

Ein Beispiel: Ein User sucht nach Satellitenfotos einer Region zu einer bestimmten Zeit. Dafür reicht nicht eine Suche, der User muss verschiedene Tools und APIs benutzten, die zwar ähnlich, aber leicht unterschiedlich sind.

## Ziele von STAC

Die Hauptziele sind eine erhöhte **Zugänglichkeit und Interoperabilität**.

STAC möchte als standardisierter Weg für die Veröffentlichung raumzeitlicher Informationen dienen, sodass nicht für jedes neue Dataset oder API neuer Code geschrieben werden muss.

Dazu sollen die Veröffentlichung von Geodaten und das Durchsuchen (Crawlen) von Geodaten vereinfacht werden.

## STAC Spezifikation

Die STAC Spezifikation beschreibt die Standardisierung von Metadaten, Namenskonventionen, Query Language (zukünftig) und Katalogstruktur.

STAC nutzt das JSON-Format. Das Kern GeoJSON-Objekt kann erweitert werden um es für verschiedene Domänen anzupassen. Die JSON-Seiten können in interaktive HTML-Seiten umgewandelt werden.

Die Spezifikation besteht aus 4 semi-unabhängigen Spezifikationen, die alleine oder zusammen genutzt werden können. Diese sind:

- STAC Item: einzelnes Spatiotemporal Asset

- STAC Catalog: JSON-Datei mit Links zur Strukturierung/Organisation von STAC-Items

- STAC Collection: Erweiterung des STAC Catalog

- STAC API: RESTful Suche nach STAC Items

### STAC Item

Ein STAC Item ist ein GeoJSON-Feature und repräsentiert eine nicht weiter teilbare Kollektion von Daten und Metadaten.

Als GeoJSON hat es Felder für id, type, bbox, geometry und properties. Das JSON kann erweitert werden mit Feldern für ein Thumbnail, Asset Links zu Daten, Relationship Links zu verwandten STAC Items und mehr.

Weitere Infos: [STAC Item Spezifikation](https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md)

### STAC Catalog

Bei dem STAC Catalog handelt es sich um eine JSON-Datei mit einer Liste von STAC Items und/oder eine Liste von Sub-Catalogs, wodurch eine hierarchische Anordnung von STAC Items möglich ist. STAC Catalogs haben eine flexible Struktur und linken STAC Items, damit sie leicht gecrawlt oder durchgebrowst werden können.

Weitere Infos: [STAC Catalog Spezifikation](https://github.com/radiantearth/stac-spec/blob/master/catalog-spec/catalog-spec.md)

### STAC Collection

Die STAC Collection ist eine Erweiterung des STAC Catalog. Eine STAC Collection enthält zusätzliche Felder für die Beschreibung des räumlichen und zeitlichen Umfangs der Daten, der Lizenz, der Keywords, der Anbieter etc. 

Weitere Infos: [STAC Collection Spezifikation](https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md)
      
### STAC API

Die STAC API ist ein RESTful Service Interface für die Suche nach STAC Items. Sie generiert eine GeoJSON FeatureCollection an STAC Items als Antwort zu einer User Anfrage. Als Anfrage nimmt sie ein JSON Objekt entgegen und filtert nach Raum und Zeit. Als Antwort werden alle Catalog Items zurückgegeben, die die Filterbedingungen erfüllen.

Beispiel User Query:
>{
>  "bbox": [5.5, 46, 8, 47.4], 
>  "time": "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
>}

Die STAC API will OGCs WFS 3 Spezifikation erfüllen. 

Weitere Infos: [STAC API Spezifikation](https://github.com/radiantearth/stac-api-spec/blob/master/api-spec.md)

## STAC Tools

Es existieren eine Reihe an Tools, die die Nutzung der STAC Spezifikation vereinfachen. Darunter:

- STAC Browser: Browser für STAC Catalogs
  - z.B. [Sentinel 2](https://sentinel.stac.cloud/?t=catalogs)
  - [Landsat](https://landsat.stac.cloud/?t=catalogs)
- STAC Validator: validiert STAC JSON Files gegen die STAC Spezifikation und lokale STAC Extensions
