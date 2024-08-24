#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import tt_util as tu


#N = 1000
N = 3
l = np.random.rand(N, N)


def f(x):
    return x ** 3

vf = np.vectorize(f)
uf = np.frompyfunc(f, 1, 1)

@tu.timeit
def timeit_f(l):
    for i in l:
        f(i)

@tu.timeit
def timeit_vf(l):
    vf(l)


@tu.timeit
def timeit_uf(l):
    uf(l)


@tu.timeit
def timeit_np(l):
    l ** 3


timeit_f(l)
timeit_vf(l)
timeit_uf(l)
timeit_np(l)

