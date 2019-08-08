#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.PIL*

import sys
import numpy as np
from PIL import Image

def f_create_image(fname, w, h):
    print("=== f_create_image() ===")
    img = Image.new('RGB', (w, h))
    ar = np.array(img, 'f')
    for y in range(h):
        for x in range(w):
            f = 255. * x / (w - 1)
            ar[y, x] = [f, 0, 0]
    img_out = Image.fromarray(np.uint8(ar))
    img_out.save(fname)

def f_load_image_uint8(fname):
    print("=== f_load_image_uint8() ===")
    img = Image.open(fname)

    width, height = img.size
    print("w h: {0} {1}".format(width, height))
    print("mode: {0}".format(img.mode))

    rgb = img.convert('RGB')

    ar = np.asarray(img)
    print("shape: {0}".format(ar.shape))
    print("dtype: {0}".format(ar.dtype))
    print("size: {0}".format(ar.size))
    print("ndim: {0}".format(ar.ndim))

    img_out = Image.fromarray(ar)
    img_out.save("_out_pil_load_image_uint8.jpg")

def f_load_image_float32(fname):
    print("=== f_load_image_float32() ===")
    ar = np.array(Image.open(fname), 'f')
    print("dtype: {0}".format(ar.dtype))
    print("ar[0, 0]: {}".format(ar[0, 0]))  # 指定した座標の画素値 (R, G, B) / 原点は左上
    print(ar[:, :, 0].min())  # Rの最小値
    print(ar[:, :, 1].min())  # Gの最小値
    print(ar[:, :, 2].min())  # Bの最小値
    print(ar[:, :, 0].max())  # Rの最大値
    print(ar[:, :, 1].max())  # Gの最大値
    print(ar[:, :, 2].max())  # Bの最大値

def main():
    fname = '../data/sample.jpg'
    f_create_image("_out_pil_create_image.png", 300, 300)
    f_load_image_uint8(fname)
    f_load_image_float32(fname)

main()

