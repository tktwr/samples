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

    img = cu.img_create(shape, dtype, bgr)

    cu.imgfile_save(f'{O_DIR}/new_c3_{dtype}.png', img)


def f_img_lab():
    img = cu.imgfile_load(I_FILE)
    img = cu.img_bgr_to_lab(img)
    cu.imgfile_save(f'{O_DIR}/lab.png', img)

    img_l, img_a, img_b = cu.img_split(img)
    cu.imgfile_save(f'{O_DIR}/lab_l.png', img_l)
    cu.imgfile_save(f'{O_DIR}/lab_a.png', img_a)
    cu.imgfile_save(f'{O_DIR}/lab_b.png', img_b)


def f_img_op():
    img = cu.imgfile_load(I_FILE)
    img = cu.img_u8_to_f32(img)

    img = cu.img_channel(img, 0)
    one_img = np.ones_like(img)
    oimg = one_img - img

    oimg = cu.img_f32_to_u8(oimg)
    cu.imgfile_save(f'{O_DIR}/op01.png', oimg)


def f_img_scale():
    img = cu.imgfile_load(I_FILE)
    oimg = nu.img_scale(img, [600, 600])
    cu.imgfile_save(f'{O_DIR}/scale01.png', oimg)


# -----------------------------------------------------
def run_funcs():
    func_lst = tu.get_all_funcs(globals().keys())
    for func in func_lst:
        tu.log_title(f' [{func}] ')
        eval(f'{func}()')


if __name__ == '__main__':
    run_funcs()
