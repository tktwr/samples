#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *sample:py.os*

import sys
import os
import glob
from datetime import datetime as dt
import tt_util as ut


# *sample:py.os.system*
def f_system():
    os.system('ls -l')  # deprecated


# *sample:py.os.glob*
def f_glob():
    files = glob.glob('*.txt')
    print(f"files = {files}")


# *sample:py.os.environ*
def f_environ():
    dir_name = os.environ['HOME']
    print(f"dir_name: {dir_name}")


# *sample:py.os.today*
def f_today():
    today      = dt.today()
    time_stamp = dt.now().strftime("%Y%m%d-%H%M%S")

    print(f'today      = {today}')
    print(f'time_stamp = {time_stamp}')


# *sample:py.os.sys*
def f_sys():
    print(sys.argv)

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    for i in sys.path:
        print(i)


