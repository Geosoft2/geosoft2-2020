**Wann, Warum, Wie**

Wann: Stapelverarbeitung bei großen Problemen, Heutzutage alltäglich (Prozessoren,HPC,Cloud computing)

Warum: Schnellere Bearbeitung, skalierbare Rechenleistung

Wie: Aufteilung eines Problems in verschiedene Teilaufgaben



![Parralleles Arbeiten](https://assets-global.website-files.com/5debb9b4f88fbc3f702d579e/5e8e265f5b27697d5ce9bf87\_parallel-computing-diagram.png)

Bild 1: [https://assets-global.website-files.com/5debb9b4f88fbc3f702d579e/5e8e265f5b27697d5ce9bf87\_parallel-computing-diagram.png](https://assets-global.website-files.com/5debb9b4f88fbc3f702d579e/5e8e265f5b27697d5ce9bf87_parallel-computing-diagram.png)

- Parallele Programmierung hängt von paralleler Hardware ab

  - Speicher
  - Architektur
    - Multi-core
    - verteilte systeme (destributed computing)
    - cluster
    - viele weitere
  
- Parallele Programmierung braucht parallele Software

- Threads

- Verwenden von parallel arbeitenden Algorithmen

[https://www.sintef.no/globalassets/upload/ikt/9011/simoslo/evita/2008/cai.pdf](https://www.sintef.no/globalassets/upload/ikt/9011/simoslo/evita/2008/cai.pdf)

**Standards**

OpenMP

- Shared-Memory

- Schleifen werden auf unterschiedliche Prozesse aufgeteilt

MPI (Message Passing Interface)

- Unabhänige Prozesse kommunizieren miteinander

- Implementierungen:

- MPICH

- MVAPICH

- Boost

- TPO++

PVM (parallel virtual machine)
- Bündelung von Computern gleicher Hardware zu einer Ressource

- Kommunikation via Netzwerk

[http://www.shodor.org/refdesk/Resources/Tutorials/ParProgProtocols/](http://www.shodor.org/refdesk/Resources/Tutorials/ParProgProtocols/)

[https://de.wikipedia.org/wiki/OpenMP](https://de.wikipedia.org/wiki/OpenMP)

[https://de.wikipedia.org/wiki/Message\_Passing\_Interface](https://de.wikipedia.org/wiki/Message_Passing_Interface)

[https://de.wikipedia.org/wiki/Parallele\_Virtuelle\_Maschine](https://de.wikipedia.org/wiki/Parallele_Virtuelle_Maschine)

[https://en.wikipedia.org/wiki/Parallel\_Virtual\_Machine](https://en.wikipedia.org/wiki/Parallel_Virtual_Machine)

**Prozessierung von EarthData**

- EarthData = riesige multi-dimensionale numerische Array (zB Temperatur, lat, long, Höhendaten, Zeit, Kalkulationen, ...)
 
 - häufige Ziele:
   - einfache Statistken
   - Komponentenanalyse (räumliche und zeitliche Verfügbarkeit)
   - Vergleich von Daten mit verschiedenen räumlichen und zeitlichen Strukturen
   - Spektralanalyse über verschiedene räumliche und zeitliche Dimensionen
   - Budgetdiagnosen
   - machine learning

Hauptprobleme: 
-  Erhaltung der schnellen und interaktiven Analyse (auch bei extrem großen Datensätzen)
-  Parralles Prozessieren ohne Abhängigkeit von der Art der Berechnung
-  Für den Anwender keine Ausseinandersetzung mit den Details der Parrallellisierung

parallel computing engine which does not strongly constrain the type of computations
nor require the user to engage with the details of parallelization


Pangeo(coordinating and supporting the development of open source software for large geoanalysis) provides configurations for deploying Jupyter, Xarray and Dask
high-performance computing clusters and cloud platforms
interactively 
 

Quellen:

[https://stories.dask.org/en/latest/pangeo.html](https://stories.dask.org/en/latest/pangeo.html)


Kostenpflichtige oder weiterführende Quellen:

https://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=&amp;ved=2ahUKEwi\_zIivt-LsAhX7IMUKHXUqCI4QFjAEegQIBxAC&amp;url=https%3A%2F%2Fwww.mdpi.com%2F2072-4292%2F12%2F1%2F62%2Fpdf&amp;usg=AOvVaw2h7\_u3dgny0xgiTNvMq02t


[https://ui.adsabs.harvard.edu/abs/2016AGUFMIN11E..06L/abstract](https://ui.adsabs.harvard.edu/abs/2016AGUFMIN11E..06L/abstract)

[https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNwBBqdj/pdf](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNwBBqdj/pdf)

[https://link.springer.com/chapter/10.1007/978-3-642-03214-1\_2](https://link.springer.com/chapter/10.1007/978-3-642-03214-1_2)

https://books.google.de/books?hl=de&amp;lr=&amp;id=GufgfWSHt28C&amp;oi=fnd&amp;pg=PR7&amp;dq=Parallel+Programming+Protocols+earth+data&amp;ots=6nPr-8sNrc&amp;sig=FIb51CqEgtmXHNKaWuFNEChkba8#v=onepage&amp;q&amp;f=false

[https://ieeexplore.ieee.org/document/7968632](https://ieeexplore.ieee.org/document/7968632)

[https://www.researchgate.net/publication/221013365\_Parallel\_Distributed\_Application\_Framework\_for\_Earth\_Science\_Data\_Processing](https://www.researchgate.net/publication/221013365_Parallel_Distributed_Application_Framework_for_Earth_Science_Data_Processing)

https://ieeexplore.ieee.org/abstract/document/7740234

**Dask**

- Python(NumPy und Pandas)

- Open-Source Library

- Rechenaufgaben auf verschiedene PCs (Worker) aufteilen und parallel abarbeiten

- Alternative: Apache Spark (SQL)

- Technologie: Xarray, Zarr

- Anwendungen:

  - High Performance Computing

  - Maschinelles Lernen und Künstliche Intelligenz

  - Modellberechnungen

**Exemplarisch, wie geht DASK:**

*Zur Installation*: 
```powershell
pip install dask[complete]
```

*Task Scheduler/Worker zusweisung:*

*Auf Scheduler Maschine(aus den Informationen Adresse kopieren):*
```python 
Dask-scheduler
```

Auf (allen) Worker Maschienen:
```python 
dask-worker tcp://192.168.178.23:8786 ### [TCP von Dask-scheduler Maschine, z.B. tcp://192.168.178.23:8786]
```

*Import von Daten:*

```python
import dask.dataframe as dd

df = dd.read\_csv(...)

from dask.distributed import Client

client = Client(tcp://192.168.178.23:8786)

df.x.sum().compute()
```

*ODER*

*Mit Anlegen von Testdaten:*

```python
Import dask.array as da


x= da.random.random((5000,5000) chunks=(1000,1000))

y=da.exp(x).sum()

from dask.distributed import Client

client = Client(tcp://192.168.178.23:8786)

y.compute()
```

https://docs.dask.org/en/latest/\_downloads/283ae48258d4a12e74080caf194279cb/daskcheatsheet.pdf
