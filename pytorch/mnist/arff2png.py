#!/usr/bin/env python

from PIL import Image
from scipy.io import arff
import numpy as np

#data, meta = arff.loadarff("mnist_784.arff")
data, meta = arff.loadarff("mnist_test.arff")

image_data = data[meta.names()[:-1]] #everything but the last column
image_array = np.asarray(image_data.tolist(), dtype=np.uint8)
label_data = data['class']
label_array = np.asarray(label_data.tolist(), dtype=np.uint8)

print(image_array.shape)
print(image_array.dtype)
print(image_array.size)
print(image_array.ndim)
print(label_array.size)

sz = label_array.size

for i in range(sz):
    fname = "img{0}_{1}.png".format(i, label_array[i])
    img = Image.fromarray(np.uint8(image_array[i].reshape(28, 28)))
    img.save(fname)


