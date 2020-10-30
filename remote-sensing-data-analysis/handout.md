**Analyse von satellietenbasiertern Fernerkundsungsdaten / Analysing Remote Sensing Data**

**Fernerkundung**
Def.: berührungsfreise Datenerfassung, sowie die analyse und interpretation dieser Daten

**Fernerkundungsdaten**
Geodaten, üblicherweise Luftaufnahmen
- 2 verschiedene Formate:
	- Rasterdaten
	- Vektordaten


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


**Verarbeitung und Verbreitung von Fernerkundsungsdaten**

Verarbeitungsschritte:
	- Digitalisieren der Sensordaten zu "Bildern" 
	- Preprocessing der Rohdaten (Korrekturen)
	- Automatisierte Prozesse 
	- manuelle Verarbeitung in GIS
	
Verbreitung:
	- Sowohl kostenlose Open Source, aber auch kostenpflichtige Dienste
	- Datensammlung
	- Web-Map-Service (WMS-Dienste)


**Die häfigsten Probleme bei der Analyse**
- Mosaik
	- Zusammenfügen mehrerer Datensätz, z.B. bei großen Beobachtungsflächen
- Wolkenentfernung
	- entfernen von Wolken(-schatten) z.B. mit Hilfe von Referenzbildern oder Einbeziehung zusätzlicher Kanäle
Bildvorverarbeitung
- atmospherische Korrekturen
	- entfernen der durch die Athmosphäre und Reflektionen verzerrte Strahlung (Wolken/Gase/gestreute Reflexionen)
- gemetrische Korrekturen
	- Überführen der Daten in ein Koordinatensystem, sowie anpassung der Verzerrung