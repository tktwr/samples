#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import cv_util as cu


def img_conv(ifname, ofname):
    img = cu.cv_load(ifname)
    img = cu.cv_channel_img(img, 0)
    img = img.astype(np.float32) / 255

    one_img = np.ones_like(img)
    out_img = one_img - img
    out_img *= 255
    out_img = out_img.astype(np.uint8)

    cu.cv_save(ofname, out_img)


if __name__ == "__main__":
    img_conv(sys.argv[1], sys.argv[2])
