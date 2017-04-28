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
