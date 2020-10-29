@Svub1

Was sind Microservices?
-----------------------

-   stammt von SOA ab (Service-orientierte Architektur)
    -   entkoppelt Dienste und stellt sie zentral bereit
-   Popularität nimmt stark zu
-   dienen zur Modularisierung von Software
    -   Unterteilung in Kernfunktionen respektive Module
-   wird unabhängig von anderen Services ausgeführt
-   In der regel umgesetzt durch Docker Container
    -   Jeder Service bekommt eigenen Container
-   Oft als RESTful APIs Implementiert
-   Einzelne Komponenten können von Unabhängigen Teams Entwickelt werden

Quellen [Microservice - Architekcture: Mehr als die Summe ihrer
Teile?](https://www.ionos.de/digitalguide/websites/web-entwicklung/microservice-architecture-so-funktionieren-microservices/)

Vorteile einer Microservices – Architektur
------------------------------------------

-   Schnellere Markteinführung
    -   kürzere Entwicklungszeit
-   Hochgradig skalierbar
    -   Serverstruktur kann schnell an den Bedarf angepasst werden
-   Robustheit
    -   wenn ein Microservice ausfällt, stürzt nicht die gesamte
        Anwendung ab
-   Einfache Implementierung
    -   neue Entwicklungsansätze werden ermöglicht
-   Besserer Zugriff
    -   leichtere Entwicklung durch Aufteilung der Anwendung in viele
        Einzelteile
-   Mehr Offenheit
    -   Jedes Modul kann in einer anderen Sprache entwickelt werden
    -   Jedes Modul kann von einem Entwicklerteam unabhänig von einem
        anderen entwickelt werden

Quellen [Was sind
Microservices?](https://www.redhat.com/de/topics/microservices/what-are-microservices)

Nachteile einer Microservices – Architektur
-------------------------------------------

-   Softwareverteilung und das Testen ist aufweniger, da es eine
    Vilezahl von Services geben kann
-   Aufwand für die Aufteilung bestehender Programme in Microservices
    ist hoch
-   Höhere Wahrscheinlichkeit von ausfällen von mindestens einer
    Komponente, da es mehrere Systeme gibt
-   Verteilung der Architektur erzeugt zusätzliche Komplexität
    -   z.B Lastverteilung, Latenzen oder Fehlertoleranzen
-   Logging und Monitoring werden komplexer, da mehrere Systeme
    involviert sind

Quellen [Microservices - Verfahren, Vorteile und
Nachteile](https://docs.docker.com/compose/)

Microservices how
-----------------

-   Microservices sind untereineander isoliert und laufen in einer
    eigenen Umgebung
    -   Umsetzung in der Regel durch Container (Bspw. Docker)
    -   Alternativ durch Virtuelle Maschinen
-   Zusammensetzen mehrer einzelner Container/Anwendungen über Docker
    Compose
-   Die einzelnen Services kommunizieren nur über Schnittstellen

Docker Compose
--------------

-   ist ein Tool zum definieren und ausführen von Anwendungen die aus
    mehreren Docker Containern bestehen
-   Konfiguration in einem YAML File

Quellen [Overview of Docker Compose](https://docs.docker.com/compose/)

Docker Compose nutzen
---------------------

-   es werden 3 Schritte ausgeführt
    1.  definiert man sich eine Umgebung mit Hilfe eines Dockerfiles
    2.  definiert man sich die einzelnen Services in der docker –
        compose.yml, welche die spätere Anwendung darstellt
    3.  führe docker– compose up aus

Docker– compose.yml
-------------------

    version: "3.8"
    services:
      web:
        build: .
        ports:
          - "5000:5000"
        volumes:
          - .:/code
          - logvolume01:/var/log
        links:
          - redis
      redis:
        image: redis
    volumes:
      logvolume01: {}

Quellen [Overview of Docker Compose](https://docs.docker.com/compose/)

Docker – compose.yml aus Geosoft 1
----------------------------------

    version: "3"
    services:
     app:
       image: legen26/geosoftproject:latest
       ports:
         - "80:80" # forward webserver on standard-http port
       depends_on:
         - mongodbservice
     mongodbservice:
       image: mongo:latest # to be retrieved from dockerhub
       ports:
         - "27017:27017" # forward mongod port
       volumes:
         - /data/db
       environment:
         MONGO_INITDB_ROOT_USERNAME: root
         MONGO_INITDB_ROOT_PASSWORD: rootpassword

Docker – compose up
-------------------

-   der Befehl docker-compose up erstellt die Ausgabe jedes Containers
    -   wenn der Befehl beendet wird, werden alle Container gestoppt
-   der Parameter -d (detached) startet die Container im Hintergrund und
    führt diese aus

Quellen [docker-compose
up](https://docs.docker.com/compose/reference/up/)

Reverse-Proxy
-------------

-   ist eine zusätzliche Schutzmaßnahme die von einen oder mehrere
    Webserver geschaltet werden kann
-   die Adressumsetzung wir in der entgegengesetzten Richtung
    durchgeführt
-   Aufgabe des Reverse Proxies ist es Anfragen von Servern
    stellvertretend anzunehmen und an den entsprechenden Clitenten
    weiterzuleiten
-   er gewährt einem oder mehreren Clienten eines externen Netzes den
    Zugriff auf ein internes Netz

Quellen [Reverse-Proxy-Server-Kernkomponente in
Sicherheitsarchitekturen](https://www.ionos.de/digitalguide/server/knowhow/was-ist-ein-reverse-proxy/)

Anwendungsgebiete von Reverse Proxy
-----------------------------------

-   Anonymisierung
    -   da der Proxy-Server zwischen dem Backend – Server und dem Client
        Server steht bleibt der Backend – Server anonym
-   Schutz und Verschlüsselung
    -   bietet die Möglichkeit ein Kontrollsystem vor dem Backend zu
        integrieren
-   Load – Balancing
    -   das Reverse – Proxy vertetill die Anfragen gleichmäßig auf alle
        Server
-   Caching
    -   speichert häufig gefragte Daten zwischen um eine schnellere
        Zugriffszeit zu ermöglichen
-   Kompression
    -   ein und ausgehende Daten können komprimiert werden

CORS: Cross – origin Resource Sharing
-------------------------------------

-   Anfragen an einen Server sollen im Normalfalls auch nur von diesem
    beantwortet werden, CORS bildet eine Ausnahme
-   Wie funktioniert’s?
    -   der zweite Server muss dem ersten Server per HTTP – Header den
        Zugriff erlauben
    -   Im Kopf der HTTp – Antwort muss genau benannt werden welche
        Server die Daten nachladen und dem Nutzer verfügbar machen
        dürfen
    -   Wildcards möglich, diese ermöglichen einen universiellen Zugriff
-   Vorteile von CORS:
    -   bietet Anbindung eines weiteren Servers
-   Nachteile von CORS:
    -   wenn zu viele Wildcards benutzt werden, kann die Same – Origing
        – Policy ausserkraft gesetzt werden

Quellen
[CORS](https://www.ionos.de/digitalguide/websites/web-entwicklung/cross-origin-resource-sharing-erklaert/)

Quellen
-------

-   [Overview of Docker Compose](https://docs.docker.com/compose/)
-   [Microservice - Architekcture: Mehr als die Summe ihrer
    Teile?](https://www.ionos.de/digitalguide/websites/web-entwicklung/microservice-architecture-so-funktionieren-microservices/)
-   [MIcorservices, Docker und
    DevOps](https://www.dev-insider.de/microservices-docker-und-devops-a-642186/)
-   [Was sind
    Microservices?](https://www.redhat.com/de/topics/microservices/what-are-microservices)
-   [docker-library/mongo](https://github.com/docker-library/mongo/blob/00a8519463e776e797c227681a595986d8f9dbe1/3.0/Dockerfile)
-   [docker-compose up](https://docs.docker.com/compose/reference/up/)
-   [Reverse-Proxy-Server-Kernkomponente in
    Sicherheitsarchitekturen](https://www.ionos.de/digitalguide/server/knowhow/was-ist-ein-reverse-proxy/)
