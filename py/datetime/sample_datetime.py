#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime as dt


# *memo:sample:py.os.today*
def f_today():
    today      = dt.today()
    time_stamp = dt.now().strftime("%Y%m%d-%H%M%S")

    print(f'today      = {today}')
    print(f'time_stamp = {time_stamp}')


