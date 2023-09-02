#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tt_util as ut


# *sample:py.syntax.list*
def f_list():
    lst = [0, 1, 2, 3, 4, 5]

    print(f'lst                    = {lst}')
    print(f'len(lst)               = {len(lst)}')
    print(f'lst[0]                 = {lst[0]}')
    print(f'lst[5]                 = {lst[5]}')
    print(f't                      = {tuple(lst)}')
    lst.append(10)
    print(f'lst.append(10)         = {lst}')
    lst.extend([100, 101])
    print(f'lst.extend([100, 101]) = {lst}')
    lst.insert(0, 20)
    print(f'lst.insert(0, 20)      = {lst}')
    lst.pop(2)
    print(f'lst.pop(2)             = {lst}')


# *sample:py.syntax.list_op*
def f_list_op():
    lst1 = [1] * 2
    lst2 = [2] * 3
    lst = lst1 + lst2
    print(f'lst      = {lst}')


# *sample:py.syntax.list.slice*
def f_list_slice():
    lst = ['zero', 1, 'two', 3, 'four', 5]
    print(f'lst        = {lst}')
    print(f'lst[:]     = {lst[:]}')     # all
    print(f'lst[0:]    = {lst[0:]}')    # from 0
    print(f'lst[1:]    = {lst[1:]}')    # from 1
    print(f'lst[:6]    = {lst[:6]}')    # before 6
    print(f'lst[:2]    = {lst[:2]}')    # before 2
    print(f'lst[2:4]   = {lst[2:4]}')   # from 2 to 4
    print(f'lst[:-1]   = {lst[:-1]}')   # before last
    print(f'lst[:-2]   = {lst[:-2]}')
    print(f'lst[-2:-1] = {lst[-2:-1]}')
    print(f'lst[-1:]   = {lst[-1:]}')   # the last


# -----------------------------------------------------
def f_list_s2l():
    s = '0 1 2 3 4 5'
    l = s.split(' ')

    print(f's = {s}')
    print(f'l = {l}')


def f_list_s2i():
    slst = ['0', '1', '2', '3', '4', '5']
    ilst = [int(i) for i in slst]
    print(f'slst = {slst}')
    print(f'ilst = {ilst}')


