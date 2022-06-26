#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.numpy*

import sys
import numpy as np
import util as ut


# *memo_py.numpy.init*
def f_init():
    x = np.array([[0, 1, 2],
                  [3, 4, 5]])
    print(f"np.empty([2, 3]) =\n{np.empty([2, 3])}")
    print(f"np.zeros([2, 3]) =\n{np.zeros([2, 3])}")
    print(f"np.ones([2, 3]) =\n{np.ones([2, 3])}")
    print(f"np.zeros_like(x) =\n{np.zeros_like(x)}")
    print(f"np.ones_like(x) =\n{np.ones_like(x)}")
    print(f"eye(3) =\n{np.eye(3)}")


# *memo_py.numpy.array_1d*
def f_array_1d():
    x = np.array([0, 1, 2])
    print(f"x = {x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")


# *memo_py.numpy.array_1d_float*
def f_array_1d_float():
    x = np.array([0, 1, 2], dtype='float32')
    print(f"x = {x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")


# *memo_py.numpy.array_2d*
def f_array_2d():
    x = np.array([[0, 1, 2],
                  [3, 4, 5]])
    print(f"x =\n{x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")


# *memo_py.numpy.array_3d*
def f_array_3d():
    x = np.array([[[0, 1], [2, 3], [4, 5]],
                  [[6, 7], [8, 9], [10, 11]]])
    print(f"x =\n{x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")
    print(f"x.max(axis=0) =\n{x.max(axis=0)}")
    print(f"x.max(axis=0).max(axis=0) =\n{x.max(axis=0).max(axis=0)}")
    print(f"x.max(axis=(0,1)) = {x.max(axis=(0,1))}")
    print(f"x[:,:,0] =\n{x[:,:,0]}")
    print(f"x[:,:,1] =\n{x[:,:,1]}")
    print(f"x[:,:,0].max() = {x[:,:,0].max()}")
    print(f"x[:,:,1].max() = {x[:,:,1].max()}")


# *memo_py.numpy.array_op*
def f_array_op():
    x = np.array([0, 1, 2])
    y = np.array([3, 4, 5])
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"x+y = {x+y}")
    print(f"x*y = {x*y}")
    print(f"np.append(x, y) = {np.append(x, y)}")


# *memo_py.numpy.arange*
def f_arange():
    x = np.arange(6)
    print(f"x = {x}")
    x = np.arange(0.0, 1.0, 0.2)
    print(f"x = {x}")
    x = np.linspace(0.0, 1.0, 5)
    print(f"x = {x}")
    x = np.arange(24).reshape(2, 3, 4)
    print(f"x =\n{x}")


# *memo_py.numpy.reshape*
def f_reshape():
    x = np.arange(6)
    print(f"x = {x}")
    print(f"x.reshape(2, -1) =\n{x.reshape(2, -1)}")
    print(f"x.reshape(-1, 2) =\n{x.reshape(-1, 2)}")


# *memo_py.numpy.list_2d*
def f_list_2d():
    l1 = [1, 2, 3, 4]
    l2 = [0.1, 0.2, 0.3, 0.4]
    l = list(zip(l1, l2))
    ar = np.asarray(l)

    print(f"l1: {l1}")
    print(f"l2: {l2}")
    print(f"l: {l}")
    print(f"ar: {ar}")
    print(f"ar[:,0]: {ar[:,0]}")
    print(f"ar[:,1]: {ar[:,1]}")
    print(f"list(ar[:,1]): {list(ar[:,1])}")


def main(argv):
    funcs = (
            "f_init",
            "f_array_1d",
            "f_array_1d_float",
            "f_array_2d",
            "f_array_3d",
            "f_array_op",
            "f_arange",
            "f_reshape",
            "f_list_2d",
            )

    if len(argv) == 1:
        selected = funcs
    else:
        selected = argv[1:]

    for i in selected:
        ut.f_title(i)
        eval(f"{i}()")


if __name__ == "__main__":
    main(sys.argv)
