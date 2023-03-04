#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *sample:py.numpy*

import sys
import numpy as np
import tt_util as ut


# *sample:py.numpy.init*
def f_init():
    x = np.array([[0, 1, 2],
                  [3, 4, 5]])

    print(f"np.empty([2, 3]) = \n{np.empty([2, 3])}")
    print(f"np.zeros([2, 3]) = \n{np.zeros([2, 3])}")
    print(f"np.ones([2, 3])  = \n{np.ones([2, 3])}")
    print(f"np.zeros_like(x) = \n{np.zeros_like(x)}")
    print(f"np.ones_like(x)  = \n{np.ones_like(x)}")
    print(f"eye(3)           = \n{np.eye(3)}")


# *sample:py.numpy.array_1d*
def f_array_1d():
    x = np.array([0, 1, 2])

    print(f"x       = {x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size  = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")


# *sample:py.numpy.array_1d_float*
def f_array_1d_float():
    x = np.array([0, 1, 2], dtype='float32')

    print(f"x       = {x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size  = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")


# *sample:py.numpy.array_2d*
def f_array_2d():
    x = np.array([[0, 1, 2],
                  [3, 4, 5]])

    print(f"x       = \n{x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size  = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")


# *sample:py.numpy.array_3d*
def f_array_3d():
    x = np.array([[[0, 1], [2, 3], [4, 5]],
                  [[6, 7], [8, 9], [10, 11]]])

    print(f"x       = \n{x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size  = {x.size}")
    print(f"x.min() = {x.min()}")
    print(f"x.max() = {x.max()}")

    print(f"x.max(axis=0)             =\n{x.max(axis=0)}")
    print(f"x.max(axis=0).max(axis=0) =\n{x.max(axis=0).max(axis=0)}")
    print(f"x.max(axis=(0,1))         = {x.max(axis=(0,1))}")

    print(f"x[:,:,0]       = \n{x[:,:,0]}")
    print(f"x[:,:,1]       = \n{x[:,:,1]}")
    print(f"x[:,:,0].max() = {x[:,:,0].max()}")
    print(f"x[:,:,1].max() = {x[:,:,1].max()}")


# *sample:py.numpy.array_op*
def f_array_op():
    x = np.array([0, 1, 2])
    y = np.array([3, 4, 5])

    print(f"x               = {x}")
    print(f"y               = {y}")
    print(f"x+y             = {x+y}")
    print(f"x*y             = {x*y}")
    print(f"np.append(x, y) = {np.append(x, y)}")


# *sample:py.numpy.arange*
# https://note.nkmk.me/python-numpy-arange-linspace/
def f_arange():
    # int
    print(np.arange(3))
    print(np.arange(3, 6))
    print(np.arange(3, 10, 2))

    # float
    print(np.arange(0.3, 1.0, 0.2))

    # minus
    print(np.arange(-3, 3))

    # wrong
    print(np.arange(10, 3))

    # decrease
    print(np.arange(10, 3, -2))

    # arange and reshape
    print(np.arange(24).reshape(2, 3, 4))


# *sample:py.numpy.linspace*
# https://note.nkmk.me/python-numpy-arange-linspace/
def f_linspace():
    print(np.linspace(0.0, 1.0, 5))


# *sample:py.numpy.reshape*
def f_reshape():
    x = np.arange(6)
    print(f"x = {x}")
    print(f"x.reshape(2, -1) =\n{x.reshape(2, -1)}")
    print(f"x.reshape(-1, 2) =\n{x.reshape(-1, 2)}")


# *sample:py.numpy.list_2d*
def f_list_2d():
    l1 = [1, 2, 3, 4]
    l2 = [0.1, 0.2, 0.3, 0.4]
    l = list(zip(l1, l2))
    ar = np.asarray(l)

    print(f"l1            = {l1}")
    print(f"l2            = {l2}")
    print(f"l             = {l}")
    print(f"ar            =\n{ar}")
    print(f"ar[:,0]       = {ar[:,0]}")
    print(f"ar[:,1]       = {ar[:,1]}")
    print(f"list(ar[:,1]) = {list(ar[:,1])}")


# -----------------------------------------------------
def _f_get_all_func_names():
    lst = []
    for i in globals():
        if callable(globals()[i]) and i.startswith('f_'):
            lst.append(i)
    return lst


if __name__ == '__main__':
    if len(sys.argv) == 1:
        func_lst = _f_get_all_func_names()
    else:
        func_lst = sys.argv[1:]
    print(func_lst)

    for func in func_lst:
        ut.print_title(f' [{func}] ', '-' * 55, 'center')
        eval(f'{func}()')
