all: all_ninja all_vs2019

all.clean: clean_ninja clean_vs2019

#=================================================

all_ninja: cmake_ninja build_ninja

cmake_ninja:
	mycmake.sh ninja Release

build_ninja:
	mycmake-build.sh ninja Release

clean_ninja:
	rm -rf build.ninja version.h

run_ninja:
	./build.ninja/Release/app.exe

#=================================================

all_vs2019: cmake_vs2019 build_vs2019

cmake_vs2019:
	mycmake.sh vs2019 Release

build_vs2019:
	mycmake-build.sh vs2019 Release

clean_vs2019:
	rm -rf build.vs2019 version.h

run_vs2019:
	./build.vs2019/Release/app.exe

