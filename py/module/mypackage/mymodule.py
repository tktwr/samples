#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mod_a


def myfunc():
    print("mypackage.mymodule.myfunc")
    print(mod_a.DICT['aa'])


class MyClass():
    def mymethod(self):
        print("mypackage.mymodule.myclass.mymethod")
