#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image, ImageDraw


def create_image_one():
    fname = "local/image_one.png"
    size = (200, 200)
    color = (0, 255, 0)

    img = Image.new("RGB", size, color)
    img.save(fname)


def create_image_four():
    fname = "local/image_four.png"
    size = (200, 200)
    w, h = size
    w2 = w / 2
    h2 = h / 2

    img = Image.new("RGB", size, (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0  , 0  , w2-1 , h2-1) , fill=(0   , 0   , 0))
    draw.rectangle((w2 , 0  , w-1  , h2-1) , fill=(255 , 0   , 0))
    draw.rectangle((0  , h2 , w2-1 , h-1)  , fill=(0   , 255 , 0))
    draw.rectangle((w2 , h2 , w-1  , h-1)  , fill=(0   , 0   , 255))
    img.save(fname)


def main(argv):
    create_image_one()
    create_image_four()


if __name__ == "__main__":
    main(sys.argv)
