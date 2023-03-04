#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *sample_py.skimage*

from skimage import io, color
from io import BytesIO

filename = '../data/sample.jpg'

# 画像ファイルパスから読み込み
img = io.imread(filename)

# バイナリから読み込み(python3なのでbinaryモードで読み込み)
with open(filename, 'rb') as f:
    binary = f.read()
img = io.imread(BytesIO(binary))

# numpy配列の取得、インスタンス自体がndarrayです
type(img)  # numpy.ndarray

# デフォルトの色はRGB/RGBAです
# 色の変換も充実しています。割とチェックもされる印象
# rgb = color.rgba2rgb(img)
# lab = color.rgb2lab(rgb)
