#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image


def f_title(str):
    print(f"=== [{str}] ===")


class ImageSize():
    def __init__(self, img):
        self.img = img

    def getSize(self, w, h, opt='keep_w'):
        sw, sh = self.img.size
        if opt == 'keep_w':
            return (w, int(w * (sh / sw)))
        elif opt == 'keep_h':
            return (int(h * (sw / sh)), h)


class FileName():
    def __init__(self, orig_path):
        self._orig_path = orig_path
        self._dirname = os.path.dirname(self._orig_path)
        self._filename = os.path.basename(self._orig_path)

    def origname(self):
        return self._orig_path

    def dirname(self):
        return self._dirname

    def filename(self):
        return self._filename

    def name(self):
        name, ext = os.path.splitext(self._filename)
        return name

    def ext(self):
        name, ext = os.path.splitext(self._filename)
        return ext

