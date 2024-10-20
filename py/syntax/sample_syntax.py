#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:syntax*

import sys
import math
import tt_util as ut


# -----------------------------------------------------
def f_syntax_comment():
    # comment
    '''
    comment
    '''


# -----------------------------------------------------
def f_syntax_encoding():
    print(f"sys.stdin.encoding  = {sys.stdin.encoding}")
    print(f"sys.stdout.encoding = {sys.stdout.encoding}")
    print(f"sys.stderr.encoding = {sys.stderr.encoding}")


# -----------------------------------------------------
def f_syntax_input():
    print(f"input: ", end="")
    s = input()
    print(f"s: {s}")


# -----------------------------------------------------
def f_syntax_print():
    print("Hello")
    print("こんにちは")


# -----------------------------------------------------
def f_syntax_if():
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
def f_syntax_for():
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
def f_syntax_while():
    i = 0
    while i < 5:
        print(f"{i} ", end="")
        i += 1
    print()


# -----------------------------------------------------
def _f_syntax_add(a, b):
    return a + b


def f_syntax_func():
    x = _f_syntax_add(1, 2)
    print(f"x: {x}")


# -----------------------------------------------------
def _f_syntax_args(a, b):
    print(f"a, b: {a} {b}")


def f_syntax_func_args():
    _f_syntax_args(1, 2)
    _f_syntax_args(2, 1)
    _f_syntax_args(b=2, a=1)


# -----------------------------------------------------
def f_syntax_type():
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
def f_syntax_tuple():
    # tuple is read only
    t = (1, 3, 5, 7, 9)
    print(f"t = {t}")
    t = (1, 'two', 3, 'four', 5)
    print(f"t = {t}")
    print(f"l = {list(t)}")


# -----------------------------------------------------
def f_syntax_set():
    s = {1, 2, 3}
    print(f's = {s}')


# -----------------------------------------------------
def f_syntax_range():
    print(f'list(range(6))       = {list(range(6))}')
    print(f'list(range(0, 6))    = {list(range(0, 6))}')
    print(f'list(range(0, 6, 1)) = {list(range(0, 6, 1))}')
    print(f'list(range(0, 6, 1)) = {list(range(0, 6, 2))}')


# -----------------------------------------------------
def f_syntax_zip():
    l1 = [1, 2, 3, 4]
    l2 = [0.1, 0.2, 0.3, 0.4]
    l = list(zip(l1, l2))
    print(l)


# -----------------------------------------------------
def f_syntax_color():
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
def f_syntax_math():
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
def f_syntax_in():
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
def f_syntax_func_object():
    func = f_syntax_print
    func()


# -----------------------------------------------------
def f_syntax_eval():
    func = 'f_syntax_print'
    eval(f'{func}()')


# -----------------------------------------------------
def f_syntax_enumerate():
    xy = [[10, 10], [11, 11]]
    for i, (x, y) in enumerate(xy):
        print(f'{i} {x} {y}')


# -----------------------------------------------------
def run_funcs():
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')


if __name__ == '__main__':
    run_funcs()
