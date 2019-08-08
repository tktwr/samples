#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch
import numpy as np

# テンソルの作成
x = torch.Tensor(2, 2)
print(x)

# リストの作成
l = [[1,2,3],[4,5,6]]
print(l)

# リストからテンソルの作成
x2 = torch.Tensor(l)
print(x2)
print(x2.size())

# Numpy配列とサイズの確認
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)

def f_tensor_rand():
    print("=== f_tensor_rand ===")

    # 一様分布の乱数生成
    print(torch.rand(2,2))

    # 正規分布の乱数生成
    print(torch.randn(2,2))

def f_tensor_create():
    print("=== f_tensor_create ===")

    # 単位行列の作成
    print(torch.eye(3,3))

    # 空のテンソルの作成
    print(torch.empty(4,1))

    # 等間隔の数列
    print(torch.linspace(0, 100, 11))

def f_tensor_op():
    print("=== f_tensor_op ===")

    # create tensors
    x = torch.Tensor([[2, 2], [1, 1]])
    y = torch.Tensor([[3, 2], [1, 2]])
    print(x)
    print(y)

    # テンソルの足し算
    print(x + y)
    print(torch.add(x, y))

    # テンソルのアダマール積（要素の乗法）
    print(x * y)
    print(torch.mul(x, y))

    # テンソルの積（ドットプロダクト）
    print(torch.mm(x, y))

    # テンソルの要素の和
    print(torch.sum(x))

    # テンソルの要素の標準偏差
    print(torch.std(x))

    # テンソルの要素の算術平均
    print(torch.mean(x))

f_tensor_rand()
f_tensor_create()
f_tensor_op()

