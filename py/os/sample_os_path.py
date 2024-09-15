#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:os_path*

import os
import tt_util as ut


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


def f_FileName():
    path = '~/MyConfig/a.txt'
    fn = ut.FileName(path)

    print(f'origname = {fn.origname()}')
    print(f'dirname  = {fn.dirname()}')
    print(f'dirname  = {fn.dirname(expand=True)}')
    print(f'dirname  = {fn.dirname(expand=True, realpath=True)}')
    print(f'filename = {fn.filename()}')
    print(f'name     = {fn.name()}')
    print(f'ext      = {fn.ext()}')


if __name__ == '__main__':
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')
