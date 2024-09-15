#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pathlib
import tt_util as ut


def f_test_expand():
    print(os.path.expandvars("~/WinHome"))
    print(os.path.expanduser("~/WinHome"))
    print(os.path.expandvars("$HOME"))
    print(os.path.expandvars("$MY_ETC/tmp"))
    print(os.path.expandvars("${MY_ETC}/tmp"))
    print(os.path.expandvars("$MY_NOENV/tmp"))
    print(os.environ["HOME"])


def f_test_pathlib():
    p = os.path.expandvars("$HOME/WinHome")
    p = os.path.realpath(p)
    print(p)

    wp = pathlib.PureWindowsPath(p)
    print(f'PureWindowsPath: {wp}')
    print(f'as_posix(): {wp.as_posix()}')

    up = pathlib.PurePosixPath(p)
    print(f'PurePosixPath: {up}')


def f2():
    p = ut.expand_env("$HOME")
    print(f'ut.expand_env("$HOME"): {p}')
    up = ut.path_unix(p)
    print(f'up: {up}')

    fname = '$AAA_AAA/bb/cc/$DDD_DDD'
    #fname = re.sub('(\$[^/]*)', '\\1_WIN', fname)
    fname = re.sub('(\$\w+)', '\\1_WIN', fname)
    print(f'fname: {fname}')


def f3():
    p = 'C:/aa/bb/cc/dd.txt'
    print(f'ut.path_unix(p): {ut.path_unix(p, "/mnt")}')
    p = '$aa/bb/cc/dd.txt'
    print(f'ut.path_unix(p): {ut.path_unix(p, "/mnt")}')


f_test_expand()
f_test_pathlib()
#f2()
#f3()

