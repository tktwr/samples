#!/bin/bash

image-create.py -o _output/out_3_uint8.png -s 300 200 -c 3 -t uint8 --bgr 1 0 0
image-create.py -o _output/out_1_uint8.png -s 300 200 -c 1 -t uint8 --bgr 1

image-create.py -o _output/out_3_uint16.png -s 300 200 -c 3 -t uint16 --bgr 1 0 0
image-create.py -o _output/out_1_uint16.png -s 300 200 -c 1 -t uint16 --bgr 1

image-create.py -o _output/out_3_float32.exr -s 300 200 -c 3 -t float32 --bgr 1 0 0
image-create.py -o _output/out_1_float32.exr -s 300 200 -c 1 -t float32 --bgr 1

