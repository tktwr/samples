#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py.path*

import re


s1 = 'C:/aaa/bbb/{ID}.png'
s2 = 'C:\\\\aaa\\\\bbb\\\\{ID}.png'
s3 = 'C:\\aaa\\bbb\\{ID}.png'
s4 = r'C:\aaa\bbb\{ID}.png'
ID = 1234

def f_path_conv_to_slash(s):
    s = s.replace('\\', '/')
    s = re.sub(r'/+', '/', s)
    return s


def f_fstring_expand(s, ID):
    print(f'{s}')
    print(f"f'{s}'")
    return eval(f"f'{s}'")


def f_test_fstring_expand():
    print('---')
    print(f_fstring_expand(s1, ID))
    print('---')
    print(f_fstring_expand(s2, ID))
    print('---')
    print(s1.replace('{ID}', str(ID)))
    print(s2.replace('{ID}', str(ID)))
    print(s3.replace('{ID}', str(ID)))
    print(s4.replace('{ID}', str(ID)))
    print('---')
    print(s2.replace('\\', '/'))
    print(s3.replace('\\', '/'))
    print(s4.replace('\\', '/'))
    print('---')
    print(s1.replace('/', '\\'))
    print(s1.replace('/', '\\\\'))

def f_test_path_slash():
    print('---')
    print(f_path_conv_to_slash(s1))
    print(f_path_conv_to_slash(s2))
    print(f_path_conv_to_slash(s3))
    print(f_path_conv_to_slash(s4))

f_test_fstring_expand()
f_test_path_slash()
