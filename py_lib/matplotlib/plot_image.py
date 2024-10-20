#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py_lib:matplotlib:plot_image*

import matplotlib.pyplot as plt


def f_plot_image():
    img = plt.imread('../../data/images/sample.jpg')
    plt.title('Image')
    plt.axis('off')
    plt.imshow(img)
    plt.savefig('_output/plot_image.png')
    plt.show()


f_plot_image()
