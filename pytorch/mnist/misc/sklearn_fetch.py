#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 手書き数字の画像データMNISTをダウンロード
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original', data_home=".")  # data_homeは保存先を指定します

