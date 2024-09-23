#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo:sample:py:os_file*

import glob
import tt_util as ut


OUTPUT_DIR = '_output'


def f_sh_glob():
    files = glob.glob('*.py')
    ut.log(f"files = {files}")


def f_sh_rmdir():
    ut.sh_rmdir(OUTPUT_DIR, ignore_errors=True)


def f_sh_mkdir():
    ut.sh_mkdir(OUTPUT_DIR, exist_ok=True)


def f_sh_chdir():
    ut.log(f'dir = {ut.sh_getcwd()}')
    ut.sh_chdir(OUTPUT_DIR)
    ut.log(f'dir = {ut.sh_getcwd()}')


def f_sh_dir():
    ut.sh_mkdir('_test_dir/a/b/c')
    ut.sh_cpdir('_test_dir', '_test_dir2')
    ut.sh_mvdir('_test_dir2', '_test_dir3')


def f_sh_file():
    ut.sh_touch('_test.txt')
    ut.sh_cp('_test.txt', '_test_cp.txt')
    ut.sh_mv('_test_cp.txt', '_test_mv.txt')
    ut.sh_rm('_test.txt')
    ut.sh_ls()


def f_sh_exists():
    print(ut.sh_isdir('_test_dir3'))
    print(ut.sh_isfile('_test_mv.txt'))
    print(ut.sh_exists('_test_mv.txt'))


# -----------------------------------------------------
def run_funcs():
    func_lst = ut.get_all_funcs(globals().keys())
    for func in func_lst:
        ut.log_title(f' [{func}] ')
        eval(f'{func}()')


if __name__ == '__main__':
    run_funcs()
