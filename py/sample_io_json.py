#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def f_read_json_file(fname):
    with open(fname, 'r') as f:
        return json.load(f)


def f_write_json_file(fname, data):
    with open(fname, 'w') as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))
        f.write('\n')


if __name__ == '__main__':
    fname = '_output/io_json.json'
    d = {'aa': 1, 'bb': 2}

    f_write_json_file(fname, d)
    d = f_read_json_file(fname)
    print(f'{d} {type(d)}')
