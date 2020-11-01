# Handeling Data Cubes in Python
@ma9dalen8
* Data Cubes
* NumPy
* XArray
* Zarr
* netCDF4
* cf_xarray


## Data Cubes - mehrdimensionale Datenbanken

Data Cubes oder auch OLAP-Würfel (**O**n**l**ine **a**nalytical **p**rocessing) sind eine Methode um Daten multidimensional zu Speichern.
Dabei enthält jede Zelle Fakten, welche eindeutig durch die Relation meherer Dimensionen und deren Merkmale bestimmbar und abrufbar sind. Dies ermöglicht die Betrachtung der
Daten aus verschiedenen Perspektiven und in unterschiedlichen Detaillierungsgraden.  Die Datenstruktur erlaubt beliebig viele Dimensionen. Häufig wird ein konkreter Wert mit den dazugehörigen Koordinaten gespeichert (3D), aber auch die Zeitliche Komponente gewinnt immer mehr an bedeutung. [Quelle](https://www.datenbanken-verstehen.de/data-warehouse/olap-grundlagen/olap-cube/)

[Mehrdimensionaler Data Cube](https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f)

![Image of Data Cube System](https://miro.medium.com/max/875/1*oIyi7fqvyjIwEw49XkMFig.png)


## NumPy - Numerical Python
*„The fundamental package for scientific computing with Python”*
  
Numpy ist eine Python Bibliothek  zum Arbeiten mit Arrays, Funktionen der linearen Algebra und Matritzen. Sollen komplexere Statistische Analysen aufgestellt werden, geht dies meist über die Funktionen der numpy Bibliothek hinaus. Dann lässt sich die [SciPy-Bibliothek](https://www.scipy.org/scipylib/index.html) empfehlen. Auch ist das Plotten von Arrays mit numpy nicht möglich. Sollen die Ergebnisse oder Daten dargestellt werden, kann man die [matplotlib-Bibliothek](https://matplotlib.org/), welche mithilfe der [Cartopy-Bibliothek](https://scitools.org.uk/cartopy/docs/latest/) auch Kartenprojektionen erstellt oder für dynamische Plots die [Bokeh-Bibliothek](https://docs.bokeh.org/en/latest/) verwenden. Array-Objekte von Numpy sind eine schnellere Alternative als die von Python zur verfügunggestellte Listenstruktur. Durch Verwendung kontinuierlicher Speicherstellen ist eine effizientere und schnellere Verarbeitung möglich. 
  
#### Erstellen eines ndarrays
*class **numpy.ndarray** (shape, dtype=float, buffer=None, offset=0, strides=None, order=None)*
  
Ndarrays sind mehrdimensionale, homogene Datenstrukturen. Die Anzahl der Dimensionen und der Elemete wird durch den Parameter *shape*, 
welcher als positiver, ganzzahliger Tupel angegben wird, definiert. Der default-Wert der Array Elemnte ist float, kann aber über den Parameter
*dtype* geändert werden. Der Zugriff auf einezelne Informationen erfolgt über den Index. 
  
[NumPy Dokumentation](https://numpy.org/doc/stable/reference/arrays.ndarray.html)


## XArray

Die Python Bibliothek xarry verbindet die Vorteile von numpy und pandas (Tabellendatenstruktur mit Zugriff über Spalten und Zeilennamen). Xarry erleichert das Arbeiten mit mehrdimensionalen Arrays durch Einführung eines Lable-Systems. So können Beschriftungen in Form von Dimensionen, Koordinaten und Attributen hinzugefügt werden, wodurch das Arbeiten intuitiver und weniger fehleranfällig ist. Sowohl einzelne Arrays können so über Namen ausgewählt und kombiniert, aber auch Daten entlang einer Dimension über mehrere Arrays können so ausgewählt und kombiniert werden. Weiterhin lassen sich auch  netCDF-Ein-und Ausgaben damit realisieren, sowie das Plotten von den Daten.

 #### Erstellen eines xarrys
 *class **xarray.DataArray**(data=<NA>, coords=None, dims=None, name=None, attrs=None, indexes=None, fastpath=False)*
    
Die im Array repräsentierten Daten werden über den Parameter *data* übergeben. Diese sollten möglichst als ndarray oder "castable" zu einem vorliegen. Es kann aber auch ein Pandas oder ein selbstegeschriebenens Obejekt verwendet werden. Hierbei wird dann versucht, die zusätzlichen Informationen auf nicht ausgefüllte Argumente zu übertragen.
  
[XArray Dokumentation](http://xarray.pydata.org/en/stable/)


## Zarr

Die Python Bibliothek Zarr dient der Speicherung von Daten in komprimierten Abschnitten (chunks), in n-dimensionalen Arrays. Es wird das Erstellen von multidimensionalen Arrays mit beliebigen numpy-dtype ermöglicht. Dabei kann entlang jeder Dimension ein Chunk-Array erstellt werden. Diese können komprimiert und/oder gefiltert mit einem beliebigen NumCodecs-Codec weiterverwendet werden. Auch das Speichern auf der Festplatte, in Zip-Datein ... ist möglich. Zusätzlich ist das Organisieren über Gruppen und Hiearachien häufig nützlich. 

#### Erstellen eines zarr's
***zarr.creation.create** (shape, chunks=True, dtype=None, compressor='default', fill_value=0, order='C', store=None, synchronizer=None, overwrite=False, path=None , chunk_store=None, filters=None, cache_metadata=True , cache_attrs=True, read_only=False, object_codec=None)*

Hierbei wird bei der Erstellung über den Parameter *shape* die Größe des mehrdimensionalen Arrays festgelegt. Dieses kann zusätzlich mit dem Argument *chunks* unterteilt und strukturiert werden werden. Beide Parameter werden als Tupel von Int oder als einfache Int angegeben.

[Zarr Dokumentation](https://zarr.readthedocs.io/en/stable/)


## netCDF4 (Network Commen Data Form)

Hierbei handelt es sich um eine Softwarebibliothek, die maschienenunabhängige Datenformate für die gemeinsame Nutzung von Array-orientierten wissenschaftlichen Daten unterstüzt. Neben den Daten, können auch Informationen über diese dort gespeichert werden. Weiterhin ist es möglich auch nur mit kleinen Teilmengen des großen Datensets zu arbeiten und auch von Remote-Servern darauf zuzugreifen.
[netCDF4 Dokumentation](http://unidata.github.io/netcdf4-python/netCDF4/index.html)

#### Erstellen einer netCDF-File
***netCDF4.Dataset**('name.nc','w', format='NETCDF4')*

Um eine neue nc-File anzulegen, wird auf die Methode Dataset zugegriffen. Die Datei wird im aktuellen Ordner gespeichert. Das 'w' im Beispiel oben, steht dabei für den Schreibzugriff (write). Anschließend kann mit dem Befehl *.createGroup, .createDimension* und *.createVariable* die Struktur der Datei angelegt/spezifiziert werden.
[arbeiten mit netCDF-Files ](https://pyhogs.github.io/intro_netcdf4.html)


## cf_xarray

Die Python-Biebliothek cf_xarray dient der Interpretation von CF(Climate and Forcast)-Attributen, welche auf einem xarray-Objekt gespeichert sein können. Cf stellt ein paar Grundlegende Informationen zur Verfügung. *Title*: gibt Informationen darüber, was in der Datei gespeichert ist, *institution*: enthält Informationen daüber wo dieser hergestellt wurde, *source*: beschreibt wie es hergestellt (model version, instrument type etc.) wurde, *history*: Verlauf der ausgeführten Operationen, *references*: Verknüpfungen oder Web-Dokumentationen und in *comment* können unterschiedliche weitere Informationen enthalten sein. [cf-Conventions](https://cfconventions.org/Data/cf-documents/overview/viewgraphs.pdf)

Mithilfe von .cf.describe können die Variablen Namen ausgegeben werden. 

[cf-xarray Dokumentation](https://cf-xarray.readthedocs.io/en/latest/examples/introduction.html)
