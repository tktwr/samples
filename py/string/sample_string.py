#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:string*


def f_sample_py_string():
    s = 'hello world'

    print(f's      = {s}')
    print(f's[0]   = {s[0]}')
    print(f's[-1]  = {s[-1]}')
    print(f's[0:4] = {s[0:4]}')
    print(f's[1:4] = {s[1:4]}')


def f_sample_py_string_if():
    s = 'hello'
    if s == 'hello':
        print('hello')
    if s != 'world':
        print('!world')


def f_sample_py_string_with():
    s = 'hello'
    if s.startswith('he'):
        print('he')
    if s.endswith('o'):
        print('o')


def f_sample_py_string_in():
    s = 'hello'
    if 'el' in s:
        print('el')
    if 'aa' not in s:
        print('!aa')


def f_sample_py_string_strip():
    s = '  aaa 123  '
    print(f's = "{s}"')
    s = s.strip()
    print(f's = "{s}"')


def f_sample_py_string_replace():
    s = f'images/img123_5.png'
    print(f's = {s}')
    s = s.replace('_', '-')
    print(f's = {s}')


def f_sample_py_string_split():
    s = 'abc,' + 'def,' + str(100)
    print(f's = {s}')
    lst = s.split(',')
    print(f'lst = {lst}')

    s = f'images/img123_5.png'
    print(f's = {s}')
    dirname, filename = s.split('/')
    print(f'dirname  = {dirname}')
    print(f'filename = {filename}')


def f_sample_py_string_join():
    lst = ['aaa', 'bbb', 'ccc']
    print(f'lst = {lst}')
    s = '/'.join(lst)
    print(f's = {s}')


