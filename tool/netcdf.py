import netCDF4
import os

#-- file name --
def inq_file(fname):
  src_nc00=netCDF4.Dataset(fname,'r')
  for v in src_nc00.variables.keys():
    print(v,src_nc00.variables[v][:].shape)
  src_nc00.close()

def dim_get(fname):
  src_nc00=netCDF4.Dataset(fname,'r')
  dims={}
  for d in src_nc00.dimensions.keys():
    x=src_nc00.dimensions.get(d)
    dims.update({x.name:x.size})
  return dims 

def nc_write(fname,vars,dtype='f4',fv=1.e37,udic='n/a',nbname='test',wrkdir='test'):
    if os.path.exists(fname):
        os.remove(fname)
    fo=netCDF4.Dataset(fname,'w')
    fo.nbname=nbname
    fo.wrkdir=wrkdir

    dcnt=0
    for vname in vars.keys():
        dlist=[]
        for n in range(vars[vname].ndim):
            fo.createDimension("dim{0}".format(dcnt),vars[vname].shape[n])
            dlist.append("dim{0}".format(dcnt))
            dcnt+=1

        vo=fo.createVariable(vname,vars[vname].dtype,dlist,fill_value=fv)
        vo[:]=vars[vname][:]
        try:
            vo.units=udic[vname]
        except:
            pass

    fo.close()
