#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import parse
import util as ut


# *memo_py.string*
def f_string():
    s = "hello world"
    print(f"s                   = {s}")
    print(f"s[0]                = {s[0]}")
    print(f"s[-1]               = {s[-1]}")
    print(f"s[0:4]              = {s[0:4]}")
    print(f"s[1:4]              = {s[1:4]}")

    # *memo_py.string.if*
    s = "hello"
    if s == "hello":
        print("hello")
    if s != "world":
        print("!world")
    if s.startswith('he'):
        print(s)
    if s.endswith('o'):
        print(s)
    if "el" in s:
        print("el")
    if 'eo' in s:
        print("eo")
    if "aa" not in s:
        print("!aa")

    # *memo_py.string.strip*
    s = "  aaa 123  "
    print(f's            = "{s}"')
    print(f's.strip()    = "{s.strip()}"')

    # *memo_py.string.split*
    s = "abc," + "def," + str(100)
    print(f"s            = {s}")
    print(f's.split(",") = {s.split(",")}')


# *memo_py.filename*
def f_filename():
    s = f"images/img123_5.png"

    print(f"s                   = {s}")

    # *memo_py.filename.split*
    dirname, filename = s.split("/")
    print(f"dirname             = {dirname}")
    print(f"filename            = {filename}")

    # *memo_py.filename.replace*
    print(f"s.replace('_', '-') = {s.replace('_', '-')}")

    # *memo_py.filename.join*
    l = ["aaa", "bbb", "ccc"]
    print(f"l            = {l}")
    print(f'"/".join(l)  = {"/".join(l)}')


def f_expand_env(s):
    r = re.search('\$\w+', s)
    if r != None:
        matched = r.group()
        env_var = matched[1:]
        if os.getenv(env_var) != None:
            s = s.replace(matched, os.environ[env_var])
    return s


# *memo_py.re*
def f_re():
    in_s = "1, 1.5, 2, 2.5:str"
    out_s = re.split(r",\s+|:", in_s)
    print(f"in_s: {in_s}")
    print(f"out_s: {out_s}")

    s = "$USERPROFILE/tmp"
    #s = "$USERPROFILE"
    #s = "/a/b/c"
    r = re.search('\$\w+', s)
    if r != None:
        print(f"r: {r}")
        print(f"r.group(): {r.group()}")
        print(f"r.start(): {r.start()}")
        print(f"r.end(): {r.end()}")
        print(f"r.span(): {r.span()}")

    o = f_expand_env(s)
    print(f"o: {o}")


# *memo_py.parse*
def f_parse():
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
    funcs = (
            "f_string",
            "f_filename",
            "f_re",
            "f_parse",
            )

    if len(argv) == 1:
        selected = funcs
    else:
        selected = argv[1:]

    for i in selected:
        ut.f_title(i)
        eval(f"{i}()")


if __name__ == "__main__":
    main(sys.argv)
