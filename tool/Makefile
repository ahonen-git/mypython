FC=f2py_mac
ffiles=$(wildcard *.f)
sfiles=$(ffiles:.f=.so)

all: $(sfiles)
	rm -rf *.dSYM
clean:
	rm -rf *~ *.so

.SUFFIXES: .f .so 
.f.so:
	$(FC) $<
