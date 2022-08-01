#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import tt_path_util as ttp


fname = os.path.expandvars('$HOME/WinHome')
print(f'fname: {fname}')

if os.path.islink(fname):
    print(f'symlink')
    fname = os.path.realpath(fname)

print(f'fname: {fname}')
print(f'fname: {ttp.path_unix(fname)}')
