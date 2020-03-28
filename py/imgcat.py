#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv2

def hconcat_resize_min(im_list, itp=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=itp) for im in im_list]
    return cv2.hconcat(im_list_resize)

def vconcat_resize_min(im_list, itp=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=itp) for im in im_list]
    return cv2.vconcat(im_list_resize)

def concat_tile_resize(im_list_2d, itp=cv2.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, itp) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, itp)

def main():
    im1 = cv2.imread("../data/sample.jpg")
    im2 = cv2.imread("../data/sample2.jpg")
    imgcat = concat_tile_resize([[im1],
                                 [im1, im2, im1, im2, im1],
                                 [im1, im2, im1]])
    cv2.imwrite("_imgcat.jpg", imgcat)
    cv2.imshow("imgcat", imgcat)
    cv2.waitKey()

main()


