      subroutine iso_surf(var2d,var3d,iso3d,isoval,miss,nz,ny,nx)
      implicit none
c
      integer                    :: nz,ny,nx
      real*8,dimension(nz,ny,nx) :: var3d,iso3d
      real*8,dimension(ny,nx)    :: var2d
      real*8                     :: isoval,miss
      integer                    :: k,j,i

Cf2py intent(out) var2d
Cf2py intent(in)  var3d,iso3d,isoval,miss,nz,ny,nx

      do j=1,ny
        do i=1,nx
          var2d(j,i)=miss
          do k=1,nz-1
            if (iso3d(k,j,i).eq.miss.or.iso3d(k+1,j,i).eq.miss)cycle
            if (var3d(k,j,i).eq.miss.or.var3d(k+1,j,i).eq.miss)cycle
            if (isoval.ge.iso3d(k,j,i)
     &          .and.isoval.lt.iso3d(k+1,j,i)) then
              var2d(j,i)=var3d(k,j,i)+
     &                  (var3d(k+1,j,i)-var3d(k,j,i))
     &                  /(iso3d(k+1,j,i)-iso3d(k,j,i))
     &                  *(isoval-iso3d(k,j,i))
            end if
          end do
        end do 
      end do
c
      return
      end
