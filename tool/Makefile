FC=f2py
ffiles=$(wildcard *.f)
sfiles=$(ffiles:.f=.so)

all: $(sfiles)

clean:
	rm -rf *~ *.so
	ln -s calc_iso_surf.cpython-36m-x86_64-linux-gnu.so calc_iso_surf.so

.SUFFIXES: .f .so 
.f.so:
	$(FC) -c $< -m calc_iso_surf
