#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *sample:py.pil*
# *sample:py.image*

import sys
import numpy as np
from PIL import Image


# pil
#   origin: upper-left
#   channel order: RGB

OUTPUT_DIR="_output"

def f_image_info(img):
    w, h = img.size
    print(f"format: {img.format}")
    print(f"mode: {img.mode}")
    print(f"size: {img.size}")
    print(f"w h: {w} {h}")
    print(f"img.getextrema(): {img.getextrema()}") 
    print(f"img.getbands(): {img.getbands()}")

    ar = np.asarray(img, 'f')
    print(f"dtype: {ar.dtype}")
    print(f"shape: {ar.shape}")
    print(f"size: {ar.size}")
    print(f"ndim: {ar.ndim}")
    print(f"ar[0, 0]: {ar[0, 0]}")
    r_min = ar[:, :, 0].min()
    g_min = ar[:, :, 1].min()
    b_min = ar[:, :, 2].min()
    r_max = ar[:, :, 0].max()
    g_max = ar[:, :, 1].max()
    b_max = ar[:, :, 2].max()
    print(f"min: {r_min} {g_min} {b_min}")
    print(f"max: {r_max} {g_max} {b_max}")


def f_image_load(fname):
    return Image.open(fname)


def f_image_save(fname, img):
    img.save(fname)


def f_image_show(img):
    img.show()


def f_image_create(w, h):
    img = Image.new('RGB', (w, h))
    ar = np.asarray(img, 'f')
    for y in range(h):
        for x in range(w):
            r = 255. * x / (w - 1)
            g = 255. * y / (h - 1)
            ar[y, x] = [r, g, 0]
    return Image.fromarray(np.uint8(ar))


# Use img.getchannel(i)
def f_image_extract_channel(img, ch):
    w, h = img.size
    out_img = Image.new('L', (w, h))
    out_ar = np.asarray(out_img, 'f')

    ar = np.asarray(img, 'f')
    for y in range(h):
        for x in range(w):
            out_ar[y, x] = ar[y, x][ch]
    return Image.fromarray(np.uint8(out_ar))


def f_image_getchannels(img):
    name = f"{OUTPUT_DIR}/pil_image_getchannel"
    for i in range(3):
        o = img.getchannel(i)
        o.save(f"{name}_{i}.png")


def f_image_exchange_channels(img):
    name = f"{OUTPUT_DIR}/pil_image_exchange_channels"
    r, g, b = img.split()
    o = Image.merge("RGB", (b, g, r))
    o.save(f"{name}.png")


def f_image_resize(img):
    name = f"{OUTPUT_DIR}/pil_image_resize"
    w, h = img.size
    size = (int(0.5 * w), int(0.5 * h))
    o = img.resize(size)
    o.save(f"{name}.png")


def f_image_gray(img):
    name = f"{OUTPUT_DIR}/pil_image_gray"
    o = img.convert("L")
    o.save(f"{name}.png")


def main(argv):
    name = f"{OUTPUT_DIR}/pil_image"
    img = f_image_create(100, 100)
    img.save(f"{name}.jpg")
    img.save(f"{name}.png")
    f_image_info(img)
    f_image_getchannels(img)
    f_image_exchange_channels(img)
    f_image_resize(img)
    f_image_gray(img)


if __name__ == "__main__":
    main(sys.argv)

