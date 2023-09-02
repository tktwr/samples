#!/bin/bash
# vim:nowrap

f_test_image_create_check() {
  image-create.py -a check     -o check01_u8_c3_check_w256.png     -s 256 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 2 2
  image-create.py -a check     -o check02_u8_c3_check_w512.png     -s 512 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 4 2
  image-create.py -a hstripe   -o check03_u8_c3_hstripe_w256.png   -s 256 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 1 8
  image-create.py -a hstripe   -o check04_u8_c3_hstripe_w512.png   -s 512 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 1 8
  image-create.py -a se_stripe -o check05_u8_c3_se_stripe_w256.png -s 256 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 8 1
  image-create.py -a se_stripe -o check06_u8_c3_se_stripe_w512.png -s 512 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 16 1
}

f_test_image_create_new() {
  image-create.py -a new -o new01_u8_c1.png -s 300 200 -c 1 -y uint8 --bgr0 1
  image-create.py -a new -o new01_u8_c3.png -s 300 200 -c 3 -y uint8 --bgr0 1 0 0
  image-create.py -a new -o new01_u8_c4.png -s 300 200 -c 4 -y uint8 --bgr0 1 0 0 1

  image-create.py -a new -o new02_u16_c1.png -s 300 200 -c 1 -y uint16 --bgr0 1
  image-create.py -a new -o new02_u16_c3.png -s 300 200 -c 3 -y uint16 --bgr0 1 0 0
  image-create.py -a new -o new02_u16_c4.png -s 300 200 -c 4 -y uint16 --bgr0 1 0 0 1

  image-create.py -a new -o new03_f32_c1.exr -s 300 200 -c 1 -y float32 --bgr0 1
  image-create.py -a new -o new03_f32_c3.exr -s 300 200 -c 3 -y float32 --bgr0 1 0 0
  image-create.py -a new -o new03_f32_c4.exr -s 300 200 -c 4 -y float32 --bgr0 1 0 0 1
}

f_test_image_create_grad() {
  image-create.py -a hgrad -o grad01_u8_c3_hgrad.png  -s 300 200 -c 3 -y uint8 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o grad02_u8_c3_vgrad.png  -s 300 200 -c 3 -y uint8 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a hgrad -o grad03_f32_c3_hgrad.exr -s 300 200 -c 3 -y float32 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o grad04_f32_c3_vgrad.exr -s 300 200 -c 3 -y float32 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a hgrad -o grad05_f32_c1_hgrad.exr -s 300 200 -c 1 -y float32 --bgr0 0 --bgr1 1
  image-create.py -a vgrad -o grad06_f32_c1_vgrad.exr -s 300 200 -c 1 -y float32 --bgr0 0 --bgr1 1
}

f_test_image_split() {
  image-op.py --split grad01_u8_c3_hgrad.png
}

f_test_image_merge() {
  image-op.py --merge -o merge.png grad01_u8_c3_hgrad_?.png
}

f_test_image_diff() {
  image-op.py --diff -o diff.png grad01_u8_c3_hgrad.png grad01_u8_c3_hgrad.png
}

f_test_image_tile() {
  image-tile.py -nx 2 grad01_u8_c3_hgrad.png grad02_u8_c3_vgrad.png grad02_u8_c3_vgrad.png grad01_u8_c3_hgrad.png
}

f_test_image_conv() {
  image-conv.py -t 200 $MY_SAMPLES/data/sample*.jpg
}

f_test_image_create_check
f_test_image_create_new
f_test_image_create_grad
f_test_image_split
f_test_image_merge
f_test_image_diff
f_test_image_tile
f_test_image_conv
