#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py.os*

import os


# *memo:sample:py.os.system*
def f_system():
    os.system('ls -l')  # deprecated


# *memo:sample:py.os.environ*
def f_environ():
    dir_name = os.environ['HOME']
    print(f"dir_name: {dir_name}")


