#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add(x, y):
    return x + y

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

# map() 関数を使用して、2つのリストから要素を取得して加算する
sums = map(add, numbers1, numbers2)

# map オブジェクトをリストに変換して結果を表示
sums_list = list(sums)
print(sums_list)  # Output: [7, 9, 11, 13, 15]
