#!/usr/bin/env python
# -*- coding: utf-8 -*-

from importlib.metadata import version


lst_pkg = [
    'numpy',
    'opencv-python',
    'pillow',
    'torch',
]

for i in lst_pkg:
    try:
        print(f'{i:20s}: {version(i)}')
    except Exception as e:
        print(f'{i:20s}: Exception: {e}')

