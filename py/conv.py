#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PIL import Image
from common import ImageSize
from common import FileName


def f_conv(w, h, dst_ext, files):
    for ifile in files:
        fname = FileName(ifile)
        name = fname.name()
        ofile = f"{name}.{dst_ext}"

        print(f"convert {ifile} {ofile}")

        img = Image.open(ifile)
        img_size = ImageSize(img)
        new_size = img_size.getSize(w, h)
        img_resize = img.resize(new_size)
        img_resize.save(ofile)


def main(argv):
    f_conv(100, 100, "png", argv[1:])


if __name__ == "__main__":
    main(sys.argv)
