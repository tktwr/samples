#!/bin/bash

#======================================================
# variables
#======================================================

#======================================================
# functions
#======================================================
f_image_tile() {
  image-tile.py -o _output/tile_X.jpg      -nx 2 $MY_SAMPLES/data/sample*.jpg BLACK WHITE BLACK WHITE
  image-tile.py -o _output/tile_Y.jpg      -ny 2 $MY_SAMPLES/data/sample*.jpg BLACK WHITE BLACK WHITE --file-order Y
  image-tile.py -o _output/tile_Y2.jpg     -nx 2 $MY_SAMPLES/data/sample*.jpg BLACK WHITE BLACK WHITE --file-order Y
  image-tile.py -o _output/tile_FILE.jpg   -nx 2 $MY_SAMPLES/data/sample*.jpg --label-type FILE
  image-tile.py -o _output/tile_NUM.jpg    -nx 2 $MY_SAMPLES/data/sample*.jpg --label-type NUM
  image-tile.py -o _output/tile_ALPHA.jpg  -nx 2 $MY_SAMPLES/data/sample*.jpg --label-type ALPHA
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
