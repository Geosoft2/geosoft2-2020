@jana2308walter

# Open EO 

Quelle: https://openeo.org/

## Was ist das? 

openEO ist eine offene API, die R, Python, JavaScript u. a. auf einheitliche Weise mit Backends zur Erdbeobachtung verbindet

#### Vorteile:
* Jeder Client kann mit jedem Backend arbeiten
* Backends können vor der Nutzung verglichen werden (Kosten, Ergebnisse, Kapazitäten)

#### openEO: 
* open: Open Source Software in Form von source code, die modifiziert und verändert werden kann
* EO: Earth Observation

#### Ziele des Projektes: 
* Simplicity: Einfachheit zur Nutzung der Daten und Verarbeitung der Ergebnisse mit verschiedenen Clients
* Unification: Einheitlichkeit der EO – Cloudbackends 

#### Probleme, die openEO beheben soll:
* Erdbeobachtungsdaten sind zu groß, um von jedem User runtergeladen zu werden
* Außerdem sind die Daten zu unstrukturiert und unsortiert, um übersichtlich zu sein

#### Lösung: 
Daten werden in der Cloud und in Backends gespeichert und verarbeitet, dann können die Ergebnisse heruntergeladen werden


## Prozesse

Es gibt interoperable Prozesse zur Verarbeitung großer Datenmengen von EO - Daten
Dabei wird jeder Prozess in einer separaten JSON – Datei angegeben, die dem passenden API – Prozessschema entspricht

Beispieldatei: [ceil.json] (https://github.com/Open-EO/openeo-processes/blob/master/ceil.json)

```
{
    "id": "ceil",
    "summary": "Round fractions up",
    "description": "The least integer greater than or equal to the number `x`.\n\nThe no-data value `null` is passed through and therefore gets propagated.",
    "categories": 
	[
	    "math > rounding"
	],
	"parameters": 
	[
	    {
	        "name": "x",
	        "description": "A number to round up.",
	        "schema": 
			{
	            "type": 
				[
					"number",
	                "null"
	            ]
	        }
	    }
	],
	"returns": 
	{
	    "description": "The number rounded up.",
	    "schema": 
		{
	        "type": 
			[
	            "integer",
	            "null"
	        ]
	    }
	},
	"examples": 
	[
	    {
	        "arguments": 
			{
	            "x": 0
	        },
	        "returns": 0
	    },
	    {
	        "arguments": 
			{
	            "x": 3.5
	        },
	        "returns": 4
	    },
	    {
	        "arguments": 
			{
	            "x": -0.4
	        },
	        "returns": 0
		},
	    {
	        "arguments": 
			{
	            "x": -3.5
	        },
	        "returns": -3
	    }
	],
	"links": 
	[
	    {
	        "rel": "about",
	        "href": "http://mathworld.wolfram.com/CeilingFunction.html",
	        "title": "Ceiling explained by Wolfram MathWorld"
	    }
	]
}
```


## Backends:

Die Daten – und Infrastrukturprovider können eine eigene Instanz der openEO API hosten.
Einige Beispiele hierfür sind:
  * GeoPySpark
  * Google Earth Engine
  * GRASS GIS
  * Sentinel Hub
  
Um einen eigenen Backend – Treiber zu starten, sollte man mit den gemeinsamen Funktionalitäten, die in einigen Programmiersprachen (z. B.: Java (Spring) API Commons, Python API Commons) implementiert sind, beginnen


## openEO Plattform:

#### Was ist das?
* Ein neues Projekt auf openEO
* Dieses bietet Datenzugriff und Datenverarbeitungsservice für die Community

#### Wer ist beteiligt?
* Gegründet von der ESA, gestartet in September 2020
* Mehrere Beteiligte: EODC, EGI, EURAC, GEO, Sinergise, VITO, WWU

![overview-openeo](https://openeo.org/assets/img/overview.dfa7e5ae.jpg)

#### Welche Verarbeitungsplattformen?
* Proba-V Exploitation Plattform: Eine der ersten privaten Clouds für EO in Europa
* Sentinel Hub: Fortgeschrittenste „on-the-fly“ Sattelitendaten – Verarbeitungsmaschine, die jeden Monat mehr als 100 000 Anfragen behandelt
* Data Cube Facility Services
* EODCs Cloud Infrastructure and HPC Experience

#### Details zur Realisierung und den Zielen der Plattform:
* Plattform wird mit der openEO API als Community Projekt mit einem userfreundlichen Ökosystem mit graphischen und command – line - basierten Clients realisiert
* Damit werden die Ziele der openEO API und der ESA vereint, die die Vereinfachung und Einheitlichkeit verschiedener Backends zur Datenverarbeitung vorsehen
* Die Plattform will verschiedene Zielgruppen bedienen, indem verschiedene Clients und Interfaces genutzt werden können, je nach den Bedürfnissen der User

#### Userbeispiele:
* Fernerkundungsforscher können ein Frontend mit JupyterLab als Hauptfrontend für Data Science verwenden
* R – Nutzer können den openEO R – Client nutzen und in RStudio entwickeln
* Interaktive Workflows können zum Erkunden von Ergebnissen und zum Verwalten von Jobs graphisch erstellt werden
* Softwareentwickler können in eigener DIE arbeiten, um Dienste in Anwendungen zu integrieren 

#### Geteilte Dienste für die Plattform
* Alle Schnittstellen teilen sich die clientseitigen openEO – Bibliotheken zur Minimierung der Komplexität (Für Python, R und JavaScript bereits verfügbar)
* Außerdem können OGC – Dienste verfügbar gemacht werden, um die Interoperabilität mit vorhandenen Tools sicherzustellen
* Das Open – Development – Modell wird während der Entwicklung beibehalten, damit ein interaktives Community – Projekt geschaffen werden kann
* Das Alleinstellungsmerkmal von openEO für diese Plattform ist die kombinierte Funktion vordefinierter und benutzerdefinierter Funktionen („Das Beste aus zwei Welten“)
* Es geht um die Optimierung alltäglicher Aufgaben durch Backend – Anbieter und trotzdem hat der Benutzer Zugriff auf Bibliotheken und Tools wie TensorFlow, GDAL, SNAP und OpenCV, dabei ist die Verwendung nur so komplex wie das Schreiben eines einfachen Codes
* Gewollt ist eine Erweiterung der Beispiele, Bibliotheken und Dokumentationen durch die Community
* Der Data Cube – Service wird aktualisiert, um als Verteilungsmittel für verschiedene abgeleitete Produkte zu dienen, nicht nur zur Visualisierung, sondern auch zur Ergebnisanalyse

#### Machine Learning (ML) und künstliche Intelligenz (KI)
* Schlüsseltechnologien, die ebenfalls bereitgestellt werden
* Basierend auf Kombination von Erdbeobachtungsrasterdaten mit anderen Datensätzen in verschiedenen Formaten, die durch flexible Datenzugriffsmechanismen unterstützt werden
* Plattform wird integrierte ML – Algorithmen für benutzerfreundliche Nutzung, externe Bibliotheken für Flexibilität und den Export für die Verwendung in externen KI - Diensten unterstützen, um ein geschlossenes Ökosystem aufzubauen

#### Kosten und Bezahlung
* Gesamtkonzept wurde auf Nachhaltigkeit ausgelegt, was durch niedrige Betriebskosten und dem Aufbau auf bestehenden Diensten mit eigener Nutzerbasis und deren Einnahmen sichergestellt wird
* Für die Mehrheit der Betriebskosten zahlen die Nutzer, die die Prozesse ausführen und dafür bezahlen
* Außerdem werden Docker – Container zur Skalierbarkeit des Systems verwendet
* Kostenlose Testversionen zur Benutzeraufnahme
* Es gibt drei Umsatzmodelle:
  * Startpaket: Angeboten über ein pauschalbasiertes Abrechnungsmodell
  * Entwicklerpaket: Basierend auf einem Pay – per – Use – System für die Stückkosten pro Artikel
  * Custompaket: Auf geschätztem Aufwand und den erforderlichen Ressourcen basierend, einschließlich individueller Unterstützung