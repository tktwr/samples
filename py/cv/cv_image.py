#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.cv2*

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import mycvmod
from common import f_title


def f_image(fname):
    f_title("f_image()")

    img = cv2.imread(fname)
    if len(img.shape) == 3:
        height, width, channels = img.shape[:3]
    else:
        height, width = img.shape[:2]
        channels = 1

    print(f"shape={img.shape}")
    print(f"height={height}")
    print(f"width={width}")
    print(f"channels={channels}")
    print(f"dtype={img.dtype}")
    print(f"type={type(img)}")


def f_resize(fname):
    f_title("f_resize()")

    img = cv2.imread(fname)
    h = img.shape[0]
    w = img.shape[1]
    print(f"h, w={h}, {w}")
    img2 = cv2.resize(img, (int(0.5*w), int(0.5*h)))
    print(f"img2.shape={img2.shape}")
    cv2.imshow("resize", img2)


def f_blur(fname):
    f_title("f_blur()")

    img = cv2.imread(fname)
    img_blur = cv2.blur(img, (7, 7))
    img_gauss = cv2.GaussianBlur(img, (7, 7), 0)
    img_median = cv2.medianBlur(img, 7)
    img_bf = cv2.bilateralFilter(img, 9, 75, 75)
    img_sub = img - img_gauss
    img_edge = cv2.Canny(img, 100, 200)

    mycv = mycvmod.MyCv()
    img_all = mycv.tile([
        [img, img_blur, img_gauss],
        [img_median, img_bf],
        [img_sub, img_edge]
        ])
    cv2.imwrite("local/blur_all.jpg", img_all)
    cv2.imshow("blur_all", img_all)


def f_cvt(fname):
    f_title("f_cvt()")

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
    f_title("f_np()")

    with open(fname, "rb") as f:
        binary = f.read()
    ar = np.asarray(bytearray(binary), dtype=np.uint8)
    img = cv2.imdecode(ar, -1)
    cv2.imshow("np", img)


def f_hist(fname):
    f_title("f_hist()")

    img = cv2.imread(fname)
    color = ('b','g','r')
    for i,col in enumerate(color):
       histr = cv2.calcHist([img],[i],None,[256],[0,256])
       plt.plot(histr,color = col)
       plt.xlim([0,256])
    plt.show()


def f_tile():
    im1 = cv2.imread("../data/sample.jpg")
    im2 = cv2.imread("../data/sample2.jpg")
    mycv = mycvmod.MyCv()
    img_cat = mycv.tile([[im1],
                         [im1, im2, im1, im2, im1],
                         [im1, im2, im1]])
    cv2.imwrite("local/img_cat.jpg", img_cat)
    cv2.imshow("img_cat", img_cat)

    img_hcat = mycv.hconcat([im1, im2, im1])
    cv2.imwrite("local/img_hcat.jpg", img_hcat)
    cv2.imshow("img_hcat", img_hcat)

    img_vcat = mycv.vconcat([im1, im2, im1])
    cv2.imwrite("local/img_vcat.jpg", img_vcat)
    cv2.imshow("img_vcat", img_vcat)


def main(argv):
    fname = "../data/sample.jpg"

    f_image(fname)
    f_resize(fname)
    f_blur(fname)
    f_cvt(fname)
    f_np(fname)
    f_tile()
    f_hist(fname)

    cv2.waitKey()


if __name__ == "__main__":
    main(sys.argv)
