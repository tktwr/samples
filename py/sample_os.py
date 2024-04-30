#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py.os*

import sys
import os
from datetime import datetime as dt
import tt_util as ut


# *memo:sample:py.os.system*
def f_system():
    os.system('ls -l')  # deprecated


# *memo:sample:py.os.environ*
def f_environ():
    dir_name = os.environ['HOME']
    print(f"dir_name: {dir_name}")


# *memo:sample:py.os.today*
def f_today():
    today      = dt.today()
    time_stamp = dt.now().strftime("%Y%m%d-%H%M%S")

    print(f'today      = {today}')
    print(f'time_stamp = {time_stamp}')


