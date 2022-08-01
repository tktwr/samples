#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tt_path_util as ttp
import pprint


def test_ttp(fname, prefix):
    print('--- test_ttp ---')
    fname_unix = ttp.path_unix(fname, prefix)
    fname_mix  = ttp.path_mixed(fname, prefix)
    fname_win  = ttp.path_windows(fname, prefix)
    print(f'orig : {fname}')
    print(f'unix : {fname_unix}')
    print(f'mix  : {fname_mix}')
    print(f'win  : {fname_win}')


pprint.pprint(sys.path)
test_ttp(*['D:/aa\\bb/cc.txt', '/mnt'])
test_ttp(*['/d/aa\\bb/cc.txt', '/mnt'])
test_ttp(*['/mnt/d/aa\\bb/mnt/cc.txt', '/mnt'])
