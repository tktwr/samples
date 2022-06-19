#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.json*

import sys
import json


# *memo_py.json.read_json*
def f_read_json(fname):
    with open(fname, "r") as f:
        json_data = json.load(f)
    return json_data


# *memo_py.json.write_json*
def f_write_json(fname, data):
    with open(fname, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4))


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
