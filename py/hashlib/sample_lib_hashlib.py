#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py.hashlib*

import hashlib

dat = 'python'

hs = hashlib.sha256(dat.encode()).hexdigest()
print(hs)

# output:
# 11a4a60b518bf24989d481468076e5d5982884626aed9faeb35b8576fcd223e1
