#!/usr/bin/env python
# -*- coding: utf-8 -*-

l = [[1, 2], [3, 4], [5, 6]]
a, b = zip(*l)
print(list(a))  # [1, 3, 5]
print(list(b))  # [2, 4, 6]

a = [1, 3, 5]
b = [2, 4, 6]

l = list(map(list, zip(a, b)))
print(l)  # [[1, 2], [3, 4], [5, 6]]

