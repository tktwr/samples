#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('Z:/data/images/sample.jpg',0)

edges = cv2.Canny(img,100,200)

cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
