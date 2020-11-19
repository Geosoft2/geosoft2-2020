#Python packages:

Packages kommen immer dann zum Einsatz, wenn die Anzahl der verwendeten Module innerhalb eines Programmes nicht mehr überschaubar ist. 
Beliebig viele Module können dann zu einem Paket „geschnürt“ werden.
Damit wird eine feste Struktur geschaffen. 
Die geschaffene Übersichtlichkeit erleichtert Zusammenarbeit am gleichen Projekt.

##Packaging:

Um ein Paket in Python zu erstellen sind folgende Schritte notwendig:
	1. 	Erzeugen eines Unterordners in einem Verzeichnis in dem Python Module erwartet bzw. sucht
	2.	Erstellen einer Initialisierungsdatei mit dem Namen __init__.py  
		Diese Datei kann mit Code gefüllt werden der bei Aufruf des Packages einmalig ausgeführt wird
	3.	Einfügen der Module

####Beispiel : 

SimplePackage ist der erzeugte Unterordner.
Darin befindet sich die Initialisierungsdatei und die Module a und b als Pythondatei (.py)
 
Inhalt Modul a: `def f1(): print("Dies ist das erste Modul")`
Inhalt Modul b:	`def f2(): print("Dies ist Modul 2")`

##Zugriff auf das Package: 

1. Navigation in das übergeordnete Verzeichnis
2. In Python mit >>> from SimplePackage import a,b

Jetzt sind die definierten Funktionen f1 und f2 aufrufbar. 
Also erhalten wir mit den Befehlen `a.f1()` den Ausdruck „Dies ist das erste Modul“ 
und `b.f2()` den Ausdruck „Dies ist Modul 2“

Es reicht nicht aus `import SimplePackage` auszuführen, da Module in einem Package nicht automatisch importiert werden.
Möglich wird dies mit einer Änderung der Initialisierungsdatei:
`from SimplePackage import a, b`
Da die Init.Datei beim Importieren des Packages ausgeführt wird, sind die Module direkt verfügbar.

Quelle des Beispiels:  
https://www.python-kurs.eu/python3_pakete.php


##Publishing a Package:

Zum Veröffentlichen des Packages im Python Package Index werden noch einige Informationen benötigt: 

1. Lizenz -> 				zeigt den Nutzern die Bedingungen zum Gebrauch des Packages an. 
							Auf https://choosealicense.com/ können vorgefertigte Lizenzen kopiert werden

2. Readme ->				Erläuterung des Packages, wie ist es zu verwenden, welche Funktionen stehen zur Verfügung

3. Setup ->					beinhaltet Metadaten über das Package (Name, Version, Autor, Beschreibung, Version...)

4. Distribution Packages -> Mit Version versehender Archiv Ordner der alle zum Release benötigten Dateien enthält 
							(Python packages, Module, Readme, Setup)

5. Erstellen eines Kontos ->	https://test.pypi.org/account/register/

6. API Token ->				 https://test.pypi.org/manage/account/#api-tokens

7. twine ->					zum Hochladen der Distribution packages wird ein Tool namens twine verwendet. 
							Dieses muss zuvor installiert werden

8. Kontrolle ->				zur Kontrolle ob das Package erfolgreich hochgeladen wurde 				
							kann es auf https://test.pypi.org gesucht werden

Eine ausführliche Beschreibung wie ein Package veröffentlicht wird ist hier zu finden: 
https://packaging.python.org/tutorials/packaging-projects/



#Semantic Versioning:

Zur Erkennung welche Version eines Programmes vorliegt definiert Semantic Versioning 5 Felder und Regeln für jedes davon:

Major: Major Versionsnummer der Software (natürliche Zahl) 
Minor: Minor Versionsnummer (natürliche Zahl) 
Patch: Patch Versionsnummer (natürliche Zahl)
Pre-Release: Pre-Release Wert (String, nicht näher definiert, meistens „alpha“  „beta“)
Build: Metadaten (werden mit einem „+“ am Ende der Versionsnummer angehangen)

Daraus ergibt sich folgende String Formatierung für die Darstellung von Versionsnummern: 
<major>.<minor>.<patch>[-pre_release][+build]

####Beispiel: 
1.3.4 < 1.3.5 < 2.0.0-alpha < 2.0.0-beta <2.0.0
Ausführliche Erklärung mit Einzelfallbehandlung:
https://semver.org

Für die Erstellung, Bearbeitung und den Vergleich von Versionsnummern gibt es vorgefertigte Module, 
die in den eigenen Code importiert werden können.
Ein Beispiel ist hier zu finden: 
https://pypi.org/project/semantic-version/

#Dependency Management:
##Installieren und Verwalten von Python Packages mit pip
Je nachdem wie Python auf dem Computer installiert wurde ist pip bereits vorhanden. 
Um dies zu prüfen kann im Terminal die Version von pip abgefragt werden (pip --version)
Sollte es nicht vorhanden sein ist hier Anleitung: https://packaging.python.org/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line
pip ermöglicht es dann mit dem Ausruck „pip install „SomePackage“ Packages vom Python Package Index (https://pypi.org) zu installieren
Handelt es sich um mehrere Packages, die installiert werden sollen, oder sollen die gleichen Packages in verschiedenen Projekten verwendet werden können diese in einer .txt Datei gespeichert und mit „pip install -r demo.txt“ installiert werden

##Virtual Environments
Problemstellung: Jedes Python Projekt speichert die verwendeten Packages im gleichen Directory und greift bei Bedarf auf dieses zu. Brauchen zwei verschiedene Projekte unterschiedliche Versionen eines Packages kommt es zu Komplikationen.
Eine Virtuelle Umgebung schafft für jedes Projekt eine isolierte Umgebung, in der jedes Projekt einen eigenen unabhängigen Bereich hat.

##venv :
-	in der Standardbibliothek ab Python 3 integriert 	
- 	bietet Unterstützung zum Erstellen von Virtuellen Umgebungen mit eigenen Nebenverzeichnissen an. 
	Optional auch mit Isolation von den Nebenverzeichnissen des Systems
- 	jede Umgebung erhält eine eigene Verbindung zur verwendeten Python-Version
- 	jede Umgebung kann eigene Packages verwenden
-	für Python 2.7 oder älter muss auf das Tool "virtualenv" zurückgegriffen werden

venv Erklärung : 
https://docs.python.org/3/tutorial/venv.html
https://www.youtube.com/watch?v=Kg1Yvry_Ydk

##pipenv :

- 	Erstellt eine Request Library in der alle verwendeten Packages gespeichert werden 	   
	und vermerkt in einer Pipfile im Projektordner die verwendeten Packages 
		   
https://docs.python-guide.org/dev/virtualenvs/

##virtualenvwrapper :

-	organisiert alle erstellten virtuellen Umgebungen an einem Ort
-	bietet Methoden an für die erstellen, löschen oder kopieren von Umgebungen
-	mit nur einem Befehl kann zwischen den Umgebungen gewechselt werden
			
https://realpython.com/python-virtual-environments-a-primer/

##Poetry :

- 	wird nicht von Python selber installiert, sondern fungiert als eigenständige 
	Applikation -> fördert die Isolierung der einzelnen Projekte
- 	Ein Tool um alle Packaging Aufgaben zu bewältigen, kann mehrere Python Versionen behandeln, 
	Packages erstellen, Abhängigkeiten verwalten, veröffentlichen von Projekten
	
######Vortrag über die Idee, Gebrauch, Vor- und Nachteile von Poetry:
https://www.youtube.com/watch?v=Au2t6VfY2_M
######Homepage Poetry:
https://python-poetry.org


