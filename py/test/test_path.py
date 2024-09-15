#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tt_util as ut
import pprint


def _f_test_path(fname, prefix):
    print('--- test_path ---')
    fname_unix = ut.path_unix(fname, prefix)
    fname_mix  = ut.path_mixed(fname, prefix)
    fname_win  = ut.path_windows(fname, prefix)
    print(f'orig : {fname}')
    print(f'unix : {fname_unix}')
    print(f'mix  : {fname_mix}')
    print(f'win  : {fname_win}')


def f_test_path_all():
    pprint.pprint(sys.path)
    _f_test_path(*['D:/aa\\bb/cc.txt', '/mnt'])
    _f_test_path(*['/d/aa\\bb/cc.txt', '/mnt'])
    _f_test_path(*['/mnt/d/aa\\bb/mnt/cc.txt', '/mnt'])


def f_test_realpath():
    fname = os.path.expandvars('$HOME/WinHome')
    print(f'fname: {fname}')

    if os.path.islink(fname):
        print(f'symlink')
        fname = os.path.realpath(fname)

    print(f'fname: {fname}')
    print(f'fname: {ut.path_unix(fname)}')


if __name__ == '__main__':
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')
