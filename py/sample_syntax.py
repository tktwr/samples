#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py_sample_syntax*

import sys
import my

def f_print():
    print("Hello")
    print("こんにちは")
    print("{0} {1} {2} ".format(1, 2, 3))
    print("%d %d %d" % (1, 2, 3))
    print("%d " % 1, end="")
    print("%d " % 2, end="")
    print("%d " % 3, end="")
    print()
    print("sys.stdin.encoding: {0}".format(sys.stdin.encoding))
    print("sys.stdout.encoding: {0}".format(sys.stdout.encoding))
    print("sys.stderr.encoding: {0}".format(sys.stderr.encoding))

def f_if(i):
    if i == 0:
        print("i == 0")
    elif i == 1:
        print("i == 1")
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

def f_func():
    x = f_add(1, 2)
    print("f_add: %d" % x)

def f_class():
    my1 = my.MyClass(10)
    my2 = my.MyClass(20)

    print(my.MyClass.n)
    my.MyClass.f("class method")

    print(my1.x)
    print(my2.x)
    print(my1.add(1))

def f_list():
    list = [1, 2, 3, 4, 5]
    print(list)
    print(list[0])
    list.append(10)
    print(list)
    list.insert(0, 20)
    print(list)
    list.pop(2)
    print(list)

    list2 = [1, 'two', 3, 'four', 5]
    print(list2)
    print(list2[:])
    print(list2[0:])
    print(list2[2:4])
    print(list2[:-1])
    print(list2[:-2])
    print(list2[-2:-1])
    print(list2[-1:])

def f_tuple():
    t = (1, 3, 5, 7, 9)
    print(t)

def f_dict():
    d = {"a":1, "b":2}
    print(d)
    print(d["a"])

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

def f_string():
    s = "abc," + "def,"
    s = s + str(100)
    print(s)
    l = s.split(",")
    print(l)

def main():
    print("=== f_print() ===")
    f_print()
    print("=== f_if() ===")
    f_if(0)
    f_if(1)
    f_if(2)
    print("=== f_while() ===")
    f_while(0)
    print("=== f_for() ===")
    f_for()
    print("=== f_func() ===")
    f_func()
    print("=== f_class() ===")
    f_class()
    print("=== f_list() ===")
    f_list()
    print("=== f_tuple() ===")
    f_tuple()
    print("=== f_dict() ===")
    f_dict()
    print("=== f_type() ===")
    f_type()
    print("=== f_string() ===")
    f_string()


if __name__ == "__main__":
    argv = sys.argv
    print(argv)
    main()

