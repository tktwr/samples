#!/bin/bash
# vim:nowrap

f_test_image_create_check() {
  image-create.py -a check     -o check_w256_c3_uint8.png     -s 256 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 2 2
  image-create.py -a check     -o check_w512_c3_uint8.png     -s 512 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 4 2
  image-create.py -a hstripe   -o hstripe_w256_c3_uint8.png   -s 256 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 1 8
  image-create.py -a hstripe   -o hstripe_w512_c3_uint8.png   -s 512 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 1 8
  image-create.py -a se_stripe -o se_stripe_w256_c3_uint8.png -s 256 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 8 1
  image-create.py -a se_stripe -o se_stripe_w512_c3_uint8.png -s 512 256 -c 3 -y uint8 --bgr0 0.5 0.5 0.5 --bgr1 1.0 1.0 1.0 -n 16 1
}

f_test_image_create_new() {
  image-create.py -a new -o new_4_uint8.png -s 300 200 -c 4 -y uint8 --bgr0 1 0 0 1
  image-create.py -a new -o new_3_uint8.png -s 300 200 -c 3 -y uint8 --bgr0 1 0 0
  image-create.py -a new -o new_1_uint8.png -s 300 200 -c 1 -y uint8 --bgr0 1

  image-create.py -a new -o new_4_uint16.png -s 300 200 -c 4 -y uint16 --bgr0 1 0 0 1
  image-create.py -a new -o new_3_uint16.png -s 300 200 -c 3 -y uint16 --bgr0 1 0 0
  image-create.py -a new -o new_1_uint16.png -s 300 200 -c 1 -y uint16 --bgr0 1

  # 4ch float32 exr is not supported
  #image-create.py -a new -o new_4_float32.exr -s 300 200 -c 4 -y float32 --bgr0 1 0 0 1
  image-create.py -a new -o new_3_float32.exr -s 300 200 -c 3 -y float32 --bgr0 1 0 0
  image-create.py -a new -o new_1_float32.exr -s 300 200 -c 1 -y float32 --bgr0 1
}

f_test_image_create_grad() {
  image-create.py -a hgrad -o hgrad_3_uint8.png -s 300 200 -c 3 -y uint8 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o vgrad_3_uint8.png -s 300 200 -c 3 -y uint8 --bgr0 0 0 1 --bgr1 0 1 0

  image-create.py -a hgrad -o hgrad_3_float32.exr -s 300 200 -c 3 -y float32 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o vgrad_3_float32.exr -s 300 200 -c 3 -y float32 --bgr0 0 0 1 --bgr1 0 1 0

  image-create.py -a hgrad -o hgrad_1_float32.exr -s 300 200 -c 1 -y float32 --bgr0 0 --bgr1 1
  image-create.py -a vgrad -o vgrad_1_float32.exr -s 300 200 -c 1 -y float32 --bgr0 0 --bgr1 1
}

f_test_image_split() {
  image-op.py --split hgrad_3_uint8.png
}

f_test_image_merge() {
  image-op.py --merge -o merge.png hgrad_3_uint8_0.png hgrad_3_uint8_1.png hgrad_3_uint8_2.png
}

f_test_image_tile() {
  image-tile.py -c 2 hgrad_3_uint8.png vgrad_3_uint8.png vgrad_3_uint8.png hgrad_3_uint8.png
}

f_test_image_conv() {
  image-conv.py -t 200 $MY_SAMPLES/data/sample*.jpg
}

f_test_image_create_check
f_test_image_create_new
f_test_image_create_grad
f_test_image_split
f_test_image_merge
f_test_image_tile
f_test_image_conv
