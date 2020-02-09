BUILD_SYS=$(shell mycmake.sh --build-sys)
BUILD_CONFIG=$(shell mycmake.sh --build-config)
BUILD_DIR=$(shell mycmake.sh --build-dir)

#------------------------------------------------------
build:
	time mycmake.sh --build

cmake:
	time mycmake.sh

#------------------------------------------------------
android:
	time mycmake-android.sh

#------------------------------------------------------
run:
	cd $(BUILD_DIR) && $(BUILD_CONFIG)/app.exe

all: cmake build

#------------------------------------------------------
all.all:
	time mycmake.sh         ninja Release
	time mycmake.sh --build ninja Release
	time mycmake.sh         ninja Debug
	time mycmake.sh --build ninja Debug
	time mycmake.sh         vs2019
	time mycmake.sh --build vs2019 Release
	time mycmake.sh --build vs2019 Debug
	time mycmake.sh --build vs2019 RelWithDebInfo
	time mycmake-android.sh

all.clean:
	rm -rf build.ninja
	rm -rf build.vs2019
	rm -rf build.android

