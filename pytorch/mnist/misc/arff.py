#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arff, numpy as np
dataset = arff.load(open('mnist_784.arff', 'rb'))
dataset = arff.load(open('test.arff'))
data = np.array(dataset['data'])
labels = np.array(dataset['labels'])

