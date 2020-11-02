# -*- coding: utf-8 -*-
"""
Created on Wed Oct. 28 11:14:09 2020

@author: Magdalena Fischer
@source http://xarray.pydata.org/en/stable/examples/multidimensional-coords.html

"""

#packages installed with anaconda 
#(conda install spyder, conda install -c conda-forge xarray,conda install numpy, conda install -c conda-forge matplotlib, conda install scipy )

import numpy as np
import xarray as xr
import requests
from matplotlib import pyplot as plt

url= 'https://github.com/pydata/xarray-data/raw/master/rasm.nc'
file=requests.get(url)
print('url loaded')
open('rasm.nc','wb').write(file.content)


ds=xr.open_dataset('rasm.nc').load()
print(ds)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(14,4))

#ds.Tair[0].plot(ax=ax1)

# define two-degree wide latitude bins
lat_bins = np.arange(0,91,2)
# define a label for each bin corresponding to the central latitude
lat_center = np.arange(1,90,2)
# group according to those bins and take the mean
Tair_lat_mean = ds.Tair.groupby_bins('xc', lat_bins, labels=lat_center).mean(dim=xr.ALL_DIMS)
# plot the result
Tair_lat_mean.plot()