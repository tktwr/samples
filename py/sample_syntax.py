#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.syntax*

import sys
import my
from dir1.mymodule import MyClassA

def f_print():
    # comment
    '''
    comment
    '''
    print("Hello")
    print("こんにちは")
    print("{} {} {}".format(0, 1, 2))
    print("{0} {1} {2}".format(0, 1, 2))
    print("{2} {2} {2}".format(0, 1, 2))
    print("%d %d %d" % (0, 1, 2))
    print("%d " % 3, end="")
    print("%d " % 4, end="")
    print("%d " % 5, end="")
    print()
    print("sys.stdin.encoding: {}".format(sys.stdin.encoding))
    print("sys.stdout.encoding: {}".format(sys.stdout.encoding))
    print("sys.stderr.encoding: {}".format(sys.stderr.encoding))

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

def f_while(i):
    while i < 5:
        print("%d " % i, end="")
        i += 1
    print()

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

def f_func():
    x = f_add(1, 2)
    print("f_add: %d" % x)
    f_args(1, 2)
    f_args(2, 1)
    f_args(b=2, a=1)

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

def f_list():
    l = [1, 2, 3, 4, 5]
    print("l = {}".format(l))
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
    print("l[2:4]  = {}".format(l[2:4]))
    print("l[:-1]  = {}".format(l[:-1]))
    print("l[:-2]  = {}".format(l[:-2]))
    print("l[-2:-1]= {}".format(l[-2:-1]))
    print("l[-1:]  = {}".format(l[-1:]))

    print("t = {}".format(tuple(l)))

def f_tuple():
    # tuple is read only
    t = (1, 3, 5, 7, 9)
    print("t = {}".format(t))
    t = (1, 'two', 3, 'four', 5)
    print("t = {}".format(t))
    print("l = {}".format(list(t)))

def f_dict():
    d = {"a":1, "b":2}
    print("d = {}".format(d))
    print("d[\"a\"] = {}".format(d["a"]))

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

def f_string():
    s = "abc," + "def,"
    s = s + str(100)
    print("s = {}".format(s))
    l = s.split(",")
    print("l = {}".format(l))

def main(argv):
    for i in argv:
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

if __name__ == "__main__":
    main(sys.argv)

