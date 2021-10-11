#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.cv2*

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv_util
from common import f_title


INPUT_DIR = "../../data"
OUTPUT_DIR = "_output"
fname = f"{INPUT_DIR}/sample.jpg"
fname2 = f"{INPUT_DIR}/sample2.jpg"


def f_image():
    img = cv2.imread(fname)
    if len(img.shape) == 3:
        height, width, channels = img.shape[:3]
    else:
        height, width = img.shape[:2]
        channels = 1

    print(f"img.shape = {img.shape}")
    print(f"height    = {height}")
    print(f"width     = {width}")
    print(f"channels  = {channels}")
    print(f"img.dtype = {img.dtype}")
    print(f"type(img) = {type(img)}")
    cv2.imshow("img", img)


def f_new():
    w = 200
    h = 200
    img = np.zeros((h, w, 3), np.uint8)
    img[:,0:w//2] = (255,0,0)      # (B, G, R)
    img[:,w//2:w] = (0,255,0)
    cv2.imwrite(f"{OUTPUT_DIR}/new.jpg", img)


def f_resize():
    img = cv2.imread(fname)
    h = img.shape[0]
    w = img.shape[1]
    img_resize = cv2.resize(img, (int(0.5*w), int(0.5*h)))
    cv2.imwrite(f"{OUTPUT_DIR}/resize.jpg", img_resize)


def f_crop():
    img = cv2.imread(fname)

    # specified by location
    # img[top:bottom, left:right]
    out = img[0:50, 0:50]
    cv2.imwrite(f"{OUTPUT_DIR}/crop.jpg", out)


def f_cvt():
    img = cv2.imread(fname)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mycv = cv_util.ImageTile()
    img_cvt = mycv.tile([
        [img, img_rgb],
        [img_lab, img_gray]
        ])
    cv2.imwrite(f"{OUTPUT_DIR}/cvt.jpg", img_cvt)


def f_red():
    img = cv2.imread(fname)
    # B, G channelsを0にする
    img[:, :, (0, 1)] = 0
    cv2.imwrite(f"{OUTPUT_DIR}/red.jpg", img)


def f_np():
    with open(fname, "rb") as f:
        binary = f.read()
    ar = np.asarray(bytearray(binary), dtype=np.uint8)
    img = cv2.imdecode(ar, -1)
    cv2.imwrite(f"{OUTPUT_DIR}/np.jpg", img)


def f_blur():
    img = cv2.imread(fname)
    img_blur = cv2.blur(img, (7, 7))
    img_gauss = cv2.GaussianBlur(img, (7, 7), 0)
    img_median = cv2.medianBlur(img, 7)
    img_bf = cv2.bilateralFilter(img, 9, 75, 75)
    img_sub = img - img_gauss
    img_edge = cv2.Canny(img, 100, 200)

    mycv = cv_util.ImageTile()
    img_all = mycv.tile([
        [img, img_blur, img_gauss],
        [img_median, img_bf],
        [img_sub, img_edge]
        ])
    cv2.imwrite(f"{OUTPUT_DIR}/blur_all.jpg", img_all)


def f_tile():
    im1 = cv2.imread(fname)
    im2 = cv2.imread(fname2)
    mycv = cv_util.ImageTile()
    img_cat = mycv.tile([[im1],
                         [im1, im2, im1, im2, im1],
                         [im1, im2, im1]])
    img_hcat = mycv.hconcat([im1, im2, im1])
    img_vcat = mycv.vconcat([im1, im2, im1])

    cv2.imwrite(f"{OUTPUT_DIR}/tile_cat.jpg", img_cat)
    cv2.imwrite(f"{OUTPUT_DIR}/tile_hcat.jpg", img_hcat)
    cv2.imwrite(f"{OUTPUT_DIR}/tile_vcat.jpg", img_vcat)


def f_hist():
    img = cv2.imread(fname)
    color = ('b','g','r')
    for i,col in enumerate(color):
       histr = cv2.calcHist([img],[i],None,[256],[0,256])
       plt.plot(histr,color = col)
       plt.xlim([0,256])
    plt.show()


def main(argv):
    dict_func = {
            "image"  : f_image,
            "new"    : f_new,
            "resize" : f_resize,
            "crop"   : f_crop,
            "cvt"    : f_cvt,
            "red"    : f_red,
            "np"     : f_np,
            "blur"   : f_blur,
            "tile"   : f_tile,
            "hist"   : f_hist,
            }

    if len(argv) == 1:
        func_names = dict_func.keys()
    else:
        func_names = argv[1:]

    for i in func_names:
        f_title(i)
        dict_func[i]()

    cv2.waitKey()


if __name__ == "__main__":
    main(sys.argv)
