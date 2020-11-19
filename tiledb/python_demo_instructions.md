## Instructions for the TiledDB python demo

#### I. Produce an array with TDB Geospatial

1. Download if you can [Docker](https://docs.docker.com/get-docker/)
2. Make a folder and download [this Geotiff](https://docs.docker.com/get-docker/) into it
3. Download TDB geospatial with the following command:
```
docker run -it --rm -u 0 -v /local/path:/data tiledb/tiledb-geospatial /bin/bash
```
Make sure to replace `/local/path` with the path to your folder with the image. If you want to learn more about how this works and Docker Volumes on Windows i can recommend this [tutorial](https://adamtheautomator.com/docker-volume-create/).

4. Now check with `gdalinfo --format TileDB` if the installation was successful.

5. Change into your mounted data folder (`cd`).

6. The following command will translate your Tiff into a TDB array with the uri **geodemo**:
```
gdal_translate -OF TileDB UTM2GTIF.TIF geodemo
```
7. Perform one last check to see if everything went smoothly. This command `gdallocationinfo UTM2GTIF.TIF 10 10` should have this output:
```
Report:
  Location: (10P,10L)
  Band 1:
    Value: 156
```
8. In your folder and should be a subfolder named **geodemo**

#### II. Open the array in the TDB python api

1. Get [Python](https://www.python.org/downloads/) and [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) if you haven't (In that order!)
2. Open the anaconda prompt
3. Make and activate a new environment like this:
```
conda create -n geosoft-ii
conda activate geosoft-ii
```
4. In this environment install [Jupyter](https://jupyter.org/) and [Pillow](https://python-pillow.org/):
```
conda install jupyter
conda install pillow
```
5. Now also install TileDB:
```
conda install -c conda-forge tiledb-py
```
6. Open Jupyter notebooks:
```
jupyter notebook
```
7. In Jupyter open `tiledb_python_demo.ipynb`
8. Change the path at `tiledb.open()` with your own path to *geodemo*
9. Run the cells and have fun :)
