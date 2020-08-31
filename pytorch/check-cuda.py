#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import torch


def main(argv):
    if torch.cuda.is_available():
        print("cuda is available")


if __name__ == "__main__":
    main(sys.argv)

