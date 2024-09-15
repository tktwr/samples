#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


# *memo:sample:py.sys*
def f_sys():
    print(sys.argv)

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    for i in sys.path:
        print(i)

f_sys()
