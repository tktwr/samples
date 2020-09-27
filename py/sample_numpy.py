#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.numpy*

import sys
import numpy as np


def main(argv):
    x = np.array([0, 1, 2])
    print(f"x =\n{x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size = {x.size}")

    x = np.array([0, 1, 2], dtype='float32')
    print(f"x =\n{x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size = {x.size}")

    x = np.array([[0, 1, 2],
                  [3, 4, 5]])
    print(f"x =\n{x}")
    print(f"x.dtype = {x.dtype}")
    print(f"x.shape = {x.shape}")
    print(f"x.size = {x.size}")

    print(f"np.empty([2, 3]) =\n{np.empty([2, 3])}")
    print(f"np.zeros([2, 3]) =\n{np.zeros([2, 3])}")
    print(f"np.ones([2, 3]) =\n{np.ones([2, 3])}")
    print(f"np.zeros_like(x) =\n{np.zeros_like(x)}")
    print(f"np.ones_like(x) =\n{np.ones_like(x)}")
    print(f"eye(3) =\n{np.eye(3)}")

    x = np.array([0, 1, 2])
    print(f"x =\n{x}")
    y = np.append(x, [3, 4, 5])
    print(f"y =\n{y}")
    z = y.reshape(2, -1)
    print(f"z =\n{z}")


if __name__ == "__main__":
    main(sys.argv)
