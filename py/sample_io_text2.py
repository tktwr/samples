#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f_read_text_file2(fname):
    f = open(fname, 'r')
    lines = []
    for line in f:
        lines.append(line)
    f.close()
    return lines


def f_write_text_file2(fname, lines):
    f = open(fname, 'w')
    for i in lines:
        f.write(i)
    f.close()


if __name__ == '__main__':
    ifname = 'data/sample.txt'
    ofname = '_output/io_text2.txt'

    lines = f_read_text_file2(ifname)
    print(lines)
    f_write_text_file2(ofname, lines)

