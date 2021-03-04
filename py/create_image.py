#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image, ImageDraw


def create_image():
    img = Image.new("RGB", (200, 200), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((  0,   0,  99,  99), fill=(  0,   0,   0))
    draw.rectangle((100,   0, 199,  99), fill=(255,   0,   0))
    draw.rectangle((  0, 100,  99, 199), fill=(  0, 255,   0))
    draw.rectangle((100, 100, 199, 199), fill=(  0,   0, 255))
    img.save("local/image.png")


def main(argv):
    create_image()


if __name__ == "__main__":
    main(sys.argv)
