#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv2


ifname = sys.argv[1]
ofname = sys.argv[2]

iimg = cv2.imread(ifname, cv2.IMREAD_COLOR)
h, w = iimg.shape[:2]
osize = (int(w/2), int(h/2))
oimg = cv2.resize(iimg, osize, interpolation=cv2.INTER_AREA)
cv2.imwrite(ofname, oimg)
