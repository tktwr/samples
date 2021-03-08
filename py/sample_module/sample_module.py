#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import mymodule
import mypackage.mymodule as mymod


# *memo_py.syntax.module*
def f_module():
    f_title("f_module()")
    mymodule.myfunc()

    mymod.myfunc()
    my = mymod.MyClass()
    my.mymethod()


def main(argv):
    f_module()


if __name__ == "__main__":
    main(sys.argv)
