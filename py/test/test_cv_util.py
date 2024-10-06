#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import np_util as nu
import cv_util as cu
import tt_util as tu


I_FILE = '$MY_SAMPLES/data/images/sample.jpg'
O_DIR = '_output'


def f_img_new():
    shape = (200, 300, 3)
    dtype = 'uint8'
    bgr = (255, 0, 0)

    img = cu.cv_create_img(shape, dtype, bgr)

    cu.cv_save(f'{O_DIR}/new_c3_{dtype}.png', img)


def f_img_lab():
    img = cu.cv_load(I_FILE)
    img = cu.cv_img_bgr2lab(img)
    cu.cv_save(f'{O_DIR}/lab.png', img)

    img_l, img_a, img_b = cu.cv_split_img(img)
    cu.cv_save(f'{O_DIR}/lab_l.png', img_l)
    cu.cv_save(f'{O_DIR}/lab_a.png', img_a)
    cu.cv_save(f'{O_DIR}/lab_b.png', img_b)


def f_img_op():
    img = cu.cv_load(I_FILE)
    img = cu.img_u8_to_f32(img)

    img = cu.cv_channel_img(img, 0)
    one_img = np.ones_like(img)
    oimg = one_img - img

    oimg = cu.img_f32_to_u8(oimg)
    cu.cv_save(f'{O_DIR}/op01.png', oimg)


def f_img_scale():
    img = cu.cv_load(I_FILE)
    oimg = nu.img_scale(img, [600, 600])
    cu.cv_save(f'{O_DIR}/scale01.png', oimg)


# -----------------------------------------------------
def run_funcs():
    func_lst = tu.get_all_funcs(globals().keys())
    for func in func_lst:
        tu.log_title(f' [{func}] ')
        eval(f'{func}()')


if __name__ == '__main__':
    run_funcs()
