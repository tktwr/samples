#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv_util as cu
import np_util as nu
import tt_path_util as pu


def f_test_scale_image():
    #ifname = pu.expand_env('$MY_SAMPLES/data/sample.jpg')
    ifname = pu.expand_env('new01_u8_c1.png')
    ofname = 'out.png'
    hw = [100, 200]
    img = cu.cv_load(ifname)
    print(img.shape)
    img = cu.cv_cvt_2d_to_3d(img)
    print(img.shape)
    oimg = nu.scale_img(img, hw)
    cu.cv_save(ofname, oimg)



if __name__ == "__main__":
    f_test_scale_image()
