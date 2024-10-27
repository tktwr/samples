#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tt_util as tu


def f_filename():
    FN = tu.FileName("$HOME/a/b/c/d.png")

    print(f"FN.origname() = {FN.origname()}")
    print(f"FN.dirname()  = {FN.dirname()}")
    print(f"FN.abspath()  = {FN.abspath(prefix='pre_', postfix='_post', ext='.jpg')}")
    print(f"FN.filename() = {FN.filename(prefix='pre_', postfix='_post', ext='.jpg')}")
    print(f"FN.filename() = {FN.filename()}")
    print(f"FN.name()     = {FN.name()}")
    print(f"FN.ext()      = {FN.ext()}")


f_filename()
