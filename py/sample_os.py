#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.os*

import sys
import os
import os.path
import glob
import shutil
from datetime import datetime as dt
import util as ut


OUTPUT_DIR="_output"
FILE_NAME="_test.txt"


# *memo_py.os.today*
def f_today():
    today = dt.today()
    print(today)
    time_stamp = dt.now().strftime("%Y%m%d-%H%M%S")
    print(time_stamp)


# *memo_py.os.glob*
def f_glob():
    print(f"glob.glob('./*'): {glob.glob('./*')}")


# *memo_py.os.chdir*
def f_chdir():
    print(f"os.getcwd(): {os.getcwd()}")
    os.chdir(OUTPUT_DIR)
    print(f"os.getcwd(): {os.getcwd()}")


# *memo_py.os.write*
def f_write():
    with open(FILE_NAME, 'w') as f:
        f.write('123\n')
        f.write('456\n')
        f.write('abc\n')
        f.write('xyz\n')


# *memo_py.os.read*
def f_read():
    with open(FILE_NAME, 'r') as f:
        for line in f:
            print(line.strip())


# *memo_py.os.path*
def f_path():
    path = "~/Desktop/a.txt"
    print(f"path={path}")

    expanduser = os.path.expanduser(path)
    print(f"expanduser={expanduser}")

    abspath = os.path.abspath(expanduser)
    print(f"abspath={abspath}")

    dirname = os.path.dirname(abspath)
    print(f"dirname={dirname}")

    basename = os.path.basename(abspath)
    print(f"basename={basename}")
    print(f"splitext={os.path.splitext(basename)}")

    join = os.path.join("a", "b", "c.txt")
    print(f"join={join}")

    #listdir = os.path.listdir(".")
    #print(f"listdir={listdir}")


# *memo_py.os.test*
def f_test():
    file = '/etc/hosts'
    dir = '/etc'
    print(f"os.path.isfile({file}): {os.path.isfile(file)}")
    print(f"os.path.isdir({dir}): os.path.isdir(dir)")


# *memo_py.os.shutil*
def f_shutil():
    os.makedirs("_test_dir/a/b/c", exist_ok=True)
    if not os.path.exists("_test_dir2"):
        shutil.copytree("_test_dir", "_test_dir2")
    #os.rmdir("_test_dir")
    shutil.rmtree("_test_dir")

    shutil.copy("_test.txt", "_test_cp.txt")
    shutil.move("_test_cp.txt", "_test_mv.txt")
    os.remove("_test.txt")

    dir_name = os.environ['USERPROFILE']
    print(f"dir_name: {dir_name}")
    os.system('ls -l')  # deprecated
    import subprocess
    result = subprocess.run(('ls', '-l'))


# *memo_py.os.sys*
def f_sys():
    print(sys.argv)

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    for i in sys.path:
        print(i)


def main(argv):
    funcs = (
        "f_today",
        "f_glob",
        "f_chdir",
        "f_write",
        "f_read",
        "f_path",
        "f_test",
        "f_shutil",
        "f_sys",
    )

    if len(argv) == 1:
        selected = funcs
    else:
        selected = argv[1:]

    for i in selected:
        ut.f_title(i)
        eval(f"{i}()")


if __name__ == "__main__":
    main(sys.argv)
