build:
	mycmake.sh --build

#------------------------------------------------------
make:
	mycmake.sh         make Release
	mycmake.sh --build make Release
	mycmake.sh         make Debug
	mycmake.sh --build make Debug

ninja:
	mycmake.sh         ninja Release
	mycmake.sh --build ninja Release
	mycmake.sh         ninja Debug
	mycmake.sh --build ninja Debug

vs2019:
	mycmake.sh         vs2019
	mycmake.sh --build vs2019 Release
	mycmake.sh --build vs2019 Debug
	mycmake.sh --build vs2019 RelWithDebInfo

vs2022:
	mycmake.sh         vs2022
	mycmake.sh --build vs2022 Release
	mycmake.sh --build vs2022 Debug
	mycmake.sh --build vs2022 RelWithDebInfo

android:
	#mycmake-android.sh
	build_android.bat

#------------------------------------------------------
all: make ninja vs2019 android

clean:
	rm -rf build* compile_commands.json

