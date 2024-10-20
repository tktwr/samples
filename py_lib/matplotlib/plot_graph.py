#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py_lib:matplotlib:plot_graph*

import numpy as np
import matplotlib.pyplot as plt


def f_plot_graph():
    # 描画範囲の指定
    # x = np.arange(x軸の最小値, x軸の最大値, 刻み)
    x = np.arange(-3, 3, 0.1)
    y = x * x
    plt.plot(x, y)
    plt.savefig('_output/plot_graph.png')
    plt.show()


f_plot_graph()
