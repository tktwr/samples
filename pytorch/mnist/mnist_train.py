#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader
from torch import nn
from torch import optim
from sklearn.model_selection import train_test_split
from scipy.io import arff

debug = False


def load_data(fname):
    data, meta = arff.loadarff(fname)

    # tuple data
    image_data = data[meta.names()[:-1]] # everything but the last column
    label_data = data['class']
    if debug:
        print(image_data)
        print(label_data)

    # ndarray
    image_array = np.asarray(image_data.tolist(), dtype=np.float32)
    label_array = np.asarray(label_data.tolist(), dtype=np.uint8)
    if debug:
        print(image_array)
        print(label_array)

    print(f"image_array.shape: {image_array.shape}")
    print(f"label_array.shape: {label_array.shape}")

    X = image_array / 255 # [0, 1]
    y = label_array

    if debug:
        print(f"label: {y[0]}")
        plt.imshow(X[0].reshape(28, 28), cmap='gray')
        plt.show()
        quit()

    return (X, y)


# 2. DataLoderの作成
def make_dataloader(X, y):
    # 2.1 データを訓練とテストに分割（6:1）
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=1/7, random_state=0)

    # 2.2 データをPyTorchのTensorに変換
    X_train = torch.Tensor(X_train)
    y_train = torch.LongTensor(y_train)

    X_test = torch.Tensor(X_test)
    y_test = torch.LongTensor(y_test)

    # 2.3 データとラベルをセットにしたDatasetを作成
    ds_train = TensorDataset(X_train, y_train)
    ds_test = TensorDataset(X_test, y_test)

    # 2.4 データセットのミニバッチサイズを指定した、Dataloaderを作成
    loader_train = DataLoader(ds_train, batch_size=64, shuffle=True)
    loader_test = DataLoader(ds_test, batch_size=64, shuffle=False)

    return (loader_train, loader_test)


# 3. ネットワークの構築
def make_network():
    model = nn.Sequential()
    model.add_module('fc1', nn.Linear(28*28, 100))
    model.add_module('relu1', nn.ReLU())
    model.add_module('fc2', nn.Linear(100, 100))
    model.add_module('relu2', nn.ReLU())
    model.add_module('fc3', nn.Linear(100, 10))

    print(model)

    return model


# 5-1. 学習1回でやることを定義します
def train(loader, model, loss_fn, optimizer, epoch):
    model.train()  # ネットワークを学習モードに切り替える

    # データローダーから1ミニバッチずつ取り出して計算する
    for data, target in loader:
        data, target = Variable(data), Variable(target)  # 微分可能に変換
        optimizer.zero_grad()  # 一度計算された勾配結果を0にリセット

        output = model(data)  # 入力dataをinputし、出力を求める
        loss = loss_fn(output, target)  # 出力と訓練データの正解との誤差を求める
        loss.backward()  # 誤差のバックプロパゲーションを求める
        optimizer.step()  # バックプロパゲーションの値で重みを更新する

    print(f"epoch {epoch}: finished\n")


# 5-2. 推論1回でやることを定義します
def test(loader, model):
    model.eval()  # ネットワークを推論モードに切り替える
    correct = 0

    # データローダーから1ミニバッチずつ取り出して計算する
    for data, target in loader:
        data, target = Variable(data), Variable(target)  # 微分可能に変換
        output = model(data)  # 入力dataをinputし、出力を求める

        # 推論する
        pred = output.data.max(1, keepdim=True)[1]  # 出力ラベルを求める
        correct += pred.eq(target.data.view_as(pred)).sum()  # 正解と一緒だったらカウントアップ

    # 正解率を出力
    data_num = len(loader.dataset)  # データの総数
    ratio = 100. * correct / data_num
    print(f'correct: {correct}/{data_num} ({ratio:.0f}%)\n')


def main(data_fname, model_fname):
    X, y = load_data(data_fname)
    loader_train, loader_test = make_dataloader(X, y)
    model = make_network()

    # 誤差関数の設定
    loss_fn = nn.CrossEntropyLoss()

    # 重みを学習する際の最適化手法の選択
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(3):
        train(loader_train, model, loss_fn, optimizer, epoch)

    torch.save(model, model_fname)

    test(loader_test, model)


data_fname, model_fname = sys.argv[1:]
main(data_fname, model_fname)
