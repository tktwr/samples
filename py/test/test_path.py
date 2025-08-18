#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import re
import tt_util as tu


def f_test_expand():
    print(os.path.expandvars("~/WinHome"))
    print(os.path.expanduser("~/WinHome"))
    print(os.path.expandvars("$HOME"))
    print(os.path.expandvars("$MY_ETC/tmp"))
    print(os.path.expandvars("${MY_ETC}/tmp"))
    print(os.path.expandvars("$MY_NOENV/tmp"))
    print(os.environ["HOME"])


def test_path2():
    fname = '$AAA_AAA/bb/cc/$DDD_DDD'
    #fname = re.sub('(\$[^/]*)', '\\1_WIN', fname)
    fname = re.sub('(\$\w+)', '\\1_WIN', fname)
    print(f'fname: {fname}')


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
