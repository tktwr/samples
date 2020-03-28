#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.cv2*

import sys
import cv2
import numpy as np
import mycvmod

def f_image(fname):
    img = cv2.imread(fname)
    if len(img.shape) == 3:
        height, width, channels = img.shape[:3]
    else:
        height, width = img.shape[:2]
        channels = 1
    print("shape={}".format(img.shape))
    print("height={}".format(height))
    print("width={}".format(width))
    print("channels={}".format(channels))
    print("dtype={}".format(img.dtype))
    print("type={}".format(type(img)))

def f_resize(fname):
    img = cv2.imread(fname)
    h = img.shape[0]
    w = img.shape[1]
    print("h, w={}, {}".format(h, w))
    img2 = cv2.resize(img, (int(0.5*w), int(0.5*h)))
    cv2.imshow("resize", img2)

def f_blur(fname):
    img = cv2.imread(fname)
    img_blur = cv2.blur(img, (7, 7))
    img_gauss = cv2.GaussianBlur(img, (7, 7), 0)
    img_median = cv2.medianBlur(img, 7)
    img_bf = cv2.bilateralFilter(img, 9, 75, 75)
    img_out = img - img_gauss
    img_edge = cv2.Canny(img, 100, 200)

    mycv = mycvmod.MyCv()
    img_all = mycv.tile([
        [img, img_blur, img_gauss],
        [img_median, img_bf, img_edge]
        ])
    cv2.imwrite("_img_all.jpg", img_all)
    cv2.imshow("all", img_all)

def f_cvt(fname):
    img = cv2.imread(fname)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mycv = mycvmod.MyCv()
    img_cvt = mycv.tile([
        [img_rgb, img_lab, img_gray]
        ])
    cv2.imshow("cvt", img_cvt)

def f_np(fname):
    with open(fname, "rb") as f:
        binary = f.read()
    ar = np.asarray(bytearray(binary), dtype=np.uint8)
    img = cv2.imdecode(ar, -1)
    cv2.imshow("np", img)

fname = "../data/sample.jpg"

f_image(fname)
f_resize(fname)
f_blur(fname)
f_cvt(fname)
f_np(fname)

cv2.waitKey()

