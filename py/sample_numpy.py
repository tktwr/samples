#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

def main():
    x = np.array([0, 1, 2])
    print("x =\n{}".format(x))
    x = np.array([[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]])
    print("x =\n{}".format(x))
    print("np.empty([2, 3]) =\n{}".format(np.empty([2, 3])))
    print("np.zeros([2, 3]) =\n{}".format(np.zeros([2, 3])))
    print("np.ones([2, 3]) =\n{}".format(np.ones([2, 3])))
    print("np.zeros_like(x) =\n{}".format(np.zeros_like(x)))
    print("np.ones_like(x) =\n{}".format(np.ones_like(x)))
    print("eye(3) =\n{}".format(np.eye(3)))

    x = np.array([0, 1, 2], dtype='float32')

main()


