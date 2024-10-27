#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pathlib


def f_test_pathlib():
    p = os.path.expandvars("$HOME/WinHome")
    p = os.path.realpath(p)
    print(p)

    wp = pathlib.PureWindowsPath(p)
    print(f'PureWindowsPath: {wp}')
    print(f'as_posix(): {wp.as_posix()}')

    up = pathlib.PurePosixPath(p)
    print(f'PurePosixPath: {up}')


f_test_pathlib()

