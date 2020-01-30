all: all.cmake all.build

all.cmake:
	time mycmake.sh ninja Release
	time mycmake.sh ninja Debug
	time mycmake.sh vs2019

all.build:
	time mycmake.sh --build ninja Release
	time mycmake.sh --build ninja Debug
	time mycmake.sh --build vs2019 Release
	time mycmake.sh --build vs2019 Debug
	time mycmake.sh --build vs2019 RelWithDebInfo
	time mycmake-android.sh

all.clean:
	rm -rf build.ninja
	rm -rf build.vs2019
	rm -rf build.android

