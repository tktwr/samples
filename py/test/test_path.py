#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import re
import tt_util as tu
import pprint


def f_test_expand():
    print(os.path.expandvars("~/WinHome"))
    print(os.path.expanduser("~/WinHome"))
    print(os.path.expandvars("$HOME"))
    print(os.path.expandvars("$MY_ETC/tmp"))
    print(os.path.expandvars("${MY_ETC}/tmp"))
    print(os.path.expandvars("$MY_NOENV/tmp"))
    print(os.environ["HOME"])


def f_path():
    print(f'{tu.path_unix(tu.expand_env("$HOME"))}')
    print(f'{tu.path_unix(tu.expand_env("$MY_DATA"))}')

    print(f'{tu.path_windows(tu.expand_env("$HOME"))}')
    print(f'{tu.path_windows(tu.expand_env("$MY_DATA"))}')


def test_path2():
    p = tu.expand_env("$HOME")
    print(f'tu.expand_env("$HOME"): {p}')
    up = tu.path_unix(p)
    print(f'up: {up}')

    fname = '$AAA_AAA/bb/cc/$DDD_DDD'
    #fname = re.sub('(\$[^/]*)', '\\1_WIN', fname)
    fname = re.sub('(\$\w+)', '\\1_WIN', fname)
    print(f'fname: {fname}')


def test_path3():
    p = 'C:/aa/bb/cc/dd.txt'
    print(f'tu.path_unix(p): {tu.path_unix(p, "/mnt")}')
    p = '$aa/bb/cc/dd.txt'
    print(f'tu.path_unix(p): {tu.path_unix(p, "/mnt")}')


def _f_test_path(fname, prefix):
    print('--- test_path ---')
    fname_unix = tu.path_unix(fname, prefix)
    fname_mix  = tu.path_mixed(fname, prefix)
    fname_win  = tu.path_windows(fname, prefix)
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
    print(f'fname: {tu.path_unix(fname)}')


if __name__ == '__main__':
    func_lst = tu.get_all_funcs(globals().keys())
    for func in func_lst:
        tu.log_title(f' [{func}] ')
        eval(f'{func}()')
