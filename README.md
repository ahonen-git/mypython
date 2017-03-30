# mypython
This is a python toolbox written by myself.

## How to use and develop
### In mypython
```python:hoge.txt
[ mypython/tool/anim.py ]
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
import mypython
octime=mypython.misc.oct2date(oct)
```
### To refer help
```
[ hoge.py ]
import mypython
help(mypython.misc.oct2date)
```
return is something like
```
Help on function oct2date in module mypython.tool.misc:

oct2date(oct, t0=datetime.date(1, 1, 1))
    function to convert octime (in list) to datetime object
```
