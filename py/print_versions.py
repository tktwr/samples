#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PIL
import cv2
import numpy
import matplotlib
import sklearn
import tkinter
import torch
# import tensorflow
# import skimage


def main():
    print(f"PIL {PIL.__version__}")
    print(f"cv2 {cv2.__version__}")
    print(f"numpy {numpy.__version__}")
    print(f"matplotlib {matplotlib.__version__}")
    print(f"sklearn {sklearn.__version__}")
    print(f"tkinter {tkinter.Tcl().eval('info patchlevel')}")
    print(f"torch {torch.__version__}")
    if torch.cuda.is_available():
        print(f"  cuda is available")
    # print(f"tensorflow {tensorflow.__version__}")
    # print(f"skimage {skimage.__version__}")


if __name__ == "__main__":
    main()
