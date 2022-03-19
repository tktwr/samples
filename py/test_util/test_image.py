#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv_util as cu


def f_new():
    shape = (200, 300, 3)
    dtype = 'uint8'
    bgr = (255, 0, 0)

    img = cu.cv_create_img(shape, dtype, bgr)

    fname = f'new_3_{dtype}.png'
    cu.cv_save(fname, img)


def f_bgr_to_bgra(dtype):
    img = cu.cv_load(f'new_3_{dtype}.png')

    img_bgra = cu.cv_bgr_to_bgra_img(img)
    cu.cv_save(f'bgra_{dtype}.png', img_bgra)

    img_bgr = cu.cv_bgra_to_bgr_img(img_bgra)
    cu.cv_save(f'bgr_{dtype}.png', img_bgr)


def main(argv):
    f_new()
    f_bgr_to_bgra('uint8')
    #f_bgr_to_bgra('uint16')


if __name__ == "__main__":
    main(sys.argv)

