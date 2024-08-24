#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func1(val):
    print(f'{val+val}')


def eval_cmd(cmd):
    print(cmd)
    eval(cmd)


if __name__ == '__main__':
    val = 10
    cmd = f'func1({val})'
    eval_cmd(cmd)
