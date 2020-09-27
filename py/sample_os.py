#!/usr/bin/env python
# -*- coding: utf-8 -*-
# *memo_py.os*

import sys
import os.path
import glob
import shutil
from datetime import datetime as dt
from common import f_title


def f_today():
    f_title("f_today()")
    today = dt.today()
    print(today)


def f_glob():
    f_title("f_glob()")
    print(f"glob={glob.glob('./*')}")


def f_chdir(dirname):
    f_title("f_chdir()")
    print(f"os.getcwd(): {os.getcwd()}")
    os.chdir(dirname)
    print(f"os.getcwd(): {os.getcwd()}")


def f_write(fname):
    f_title("f_write()")
    with open(fname, 'w') as f:
        f.write('123\n')
        f.write('456\n')
        f.write('abc\n')
        f.write('xyz\n')


def f_read(fname):
    f_title("f_read()")
    with open(fname, 'r') as f:
        for line in f:
            print(line.strip())


def f_path(fname):
    f_title("f_path()")
    path = "~/Desktop/" + fname
    print(f"path={path}")
    expanduser = os.path.expanduser(path)
    print(f"expanduser={expanduser}")
    abspath = os.path.abspath(expanduser)
    print(f"abspath={abspath}")
    dirname = os.path.dirname(abspath)
    print(f"dirname={dirname}")
    basename = os.path.basename(abspath)
    print(f"basename={basename}")
    #listdir = os.path.listdir(".")
    #print(f"listdir={listdir}")
    print(f"splitext={os.path.splitext(basename)}")
    join = os.path.join("a", "b", "c.txt")
    print(f"join={join}")


def f_test(fname):
    f_title("f_test()")
    if os.path.isfile(fname) == True:
        print("isfile: True")
    else:
        print("isfile: False")

    if os.path.isdir(fname) == True:
        print("isdir: True")
    else:
        print("isdir: False")


def f_shutil(fname):
    f_title("f_shutil()")
    os.makedirs("_test_dir/a/b/c", exist_ok=True)
    if not os.path.exists("_test_dir2"):
        shutil.copytree("_test_dir", "_test_dir2")
    #os.rmdir("_test_dir")
    shutil.rmtree("_test_dir")

    shutil.copy("_test.txt", "_test_cp.txt")
    shutil.move("_test_cp.txt", "_test_mv.txt")
    os.remove("_test.txt")


def main(argv):
    f_today()
    f_glob()
    f_chdir("local")
    f_write("_test.txt")
    f_read("_test.txt")
    f_path("_test.txt")
    f_test("_test.txt")
    f_shutil("_test.txt")


if __name__ == "__main__":
    main(sys.argv)
