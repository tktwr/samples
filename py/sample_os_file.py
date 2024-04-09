#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import shutil
import tt_util as ut


OUTPUT_DIR = '_output'


# *sample:py.os.glob*
def f_glob():
    files = glob.glob('*.py')
    print(f"files = {files}")


# *sample:py.os.mkdir*
def f_mkdir():
    shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)


# *sample:py.os.chdir*
def f_chdir():
    print(f'dir = {os.getcwd()}')
    os.chdir(OUTPUT_DIR)
    print(f'dir = {os.getcwd()}')


# *sample:py.os.shutil.dir*
def f_shutil_dir():
    os.makedirs('_test_dir/a/b/c', exist_ok=True)

    if os.path.exists('_test_dir2'):
        shutil.rmtree('_test_dir2')

    shutil.copytree('_test_dir', '_test_dir2')
    shutil.move('_test_dir2', '_test_dir3')
    shutil.rmtree('_test_dir')


# *sample:py.os.shutil.file*
def f_shutil_file():
    with open('_test.txt', 'w') as f:
        f.write('')
    shutil.copy('_test.txt', '_test_cp.txt')
    shutil.move('_test_cp.txt', '_test_mv.txt')
    os.remove('_test.txt')
    print(os.listdir('.'))


