CONTAINER = docker run --rm -it -v ${CURDIR}:/workspace -w /workspace malmaud/julia:cxx
run_test: libArrayMaker.so
	${CONTAINER} julia testing.jl

run_it: libArrayMaker.so
	${CONTAINER}

libArrayMaker.so:
	${CONTAINER} g++ -shared -fPIC ArrayMaker.cpp -o libArrayMaker.so
