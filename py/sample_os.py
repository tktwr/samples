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


# *memo_py.os.f_today*
def f_today():
    ut.f_title("f_today()")
    today = dt.today()
    print(today)
    time_stamp = dt.now().strftime("%Y%m%d-%H%M%S")
    print(time_stamp)


# *memo_py.os.f_glob*
def f_glob():
    ut.f_title("f_glob()")
    print(f"glob={glob.glob('./*')}")


# *memo_py.os.f_chdir*
def f_chdir(dirname):
    ut.f_title("f_chdir()")
    print(f"os.getcwd(): {os.getcwd()}")
    os.chdir(dirname)
    print(f"os.getcwd(): {os.getcwd()}")


# *memo_py.os.f_write*
def f_write(fname):
    ut.f_title("f_write()")
    with open(fname, 'w') as f:
        f.write('123\n')
        f.write('456\n')
        f.write('abc\n')
        f.write('xyz\n')


# *memo_py.os.f_read*
def f_read(fname):
    ut.f_title("f_read()")
    with open(fname, 'r') as f:
        for line in f:
            print(line.strip())


# *memo_py.os.f_path*
def f_path(fname):
    ut.f_title("f_path()")
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


# *memo_py.os.f_test*
def f_test(fname):
    ut.f_title("f_test()")
    if os.path.isfile(fname) == True:
        print("isfile: True")
    else:
        print("isfile: False")

    if os.path.isdir(fname) == True:
        print("isdir: True")
    else:
        print("isdir: False")


# *memo_py.os.f_shutil*
def f_shutil(fname):
    ut.f_title("f_shutil()")
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


# *memo_py.os.f_sys*
def f_sys():
    ut.f_title("f_sys()")
    print(sys.argv)

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    for i in sys.path:
        print(i)


def main(argv):
    f_today()
    f_glob()
    f_chdir("_output")
    f_write("_test.txt")
    f_read("_test.txt")
    f_path("_test.txt")
    f_test("_test.txt")
    f_shutil("_test.txt")
    f_sys()


if __name__ == "__main__":
    #main(sys.argv)
    f_path("_test.txt")
