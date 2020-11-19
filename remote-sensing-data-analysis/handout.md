**Analyse von satellietenbasiertern Fernerkundsungsdaten / Analysing Remote Sensing Data**

**Fernerkundung**
Def.: berührungsfreise Datenerfassung, sowie die analyse und interpretation dieser Daten

**Fernerkundungsdaten**
Geodaten, üblicherweise Luftaufnahmen
- 2 verschiedene Formate:
	- Rasterdaten
	- Vektordaten
Um die Unterschiede zu verdeutlichen kann die folgende Grafik dienen:
https://slideplayer.org/slide/13329129/80/images/5/Vektor-+und+Rasterdaten.jpg

Für Rasterdaten werden hauptsächlich vier Auflösungsdimensionen berücksichtigt:
	- zeitlich (Variationen, z.B. Herbst/Frühling)
	- räumlich (Variationen, z.B. m/Pixel, d.h. Größenveränderung, Maßstab)
	- radiometrisch (Datentiefen, z.B. 8 bit, 16 bit etc. mögliche Werte pro Pixel)
	- spektral (Wellenlängen, z.B. VIS und IR, Kanäle)


**Datenerfassung**
Üblicherweise durch Luftaufnahmen
Die umfassendste Art diese auf zu nehmen ist per Satellite, 
lokal eignen sich ebenfalls Drohnen und Flugzeuge mit speziellen Aufnahmesystemen

Die Sensoren der Aufnahmesysteme messen Variationen physikalisch:
	- Druckfelder (z.B. Meteorologie, Klimatologie)
	- Schwerefelder (z.B. Geophysik, Planetologie)
	- elektrostatische Felder (z.B. Geophysik, Planetologie)
	- elektromagnetische Felder (z.B. Geologie, Geophysik, Planetologie, Oekologie, Klimatologie, Geographie i.w.S.)


**Verwendungszweck der Fernerkundsungsdaten**
größte Einsatzgebiete:
	- Raumplanung
	- Umweltschutz
	- Versorgungswirtschaft
	- Lagerstättenexploration
	- Kartographie
	- Katastrophenmanagement
	- Raum-Überwachung
	- Raumanalysen
expliziete Beispiele: 
	- Erkennen von Vegatation
	- Erstellen von Karten

https://ivvgeo.uni-muenster.de/vorlesung/FE_Script/1_2.html

**Verarbeitung und Verbreitung von Fernerkundsungsdaten**

Verarbeitungsschritte:
	- Digitalisieren der Sensordaten zu "Bildern" 
	- Preprocessing der Rohdaten (Korrekturen der Rohdaten)
	- Automatisierte Prozesse (z.B. für Satellietengestütze Karten)
	- manuelle Verarbeitung in GIS
	
Verbreitung:
	- Sowohl kostenlose Open Source, aber auch kostenpflichtige Dienste
	- Datensammlung
	- Web-Map-Service (WMS-Dienste)
https://earthexplorer.usgs.gov

**Die häufigsten Probleme bei der Analyse**

Bildvorverarbeitung
- Mosaik
	- Zusammenfügen mehrerer Datensätz, z.B. bei großen Beobachtungsflächen
	R-Beispiel:
	https://www.rdocumentation.org/packages/raster/versions/3.3-13/topics/mosaic
	
- Wolkenentfernung
	- entfernen von Wolken(-schatten) z.B. mit Hilfe von Referenzbildern oder Einbeziehung zusätzlicher Kanäle
	R-Beispiel:
	https://www.earthdatascience.org/courses/earth-analytics/multispectral-remote-sensing-modis/intro-spectral-data-r/
	
- Atmosphärische Korrekturen
	- entfernen der durch die Athmosphäre und Reflektionen verzerrte Strahlung (Wolken/Gase/gestreute Reflexionen)
	Mehr Informationen:
	http://www.fis.uni-bonn.de/recherchetools/infobox/profis/bildvorverarbeitung/atmosph%C3%A4renkorrektur
	
- Geometrische Korrekturen
	- Überführen der Daten in ein Koordinatensystem, sowie Anpassung der Verzerrung
	Mehr Informationen:
	http://www.fis.uni-bonn.de/recherchetools/infobox/profis/bildvorverarbeitung/geometrische-korrektur
	