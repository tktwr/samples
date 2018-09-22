LANG=C

.PHONY: build build.vs2017

all:
	cd build && cmake --build . --config release

build:
	mkdir -p build
	cd build && cmake -G "Unix Makefiles" ..

build.vs2017:
	mkdir -p build.vs2017
	cd build.vs2017 && cmake -G "Visual Studio 15 2017" ..

install:
	cd build && cmake --build . --target install

clean:
	cd build && cmake --build . --target clean

cleanall:
	rm -rf build lib

format:
	clang-format -i *.cpp

help:
	@echo "make all"
	@echo "make build"
	@echo "make build.vs2017"
	@echo "make install"
	@echo "make clean"
	@echo "make cleanall"
	@echo "make format"
