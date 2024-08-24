#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

#pattern = re.compile(r"(@\w+)(:\d*\.\d+)?")
pattern = re.compile(r"(@.+)")

# テストケース
test_strings = [
    "f_abc:0.1",
    "@f_abc",
    "@f_abc:1",
    "@f_abc:.1",
    "@f_abc:0.1",
]

for s in test_strings:
    r = pattern.match(s)
    if r:
        print(f'[o] {s}, {r.group(0)}')
    else:
        print(f'[x] {s}')

