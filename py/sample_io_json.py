#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json


def f_read_json_file(fname):
    with open(fname, 'r') as f:
        return json.load(f)


def f_write_json_file(fname, data):
    with open(fname, 'w') as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    fname = '_output/io_json.json'

    data = [1, 2, 3, 4]
    data = {'aa': 1, 'bb': 2}

    f_write_json_file(fname, data)
    data2 = f_read_json_file(fname)
    print(data2)
