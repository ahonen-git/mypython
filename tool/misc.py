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

def z3d_cal(grd,zeta=0.0,Cpos='rho'):

  if Cpos=='rho':
    Cs=grd.vgrid.Cs_r
    s =grd.vgrid.s_rho
  elif Cpos=='w':
    Cs=grd.vgrid.Cs_w
    s =grd.vgrid.s_w

  h    =grd.vgrid.z_r.h
  hc   =grd.vgrid.z_r.hc

  ns=len(s)
  ny,nx,=h.shape
    
  s_3d=np.zeros((ns,ny,nx))
  s_3d=s_3d.swapaxes(0,2)+s
  s_3d=s_3d.swapaxes(0,2)

  Cs_3d=np.zeros((ns,ny,nx))
  Cs_3d=Cs_3d.swapaxes(0,2)+Cs
  Cs_3d=Cs_3d.swapaxes(0,2)
  
  s=(hc*s_3d+h*Cs_3d)/(hc+h)
    
  z3d=zeta+(zeta+h)*s
  return z3d
