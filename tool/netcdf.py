import netCDF4

#-- file name --
def inq_file(fname):
  src_nc00=netCDF4.Dataset(fname,'r')
  for v in src_nc00.variables.keys():
    print v,src_nc00.variables[v][:].shape
  src_nc00.close()

def dim_get(fname):
  src_nc00=netCDF4.Dataset(fname,'r')
  dims={}
  for d in src_nc00.dimensions.keys():
    x=src_nc00.dimensions.get(d)
    dims.update({x.name:x.size})
  return dims 

def nc_write(fname,vars,dtype='f4',fv=1.e37,units='n/a',nbname='test',wrkdir='test'):
    fo=netCDF4.Dataset(fname,'w')
    fo.nbname=nbname
    fo.wrkdir=wrkdir
    
    for n,d in zip(range(vars[vars.keys()[0]].ndim),vars[vars.keys()[0]].shape):
        fo.createDimension('dim'+str(n),d)
    for v in sorted(vars.keys()):
        vo=fo.createVariable(v,dtype,['dim'+str(n) for n in range(vars[vars.keys()[0]].ndim)],fill_value=fv)
        vo[:]=vars[v][:]
        vo.units=units
    fo.close()
