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


def f_search():
    s = '/a/$MY_DATA/a/b'
    #s = '$HOME/a/b'
    r = re.search('^\$MY_', s)
    print(r)


