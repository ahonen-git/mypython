import datetime
import numpy as np
def oct2date(oct,t0=datetime.date(1,1,1)):
  """function to convert octime (in list) to datetime object"""
  tlist=np.array(oct)/86400.0
  tt=[]
  for n in range(len(tlist)):
    tt.append(t0+datetime.timedelta(days=tlist[n]))
  return tt

def arglatlon(latP,lonP,lat2d,lon2d):
  ny,nx=lat2d.shape
  lon0=np.zeros((ny,nx))+lonP
  lat0=np.zeros((ny,nx))+latP
  dlon=np.abs(lon2d-lon0)
  dlat=np.abs(lat2d-lat0)
  d=np.sqrt(dlon**2+dlat**2)
  ind1d=np.argmin(d)
  jind=ind1d/nx
  iind=ind1d%nx
  a=np.array([jind,iind])
  return a
