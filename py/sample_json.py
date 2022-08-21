#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.json*

import sys
import json


# *memo_py.json.read_json*
def f_read_json(fname):
    with open(fname, "r") as f:
        return json.load(f)


# *memo_py.json.write_json*
def f_write_json(fname, data):
    with open(fname, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


def f_read_json2(fname):
    f = open(fname, "r")
    json_data = json.load(f)
    print(json_data)
    f.close()
    return json_data


def f_write_json2(fname, data):
    f = open(fname, "w")
    f.write(json.dumps(data))
    f.close()


def main(argv):
    fname = "_output/out.json"

    data = [1, 2, 3, 4]
    data = {"a":1, "b":2}

    f_write_json(fname, data)
    data2 = f_read_json(fname)

    print(data2)
    print(data2["a"])
    print(data2["b"])


if __name__ == "__main__":
    main(sys.argv)
