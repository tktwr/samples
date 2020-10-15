#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from PIL import Image


def f_image_create(w, h):
    img = Image.new('RGB', (w, h))
    ar = np.asarray(img, 'f')
    for y in range(h):
        for x in range(w):
            r = 255. * x / (w - 1)
            g = 255. * y / (h - 1)
            ar[y, x] = [r, g, 0]
    return Image.fromarray(np.uint8(ar))


def f_image_load(fname):
    return Image.open(fname)


def f_image_save(fname, img):
    img.save(fname)


def f_image_show(img):
    img.show()


def f_image_info(img):
    print(f"format: {img.format}")
    print(f"mode: {img.mode}")
    print(f"size: {img.size}")
    print(f"extrema: {img.getextrema()}") 


def f_image_extract_channel(img, ch):
    w, h = img.size
    out_img = Image.new('L', (w, h))
    out_ar = np.asarray(out_img, 'f')

    ar = np.asarray(img, 'f')
    for y in range(h):
        for x in range(w):
            out_ar[y, x] = ar[y, x][ch]
    return Image.fromarray(np.uint8(out_ar))


def f_test(img):
    print(img.getbands())
    img_0 = img.getchannel(0)
    img_0.save("local/img_0.png")


def main(argv):
    fname = "local/image_tool_create"

    img = f_image_create(100, 100)
    f_image_info(img)
    f_image_save(f"{fname}.jpg", img)
    f_image_save(f"{fname}.png", img)

    img_0 = f_image_extract_channel(img, 0)
    f_image_save(f"{fname}_0.png", img_0)

    img_1 = f_image_extract_channel(img, 1)
    f_image_save(f"{fname}_1.png", img_1)

    f_test(img)


if __name__ == "__main__":
    main(sys.argv)

