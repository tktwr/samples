#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import glob
import shutil

def f_remove(fname):
    if os.path.exists(fname):
        print("file exist")
        os.remove(fname)
        print("file removed")
    else:
        print("file not exist")

def f_write(fname):
    f = open(fname, 'w')
    f.write('123\n')
    f.write('456\n')
    f.write('abc\n')
    f.write('xyz\n')
    f.close()

def f_write2(fname):
    with open(fname, 'w') as f:
        f.write('123\n')
        f.write('456\n')
        f.write('abc\n')
        f.write('xyz\n')

def f_read(fname):
    f = open(fname, 'r')
    for line in f:
        print(line.strip())
    f.close()

def f_path(fname):
    path = "~/Desktop/" + fname
    print("path={0}".format(path))
    expanduser = os.path.expanduser(path)
    print("expanduser={0}".format(expanduser))
    abspath = os.path.abspath(expanduser)
    print("abspath={0}".format(abspath))
    dirname = os.path.dirname(abspath)
    print("dirname={0}".format(dirname))
    basename = os.path.basename(abspath)
    print("basename={0}".format(basename))
    #listdir = os.path.listdir(".")
    #print("listdir={0}".format(listdir))
    print("splitext={0}".format(os.path.splitext(basename)))
    print("glob={0}".format(glob.glob("./*")))
    join = os.path.join("a", "b", "c.txt")
    print("join={0}".format(join))
    os.path.isfile(abspath)
    os.path.isdir(dirname)

def f_sh(fname):
    os.makedirs("a/b/c", exist_ok=True)
    if not os.path.exists("a2"):
        shutil.copytree("a", "a2")
    #os.rmdir("a")
    shutil.rmtree("a")
    shutil.copy("_test.txt", "_test_cp.txt")
    shutil.move("_test_cp.txt", "_test_mv.txt")
    os.remove("_test.txt")

f_write("_test.txt")
f_read("_test.txt")
f_path("_test.txt")

