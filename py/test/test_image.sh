#!/bin/bash

f_test_image_create_new() {
  image-create.py -o new_4_uint8.png -s 300 200 -c 4 -t uint8 --bgr0 1 0 0 1
  image-create.py -o new_3_uint8.png -s 300 200 -c 3 -t uint8 --bgr0 1 0 0
  image-create.py -o new_1_uint8.png -s 300 200 -c 1 -t uint8 --bgr0 1

  image-create.py -o new_4_uint16.png -s 300 200 -c 4 -t uint16 --bgr0 1 0 0 1
  image-create.py -o new_3_uint16.png -s 300 200 -c 3 -t uint16 --bgr0 1 0 0
  image-create.py -o new_1_uint16.png -s 300 200 -c 1 -t uint16 --bgr0 1

  # 4ch float32 exr is not supported
  #image-create.py -o new_4_float32.exr -s 300 200 -c 4 -t float32 --bgr0 1 0 0 1
  image-create.py -o new_3_float32.exr -s 300 200 -c 3 -t float32 --bgr0 1 0 0
  image-create.py -o new_1_float32.exr -s 300 200 -c 1 -t float32 --bgr0 1
}

f_test_image_create_grad() {
  image-create.py -a hgrad -o hgrad_3_uint8.png -s 300 200 -c 3 -t uint8 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o vgrad_3_uint8.png -s 300 200 -c 3 -t uint8 --bgr0 0 0 1 --bgr1 0 1 0

  image-create.py -a hgrad -o hgrad_3_float32.exr -s 300 200 -c 3 -t float32 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o vgrad_3_float32.exr -s 300 200 -c 3 -t float32 --bgr0 0 0 1 --bgr1 0 1 0

  image-create.py -a hgrad -o hgrad_1_float32.exr -s 300 200 -c 1 -t float32 --bgr0 0 --bgr1 1
  image-create.py -a vgrad -o vgrad_1_float32.exr -s 300 200 -c 1 -t float32 --bgr0 0 --bgr1 1
}

f_test_image_split() {
  image-split.py hgrad_3_uint8.png
}

f_test_image_merge() {
  image-merge.py merge.png hgrad_3_uint8_0.png hgrad_3_uint8_1.png hgrad_3_uint8_2.png
}

f_test_image_tile() {
  image-tile.py -c 2 hgrad_3_uint8.png vgrad_3_uint8.png vgrad_3_uint8.png hgrad_3_uint8.png
}

f_test_image_create_new
f_test_image_create_grad
f_test_image_split
f_test_image_merge
f_test_image_tile

