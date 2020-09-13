#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.syntax*

import sys
import my
from dir1.mymodule import MyClassA

# *memo_py.syntax.input*
def f_input():
    print("input:")
    in_s = input()
    print("in_s: {}".format(in_s))

# *memo_py.syntax.print*
def f_print():
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
    print("sys.stdin.encoding: {}".format(sys.stdin.encoding))
    print("sys.stdout.encoding: {}".format(sys.stdout.encoding))
    print("sys.stderr.encoding: {}".format(sys.stderr.encoding))

# *memo_py.syntax.if*
def f_if(i):
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
def f_while(i):
    while i < 5:
        print("%d " % i, end="")
        i += 1
    print()

# *memo_py.syntax.for*
def f_for():
    for i in range(0, 5, 1):
        print("%d " % i, end="")
    print()

    for i in range(0, 5):
        print("%d " % i, end="")
    print()

    for i in range(5):
        print("%d " % i, end="")
    print()

    list = [1, 3, 5, 7, 9]
    for i in list:
        print("%d " % i, end="")
    print()

def f_add(a, b):
    return a + b

def f_args(a, b):
    print("a, b: {} {}".format(a, b))

# *memo_py.syntax.func*
def f_func():
    x = f_add(1, 2)
    print("f_add: %d" % x)
    f_args(1, 2)
    f_args(2, 1)
    f_args(b=2, a=1)

# *memo_py.syntax.class*
def f_class():
    my1 = my.MyClass(10)
    my2 = my.MyClass(20)
    sub1 = my.MySubClass(100)

    print(my.MyClass.n)
    my.MyClass.f("class method")
    print(my1.x)
    print(my2.x)
    print(my1.add(1))
    print(sub1.g())

    a1 = MyClassA(123)
    print(a1.x)

# *memo_py.syntax.list*
def f_list():
    l = [1, 2, 3, 4, 5]
    print("l = {}".format(l))
    print("len(l) = {}".format(len(l)))
    print("l[0] = {}".format(l[0]))
    l.append(10)
    print("l.append(10) = {}".format(l))
    l.insert(0, 20)
    print("l.insert(0, 20) = {}".format(l))
    l.pop(2)
    print("l.pop(2) = {}".format(l))

    l = ['zero', 1, 'two', 3, 'four', 5]
    print("l       = {}".format(l))
    print("l[:]    = {}".format(l[:]))
    print("l[0:]   = {}".format(l[0:]))
    print("l[2:4]  = {}".format(l[2:4]))  # 2 + 2 chars
    print("l[:-1]  = {}".format(l[:-1]))
    print("l[:-2]  = {}".format(l[:-2]))
    print("l[-2:-1]= {}".format(l[-2:-1]))
    print("l[-1:]  = {}".format(l[-1:]))

    print("t = {}".format(tuple(l)))

    s = "1 2 3 4 5"
    print("s = {}".format(s))
    str_list = s.split(" ")
    print("str_list = {}".format(str_list))
    int_list = list(int(i) for i in str_list)
    print("int_list = {}".format(int_list))
    int_list = list(range(1, 6, 1))
    print("int_list = {}".format(int_list))

# *memo_py.syntax.tuple*
def f_tuple():
    # tuple is read only
    t = (1, 3, 5, 7, 9)
    print("t = {}".format(t))
    t = (1, 'two', 3, 'four', 5)
    print("t = {}".format(t))
    print("l = {}".format(list(t)))

# *memo_py.syntax.dict*
def f_dict():
    d = {"a":1, "b":2}
    print("d = {}".format(d))
    print("d[\"a\"] = {}".format(d["a"]))

# *memo_py.syntax.type*
def f_type():
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

# *memo_py.syntax.re*
def f_re():
    import re
    in_s = "1, 1.5, 2, 2.5:str"
    out_s = re.split(r",\s+|:", in_s)
    print("in_s: {}".format(in_s))
    print("out_s: {}".format(out_s))

# *memo_py.syntax.parse*
def f_parse():
    import parse
    in_s = "123 str1 str2 12.34"
    out_s = parse.parse("{:d} str1 {:w} {:f}", in_s)
    print("in_s: {}".format(in_s))
    print("out_s: {}".format(out_s))

    in_s = "123 str1 str2 12.34"
    out_s = parse.parse("{var1:d} str1 {:w} {var2}", in_s)
    print("in_s: {}".format(in_s))
    print("out_s: {}".format(out_s))
    print("out_s['var1']: {}".format(out_s['var1']))
    print("out_s['var2']: {}".format(out_s['var2']))
    print("out_s[0]: {}".format(out_s[0]))

# *memo_py.syntax.string*
def f_string():
    s = "abc," + "def,"
    s = s + str(100)
    print("s = {}".format(s))
    l = s.split(",")
    print("l = {}".format(l))

    import parse
    s = "images/img{}_{}.png".format(123, 5)
    print("s: {}".format(s))
    print("s[0]: {}".format(s[0]))
    print("s[-1]: {}".format(s[-1]))
    print("s[0:4]: {}".format(s[0:4]))
    print("s[1:4]: {}".format(s[1:4]))
    print("s.split('/'): {}".format(s.split('/')))
    print("s.replace('/', '-'): {}".format(s.replace('/', '-')))
    dirname, filename = s.split("/")
    print("dirname: {}".format(dirname))
    print("filename: {}".format(filename))
    result = parse.parse("img{nr:d}_{label:d}.png", filename)
    print("nr, label: {}, {}".format(result['nr'], result['label']))

def main(argv):
    for i in argv:
        if i == "input":
            print("=== f_input() ===")
            f_input()
        if i == "all" or i == "print":
            print("=== f_print() ===")
            f_print()
        if i == "all" or i == "if":
            print("=== f_if() ===")
            f_if(0)
            f_if(1)
            f_if(2)
            f_if(3)
            f_if(4)
            f_if(5)
            f_if(9)
        if i == "all" or i == "while":
            print("=== f_while() ===")
            f_while(0)
        if i == "all" or i == "for":
            print("=== f_for() ===")
            f_for()
        if i == "all" or i == "func":
            print("=== f_func() ===")
            f_func()
        if i == "all" or i == "class":
            print("=== f_class() ===")
            f_class()
        if i == "all" or i == "list":
            print("=== f_list() ===")
            f_list()
        if i == "all" or i == "tuple":
            print("=== f_tuple() ===")
            f_tuple()
        if i == "all" or i == "dict":
            print("=== f_dict() ===")
            f_dict()
        if i == "all" or i == "type":
            print("=== f_type() ===")
            f_type()
        if i == "all" or i == "string":
            print("=== f_string() ===")
            f_string()
        if i == "all" or i == "re":
            print("=== f_re() ===")
            f_re()
        if i == "all" or i == "parse":
            print("=== f_parse() ===")
            f_parse()

if __name__ == "__main__":
    main(sys.argv)

