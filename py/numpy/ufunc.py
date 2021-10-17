#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import numpy as np

N = 1000000
l = np.random.rand(N)

#f = lambda x: x ** 3

def f(x):
    return x ** 3

vf = np.vectorize(f)
uf = np.frompyfunc(f, 1, 1)

def timeit(func):
    def wrapper(*args, **kargs):
        time_list = []
        for i in range(5):
            start = time.time()
            func(*args, **kargs)
            end = time.time()
            time_list.append(end - start)
        avg = np.mean(time_list)
        median = np.median(time_list)
        print(f"{func.__name__}: avg={avg:.3f} sec, median={median:.3f} sec")
    return wrapper


@timeit
def timeit_f(l):
    for i in l:
        f(i)

@timeit
def timeit_vf(l):
    vf(l)


@timeit
def timeit_uf(l):
    uf(l)


@timeit
def timeit_np(l):
    l ** 3


timeit_f(l)
timeit_vf(l)
timeit_uf(l)
timeit_np(l)

