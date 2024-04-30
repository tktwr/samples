#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mod_a
import mod_b
#import mypackage.mymodule as mymod
from mypackage import mymodule as mymod


# *memo:sample:py.syntax.module*
def f_module():
    print("=== f_module() ===")
    mod_a.DICT['aa'] = 100
    mod_a.myfunc()


# *memo:sample:py.syntax.package*
def f_package():
    print("=== f_package() ===")
    mymod.myfunc()
    my = mymod.MyClass()
    my.mymethod()


if __name__ == "__main__":
    f_module()
    f_package()
