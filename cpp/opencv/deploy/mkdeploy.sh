#!/bin/sh

cd ..

DATE=`LC_TIME=C date '+%Y%m%d'`
TIME=`LC_TIME=C date '+%H%M%S'`
BRANCH=`git rev-parse --abbrev-ref HEAD`
COMMIT=`git rev-parse --short HEAD`
DIR=opencv-$DATE-$TIME-$BRANCH-$COMMIT

echo $DIR
mkdir -p $DIR
cd $DIR

cp -a ../deploy/run.bat .
cp -a ../../data .
mkdir -p bin
cp -a ../build/display_image.exe bin
cd bin
cp-ldd-mingw64.sh display_image.exe

