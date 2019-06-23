all: all.cmake all.build

all.cmake:
	time mycmake.sh ninja Release
	time mycmake.sh ninja Debug
	time mycmake.sh make Release
	time mycmake.sh make Debug
	time mycmake.sh vs2017

all.build:
	time mycmake-build.sh ninja Release
	time mycmake-build.sh ninja Debug
	time mycmake-build.sh make Release
	time mycmake-build.sh make Debug
	time mycmake-build.sh vs2017 Release
	time mycmake-build.sh vs2017 Debug
	time mycmake-build.sh vs2017 RelWithDebInfo

all.clean:
	rm -rf build.ninja
	rm -rf build.make
	rm -rf build.vs2017

