tags: tags.memo

.PHONY: tags.memo
tags.memo:
	memotags.sh cpp/*.cpp cpp_lib/*.cpp opencv/*.cpp py/*.py vim/*.vim sh/*.sh bat/*.bat > tags.memo

all:
	cd cpp && make all
	cd cpp_lib && make all
	cd mycmake.base && make all
	cd mycmake.test && make all

all.clean:
	cd cpp && make all.clean
	cd cpp_lib && make all.clean
	cd mycmake.base && make all.clean
	cd mycmake.test && make all.clean

