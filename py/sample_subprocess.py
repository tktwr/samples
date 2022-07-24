#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.subprocess*

import subprocess

dirnames = ['numpy', 'cv', 'pil']

for dirname in dirnames:
    subprocess.run(['pwd'], cwd=dirname)
    ret = subprocess.run(['ls', '-l'],
            cwd=dirname,
            encoding='utf-8',
            capture_output=True)
    print(f'{ret.stdout}')
