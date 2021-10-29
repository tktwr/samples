#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def f1(s, x):
    print(f"{s}: {x+x}")


def eval_cmd(cmd):
    print(cmd)
    eval(cmd)


if __name__ == "__main__":
    s = "x"
    x = 10
    #cmd = f'f1("{s}", {x})'
    cmd = f'f1("x", 10)'
    eval_cmd(cmd)

