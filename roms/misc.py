import sys
import numpy as np
import numpy.ma as ma
def zCal(grd,pos):
    gh=grd.hgrid
    gv=grd.vgrid
    ny,nx=gv.h.shape
    if   pos=='rho':
        ns=gv.N
        s=gv.s_rho
        c=gv.Cs_r
        m=gh.mask_rho
    elif pos=='w':
        ns=gv.N+1
        s=gv.s_w
        c=gv.Cs_w
        m=gh.mask_rho
    else:
        sys.exit()
    ary=np.zeros((ns,ny,nx))
    hc=ary+gv.hc
    s=ary.swapaxes(0,2)+s
    s=s.swapaxes(0,2)
    h=ary+gv.h
    c=ary.swapaxes(0,2)+c
    c=c.swapaxes(0,2)
    S=(hc*s+h*c)/(hc+h)
    z=S*h
    m=ary+m
    z=ma.masked_where(m==0,z)
    return z


def uv_shift(uvar,vvar):
    """
    u,v=uv_shift(u,v)
    lon_u,lat_v=uv_shift(lon_u,lat_v)
    """
    if uvar.ndim == vvar.ndim:
        d=uvar.ndim
        uvar=0.5*(uvar+np.roll(uvar,1,axis=d-1))
        vvar=0.5*(vvar+np.roll(vvar,1,axis=d-2))
        if   d==2:
            uvar=uvar[1:-1,1:]
            vvar=vvar[1:,1:-1]
        elif d==3:
            uvar=uvar[:,1:-1,1:]
            vvar=vvar[:,1:,1:-1]
        elif d==4:
            uvar=uvar[:,:,1:-1,1:]
            vvar=vvar[:,:,1:,1:-1]
        else:
            print 'Error ndim must be 2, 3 or 4.'
    else:
        print 'Error'
    return uvar,vvar
