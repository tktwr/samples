#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py.subprocess*

import subprocess

dirnames = ['../numpy', '../cv', '../pil']

for dirname in dirnames:
    ret = subprocess.run(['pwd'], cwd=dirname)
    ret = subprocess.run(['ls', '-l'], cwd=dirname, encoding='utf-8', capture_output=True)
    print(f'{ret.stdout}')

ret = subprocess.run(['./hello.py'])
