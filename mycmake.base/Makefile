build:
	mycmake.sh --build

cmake:
	mycmake.sh

run:
	./build.$(MY_BUILD_SYS)/$(MY_BUILD_CONFIG)/app.exe

clean:
	rm -rf build.$(MY_BUILD_SYS)

all: cmake build

