#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


# *memo:sample:py.syntax.print_format*
def f_print_format():
    # str.format() method (python >= 2.6)
    print("{} {} {}".format(0, 1, 2))
    print("{0} {1} {2}".format(0, 1, 2))
    print("{2} {2} {2}".format(0, 1, 2))


# -----------------------------------------------------
# *memo:sample:py.syntax.print_operator*
def f_print_operator():
    # % operator (old)
    print("%d " % 0)
    print("%d %d %d" % (0, 1, 2))


