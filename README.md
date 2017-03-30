# mypython
This is a python toolbox written by myself.

## How to use and develop
### To develop
```
[ mypython/__init__.py ]
...
import tool
import map
...
```
```
[ mypython/tool/__init__.py]
import calc_iso_surf
import misc
```
```
[ mypython/tool/misc.py ]
import datetime
import numpy as np
def oct2date(oct,t0=datetime.date(1,1,1)):
  """function to convert octime (in list) to datetime object"""
  tlist=np.array(oct)/86400.0
  tt=[]
  for n in range(len(tlist)):
  tt.append(t0+datetime.timedelta(days=tlist[n]))
  return tt
```
### To use
```
[ hoge.py ]
import sys
sys.path.append('/Users/misumi')
import mypython
# use
octime=mypython.tool.misc.oct2date(oct)
# see help
help(mypython.tool.misc.oct2date)
```
