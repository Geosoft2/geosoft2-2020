Ich habe wirklich Probleme gute Quellen zu finden, es scheint als ob jede Quelle, die halbwegs zu passen scheint von anderen Standards/Frameworks/Mathematischen Modellen spricht oder einfach Jahrzehnte alt ist… (Oder man muss für Wissenschaftliche Paper Geld bezahlen)

Es wäre sehr hilfreich ein paar Quellen zu bekommen, auf die ich mich bedenkenlos beziehen kann und die die Standarts und Inhalte umreißt, die beleuchtet werden sollen.

So weit bin ich auf einer allgemeinen Ebene gekommen (mit veralteten und schlechten Quellen):

**Wann, Warum, Wie**

Wann: Stapelverarbeitung bei großen Problemen, Heutzutage alltäglich (Prozessoren,HPC,Cloud computing)

Warum: Schnellere Bearbeitung, skalierbare Rechenleistung

Wie: Aufteilung eines Problems in verschiedene Teilaufgaben

![](RackMultipart20201102-4-1bw009h_html_9355693fbef3ced4.png)

Bild 1: [https://assets-global.website-files.com/5debb9b4f88fbc3f702d579e/5e8e265f5b27697d5ce9bf87\_parallel-computing-diagram.png](https://assets-global.website-files.com/5debb9b4f88fbc3f702d579e/5e8e265f5b27697d5ce9bf87_parallel-computing-diagram.png)

Parallele Programmierung hängt von paralleler Hardware ab

**Wie weit soll hier auf die Hardware eingegangen werden ?**

Parallele Programmierung braucht parallele Software

Threads

Verwenden von parallel arbeitenden Algorithmen

[https://www.sintef.no/globalassets/upload/ikt/9011/simoslo/evita/2008/cai.pdf](https://www.sintef.no/globalassets/upload/ikt/9011/simoslo/evita/2008/cai.pdf)

**Standards**

OpenMP

      Shared-Memory

      Schleifen werden auf unterschiedliche Prozesse aufgeteilt

MPI (Message Passing Interface)

      Unabhänige Prozesse kommunizieren miteinander

      Implementierungen:

      MPICH

      MVAPICH

      Boost

      TPO++

PVM (parallel virtual machine)

      Bündelung von Computern gleicher Hardware zu einer Ressource

      Kommunikation via Netzwerk

[http://www.shodor.org/refdesk/Resources/Tutorials/ParProgProtocols/](http://www.shodor.org/refdesk/Resources/Tutorials/ParProgProtocols/)

[https://de.wikipedia.org/wiki/OpenMP](https://de.wikipedia.org/wiki/OpenMP)

[https://de.wikipedia.org/wiki/Message\_Passing\_Interface](https://de.wikipedia.org/wiki/Message_Passing_Interface)

[https://de.wikipedia.org/wiki/Parallele\_Virtuelle\_Maschine](https://de.wikipedia.org/wiki/Parallele_Virtuelle_Maschine)

[https://en.wikipedia.org/wiki/Parallel\_Virtual\_Machine](https://en.wikipedia.org/wiki/Parallel_Virtual_Machine)

**Prozessierung von EarthData**

?

Gerade hier brauche ich wirklich Hilfe. Ich habe keine Ahnung was ich hier erzählen soll. Mögliche, aber immer knapp nicht passende Quellen:

[https://ui.adsabs.harvard.edu/abs/2016AGUFMIN11E..06L/abstract](https://ui.adsabs.harvard.edu/abs/2016AGUFMIN11E..06L/abstract)

[https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNwBBqdj/pdf](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNwBBqdj/pdf)

[https://stories.dask.org/en/latest/pangeo.html](https://stories.dask.org/en/latest/pangeo.html)

https://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=&amp;ved=2ahUKEwi\_zIivt-LsAhX7IMUKHXUqCI4QFjAEegQIBxAC&amp;url=https%3A%2F%2Fwww.mdpi.com%2F2072-4292%2F12%2F1%2F62%2Fpdf&amp;usg=AOvVaw2h7\_u3dgny0xgiTNvMq02t

Kostenpflichtige Quellen:

[https://link.springer.com/chapter/10.1007/978-3-642-03214-1\_2](https://link.springer.com/chapter/10.1007/978-3-642-03214-1_2)

https://books.google.de/books?hl=de&amp;lr=&amp;id=GufgfWSHt28C&amp;oi=fnd&amp;pg=PR7&amp;dq=Parallel+Programming+Protocols+earth+data&amp;ots=6nPr-8sNrc&amp;sig=FIb51CqEgtmXHNKaWuFNEChkba8#v=onepage&amp;q&amp;f=false

[https://ieeexplore.ieee.org/document/7968632](https://ieeexplore.ieee.org/document/7968632)

[https://www.researchgate.net/publication/221013365\_Parallel\_Distributed\_Application\_Framework\_for\_Earth\_Science\_Data\_Processing](https://www.researchgate.net/publication/221013365_Parallel_Distributed_Application_Framework_for_Earth_Science_Data_Processing)

https://ieeexplore.ieee.org/abstract/document/7740234

**Dask**

Python(NumPy und Pandas)

Open-Source Library

Rechenaufgaben auf verschiedene PCs (Worker) aufteilen und parallel abarbeiten

Alternative: Apache Spark (SQL)

Anwendungen:

- High Performance Computing

- Maschinelles Lernen und Künstliche Intelligenz

- Modellberechnungen

**Exemplarisch, wie geht DASK:**

*Zur Installation*: pip install dask[complete]

*Task Scheduler/Worker zusweisung:*

*Auf Scheduler Maschine(aus den Informationen Adresse kopieren):* Dask-scheduler

Auf (allen) Worker Maschienen: dask-worker [TCP von Dask-scheduler Maschine, z.B. tcp://192.168.178.23:8786]

*Import von Daten:*

import dask.dataframe as dd

df = dd.read\_csv(...)

from dask.distributed import Client

client = Client(tcp://192.168.178.23:8786)

df.x.sum().compute()

*ODER*

*Mit Anlegen von Testdaten:*

Import dask.array as da

x= da.random.random((5000,5000) chunks=(1000,1000))

y=da.exp(x).sum()

from dask.distributed import Client

client = Client(tcp://192.168.178.23:8786)

y.compute()

https://docs.dask.org/en/latest/\_downloads/283ae48258d4a12e74080caf194279cb/daskcheatsheet.pdf
