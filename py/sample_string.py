#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import parse
import util as ut


# *memo_py.string*
def f_string():
    s = 'hello world'
    print(f's                   = {s}')
    print(f's[0]                = {s[0]}')
    print(f's[-1]               = {s[-1]}')
    print(f's[0:4]              = {s[0:4]}')
    print(f's[1:4]              = {s[1:4]}')


# *memo_py.string.if*
def f_if():
    s = 'hello'
    if s == 'hello':
        print('hello')
    if s != 'world':
        print('!world')


# *memo_py.string.with*
def f_with():
    s = 'hello'
    if s.startswith('he'):
        print('he')
    if s.endswith('o'):
        print('o')


# *memo_py.string.in*
def f_in():
    s = 'hello'
    if 'el' in s:
        print('el')
    if 'aa' not in s:
        print('!aa')


# *memo_py.string.strip*
def f_strip():
    s = '  aaa 123  '
    print(f's = "{s}"')
    s = s.strip()
    print(f's = "{s}"')


# *memo_py.string.replace*
def f_replace():
    s = f'images/img123_5.png'
    print(f's = {s}')
    s = s.replace('_', '-')
    print(f's = {s}')


# *memo_py.string.split*
def f_split():
    s = 'abc,' + 'def,' + str(100)
    print(f's = {s}')
    lst = s.split(',')
    print(f'lst = {lst}')

    s = f'images/img123_5.png'
    print(f's = {s}')
    dirname, filename = s.split('/')
    print(f'dirname  = {dirname}')
    print(f'filename = {filename}')


# *memo_py.string.join*
def f_join():
    lst = ['aaa', 'bbb', 'ccc']
    print(f'lst = {lst}')
    s = '/'.join(lst)
    print(f's = {s}')


def f_expand_env(s):
    r = re.search(r'\$\w+', s)
    if r is not None:
        matched = r.group()
        env_var = matched[1:]
        if os.getenv(env_var) is not None:
            s = s.replace(matched, os.environ[env_var])
    return s


# *memo_py.string.re*
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

    o = f_expand_env(s)
    print(f'o: {o}')


# *memo_py.string.parse*
def f_parse():
    filename = 'img123_5.png'
    result = parse.parse('img{nr:d}_{label:d}.png', filename)
    print(f'nr, label: {result["nr"]}, {result["label"]}')

    in_s = '123 str1 str2 12.34'
    out_s = parse.parse('{:d} str1 {:w} {:f}', in_s)
    print(f'in_s: {in_s}')
    print(f'out_s: {out_s}')
    print(f'out_s[0]: {out_s[0]}')

    in_s = '123 str1 str2 12.34'
    out_s = parse.parse('{var1:d} str1 {:w} {var2}', in_s)
    print(f'in_s: {in_s}')
    print(f'out_s: {out_s}')
    print(f'out_s["var1"]: {out_s["var1"]}')
    print(f'out_s["var2"]: {out_s["var2"]}')
    print(f'out_s[0]: {out_s[0]}')


def main(argv):
    funcs = ('f_string',
             'f_if',
             'f_with',
             'f_in',
             'f_strip',
             'f_replace',
             'f_split',
             'f_join',
             'f_re',
             'f_parse',
             )

    if len(argv) == 1:
        selected = funcs
    else:
        selected = argv[1:]

    for i in selected:
        ut.f_title(i)
        eval(f'{i}()')


if __name__ == '__main__':
    main(sys.argv)
