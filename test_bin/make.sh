#!/bin/bash

#======================================================
# variables
#======================================================
B_DIR=$(pwd)
O_DIR=$B_DIR/_output
I_DIR=$MY_SAMPLES/data/images

#======================================================
# functions
#======================================================
f_print_output() {
  echo "BASE_DIR   : $B_DIR"
  echo "OUTPUT_DIR : $O_DIR"
  echo "IMAGE_DIR  : $I_DIR"
}
_print_output() {
  echo "$1 [$(pwd)]"
}
_enter_output() {
  mkdir -p $O_DIR
  cd $O_DIR
  _print_output "Enter"
}
_leave_output() {
  cd $B_DIR
  _print_output "Leave"
}
#------------------------------------------------------
f_image_create_new() {
  image-create.py -a new -o $O_DIR/new01_u8_c1.png  -s 300 200 -ch 1 -ty uint8   -c0 1
  image-create.py -a new -o $O_DIR/new01_u8_c3.png  -s 300 200 -ch 3 -ty uint8   -c0 1 0 0
  image-create.py -a new -o $O_DIR/new01_u8_c4.png  -s 300 200 -ch 4 -ty uint8   -c0 1 0 0 1

  image-create.py -a new -o $O_DIR/new02_u16_c1.png -s 300 200 -ch 1 -ty uint16  -c0 1
  image-create.py -a new -o $O_DIR/new02_u16_c3.png -s 300 200 -ch 3 -ty uint16  -c0 1 0 0
  image-create.py -a new -o $O_DIR/new02_u16_c4.png -s 300 200 -ch 4 -ty uint16  -c0 1 0 0 1

  image-create.py -a new -o $O_DIR/new03_f32_c1.exr -s 300 200 -ch 1 -ty float32 -c0 1
  image-create.py -a new -o $O_DIR/new03_f32_c3.exr -s 300 200 -ch 3 -ty float32 -c0 1 0 0
  image-create.py -a new -o $O_DIR/new03_f32_c4.exr -s 300 200 -ch 4 -ty float32 -c0 1 0 0 1
}

f_image_create_grad() {
  image-create.py -a hgrad -o $O_DIR/grad01_u8_c3_hgrad.png  -s 300 200 -ch 3 -ty uint8   -c0 0 0 1 -c1 0 1 0
  image-create.py -a vgrad -o $O_DIR/grad02_u8_c3_vgrad.png  -s 300 200 -ch 3 -ty uint8   -c0 0 0 1 -c1 0 1 0
  image-create.py -a hgrad -o $O_DIR/grad03_f32_c3_hgrad.exr -s 300 200 -ch 3 -ty float32 -c0 0 0 1 -c1 0 1 0
  image-create.py -a vgrad -o $O_DIR/grad04_f32_c3_vgrad.exr -s 300 200 -ch 3 -ty float32 -c0 0 0 1 -c1 0 1 0
  image-create.py -a hgrad -o $O_DIR/grad05_f32_c1_hgrad.exr -s 300 200 -ch 1 -ty float32 -c0 0     -c1 1
  image-create.py -a vgrad -o $O_DIR/grad06_f32_c1_vgrad.exr -s 300 200 -ch 1 -ty float32 -c0 0     -c1 1
}

f_image_create_check() {
  image-create.py -a check     -o $O_DIR/check01_u8_c3_check_w256.png     -s 256 256 -ch 3 -ty uint8 -c0 0.5 0.5 0.5 -c1 1.0 1.0 1.0 -n 2 2
  image-create.py -a check     -o $O_DIR/check02_u8_c3_check_w512.png     -s 512 256 -ch 3 -ty uint8 -c0 0.5 0.5 0.5 -c1 1.0 1.0 1.0 -n 4 2
  image-create.py -a hstripe   -o $O_DIR/check03_u8_c3_hstripe_w256.png   -s 256 256 -ch 3 -ty uint8 -c0 0.5 0.5 0.5 -c1 1.0 1.0 1.0 -n 1 8
  image-create.py -a hstripe   -o $O_DIR/check04_u8_c3_hstripe_w512.png   -s 512 256 -ch 3 -ty uint8 -c0 0.5 0.5 0.5 -c1 1.0 1.0 1.0 -n 1 8
  image-create.py -a se_stripe -o $O_DIR/check05_u8_c3_se_stripe_w256.png -s 256 256 -ch 3 -ty uint8 -c0 0.5 0.5 0.5 -c1 1.0 1.0 1.0 -n 8 1
  image-create.py -a se_stripe -o $O_DIR/check06_u8_c3_se_stripe_w512.png -s 512 256 -ch 3 -ty uint8 -c0 0.5 0.5 0.5 -c1 1.0 1.0 1.0 -n 16 1
}

f_image_op() {
  _enter_output
  image-op.py --split grad01_u8_c3_hgrad.png
  image-op.py --merge -o merge.png grad01_u8_c3_hgrad_?.png
  image-op.py --diff -o diff.png grad01_u8_c3_hgrad.png grad01_u8_c3_hgrad.png
  image-op.py --diff -o diff2.png grad01_u8_c3_hgrad_0.png grad01_u8_c3_hgrad_1.png -sc 1
  _leave_output
}

f_image_tile() {
  _enter_output
  image-tile.py -nx 2 grad01_u8_c3_hgrad.png grad02_u8_c3_vgrad.png grad02_u8_c3_vgrad.png grad01_u8_c3_hgrad.png
  _leave_output
}
f_image_tile_samples() {
  image-tile.py -o $O_DIR/tile%02d_X.jpg      -nx 2 $I_DIR/sample*.jpg BLACK WHITE BLACK WHITE
  image-tile.py -o $O_DIR/tile%02d_Y.jpg      -ny 2 $I_DIR/sample*.jpg BLACK WHITE BLACK WHITE -O Y
  image-tile.py -o $O_DIR/tile%02d_Y2.jpg     -nx 2 $I_DIR/sample*.jpg BLACK WHITE BLACK WHITE -O Y
  image-tile.py -o $O_DIR/tile%02d_FILE.jpg   -nx 2 $I_DIR/sample*.jpg -L FILE
  image-tile.py -o $O_DIR/tile%02d_NUM.jpg    -nx 2 $I_DIR/sample*.jpg -L NUM
  image-tile.py -o $O_DIR/tile%02d_ALPHA.jpg  -nx 2 $I_DIR/sample*.jpg -L ALPHA -b 2 -t 'Left;Right'
}
f_image_conv() {
  _enter_output
  image-conv.py -T 200 $I_DIR/sample*.jpg
  _leave_output
}
#------------------------------------------------------
f_clean() {
  rm -rf $O_DIR
}
f_all() {
  f_image_create_new
  f_image_create_grad
  f_image_create_check
  f_image_op
  f_image_tile
  f_image_tile_samples
  f_image_conv
}
#======================================================
# main
#======================================================
f_fzf_default() { f_all; }
f_fzf_main "$@"
