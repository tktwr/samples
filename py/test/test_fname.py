#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tt_util as tu

FN = tu.FileName("a/b/c/d.png")

print(f"FN.origname() = {FN.origname()}")
print(f"FN.dirname()  = {FN.dirname()}")
print(f"FN.filename() = {FN.filename()}")
print(f"FN.name()     = {FN.name()}")
print(f"FN.ext()      = {FN.ext()}")

print(f'{tu.path_unix(tu.expand_env("$HOME"))}')
print(f'{tu.path_unix(tu.expand_env("$MY_DATA"))}')

print(f'{tu.path_windows(tu.expand_env("$HOME"))}')
print(f'{tu.path_windows(tu.expand_env("$MY_DATA"))}')

s = '/a/$MY_DATA/a/b'
#s = '$HOME/a/b'
r = re.search('^\$MY_', s)
print(r)
