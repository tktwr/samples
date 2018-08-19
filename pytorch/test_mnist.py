#!/usr/bin/env python

from scipy.io import arff
import numpy as np
data, meta = arff.loadarff("test.arff")

image_data = data[meta.names()[:-1]] #everything but the last column
image_array = np.asarray(image_data.tolist(), dtype=np.float32)
label_data = data['class']
label_array = np.asarray(label_data.tolist(), dtype=np.uint8)

X = image_array / 255
y = label_array

index = 9

import matplotlib.pyplot as plt
plt.imshow(X[index].reshape(28, 28), cmap='gray')
plt.show()



import torch
from torch.autograd import Variable

# 2.2 データをPyTorchのTensorに変換
X_test = torch.Tensor(X)
y_test = torch.LongTensor(y)


model = torch.load('mnist.model')

model.eval()  # ネットワークを推論モードに切り替える
data = Variable(X_test[index])
output = model(data)  # 入力dataをinputし、出力を求める
 
pred = output.data.max(0, keepdim=True)[1]  # 出力ラベルを求める
 
print("予測結果は{}".format(pred))
 
 
X_test_show = (X_test[index]).numpy()
plt.imshow(X_test_show.reshape(28, 28), cmap='gray')
plt.show()
print("この画像データの正解ラベルは{}です".format(y_test[index]))
