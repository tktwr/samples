#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import parse
from common import f_title


# *memo_py.string*
# *memo_py.string.split*
# *memo_py.string.strip*
# *memo_py.string.replace*
# *memo_py.string.join*
def f_string():
    f_title("f_string()")
    s = "abc," + "def,"
    s = s + str(100)
    print(f"s = {s}")
    l = s.split(",")
    print(f"l = {l}")

    s = f"images/img{123}_{5}.png"
    print(f"s: {s}")
    print(f"s[0]: {s[0]}")
    print(f"s[-1]: {s[-1]}")
    print(f"s[0:4]: {s[0:4]}")
    print(f"s[1:4]: {s[1:4]}")
    print(f"s.split('/'): {s.split('/')}")
    print(f"s.replace('/', '-'): {s.replace('/', '-')}")

    dirname, filename = s.split("/")
    print(f"dirname: {dirname}")
    print(f"filename: {filename}")

    s = "/".join(["aaa", "bbb", "ccc"])
    print(f"s: {s}")
    s = "  aaa 123  ".strip()
    print(f"s: [{s}]")


# *memo_py.re*
def f_re():
    f_title("f_re()")
    in_s = "1, 1.5, 2, 2.5:str"
    out_s = re.split(r",\s+|:", in_s)
    print(f"in_s: {in_s}")
    print(f"out_s: {out_s}")


# *memo_py.parse*
def f_parse():
    f_title("f_parse()")
    filename = "img123_5.png"
    result = parse.parse("img{nr:d}_{label:d}.png", filename)
    print(f"nr, label: {result['nr']}, {result['label']}")

    in_s = "123 str1 str2 12.34"
    out_s = parse.parse("{:d} str1 {:w} {:f}", in_s)
    print(f"in_s: {in_s}")
    print(f"out_s: {out_s}")
    print(f"out_s[0]: {out_s[0]}")

    in_s = "123 str1 str2 12.34"
    out_s = parse.parse("{var1:d} str1 {:w} {var2}", in_s)
    print(f"in_s: {in_s}")
    print(f"out_s: {out_s}")
    print(f"out_s['var1']: {out_s['var1']}")
    print(f"out_s['var2']: {out_s['var2']}")
    print(f"out_s[0]: {out_s[0]}")


def main(argv):
    f_string()
    f_re()
    f_parse()


if __name__ == "__main__":
    main(sys.argv)
