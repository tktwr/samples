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


def main(argv):
    f_new()


if __name__ == "__main__":
    main(sys.argv)

