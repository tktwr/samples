#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable
from PIL import Image

model_file = "mnist.model"
image_file = "images_test/img0_5.png"

def show_image(img):
    plt.imshow(img.reshape(28, 28), cmap='gray')
    plt.show()

label_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

img = Image.open(image_file)
width, height = img.size
print("w h: {0} {1}".format(width, height))
print("mode: {0}".format(img.mode))
image_array = np.asarray(img, dtype=np.float32).reshape(784)

X = image_array / 255

show_image(X)


# tensor
X_test = torch.Tensor(X)
y_test = torch.LongTensor(label_data)
print("X_test: {}".format(X_test))
print("y_test: {}".format(y_test))

show_image(X_test.numpy())


# prediction
model = torch.load(model_file)
model.eval()
data = Variable(X_test)
output = model(data)  # 入力dataをinputし、出力を求める
print("output: {}".format(output))
 
pred = output.data.max(0, keepdim=True)[1]  # 出力ラベルを求める
 
print("predicted result: {}".format(pred))
 
