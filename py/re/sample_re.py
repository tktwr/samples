#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:re*

import re
import tt_util as ut


def f_re_search():
    s = '$HOME/tmp'
    # s = '$USERPROFILE'
    # s = '/a/b/c'
    r = re.search(r'\$\w+', s)
    if r is not None:
        print(f'r: {r}')
        print(f'r.group(): {r.group()}')
        print(f'r.start(): {r.start()}')
        print(f'r.end(): {r.end()}')
        print(f'r.span(): {r.span()}')


def f_expand_env():
    istr = '$HOME/tmp'
    ostr = ut.expand_env(istr)
    print(f'istr: {istr}')
    print(f'ostr: {ostr}')


def f_re_sub():
    istr = ' aa bb  cc    dd  '
    ostr = re.sub(r'\s+', ' ', istr)
    ostr = ostr.strip()
    print(f'istr: "{istr}"')
    print(f'ostr: "{ostr}"')


def f_re_split():
    istr = '1, 1.5 ; 2,  2.5; str'
    olst = re.split(r',|;', istr)
    olst = [i.strip() for i in olst]
    print(f'istr: {istr}')
    print(f'olst: {olst}')


if __name__ == '__main__':
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')
