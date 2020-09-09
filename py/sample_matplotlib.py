#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.matplotlib*

import sys
import numpy as np
import matplotlib.pyplot as plt


def plot_graph():
    # 描画範囲の指定
    # x = np.arange(x軸の最小値, x軸の最大値, 刻み)
    x = np.arange(-3, 3, 0.1)
    y = x * x
    plt.plot(x, y)
    plt.show()


def read_data(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()

    x = []
    y = []

    for line in lines:
        l = line.split(" ")
        x.append(float(l[0]))
        y.append(float(l[1]))

    return (x, y)


def plot_data():
    #x = np.random.rand(100)
    #y = np.random.rand(100)
    x, y = read_data("data_plot.txt")

    fig, ax = plt.subplots()
    ax.plot(x, y, "o")
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    plt.show()


def main(argv):
    plot_graph()
    plot_data()


if __name__ == "__main__":
    main(sys.argv)
