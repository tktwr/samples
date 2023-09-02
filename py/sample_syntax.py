#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *sample:py.syntax*

import sys
import math
import tt_util as ut


# -----------------------------------------------------
# *sample:py.syntax.comment*
def f_comment():
    # comment
    '''
    comment
    '''


# -----------------------------------------------------
# *sample:py.syntax.encoding*
def f_encoding():
    print(f"sys.stdin.encoding  = {sys.stdin.encoding}")
    print(f"sys.stdout.encoding = {sys.stdout.encoding}")
    print(f"sys.stderr.encoding = {sys.stderr.encoding}")


# -----------------------------------------------------
# *sample:py.syntax.input*
def f_input():
    print(f"input: ", end="")
    s = input()
    print(f"s: {s}")


# -----------------------------------------------------
# *sample:py.syntax.print*
def f_print():
    print("Hello")
    print("こんにちは")


# -----------------------------------------------------
# *sample:py.syntax.print_fstring*
def f_print_fstring():
    # f-string (python >= 3.6)
    ival = 2
    fval = 1 / 3
    word = "hello"
    width = 10

    print(f"1+1         = {1+1}")
    print(f"1+0.5       = {1+0.5}")
    print(f"ival        = {ival}")
    print(f"ival:3d     = {ival:3d}")
    print(f"ival:03d    = {ival:03d}")
    print(f"ival**10:,d = {ival**10:,d}")
    print(f"fval        = {fval}")
    print(f"fval:.3f    = {fval:.3f}")
    print(f"word:<10s   = [{word:<{width}s}]")
    print(f"word:^10s   = [{word:^{width}s}]")
    print(f"word:>10s   = [{word:>{width}s}]")
    print(f"word        = ", end='')
    print(word)


# -----------------------------------------------------
# *sample:py.syntax.if*
def f_if():
    l = [0, 1, 2, 3, 4]
    i = 1

    print(f'l = {l}')
    print(f'i = {i}')

    if i == 0:
        print("i == 0")
    elif i == 1:
        print("i == 1")
    else:
        print("i == else")

    if not (i == 0):
        print("not (i == 0)")

    if i == 0 or \
       i == 1:
        print("i == 0 or i == 1")

    if 0 <= i and i < 2:
        print("0 <= i and i < 2")

    if 0 <= i < 2:
        print("0 <= i < 2")

    if i in l:
        print(f"{i} = inside")
    else:
        print(f"{i} = outside")


# -----------------------------------------------------
# *sample:py.syntax.for*
def f_for():
    for i in range(5):
        print(f"{i} ", end="")
    print()

    for i in range(0, 5):
        print(f"{i} ", end="")
    print()

    for i in range(0, 5, 1):
        print(f"{i} ", end="")
    print()

    list = [0, 1, 2, 3, 4]
    for i in list:
        print(f"{i} ", end="")
    print()


# -----------------------------------------------------
# *sample:py.syntax.while*
def f_while():
    i = 0
    while i < 5:
        print(f"{i} ", end="")
        i += 1
    print()


# -----------------------------------------------------
# *sample:py.syntax.func*
def _f_add(a, b):
    return a + b


def f_func():
    x = _f_add(1, 2)
    print(f"x: {x}")


# -----------------------------------------------------
# *sample:py.syntax.func_args*
def _f_args(a, b):
    print(f"a, b: {a} {b}")


def f_func_args():
    _f_args(1, 2)
    _f_args(2, 1)
    _f_args(b=2, a=1)


# -----------------------------------------------------
# *sample:py.syntax.class*
class MyClass():
    def __init__(self):
        print(f"MyClass.__init__")
        self.a = {0: 123}

    def __del__(self):
        print(f"MyClass.__del__")

    def f(self, x):
        self.x = x
        print(f"MyClass.f: {x}")

    def g(self):
        print(dir(self))
        print(f"hasattr(self, 'x') = {hasattr(self, 'x')}")
        print(f"hasattr(self, 'a') = {hasattr(self, 'a')}")

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


def f_class():
    my = MyClass()
    my.f(10)
    my.g()
    MyClass.class_method()
    MyClass.class_method()
    print(f"MyClass.class_member: {MyClass.class_member}")


# -----------------------------------------------------
# *sample:py.syntax.subclass*
class MySubClass(MyClass):
    def f(self, x):
        print(f"MySubClass.f: {x}")


def f_subclass():
    my = MySubClass()
    my.f(10)


# -----------------------------------------------------
# *sample:py.syntax.type*
def f_type():
    n = None
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


# -----------------------------------------------------
# *sample:py.syntax.tuple*
def f_tuple():
    # tuple is read only
    t = (1, 3, 5, 7, 9)
    print(f"t = {t}")
    t = (1, 'two', 3, 'four', 5)
    print(f"t = {t}")
    print(f"l = {list(t)}")


# -----------------------------------------------------
# *sample:py.syntax.set*
def f_set():
    s = {1, 2, 3}
    print(f's = {s}')


# -----------------------------------------------------
# *sample:py.syntax.range*
def f_range():
    print(f'list(range(6))       = {list(range(6))}')
    print(f'list(range(0, 6))    = {list(range(0, 6))}')
    print(f'list(range(0, 6, 1)) = {list(range(0, 6, 1))}')
    print(f'list(range(0, 6, 1)) = {list(range(0, 6, 2))}')


# -----------------------------------------------------
# *sample:py.syntax.zip*
def f_zip():
    l1 = [1, 2, 3, 4]
    l2 = [0.1, 0.2, 0.3, 0.4]
    l = list(zip(l1, l2))
    print(l)


# -----------------------------------------------------
# *sample:py.syntax.color*
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
        print(f"{i:10s}, {hex_str}, {r:3d}, {g:3d}, {b:3d}")

    R, G, B = 0, 1, 2
    print(f"R, G, B: {R}, {G}, {B}")


# -----------------------------------------------------
# *sample:py.syntax.math*
def f_math():
    print(f" 5  / 2 = { 5  / 2}")
    print(f" 5 // 2 = { 5 // 2}")
    print(f" 5  / 3 = { 5  / 3}")
    print(f" 5 // 3 = { 5 // 3}")
    print(f"10  / 3 = {10  / 3}")
    print(f"10 // 3 = {10 // 3}")
    print(f"2**10   = {2**10}")
    a = 0
    a += 1
    print(f"a = {a}")

    x = -10
    print(f"0 if x < 0 else x = {0 if x < 0 else x}")
    x = 10
    print(f"0 if x < 0 else x = {0 if x < 0 else x}")

    print(f"math.pi               = {math.pi}")
    print(f"math.radians(180)     = {math.radians(180)}")
    print(f"math.degrees(math.pi) = {math.degrees(math.pi)}")
    print(f"math.sin(math.pi/2)   = {math.sin(math.pi/2)}")

    l = [0, math.pi / 2, math.pi]
    ll = [math.degrees(i) for i in l]
    print(f"ll = {ll}")


# -----------------------------------------------------
# *sample:py.syntax.in*
# *sample:py.syntax.not_in*
def f_in():
    a = 123

    print(f"locals()             = {locals()}")
    print(f"globals()            = {globals()}")
    print(f"'a' in locals()      = {'a' in locals()}")
    print(f"'a' in globals()     = {'a' in globals()}")
    print(f"'a' not in globals() = {'a' not in globals()}")

    t = (1, 3, 4)

    print(f"t            = {t}")
    print(f"1 in t       = {1 in t}")
    print(f"0 in t       = {0 in t}")
    print(f"0 not in t   = {0 not in t}")
    print(f"not (0 in t) = {not (0 in t)}")

    d = {1: "apple"}

    print(f"d            = {d}")
    print(f"1 in d       = {1 in d}")
    print(f"0 in d       = {0 in d}")
    print(f"0 not in d   = {0 not in d}")
    print(f"not (0 in d) = {not (0 in d)}")


# -----------------------------------------------------
# *sample:py.syntax.func_object*
def f_func_object():
    func = f_print
    func()


# -----------------------------------------------------
# *sample:py.syntax.eval*
def f_eval():
    func = 'f_print'
    eval(f'{func}()')


