#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import tt_util as tu


# Vectorize wraps frompyfunc. Vectorize adds extra features:
# - Copies the docstring from the original function
# - Allows you to exclude an argument from broadcasting rules.
# - Returns an array of the correct dtype instead of dtype=object

# $ ./ufunc.py 
# timeit_f : avg=0.375 sec, median=0.376 sec
# timeit_vf: avg=0.325 sec, median=0.321 sec
# timeit_uf: avg=0.271 sec, median=0.268 sec
# timeit_np: avg=0.040 sec, median=0.040 sec


N = 1000000
l = np.random.rand(N)

#f = lambda x: x ** 3

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

