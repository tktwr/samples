#!/bin/bash

source common.sh

fname="/a/b/c/d.txt"

echo "dirname: " `f_get_dirname $fname`
echo "fname: " `f_get_fname $fname`
echo "name: " `f_get_name $fname`
echo "ext: " `f_get_ext $fname`
echo "snapfname: " `f_get_snapfname $fname`
echo "git_snapfname: " `f_get_git_snapfname $fname`
