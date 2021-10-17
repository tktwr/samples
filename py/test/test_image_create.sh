#!/bin/bash

f_create_new() {
  image-create.py -o _output/new_4_uint8.png -s 300 200 -c 4 -t uint8 --bgr0 1 0 0 1
  image-create.py -o _output/new_3_uint8.png -s 300 200 -c 3 -t uint8 --bgr0 1 0 0
  image-create.py -o _output/new_1_uint8.png -s 300 200 -c 1 -t uint8 --bgr0 1

  image-create.py -o _output/new_4_uint16.png -s 300 200 -c 4 -t uint16 --bgr0 1 0 0 1
  image-create.py -o _output/new_3_uint16.png -s 300 200 -c 3 -t uint16 --bgr0 1 0 0
  image-create.py -o _output/new_1_uint16.png -s 300 200 -c 1 -t uint16 --bgr0 1

  # 4ch float32 exr is not supported
  #image-create.py -o _output/new_4_float32.exr -s 300 200 -c 4 -t float32 --bgr0 1 0 0 1
  image-create.py -o _output/new_3_float32.exr -s 300 200 -c 3 -t float32 --bgr0 1 0 0
  image-create.py -o _output/new_1_float32.exr -s 300 200 -c 1 -t float32 --bgr0 1
}

f_create_hgrad() {
  image-create.py -a hgrad -o _output/hgrad_3_uint8.png -s 300 200 -c 3 -t uint8 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o _output/vgrad_3_uint8.png -s 300 200 -c 3 -t uint8 --bgr0 0 0 1 --bgr1 0 1 0

  image-create.py -a hgrad -o _output/hgrad_3_float32.exr -s 300 200 -c 3 -t float32 --bgr0 0 0 1 --bgr1 0 1 0
  image-create.py -a vgrad -o _output/vgrad_3_float32.exr -s 300 200 -c 3 -t float32 --bgr0 0 0 1 --bgr1 0 1 0

  image-create.py -a hgrad -o _output/hgrad_1_float32.exr -s 300 200 -c 1 -t float32 --bgr0 0 --bgr1 1
  image-create.py -a vgrad -o _output/vgrad_1_float32.exr -s 300 200 -c 1 -t float32 --bgr0 0 --bgr1 1
}

f_create_new
f_create_hgrad

