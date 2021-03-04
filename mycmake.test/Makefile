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
	mycmake-android.sh

#------------------------------------------------------
all: cmake build

run:
	cd $(BUILD_DIR) && $(BUILD_CONFIG)/app.exe

#------------------------------------------------------
all.all:
	mycmake.sh         make Release
	mycmake.sh --build make Release
	mycmake.sh         make Debug
	mycmake.sh --build make Debug
	mycmake.sh         vs2019
	mycmake.sh --build vs2019 Release
	mycmake.sh --build vs2019 Debug
	mycmake.sh --build vs2019 RelWithDebInfo
	mycmake-android.sh

all.clean:
	rm -rf build.make
	rm -rf build.ninja
	rm -rf build.vs2019
	rm -rf build.android
	rm -f version.h

#------------------------------------------------------
env:
	@echo "PATH: $(PATH)"
	@echo "which python: $(shell which python)"

