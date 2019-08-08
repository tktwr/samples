#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import PIL
import cv2
import numpy
import matplotlib
import skimage
import sklearn
import torch
#import tensorflow

def main():
    print("PIL {}".format(PIL.__version__))
    print("cv2 {}".format(cv2.__version__))
    print("numpy {}".format(numpy.__version__))
    print("matplotlib {}".format(matplotlib.__version__))
    print("skimage {}".format(skimage.__version__))
    print("sklearn {}".format(sklearn.__version__))
    print("torch {}".format(torch.__version__))
    if torch.cuda.is_available():
        print("  cuda is available")
    #print("tensorflow {}".format(tensorflow.__version__))

main()

