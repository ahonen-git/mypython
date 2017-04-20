import netCDF4
import mypython

class pop_grid:
  '''POP grid class'''

  def __init__(self):
    self.name=''

  def set_grid(self):
    src_nc00=netCDF4.Dataset('/Users/misumi/pop_data/gx1v6.nc','r')
    src_nc01=netCDF4.Dataset('/Users/misumi/pop_data/gx1v6.concat.nc','r')
    self.tlon=src_nc00.variables['TLONG'][:]
    self.tlat=src_nc00.variables['TLAT'][:]
    self.tarea=src_nc00.variables['TAREA'][:]
    self.z_t=src_nc00.variables['z_t'][:]
    self.z_t_150m=src_nc00.variables['z_t_150m'][:]
    self.dz=src_nc00.variables['dz'][:]
    self.region_mask=src_nc00.variables['REGION_MASK'][:]
    self.tlon_conc=src_nc01.variables['tlon'][:]
    self.tlat_conc=src_nc01.variables['tlat'][:]
    self.vlon_conc=src_nc01.variables['vlon'][:]
    self.vlat_conc=src_nc01.variables['vlat'][:]
    src_nc00.close()
    src_nc01.close()
