#!/usr/bin/env python
# coding: utf-8
# *memo_py_sample_syntax*

import sys

print("sys.stdin.encoding {0}", sys.stdin.encoding)
print("sys.stdout.encoding {0}", sys.stdin.encoding)
print("sys.stderr.encoding {0}", sys.stdin.encoding)

print("Hello")
print(u"こんにちは")

i = 0
if i == 0:
    print("i == 0")
elif i == 1:
    print("i == 1")
else:
    print("other")

while i < 5:
    print("%d " % i, end="")
    i += 1
print("")

for i in range(5):
    print("%d " % i, end="")
print("")

for i in range(5, 10):
    print("%d " % i, end="")
print("")

list = [1, 2, 3, 4, 5]
for i in list:
    print("%d " % i, end="")
print("")

