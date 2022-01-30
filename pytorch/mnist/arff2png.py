#!/usr/bin/env python

import sys
from PIL import Image
from scipy.io import arff
import numpy as np


def load_arff(fname):
    data, meta = arff.loadarff(fname)
    image_data = data[meta.names()[:-1]] #everything but the last column
    image_array = np.asarray(image_data.tolist(), dtype=np.uint8)
    label_data = data['class']
    label_array = np.asarray(label_data.tolist(), dtype=np.uint8)
    return (image_array, label_array)


def save_images(image_array, label_array):
    size = image_array.shape[0]
    for i in range(size):
        fname = f"_images/img{i}_{label_array[i]}.png"
        img = Image.fromarray(image_array[i].reshape(28, 28).astype('uint8'))
        img.save(fname)


def main(fname):
    image_array, label_array = load_arff(fname)

    print(f"image_array.shape = {image_array.shape}")
    print(f"image_array.ndim  = {image_array.ndim}")
    print(f"image_array.dtype = {image_array.dtype}")
    print(f"image_array.size  = {image_array.size}")
    print(f"label_array.size  = {label_array.size}")

    save_images(image_array, label_array)


main(sys.argv[1])
