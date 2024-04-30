#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tt_util as ut


# *memo:sample:py.os.path*
def f_path():
    path       = '~/Desktop/a.txt'
    expanduser = os.path.expanduser(path)
    abspath    = os.path.abspath(expanduser)
    dirname    = os.path.dirname(abspath)
    basename   = os.path.basename(abspath)
    splittxt   = os.path.splitext(basename)
    join       = os.path.join('a', 'b', 'c.txt')

    print(f'path       = {path}')
    print(f'expanduser = {expanduser}')
    print(f'abspath    = {abspath}')
    print(f'dirname    = {dirname}')
    print(f'basename   = {basename}')
    print(f'splitext   = {splittxt}')
    print(f'join       = {join}')


# *memo:sample:py.os.path.test*
def f_path_test():
    file = '/etc/hosts'
    dir = '/etc'

    print(f'isfile(file) : {os.path.isfile(file)}')
    print(f'isdir(dir)   : {os.path.isdir(dir)}')


