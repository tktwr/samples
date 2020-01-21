#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.matplotlib*

import sys
import numpy as np
import matplotlib.pyplot as plt

def main():
    # 描画範囲の指定
    # x = np.arange(x軸の最小値, x軸の最大値, 刻み)
    x = np.arange(-3, 3, 0.1)

    # 計算式
    y = x * x

    # 横軸の変数。縦軸の変数。
    plt.plot(x, y)

    # 描画実行
    plt.show()

main()

