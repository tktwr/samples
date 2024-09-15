#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:os*

import os


def f_system():
    os.system('ls -l')  # deprecated


def f_environ():
    dir_name = os.environ['HOME']
    print(f"dir_name: {dir_name}")


