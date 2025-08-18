#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリを再インポート
import numpy as np
import matplotlib.pyplot as plt

# データ作成
x = np.arange(1, 6)  # x軸の値（1, 2, 3, 4, 5）
y1 = np.array([3, 7, 1, 8, 5])  # 折れ線グラフのデータ
y2 = np.array([2, 6, 4, 7, 3])  # 棒グラフのデータ

# 図の作成
fig, ax = plt.subplots(figsize=(8, 5))

# 折れ線グラフ
ax.plot(x, y1, marker='o', linestyle='-', color='b', label='Line Graph')

# 棒グラフ
ax.bar(x, y2, color='orange', alpha=0.7, label='Bar Graph')

# ラベルとタイトル
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('Line and Bar Graph')

#ax.set_xlim(x[0], x[-1])
#ax.set_ylim(y[0], y[-1])

# 凡例の表示
ax.legend()

# グリッド表示
ax.grid(True, linestyle='--', alpha=0.6)

# 表示
plt.show()

