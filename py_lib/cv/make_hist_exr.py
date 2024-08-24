#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def f_image_show(fname):
    img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
    h, w = img.shape[:2]
    new_wh = (1000, int(1000 * h / w))
    img = cv2.resize(img, new_wh, interpolation=cv2.INTER_AREA)
    #img = np.power(img, 1.0/2.2)

    img = np.clip(img * 255, 0, 255).astype(np.uint8)
    cv2.imwrite(f'srgb_{fname}.png', img)
    cv2.imshow(f"{fname}", img)


def f_hist_exr(fname):
    img = cv2.imread(fname, cv2.IMREAD_UNCHANGED)
    #img = np.power(img, 1.0/2.2)

    img = np.clip(img * 255, 0, 255).astype(np.uint8)
    color = ('b','g','r')
    for i,col in enumerate(color):
       histr = cv2.calcHist([img],[i],None,[256],[0,256])
       plt.plot(histr,color = col)
       plt.xlim([0,256])
    plt.savefig(f'hist_{fname}.png')
    plt.show()


def main(argv):
    fname = argv[1]
    f_image_show(fname)
    f_hist_exr(fname)


if __name__ == "__main__":
    main(sys.argv)

