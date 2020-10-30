@jona159
# Testing
## Test Driven Development (TDD) 
* _Kennzeichnet sich dadurch, dass zuerst die Tests geschrieben werden und erst später die Implementierung der dazugehörigen Komponenten geschieht_
* _Es wird kein Produktivcode geschrieben, es sei denn es existiert bereits ein Test welcher dies vorsieht_
* _Zyklischer Ablauf:_
    1. _Test schreiben_
    1. _Test auf Fehler überprüfen_
    1. _Code implementieren, sodass Test erfolreich durchläuft_
    1. _Sicherstellen, dass alle Tests OK sind_
    1. _Test und Produktivcode werden refaktorisiert_
Quellen: 
 * [Youtube Vortrag](https://www.youtube.com/watch?v=IvqX-HTd8o0)
 * [Einführung in TDD](https://medium.com/hackernoon/introduction-to-test-driven-development-tdd-61a13bc92d92)
 * [TDD Vorteile](https://www.it-agile.de/wissen/agiles-engineering/testgetriebene-entwicklung-tdd/)
* __Vorteile von TDD:__
    * _gute Wartbarkeit und Qualität (kein ungetesteter Code, saubere Struktur, Minimierung der Redundanzen)_
    * _Erhöhte Effektivität und Effizienz bei der Codeerstellung (gewünschtes Ergebnis bei minimaler Anzahl an geschriebenen Zeilen)_
## Unit Tests vs Integration Tests
 * __Unit Tests__
   * _Einzelne Codeeinheit die getestet werden soll (z.B. Funktion)_
   * _Testen auf dem niedrigsten Level_
   * _Simpler, schneller Entwurf_
   * _Reduziert Bugs, schnelleres Debugging_
   * _Tests können auch zur Dokumentation dienen_
   * _stellt die korrekte Implementierung der vorher festgelegten Bedingungen sicher_
   * _Ursache der falschen Implementierung wird schnell ersichtlich_
   
 * __Integration Tests__
   * _Zusammenhängende Systemkomponenten werden auf erfolgreiches Zusammenwirken getestet_
   * _Dabei sollen Module dem gewünschten Interaktionsprotokoll folgen_
## pytest
* Framework zum einfachen Erstellen von skalierbaren Tests
 1. **Parallel Tests**
      * _Tests sollen gleichzeitig laufen, um Zeit bei der Ausführung zu gewinnen_
      * __xdist__ _plugin für pytest installieren_
         * _Installation über:_
            ```
            pip install pytest-xdist
            ```
      * _Ausführen der Tests mit:_
          ```
          pytest -n auto
          ```
          _oder_
          ```
          pytest -n 2
          ``` 
          
      
 1. **Test Suites**

 1. **Most Important CLI Instructions**
    * pytest --version
    * pytest --fixtures
    * pytest --help
    * pytest -x
    * pytest --maxfail=2
    * pytest 
 1. **writing assertions**

 1. **paths/testdata/testfiles**
     * Ausführen aller Tests in files mit Namen ...test.py und test___.py über *pytest* im current directory und in Subordnern
     * Wenn man nicht im cd arbeiten möchte kann man ein directory mit *pytest* + *Pfad* angeben, z.B. : *pytest tests/../..*
     * Man kann auch mit einem Befehl mehrere directories/files angeben, z.B.: *pytest tests/../.. tests/test.py*
     * einzelne Tests innerhalb eines Files lassen sich mit *pytest* + *Test-File* + *Testfunktionsname* ausführen
     
 1. **temp dirs/files**

 1. **fixtures**
     * beschreibt die Umgebung in welcher der Test läuft, z.B. eine Datenbank
 1. **mocking/patching (engl. Mock=Attrape)**
     * _wird verwendet wenn sich Platzhalter statt der echten Objekte beim Testen besser eignen, zum Beispiel bei API-Abfragen, da man beim Testen nicht jedesmal wieder die API-
        Abfrage durchführen möchte weil diese das Testen stark verlangsamen würde_
     * weitere Anwendungsbereiche von mocking: 
        * _das zu testende Objekt liefert nicht-deterministische Ergebnisse, bspw: Uhrzeit_
        * _das echte Objekt existiert noch gar nicht_
        * _schwierig auslösbares Verhalten_
        (bei Integrationstest ist mocking normalerweise nicht notwendig)
     * die wichtigsten Mocking-Typen: 
       * _Dummy: Objekt, das weitergereicht, aber nicht benutzt wird_
       * _Fake: Objekt mit eingeschränkter Implementierung_
       * _Mock: Objekt das bei Funktionsaufrufen mit übergebenen Werten eine Rückgabe liefert (erfordert die Verwendung eines mocking-Frameworks)_
     * Pytest Mocking-Framework: __Pytest-Mock_
       Installation über: 
       ```
       pip install pytest-mock
       ```
 1. **test cache**
