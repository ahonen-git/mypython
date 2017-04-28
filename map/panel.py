import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import numpy.ma as ma

def cyl(var,lon,lat,nrow=1,ncol=1,sel=[0],size=[15,15],mn=-999.,mx=-999.):
  """function to convert octime (in list) to datetime object"""
  fig0 = plt.figure(figsize=(size))

  lon_mn = np.min(lon)
  lon_mx = np.max(lon)
  lat_mn = np.min(lat)
  lat_mx = np.max(lat)

  if mn == -999.:
    mn=ma.min(var)
  if mx == -999.:
    mx=ma.max(var)

  nnum=nrow*ncol
  for n in range(nnum):
    ax0 = fig0.add_subplot(nrow,ncol,n+1)
    m0 = Basemap(projection='cyl',llcrnrlat=lat_mn,urcrnrlat=lat_mx,llcrnrlon=lon_mn,urcrnrlon=lon_mx,resolution='l')
    x,y = m0(lon,lat)
    if var.ndim > 2:
      im0 = m0.pcolormesh(x,y,var[sel[n],:,:],vmin=mn,vmax=mx)
    else:
      im0 = m0.pcolormesh(x,y,var[:,:],vmin=mn,vmax=mx)
    m0.drawcoastlines()
    cb0 = m0.colorbar(im0)

  plt.tight_layout()
