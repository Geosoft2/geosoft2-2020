@digilog11

# STAC: Spatiotemporal Asset Catalogs

## Was ist STAC?

STAC ist eine **Spezifikation**

STAC ist eine Sprache zur Beschreibung von räumlichen Katalogen und Assets. Der Fokus liegt auf die Suche und Entdeckung von Daten.

Mit „Spatiotemporal Asset“ sind alle Dokumente gemeint, die Information mit Raum- und Zeitbezug über die Erde repräsentieren. Momentan sind dies hauptsächlich Fernerkundungsaufnahmen (Satellit, Flugzeug, Drohne etc.), aber STAC ist erweiterbar auf SAR, Full Motion Pictures, Point Clouds, Hyperspectral, LiDAR und abgeleitete Daten wie NDVI, Digital Elevation Models, Mosaics etc. STAC arbeitet nicht mit Vektordaten.

STAC ist ebenfalls eine **Community**

STAC ist ebenfalls eine Community von Developern, siehe das [STAC Github Repository](https://github.com/radiantearth/stac-spec). Die Unternehmen in der Darstellung unterstützen die Entwicklung von STAC/nutzen STAC.

![STAC Unternehmen](https://stacspec.org/images/STAC_companies.png)

Weitere Infos: [Website STAC](https://stacspec.org/), [Video Vorstellung STAC](http://bofh.nikhef.nl/events/FOSDEM/2020/AW1.126/introduction_to_spatiotemporal_asset_catalogs_stac.mp4) 

## Gründe für die Entwicklung von STAC

Geodaten existieren heutzutage in vielen verschiedenen Formaten. Es gibt keinen einheitlichen Weg Geodaten zu finden, was die Suche und Nutzung der Geodaten erschwert. Man muss viele verschiedene Portale kennen und diese durchsuchen ([USGSEarthExplorer](https://earthexplorer.usgs.gov/), [Copernicus Open Access Hub](https://scihub.copernicus.eu/dhus/#/home), [NASA Earthdata Search](https://search.earthdata.nasa.gov/search) ...), um an die gewünschten Geodaten zu kommen. Es gibt auch viele verschiedene APIs, die zwar ähnlich, aber leicht unterschiedlich sind und z.B. verschiedene Endpoints und Filterparameter haben.

Data Users haben zusätzlichen Aufwand durch die schwierige Suche nach Daten und dem Schreiben neuen Codes für jede Datenkollektion, die sie nutzten.

Weitere Infos: [Website STAC](https://stacspec.org/why-stac.html)

## Ziele von STAC

Die Hauptziele sind eine erhöhte **Zugänglichkeit und Interoperabilität**.

STAC möchte als standardisierter Weg für die Veröffentlichung raumzeitlicher Informationen dienen, sodass nicht für jedes neue Dataset oder API neuer Code geschrieben werden muss.

Dazu sollen die Veröffentlichung von Geodaten und das Durchsuchen (Crawlen) von Geodaten vereinfacht werden.

Weitere Infos: [Website STAC](https://stacspec.org/overview.html)

## STAC Spezifikation

Die STAC Spezifikation beschreibt die Standardisierung von Metadaten, Namenskonventionen, Query Language (zukünftig) und Katalogstruktur.

STAC nutzt das JSON-Format. Das Kern GeoJSON-Objekt kann erweitert werden um es für verschiedene Domänen anzupassen. Die JSON-Seiten können in interaktive HTML-Seiten umgewandelt werden.

Die Spezifikation besteht aus 4 semi-unabhängigen Spezifikationen, die alleine oder zusammen genutzt werden können. Diese sind:

- STAC Item: einzelnes Spatiotemporal Asset

- STAC Catalog: JSON-Datei mit Links zur Strukturierung/Organisation von STAC-Items

- STAC Collection: Erweiterung des STAC Catalog

- STAC API: RESTful Suche nach STAC Items

### STAC Item

Ein STAC Item ist ein GeoJSON-Feature und repräsentiert eine nicht weiter teilbare Kollektion von Daten und Metadaten. Ein Item könnte zum Beispiel ein Satellitenfoto sein und seine Bänder sind Assets. Assets sind Dateien zum Downloaden.

Als GeoJSON hat das STAC Item Felder für id, type, bbox, geometry und properties. Das STAC Item hat zusätzliche Felder für ein Thumbnail, Asset Links zu Daten, Relationship Links zu verwandten STAC Items und mehr.

Beispiele: [Minimales Beispiel](https://github.com/radiantearth/stac-spec/blob/master/item-spec/examples/sample.json), [Ausgebautes Beispiel](https://github.com/radiantearth/stac-spec/blob/master/item-spec/examples/sample-full.json)

Weitere Infos: [Website STAC](https://stacspec.org/core.html), [STAC Item Spezifikation](https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md)

### STAC Catalog

Bei dem STAC Catalog handelt es sich um eine JSON-Datei mit einer Liste von STAC Items und/oder eine Liste von Sub-Catalogs, wodurch eine hierarchische Anordnung von STAC Items möglich ist. STAC Catalogs haben eine flexible Struktur und linken STAC Items, damit sie leicht gecrawlt oder durchgebrowst werden können.

STAC Catalogs können als statische oder dynamische Kataloge implementiert werden. Statische Kataloge bestehen aus einem Set aus Dateien auf einem Web-Server, die zueinander linken und deswegen gecrawlt werden können. Dynamische Kataloge werden als API implementiert und antworten dynamisch auf Nutzeranfragen. Statische Kataloge bieten den Vorteil, dass sie sehr zuverlässig und einfacher zu implementieren sind.

Beispiele: [Minimales Beispiel](https://github.com/radiantearth/stac-spec/blob/master/catalog-spec/examples/catalog.json), [Ausgebautes Beispiel](https://github.com/radiantearth/stac-spec/blob/master/catalog-spec/examples/catalog-items.json)

Weitere Infos: [STAC Website](https://stacspec.org/core.html), [STAC Catalog Spezifikation](https://github.com/radiantearth/stac-spec/blob/master/catalog-spec/catalog-spec.md)

### STAC Collection

Die STAC Collection ist eine Erweiterung des STAC Catalog. Eine STAC Collection enthält zusätzliche Felder für die Beschreibung des räumlichen und zeitlichen Umfangs der Daten, der Lizenz, der Keywords, der Anbieter etc. 

Beispiele: [Collection ohne Item](https://github.com/radiantearth/stac-spec/blob/master/collection-spec/examples/sentinel2.json), [Collection mit Item](https://github.com/radiantearth/stac-spec/blob/master/collection-spec/examples/landsat-collection.json)

Weitere Infos: [Website STAC](https://stacspec.org/core.html), [STAC Collection Spezifikation](https://github.com/radiantearth/stac-spec/blob/master/collection-spec/collection-spec.md)
      
### STAC API

Die STAC API ist ein RESTful Service Interface für die Suche nach STAC Items. Sie generiert eine GeoJSON FeatureCollection an STAC Items als Antwort zu einer User Anfrage. Als Anfrage nimmt sie ein JSON Objekt entgegen und filtert nach Raum und Zeit. Als Antwort werden alle Catalog Items zurückgegeben, die die Filterbedingungen erfüllen.

Beispiel User Query:
>{
>  "bbox": [5.5, 46, 8, 47.4], 
>  "time": "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
>}

Die STAC API will OGCs WFS 3 Spezifikation erfüllen. 

Weitere Infos: [STAC Website](https://stacspec.org/core.html), [STAC API Spezifikation](https://github.com/radiantearth/stac-api-spec/blob/master/api-spec.md)

## STAC Extensions

## STAC Tools

Es existieren eine Reihe an Tools, die die Nutzung der STAC Spezifikation vereinfachen. Darunter:

- STAC Browser: Browser für STAC Catalogs
  - z.B. [Sentinel 2](https://sentinel.stac.cloud/?t=catalogs), [Landsat](https://landsat.stac.cloud/?t=catalogs)
- STAC Validator: validiert STAC JSON Files gegen die STAC Spezifikation und lokale STAC Extensions
- [STAC Index](https://stacindex.org/ecosystem): alle Software und Tools für STAC
