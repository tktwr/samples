#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.syntax*

import sys
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


# *memo_py.syntax.func*
def f_add(a, b):
    return a + b


def f_args(a, b):
    print(f"a, b: {a} {b}")


def f_func():
    f_title("f_func()")
    x = f_add(1, 2)
    print(f"x: {x}")
    f_args(1, 2)
    f_args(2, 1)
    f_args(b=2, a=1)


# *memo_py.syntax.class*
class MyClass():
    def __init__(self):
        print(f"MyClass.__init__")

    def __del__(self):
        print(f"MyClass.__del__")

    def f(self, x):
        self.x = x
        print(f"MyClass.f: {x}")

    def public_method(self):
        pass

    def _protected_method(self):
        pass

    def __private_method(self):
        pass
    
    class_member = 0

    @classmethod
    def class_method(cls):
        cls.class_member += 1
        print(f"class_method: {cls.class_member}")


class MySubClass(MyClass):
    def f(self, x):
        print(f"MySubClass.f: {x}")


def f_class():
    f_title("f_class()")
    my = MyClass()
    my.f(10)
    MyClass.class_method()
    MyClass.class_method()


def f_subclass():
    f_title("f_subclass()")
    my = MySubClass()
    my.f(10)


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


# *memo_py.syntax.set*
def f_set():
    s = {1, 2, 3}

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


# *memo_py.syntax.zip*
def f_zip():
    pass


def f_color():
    color = {
        "Red"    : "fb4934",
        "Green"  : "b8bb26",
        "Yellow" : "fabd2f",
        "Blue"   : "707fd9",
        "Purple" : "d3869b",
        "Aqua"   : "8ec07c",
        "Orange" : "fe8019",
    }
    for i in color:
        hex_str = color[i]
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        print(f"{i}, {hex_str}, {r}, {g}, {b}")


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
        if i == "all" or i == "subclass":
            f_subclass()
        if i == "all" or i == "list":
            f_list()
        if i == "all" or i == "tuple":
            f_tuple()
        if i == "all" or i == "set":
            f_set()
        if i == "all" or i == "dict":
            f_dict()
        if i == "all" or i == "type":
            f_type()
        if i == "all" or i == "color":
            f_color()
        if i == "all" or i == "other":
            f_other()


if __name__ == "__main__":
    main(sys.argv)
