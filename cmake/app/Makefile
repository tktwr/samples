LANG=C

BUILD_SYS=$(shell mycmake.sh --build-sys)
BUILD_CONFIG=$(shell mycmake.sh --build-config)
BUILD_DIR=$(shell mycmake.sh --build-dir)

#------------------------------------------------------
.PHONY: default
default:
	test -d $(BUILD_DIR) || make cmake
	make build

#------------------------------------------------------
.PHONY: cmake
cmake:
	mycmake.sh

.PHONY: build
build:
	mycmake.sh --build

.PHONY: clean
clean:
	mycmake.sh --build $(BUILD_SYS) $(BUILD_CONFIG) --target clean

.PHONY: install
install:
	mycmake.sh --build $(BUILD_SYS) $(BUILD_CONFIG) --target install

#------------------------------------------------------
.PHONY: android
android:
	#mycmake-android.sh
	build_android.bat

#------------------------------------------------------
all: cmake build

run:
	cd $(BUILD_DIR) && $(BUILD_CONFIG)/app.exe

#------------------------------------------------------
all.all:
	mycmake.sh         make Release
	mycmake.sh --build make Release
	mycmake.sh         vs2019
	mycmake.sh --build vs2019 Release

all.clean:
	rm -rf build.make
	rm -rf build.vs2019
	rm -f version.h

all.run:
	cd build.make   && ./Release/app.exe
	cd build.vs2019 && ./Release/app.exe

#------------------------------------------------------
env:
	@echo "PATH: $(PATH)"
	@echo "which python: $(shell which python)"

