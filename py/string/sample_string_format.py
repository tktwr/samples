#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:string_format*


def f_sample_py_string_format():
    # f-string (python >= 3.6)
    ival = 2
    fval = 1 / 3
    word = "hello"
    width = 10

    print(f"1+1         = {1+1}")
    print(f"1+0.5       = {1+0.5}")
    print(f"ival        = {ival}")
    print(f"ival:3d     = {ival:3d}")
    print(f"ival:03d    = {ival:03d}")
    print(f"ival**10:,d = {ival**10:,d}")
    print(f"fval        = {fval}")
    print(f"fval:.3f    = {fval:.3f}")
    print(f"word:<10s   = [{word:<{width}s}]")
    print(f"word:^10s   = [{word:^{width}s}]")
    print(f"word:>10s   = [{word:>{width}s}]")
    print(f"word        = ", end='')
    print(word)


f_sample_py_string_format()
