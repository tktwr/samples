#!/usr/bin/env python

from scipy.io import arff
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable

test_file = "mnist_test.arff"
model_file = "mnist.model"

data, meta = arff.loadarff(test_file)

image_data = data[meta.names()[:-1]] #everything but the last column
label_data = data['class']

image_array = np.asarray(image_data.tolist(), dtype=np.float32)
label_array = np.asarray(label_data.tolist(), dtype=np.uint8)

X = image_array / 255
y = label_array

index = 1

plt.imshow(X[index].reshape(28, 28), cmap='gray')
plt.show()



# 2.2 データをPyTorchのTensorに変換
X_test = torch.Tensor(X)
y_test = torch.LongTensor(y)
print("X_test: {}".format(X_test))
print("y_test: {}".format(y_test))


model = torch.load(model_file)
model.eval()  # ネットワークを推論モードに切り替える

data = Variable(X_test[index])
output = model(data)  # 入力dataをinputし、出力を求める
 
pred = output.data.max(0, keepdim=True)[1]  # 出力ラベルを求める
 
print("predicted result: {}".format(pred))
 
 
X_test_show = X_test[index].numpy()
plt.imshow(X_test_show.reshape(28, 28), cmap='gray')
plt.show()
print("correct result: {}".format(y_test[index]))

