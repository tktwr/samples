#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.numpy*

import sys
import numpy as np

def main():
    x = np.array([0, 1, 2])
    print("x =\n{}".format(x))
    print("x.dtype = {}".format(x.dtype))
    print("x.shape = {}".format(x.shape))
    print("x.size = {}".format(x.size))

    x = np.array([0, 1, 2], dtype='float32')
    print("x =\n{}".format(x))
    print("x.dtype = {}".format(x.dtype))
    print("x.shape = {}".format(x.shape))
    print("x.size = {}".format(x.size))

    x = np.array([[0, 1, 2],
                  [3, 4, 5]])
    print("x =\n{}".format(x))
    print("x.dtype = {}".format(x.dtype))
    print("x.shape = {}".format(x.shape))
    print("x.size = {}".format(x.size))

    print("np.empty([2, 3]) =\n{}".format(np.empty([2, 3])))
    print("np.zeros([2, 3]) =\n{}".format(np.zeros([2, 3])))
    print("np.ones([2, 3]) =\n{}".format(np.ones([2, 3])))
    print("np.zeros_like(x) =\n{}".format(np.zeros_like(x)))
    print("np.ones_like(x) =\n{}".format(np.ones_like(x)))
    print("eye(3) =\n{}".format(np.eye(3)))

    x = np.array([0, 1, 2])
    print("x =\n{}".format(x))
    y = np.append(x, [3, 4, 5])
    print("y =\n{}".format(y))
    z = y.reshape(2, -1)
    print("z =\n{}".format(z))

main()


