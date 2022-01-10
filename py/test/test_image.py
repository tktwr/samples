#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv_util as cu


def bgr_to_bgra(dtype):
    img = cu.cv_load(f'new_3_{dtype}.png')
    img_bgra = cu.cv_bgr_to_bgra_img(img)
    cu.cv_save(f'bgra_{dtype}.png', img_bgra)

    img_bgr = cu.cv_bgra_to_bgr_img(img_bgra)
    cu.cv_save(f'bgr_{dtype}.png', img_bgr)


def main(argv):
    bgr_to_bgra('uint8')
    bgr_to_bgra('uint16')


if __name__ == "__main__":
    main(sys.argv)

