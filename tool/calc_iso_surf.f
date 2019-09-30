      subroutine iso_surf(var2d,var3d,iso3d,isoval,
     &                    miss,thres,nz,ny,nx)
      implicit none
c
      integer                    :: nz,ny,nx
      real*8,dimension(nz,ny,nx) :: var3d,iso3d
      real*8,dimension(ny,nx)    :: var2d
      real*8                     :: isoval,thres,miss
      integer                    :: k,j,i

Cf2py intent(out) var2d
Cf2py intent(in)  var3d,iso3d,isoval,thres,miss,nz,ny,nx

      do j=1,ny
        do i=1,nx
          var2d(j,i)=miss
          do k=1,nz-1
            if (abs(iso3d(k,j,i)).gt.abs(thres)
     &       .or. abs(iso3d(k+1,j,i)).gt.abs(thres))cycle
            if (abs(var3d(k,j,i)).gt.abs(thres)
     &       .or. abs(var3d(k+1,j,i)).gt.abs(thres))cycle
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
