#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.cv2*

import sys
import numpy as np
import cv2

filename = '../data/sample.jpg'

img = cv2.imread(filename)

with open(filename, 'rb') as f:
    binary = f.read()
# 一度ndarrayに変換してからdecodeします。reshapeだけしてると思われます
ar = np.asarray(bytearray(binary), dtype=np.uint8)
img = cv2.imdecode(ar, -1)  # 'load it as it is'

# numpy配列の取得、インスタンス自体がndarrayです
type(img) # numpy.ndarray

# デフォルトの色がBGR
# 色の変換は充実。ただし指定のチェックは甘い(間違えて指定しても普通に変換される)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

