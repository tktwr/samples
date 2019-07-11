all: all.cmake all.build

all.cmake:
	time mycmake.sh ninja Release
	time mycmake.sh ninja Debug
	time mycmake.sh vs2019

all.build:
	time mycmake-build.sh ninja Release
	time mycmake-build.sh ninja Debug
	time mycmake-build.sh vs2019 Release
	time mycmake-build.sh vs2019 Debug
	time mycmake-build.sh vs2019 RelWithDebInfo

all.clean:
	rm -rf build.ninja
	rm -rf build.vs2019

