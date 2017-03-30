def dim_get(f):
  dims={}
  for d in f.dimensions.keys():
    x=f.dimensions.get(d)
    dims.update({x.name:x.size})
  return dims
