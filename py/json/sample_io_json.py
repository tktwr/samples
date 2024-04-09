#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def f_read_json_file(fname):
    try:
        with open(fname, 'r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except Exception as e:
        print(f"Exception: {e}")


def f_write_json_file(fname, data):
    try:
        with open(fname, 'w') as f:
            f.write(json.dumps(data, sort_keys=True, indent=4))
            f.write('\n')
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == '__main__':
    fname = '_output/io_json.json'
    d = {'aa': 1, 'bb': 2}

    f_write_json_file(fname, d)
    d = f_read_json_file(fname)
    print(f'{d} {type(d)}')

    fname = '/io_json.json'
    f_write_json_file(fname, d)
    d = f_read_json_file(fname)
