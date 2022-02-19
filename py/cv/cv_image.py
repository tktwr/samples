#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.cv2*

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv_util as cvut
import util as ut


INPUT_DIR = "../../data"
OUTPUT_DIR = "_output"
fname = f"{INPUT_DIR}/sample.jpg"
fname2 = f"{INPUT_DIR}/sample2.jpg"


def f_info():
    cvut.cv_info(fname)


# *memo_py.cv2.f_new*
def f_new():
    w = 200
    h = 200
    img = np.zeros((h, w, 3), np.uint8)
    img[:,0:w//2] = (255,0,0)      # (B, G, R)
    img[:,w//2:w] = (0,255,0)
    cv2.imwrite(f"{OUTPUT_DIR}/new.jpg", img)


# *memo_py.cv2.f_resize*
def f_resize():
    img = cv2.imread(fname)
    h = img.shape[0]
    w = img.shape[1]
    img_resize = cv2.resize(img, (int(0.5*w), int(0.5*h)))
    cv2.imwrite(f"{OUTPUT_DIR}/resize.jpg", img_resize)


# *memo_py.cv2.f_crop*
def f_crop():
    img = cv2.imread(fname)

    # specified by location
    # img[top:bottom, left:right]
    out = img[0:50, 0:50]
    cv2.imwrite(f"{OUTPUT_DIR}/crop.jpg", out)


# *memo_py.cv2.f_cvt*
def f_cvt():
    img = cv2.imread(fname)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_list = [
        [img, img_rgb],
        [img_lab, img_gray]
        ]
    img_tile = cvut.cv_htile(img_list)
    cv2.imwrite(f"{OUTPUT_DIR}/cvt.jpg", img_tile)


# *memo_py.cv2.f_red*
def f_red():
    img = cv2.imread(fname)
    # B, G channelsを0にする
    img[:, :, (0, 1)] = 0
    cv2.imwrite(f"{OUTPUT_DIR}/red.jpg", img)


# *memo_py.cv2.f_np*
def f_np():
    with open(fname, "rb") as f:
        binary = f.read()
    ar = np.asarray(bytearray(binary), dtype=np.uint8)
    img = cv2.imdecode(ar, -1)
    cv2.imwrite(f"{OUTPUT_DIR}/np.jpg", img)


# *memo_py.cv2.f_blur*
def f_blur():
    img = cv2.imread(fname)
    img_blur = cv2.blur(img, (7, 7))
    img_gauss = cv2.GaussianBlur(img, (7, 7), 0)
    img_median = cv2.medianBlur(img, 7)
    img_bf = cv2.bilateralFilter(img, 9, 75, 75)
    img_sub = img - img_gauss
    img_edge = cv2.Canny(img, 100, 200)

    img_list = [
        [img, img_blur, img_gauss],
        [img_median, img_bf],
        [img_sub, img_edge]
        ]
    img_tile = cvut.cv_htile(img_list)
    cv2.imwrite(f"{OUTPUT_DIR}/blur_all.jpg", img_tile)


# *memo_py.cv2.f_tile*
def f_tile():
    im1 = cv2.imread(fname)
    im2 = cv2.imread(fname2)

    img_list = [
        [im1],
        [im1, im2, im1, im2, im1],
        [im1, im2, im1]
        ]
    img_tile   = cvut.cv_htile(img_list)
    img_tile_h = cvut.cv_hconcat([im1, im2, im1])
    img_tile_v = cvut.cv_vconcat([im1, im2, im1])

    cv2.imwrite(f"{OUTPUT_DIR}/tile.jpg",   img_tile)
    cv2.imwrite(f"{OUTPUT_DIR}/tile_h.jpg", img_tile_h)
    cv2.imwrite(f"{OUTPUT_DIR}/tile_v.jpg", img_tile_v)


# *memo_py.cv2.f_hist*
def f_hist():
    img = cv2.imread(fname)
    color = ('b','g','r')
    for i,col in enumerate(color):
       histr = cv2.calcHist([img],[i],None,[256],[0,256])
       plt.plot(histr,color = col)
       plt.xlim([0,256])
    plt.show()


# *memo_py.cv2.f_draw*
def f_draw():
    img = cv2.imread(fname)
    img = cv2.rectangle(img, (50, 50), (100, 100), (255, 0, 0), 3)
    cv2.imwrite(f"{OUTPUT_DIR}/draw_rect.jpg", img)


def main(argv):
    funcs = (
            "f_info",
            "f_new",
            "f_resize",
            "f_crop",
            "f_cvt",
            "f_red",
            "f_np",
            "f_blur",
            "f_tile",
            "f_hist",
            "f_draw",
            )

    if len(argv) == 1:
        selected = funcs
    else:
        selected = argv[1:]

    for i in selected:
        ut.f_title(i)
        eval(f"{i}()")

    cv2.waitKey()


if __name__ == "__main__":
    main(sys.argv)
