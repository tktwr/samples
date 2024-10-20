#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py_lib:matplotlib:plot_data*

import numpy as np
import matplotlib.pyplot as plt


def f_read_data(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()

    x = []
    y = []

    for line in lines:
        l = line.split(" ")
        x.append(float(l[0]))
        y.append(float(l[1]))

    return (x, y)


def f_plot_data(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, "o")
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    plt.savefig('_output/plot_data.png')
    plt.show()


x = np.random.rand(100)
y = np.random.rand(100)
#x, y = f_read_data("../../data/plot_data.txt")
f_plot_data(x, y)
