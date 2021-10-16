#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ttpy import FileName

fname = FileName("a/b/c/d.png")

print(f"fname.origname() = {fname.origname()}")
print(f"fname.dirname()  = {fname.dirname()}")
print(f"fname.filename() = {fname.filename()}")
print(f"fname.name()     = {fname.name()}")
print(f"fname.ext()      = {fname.ext()}")
