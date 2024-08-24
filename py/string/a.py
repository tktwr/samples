#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

#pattern = re.compile(r"@[A-Za-z0-9_]+:[0-9]*\.[0-9]+")
#pattern = re.compile(r"@\w+:[0-9]*\.[0-9]+")
pattern = re.compile(r"@\w+:\d*\.\d+")

# テストケース
test_strings = [
    "@f_abc:0.3",
    "@example:123.456",
    "@test:3.14",
    "@user_123:0.001",
    "@invalid:.3",  # 無効：数字なし
    "@invalid:3.",  # 無効：小数点の後に数字なし
]

for s in test_strings:
    if pattern.match(s):
        print(f"'{s}' はマッチしました")
    else:
        print(f"'{s}' はマッチしませんでした")

