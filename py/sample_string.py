#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tt_util as ut


# *sample:py.string*
def f_string():
    s = 'hello world'

    print(f's      = {s}')
    print(f's[0]   = {s[0]}')
    print(f's[-1]  = {s[-1]}')
    print(f's[0:4] = {s[0:4]}')
    print(f's[1:4] = {s[1:4]}')


# *sample:py.string.fstring*
def f_fstring():
    # f-string (python >= 3.6)
    ival = 2
    fval = 1 / 3
    word = "hello"
    width = 10

    print(f"1+1         = {1+1}")
    print(f"1+0.5       = {1+0.5}")
    print(f"ival        = {ival}")
    print(f"ival:3d     = {ival:3d}")
    print(f"ival:03d    = {ival:03d}")
    print(f"ival**10:,d = {ival**10:,d}")
    print(f"fval        = {fval}")
    print(f"fval:.3f    = {fval:.3f}")
    print(f"word:<10s   = [{word:<{width}s}]")
    print(f"word:^10s   = [{word:^{width}s}]")
    print(f"word:>10s   = [{word:>{width}s}]")
    print(f"word        = ", end='')
    print(word)


# *sample:py.string.if*
def f_if():
    s = 'hello'
    if s == 'hello':
        print('hello')
    if s != 'world':
        print('!world')


# *sample:py.string.with*
def f_with():
    s = 'hello'
    if s.startswith('he'):
        print('he')
    if s.endswith('o'):
        print('o')


# *sample:py.string.in*
def f_in():
    s = 'hello'
    if 'el' in s:
        print('el')
    if 'aa' not in s:
        print('!aa')


# *sample:py.string.strip*
def f_strip():
    s = '  aaa 123  '
    print(f's = "{s}"')
    s = s.strip()
    print(f's = "{s}"')


# *sample:py.string.replace*
def f_replace():
    s = f'images/img123_5.png'
    print(f's = {s}')
    s = s.replace('_', '-')
    print(f's = {s}')


# *sample:py.string.split*
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


# *sample:py.string.join*
def f_join():
    lst = ['aaa', 'bbb', 'ccc']
    print(f'lst = {lst}')
    s = '/'.join(lst)
    print(f's = {s}')


