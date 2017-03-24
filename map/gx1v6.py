import os
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import netCDF4

def plot2d(var,vmin=0.0,vmax=1.0,lon_mn=0.0,lon_mx=360.0,lat_mn=-90.0,lat_mx=90.0):
  src_nc00=netCDF4.Dataset('/Users/misumi/pop_data/gx1v6.concat.nc','r')
  tlon=src_nc00.variables['tlon'][:]
  tlat=src_nc00.variables['tlat'][:]
  vlon=src_nc00.variables['vlon'][:]
  vlat=src_nc00.variables['vlat'][:]
  src_nc00.close()
  
  var2=ma.concatenate((var,var),axis=1)
  
  fig0 = plt.figure(figsize=(20,10))
  
  ax0 = fig0.add_subplot(111)
  m0 = Basemap(projection='cyl',llcrnrlat=lat_mn,urcrnrlat=lat_mx,llcrnrlon=lon_mn,urcrnrlon=lon_mx,resolution='l')
  x,y = m0(vlon,vlat)
  im0 = m0.pcolormesh(x,y,var2,vmin=vmin,vmax=vmax,cmap='viridis')
  m0.drawcoastlines()
  cb0 = m0.colorbar(im0)
  
  plt.tight_layout()
