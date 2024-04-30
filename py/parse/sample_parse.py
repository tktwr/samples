#!/usr/bin/env python
# -*- coding: utf-8 -*-

import parse


# *memo:sample:py.parse*
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


