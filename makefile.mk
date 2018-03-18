LANG=C

all:
	cd build && make

clean:
	cd build && make clean

mkbuild:
	mkdir -p build
	cd build && cmake -G "Unix Makefiles" ..

rmbuild:
	rm -rf build

format:
	clang-format -i *.cpp

