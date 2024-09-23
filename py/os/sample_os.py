#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:os*

import os
import sys


def f_os_system():
    os.system('ls -l')  # deprecated


def f_os_environ():
    dir_name = os.environ['HOME']
    print(f"dir_name: {dir_name}")


def f_sys_argv():
    print(sys.argv)


def f_sys_path():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    for i in sys.path:
        print(i)


f_os_system()
f_os_environ()
f_sys_argv()
f_sys_path()
