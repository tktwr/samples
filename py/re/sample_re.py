#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re


def _f_expand_env(s):
    r = re.search(r'\$\w+', s)
    if r is not None:
        matched = r.group()
        env_var = matched[1:]
        if os.getenv(env_var) is not None:
            s = s.replace(matched, os.environ[env_var])
    return s


# *memo:sample:py.re*
def f_re():
    in_s = '1, 1.5, 2, 2.5:str'
    out_s = re.split(r',\s+|:', in_s)
    print(f'in_s: {in_s}')
    print(f'out_s: {out_s}')

    s = '$USERPROFILE/tmp'
    # s = '$USERPROFILE'
    # s = '/a/b/c'
    r = re.search(r'\$\w+', s)
    if r is not None:
        print(f'r: {r}')
        print(f'r.group(): {r.group()}')
        print(f'r.start(): {r.start()}')
        print(f'r.end(): {r.end()}')
        print(f'r.span(): {r.span()}')

    o = _f_expand_env(s)
    print(f'o: {o}')


# *memo:sample:py.re.sub*
def f_re_sub():
    s = ' aa bb  cc    dd  '
    o = re.sub(r'\s+', ' ', s)
    print(f's: [{s}]')
    print(f'o: [{o}]')


