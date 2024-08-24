#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pil_util as pu


fname = "_output/skin_albedo.png"
size = (256, 256)
color = [0.816, 0.604, 0.514]
pu.img_create_color(fname, size, "RGB", color)

fname = "_output/metalrough.png"
size = (256, 256)
color = [0.0, 1.0, 0.0, 1.0]
pu.img_create_color(fname, size, "RGBA", color)

fname = "_output/normal.png"
size = (256, 256)
nml = [0.0, 0.0, 1.0]
pu.img_create_nml(fname, size, nml)

colors = (
    (0   , 0   , 0),
    (255 , 0   , 0),
    (0   , 255 , 0),
    (0   , 0   , 255),
)
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])

fname = "_output/image_tile.png"
size = (200, 200)
pu.img_create_tile(fname, size, colors)

