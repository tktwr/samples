#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plt_util as pu


def f1(x):
    return x


def f2(x):
    return x * x


def f3(x):
    return x * x * x


if __name__ == "__main__":
    xrange = (0, 1, 10)
    x, y1 = pu.make_data(f1, xrange)
    x, y2 = pu.make_data(f2, xrange)
    x, y3 = pu.make_data(f3, xrange)
    y = list(zip(y1, y2, y3))

    plot_data1 = '_output/plot_data1.txt'
    pu.write_data(plot_data1, x, y1)
    pu.plot_data(x, y1)

    plot_data2 = '_output/plot_data2.txt'
    pu.write_data(plot_data2, x, y)
    pu.plot_rgb_data(x, y)

    x, r, g, b = pu.read_data(plot_data2)
    rgb = list(zip(r, g, b))
    pu.plot_rgb_data(x, rgb)

