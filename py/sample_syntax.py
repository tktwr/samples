#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.syntax*

import sys
import my
import modules.mymodule as mymod
from common import f_title


# *memo_py.syntax.input*
def f_input():
    f_title("f_input()")
    print("input:")
    in_s = input()
    print("in_s: {in_s}")


# *memo_py.syntax.print*
def f_print():
    f_title("f_print()")
    # comment
    '''
    comment
    '''

    print("Hello")
    print("こんにちは")

    # f-string (python >= 3.6)
    a = 123
    print(f"a: {a}")
    print(f"1+1: {1+1}")
    print(f"1/3: {1/3:.3f}")

    # str.format() method (python >= 2.6)
    print("{} {} {}".format(0, 1, 2))
    print("{0} {1} {2}".format(0, 1, 2))
    print("{2} {2} {2}".format(0, 1, 2))

    # % operator
    print("%d %d %d" % (0, 1, 2))
    print("%d " % 3, end="")
    print("%d " % 4, end="")
    print("%d " % 5, end="")
    print()

    # encoding
    print(f"sys.stdin.encoding: {sys.stdin.encoding}")
    print(f"sys.stdout.encoding: {sys.stdout.encoding}")
    print(f"sys.stderr.encoding: {sys.stderr.encoding}")


# *memo_py.syntax.if*
def f_if():
    f_title("f_if()")
    for i in (0, 1, 2, 3, 4, 5, 9):
        if i == 0:
            print("i == 0")
        elif i == 1:
            print("i == 1")
        elif i == 2 or i == 3:
            print("i == 2 or i == 3")
        elif 4 <= i <= 5:
            print("4 <= i <= 5")
        else:
            print("i == other")


# *memo_py.syntax.while*
def f_while():
    f_title("f_while()")
    i = 0
    while i < 5:
        print(f"{i} ", end="")
        i += 1
    print()


# *memo_py.syntax.for*
def f_for():
    f_title("f_for()")
    for i in range(0, 5, 1):
        print(f"{i} ", end="")
    print()

    for i in range(0, 5):
        print(f"{i} ", end="")
    print()

    for i in range(5):
        print(f"{i} ", end="")
    print()

    list = [1, 3, 5, 7, 9]
    for i in list:
        print(f"{i} ", end="")
    print()


def f_add(a, b):
    return a + b


def f_args(a, b):
    print(f"a, b: {a} {b}")


# *memo_py.syntax.func*
def f_func():
    f_title("f_func()")
    x = f_add(1, 2)
    print(f"x: {x}")
    f_args(1, 2)
    f_args(2, 1)
    f_args(b=2, a=1)


# *memo_py.syntax.class*
def f_class():
    f_title("f_class()")
    my1 = my.MyClass(10)
    my2 = my.MyClass(20)
    sub1 = my.MySubClass(100)

    print(my.MyClass.n)
    my.MyClass.f("class method")
    print(my1.x)
    print(my2.x)
    print(my1.add(1))
    print(sub1.g())

    a1 = mymod.MyClassA(123)
    print(a1.x)


# *memo_py.syntax.list*
def f_list():
    f_title("f_list()")
    l = [1, 2, 3, 4, 5]
    print(f"l = {l}")
    print(f"len(l) = {len(l)}")
    print(f"l[0] = {l[0]}")
    l.append(10)
    print(f"l.append(10) = {l}")
    l.insert(0, 20)
    print(f"l.insert(0, 20) = {l}")
    l.pop(2)
    print(f"l.pop(2) = {l}")

    l = ['zero', 1, 'two', 3, 'four', 5]
    print(f"l       = {l}")
    print(f"l[:]    = {l[:]}")
    print(f"l[0:]   = {l[0:]}")
    print(f"l[2:4]  = {l[2:4]}")  # 2 + 2 chars
    print(f"l[:-1]  = {l[:-1]}")
    print(f"l[:-2]  = {l[:-2]}")
    print(f"l[-2:-1]= {l[-2:-1]}")
    print(f"l[-1:]  = {l[-1:]}")

    print(f"t = {tuple(l)}")

    s = "1 2 3 4 5"
    print(f"s = {s}")
    str_list = s.split(" ")
    print(f"str_list = {str_list}")
    int_list = list(int(i) for i in str_list)
    print(f"int_list = {int_list}")
    int_list = list(range(1, 6, 1))
    print(f"int_list = {int_list}")


# *memo_py.syntax.tuple*
def f_tuple():
    f_title("f_tuple()")
    # tuple is read only
    t = (1, 3, 5, 7, 9)
    print(f"t = {t}")
    t = (1, 'two', 3, 'four', 5)
    print(f"t = {t}")
    print(f"l = {list(t)}")


# *memo_py.syntax.dict*
def f_dict():
    f_title("f_dict()")
    d = {"a":1, "b":2}
    print(f"d = {d}")
    print(f"d['a'] = {d['a']}")


# *memo_py.syntax.type*
def f_type():
    f_title("f_type()")
    b = True
    b = False
    i = 0
    f = 0.0
    s = ""
    l = []
    t = ()
    d = {}
    i = int(1.23)
    f = float(1)
    s = str(1)
    l = list(t)
    t = tuple(l)


# *memo_py.syntax.string*
def f_string():
    f_title("f_string()")
    s = "abc," + "def,"
    s = s + str(100)
    print(f"s = {s}")
    l = s.split(",")
    print(f"l = {l}")

    import parse
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
    result = parse.parse("img{nr:d}_{label:d}.png", filename)
    print(f"nr, label: {result['nr']}, {result['label']}")


# *memo_py.syntax.re*
def f_re():
    f_title("f_re()")
    import re
    in_s = "1, 1.5, 2, 2.5:str"
    out_s = re.split(r",\s+|:", in_s)
    print(f"in_s: {in_s}")
    print(f"out_s: {out_s}")


# *memo_py.syntax.parse*
def f_parse():
    f_title("f_parse()")
    import parse
    in_s = "123 str1 str2 12.34"
    out_s = parse.parse("{:d} str1 {:w} {:f}", in_s)
    print(f"in_s: {in_s}")
    print(f"out_s: {out_s}")

    in_s = "123 str1 str2 12.34"
    out_s = parse.parse("{var1:d} str1 {:w} {var2}", in_s)
    print(f"in_s: {in_s}")
    print(f"out_s: {out_s}")
    print(f"out_s['var1']: {out_s['var1']}")
    print(f"out_s['var2']: {out_s['var2']}")
    print(f"out_s[0]: {out_s[0]}")


def f_other():
    f_title("f_other()")
    print(f" 5  / 2 = { 5  / 2}")
    print(f" 5 // 2 = { 5 // 2}")
    print(f" 5  / 3 = { 5  / 3}")
    print(f" 5 // 3 = { 5 // 3}")
    print(f"10  / 3 = {10  / 3}")
    print(f"10 // 3 = {10 // 3}")

    R, G, B = 0, 1, 2
    print(f"R, G, B: {R}, {G}, {B}")


def main(argv):
    print(f"argv: {argv}")
    for i in argv:
        if i == "input":
            f_input()
        if i == "all" or i == "print":
            f_print()
        if i == "all" or i == "if":
            f_if()
        if i == "all" or i == "while":
            f_while()
        if i == "all" or i == "for":
            f_for()
        if i == "all" or i == "func":
            f_func()
        if i == "all" or i == "class":
            f_class()
        if i == "all" or i == "list":
            f_list()
        if i == "all" or i == "tuple":
            f_tuple()
        if i == "all" or i == "dict":
            f_dict()
        if i == "all" or i == "type":
            f_type()
        if i == "all" or i == "string":
            f_string()
        if i == "all" or i == "re":
            f_re()
        if i == "all" or i == "parse":
            f_parse()
        if i == "all" or i == "other":
            f_other()


if __name__ == "__main__":
    main(sys.argv)
