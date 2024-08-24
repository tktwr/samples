#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import tt_util as ut


def f_max():
    a = np.arange(6).reshape(2, 3)
    print(a)
    print(a.max())
    print(a.max(axis=0))
    print(a.max(axis=1))


def f_maximum():
    a = np.arange(6).reshape(2, 3)
    b = np.arange(6, 0, -1).reshape(2, 3)
    print(a)
    print(b)
    print(np.maximum(a, b))


def f_max_img():
    a = np.arange(6).reshape(2, 3)
    b = np.arange(6, 0, -1).reshape(2, 3)
    c = np.arange(6).reshape(2, 3)
    lst = np.array([a, b, c])
    print(lst)
    print(lst.max(axis=0))
    print(lst.max(axis=1))
    print(lst.max(axis=2))


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
