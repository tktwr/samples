#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pathlib
import tt_path_util as ttp


def f1():
    p = os.path.expandvars("$HOME")
    print(f'$HOME: {p}')
    wp = pathlib.PureWindowsPath(p)
    print(f'PureWindowsPath: {wp}')
    print(f'as_posix(): {wp.as_posix()}')
    up = pathlib.PurePosixPath(p)
    print(f'PurePosixPath: {up}')

    print(f'os.environ["HOME"]: {os.environ["HOME"]}')


def f2():
    p = ttp.expand_env("$HOME")
    print(f'ttp.expand_env("$HOME"): {p}')
    up = ttp.path_unix(p)
    print(f'up: {up}')

    fname = '$AAA_AAA/bb/cc/$DDD_DDD'
    #fname = re.sub('(\$[^/]*)', '\\1_WIN', fname)
    fname = re.sub('(\$\w+)', '\\1_WIN', fname)
    print(f'fname: {fname}')


def f3():
    p = 'C:/aa/bb/cc/dd.txt'
    print(f'ttp.path_unix(p): {ttp.path_unix(p, "/mnt")}')
    p = '$aa/bb/cc/dd.txt'
    print(f'ttp.path_unix(p): {ttp.path_unix(p, "/mnt")}')


#f1()
#f2()
f3()

