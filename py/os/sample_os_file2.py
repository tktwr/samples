#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:os_file2*

import tt_util as ut


OUTPUT_DIR = '_output2'


def f_all():
    ut.sh_mkdir(OUTPUT_DIR)
    ut.sh_chdir(OUTPUT_DIR)
    ut.sh_mkdir('_test dir')
    ut.sh_touch('_test 1.txt')
    ut.sh_cp('_test 1.txt', '_test 1 cp.txt')
    ut.sh_ls()
    files = ut.sh_glob('*.txt')
    for i in files:
        print(i)


f_all()
