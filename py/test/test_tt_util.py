#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tt_util as tu


O_DIR = '_output'


def f_io_text():
    lines = tu.read_text('input.txt')
    tu.write_text(f'{O_DIR}/output.txt', lines)


def f_io_json():
    json_data = tu.read_json('input.json')
    tu.write_json(f'{O_DIR}/output.json', json_data)


def f_filename():
    FN = tu.FileName("a/b/c/d.png")

    print(f"FN.origname() = {FN.origname()}")
    print(f"FN.dirname()  = {FN.dirname()}")
    print(f"FN.filename() = {FN.filename()}")
    print(f"FN.name()     = {FN.name()}")
    print(f"FN.ext()      = {FN.ext()}")

    print(f'{tu.path_unix(tu.expand_env("$HOME"))}')
    print(f'{tu.path_unix(tu.expand_env("$MY_DATA"))}')

    print(f'{tu.path_windows(tu.expand_env("$HOME"))}')
    print(f'{tu.path_windows(tu.expand_env("$MY_DATA"))}')


def f_search():
    s = '/a/$MY_DATA/a/b'
    #s = '$HOME/a/b'
    r = re.search('^\$MY_', s)
    print(r)

