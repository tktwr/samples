#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.text_io*

import sys


# *memo_py.text_io.read_text*
def f_read_text(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    return lines


# *memo_py.text_io.write_text*
def f_write_text(fname, lines):
    with open(fname, "w") as f:
        for i in lines:
            f.write(i)


def main(argv):
    ifname = "data/sample.txt"
    ofname = "_output/text_io.txt"

    lines = f_read_text(ifname)
    print(lines)
    f_write_text(ofname, lines)


if __name__ == "__main__":
    main(sys.argv)
