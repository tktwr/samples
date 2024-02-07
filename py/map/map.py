#!/usr/bin/env python
# -*- coding: utf-8 -*-

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]


# map() 関数を使用して、リストの各要素を二乗する
squares = map(square, numbers)

# map オブジェクトをリストに変換して結果を表示
squares_list = list(squares)
print(squares_list)  # Output: [1, 4, 9, 16, 25]
