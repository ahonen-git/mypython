import datetime
import numpy as np
def oct2date(oct,t0=datetime.date(1,1,1)):
  """function to convert octime (in list) to datetime object"""
  tlist=np.array(oct)/86400.0
  tt=[]
  for n in range(len(tlist)):
    tt.append(t0+datetime.timedelta(days=tlist[n]))
  return tt
