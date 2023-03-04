#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *sample:py.os*

import sys
import os
import os.path
import glob
import shutil
from datetime import datetime as dt
import tt_util as ut


OUTPUT_DIR = "_output"
FILE_NAME = "_test.txt"


# *sample:py.os.mkdir*
def f_mkdir():
    shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)


# *sample:py.os.chdir*
def f_chdir():
    print(f"dir = {os.getcwd()}")
    os.chdir(OUTPUT_DIR)
    print(f"dir = {os.getcwd()}")


# *sample:py.os.write*
def f_write():
    with open(FILE_NAME, 'w') as f:
        f.write('123\n')
        f.write('456\n')
        f.write('abc\n')
        f.write('xyz\n')


# *sample:py.os.read*
def f_read():
    with open(FILE_NAME, 'r') as f:
        for line in f:
            print(line.strip())


# *sample:py.os.shutil.dir*
def f_shutil_dir():
    os.makedirs("_test_dir/a/b/c", exist_ok=True)

    if os.path.exists("_test_dir2"):
        shutil.rmtree("_test_dir2")

    shutil.copytree("_test_dir", "_test_dir2")
    shutil.move("_test_dir2", "_test_dir3")
    shutil.rmtree("_test_dir")


# *sample:py.os.shutil.file*
def f_shutil_file():
    shutil.copy("_test.txt", "_test_cp.txt")
    shutil.move("_test_cp.txt", "_test_mv.txt")
    os.remove("_test.txt")
    print(os.listdir('.'))


# *sample:py.os.system*
def f_system():
    os.system('ls -l')  # deprecated


# *sample:py.os.subprocess*
def f_subprocess():
    import subprocess
    result = subprocess.run(('ls', '-l'))


# *sample:py.os.glob*
def f_glob():
    files = glob.glob('*.txt')
    print(f"files = {files}")


# *sample:py.os.path*
def f_path():
    path = "~/Desktop/a.txt"
    print(f"path = {path}")

    expanduser = os.path.expanduser(path)
    print(f"expanduser = {expanduser}")

    abspath = os.path.abspath(expanduser)
    print(f"abspath = {abspath}")

    dirname = os.path.dirname(abspath)
    print(f"dirname = {dirname}")

    basename = os.path.basename(abspath)
    print(f"basename = {basename}")
    print(f"splitext = {os.path.splitext(basename)}")

    join = os.path.join("a", "b", "c.txt")
    print(f"join = {join}")


# *sample:py.os.path.test*
def f_test():
    file = '/etc/hosts'
    dir = '/etc'
    print(f"os.path.isfile({file}): {os.path.isfile(file)}")
    print(f"os.path.isdir({dir})  : {os.path.isdir(dir)}")


# *sample:py.os.environ*
def f_environ():
    dir_name = os.environ['HOME']
    print(f"dir_name: {dir_name}")


# *sample:py.os.today*
def f_today():
    today = dt.today()
    print(f'today = {today}')
    time_stamp = dt.now().strftime("%Y%m%d-%H%M%S")
    print(f'time_stamp = {time_stamp}')


# *sample:py.os.sys*
def f_sys():
    print(sys.argv)

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    for i in sys.path:
        print(i)


# -----------------------------------------------------
def _f_get_all_func_names():
    lst = []
    for i in globals():
        if callable(globals()[i]) and i.startswith('f_'):
            lst.append(i)
    return lst


if __name__ == '__main__':
    if len(sys.argv) == 1:
        func_lst = _f_get_all_func_names()
    else:
        func_lst = sys.argv[1:]
    print(func_lst)

    for func in func_lst:
        ut.print_title(f' [{func}] ', '-' * 55, 'center')
        eval(f'{func}()')
