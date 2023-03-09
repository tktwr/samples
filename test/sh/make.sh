#!/bin/bash

#======================================================
# variables
#======================================================

#======================================================
# functions
#======================================================
f_image_tile() {
  image-tile.py -o _output/tile.jpg        -c 2 $MY_SAMPLES/data/sample*.jpg BLACK WHITE
  image-tile.py -o _output/tile_FILE.jpg   -c 2 $MY_SAMPLES/data/sample*.jpg -l FILE
  image-tile.py -o _output/tile_NUM.jpg    -c 2 $MY_SAMPLES/data/sample*.jpg -l NUM
  image-tile.py -o _output/tile_ALPHA.jpg  -c 2 $MY_SAMPLES/data/sample*.jpg -l ALPHA
}

f_test_image() {
  mkdir -p _output/image
  cd _output/image && ../../test_image.sh
}

#------------------------------------------------------
f_help() {
  echo "image_tile"
  echo "test_image"
  echo "help"
}

f_default() {
  f_help
}

#======================================================
# main
#======================================================
func_name=${1:-"default"}
shift
eval "f_$func_name $@"
