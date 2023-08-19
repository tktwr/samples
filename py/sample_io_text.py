#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f_read_text_file(fname):
    with open(fname, 'r') as f:
        return f.readlines()


def f_write_text_file(fname, lines):
    with open(fname, 'w') as f:
        for i in lines:
            f.write(i)


if __name__ == '__main__':
    ifname = 'data/sample.txt'
    ofname = '_output/io_text.txt'

    lines = f_read_text_file(ifname)
    print(lines)
    f_write_text_file(ofname, lines)
