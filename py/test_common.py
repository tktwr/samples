#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ttpy import FileName

fname = FileName("a/b/c/d.png")
print(fname.origname())
print(fname.dirname())
print(fname.filename())
print(fname.name())
print(fname.ext())
