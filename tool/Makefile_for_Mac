FC=f2py_mac
ffiles=$(wildcard *.f)
sfiles=$(ffiles:.f=.so)

all: $(sfiles)
	rm -rf *.dSYM
	ln -s calc_iso_surf.cpython-36m-darwin.so calc_iso_surf.so
clean:
	rm -rf *~ *.so

.SUFFIXES: .f .so 
.f.so:
	$(FC) $<
