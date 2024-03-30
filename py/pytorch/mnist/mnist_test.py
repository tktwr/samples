#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
from PIL import Image
from scipy.io import arff


def load_image_from_arff(fname, index):
    data, meta = arff.loadarff(fname)

    image_data = data[meta.names()[:-1]] #everything but the last column
    label_data = data['class']

    image_array = np.asarray(image_data.tolist(), dtype=np.float32)
    label_array = np.asarray(label_data.tolist(), dtype=np.uint8)

    X = image_array / 255
    y = label_array

    # 2.2 データをPyTorchのTensorに変換
    X_test = torch.Tensor(X)
    y_test = torch.LongTensor(y)
    #print(f"X_test: {X_test}")
    #print(f"y_test: {y_test}")

    img = X_test[index]
    label = y_test[index]

    print(f"label: {label}")

    return (img, label)


def load_image(fname):
    img = Image.open(fname)
    width, height = img.size
    print(f"w h : {width} {height}")
    print(f"mode: {img.mode}")

    size = width * height
    img_ar = np.asarray(img, dtype=np.float32).reshape(size)
    img_ar /= 255
    return  torch.Tensor(img_ar)


def test(model, tensor):
    model.eval()  # ネットワークを推論モードに切り替える

    data = Variable(tensor)
    output = model(data)  # 入力dataをinputし、出力を求める
     
    pred = output.data.max(0, keepdim=True)[1]  # 出力ラベルを求める
     
    print(f"predicted result: {pred}")
 

def show_array(ar):
    plt.imshow(ar.reshape(28, 28), cmap='gray')
    plt.show()


def show_tensor(tensor):
    ar = tensor.numpy()
    plt.imshow(ar.reshape(28, 28), cmap='gray')
    plt.show()


def main():
    argc = len(sys.argv[1:])

    if argc == 3:
        model_fname, test_fname, index = sys.argv[1:]
        img, label = load_image_from_arff(test_fname, int(index))
    elif argc == 2:
        model_fname, image_fname = sys.argv[1:]
        img = load_image(image_fname)

    show_tensor(img)
    model = torch.load(model_fname)
    test(model, img)

main()
