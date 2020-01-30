#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np

def main():
    img = cv2.imread("../data/sample.jpg")
    cv2.imshow("img", img)

    blur = cv2.blur(img, (7, 7))
    cv2.imshow("blur", blur)

    gauss = cv2.GaussianBlur(img, (7, 7), 0)
    cv2.imshow("gauss", gauss)

    median = cv2.medianBlur(img, 7)
    cv2.imshow("median", median)

    bf = cv2.bilateralFilter(img, 9, 75, 75)
    cv2.imshow("bf", bf)

    out = img - gauss
    cv2.imshow("out", out)

    cv2.waitKey()

main()


