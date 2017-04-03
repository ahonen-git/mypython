import netCDF4
import mypython
def set_dim():
  src_nc00=netCDF4.Dataset('/Users/misumi/pop_data/gx1v6.nc','r')
  dims=mypython.tool.netcdf.dim_get(src_nc00)
  ne=dims['z_t_150m']
  nz=dims['z_t']
  ny=dims['nlat']
  nx=dims['nlon']
  src_nc00.close()
  return ne, nz, ny, nx
