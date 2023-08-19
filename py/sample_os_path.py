#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tt_util as ut


# *sample:py.os.path*
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


# *sample:py.os.path.test*
def f_path_test():
    file = '/etc/hosts'
    dir = '/etc'

    print(f'isfile(file) : {os.path.isfile(file)}')
    print(f'isdir(dir)   : {os.path.isdir(dir)}')


if __name__ == '__main__':
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')
