#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import parse
import tt_util as ut


# *sample:py.string*
def f_string():
    s = 'hello world'

    print(f's      = {s}')
    print(f's[0]   = {s[0]}')
    print(f's[-1]  = {s[-1]}')
    print(f's[0:4] = {s[0:4]}')
    print(f's[1:4] = {s[1:4]}')


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


def _f_expand_env(s):
    r = re.search(r'\$\w+', s)
    if r is not None:
        matched = r.group()
        env_var = matched[1:]
        if os.getenv(env_var) is not None:
            s = s.replace(matched, os.environ[env_var])
    return s


# *sample:py.string.re*
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


# *sample:py.string.re.sub*
def f_re_sub():
    s = ' aa bb  cc    dd  '
    o = re.sub(r'\s+', ' ', s)
    print(f's: [{s}]')
    print(f'o: [{o}]')


# *sample:py.string.parse*
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


