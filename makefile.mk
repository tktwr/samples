LANG=C
CONFIG=Release
#CONFIG=Debug

.PHONY: build tags

all: all.unix

all.unix: cmake.unix build

all.vs2017: cmake.vs2017 build

cmake.unix:
	mkdir -p build
	cd build && winpty cmake -G "Unix Makefiles" ..

cmake.vs2017:
	mkdir -p build
	cd build && winpty cmake -G "Visual Studio 15 2017 Win64" ..

build:
	cd build && winpty cmake --build . --config $(CONFIG)

install:
	cd build && winpty cmake --build . --config $(CONFIG) --target install

clean:
	cd build && winpty cmake --build . --config $(CONFIG) --target clean

cleanall:
	rm -rf build

cleanout:
	rm -f _*.png

tags:
	ctags -R .

format:
	clang-format -i *.cpp

help:
	@echo "make all"
	@echo "make all.unix"
	@echo "make all.vs2017"
	@echo "make cmake.unix"
	@echo "make cmake.vs2017"
	@echo "make build"
	@echo "make install"
	@echo "make clean"
	@echo "make cleanall"
	@echo "make tags"
	@echo "make format"

