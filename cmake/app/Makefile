LANG=C

BUILD_SYS=$(MY_BUILD_SYS)
BUILD_CONFIG=$(MY_BUILD_CONFIG)
BUILD_DIR=$(MY_BUILD_DIR)

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
	mycmake-build.sh

.PHONY: clean
clean:
	mycmake-build.sh --target clean

.PHONY: install
install:
	mycmake-build.sh --target install

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
	@echo "MY_BUILD_SYS    : $(MY_BUILD_SYS)"
	@echo "MY_BUILD_CONFIG : $(MY_BUILD_CONFIG)"
	@echo "MY_BUILD_DIR    : $(MY_BUILD_DIR)"
	@echo "PATH            : $(PATH)"
	@echo "which python    : $(shell which python)"

