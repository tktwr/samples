#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.PIL*

import sys
import numpy as np
from PIL import Image


def f_create_image(w, h):
    print("=== f_create_image() ===")
    img = Image.new('RGB', (w, h))
    ar = np.asarray(img, 'f')
    for y in range(h):
        for x in range(w):
            r = 255. * x / (w - 1)
            g = 255. * y / (h - 1)
            ar[y, x] = [r, g, 0]
    img_out = Image.fromarray(np.uint8(ar))
    img_out.save("local/pil_create_image.jpg")


def f_load_image_uint8(fname):
    print("=== f_load_image_uint8() ===")
    img = Image.open(fname)

    print(f"size: {img.size}")
    print(f"mode: {img.mode}")
    width, height = img.size
    print(f"w h: {width} {height}")

    rgb = img.convert('RGB')

    ar = np.asarray(img)
    print(f"shape: {ar.shape}")
    print(f"dtype: {ar.dtype}")
    print(f"size: {ar.size}")
    print(f"ndim: {ar.ndim}")

    img_out = Image.fromarray(ar)
    img_out.save("local/pil_load_image_uint8.jpg")


def f_load_image_float32(fname):
    print("=== f_load_image_float32() ===")
    ar = np.asarray(Image.open(fname), 'f')
    print(f"dtype: {ar.dtype}")
    print(f"ar[0, 0]: {ar[0, 0]}")  # 指定した座標の画素値 (R, G, B) / 原点は左上
    print(ar[:, :, 0].min())  # Rの最小値
    print(ar[:, :, 1].min())  # Gの最小値
    print(ar[:, :, 2].min())  # Bの最小値
    print(ar[:, :, 0].max())  # Rの最大値
    print(ar[:, :, 1].max())  # Gの最大値
    print(ar[:, :, 2].max())  # Bの最大値


def main(argv):
    fname = '../data/sample.jpg'
    f_create_image(300, 300)
    f_load_image_uint8(fname)
    f_load_image_float32(fname)


if __name__ == "__main__":
    main(sys.argv)
