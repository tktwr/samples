#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import tt_util as tu

fname = tu.FileName("a/b/c/d.png")

print(f"fname.origname() = {fname.origname()}")
print(f"fname.dirname()  = {fname.dirname()}")
print(f"fname.filename() = {fname.filename()}")
print(f"fname.name()     = {fname.name()}")
print(f"fname.ext()      = {fname.ext()}")

print(f'{tu.unix_path(tu.expand_env("$HOME"))}')
print(f'{tu.unix_path(tu.expand_env("$MY_DATA"))}')

print(f'{tu.win_path(tu.expand_env("$HOME"))}')
print(f'{tu.win_path(tu.expand_env("$MY_DATA"))}')

s = '/a/$MY_DATA/a/b'
#s = '$HOME/a/b'
r = re.search('^\$MY_', s)
print(r)
